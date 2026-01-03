---
title: "Distillation Pipeline (Raw → Distilled → Notes)"
tags: [distillation, workflow, agents]
---

# Distillation Pipeline (Raw → Distilled → Notes)

This is a working design doc for capturing and distilling external sources (web pages, YouTube, tweets, Reddit, etc.) into a repo-friendly workflow aligned to:

- **Capture** → store the original material with minimal transformation
- **Organize** → group and index captured items
- **Distill** → extract the useful parts (summary, ideas, entities, patterns)
- **Express** → publish or incorporate into notes / essays

Reference framework: Tiago Forte’s **CODE** (Capture → Organize → Distill → Express):

- https://fortelabs.com/blog/basboverview/

The guiding principle: **raw is append-only and reproducible**; distilled content is allowed to evolve.
In practice, keep the raw *body* append-only; it’s fine to update raw front matter to reflect processing status and add backlinks (raw is local-only).

## Folder structure

Top-level:

- `raw/` — minimally processed source material (local-only; intentionally not committed)
- `distilled/` — refined files (summaries + structured extraction + backlinks)
- `notes/` — integrated structured knowledge (eventual target)

Git hygiene:

- `raw/` contents are ignored by git (except `raw/README.md` and `raw/.gitkeep`).
- `distilled/` is intended to be committed and (optionally) published.

Suggested growth path (optional later):

- `raw/2026/01/…` and `distilled/2026/01/…` once volume grows
- keep a lightweight index file per month (e.g. `distilled/2026/01/_index.md`)

## File naming convention

Use a name that is:

1) stable, 2) sortable by time, 3) traceable to the original source.

Proposed:

- `YYYYMMDD-HHMMSSZ--<slug>.<ext>`

Examples:

- `20260101-142233Z--openai-agent-standards.md`
- `20260101-142233Z--some-blog-post.html`
- `20260101-142233Z--youtube-transcript-building-agents.md`

Slug rules:

- lowercase, words separated by `-`
- avoid super long slugs; 6–12 words is usually enough

## Front matter (metadata) schema

Every item (raw and distilled) should have minimal front matter so you can:

- trace origin
- know when/how it was captured
- track processing status
- connect raw ↔ distilled ↔ notes

### Raw file front matter

Recommended keys:

- `title` — best-effort extracted title
- `source_url` — canonical URL (or best known)
- `captured_at` — ISO timestamp (UTC), e.g. `2026-01-01T14:22:33Z`
- `capture_type` — `web_page|youtube_transcript|tweet_thread|reddit_thread|screenshot|other`
- `capture_tool` — `curl|browser|ytt|manual|screenshot-tool|other` (best effort)
- `raw_format` — `markdown|html|json|image|other` (what the body is)
- `status` — `captured|distilled|integrated|archived` (flexible; add values as needed)

Optional keys:

- `source_kind` — `article|docs|video|thread|post|repo`
- `author` — best effort
- `published_at` — best effort
- `distilled_refs` — list of Obsidian-style internal links to distilled outputs (backlinks; supports multiple; always a list, even for one; quote `[[...]]` values in YAML)
- `tags` — lightweight labels (`[ai-agent, workflow, …]`)

Example:

```yaml
---
title: "Some Page Title"
source_url: "https://example.com/page"
captured_at: "2026-01-01T14:22:33Z"
capture_type: web_page
capture_tool: curl
raw_format: markdown
status: captured
---
```

### Distilled file front matter

Recommended keys:

- `title`
- `source_url` — primary source URL (optional; `raw_refs` is the source of truth)
- `captured_at` — capture timestamp (optional; see `raw_refs` for full provenance)
- `distilled_at` — when this distilled file was produced
- `raw_refs` — list of Obsidian-style internal links to the raw files (source of truth; supports multiple; always a list, even for one; quote `[[...]]` values in YAML)
- `capture_type`
- `status` — `draft|reviewed|integrated|archived|viewed` (flexible; add values as needed)

Optional keys:

- `tags`
- `confidence_notes` — uncertainty flags (pay attention to hallucination risk)
- `agent` — agent that created this distilled content (e.g., `github-copilot`, `codex`)
- `model` — model used for generation (e.g., `claude-sonnet-4.5`, `gpt-4o`)
- `skills_used` — list of Agent Skills used (e.g., `[make-distilled, extract-concepts]`)

Example:

```yaml
---
title: "Some Page Title (Distilled)"
source_url: "https://example.com/page"
captured_at: "2026-01-01T14:22:33Z"
distilled_at: "2026-01-01T14:30:00Z"
raw_refs:
  - "[[raw/20260101-142233Z--some-page-title]]"
capture_type: web_page
status: draft
agent: github-copilot
model: claude-sonnet-4.5
---
```

## Raw content formats: what to store

Keep it simple:

- **Default bias:** store **extracted text / Markdown** because a human will read it.
- **Web pages:** store extracted Markdown as the primary raw artifact; optionally keep HTML alongside it for traceability (raw is local-only).
- **YouTube:** store transcript as Markdown and keep the video URL in front matter.
- **Tweets/threads:** store rendered text (`.md`) plus per-tweet permalinks if you have them.
- **Reddit threads:** store rendered thread text (`.md`) plus the canonical thread URL.
- **Screenshots:** store image files (`.png`, `.jpg`, etc.) with descriptive front matter; AI can re-visualize diagrams during distillation.
Avoid trying to “clean” raw on day 1. Treat “cleanup” as derived work.

## Distilled content template

A suggested structure for `distilled/…/*.md`:

- short summary (5–10 lines)
- “key points” bullets
- extracted:
  - principles
  - patterns
  - entities
  - follow-ups / open questions
- “quotes” section (verbatim snippets with minimal context)
- "next steps" — agent-suggested actions (e.g., integrate into specific notes, follow-up research)
- links:
  - `source_url`
  - `raw_refs`

Keep provenance in front matter (`raw_refs`) and avoid repeating a `raw:` link in the body.

Template:

```md
---
title: "…"
source_url: "…"
captured_at: "…"
distilled_at: "…"
raw_refs:
  - "[[raw/…]]"
capture_type: web_page
---

## Summary

## Key points

## Concepts / principles

## Entities

## Quotes

## Next steps

## Links
- source: …
- <other relevant external links, if any>
```

## Agent skills (capabilities) to implement

This section translates the workflow into “skills” an AI agent can perform.

In this repo, “skills” should follow the **Agent Skills** packaging model (a discoverable folder with a required `SKILL.md` plus optional resources). See:

- `notes/agent-skills.md`

Design goals:

- each skill is **narrow and testable**
- each skill produces deterministic outputs (file path + metadata)
- avoid overloading “capture” with “summarize”
- progressive disclosure: discover by `name` + `description`, then load full `SKILL.md`

### Proposed skill package layout

Illustrative (not yet created):

```
skills/
  get-web-page-raw/
    SKILL.md
    scripts/
  get-youtube-transcript-raw/
    SKILL.md
  get-tweet-thread-raw/
    SKILL.md
  get-reddit-thread-raw/
    SKILL.md
  get-screenshot-raw/
    SKILL.md
  make-distilled/
    SKILL.md
    assets/
  search-web/
    SKILL.md
  search-youtube/
    SKILL.md
  search-twitter/
    SKILL.md
  search-reddit/
    SKILL.md
```

Note: some skills may be “instructions only” and rely on an existing utility (e.g., `ytt`), so they won’t need scripts.

### Skill 1: get web page (raw)

**Name:** `get-web-page-raw`

**Input:**

- `url: string`
- optional `title_hint: string`

**Output:**

- writes one file into `raw/`
- returns `{ raw_path, title, canonical_url, captured_at }`

**Implementation options:**

- minimal: fetch content and store as extracted text/Markdown
- better: extract canonical URL from HTML (`<link rel="canonical">`) when possible
- optional: also store HTML alongside extracted text for traceability

**Failure modes to handle:**

- 403 / bot blocks
- redirects
- huge pages / binary downloads

### Skill 2: get YouTube transcript (raw)

**Name:** `get-youtube-transcript-raw`

**Input:**

- `url: string` (or `video_id`)

**Output:**

- writes transcript into `raw/` as Markdown
- stores the original URL + capture timestamp in front matter

**Implementation options:**

- use your existing `YTT` utility (skill can be instructions-only)
- keep transcript as-is; do not summarize here

### Skill 3: get tweet/thread (raw)

**Name:** `get-tweet-thread-raw`

**Input:**

- `url: string`

**Output:**

- writes a `.md` into `raw/` containing:
  - best-effort thread text
  - per-tweet links if available

**Implementation options:**

- browser automation (because scraping is often blocked)
- store a “capture note” if content is gated (what failed, what to retry)

### Skill 4: get Reddit thread (raw)

**Name:** `get-reddit-thread-raw`

**Input:**

- `url: string`

**Output:**

- writes a `.md` into `raw/` containing best-effort thread text

**Implementation options:**

- simple HTML fetch + text extraction for public threads
- browser automation if content is gated or requires login

### Skill 5: get screenshot (raw)

**Name:** `get-screenshot-raw`

**Input:**

- `source_url: string` (or `description: string` if manual)
- optional `context: string` (what the screenshot shows)

**Output:**

- writes an image file into `raw/` (e.g. `.png`)
- writes a small markdown file with front matter linking to the image

**Implementation options:**

- manual capture (OS screenshot tool) with agent-assisted metadata entry
- automated browser screenshot for web content
- clipboard monitoring for quick capture

**Notes:**

- Store original resolution; AI re-visualization happens during distillation
- Front matter should describe what the diagram/screenshot represents

### Skill 6: make distilled content

**Name:** `make-distilled`

**Input:**

- `raw_path: string`

**Output:**

- writes a distilled file into `distilled/` with:
  - summary
  - extracted structured items
  - backlinks to `raw_refs` + `source_url`

**Notes:**

- Use the raw file as the only context.
- Be explicit about uncertainty; avoid inventing author/published_at if it’s not in the raw.- For screenshots/diagrams: consider AI re-visualization (generate new diagrams inspired by the original).
### Skill 6: search sources (optional; supports automation)

Instead of one generic search skill, assume **vertical searches** so constraints and tools match the source:

- `search-web`
- `search-youtube`
- `search-twitter`
- `search-reddit`

**Intent:** periodically find candidate URLs to capture (e.g., “agent standards in the last week”), returning a shortlist for capture.

**Notes:**

- This can be run manually (operator asks for it) or as a scheduled/irregular agent job.
- Keep it conservative: it should propose candidates, not silently ingest everything.

### Skill 7: organize (optional, later)

**Name:** `organize_captures_by_month`

**Input:**

- none (or a date range)

**Output:**

- moves files into `YYYY/MM/` folders OR generates monthly `_index.md` files

Recommendation: start without this until volume forces it.

## Manual vs scheduled execution

Two modes are worth supporting explicitly:

- **Manual (interactive):** a human asks an IDE/CLI agent to perform a capture or distillation and reviews outputs.
- **Scheduled/irregular (automated):** an agent runs periodically with a limited skill set to keep the pipeline “warm” (e.g., search for candidates, capture a small number of raws, or prepare drafts).

For the automated mode, constrain risk:

- limit volume (e.g., a small weekly quota)
- keep all raw local-only
- require human review before distillation is promoted into `distilled/` (if desired)

## Current decisions and constraints

- **Raw format:** mostly extracted text / Markdown (optimized for human reading)
- **Slugs:** automatic (rely on metadata + URL for matching)
- **Distilled files per raw:** allow multiple (e.g., summary vs concept extraction) to stay flexible
- **Schema:** unified schema with optional per-source fields

## Next steps

Pick one “vertical slice” and implement it end-to-end as **Agent Skills packages**:

1) `skills/get-web-page-raw/SKILL.md` (and optional `scripts/`) that produces a Markdown raw file
2) `skills/make-distilled/SKILL.md` (and optional templates/assets) that produces distilled content in `distilled/`

Once that feels good, add `skills/get-youtube-transcript-raw/` (likely instructions-only, delegating to `ytt`).
