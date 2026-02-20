---
title: Skill Extraction Loop (Solve Once → Codify → Delegate)
tags:
  - skills
  - workflow
  - delegation
  - guardrails
  - continuous-improvement
  - publish
status: draft
---

# Skill Extraction Loop

The **skill extraction loop** is the practice of turning a repeatedly-used workflow into a reusable, delegatable **skill** (instructions + tooling + verification) so agents can run it with less supervision and less variance.

You’ll also see this described as a **skill-capture loop** or “solve once → codify → reuse”.

The goal is not “more automation”. The goal is **more reliable delegation**: fewer reminders, fewer one-off explanations, and tighter feedback loops.

## When to extract a skill

Extract a skill when:

- The task recurs (or will recur) and the *successful path* is mostly stable.
- You can define a clear **definition of done**.
- There is a cheap **verification step** (tests, checks, diff review, invariants).
- The work can be bounded with explicit **inputs/outputs/constraints**.

Hold off when the task is genuinely one-off, the domain is still shifting daily, or the work is primarily taste/judgment that you can’t yet explain as constraints.

## The loop

1. **Do it once (with instrumentation)**  
   Run the task end-to-end (often with an agent), keeping a short log of: what worked, what failed, what the agent misunderstood, and what checks actually caught issues.

2. **Extract the minimal runbook**  
   Write the smallest set of steps that reliably reaches “done”:
   - inputs required and where to find them
   - constraints (what not to change, safety limits)
   - expected outputs/artifacts

3. **Add guardrails**  
   Make the skill hard to misuse:
   - verification commands (tests, linters, formatters, sanity checks)
   - stop conditions (“if X fails, do Y / escalate”)
   - permissions boundaries (what systems/accounts the skill can touch)

4. **Package as a skill**  
   Put the runbook somewhere agents can reliably load and follow, with a predictable interface (arguments, expected files, output format). A “skill” might be a Markdown procedure, a small script, or a directory that bundles instructions + tooling.

5. **Reuse and refine**  
   Each time the skill fails, treat it as signal:
   - fix the skill (instructions/tooling) before running again
   - add a new check if the failure was preventable
   - prune steps that don’t change outcomes

## What “good” looks like

A good extracted skill:

- has a narrow scope (“upgrade dependency X safely”, not “fix the repo”)
- produces a reviewable artifact (diff, report, checklist, PR)
- includes a verification path and “what to do on failure”
- is safe-by-default (least privilege, no surprising side effects)
- is versioned like code (reviewed, updated, and retired when stale)

## Related notes

- [[Compounding Engineering Loop]]
- [[Agentic Harness]]

## References

- Quinn & Thorsten. “Raising An Agent Episode 10 (Sidebar Is Dead)”. YouTube. https://www.youtube.com/watch?v=4rx36wc9ugw
- Lev Selector. “Have you heard these exciting AI news? - February 16, 2026 AI Updates Weekly”. YouTube. https://www.youtube.com/watch?v=GsHA0eAcmaI
- Aleksander Stensby. “10 tips to level up your ai-assisted coding”. YouTube. https://www.youtube.com/watch?v=z8XWvBpL_EA
- Daniel Miessler. “A Deepdive on my Personal AI Infrastructure (PAI v2.0, December 2025)”. YouTube. https://www.youtube.com/watch?v=Le0DLrn7ta0
- Daniel Miessler. “Personal AI Infrastructure”. https://danielmiessler.com/blog/personal-ai-infrastructure
- “You are Not Ready: Agentic coding in 2026”. YouTube. https://www.youtube.com/watch?v=6W_-YWHKwZ4
- Kepano. “Obsidian + Claude Code workflows”. X (thread). https://x.com/kepano/status/2007223691315499199
