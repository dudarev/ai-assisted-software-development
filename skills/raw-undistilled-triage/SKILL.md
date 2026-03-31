---
name: raw-undistilled-triage
description: Identify raw notes in this vault that do not have corresponding distilled notes yet (based on wikilinks and front matter), and report broken raw↔distilled references.
---

# Raw undistilled triage

Use this when you want a quick, repeatable inventory of:
- raw notes that have **no** corresponding distilled note yet
- broken `[[raw/...]]` links from `distilled/`
- broken `[[distilled/...]]` links from `raw/`

## Run

From the repo root:
- `python3 skills/raw-undistilled-triage/scripts/find_undistilled_raw.py`

Optional:
- `--limit 0` to print all items
- `--format json` for machine-readable output

## Interpretation

- “Undistilled raw” means the raw file has **no outgoing** `[[distilled/...]]` link and **no incoming** `[[raw/...]]` link from any distilled note.
- If a raw note is already distilled, record lineage in raw front matter:
  - `distilled_refs:`
  - `  - "[[distilled/<note>.md]]"`

