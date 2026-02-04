---
name: youtube-history-markdown-triage
description: Given pasted Markdown of YouTube watch history, triage which videos are worth distilling for this AI-assisted software development vault, check whether they are already captured in raw/, and propose the top priorities.
---

# YouTube History (Markdown) Triage

## When to use

Use this skill when the user asks to analyze their YouTube watch history and they paste Markdown (instead of relying on Chrome/AppleScript extraction).

## Inputs

Required:
- `history_markdown`: user-pasted Markdown containing YouTube URLs (optionally as `[Title](URL)` links)

Optional:
- `priority_count`: how many top picks to recommend (default: 5)
- `include_shorts`: `true|false` (default: `false`)
- `focus`: 1-sentence focus (default: “AI-assisted software development”)

## Outputs

1. A ranked list of candidate videos (top `priority_count`) with short reasons.
2. A “captured vs not captured” check against `raw/` for those candidates.
3. A question asking which videos to capture/distill next.

## Procedure

### 1) Normalize, dedupe, and hard-skip obvious off-topic items

Take the user’s pasted Markdown and run the helper script to:
- extract YouTube video URLs + IDs
- dedupe by video ID
- detect whether each ID is already present in `raw/` (best-effort)
- **hard-skip** obvious off-topic topics (defaults: physics/math, politics, sports/entertainment), configurable via `skills/youtube-history-markdown-triage/filters.json`

Run (paste the user’s Markdown into the heredoc):

```bash
python3 skills/youtube-history-markdown-triage/scripts/check_youtube_history_md.py --raw-dir raw <<'MD'
<PASTE USER MARKDOWN HERE>
MD
```

If the user wants to include shorts, add `--include-shorts`. Otherwise default behavior is to ignore shorts.
If you want to see everything (no filtering), add `--no-hard-skip`.

### 2) Triage for relevance (human judgment)

Using titles + your knowledge of this vault’s focus, classify into:
- `suggest`: clearly relevant to AI-assisted software development
- `maybe`: adjacent / uncertain
- `skip`: unrelated (entertainment, general news without a clear work tie-in, etc.)

Heuristics for `suggest`:
- coding agents, agent workflows, evals, benchmarking pitfalls
- prompting patterns for software work, specs, tests, refactors, reviews
- developer tooling, IDE workflows, CI/testing, code search, architecture
- org/process changes driven by AI (roles, reviews, quality bars) with concrete detail

Avoid over-weighting hypey titles; prefer topics that plausibly add durable, reusable ideas to the vault.

### 3) Propose top priorities (default 5)

Present a ranked top list (default 5) with:
- title (as given)
- URL
- why it’s high leverage for this vault (1–2 sentences)
- whether it’s already captured in `raw/` (from the script output)

### 4) Ask for approval before capturing/distilling

Ask the user which items (by number) to capture and/or distill next.
Do **not** capture or distill without explicit approval.

### 5) Capture approved (raw) items

For each approved URL not already captured in `raw/`:

```bash
./scripts/ytraw "<youtube_url>"
```

If YouTube access is blocked in this environment, ask the user to run `./scripts/ytraw` locally and share the resulting raw file path(s).

### 6) Distill

Use the `make-distilled` skill on newly captured raw file(s), and ensure each raw file has `distilled_refs` in front matter (not in the body).

## Guardrails

- Never capture/distill without user approval.
- If the pasted Markdown is incomplete or ambiguous, say so and ask for a better export.
- Do not include private/sensitive items in any published note.

## Compounding improvement (lightweight)

After you show the triage, ask 1–2 quick questions:
- “Any false hard-skips (something excluded that you’d want to keep)?”
- “Any new hard-skip categories/keywords you want as defaults?”

If the user gives concrete keywords/categories, update `skills/youtube-history-markdown-triage/filters.json` in a small, reviewable diff.
