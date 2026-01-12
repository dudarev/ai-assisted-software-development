---
title: "Tool definitions are the new Prompt Engineering"
source_url: "https://www.youtube.com/watch?v=rMhvSkXbv4A"
captured_at: "2026-01-11T12:41:23Z"
distilled_at: "2026-01-11T12:43:47Z"
raw_refs:
  - "[[raw/20260111-124123Z--tool-definitions-are-the-new-prompt-engineering.md]]"
capture_type: youtube_transcript
status: draft
tags: ["tool-design", "ai-agents", "context-engineering", "latency", "evaluation", "ux"]
confidence_notes: "YouTube auto-transcript; speaker attributions are ambiguous; distillation is based on selected excerpts (not full line-by-line review)."
---
## Summary

This conversation argues that “tool definition” quality often matters more than prompt tweaks once an agent hits production scale.
Tools that bundle workflows and align to user intent can reduce token usage, lower latency, and improve stability by pushing work into deterministic code.
Treat MCP (and APIs more generally) as plumbing; don’t expose low-level service contracts directly to the LLM if the agent’s intention is higher-level.
Tool outputs (not just the system prompt) can carry dynamic, need-to-know context and next-step guidance.
Much of what makes agents “work” in practice is UX, evaluation design, and operational feedback loops—not model choice alone.

## Topics

- Intro
- Insights from iFood (WhatsApp vs in-app UX; latency expectations)
- API vs agent intention (“tools are not APIs”)
- Tool definition clarity (reviewability, token cost, stability)
- Preemptive context loading (esp. voice / real-time)
- Contextualizing agent data (what to load, when)
- Prompt bloat (payments edge cases; avoid stuffing prompts)
- Agent building evolution (determinism dial; tool outputs can carry instructions)
- Agent program scalability (workflow encapsulation; reuse vs specificity)
- Why multi-agent is a dead end (speculative prediction; governance vs necessity)

## Key points

- Tool definitions tend to accrete edge cases; “if X then call Y” quickly becomes prompt-like code that bloats context and harms latency.
- A useful design test: write tools as if another team will reuse them, and have someone unfamiliar review whether the name/params make sense.
- “Tools are not APIs”: APIs describe downstream services; agent tools should describe the agent’s intentions and desired outcomes.
- Layer tools: keep lower-level integrations (e.g., MCP servers) behind intention-level tools (e.g., `get_brochure`) to reduce turns and hallucination surface area.
- Limit tool choice where possible to reduce hallucinations/context bloat; encapsulate common multi-step flows as a single workflow tool.
- Put instructions in tool responses when they’re conditional on state (“need-to-know”), instead of permanently inflating the system prompt.
- **Pattern**: Preemptive context loading can improve perceived latency in real-time/voice settings (grab likely-needed data “just in case”).
- Evaluations need to reflect product-specific outcomes and UX, not only generic “helpfulness”; error analysis → taxonomy → targeted eval sets.

## Concepts / principles

**Intention-based interfaces**
Agent-facing tools are closer to “what the agent is trying to do” than “how the backend works”. That shift reduces reasoning burden and context engineering overhead.

**Determinism as a dial**
Push stable, well-understood logic into deterministic software; keep the LLM where it adds flexibility/generalization. Tool design is one of the main knobs.

**Context on a need-to-know basis**
Instead of paying the token/latency tax up-front, fetch and inject context dynamically when the conversation/state indicates it’s needed. **Pattern**.

**UX is part of the agent**
Interface expectations vary (e.g., in-app vs WhatsApp); success depends on interaction design, latency tolerance, and trust calibration, not only model outputs.

## Patterns

- Workflow tool encapsulation: wrap multi-step retrieval/classification flows behind a single tool call (reduce turns and tool-choice branching).
- **Dynamic system prompt by state: keep the stable core prompt small; vary state-dependent instructions to reduce repeated context.**
- Tool response as control surface: return both data and constrained UI/actions (buttons/components) so the user (or test agent) can “click” instead of re-describing.
- Trace-driven evaluation loop: inspect traces → build an error taxonomy → generate a product-specific test set → iterate on tools/prompts/models.
- Simulated user + UI-aware harness: run scenario-based evals with an agent that impersonates a user, including interaction with returned UI elements.

## Entities

- Prosus / iFood (food delivery in Brazil; WhatsApp vs in-app agent UX differences)
- Arcade.dev (agent action platform)
- MCP (wire protocol for tool invocation; “plumbing” rather than an agent UX)
- LangGraph (mentioned as orchestration under-the-hood)
- “Large Commerce Model (LCM)” (Prosus internal model for user/item representations)
- Sierra (mentioned in context of voice agents and preemptive context loading)

## Quotes

> tools are not APIs.

> a tool is kind of like the service contract for the agents intentions.

> let somebody else look at your tool definitions. Let them see if they can understand it.

> I don't need to to bloat the system prompt with those instructions.

> an agent is really just a collection of prompts and tools.

## Open questions / follow-ups

- What’s a good “tool definition review checklist” (naming, parameter design, error modes, deterministic fallback, output format)?
- How do you measure UX quality in agent evals without conflating it with model quality (and how do you keep it cheap to run)?
- When does a multi-agent setup add real value vs. acting as a governance boundary (permissions/ownership) rather than a technical necessity?
- What’s the right boundary between “dynamic tool response guidance” and “policy/system prompt” to avoid accidental prompt injection?

## Next steps

- Create a durable note on “Intention-based tool design” (API vs tool, layering, workflow tools, determinism dial).
- Create a durable note on “[[Context engineering patterns]]” (need-to-know injection, preemptive loading, dynamic prompts).
- Create a durable note on “Agent evaluation in product contexts” (trace-driven error taxonomy, UI-in-the-loop evals).

## Links

- Source: https://www.youtube.com/watch?v=rMhvSkXbv4A
