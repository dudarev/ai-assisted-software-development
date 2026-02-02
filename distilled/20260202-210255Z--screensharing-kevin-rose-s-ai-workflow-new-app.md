---
title: "Screensharing Kevin Rose's AI Workflow / New App (Distilled)"
source_url: "https://www.youtube.com/watch?v=QPAy9R9V1rA"
captured_at: "2026-02-02T21:02:01Z"
distilled_at: "2026-02-02T21:02:55Z"
raw_refs:
  - "[[raw/20260202-210201Z--screensharing-kevin-rose-s-ai-workflow-new-app.md]]"
capture_type: youtube_transcript
status: draft
agent: codex
model: gpt-5
skills_used: [make-distillation]
---

## Summary

Kevin Rose walks through “Nylon,” a personal Techmeme-style news engine he vibe-coded to track AI/tech stories. The workflow ingests RSS and social sources into Postgres, enriches each article via multiple tools, chooses a “winner” per field, generates TLDRs and embeddings, clusters stories, and applies an editorial “gravity engine” to rank what matters most for a specific person. The broader lesson is that solo builders can ship ambitious systems quickly, then prune to the few features that actually matter.

## Key points

- Nylon’s pipeline pulls from dozens of RSS and social sources, storing articles with processing statuses in Postgres.
- Article enrichment uses a multi-source “winner” judge: RSS, iFramely (metadata cards), Firecrawl (full text), and Gemini as a grounded fallback.
- TLDRs are generated for embeddings; vector similarity supports meaning-level clustering beyond keywords.
- trigger.dev orchestrates background jobs with retries and observability, keeping solo workflows resilient.
- The “gravity engine” encodes editorial judgment with scoring dimensions like novelty, impact, technical depth, and builder relevance.
- Kevin treats the product as a personal tool; the real skill is cutting 90% of features after exploration.
- He emphasizes small, loyal audiences and “play” projects as viable paths to value and potential businesses.

## Concepts / principles

- **Winner selection by field:** keep best-available representation for summary/metadata/content, not a single source of truth.
- **Embeddings for nuance:** clustering by meaning captures role reversals and subtle differences that keyword search misses.
- **Editorial scoring as code:** ranking systems can encode subjective criteria to reflect a specific user’s priorities.
- **Build broad, then prune:** rapid exploration is useful only if followed by aggressive feature cuts.
- **Personal software:** tools tuned to one person’s taste can still be valuable to a small, devoted audience.

## Entities

- Kevin Rose
- Nylon (personal Techmeme-style news engine)
- Techmeme (comparison point)
- iFramely (link metadata)
- Firecrawl (page crawl / full text)
- Gemini (grounded fallback summary)
- trigger.dev (task orchestration)
- Postgres (data store)
- DIG (context for Kevin’s exploration work)
- IdeaBrowser (example retention mechanic)

## Quotes

- “The future engineer … it’s not going to be what you build as much as what you don’t build.”
- “I built this … can one person assemble a Techmeme-quality feed tailored to AI velocity.”
- “If you have 500 people that really love what you’ve created … we lose this perspective of what success means.”

## Next steps

- Consider a notes/ entry on “Editorial scoring as code” and “winner selection by field” patterns if they recur in other sources.
- If you want a future durable note, identify the most reusable pattern here (e.g., enrichment winner selection or gravity scoring rubric).

## Links

- source: https://www.youtube.com/watch?v=QPAy9R9V1rA
