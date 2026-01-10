---
title: Shipping at Inference-Speed
source_url: https://steipete.me/posts/2025/shipping-at-inference-speed
captured_at: 2026-01-03T11:00:50Z
distilled_at: 2026-01-03T11:02:29Z
raw_refs:
  - "[[raw/2026-01-03T130050+0200 - Shipping at Inference-Speed]]"
capture_type: web_page
status: draft
agent: codex
model: gpt-5.2
confidence_notes: This is a first-pass distillation of a single blog post; it reflects the author’s anecdotes and preferences. Some product/model names and features may be time-sensitive.
tags:
  - agentic-coding
  - developer-workflow
  - inference-time
  - cli-first
  - context-management
  - model-selection
  - automation
  - tooling
twitter_thread: https://x.com/steipete/status/2005451576971043097
---

## Summary

Peter Steinberger argues that, compared to earlier in 2025, agentic coding has shifted from “sometimes works” to “working is the expectation”, changing the practical bottlenecks from typing and implementation to **inference time** and **hard thinking**. He describes a workflow where he reads far less code, instead watching agent output streams, and focuses his attention on higher-leverage choices (language/ecosystem, dependencies, and system design). He also contrasts “codex” and “Opus” behaviors (especially around how much code they read before editing), and shares concrete tactics for building faster: start with a CLI to close the tool loop, reuse patterns across projects, keep agent-friendly docs, and automate recurring tasks via skills/scripts.

## Key points

- Expectations changed: “working code from prompts” is treated as the default, not a lucky outcome.
- Main constraints become: inference latency + the genuinely hard parts (dependencies, architecture, data flow).
- “CLI first” is a speed tactic: agents can run CLIs directly and verify outputs, tightening feedback loops.
- Trust shifts from reading to monitoring: he often watches the code stream and samples key areas rather than reading everything.
- Model behavior differences matter in practice: a slower model that reads more can be faster overall if it reduces “fix the fix” cycles.
- Workflow is built for iteration: queue tasks, avoid heavy orchestration, steer by playing with results, and evolve the system incrementally.
- Context management is treated as engineering: maintain `docs/` per project, reuse context across projects, and design repositories so agents navigate them easily.

## Concepts / principles

**Inference-limited development**: throughput is dominated by model runtime (and prompt/feedback cycles), not human typing speed.

**Watch the stream, sample the system**: replacing comprehensive code-reading with monitoring generation + spot-checking critical parts (with higher reliance on tests/tooling).

**CLI as the default harness**: start with a command-line interface so the agent can execute, observe, and iterate with minimal friction.

**Agent-friendly codebase design**: structure and documentation optimized for model navigation (clear folders, local docs, predictable conventions).

**Benchmarks are insufficient** (author claim): “close” benchmark scores can hide large differences in real workflows like refactors and multi-file work.

## Patterns

**Cross-project pattern propagation**: once a practice works in one repo, ask the agent to replicate it across similar projects (then validate).

**Queue-driven iteration**: keep a rolling queue of tasks and steer based on what you learn from running systems, not a fully pre-specified plan.

**Ad-hoc refactoring**: clean up when prompts slow down or “ugly” code appears in the stream, rather than scheduling dedicated refactor days.

**Short prompts + rich evidence**: write shorter prompts and attach concrete artifacts (e.g., screenshots for UI issues) instead of long textual instructions.

## Entities

- Author: Peter Steinberger
- Models/tools mentioned: codex, Opus, Claude Code, GPT-5, GPT-5.2, GPT-5 Pro
- Projects/examples: oracle (CLI), VibeTunnel, Clawdis, summarize
- Tooling referenced: Swift build tooling (without Xcode), iOS Simulator, Playwright, Tailscale, Jump Desktop

## Quotes

> "The amount of software I can create is now mostly limited by inference time and hard thinking."

> "These days I don’t read much code anymore."

> "Sometimes it just silently reads files for 10, 15 minutes before starting to write any code."

> "Whatever you build, start with the model and a CLI first."

## Open questions / follow-ups

- What validation practices make “not reading most code” safe enough (tests, linters, tracing, typed boundaries, staged rollouts)?
- How does this workflow change in teams (review, shared context, conflict resolution), vs a mostly-solo setup?
- What repository/doc conventions most reliably improve agent navigation and reduce rework across refactors?

## Next steps

- Consider integrating “inference-limited development” and “CLI as harness” into `notes/Agentic Coding.md`.
- Cross-link to `notes/agentic-harness.md` for patterns about closing the loop via executable interfaces.
- Connect the “execution vs orchestration” role shift framing to `notes/Orchestrator vs. Executor.md`.
- Capture a small checklist for “agent-friendly codebase design” (folder conventions, docs hygiene, dependency selection heuristics).
- We can also cross-link it to agent skills because this is something that's relevant to that pattern of cross project pattern propagation. skills can be copied from one place to another.

## Links

- source: https://steipete.me/posts/2025/shipping-at-inference-speed
