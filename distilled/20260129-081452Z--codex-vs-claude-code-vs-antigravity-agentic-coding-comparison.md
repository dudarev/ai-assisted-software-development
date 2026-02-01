---
title: "Codex vs Claude Code vs Antigravity – Agentic Coding Comparison"
source_url: "https://www.youtube.com/watch?v=xYFcJT9XOIk"
captured_at: "2026-01-29T08:14:52Z"
distilled_at: "2026-01-29T10:15:02+02:00"
raw_refs:
  - "[[raw/20260129-081452Z--codex-vs-claude-code-vs-antigravity-agentic-coding-comparison.md]]"
capture_type: youtube_transcript
status: draft
agent: antigravity
model: gemini-2.0-pro-exp-0211
confidence_notes: "Transcript names specific future/hypothetical models (Codex 5.2, Claude Opus 4.5, Gemini 3 Pro) which implies this content might be from a future timeline or a specific scenario enactment. Treated as factual within the context of the source."
tags: ["agentic-coding", "comparison", "codex", "claude-code", "antigravity", "game-dev", "vibe-coding"]
---

## Summary

In a head-to-head comparison, three advanced agentic coding systems—Codex (GPT-5.2), Claude Code (Opus 4.5), and Antigravity (Gemini 3 Pro)—are tasked with building a game for a custom arcade cabinet. The challenge involves using specific hardware controls (joystick, steering wheel) and a two-stage workflow: initial planning via web chat interfaces followed by autonomous execution. The results were mixed and generally disappointing compared to simpler workflows. Antigravity and Codex produced functional but basic games, while Claude Code attempted a more ambitious project in Godot that failed to map controls correctly. The experiment highlights the potential friction of complex agentic planning versus direct "vibe coding."

## Topics

- Introduction and challenge setup (Arcade cabinet game)
- Agent planning phase (Web interfaces)
- Execution phase: Codex (GPT-5.2 xHigh)
- Execution phase: Claude Code (Opus 4.5)
- Execution phase: Antigravity (Gemini 3 Pro)
- Comparative analysis of workflows
- Installation and testing of results
- Critique of "over-planning" vs. "vibe coding"
- Final results and disappointment

## Key points

- **Task Complexity:** Mapping custom hardware inputs (joystick, steering wheel) proved a significant differentiator. Python-based solutions (Antigravity/Codex) worked better for controls than the engine-based solution (Godot/Claude).
- **Antigravity (Gemini 3 Pro):**
    - Created "Bore Core" (tunnel shooter).
    - Used Python and Ursina engine.
    - Easiest to install and run.
    - Controls worked immediately, but had initial rendering issues (missing assets/shapes).
- **Codex (GPT-5.2 xHigh):**
    - Created a "neon drift racer".
    - Controls worked correctly.
    - Low-poly aesthetic was functional but underwhelming ("not what I hoped to see").
- **Claude Code (Opus 4.5):**
    - Most ambitious technical choice: Godot Game Engine.
    - Visually most promising ("Steel Thunder" tank game).
    - **Failure:** Controls did not map correctly, making the game unplayable despite the visuals.
- **Workflow Insight:** The elaborate "plan then build" workflow initially seemed robust but yielded worse results than previous, more casual "vibe coding" sessions (e.g., with GLM 4.7 Flash).
- **Dependencies:** Claude Code's choice of Godot introduced an installation step, though it was noted as surprisingly easy on Ubuntu.

## Concepts / principles

**Agentic Over-Engineering**
The video suggests that formalizing the process with distinct "planning" and "building" phases for creative tasks ("vibe coding") might stifle the output. A direct, iterative prompt often yields better "vibes" and immediate results than a heavy architectural plan.

**Hardware Hallucination/DRI (Directly Responsible Individual)**
Agents struggle with hardware integration when they cannot close the feedback loop. Without being able to press the buttons and see the log, they rely on theoretical mapping, which failed in the Godot instance.

## Entities

- **Tools:**
    - **Codex (GPT-5.2 xHigh):** OpenAI's coding agent model.
    - **Claude Code (Opus 4.5):** Anthropic's agentic coding tool.
    - **Antigravity (Gemini 3 Pro):** Google's agentic coding environment (with UI).
    - **Godot:** Open-source game engine chosen by Claude.
    - **Ursina:** Python game engine library used by Antigravity.
- **Hardware:**
    - Custom Arcade Cabinet (Steering wheel, joystick, buttons).

## Quotes

> "I almost feel like if I just prompted them and said here's a file that maps the controls... Make me a 3D low poly highway racer. We probably would have received a better result."

> "Basically, it's missing shapes and things that would make this game not look like a 2D piece of garbage." — *On Antigravity's initial result*

> "I can now say that I have used Godot because that was probably one of the simplest application installs that I've seen on Ubuntu."

> "So, I was kind of anticipating more of what we just saw instead of the three very unique results we received today. I don't know what to do. I basically hate all of these results so much that I don't even want to spend time trying to make them better."

## Open questions / follow-ups

- Does the "planning" phase reduce creativity by locking agents into a spec before they encounter implementation reality?
- How can agents be given better access to hardware states for debugging custom peripherals?

## Next steps

- Explore "vibe coding" workflows that skip formal planning in favor of rapid iteration.
- Investigate best practices for agents using complex engines like Godot (e.g., providing better initial context for input mapping).
