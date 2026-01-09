---
title: Separate Discovery from Delivery
tags:
  - publish
  - principle
  - workflow
  - planning
  - publish
summary: Keep exploration and decision-making separate from execution to reduce scope creep and improve quality.
status: draft
---

# Separate Discovery from Delivery

Discovery is for exploring options and clarifying what to build. Delivery is for implementing a decided scope. Treat them as distinct modes with different outputs and different success criteria.

## Why separate them

- **Different feedback loops**: Discovery benefits from wide search and fast iteration, while delivery benefits from focus and constraints.
- **Reduced scope creep**: Capturing decisions first prevents implementation from drifting into new ideas mid-build.
- **Cleaner context**: A delivery session can start with a concise, stable plan instead of a trail of exploration.
- **Better reviewability**: Specs and PRDs are easier to review than half-implemented experiments.

## Practical workflow

1. **Discovery phase**
   - Gather inputs: goals, constraints, user needs, risks, edge cases.
   - Produce a concrete artifact: a PRD, a spec, a checklist, or a decision log.

2. **Delivery phase**
   - Execute against the artifact.
   - Keep changes small and testable.
   - Defer new ideas to a follow-up discovery pass.

## Examples

- **Large feature work**: Use interview-driven specification to expand requirements, then start a fresh session to implement the spec.
- **Ambiguous refactors**: Explore design options first, decide on a direction, then execute in a constrained PR.
- **Multi-part roadmap items**: Split discovery (what to do next) from delivery (making the next change real).

## Trade-offs

- **Upfront time**: Discovery takes time before visible code changes.
- **Requires discipline**: It is easy to slip back into exploration mid-delivery.
- **Artifacts can go stale**: Specs need updates if the delivery phase uncovers new facts.

## Related

- [[Interview-Driven Specification]]
- [[Spec-Driven Development]]
- [[ten-principles-for-coding-with-ai]]
