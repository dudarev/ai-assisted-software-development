#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


# Avoid treating emails like "name@gmail.com" as X handles.
HANDLE_RE = re.compile(r"(?<![A-Za-z0-9_])@([A-Za-z0-9_]{1,15})\b")
TITLE_AUTHOR_RE = re.compile(r"Thread by @([A-Za-z0-9_]{1,15})\b")


@dataclass(frozen=True)
class ThreadDoc:
    path: Path
    title: str | None
    source_url: str | None
    created: str | None
    published: str | None
    author_handle: str | None  # with leading "@"
    segments: list[list[str]]  # each segment is a list of lines


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and ((value[0] == value[-1] == '"') or (value[0] == value[-1] == "'")):
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text

    fm_lines: list[str] = []
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
        fm_lines.append(lines[i])

    if end_idx is None:
        return {}, text

    data = parse_frontmatter_lines(fm_lines)

    body = "\n".join(lines[end_idx + 1 :]).lstrip("\n")
    return data, body


def parse_frontmatter_lines(fm_lines: list[str]) -> dict[str, object]:
    data: dict[str, object] = {}
    i = 0
    while i < len(fm_lines):
        raw = fm_lines[i].rstrip("\n")
        if not raw.strip() or raw.lstrip().startswith("#"):
            i += 1
            continue

        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", raw)
        if not m:
            i += 1
            continue

        key = m.group(1)
        value = m.group(2).rstrip()

        if value == "":
            # Possibly a YAML list:
            items: list[str] = []
            j = i + 1
            while j < len(fm_lines):
                nxt = fm_lines[j]
                m_item = re.match(r"^\s*-\s*(.*)$", nxt)
                if not m_item:
                    break
                items.append(_strip_quotes(m_item.group(1).strip()))
                j += 1
            if items:
                data[key] = items
                i = j
                continue
            data[key] = ""
            i += 1
            continue

        data[key] = _strip_quotes(value)
        i += 1

    return data


def parse_loose_frontmatter(text: str) -> tuple[dict[str, object], str]:
    """
    Some raw captures start with YAML-ish metadata but omit the leading '---'.
    Treat everything up to the first '---' separator as frontmatter if it looks
    like key/value lines.
    """
    lines = text.splitlines()
    fm_lines: list[str] = []
    end_idx = None

    for i, line in enumerate(lines):
        if line.strip() == "---":
            end_idx = i
            break
        if re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line) or re.match(r"^\s*-\s*(.*)$", line):
            fm_lines.append(line)
            continue
        break

    if end_idx is None or not fm_lines:
        return {}, text

    data = parse_frontmatter_lines(fm_lines)
    body = "\n".join(lines[end_idx + 1 :]).lstrip("\n")
    return data, body


def split_segments(body: str) -> list[list[str]]:
    segments: list[list[str]] = []
    current: list[str] = []
    for line in body.splitlines():
        if line.strip() == "---":
            if current and any(ln.strip() for ln in current):
                segments.append(current)
            current = []
            continue
        current.append(line)

    if current and any(ln.strip() for ln in current):
        segments.append(current)
    return segments


def normalize_text_for_handles(text: str) -> str:
    # Raw captures escape underscores as "\_" in handles.
    return text.replace("\\_", "_")


def canonicalize_handle(handle: str) -> str:
    handle = handle.strip()
    if handle.startswith("@"):
        handle = handle[1:]
    return f"@{handle.lower()}"


def extract_first_handle(line: str) -> str | None:
    line = normalize_text_for_handles(line)
    m = HANDLE_RE.search(line)
    if not m:
        return None
    return canonicalize_handle(m.group(1))


def extract_mentioned_handles(text: str) -> list[str]:
    text = normalize_text_for_handles(text)
    return [canonicalize_handle(m.group(1)) for m in HANDLE_RE.finditer(text)]


def parse_thread_doc(path: Path) -> ThreadDoc | None:
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if not fm:
        fm, body = parse_loose_frontmatter(text)

    title = fm.get("title") if isinstance(fm.get("title"), str) else None
    source_url = None
    for key in ("source_url", "source"):
        v = fm.get(key)
        if isinstance(v, str) and ("x.com/" in v or "twitter.com/" in v):
            source_url = v.strip()
            break

    if not source_url:
        # Fallback: take the first x.com/twitter.com link in the file.
        m = re.search(r"https?://(?:x\.com|twitter\.com)/\S+", text)
        if m:
            source_url = m.group(0).rstrip(").,]\"'")

    if not source_url:
        return None

    created = fm.get("created") if isinstance(fm.get("created"), str) else None
    published = fm.get("published") if isinstance(fm.get("published"), str) else None

    author_handle: str | None = None
    authors = fm.get("author")
    if isinstance(authors, list):
        for item in authors:
            if not isinstance(item, str):
                continue
            m = re.search(r"@([A-Za-z0-9_]{1,15})\b", item)
            if m:
                author_handle = canonicalize_handle(m.group(1))
                break

    if not author_handle and title:
        m = TITLE_AUTHOR_RE.search(title)
        if m:
            author_handle = canonicalize_handle(m.group(1))

    segments = split_segments(body)
    if not author_handle and segments:
        author_handle = extract_first_handle(segments[0][0]) if segments[0] else None

    return ThreadDoc(
        path=path,
        title=title,
        source_url=source_url,
        created=created,
        published=published,
        author_handle=author_handle,
        segments=segments,
    )


def iter_thread_docs(raw_dir: Path) -> Iterable[ThreadDoc]:
    for path in sorted(raw_dir.glob("*.md")):
        doc = parse_thread_doc(path)
        if doc:
            yield doc


def utc_timestamp_for_filename(now: dt.datetime) -> str:
    if now.tzinfo is None:
        now = now.replace(tzinfo=dt.timezone.utc)
    else:
        now = now.astimezone(dt.timezone.utc)
    return now.strftime("%Y%m%d-%H%M%SZ")


def utc_timestamp_iso(now: dt.datetime) -> str:
    if now.tzinfo is None:
        now = now.replace(tzinfo=dt.timezone.utc)
    else:
        now = now.astimezone(dt.timezone.utc)
    return now.isoformat().replace("+00:00", "Z")


def thread_display_title(doc: ThreadDoc) -> str:
    if doc.title:
        return doc.title
    return doc.path.stem


def handle_to_x_url(handle: str) -> str:
    handle = canonicalize_handle(handle)
    return f"https://x.com/{handle[1:]}"


def render_handle_link(handle: str) -> str:
    handle = canonicalize_handle(handle)
    return f"[{handle}]({handle_to_x_url(handle)})"


def render_report(
    docs: list[ThreadDoc],
    now: dt.datetime,
    top_n_mentions: int,
    top_n_commenters: int,
) -> str:
    threads_lines: list[str] = []
    mention_counts: dict[str, int] = {}
    mention_threads: dict[str, set[str]] = {}
    commenter_counts: dict[str, int] = {}
    commenter_threads: dict[str, set[str]] = {}

    for doc in docs:
        thread_key = str(doc.path)
        title = thread_display_title(doc)
        author = render_handle_link(doc.author_handle) if doc.author_handle else "(@unknown)"
        date = doc.published or doc.created or ""
        date_str = f" — {date}" if date else ""
        threads_lines.append(f"- [[{doc.path.as_posix()}]] — {author}{date_str} — {doc.source_url}")

        for seg in doc.segments:
            header_idx = next((i for i, ln in enumerate(seg) if ln.strip()), None)
            if header_idx is None:
                continue
            author_line = seg[header_idx]
            seg_author = extract_first_handle(author_line)

            body_text = "\n".join(seg[header_idx + 1 :]) if header_idx + 1 < len(seg) else ""
            for handle in extract_mentioned_handles(body_text):
                mention_counts[handle] = mention_counts.get(handle, 0) + 1
                mention_threads.setdefault(handle, set()).add(thread_key)

            if seg_author and doc.author_handle and seg_author != doc.author_handle:
                commenter_counts[seg_author] = commenter_counts.get(seg_author, 0) + 1
                commenter_threads.setdefault(seg_author, set()).add(thread_key)

    mention_ranked = sorted(
        mention_counts.items(),
        key=lambda kv: (-kv[1], kv[0].lower()),
    )[:top_n_mentions]

    commenter_ranked = sorted(
        commenter_counts.items(),
        key=lambda kv: (-kv[1], kv[0].lower()),
    )[:top_n_commenters]

    lines: list[str] = []
    lines.append("---")
    lines.append('title: "People in captured X/Twitter threads"')
    lines.append(f'distilled_at: "{utc_timestamp_iso(now)}"')
    lines.append("capture_type: analysis")
    lines.append("status: draft")
    lines.append("agent: codex")
    lines.append("model: gpt-5.2")
    lines.append("scope:")
    lines.append("  - raw/")
    lines.append('tags: ["twitter-threads", "community-graph"]')
    lines.append("---")
    lines.append("")
    lines.append("## Threads captured")
    lines.extend(threads_lines or ["- (none found)"])
    lines.append("")
    lines.append("## People mentioned in thread text (top)")
    if mention_ranked:
        for handle, count in mention_ranked:
            tcount = len(mention_threads.get(handle, set()))
            lines.append(f"- {render_handle_link(handle)} — {count} mentions ({tcount} threads)")
    else:
        lines.append("- (none found)")
    lines.append("")
    lines.append("## Frequent commenters (top)")
    if commenter_ranked:
        for handle, count in commenter_ranked:
            tcount = len(commenter_threads.get(handle, set()))
            lines.append(f"- {render_handle_link(handle)} — {count} replies captured ({tcount} threads)")
    else:
        lines.append("- (none found)")
    lines.append("")
    lines.append("## Notes / caveats")
    lines.append("- Counts come from local `raw/` captures only (no API calls).")
    lines.append("- \"Mentions\" are `@handle` tokens in the body text (not including the header author line).")
    lines.append("- \"Commenters\" exclude the thread author for each thread.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analyze raw X/Twitter thread captures for mentioned people and frequent commenters."
    )
    parser.add_argument("--raw-dir", default="raw", help="Directory with raw captures (default: raw)")
    parser.add_argument("--out-dir", default="distilled", help="Directory for generated report (default: distilled)")
    parser.add_argument(
        "--top-mentions",
        type=int,
        default=80,
        help="Number of mentioned handles to include (default: 80)",
    )
    parser.add_argument(
        "--top-commenters",
        type=int,
        default=80,
        help="Number of commenter handles to include (default: 80)",
    )
    parser.add_argument(
        "--output",
        default="",
        help="Optional output path. If omitted, writes to distilled/<timestamp>--x-thread-people.md",
    )
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    out_dir = Path(args.out_dir)
    if not raw_dir.exists():
        raise SystemExit(f"raw dir not found: {raw_dir}")
    out_dir.mkdir(parents=True, exist_ok=True)

    docs = list(iter_thread_docs(raw_dir))
    now = dt.datetime.now(dt.timezone.utc)
    report = render_report(
        docs=docs,
        now=now,
        top_n_mentions=args.top_mentions,
        top_n_commenters=args.top_commenters,
    )

    if args.output:
        out_path = Path(args.output)
    else:
        stamp = utc_timestamp_for_filename(now)
        out_path = out_dir / f"{stamp}--x-thread-people.md"

    out_path.write_text(report, encoding="utf-8")
    rel = os.path.relpath(out_path, Path.cwd())
    print(rel)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
