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

When adding new material:
- Start minimal
- Leave room for future refinement
- Link concepts instead of duplicating them

When working with notes (in `notes/` directory):
- Keep notes self-contained and publishable
- Do not include links to `raw/` or `distilled/` files in the note content
- Source references belong in the frontmatter `distilled` property, not in the body
- Link only to public external resources (articles, papers, podcasts) in the References section
- Notes should be readable and useful without access to the capture/distillation pipeline
- Avoid redundant tags: since the entire repository focuses on AI-assisted software development, do not tag notes with generic terms like "ai-assisted-development"—use specific, descriptive tags instead

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