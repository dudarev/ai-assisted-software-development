#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


RAW_LINK_RE = re.compile(r"\[\[raw/([^\]|]+)")
DISTILLED_LINK_RE = re.compile(r"\[\[distilled/([^\]|]+)")


@dataclass(frozen=True)
class NoteMeta:
    title: str | None = None
    captured_at: str | None = None
    capture_type: str | None = None
    status: str | None = None
    distilled_refs: list[str] | None = None


def _iter_md_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".md"):
                files.append(Path(dirpath) / filename)
    return sorted(files)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _strip_md_ext(s: str) -> str:
    return s[:-3] if s.endswith(".md") else s


def _norm_wikilink_target(prefix: str, target: str) -> str:
    cleaned = target.strip().removeprefix("./")
    cleaned = _strip_md_ext(cleaned)
    if not cleaned.startswith(prefix):
        cleaned = f"{prefix}{cleaned}"
    return cleaned


def _extract_front_matter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


_FM_SIMPLE_KV_RE = re.compile(r"^(?P<k>[A-Za-z0-9_]+):\s*(?P<v>.*)\s*$")


def _parse_front_matter_meta(front_matter: str) -> NoteMeta:
    title: str | None = None
    captured_at: str | None = None
    capture_type: str | None = None
    status: str | None = None
    distilled_refs: list[str] | None = None

    lines = front_matter.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _FM_SIMPLE_KV_RE.match(line)
        if not m:
            i += 1
            continue

        key = m.group("k")
        raw_value = m.group("v").strip()

        if key == "distilled_refs":
            distilled_refs = []
            i += 1
            while i < len(lines) and lines[i].startswith("  - "):
                item = lines[i][len("  - ") :].strip().strip('"').strip("'")
                distilled_refs.append(item)
                i += 1
            continue

        value = raw_value.strip('"').strip("'")
        if key == "title":
            title = value
        elif key == "captured_at":
            captured_at = value
        elif key == "capture_type":
            capture_type = value
        elif key == "status":
            status = value
        i += 1

    return NoteMeta(
        title=title,
        captured_at=captured_at,
        capture_type=capture_type,
        status=status,
        distilled_refs=distilled_refs,
    )


def _extract_wikilink_targets(text: str, regex: re.Pattern[str], prefix: str) -> set[str]:
    targets: set[str] = set()
    for match in regex.finditer(text):
        targets.add(_norm_wikilink_target(prefix, match.group(1)))
    return targets


def _repo_relpath(repo_root: Path, path: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def _build_index(repo_root: Path) -> dict[str, Any]:
    raw_root = repo_root / "raw"
    distilled_root = repo_root / "distilled"

    raw_files = [p for p in _iter_md_files(raw_root) if p.name != "README.md"]
    distilled_files = _iter_md_files(distilled_root)

    raw_notes: dict[str, dict[str, Any]] = {}
    for raw_path in raw_files:
        rel = _repo_relpath(repo_root, raw_path)
        rel_no_ext = _strip_md_ext(rel)
        text = _read_text(raw_path)

        fm = _extract_front_matter(text)
        meta = _parse_front_matter_meta(fm) if fm else NoteMeta()

        raw_notes[rel_no_ext] = {
            "path": rel,
            "link_key": rel_no_ext,
            "meta": {
                "title": meta.title,
                "captured_at": meta.captured_at,
                "capture_type": meta.capture_type,
                "status": meta.status,
                "distilled_refs": meta.distilled_refs,
            },
            "has_distilled_link": bool(DISTILLED_LINK_RE.search(text)),
        }

    distilled_notes: dict[str, dict[str, Any]] = {}
    referenced_raw: set[str] = set()
    for distilled_path in distilled_files:
        rel = _repo_relpath(repo_root, distilled_path)
        rel_no_ext = _strip_md_ext(rel)
        text = _read_text(distilled_path)
        distilled_notes[rel_no_ext] = {"path": rel, "link_key": rel_no_ext}
        referenced_raw |= _extract_wikilink_targets(text, RAW_LINK_RE, prefix="raw/")

    # Validate references in both directions.
    distilled_targets_in_raw: set[str] = set()
    for raw in raw_notes.values():
        if not raw["has_distilled_link"]:
            continue
        raw_text = _read_text(repo_root / raw["path"])
        distilled_targets_in_raw |= _extract_wikilink_targets(
            raw_text, DISTILLED_LINK_RE, prefix="distilled/"
        )

    existing_raw_keys = set(raw_notes.keys())
    existing_distilled_keys = set(distilled_notes.keys())

    missing_distilled_targets = sorted(d for d in distilled_targets_in_raw if d not in existing_distilled_keys)
    missing_raw_targets = sorted(r for r in referenced_raw if r not in existing_raw_keys)

    undistilled_raw: list[dict[str, Any]] = []
    suspicious_raw_marked_distilled: list[dict[str, Any]] = []
    for raw_key, raw in sorted(raw_notes.items()):
        has_outgoing = raw["has_distilled_link"]
        has_incoming = raw_key in referenced_raw
        if has_outgoing or has_incoming:
            continue
        undistilled_raw.append(raw)
        if raw["meta"].get("status") == "distilled":
            suspicious_raw_marked_distilled.append(raw)

    return {
        "counts": {
            "raw_total": len(raw_notes),
            "distilled_total": len(distilled_notes),
            "raw_with_incoming_distilled_ref": sum(1 for k in raw_notes if k in referenced_raw),
            "raw_with_outgoing_distilled_link": sum(1 for r in raw_notes.values() if r["has_distilled_link"]),
            "raw_undistilled": len(undistilled_raw),
            "raw_suspicious_marked_distilled": len(suspicious_raw_marked_distilled),
            "missing_distilled_targets_referenced_from_raw": len(missing_distilled_targets),
            "missing_raw_targets_referenced_from_distilled": len(missing_raw_targets),
        },
        "undistilled_raw": undistilled_raw,
        "suspicious_raw_marked_distilled": suspicious_raw_marked_distilled,
        "missing_distilled_targets_referenced_from_raw": [
            {"distilled_ref": d} for d in missing_distilled_targets
        ],
        "missing_raw_targets_referenced_from_distilled": [{"raw_ref": r} for r in missing_raw_targets],
    }


def _print_text_report(index: dict[str, Any], limit: int) -> None:
    counts = index["counts"]
    print("Raw vs distilled report\n")
    print("Counts:")
    for k in (
        "raw_total",
        "distilled_total",
        "raw_undistilled",
        "missing_distilled_targets_referenced_from_raw",
        "missing_raw_targets_referenced_from_distilled",
    ):
        print(f"- {k}: {counts[k]}")
    print("")

    def _print_section(title: str, items: list[dict[str, Any]], render) -> None:
        if not items:
            return
        print(f"{title}:")
        for item in items[:limit]:
            print(f"- {render(item)}")
        if len(items) > limit:
            print(f"- … and {len(items) - limit} more (use --limit 0 for all)")
        print("")

    undistilled = index["undistilled_raw"]

    def _render_raw(raw: dict[str, Any]) -> str:
        meta = raw.get("meta", {}) or {}
        suffix: list[str] = []
        if meta.get("captured_at"):
            suffix.append(meta["captured_at"])
        if meta.get("capture_type"):
            suffix.append(meta["capture_type"])
        if meta.get("status"):
            suffix.append(f"status={meta['status']}")
        suffix_s = f" ({', '.join(suffix)})" if suffix else ""
        title = meta.get("title")
        title_s = f" — {title}" if title else ""
        return f"{raw['path']}{title_s}{suffix_s}"

    _print_section("Undistilled raw (no incoming/outgoing link)", undistilled, _render_raw)

    _print_section(
        "Suspicious raw (status=distilled but no links)",
        index["suspicious_raw_marked_distilled"],
        lambda raw: raw["path"],
    )

    _print_section(
        "Broken distilled links referenced from raw",
        index["missing_distilled_targets_referenced_from_raw"],
        lambda item: f"[[{item['distilled_ref']}]]",
    )

    _print_section(
        "Broken raw links referenced from distilled",
        index["missing_raw_targets_referenced_from_distilled"],
        lambda item: f"[[{item['raw_ref']}]]",
    )


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Find raw notes without corresponding distilled notes (based on wikilinks)."
    )
    parser.add_argument("--repo-root", default=".", help="Repository root (default: .)")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Max items to print per section; 0 prints all (default: 200)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    repo_root = Path(args.repo_root).resolve()
    index = _build_index(repo_root)

    if args.format == "json":
        print(json.dumps(index, indent=2, sort_keys=True))
    else:
        limit = 10**9 if args.limit == 0 else args.limit
        _print_text_report(index, limit=limit)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
