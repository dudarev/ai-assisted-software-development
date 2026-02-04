---
title: "Context graphs: AI’s trillion-dollar opportunity — Jaya Gupta, Ashu Garg (Foundation Capital)"
source_url: "https://www.youtube.com/watch?v=zP8P7hJXwE0"
captured_at: "2026-02-04T21:43:34Z"
distilled_at: "2026-02-04T21:45:22Z"
raw_refs:
  - "[[raw/20260204-214334Z--context-graphs-ai-s-trillion-dollar-opportunity-jaya-gupta-ashu-garg-foundation-.md]]"
capture_type: youtube_transcript
status: draft
agent: codex
model: gpt-5.2
skills_used: [make-distillation]
confidence_notes: "Auto-transcribed podcast; some company/product names and phrasing may be mistranscribed."
tags: ["context-graphs", "agents", "enterprise-ai", "decision-traces", "data-governance", "systems-of-record", "moats"]
---

## Summary

The episode proposes **context graphs** as a new “institutional memory” layer for enterprises: a machine-usable representation of *why* decisions were made, built by aggregating **decision traces** (the sequence of steps, exceptions, overrides, and human-in-the-loop reasoning during real work). The claim is that as “systems of agents” (multi-agent + human-in-loop process automation) become common, the context graph becomes the durable, defensible moat for applied AI companies—because it’s created in the operational execution path and stitched across many systems of record and engagement (email, Slack, Salesforce, code/tickets, etc.).

They argue this is not a single ideal data structure so much as a framework whose implementation varies by workflow and data type. A key distinction is **read path vs write/orchestration path** (the transcript often sounds like “right path,” but the intended contrast is conceptual): systems of record and analytical stacks mostly capture outcomes (“what happened”), while agentic orchestration can capture the step-by-step path (“how it happened”), which is where decision traces are generated. They also address objections (you can’t fully capture “why”), privacy/governance challenges, and why “universal” enterprise graphs are unlikely; instead, context graphs emerge per workflow/vertical and compound via an automation flywheel.

## Key points

- **Context graph = aggregated decision traces** that preserve “the why” behind enterprise decisions (including exceptions, overrides, and cross-system context).
- **Decision traces live in the operational loop** (the work being executed), not primarily in post-hoc analytics/ETL.
- **Systems of agents** (multi-agent, multi-step automation with humans in the loop) have an advantage because they sit in the orchestration path where traces are produced.
- **Incumbents may struggle** because they don’t orchestrate end-to-end workflows and much enterprise value is in messy unstructured “dark data” (email, chat, calls).
- **Systems of record still matter**: they remain the “source of truth” for outcomes, while context graphs aim to capture the missing connective tissue (process + rationale) across systems.
- **Data governance/security is core**, not an afterthought: sensitive data + permissions determine what can be captured and replayed.
- **Not a universal graph thesis**: context graphs emerge per process; “one enterprise-wide context graph” is framed as impractical.
- **Prediction**: within ~12 months, hundreds of context graphs run in production; a “context graph stack” becomes a recognizable best-practice layer.

## Concepts / principles

**Decision trace (core unit)**  
The trace of how an outcome was reached: steps taken, human interventions, exceptions/overrides, and cross-system evidence.

**Systems of record (“what”) vs context graphs (“why/how”)**  
Systems of record (e.g., CRM, ticketing, warehouses) capture authoritative endpoints (deal closed, bug fixed, revenue amount). Context graphs are positioned as a layer that stitches together the evidence and reasoning that led to those endpoints, across both structured and unstructured systems.

**Read path vs write/orchestration path (conceptual)**  
Read-path systems look back on outcomes (analytics, reporting, historical states). Write/orchestration-path systems participate while work is being done (triage → queries → human review → decision → execution), enabling capture of the *sequence* and interventions that become decision traces.

**Emergent capture beats upfront modeling**  
Decision traces are captured as a byproduct of doing work (especially with agentic automation), rather than being defined via workshops/ontologies first.

**Automation flywheel**  
More automation → more traces captured → richer context graph → more value extraction → more automation.

## Example: Player Zero (as described in the episode)

Player Zero is used as a concrete example of a “system of agents” in software engineering / debugging. The workflow described is roughly:

1) a support ticket arrives, 2) an agent triages and runs investigations/queries across code + tooling, 3) a human is pulled in when needed, 4) the human’s actions/queries become part of the trace, 5) a hypothesis is formed, 6) a fix is produced and shipped, 7) the full loop becomes reusable “institutional memory” for similar future incidents.

## Companies mentioned (non-exhaustive; names may be mistranscribed)

- “Systems of agents” / workflow examples: Player Zero; “Olive” (sales); Tenor (healthcare intake); “Anvilogic” (security).
- Adjacent / ecosystem: Glean (discussed as a horizontal player); Atlan (data catalog); Okta (security); Skyflow (PII / sensitive data management).
- Other examples named in passing: Sierra; Decagon; Salesforce; Slack; email; Zoom.

## Entities (mentioned)

- People: Jaya Gupta, Ashu Garg, swyx
- Orgs/products: Foundation Capital, Player Zero, Glean, Atlan, Okta, Salesforce, Slack, Skyflow
- Related infra: data catalogs, graph databases (general category), data warehouses (general category)

## Quotes

> “A context graph is the institutional memory of all the why behind the set of decisions.”

> “When you aggregate decision traces in a way that you can then learn from them… that layer becomes a context graph.”

> “Analytical systems… capture the end point of a decision… What they don't know… is… the sequence of steps.”

## Open questions / follow-ups

- What minimum schema makes decision traces *machine-usable* without forcing heavy human annotation?
- What governance model works in practice (PII, permissions, retention) while still enabling learning from traces?
- What are the “best first” workflows where traces are high-signal (vs noisy) and the flywheel turns fastest?

## Next steps

- If this thesis feels relevant, capture and distill the linked Foundation Capital post and Jaya’s thread for sharper definitions and examples.
- Consider a durable `notes/` write-up that distinguishes context graphs from adjacent ideas (knowledge graphs, data catalogs, “metadata layers”, data mesh) and lists falsifiable bets.

## Links

- Source (YouTube): https://www.youtube.com/watch?v=zP8P7hJXwE0
- Show notes: https://foundationcapital.com/context-graphs-ais-trillion-dollar-opportunity/
- Jaya’s thread: https://x.com/JayaGup10/status/2003525933534179480
- Related: https://simple.ai/p/what-are-context-graphs
