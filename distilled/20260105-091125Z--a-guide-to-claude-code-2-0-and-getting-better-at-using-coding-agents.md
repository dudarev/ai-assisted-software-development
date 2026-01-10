---
title: A Guide to Claude Code 2.0 and Knowledge Extraction for Coding Agents
source_url: https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/
captured_at: 2026-01-05
distilled_at: 2026-01-06T00:26:00Z
raw_refs:
  - "[[raw/2026-01-05T111125+0200 - A Guide to Claude Code 2.0 and getting better at using coding agents.md]]"
capture_type: clippings
status: draft
agent: antigravity
model: gemini-3-flash
confidence_notes: Author is Sankalp (@sankalp-s). Content is a detailed guide on Claude Code 2.0 and general agent usage strategies.
tags:
  - claude-code
  - coding-agents
  - context-engineering
  - mcp
---

## Summary

A comprehensive guide to utilizing Claude Code 2.0 and Opus 4.5 for software development. The author shares their experience transitioning between OpenAI Codex and Anthropic's ecosystem, highlighting the "redemption arc" of Opus 4.5. The post delves into **Context Engineering** as a critical skill for managing agentic workflows, explains the mechanics of specialized sub-agents (Explore, Plan, etc.), and provides practical advice for both technical and "technically-lite" users. It emphasizes that while AI drastically increases implementation speed, the value of domain knowledge, judgment, and "taste" has become the primary differentiator for professional developers.

## Key points

- **Augmented Development**: Instead of merely "keeping up," focus on upskilling in domain depth and judgment to better steer AI agents.
- **Context Engineering**: The success of an agent depends heavily on how effectively the "attention budget" (context window) is managed to avoid "context rot."
- **Sub-agents as Specialists**: Claude Code uses specialized sub-agents (e.g., Explore for read-only search, Plan for architecture) to handle complex tasks without bloating the main conversation context.
- **Micro-management & Iteration**: High-speed feedback loops allow for "throw-away drafts" where you let the agent fail first to reveal gaps, then refine prompts for a successful second pass.
- **Skills & Plugins**: These provide "knowledge on demand," allowing the model to load specific instructions or tools only when relevant, preserving precious context space.
- **Personality & Collaboration**: Opus 4.5 is praised for its "soul" and collaborative persona, making it a superior pair-programmer despite being slightly behind GPT-5.2 in raw capability.
- **Cross-Model Review**: A powerful pattern is to use Claude for execution (vibe-coding/speed) and GPT-5.2/o-series models for rigorous code review and bug finding.

## Concepts / principles

- **The Map is not the Territory**: Learning the specific mechanics of one tool like Claude Code (the map) translates to navigating the broader landscape of AI development tools (the territory).
- **Context Rot**: Model performance degrades as the context window fills, regardless of task difficulty. Effective context is often significantly smaller than the theoretical maximum (e.g., 200K for Opus 4.5).
- **Attention Budget**: Context tokens are a limited resource. Every tool call and output "guzzles" tokens, necessitating techniques like compaction, handoffs, and clear role definition.
- **Recitation for Attention**: Persistently updating TODOs or plans "recites" objectives into the end of the context, pushing the global plan into the model's recent attention span and preventing goal drift.
- **Knowledge On-Demand (Skills)**: Instead of bloating system prompts with static instructions, load domain-specific expertise only when triggered by task requirements.

## Patterns

- **Handoff Prompt**: When context limits are reached, having the agent summarize the current state and pending tasks to "carry over" to a fresh conversation session.
- **Explore-Summarize-Read**: Using a sub-agent (Explore) to produce summaries first, then having the main model read the most relevant files to ensure full cross-attention and detailed understanding.
- **Throw-away First Draft**: Let the agent attempt a complex feature end-to-end to reveal gaps in your mental model or its understanding, then restart with a perfected prompt informed by that failure.
- **Lifecycle Hooks**: Using hooks (e.g., `Stop`) to trigger secondary actions like playing notification sounds or initiating "Do more" refinement loops.
- **Review with "Total Verbosity"**: Explicitly asking models to "reveal thoughts in detail" or using high-verbosity settings to catch subtle architectural bugs.

## Entities

- **Claude Code 2.0**: Anthropic's CLI agent product.
- **Opus 4.5**: Anthropic's flagship model, noted for its collaborative "personality" and intent detection.
- **OpenAI Codex**: A primary competitor used by the author for benchmarks and code review.
- **MCP (Model Context Protocol)**: A protocol for exposing tools and resources to agents via sandbox environments.
- **Manus & Karpathy**: Referenced for their insights into agent architecture and the future of LLMs as "ghosts in the machine."
- **Armin Ronacher**: Referenced for his deep dive into the implementation of "Plan Mode."

## Quotes

> "You can spend more time on taste refinement... Since implementation is much faster now, you can spend more time on taste refinement."
> 
> — Sankalp

> "Context engineering is about answering 'what configuration of context is most likely to generate our model's desired behavior?'"
> 
> — Anthropic Engineering Blog

> "It's a little spirit/ghost that 'lives' on your computer."
> 
> — Andrej Karpathy

> "By constantly rewriting the todo list, Manus is reciting its objectives into the end of the context... avoiding 'lost-in-the-middle' issues."
> 
> — Manus Blog

## Open questions / follow-ups

- How will throughput improvements (inference-speed shipping) further change the human-in-the-loop "micro-management" dynamic?
- At what point does the cost of "token guzzling" via agentic loops outweigh the speed benefits?
- To what extent can "Skills" replace RAG systems for dynamic codebase understanding?

## Next steps

- Integrate "Context Engineering" and "Attention Budget" principles into `notes/agentic-workflows.md`.
- Create a `notes/sub-agent-specialization.md` exploring the Explore/Plan/Guide pattern.
- Research "Context Rot" more deeply to determine optimal compaction thresholds for Antigravity's own workflows.

## Links

- Source: [https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Anthropic: Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
