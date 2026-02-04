#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs, urlparse


YOUTUBE_HOST_SUFFIXES = (
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "youtu.be",
)


@dataclass
class HistoryItem:
    title: str
    url: str
    video_id: str
    is_short: bool
    raw_files: list[str]
    hard_skip: bool
    hard_skip_category: str
    hard_skip_reason: str


def _strip_trailing_punct(s: str) -> str:
    return s.rstrip(").,;:!?]}>\"'")


def extract_youtube_id(url: str) -> tuple[str, bool]:
    """
    Returns (video_id, is_short). Empty id means "not a supported youtube url".
    """
    url = _strip_trailing_punct(url.strip())
    if not url:
        return ("", False)

    try:
        parsed = urlparse(url)
    except Exception:
        return ("", False)

    host = (parsed.netloc or "").lower()
    if not host:
        return ("", False)
    if not any(host == h or host.endswith("." + h) for h in YOUTUBE_HOST_SUFFIXES):
        return ("", False)

    path = parsed.path or ""

    if host.endswith("youtu.be"):
        vid = path.lstrip("/").split("/", 1)[0]
        return (vid, False) if vid else ("", False)

    if path == "/watch":
        qs = parse_qs(parsed.query or "")
        vid = (qs.get("v") or [""])[0]
        return (vid, False) if vid else ("", False)

    m = re.match(r"^/shorts/([A-Za-z0-9_-]{6,})", path)
    if m:
        return (m.group(1), True)

    m = re.match(r"^/live/([A-Za-z0-9_-]{6,})", path)
    if m:
        return (m.group(1), False)

    return ("", False)


MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
URL_RE = re.compile(r"https?://[^\s<>()]+")


def parse_history_markdown(md: str, include_shorts: bool) -> list[HistoryItem]:
    by_id: dict[str, HistoryItem] = {}

    for line in md.splitlines():
        line = line.strip()
        if not line:
            continue

        # Prefer explicit Markdown links because they include a title.
        for m in MD_LINK_RE.finditer(line):
            title = (m.group(1) or "").strip()
            url = (m.group(2) or "").strip()
            vid, is_short = extract_youtube_id(url)
            if not vid:
                continue
            if is_short and not include_shorts:
                continue
            existing = by_id.get(vid)
            if existing is None:
                by_id[vid] = HistoryItem(
                    title=title,
                    url=normalize_youtube_url(url, vid, is_short),
                    video_id=vid,
                    is_short=is_short,
                    raw_files=[],
                    hard_skip=False,
                    hard_skip_category="",
                    hard_skip_reason="",
                )
            elif (not existing.title) and title:
                existing.title = title

        # Also accept plain URLs (with no titles).
        for url in URL_RE.findall(line):
            vid, is_short = extract_youtube_id(url)
            if not vid:
                continue
            if is_short and not include_shorts:
                continue
            if vid not in by_id:
                by_id[vid] = HistoryItem(
                    title="",
                    url=normalize_youtube_url(url, vid, is_short),
                    video_id=vid,
                    is_short=is_short,
                    raw_files=[],
                    hard_skip=False,
                    hard_skip_category="",
                    hard_skip_reason="",
                )

    return list(by_id.values())


def normalize_youtube_url(original_url: str, video_id: str, is_short: bool) -> str:
    if is_short:
        return f"https://www.youtube.com/shorts/{video_id}"
    return f"https://www.youtube.com/watch?v={video_id}"


SOURCE_URL_RE = re.compile(r'^\s*source_url:\s*"?([^"\n]+)"?\s*$')


def iter_raw_markdown_files(raw_dir: Path) -> Iterable[Path]:
    if not raw_dir.exists() or not raw_dir.is_dir():
        return []
    return (p for p in raw_dir.iterdir() if p.is_file() and p.suffix.lower() == ".md")


def index_raw_youtube_ids(raw_dir: Path, max_lines: int) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}

    for path in iter_raw_markdown_files(raw_dir):
        try:
            with path.open("r", encoding="utf-8", errors="replace") as f:
                head_lines = []
                for _ in range(max_lines):
                    ln = f.readline()
                    if not ln:
                        break
                    head_lines.append(ln.rstrip("\n"))
        except OSError:
            continue

        candidate_urls: list[str] = []

        # Prefer front matter `source_url`.
        for ln in head_lines[: max_lines // 2]:
            m = SOURCE_URL_RE.match(ln)
            if m:
                candidate_urls.append(m.group(1).strip())
                break

        # Fallback: any YouTube URLs in the header.
        if not candidate_urls:
            for ln in head_lines:
                candidate_urls.extend(URL_RE.findall(ln))

        for url in candidate_urls:
            vid, _is_short = extract_youtube_id(url)
            if not vid:
                continue
            index.setdefault(vid, []).append(str(path))
            break

    return index


def _lower_tokens(s: str) -> set[str]:
    return set(re.findall(r"[a-z0-9][a-z0-9_-]+", s.lower()))


def load_filters_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def apply_hard_skip_filters(items: list[HistoryItem], filters: dict) -> None:
    keep_keywords = [str(k).lower() for k in (filters.get("keep_keywords") or []) if str(k).strip()]
    categories = filters.get("categories") or {}

    for it in items:
        title = (it.title or "").strip()
        if not title:
            continue

        title_lower = title.lower()
        has_keep_keyword = bool(keep_keywords) and any(k in title_lower for k in keep_keywords)

        for category, rule in categories.items():
            keywords = [str(k).lower() for k in (rule.get("keywords") or []) if str(k).strip()]
            if not keywords:
                continue
            allow_keep_override = bool(rule.get("allow_keep_override", True))
            if has_keep_keyword and allow_keep_override:
                continue
            if any(k in title_lower for k in keywords):
                it.hard_skip = True
                it.hard_skip_category = str(category)
                it.hard_skip_reason = f"matched keyword for category '{category}'"
                break


def to_markdown(items: list[HistoryItem]) -> str:
    total = len(items)
    hard_skipped = sum(1 for it in items if it.hard_skip)
    kept = [it for it in items if not it.hard_skip]

    captured = sum(1 for it in kept if it.raw_files)
    uncaptured = len(kept) - captured

    lines: list[str] = []
    lines.append("## Parsed YouTube history")
    lines.append(f"- Unique videos: {total}")
    lines.append(f"- Hard-skipped (excluded): {hard_skipped}")
    lines.append(f"- Considered after skip: {len(kept)}")
    lines.append(f"- Already captured in raw/: {captured}")
    lines.append(f"- Not captured: {uncaptured}")
    lines.append("")
    lines.append("## Videos (considered)")
    lines.append("| # | Captured | Title | URL | Raw files |")
    lines.append("|---:|:--:|---|---|---|")

    for idx, it in enumerate(kept, start=1):
        captured_mark = "✅" if it.raw_files else "—"
        title = (it.title or "").replace("|", "\\|").strip()
        if not title:
            title = "(no title provided)"
        url = it.url
        raw_files = ", ".join(it.raw_files[:2])
        if len(it.raw_files) > 2:
            raw_files = f"{raw_files} (+{len(it.raw_files) - 2} more)"
        lines.append(f"| {idx} | {captured_mark} | {title} | {url} | {raw_files} |")

    lines.append("")
    lines.append("## Not yet captured (copy/paste)")
    for it in kept:
        if it.raw_files:
            continue
        if it.title:
            lines.append(f"- [{it.title}]({it.url})")
        else:
            lines.append(f"- {it.url}")

    if hard_skipped:
        lines.append("")
        lines.append("## Hard-skipped (excluded)")
        lines.append("| Title | URL | Category |")
        lines.append("|---|---|---|")
        for it in items:
            if not it.hard_skip:
                continue
            title = (it.title or "").replace("|", "\\|").strip() or "(no title provided)"
            lines.append(f"| {title} | {it.url} | {it.hard_skip_category or 'unknown'} |")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Parse pasted Markdown YouTube history; dedupe by video id; check if already captured in raw/."
    )
    parser.add_argument(
        "--raw-dir",
        default="raw",
        help="Path to raw/ directory to scan (default: raw).",
    )
    parser.add_argument(
        "--include-shorts",
        action="store_true",
        help="Include YouTube Shorts URLs (default: ignore).",
    )
    parser.add_argument(
        "--max-raw-head-lines",
        type=int,
        default=80,
        help="How many lines to read from the top of each raw/*.md when indexing (default: 80).",
    )
    parser.add_argument(
        "--hard-skip-config",
        default="",
        help="Path to JSON hard-skip config. Default: skills/youtube-history-markdown-triage/filters.json.",
    )
    parser.add_argument(
        "--no-hard-skip",
        action="store_true",
        help="Disable hard-skip filtering (default: enabled).",
    )
    parser.add_argument(
        "--format",
        choices=["md", "json"],
        default="md",
        help="Output format (default: md).",
    )

    args = parser.parse_args()

    md = sys.stdin.read()
    if not md.strip():
        print("No input received on stdin.", file=sys.stderr)
        return 2

    items = parse_history_markdown(md, include_shorts=args.include_shorts)
    items.sort(key=lambda x: (0 if x.title else 1, x.title.lower(), x.video_id))

    raw_dir = Path(os.path.expanduser(args.raw_dir))
    raw_index = index_raw_youtube_ids(raw_dir, max_lines=args.max_raw_head_lines)

    for it in items:
        it.raw_files = raw_index.get(it.video_id, [])

    if not args.no_hard_skip:
        config_path = args.hard_skip_config.strip()
        if config_path:
            filters_path = Path(os.path.expanduser(config_path))
        else:
            skill_dir = Path(__file__).resolve().parents[1]
            filters_path = skill_dir / "filters.json"
        filters = load_filters_json(filters_path)
        apply_hard_skip_filters(items, filters)

    if args.format == "json":
        payload = [asdict(it) for it in items]
        json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0

    sys.stdout.write(to_markdown(items))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
