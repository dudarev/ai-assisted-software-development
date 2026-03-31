---
title: "Head of Claude Code: What happens after coding is solved | Boris Cherny"
source_url: "https://www.youtube.com/watch?v=We7BZVKbCVw"
captured_at: "2026-02-28T09:18:39Z"
distilled_at: "2026-02-28T09:22:08Z"
raw_refs:
  - "[[raw/20260228-091839Z--head-of-claude-code-what-happens-after-coding-is-solved-boris-cherny]]"
capture_type: youtube_transcript
status: draft
agent: codex
model: gpt-5.2
skills_used: ["make-distillation"]
confidence_notes: "Based on an auto-generated transcript with likely transcription errors and paraphrase-y segments; treat exact numbers and proper nouns as unverified unless checked against the linked episode transcript."
tags: ["coding-agents", "agentic-workflows", "latent-demand", "product-strategy", "ai-safety", "future-of-software-engineering"]
---

## Summary

Boris Cherny (Anthropic) describes a “post-coding” trajectory where code generation becomes cheap and reliable enough that the bottlenecks move *after* writing code: deciding what to build, coordinating work, and safely running agents that can act on your behalf. In this framing, “coding is solved” doesn’t mean software is solved; it means attention shifts to product sense, evaluation, and tool-connected execution.

Two recurring themes:
- **Product follows latent demand:** watch how people (and even the model) “abuse” a tool, then build the simplest product that makes that behavior easy.
- **Speed via loosened constraints:** ship earlier, iterate from real usage, and don’t prematurely optimize costs (e.g., token budgets) before you’ve found what works.

## Key points

- **What comes after code:** agents start scanning feedback/bug reports/telemetry and proposing work (and even raising PRs), pushing the bottleneck toward prioritization.
<!-- TODO: Create a permanent document that discusses a blur between the roles for developers that become more like engineering design and PM roles so that they increasingly overlap there are similar sentiments in other distilled notes so they should be combined into a single coherent note. -->
- **Role blur:** engineering/design/PM roles increasingly overlap; “builder” becomes a plausible umbrella role (with specialties rather than strict boundaries).
- **Team principles (as described):**
  - Underfund projects slightly to force clarity and leverage automation.
  - Bias to shipping *today*; speed compounds via shorter feedback loops.
  - Give engineers “unlimited tokens” early to explore; optimize costs only after something works at scale.
- **“Don’t box the model in”:** prefer a goal + tools over rigid orchestrations; let the model pull context via tools instead of front-loading it.
- **Bitter Lesson as product advice:** bet on more general capabilities; workflow scaffolding gains can get eclipsed by the next model release.
- **Safety as layered practice:** (1) alignment/interpretability, (2) lab-style evals, (3) real-world behavior; “research preview” releases are part of learning what fails in the wild.
- **Race to the top:** open-sourcing safety primitives (e.g., a sandbox) is positioned as a way to raise the industry baseline.

## Concepts / patterns

**“Coding solved” shifts where expertise matters**
If generating code is increasingly a commodity, differentiation shifts to: choosing problems, defining success, instrumenting systems, and integrating tools/workflows where agents can execute.

**Latent demand, two ways**
- *User latent demand:* repeated hacks/misuse show what people want the product to be.
- *Model latent demand:* observe what the model “wants to do” when given minimal scaffolding, then shape tools and interfaces around that.

**Release early for both product and safety**
When capabilities are hard to predict a priori, iteration requires exposure to real usage patterns—while still using guardrails (sandboxing, permissions, etc.) to bound damage.

## Practical usage tips (from the episode)

- Start with one tool-connected task (e.g., email triage, desktop cleanup).
- Then connect tools across systems (e.g., email → spreadsheet → Slack follow-ups).
- Run tasks in parallel (“multi-quading”) and treat waiting time as the new workflow primitive.

## Quotes

> “Coding is largely solved.”

> “The product is the model.”

> “Don’t try to box the model in.”

> “Use common sense.”

## Open questions / follow-ups

- If agents can propose and implement work, what becomes the highest-leverage “prioritization interface” (telemetry, feedback, strategy docs, constraints)?
- What are failure modes of “minimal scaffolding” as models get more agentic (especially with connected tools)?
- How do you operationalize “safe in the wild” beyond anecdote (what metrics, audits, or incident playbooks)?

