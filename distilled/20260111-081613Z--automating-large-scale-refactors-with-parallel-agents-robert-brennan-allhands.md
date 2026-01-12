---
title: "Automating Large Scale Refactors with Parallel Agents - Robert Brennan, AllHands"
source_url: "https://www.youtube.com/watch?v=rcsliSIy_YU"
captured_at: "2026-01-11T08:16:13Z"
distilled_at: "2026-01-11T08:18:21Z"
raw_refs:
  - "[[raw/20260111-081613Z--automating-large-scale-refactors-with-parallel-agents-robert-brennan-allhands]]"
capture_type: youtube_transcript
status: draft
agent: codex-cli
model: gpt-5.2
confidence_notes: "This is distilled from an auto-generated YouTube transcript with noticeable transcription errors; some proper nouns and technical terms may be misheard. The talk references a live workshop/demo; exact code and API details are not fully present in the capture."
tags: ["agent-orchestration", "refactoring", "parallel-agents", "tech-debt", "dependency-graph", "cve-remediation", "task-decomposition"]
---

## Summary

Robert Brennan (OpenHands) argues that many “large, repeatable, automatable” engineering tasks—especially dependency upgrades, vulnerability remediation, and framework/library migrations—are achievable with agents, but usually not as a single long-running one-shot. The practical approach is agent orchestration: decompose a refactor into PR-sized tasks, run multiple agents in parallel, and keep a human in the loop for intermediate review and validation. Examples include using dependency graphs to batch changes, a “verifier/fixer” loop that generates reviewable PRs, “scaffolding” that lets a codebase temporarily support both old and new APIs (e.g., Redux and Zustand) during incremental migration, and lightweight mechanisms for sharing discoveries across agents without blowing the context window.

## Key points

- Orchestration fits best for large, repeatable work: CVE/CDE remediation, dependency upgrades, modernization migrations, documentation/release notes.
- Long trajectories fail for predictable reasons: context window limits, compounding errors, missing domain knowledge, and unclear definition of “done”.
- Effective orchestration decomposes work into “one-shot” tasks that fit in a single commit/PR and are easy to verify (ideally via CI).
- Batching strategies can mirror team practices: parallelize what you can, define dependencies/order, and collate results into an integration branch.
- Dependency-graph batching + dependency-order execution helps avoid stepping on incomplete prerequisites.
- “Scaffolding” can allow partial migration while keeping the app runnable, enabling per-component parallel migration and progressive validation.
- Context sharing across agents is useful but has trade-offs: shared-everything doesn’t scale; file-based shared context can work with human review; agent-to-agent messaging increases non-determinism.
- A CVE remediation workflow: run one agent to scan and enumerate vulnerabilities, then spawn one agent per vulnerability to fix and open separate PRs (merge as ready; accept 90–95% solved).

## Concepts / principles

**90% automation target**  
Aim for “mostly automated” with human checkpoints, rather than full autonomy. An order-of-magnitude lift can come from human review + automated execution.

**PR-sized batches**  
Break refactors into chunks an agent can complete in one shot and a human can review quickly; constrain scope to reduce drift.

**Dependency-first sequencing**  
When changes depend on shared utilities or low-level modules, start from leaf nodes and work upward to reduce cascading failures.

**Scaffolding for incremental migration**  
Introduce temporary compatibility layers so old and new systems can coexist during migration; remove scaffolding at the end.

**Context sharing without context blowup**  
Share only the high-value discoveries (versions, conventions, gotchas) via a curated file or targeted broadcast, rather than merging all agent histories.

## Patterns

**Integration branch + accumulating PRs**  
Create a dedicated branch for the migration/refactor, optionally seed it with an “agent.md/micro-agent” context file, have agents land changes there, then remove scaffolding and merge to main.

**Dependency graph batching + verifier/fixer loop**  
Batch the repo (e.g., by directory) and use a verifier to flag issues per batch; when a batch fails verification, run a fixer agent to generate a focused PR; repeat until all batches pass.

**Scan-then-fan-out vulnerability remediation**  
Run one agent to choose an appropriate scanner (e.g., Trivy, `npm audit`) and produce a vulnerability list, then fan out to parallel fix agents that each update dependencies, fix breakages, and open PRs.

## Entities

- Robert Brennan: Co-founder/CEO of OpenHands; speaker.
- OpenHands: MIT-licensed coding agent; also referenced via an Agent SDK and a refactor SDK.
- Redux, Zustand: Example of a library migration with scaffolding and per-component parallelization.
- Trivy / `npm audit`: Example vulnerability scanning approaches mentioned in the workflow.

## Quotes

> The goal is not to automate this process 100%. It's something like 90% automation.

> I would suggest limiting yourself to about three to five concurrent agents. I find more than that your brain starts to break.

> One strategy… the most naive thing you can do is share everything… you're going to leave your context window really quickly.

## Open questions / follow-ups

- What exactly is the “micro agent” / `agent.md` format and how is it used in OpenHands workflows?
- What batching algorithms besides directory structure are most effective in practice (and how are they chosen)?
- How does the refactor SDK define “complexity” and “verifier” rules, and how well do those generalize beyond code smells?

## Next steps

- Capture the slides content (if available publicly) to fill in the missing implementation details referenced in the workshop.
- Turn the three orchestration strategies (piece-by-piece, dependency-tree order, scaffolding coexistence) into a reusable checklist for large migrations.
- Create a minimal “scan-then-fan-out” template for dependency/CVE remediation that can be reused across ecosystems (npm, pip, Maven, etc.).

## Links

- Source: [https://www.youtube.com/watch?v=rcsliSIy_YU](https://www.youtube.com/watch?v=rcsliSIy_YU)
- Slides: [https://dub.sh/openhands-workshop](https://dub.sh/openhands-workshop)
- Speaker: [https://twitter.com/RobertBrennan](https://twitter.com/RobertBrennan)
