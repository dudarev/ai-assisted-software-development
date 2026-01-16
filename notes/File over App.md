---
title: File over App
created: 2026-01-16
tags:
  - publish
  - local-first
  - data-ownership
  - software-design
  - pkm
summary: A philosophy prioritizing data (the file) over the tools used to create it (the app), ensuring longevity, portability, and high-bandwidth access for AI agents.
distilled_refs:
  - "[[distilled/20260114-233350Z--local-context-renaissance-dannypostma.md]]"
---

# File over App

**File over App** is a design and data-management philosophy that prioritizes the permanence and accessibility of data by storing it in universal, open formats (like Markdown) on the local file system, rather than within the proprietary silos of SaaS applications.

As Steph Ango (Kepano), CEO of Obsidian, articulates: "If you can’t open your data in another app, you don’t own it."

## Why It Matters in the AI Era

While the philosophy originally focused on data sovereignty and longevity, it has seen a massive resurgence due to the rise of agentic AI.

### The Context Bottleneck
AI agents perform significantly better when they have direct, high-bandwidth access to a local file system. 
- **Bandwidth**: Agents can use local tools like `grep`, `find`, and `fd` to scan thousands of files in milliseconds.
- **Coordination**: When project specs, documentation, and code all live in a single local repository, agents can coordinate across domains without manual context engineering.
- **Reliability**: Cloud APIs (Notion, Google Docs) introduce latency, rate limits, and authentication hurdles that throttle an agent's "thinking" speed.

## Core Principles

1.  **Format Independence**: Use open, human-readable formats (primarily Markdown, but also JSON, YAML, etc.).
2.  **Local First**: The primary source of truth is your local drive. Cloud is for backup/sync, not the primary interaction layer.
3.  **Tool Agnosticism**: You should be able to switch between Obsidian, VS Code, and terminal agents (Aider, Claude Code) without data migration.
4.  **Longevity**: Files should remain readable and useful decades after the application used to create them has disappeared.

## Patterns and Workflows

- **The Spec Folder Pattern**: Keeping a dedicated `/specs` folder in local Markdown within the codebase. This allows agents to "orchestrate" environments by reading the high-level roadmap directly.
- **SaaS unbundling**: Moving knowledge from Notion or Google Docs back into Markdown repositories to give agents "repo-wide" context.
- **Local RAG (No Vector Store)**: Leveraging the large context windows of modern models. Instead of complex vector databases, agents simply browse and read relevant local files.

## Related Notes
- [[Disposable Software]] - Why local files are the best home for ephemeral utilities.
- [[Spec-Driven Development]] - Specs as the primary file-based source of truth.
- [[Agentic Coding]] - High-bandwidth context as the "fuel" for agents.
- [[Rebuild Threshold]] - Using local history to inform regeneration.

## References
- Steph Ango (Kepano), ["File over App"](https://stephango.com/file-over-app)
- Danny Postma, ["The Renaissance of Local Context"](https://x.com/dannypostma/status/2011065092843139291) (2026) — On how coding agents are driving the return to local file-system context.
