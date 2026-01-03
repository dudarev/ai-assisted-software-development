#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF' >&2
Usage:
  capture_youtube_transcript_raw.sh <youtube_url> [title_hint]
  capture_youtube_transcript_raw.sh --from-file <ytt_output_file> [title_hint]
  capture_youtube_transcript_raw.sh --from-stdin [title_hint]

Writes:
  raw/YYYYMMDD-HHMMSSZ--<slug>.md

Prints:
  The created raw file path.

Notes:
  - Default mode runs: ytt fetch --no-copy "<youtube_url>"
  - If the runtime can’t access the network, use:
      ytt fetch --no-copy "<youtube_url>" | capture_youtube_transcript_raw.sh --from-stdin
EOF
}

if [[ "${1:-}" == "" || "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 2
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "error: missing dependency: python3 (used for slugging/escaping)" >&2
  exit 127
fi

mode="fetch"
youtube_url=""
input_path=""
title_hint=""

if [[ "${1:-}" == "--from-file" ]]; then
  mode="from-file"
  input_path="${2:-}"
  title_hint="${3:-}"
  if [[ "$input_path" == "" ]]; then
    usage
    exit 2
  fi
  if [[ ! -f "$input_path" ]]; then
    echo "error: input file not found: $input_path" >&2
    exit 2
  fi
elif [[ "${1:-}" == "--from-stdin" ]]; then
  mode="from-stdin"
  title_hint="${2:-}"
else
  youtube_url="$1"
  title_hint="${2:-}"
fi

captured_at_iso="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
timestamp_slug="$(date -u +"%Y%m%d-%H%M%SZ")"

mkdir -p raw

tmp_meta="$(mktemp -t ytt-meta.XXXXXX.txt)"
tmp_err="$(mktemp -t ytt-err.XXXXXX.txt)"
trap 'rm -f "$tmp_meta" "$tmp_err"' EXIT

if [[ "$mode" == "from-file" ]]; then
  cat "$input_path" >"$tmp_meta"
elif [[ "$mode" == "from-stdin" ]]; then
  cat >"$tmp_meta"
else
  if ! command -v ytt >/dev/null 2>&1; then
    echo "error: missing dependency: ytt" >&2
    exit 127
  fi

  if ! ytt fetch --no-copy "$youtube_url" >"$tmp_meta" 2>"$tmp_err"; then
    title="${title_hint:-YouTube video}"
    slug="$(python3 - "$title" "$youtube_url" <<'PY'
import re, sys
title = sys.argv[1].strip()
url = sys.argv[2].strip()

def slugify(s: str) -> str:
  s = s.strip().lower()
  s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
  return s

base = slugify(title) if title else ""
if not base and url:
  m = re.search(r"[?&]v=([^&]+)", url)
  if m:
    base = f"youtube-{slugify(m.group(1))}"
  else:
    m = re.search(r"youtu\\.be/([^?&#/]+)", url)
    if m:
      base = f"youtube-{slugify(m.group(1))}"

base = (base or "youtube-video")[:70]
print(base + "--capture-failed")
PY
)"
    out_path="raw/${timestamp_slug}--${slug}.md"
    cat >"$out_path" <<EOF
---
title: "$(printf '%s' "$title" | python3 -c 'import sys, json; print(json.dumps(sys.stdin.read().strip())[1:-1])')"
source_url: "$(printf '%s' "$youtube_url" | python3 -c 'import sys, json; print(json.dumps(sys.stdin.read().strip())[1:-1])')"
captured_at: "$captured_at_iso"
capture_type: youtube_transcript
capture_tool: ytt
raw_format: markdown
status: capture_failed
---

Capture failed while running:

ytt fetch --no-copy "<youtube_url>"

Error output:

	EOF
	    cat "$tmp_err" >>"$out_path" || true
	    cat >>"$out_path" <<EOF

Next step:

- Retry from this repo:
  ./scripts/ytraw "$youtube_url"

- If this environment can’t reach YouTube, run locally and pipe the output:
  ytt fetch --no-copy "$youtube_url" | ./scripts/ytraw
EOF
	    printf '%s\n' "$out_path"
	    echo >&2
	    echo "hint: if this environment can’t reach YouTube, run locally and pipe the output:" >&2
	    echo "  ytt fetch --no-copy \"$youtube_url\" | ./scripts/ytraw" >&2
	    exit 0
  fi
fi

meta_json="$(
  python3 - "$tmp_meta" "$title_hint" <<'PY'
import json, re, sys

path = sys.argv[1]
hint = sys.argv[2].strip()

with open(path, "r", encoding="utf-8", errors="replace") as f:
  lines = []
  for _ in range(200):
    line = f.readline()
    if not line:
      break
    lines.append(line.rstrip("\n"))

url = ""
url_idx = None
for i, line in enumerate(lines):
  if re.match(r"^https?://", line.strip()):
    url_idx = i
    url = line.strip()
    break

title = ""
if url_idx is not None:
  for j in range(url_idx + 1, len(lines)):
    candidate = lines[j].strip()
    if candidate:
      candidate = re.sub(r"^#{1,6}\s+", "", candidate).strip()
      candidate = re.sub(r"^title\s*:\s*", "", candidate, flags=re.IGNORECASE).strip()
      title = candidate
      break

if not title:
  title = hint or "YouTube video"

print(json.dumps({"url": url, "title": title}, ensure_ascii=False))
PY
)"

parsed_url="$(python3 -c 'import json,sys; print(json.loads(sys.argv[1])["url"])' "$meta_json")"
title="$(python3 -c 'import json,sys; print(json.loads(sys.argv[1])["title"])' "$meta_json")"

source_url="$youtube_url"
if [[ -n "$parsed_url" ]]; then
  source_url="$parsed_url"
fi
if [[ "$source_url" == "" ]]; then
  source_url="$youtube_url"
fi

slug="$(python3 - "$title" <<'PY'
import re, sys
t = sys.argv[1].strip().lower()
t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
print((t or "youtube-video")[:80])
PY
)"

out_path="raw/${timestamp_slug}--${slug}.md"

cat >"$out_path" <<EOF
---
title: "$(printf '%s' "$title" | python3 -c 'import sys, json; print(json.dumps(sys.stdin.read().strip())[1:-1])')"
source_url: "$(printf '%s' "$source_url" | python3 -c 'import sys, json; print(json.dumps(sys.stdin.read().strip())[1:-1])')"
captured_at: "$captured_at_iso"
capture_type: youtube_transcript
capture_tool: ytt
raw_format: markdown
status: captured
---

EOF

cat "$tmp_meta" >>"$out_path"
printf '%s\n' "$out_path"
