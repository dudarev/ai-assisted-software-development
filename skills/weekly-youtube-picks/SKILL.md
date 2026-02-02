---
name: weekly-youtube-picks
description: Create or update the weekly YouTube picks note in notes/ using the existing template, linking directly to sources and referencing published notes.
---

# Weekly YouTube Picks

## When to use

Use this skill when the user asks to create or update the weekly YouTube picks note (or "weekly picks") based on newly distilled videos or other curated sources.

**Keywords:** weekly picks, weekly YouTube picks, roundup, weekly note

## Inputs

Required:
- `sources` (list): Each source must include `title`, `url`, and a 1-2 sentence takeaway.

Optional:
- `week` (string): ISO week in `YYYY-Www` format. If missing, use the current local week.
- `focus_note` (string): One-sentence theme for the week (used in front matter `note`).
- `published_notes` (list): Relevant note titles to reference (must have the `publish` tag).
- `distilled_refs` (list): Distilled note paths to mine for `source_url` only (do not link to distilled notes).
- `tags` (list): Extra tags for front matter.
- `status` (string): `draft` (default) or `published`.

## Output

- A note in `notes/` named `Weekly YouTube Picks - YYYY-Www.md` using the existing weekly template.

## Procedure

1. **Determine target week**
   - If `week` is provided, use it.
   - Otherwise, use the current local ISO week (`date +%G-W%V`).

2. **Find the most recent weekly picks note**
   - Search `notes/` for a file tagged `weekly`.
   - Use that file as the format template (title, sections, tone).

3. **Assemble source list**
   - If `distilled_refs` are provided, open each distilled note and copy only its `source_url` (and inferred title). Do not link to the distilled note itself.
   - For each source, ensure:
     - A direct, public URL
     - A short, concrete takeaway

4. **Draft the note**
   - Title: `Weekly YouTube Picks (YYYY-Www)`
   - Front matter:
     - `tags` must include `weekly` and `youtube`
     - Include `publish` tag only if `status` is `published`
     - Include `status` field
     - Include `note` with the weekly theme if provided
   - Sections:
     - `## Picks`: bullet list of sources formatted like:
       - `**[Title](URL)** — 1-3 sentence summary with key ideas; link to published notes with `[[Note Title]]` when relevant.
     - `## Related Notes`: list of relevant published notes as wiki links.

5. **Write or update file**
   - If a note for the target week exists, update it.
   - Otherwise, create a new file in `notes/`.

## Guardrails

- Do **not** link to `distilled/` notes in the body.
- Prefer direct source URLs (YouTube, articles).
- Only reference notes that have the `publish` tag.
- Keep summaries tight and concrete; no hype.

