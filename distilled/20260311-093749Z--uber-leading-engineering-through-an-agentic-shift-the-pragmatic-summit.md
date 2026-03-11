---
title: "Uber: Leading engineering through an agentic shift - The Pragmatic Summit"
source_url: "https://www.youtube.com/watch?v=i1tZN41VKcE"
captured_at: "2026-03-11T09:36:23Z"
distilled_at: "2026-03-11T09:37:49Z"
raw_refs:
  - "[[raw/20260311-093623Z--uber-leading-engineering-through-an-agentic-shift-the-pragmatic-summit.md]]"
capture_type: youtube_transcript
status: draft
tags:
  - agentic-coding
  - developer-platform
  - code-review
  - testing
  - migrations
  - engineering-management
  - internal-tools
  - ai-costs
agent: codex
model: gpt-5
skills_used:
  - make-distillation
confidence_notes: "First-pass distillation from an auto-transcribed conference talk. Product names, internal tool names, and some metrics may reflect transcription errors; ROI and performance numbers are presented as speaker claims."
---

## Summary

Uber frames its current AI push as a shift from pair programming to what the speakers call "peer programming": engineers act more like tech leads for multiple asynchronous agents rather than line-by-line authors. The talk argues that the main leverage is not autonomous feature creation, but moving large volumes of toil such as bug fixes, upgrades, migrations, unit tests, and review support into internal agent workflows.

The deeper point is organizational. Uber is not presented as succeeding because of one model or one agent product, but because it built a platform layer around model access, MCPs, client configuration, background execution, code review, validation, and migration campaign management. The claimed bottlenecks then move downstream: review load, test quality, adoption behavior, measurement, and cost control.

## Topics

- Toil as the highest-fit entry point for agents
- MCP gateway and internal agent platform architecture
- AIFX as the standard client/configuration layer
- Minion as the background agent platform
- Code Inbox for review routing and notification control
- UReview for AI-assisted review with grading and deduplication
- AutoCover for test generation plus independent validation
- AutoMigrate and Shephard for large-scale code changes
- Adoption tactics, measurement limits, and model-cost management

## Key points

- The talk reports an early productivity bump from Copilot-style assistance of roughly 10-15% in diff velocity, but treats that as materially smaller than the later gains from asynchronous agent workflows.
- Once Uber exposed agentic workflows internally, the speakers say about 70% of submitted workloads were toil tasks, suggesting that repetitive maintenance work is where trust and accuracy compound fastest.
- Uber's platform strategy is explicitly layered: model gateway and ML platform foundations, organizational context sources, MCP infrastructure, agent-building capabilities, client management, and then task-specific products on top.
- A central MCP gateway is used to proxy internal and external MCPs while standardizing authorization, telemetry, logging, registry, and sandboxing.
- AIFX is described as the common CLI for provisioning agent clients, installing/configuring MCPs, distributing default settings, and connecting developers to the broader agent platform.
- Minion is Uber's internal background-agent system, running on Uber infrastructure rather than vendor-hosted environments so it can access monorepos, networked systems, and internal defaults safely and quickly.
- Good defaults are treated as a major product feature: prompt templates, repository-specific setup, and prompt-improvement feedback are meant to raise task success for ordinary engineers rather than only power users.
- As agent throughput rises, review becomes the next bottleneck. Code Inbox attempts to solve the coordination side by surfacing only actionable reviews, assigning reviewers intelligently, and respecting focus time, time zones, and existing team workflows.
- UReview addresses the quality side of review by preprocessing diffs, running multiple internal or external analyzers, grading comments, deduplicating them, and favoring high-confidence actionable issues over noisy nits.
- AutoCover reflects a recurring pattern in the talk: generic agents were not considered sufficient for high-quality output, so Uber built a specialized generation plus critic pipeline and then exposed the validator separately for broader use.
- Large-scale maintenance work required a distinct platform. AutoMigrate handles identification, transformation, validation, and campaign management, while Shephard manages large batches of migration PRs over time.
- The speakers are careful to distinguish activity metrics from business outcomes. They claim strong improvements in developer sentiment and engineering velocity, but say the harder unresolved problem is tying those gains to revenue or feature-delivery outcomes.
- Cost is framed as a first-order design constraint. Uber reportedly moved from manageable spend to CFO-level scrutiny, which forced more deliberate model selection and a separation between planning models and cheaper execution models.

## MCP gateway setup

The talk gives only a medium-level description of Uber's MCP setup, but a few design choices are clear.

- Uber formed a cross-functional "tiger team" to move quickly on MCP adoption once the protocol started gaining traction.
- Instead of letting teams wire MCP servers directly into each client in ad hoc ways, they built a central MCP gateway.
- That gateway proxies both internal and external MCPs from Uber service infrastructure and exposes them to engineers in a consistent way.
- The gateway is responsible for the platform concerns the speakers call out explicitly: authorization, telemetry, logging, and the other standard control-plane concerns they do not enumerate in detail.
- On top of the gateway, they provide a registry so engineers can discover available MCPs rather than configuring everything manually.
- They also provide a sandbox so developers can try MCPs safely, confirm behavior, and evaluate whether a tool does what they expect before using it in real workflows.
- The setup appears to be part of a broader reuse strategy: MCPs and agents become discoverable building blocks that can be consumed from laptops, remote dev environments, Minion, and other internal systems.
- One important constraint from the later part of the talk is that integration remains hard in practice. The speakers explicitly say that exposing older and more fragmented parts of Uber's ecosystem through MCP endpoints has been a continuing challenge.

What seems to matter architecturally is not MCP as a protocol by itself, but MCP wrapped in enterprise control surfaces: one gateway, one registry/discovery layer, one sandbox/testing surface, and shared telemetry. That reduces per-team setup cost and makes it more realistic to connect many agent clients and internal tools without duplicating security and observability work everywhere.

## Concepts / principles

**Toil-first adoption**
The best entry point for agent systems is not ambiguous greenfield work, but bounded maintenance tasks with clearer start and end states.

**Platform before product**
What scales is not a single agent interface but the common substrate: auth, context access, MCP management, logging, tracing, defaults, and execution environments.

**Review is the new bottleneck**
Once code generation accelerates, organizational throughput depends on routing, filtering, grading, and validating much larger volumes of code safely.

**Specialized pipelines beat generic prompting**
For review, testing, and migrations, Uber repeatedly chose custom systems with critics, graders, validators, or campaign management rather than relying on a raw general-purpose coding agent.

**Abstraction as hedge**
Because models and vendor capabilities change quickly, internal systems need clean abstraction boundaries so the organization can swap underlying technology without rewriting everything above it.

**Adoption through peer proof**
Mandates can move a metric, but sustained adoption comes more from engineers sharing wins with engineers.

## Patterns

**Prompt improver**
- Inspect a user prompt before launch.
- Flag low-quality task descriptions.
- Suggest concrete improvements that raise the chance of a successful autonomous run.

**Background-agent PR loop**
- Submit a task to a hosted internal agent.
- Let it work asynchronously inside a prepared repo environment.
- Return a PR with artifacts, logs, test plan, and follow-up path if it fails.

**Maker-checker review pipeline**
- Run multiple review analyzers or plugins.
- Grade and deduplicate comments.
- Surface only the high-confidence subset to developers.

**Generation plus independent critic**
- Generate tests or code automatically.
- Run a separate validator/critic stage.
- Reuse the validator independently for human-authored output as well.

**Migration campaign manager**
- Define the transformation once, via prompt or deterministic script.
- Slice the rollout into many owner-scoped PRs.
- Refresh, route, notify, and track them as a managed campaign rather than one-off automation.

## Entities

- Michelangelo
- MCP gateway
- AIFX
- Minion
- Code Inbox
- UReview
- AutoCover
- AutoMigrate
- Shephard

## Quotes

> "AI is enabling people to become superhumans."

> "We want to focus on enabling our engineers to focus on creative work rather than toil."

> "We're going from pair programming to peer programming."

> "The cost of AI is too damn high."

## Open questions / follow-ups

- Which parts of Uber's platform stack are truly necessary for agentic adoption at scale, and which are artifacts of operating inside a very large, complex company?
- How should teams measure business impact once developer-activity metrics stop being persuasive to finance leadership?
- What quality thresholds should determine when a specialized internal pipeline is worth building instead of using a general-purpose coding agent plus better prompts?
- If review becomes the bottleneck, what combination of routing, grading, validation, and risk-scoring best preserves engineering judgment rather than automating it away?

## Next steps

- Compare this talk with other large-org adoption stories in the vault to isolate the common platform pattern: toil-first rollout, review support, and internal workflow embedding.
- Extract a reusable note on "review as the bottleneck in agentic coding" if Code Inbox, UReview, and similar systems keep recurring across sources.
- Revisit migration infrastructure as a distinct category of AI leverage, separate from day-to-day coding assistance.

## Links

- Source: [https://www.youtube.com/watch?v=i1tZN41VKcE](https://www.youtube.com/watch?v=i1tZN41VKcE)
