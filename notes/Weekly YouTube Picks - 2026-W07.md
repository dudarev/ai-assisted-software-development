---
title: Weekly YouTube Picks (2026-W07)
tags:
  - weekly
  - youtube
  - agentic-workflows
  - publish
status: draft
note: This week's picks focus on "skills-in-the-middle" (skills as docs), guardrailed agent loops, and shipping with evals.
---
# Weekly YouTube Picks (2026-W07)

This week's picks share a throughline: the shift from "vibe-driven" AI use toward deliberate engineering discipline — guardrailed loops, skills-as-docs, evals as acceptance criteria, and context loaded with intent.

*   **[AI Updates Weekly — February 16, 2026 (Lev Selector)](https://www.youtube.com/watch?v=GsHA0eAcmaI)** — "Skills-in-the-middle" reframes app development: move middle-layer logic out of hard-coded decision trees and into auditable Markdown skill files. The catch is governance: skills become a supply-chain problem — enable least-privilege, review what any skill can touch, and anticipate needing a "skills security officer" before long. The tagline says it all: *"You are becoming a skills developer, not a software developer."*

*   **[You are Not Ready: Agentic coding in 2026](https://www.youtube.com/watch?v=6W_-YWHKwZ4)** — A clear maturity ladder for agentic coding: chat → IDE suggestions → in-the-loop agentic (babysitting, learning failure modes) → out-of-the-loop (spec → delegate → verify) → multi-agent orchestration. The core pitch: you don't need AGI, you need *persistence + verification* — a guardrailed loop that runs tools, checks deterministically, and retries. Don't jump to multi-agent until you can reliably pass a [[Maker-Checker Pattern|checker]]; skipping stages just amplifies risk.

*   **[The senior engineer's guide to AI coding: Context loading, custom hooks, and automation](https://www.youtube.com/watch?v=LvLdNkgO-N0)** — Three reliability levers: (1) preload high-signal context (Mermaid diagrams beat rule lists — they give the agent a "flow map" of the system); (2) encode recurring prompts as aliases/CLIs so the workflow is repeatable; (3) add stop hooks that run typecheck/lint after the agent finishes and re-feed failures until it's actually shippable. "Done" should mean "validated." And if the conversation drifts: export it, get a second-model critique, reset and restart.

*   **[DIY dev tools: How this engineer created "Flowy" to visualize his plans and accelerate coding](https://www.youtube.com/watch?v=LC1mKvLWZ2E)** — An "artifacts over vibes" story: plans, flowcharts, and mockups become editable JSON that both the human and the model can read and write back to — a shared intermediate language. Skills become the place you codify what worked so the next run starts smarter, not from scratch. Bonus: a second model in "staff engineer reviewer" mode diffs the implementation against the plan artifact, catching mismatches and smells the primary agent missed.

*   **[435: How to Actually Use Claude Code to Build Serious Software](https://www.youtube.com/watch?v=0eI1NgXWxA0)** — The headline move: make the agent *see* the running app (browser-in-the-loop via a Chrome bridge) so it stops guessing on UI work. Pair that with strict allow/deny permissions (deny database-wiping commands; watch for scripts that bypass denials) and a completion-promise loop that keeps iterating until checks pass. Most of the value is in "the code it doesn't generate so you don't have to throw it away."

*   **[Shipping AI That Works: An Evaluation Framework for PMs (Distilled)](https://www.youtube.com/watch?v=2HNSG990Ew8)** — "Vibes" don't scale. Treat evals like tests for non-deterministic systems: collect representative examples, run A/B experiments over a dataset, use a judge/human calibration loop. The minimum viable eval loop is 10–50 examples, 2–4 discrete labels, and a calibration pass against human raters. The punchline: ship features with evals as acceptance criteria, not a PRD that vanishes after kickoff.

*   **[Context Engineering: Connecting the Dots with Graphs — Stephen Chin (Neo4j)](https://www.youtube.com/watch?v=LLuKshphGOE)** — Prompts aren't the whole game. Context engineering is a pipeline: instruction prompts + retrieval + memory + structured outputs. GraphRAG earns its complexity when you need multi-hop answers (people ↔ events ↔ artifacts) and inspectable evidence — you can see which subgraph was retrieved and layer access control before anything hits the model. Ties naturally to [[Agent Memory Systems]].

*   **[Why maintaining a codebase is so damn hard – with Oh My Zsh creator Robby Russell (Podcast #207)](https://www.youtube.com/watch?v=cjam-BWAaL8)** — Rewrites often delete hidden knowledge baked into existing systems by years of incidents; the *promise* of a rewrite also demotivates tending today's code. Guardrails added after incidents have a half-life — periodically prune what no longer pays its cycle-time cost. Keep diffs small (AI-assisted or not) so review stays possible. Useful framing: "How long for a typo to reach production?" — that number exposes your real workflow drag.

## Related Notes

*   [[Agentic Harness]]
*   [[Spec-Driven Development]]
*   [[Separate Discovery from Delivery]]
*   [[Context Hygiene]]
*   [[Maker-Checker Pattern]]
*   [[Sandboxing AI Agents]]
*   [[Agent Memory Systems]]
