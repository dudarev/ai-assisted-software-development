---
title: Disposable Software
created: 2026-01-16
tags:
  - publish
  - software-engineering
  - vibe-coding
  - future-of-work
  - engineering-economics
summary: A shift from long-lived SaaS platforms to ephemeral, bespoke tools built to solve immediate problems and then discarded or regenerated.
distilled_refs:
  - "[[distilled/20260115-204021Z--what-happens-now-t3-theo.md]]"
  - "[[distilled/20260107-082632Z--coding-with-ai-chip-huyen.md]]"
  - "[[distilled/20260114-233350Z--local-context-renaissance-dannypostma.md]]"
---

# Disposable Software

**Disposable Software** refers to programs and utilities built with the expectation that they will solve a specific, one-off problem and then be discarded, rather than maintained as long-term assets. This shift is driven by the collapse of implementation costs due to AI, moving the "make vs. buy" and "build vs. ignore" thresholds significantly.

## The Economic Engine: Code is Cheap, Software is Expensive

Traditionally, code was expensive to write, requiring teams of specialized engineers. In that era, software longevity and maintenance were the primary goals to recoup the high initial investment.

In the AI-native era, this relationship has inverted:
- **Code is Cheap**: LLMs and agents (like Claude Code and Aider) have effectively killed the cost of generating lines of code.
- **Software is Expensive**: "Real" software—which accounts for maintenance, edge cases, security, data ownership, and scaling—remains as difficult and costly as ever.

As a result, we are entering an era of **Personal Disposable Software**. If a custom solution can be generated in 5 minutes, the effort of maintaining it often exceeds the effort of simply regenerating it the next time it's needed.

## Characteristics of Disposable Software

- **CLI-First**: Optimized for high-bandwidth interaction with agents.
- **Local-First**: Leverages the local file system for maximum context bandwidth and data sovereignty (see: [[File over App]]).
- **Zero Friction**: No onboarding, no signup, no complex database configuration. It is "software as a scratchpad."
- **Niche/Bespoke**: Solves a problem too small to be worth a SaaS product but annoying enough to warrant 5 minutes of "vibe coding."

## Key Patterns

### Burn and Rebuild
When an AI-generated codebase becomes messy or brittle ("eldritch horrors"), the most efficient path is often to discard the implementation and have an agent regenerate it from a verified specification. This requires that the **specification**, not the code, be the primary source of truth.
- *See also: [[Rebuild Threshold]], [[Spec-Driven Development]]*

### Endpoint Dynamics
A future architectural pattern where a network endpoint doesn't just execute static code, but generates a new binary or logic path tailored specific to the shape of the incoming request payload.

### From SaaS to Scratchpads
While legacy SaaS (Software as a Service) optimizes for **retention, lock-in, and expansion**, disposable software optimizes for **immediacy, control, and solution-delivery**.

## The New Differentiators

When anyone can generate a functional app in a weekend, the primary competitive advantages shift from "coding skill" to:
1. **Taste & Timing**: Knowing what to build and when it matters.
2. **Distribution**: Not just building, but getting people to care.
3. **Motivation**: The resilience to push through the "hard parts" (architecture, rigor, deployment) that AI still struggles with.
4. **Orchestration**: The ability to direct a swarm of agents toward a coherent system goal.

## Related Notes
- [[Rebuild Threshold]] - The decision rule for when to replace vs. refactor.
- [[Vibe Coding Is FAAFO]] - The internal loop of experimentation.
- [[Spec-Driven Development]] - Ensuring reliable outcomes from disposable generation.
- [[Three Developer Loops of Vibe Coding]] - The different timescales of software evolution.
- [[File over App]] - Why local files are the best home for disposable utilities.

## References
- Theo (t3.gg), ["What happens now?"](https://www.youtube.com/watch?v=28z6OjsNsUk) (2026)
- Chris Gregori, ["Code is cheap now, software isn't"](https://www.chrisgregori.dev/opinion/code-is-cheap-now-software-isnt)
- Chip Huyen, ["Coding with AI"](https://www.youtube.com/watch?v=xY1FcjIbErQ) (2025)
- Danny Postma, ["The Renaissance of Local Context"](https://x.com/dannypostma/status/2011065092843139291) (2026) — see [[File over App]]
