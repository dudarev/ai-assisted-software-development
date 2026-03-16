---
title: Context Graphs
tags:
  - publish
  - agents
  - memory
  - context-engineering
status: growing
distilled_refs:
  - "[[distilled/20260301-065737Z--the-great-transition.md]]"
---

# Context Graphs

A **context graph** captures decision traces: the evidence, actions, forks, and approvals behind an outcome. It matters when the outcome alone is not enough to answer questions like: *Have we seen this before? Why did we choose that? What did we try? What changed the decision?*

In that sense, a context graph is not just a graph of entities or documents. It is a way to preserve the path of work in machine-usable form so future humans and agents can inspect and reuse it.

## Working definition

**Context graph = connected decision traces across tools and time.**

The goal is to preserve more than the final "what." A useful context graph also preserves parts of the "how" and enough evidence to reconstruct the "why."

This is a claim about where durable context comes from: not only from documents or records, but from the operational path of doing work.

## The Core Unit: Decision Trace

A **decision trace** is the smallest reusable unit of context. It includes:

- what triggered the work
- what was observed
- what actions were taken
- where humans intervened
- what outcome happened
- why a key branch was chosen over another

In software engineering terms, this looks like an incident or ticket timeline that preserves not only summaries, but also evidence and rationale at important forks.

### Worked Example

A minimal decision trace for a production incident might look like this:

- **Trigger:** latency spike after deploy `api@2026.03.14.2`
- **Observed:** p95 up 4x, errors isolated to EU region, similar signature to incident `INC-1842`
- **Actions:** checked dashboards, compared deploy diff, disabled one feature flag, replayed failing requests
- **Human intervention:** on-call approved rollback after mitigation failed
- **Outcome:** rollback restored latency; feature flag left disabled pending root-cause fix
- **Rationale:** rollback chosen because a prior similar incident showed cache warmup was not the cause

The point is not just chronology. The useful property is that the trace preserves evidence, forks, and justification in a form another operator or agent can inspect.

## What Makes It Different

A context graph overlaps with several familiar systems, but the emphasis is different.

- **Knowledge graphs** model entities and relationships. Context graphs model decisions, evidence, and workflow paths.
- **RAG and document retrieval** return artifacts like docs, tickets, or PRs. Context graphs try to return the connected path: what was checked, what branches were considered, and what changed the conclusion.
- **Audit logs and process mining** capture events and common flows, but often miss the semantic forks: exceptions, approvals, overrides, and reasons.

In practice, a context graph may use knowledge-graph-style entities and retrieval systems underneath. The differentiator is that operational decisions and their evidence are first-class.

## Why It Matters

Most organizations store outcomes well and reconstruct reasoning badly.

The highest-signal context is often produced while work is being done: the checks, escalations, failed attempts, approvals, and exceptions. If humans and agents increasingly work through orchestrated loops, those traces can be captured as a byproduct rather than reconstructed later from incomplete records.

That matters because reusable traces can help with:

- faster triage by surfacing similar past cases
- better explanations by showing what evidence mattered
- safer automation by making approvals and exceptions explicit
- skill extraction by turning recurring successful traces into repeatable procedures

## Practical Shape

The useful starting point is probably not a universal ontology. It is a small core plus workflow-specific extensions.

A minimal core might include:

- **Trace identity:** trace ID, step ID, parent-child links, timestamps
- **Actors and artifacts:** humans, agents, services, tickets, PRs, dashboards, deploys, documents
- **Observations and actions:** signals, retrieved evidence, queries, mitigations, approvals, escalations, changes
- **Decision points:** options considered, selected option, constraints, confidence, human override
- **Outcome and provenance:** final state, verification result, side effects, source system, permissions, retention rules

This matches a pattern that already appears in adjacent systems: small interoperable cores, rich domain-specific extensions.

## Connection To Skills

One useful way to think about [[Agent Skills]] is that they are packaged procedures distilled from recurring decision traces.

- A decision trace is a single path through a workflow.
- A skill is a reusable procedure with instructions, constraints, tools, and expected outputs.

That suggests a practical loop:

1. Capture traces from real workflows.
2. Identify recurring high-value segments.
3. Package them into skills with guardrails and validation.
4. Feed those skills back into the workflow, producing cleaner traces and better outcomes.

This is one reason context graphs matter for agentic systems: they do not just store history. They create raw material for better procedures.

## Limits

Several caveats matter.

- **You do not capture "why" perfectly.** Often you capture the path directly and reconstruct the why from evidence, policy, and exceptions.
- **Not every workflow needs this.** Context graphs are most useful where exceptions are frequent, mistakes are costly, and simple checklists are not enough.
- **Precedent can decay.** Old traces may reflect stale policy, outdated infrastructure, or obsolete org structure.
- **Governance is central.** Permissions, retention, and sensitive data handling are not optional.
- **This may be a feature more than a category.** In some systems, a context graph may be an internal layer rather than a standalone product.

## Related

- [[Agent Skills]]
- [[Spec-Driven Development]]
- [[Maker-Checker Pattern]]
- [[Context Hygiene]]

## References

- Foundation Capital: “Context graphs: AI’s trillion-dollar opportunity” (December 22, 2025): https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity
- Foundation Capital: “Context graphs, one month in” (January 30, 2026): https://foundationcapital.com/ideas/context-graphs-one-month-in
- YouTube episode with Jaya Gupta and Ashu Garg: https://www.youtube.com/watch?v=zP8P7hJXwE0
- PlayerZero: “Context Graphs: Building Production World Models for the Age of AI Agents”: https://playerzero.ai/resources/context-graphs-building-production-world-models-for-the-age-of-ai-agents
- OpenTelemetry overview: https://opentelemetry.io/docs/specs/otel/overview/
- W3C PROV-O recommendation: https://www.w3.org/TR/prov-o/
- OpenLineage facets guide: https://openlineage.io/docs/guides/facets/
- Anthropic: “Skills” announcement: https://claude.com/blog/skills
- Anthropic engineering: “Equipping Agents for the Real World with Agent Skills”: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Stephen Chin (Neo4j): “Context Engineering: Connecting the Dots with Graphs”: https://www.youtube.com/watch?v=LLuKshphGOE
- Duncan Winn: “Using AI for Mission-Critical Production Systems”: https://www.youtube.com/watch?v=K35pC92MLyY
- Daniel Miessler: “The Great Transition”: https://danielmiessler.com/blog/the-great-transition
