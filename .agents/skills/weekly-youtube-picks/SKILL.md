---
name: weekly-youtube-picks
description: Create or update the weekly YouTube picks note in notes/ — mining distilled notes for insights, sanitizing video titles, writing tight editorial copy, and linking to published notes.
---

# Weekly YouTube Picks

## When to use

Use this skill when the user asks to create, update, or improve the weekly YouTube picks note (or "weekly picks") based on newly distilled videos or other curated sources.

**Keywords:** weekly picks, weekly YouTube picks, roundup, weekly note

## Inputs

Required:
- `sources` (list): Each source must include `title`, `url`, and a reference to its distilled note path (if available).

Optional:
- `week` (string): ISO week in `YYYY-Www` format. If missing, use the current local week.
- `focus_note` (string): One-sentence theme for the week (used in front matter `note`).
- `published_notes` (list): Relevant note titles to reference (must have the `publish` tag).
- `distilled_refs` (list): Distilled note paths to read for insights (see step 3 below).
- `tags` (list): Extra tags for front matter.
- `status` (string): `draft` (default) or `published`.

## Output

- A note in `notes/` named `Weekly YouTube Picks - YYYY-Www.md`.

## Procedure

### 1. Determine target week

- If `week` is provided, use it.
- Otherwise, use the current local ISO week (`date +%G-W%V`).

### 2. Find the most recent weekly picks note

- Search `notes/` for existing `Weekly YouTube Picks - *.md` files.
- Read the most recent one as the style/format template (title, tone, bullet structure, related notes pattern).
- Do **not** copy its content — only use it as a format reference.

### 3. Resolve sources and mine distilled notes

For each video in the source list:
1. If a distilled note exists, **read it in full** to extract:
   - The best 1-3 ideas, patterns, or quotes to surface in the pick
   - The correct `source_url` (use this as the YouTube link, not the distilled path)
   - Notable framing, terminology, or concepts that deserve a wikilink
2. Do **not** link to the distilled note in the body — only link to the external source URL.
3. If no distilled note exists, use whatever summary or takeaway is available.

### 4. Sanitize video titles

YouTube titles are often clickbait and make poor display text for a curated weekly note. Apply these rules before using a title in the bullet:

- **Remove SEO filler**: strip phrases like "Have you heard these exciting AI news?", "You won't believe...", "This changed everything", etc.
- **Prefer author/series identity over episode title**: if a video belongs to a named series (e.g., "AI Updates Weekly") or the author is the signal (e.g., a named podcast), lead with the series name and/or episode date, then attribute the creator in parentheses. Example:
  - ❌ `Have you heard these exciting AI news? - February 16, 2026 AI Updates Weekly`
  - ✓ `AI Updates Weekly — February 16, 2026 (Lev Selector)`
- **Keep the actual title when it is good**: if the title is clear and non-clickbait (e.g., "Why maintaining a codebase is so damn hard"), keep it as-is.
- The display title in the markdown link and the `href` URL are independent — the URL stays unchanged.

### 5. Draft the intro paragraph

Write a 1-2 sentence editorial intro that names the **throughline** or unifying theme of this week's picks. This is not a summary of each item — it is an editorial observation about what the week's content has in common. Examples of good throughlines:
- "This week's picks share a common argument: the shift from vibe-driven AI use toward deliberate engineering discipline."
- "A recurring tension this week: the more capable models get, the more important governance, verification, and small diffs become."

Avoid:
- Generic openers like "Some interesting ideas from the videos this week."
- Listing the videos in the intro.

### 6. Write bullet copy

Each bullet follows this format:
```
*   **[Sanitized Title](URL)** — 1-4 sentences: key insight(s) from the distilled note, written in editorial voice. Link to relevant published notes with `[[Note Title]]` when a concept is well established.
```

Quality bar for bullet copy:
- **Lead with the idea, not the person**: "Skills-in-the-middle reframes..." not "Lev Selector argues that..."
- **Concrete, not abstract**: name the pattern, the technique, the trade-off.
- **One controlling idea per bullet**: if a video has multiple good ideas, pick the most distinctive one and allude to the rest.
- **Inline wikilinks sparingly**: only link to published notes (`[[Note Title]]`) when the concept has a dedicated note and the link adds meaning. Don't invent links.
- **No hype**: no "game-changing", "revolutionary", "must-watch". Short, precise, useful.
- **Voice**: think edited newsletter copy — confident, editorial, slightly opinionated.

Good example:
> *   **[AI Updates Weekly — February 16, 2026 (Lev Selector)](https://www.youtube.com/watch?v=GsHA0eAcmaI)** — "Skills-in-the-middle" reframes app development: move middle-layer logic out of hard-coded decision trees and into auditable Markdown skill files. The catch is governance: skills become a supply-chain problem — enable least-privilege, review what any skill can touch, and anticipate needing a "skills security officer" before long.

Bad example:
> *   **[Have you heard these exciting AI news? - February 16, 2026 AI Updates Weekly](https://www.youtube.com/watch?v=GsHA0eAcmaI)** — "Skills-in-the-middle" is basically: write the reliable path down as a skill file, then review it like code. The catch is governance: least privilege + skill review, or you've built a supply-chain problem.

### 7. Assemble the Related Notes section

- Collect all `[[Note Title]]` wikilinks used inline in the bullets.
- Add any additional published notes that are thematically relevant to the week but weren't naturally embedded in a bullet.
- List them under `## Related Notes` as a bullet list of wikilinks.
- Only include notes that have the `publish` tag in their front matter.

### 8. Implement inline tag comments

The user may leave improvement hints in the draft using XML-style tags:
```
<some comment about what to change/>
```
- Treat these as inline editorial instructions — implement the change they describe, then remove the tag.
- Common patterns:
  - `<improve this line/>` — rewrite the surrounding text to be stronger
  - `<I think the title can be.../>` — apply the title change described

### 9. Assemble front matter

```yaml
---
title: Weekly YouTube Picks (YYYY-Www)
tags:
  - weekly
  - youtube
  - <any thematic tag, e.g. agentic-workflows>
  - publish   # only if status is published
status: draft
note: <one-sentence theme for the week>
---
```

### 10. Write or update file

- Target path: `notes/Weekly YouTube Picks - YYYY-Www.md`
- If the file already exists, update it (don't create a duplicate).
- Structure:
  1. Front matter
  2. `# Weekly YouTube Picks (YYYY-Www)` heading
  3. Intro paragraph (from step 5)
  4. Bullet list of picks (no `## Picks` subheader — bullets follow the intro directly)
  5. `## Related Notes` section

## Guardrails

- Do **not** link to `distilled/` notes in the body — only to external source URLs.
- Only reference `[[Note Title]]` wikilinks for notes with the `publish` tag.
- Keep bullet summaries tight and concrete — no filler, no hype.
- Do not copy-paste from distilled notes verbatim — synthesize and reframe for editorial voice.
- Apply title sanitization to every bullet; do not use raw YouTube titles if they are clickbait.

## Integration with other skills

- **`youtube-history-triage`**: Use this skill first to identify candidate videos from watch history. The triage output is the input to this skill.
- **`make-distilled`**: Run this skill on raw transcripts before running `weekly-youtube-picks`. The distilled notes are the primary source for bullet copy.
- **`raw-undistilled-triage`**: Use this to check whether all videos in the week have been distilled before drafting the picks note.

## Examples

### Minimal invocation (all distilled, current week)

```
Use the weekly-youtube-picks skill.
The distilled notes for this week are in distilled/20260215-*.md.
Theme: guardrailed loops, skills-as-docs, evals as acceptance criteria.
```

### With title sanitization example

| Raw YouTube title | Sanitized display title |
|---|---|
| Have you heard these exciting AI news? - February 16, 2026 AI Updates Weekly | AI Updates Weekly — February 16, 2026 (Lev Selector) |
| 435: How to Actually Use Claude Code to Build Serious Software | 435: How to Actually Use Claude Code to Build Serious Software *(keep as-is)* |
| DIY dev tools: How this engineer created "Flowy" to visualize his plans and accelerate coding | DIY dev tools: How this engineer created "Flowy" *(shorten if too long)* |
