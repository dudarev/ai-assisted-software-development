---
title: Compounding Engineering Loop (Plan → Delegate → Assess → Codify)
created: 2026-01-02
tags:
  - workflow
  - continuous-improvement
  - productivity
  - publish
chats: https://chatgpt.com/c/6957c2d0-7370-8326-a6b8-8ec8c6670cbc
---

# Compounding Engineering Loop

Dan Shipper (Every) describes **compounding engineering** as an AI-native way of building software where each shipped feature makes the next feature easier (not harder).

The loop: **Plan → Delegate → Assess → Codify**

(Also phrased as Plan → Work → Review → Compound in Every's write-up. "Codify" is the "Compound" step.)

## Core Idea

Treat process knowledge as a first-class artifact. The code is not the only output—your prompts, templates, checks, and conventions should improve with every iteration.

**Heuristic**: If you did not codify, you only shipped code once. If you codify, you shipped capability.

## The Loop

### 1. Plan

Create a plan detailed enough that an agent can execute it:
- Goal, scope, non-goals
- Constraints (security, performance, UX, compatibility)
- Acceptance criteria (definition of done)
- Where to change things (files/components) and repo conventions
- Test plan (what proves it works)

**Output**: a plan you can reuse as a template.

### 2. Delegate

Delegate execution to one or more agents:
- Implementation, refactors, investigations, tests, docs
- Keep tasks chunked into reviewable units (diff/PR-sized)

**Output**: code + tests + notes.

### 3. Assess

Verify correctness and fit:
- Run tests, lint/typecheck, build
- Manual product checks where needed
- Review against acceptance criteria
- Optional: agent-based review as a second pass

**Output**: confirmed result + a short list of issues/surprises.

### 4. Codify (the compounding step)

Do a short reflection and encode what you learned so the next cycle is faster and safer.

Codify into:
- Repo rules / agent instructions (how we do X here)
- Reusable prompts, slash commands, sub-agents
- Templates (plan template, PR template, investigation template)
- Guardrails (tests, linters, CI checks, invariants)
- "Known pitfalls" + how to detect them

**Output**: better defaults for both humans and agents.

## 5-Minute Codify Checklist

After shipping, answer and encode:

1. What confused the agent or us?
2. What instruction would have prevented the first mistake?
3. What automated check/test would catch this earlier next time?
4. What pattern/component/template should become the default?
5. Where should this live so it gets reused automatically? (rules, prompts, CI, docs)

---

## References

### Primary Sources (Shipper / Every)

- Shipper, Dan. ["Dispatch from the Future: building an AI-native Company"](https://www.youtube.com/watch?v=MGzymaYBiss). YouTube.
- Shipper, Dan. ["Compound Engineering: How Every Codes With Agents"](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents). Every.
- [compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin). GitHub, EveryInc.

### Related Prior Work

The Plan-Delegate-Assess-Codify pattern maps to established continuous improvement loops:

**PDCA / PDSA cycles** (Plan-Do-Check-Act / Plan-Do-Study-Act):
- [PDCA Cycle (Plan-Do-Check-Act)](https://asq.org/quality-resources/pdca-cycle). ASQ.
- [PDSA Cycle (Plan-Do-Study-Act)](https://deming.org/explore/pdsa/). Deming Institute.

Mapping: Plan ≈ Plan, Delegate/Work ≈ Do, Assess/Review ≈ Check/Study, Codify/Compound ≈ Act (standardize + feed learning forward).

**Agile retrospectives** ("inspect and adapt"):
- [The Scrum Guide](https://scrumguides.org/scrum-guide.html). Scrum Team events and adaptation.

**After Action Reviews** (structured learning after execution):
- [FM 7-0 Appendix K: After Action Reviews (AAR)](https://www.first.army.mil/Portals/102/FM%207-0%20Appendix%20K.pdf). U.S. Army.

**Improvement Kata** (scientific thinking as a practiced loop):
- Rother, Mike. [The Improvement Kata](https://www-personal.umich.edu/~mrother/The_Improvement_Kata.html).

