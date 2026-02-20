---
title: Preflight the Plane
tags:
  - workflow
  - context-management
  - verification
  - publish
status: draft
chats:
  - https://app.napkin.ai/page/CgoiCHByb2Qtb25lEiwKBFBhZ2UaJDQ4NGI3YzkyLTEzYTUtNDI0ZC04ZTU1LTM3ZDY2ODFkNWVjMw
---
# Preflight the Plane

**Preflight** is a session initiation checklist for AI-assisted / agentic work.

It is the counterpart to **[[Landing the Plane]]** (session shutdown): where landing focuses on cleanup + handoff, preflight focuses on **scoping + context selection + verification setup** so the session doesn’t drift.

![[preflight-the-plane.svg]]

## When to run it

Run preflight when:
- you start a new chat (especially after a reset)
- you resume after time away
- you’re about to start an autonomous “loop” (background run / repeated iterations)
- you notice context pollution and decide to restart cleanly

## The Problem

Without a preflight:
- the session starts with **ambiguous intent**
- the agent invents defaults and “helpful” scope expansions
- there’s no shared definition of **done**
- verification is an afterthought (“looks right”)
- you waste the first 10–20 minutes rebuilding context from memory

## The Preflight Checklist

### 1) Pick *one unit of work*

State the task in one sentence.

Add:
- what’s explicitly *out of scope*
- what “done” means (observable outcome)

(If you can’t do this, the session will likely mix concerns.)

### 2) Rehydrate only the *minimum* context

Decide what the agent should read first:
- the smallest set of files/docs that define intent and constraints
- the current “state” artifact (plan/status/progress) if one exists

Rule of thumb: prefer **a few high-signal artifacts** over “here’s everything”.

### 3) Establish ground truth (verification first)

Before implementing, agree on:
- the command(s)/checklist that will prove progress (tests, build, smoke check, lint, or a manual verification script)
- what output counts as success vs failure

This turns “done” into something the workflow can actually detect.

### 4) Write a tiny plan (and stop)

Produce:
- 3–7 steps max
- the first step should be a small, reversible move
- call out the first verification point (“after step N, run X”)

Then pause for confirmation before large code changes.

### 5) Set guardrails for this session

Pick the constraints that prevent common failure modes:
- timebox (e.g., 25–60 minutes)
- “ask-first” actions (renames, deletions, major refactors)
- rollback strategy (checkpoint/commit frequency)
- if doing autonomous work: scope limits and where the agent may write

## Preflight for Autonomous Loops (extra)

If you’re starting a loop (iterative agent runs), preflight must include:

- **Exit criteria**: an unambiguous condition (tests green, specific string promise, checklist complete)
- **Objective checks**: the loop must run the checks, not just claim it did
- **Max iterations / circuit breaker**: stop after N attempts
- **State file**: a `progress.md`/ledger/checklist the loop reads and updates each iteration
- **One change per iteration**: reduce blast radius and make rollback possible

## A trigger phrase (human → agent)

“Preflight this session:
1) ask clarifying questions until the task is one unit of work with explicit done criteria,
2) list the minimal files/docs you need to read,
3) propose a 3–7 step plan with verification points,
4) propose guardrails (ask-first actions, checkpoints),
then stop and wait for approval.”

## References

- Geoffrey Huntley, “Fundamental Knowledge SWE's in 2026 Must Have (Hiring Bar)” (one task per context window; frequent new-chat resets): https://www.youtube.com/watch?v=F5wxBoGSWtk
- “AI Techniques Distilled From Thousands of Hours of Real Work” (silent requirement dropping; clear context as fix): https://www.youtube.com/watch?v=kf6h6DOPjpI
- Aleksander Stensby, “10 tips to level up your ai-assisted coding” (plan first; manage context; recap + reset): https://www.youtube.com/watch?v=z8XWvBpL_EA
- Geoffrey Huntley, “Ralph Wiggum as a ‘software engineer’” (loop framing; objective checks): https://ghuntley.com/ralph/
- [[Steve Yegge]], “Beyond Instructions: How Beads Lets AI Agents Build Like Engineers” (landing-the-plane idea; continuity discipline): https://www.youtube.com/watch?v=s96O9oWI_tI
- pi (minimal agent stance; context/tooling as a budget): https://www.youtube.com/watch?v=4p2uQ4FQtis
