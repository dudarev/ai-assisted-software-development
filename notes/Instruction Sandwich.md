---
title: Instruction Sandwich
status: draft
tags:
  - pattern
  - reliability
  - checklists
  - verification
  - context-management
  - publish
summary: A prompt-structuring technique where you repeat a critical instruction as explicit checklist steps before and after (and sometimes during) the main task, so the agent executes it as part of the plan rather than treating it as optional framing.
source_url: "https://www.youtube.com/watch?v=M-zOSEJFNos"
---

# Instruction Sandwich

**Instruction sandwich** is a prompt-structuring pattern for increasing compliance on *critical* instructions that assistants often skip (tests, validation, constraints, evidence).

Instead of saying “remember to run tests,” you structure the task so that the instruction becomes an explicit **step** *before* and *after* the main work (and sometimes between sub-steps).

The simplest form:

1. Run tests (baseline)
2. Do the change
3. Run tests again (proof)

## Why it works

Critical instructions are easy for a model to treat as “background.” When the instruction is a **first-class step** in a numbered plan or to-do list, it becomes part of the agent’s execution trace:

- it gets revisited during plan-following (not just read once in the preamble)
- it creates a natural place to *stop and produce evidence*
- it reduces “selective hearing” where the agent optimizes for completion and silently relaxes constraints

This is closely related to the broader idea: **convert prose constraints into executable checklists**.

## When to use it

Use an instruction sandwich when:

- the instruction is *non-negotiable* (tests, lint, safety boundaries)
- the task is multi-step (refactors, migrations, “touch many files” work)
- you want an artifact that a human checker can quickly evaluate (logs, outputs, diff + green checks)

## Common sandwiches

### Verification sandwich

- Run `X` — tests, lint, or build
- Make the smallest change toward the goal
- Run `X` again and paste the output

### Evidence sandwich

- Define what evidence will prove success
- Do the task
- Provide the evidence — call out any gaps

### Alignment sandwich

- Restate goal + constraints in your own words
- Do the task
- Re-check constraints: explicitly confirm each one is satisfied

### Refactor sandwich

Repeat verification between sub-steps:

- Run tests
- Refactor step A
- Run tests
- Refactor step B
- Run tests

## Failure modes

- **“Fake sandwich”**: the agent writes the steps but doesn’t run them. Fix: require command output or a specific success string.
- **Over-sandwiching**: too many repeated steps creates overhead and context noise. Fix: sandwich only the few instructions you *actually* care about.
- **Wrong verification**: running the wrong tests or an incomplete check. Fix: specify the exact command(s) and what “green” means.

## Relationship to other patterns

- [[Maker-Checker Pattern]]: sandwiches are a cheap way to force a maker to produce checker-grade evidence.
- [[Preflight the Plane]]: preflight often includes “what will we run to prove progress”; sandwiches operationalize that inside the task.
- [[Context Hygiene]]: checklists reduce drift and make it easier to reset context without losing rigor.
- [[Role Separation Pattern]]: a dedicated “reviewer/checker” role can enforce sandwich steps, or you can use sandwiches to approximate a role switch inside one thread.

## References

- [Lada Kessler — Emerging Patterns for Coding with Generative AI (DevCon Fall 2025)](https://www.youtube.com/watch?v=M-zOSEJFNos)
- [Workshop resources (linked from the talk description)](https://github.com/lexler/Talks/blob/main/augmented_coding_patterns_masterclass.md)
