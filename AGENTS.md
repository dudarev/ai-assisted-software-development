# Agents Guide

This document explains how AI agents (human-operated or autonomous) should work with this repository.

## Purpose

Agents are used to:
- assist with research and synthesis
- draft and refine documents
- extract patterns from talks, papers, and practice
- challenge assumptions and highlight gaps

Agents are **assistive**, not authoritative.

## Core principles for agents

1. **Prefer clarity over verbosity**  
   Short, precise explanations are preferred to exhaustive ones.

2. **Preserve intent**  
   Do not “improve” tone, structure, or scope unless explicitly asked.

3. **Think in systems and patterns**  
   Favor principles, trade-offs, and reusable ideas over tool-specific advice.

4. **Show uncertainty explicitly**  
   If something is speculative, early, or unclear — say so.

5. **Avoid hype**  
   No marketing language, no inflated claims, no trend-chasing.

## How agents should contribute

When creating or modifying content:
- Keep changes small and reviewable
- Explain *why* a change is suggested
- Prefer incremental evolution over rewrites
- Respect existing terminology and structure
- Avoid exposing private information (private repository names, local file paths, personal data)
- Link to public resources when referencing external concepts or workflows

### Distillations: raw → distilled references

When you create a new `distilled/…` note from a `raw/…` note, reference the distilled note from the raw note’s front matter (instead of a body section), e.g.:

```yaml
distilled_refs:
  - "[[distilled/<new-note>.md]]"
```

When adding new material:
- Start minimal
- Leave room for future refinement
- Link concepts instead of duplicating them

When working with notes (in `notes/` directory):
- Keep notes self-contained and publishable
- Do not reference or link to `distilled/` or `raw/` content from the **body** of the notes.
- Use the original sources (articles, threads, etc.) if referencing external work, adding your own synthesis and comments.
- **Direction:** Distilled notes (`distilled/`) CAN reference domain notes (`notes/`), but domain notes (`notes/`) SHOULD NOT depend on distilled content. They should stand alone as domain knowledge.
- However, linking to `distilled/` notes from the **front matter** (using a property like `distilled_refs` or `source` if applicable) is encouraged to maintain the lineage, but keep the prose clean.
- Nodes must be publishable to the web without the internal `distilled/` folder, which is why the body remains clean of internal links.
- Use the original sources (articles, threads, etc.) if referencing external work, adding your own synthesis and comments.
- Link only to public external resources (articles, papers, podcasts) in the References section
- Notes should be readable and useful without access to the capture/distillation pipeline
- Avoid redundant tags: since the entire repository focuses on AI-assisted software development, do not tag notes with generic terms like "ai-assisted-development"—use specific, descriptive tags instead

## Voice Dictation & Transcription

Prompts are frequently voice-dictated. Agents must:
1. **Account for transcription errors** contextually.
2. **Update this section** with new common mistranscriptions if the user corrects them.

**Common mistranscriptions & terminology:**
- "node" / "note": These are used interchangeably. When the user says "node", they usually mean a permanent "note" in the `notes/` directory.

## Authority model

This repository represents the author’s evolving understanding.

Agents may:
- propose
- question
- refactor
- summarize

Agents may not:
- present opinions as settled facts
- remove nuance for simplicity
- optimize for popularity or SEO

## Long-term goal

The goal is to build a durable, coherent body of knowledge about AI-assisted software development that remains useful even as tools and models change.
