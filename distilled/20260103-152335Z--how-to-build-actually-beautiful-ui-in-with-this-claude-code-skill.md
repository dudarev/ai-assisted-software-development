---
title: How to Build ACTUALLY Beautiful UI in With This Claude Code Skill
source_url: https://www.youtube.com/watch?v=95_NJ-a-CMQ
captured_at: 2026-01-03T15:23:35Z
distilled_at: 2026-01-03T15:33:36Z
raw_refs:
  - "[[raw/20260103-152335Z--how-to-build-actually-beautiful-ui-in-with-this-claude-code-skill]]"
capture_type: youtube_transcript
status: draft
agent: codex
model: gpt-5.2
confidence_notes: Transcript-derived; the “plugin marketplace” and “front-end design skill” installation commands are copied from the transcript and may be version-sensitive.
tags:
  - agent-instructions
  - design-systems
  - frontend
  - prompting
  - ux-ui
---

## Summary

A walkthrough of a Claude Code “front-end design skill” plugin aimed at reducing the “generic AI UI” look. The demo compares (1) a baseline landing page generated from a functional prompt, (2) a redesign after invoking the skill with no additional guidance, and (3) a second redesign after providing a visual reference (a Dribbble screenshot). The main claim is that specialized instructions + critique patterns inside a skill can push UI output closer to “designerly defaults”, but the results still benefit from human review (CTA emphasis, layout consistency, broken sections/icons).

## Key points

- Setup: add the Claude Code plugin marketplace, then install a “front-end design” plugin/skill.
- Workflow: build a baseline UI first, then ask the agent to “use the front-end design skill” to redesign.
- Without a reference image, the skill improves typography, spacing, consistency, hover/scroll animations, and color discipline (e.g., black/white + one accent).
- The redesign can still miss UX priorities (e.g., primary CTA not prominent) and can produce uneven sections.
- With a reference screenshot, the agent shifts style more aggressively to match the reference (rounded corners, soft gradients/shadows, smoother motion).
- A design system (tokens/components) is suggested as a next level to improve consistency and reduce regressions across sections.

## Concepts / principles

**Skill as “opinionated review loop”**: a plugin can encode critique heuristics (contrast, hierarchy, spacing rhythm, interaction polish) that are hard to evoke reliably with one-off prompts.

**Baseline → transform**: generating a usable baseline quickly, then iterating with a specialized “redesign pass”, mirrors real design workflows (rough draft → critique → refine).

**Reference-guided generation**: attaching a screenshot turns “make it nicer” into “match this style”, which often increases coherence (but can introduce mismatches like inappropriate icons).

**Design systems as constraints**: once a direction is chosen, a design system can keep future agent changes consistent across the page/app.

## Patterns

**Two-pass UI generation**
- Pass 1: generate structure + copy (sections, CTA, proof points).
- Pass 2: invoke a design-focused skill to redesign and add interaction polish.

**Reference screenshot prompt**
- Provide a single strong reference.
- Ask for a style transfer, then review for UX breakage (contrast, responsiveness, icons, broken components).

**Triage after redesign**
- Identify “above the fold” conversion-critical issues first (primary CTA contrast, heading hierarchy).
- Then fix consistency issues (card layouts, section alignment, icon set).

## Entities

- Claude Code (tool)
- Plugin marketplace and plugin install commands (tooling surface; exact syntax may drift)
- Dribbble (source of visual references)

## Quotes

> “use the front-end design skill to improve the design of this landing page.”

> “This is better than 99% of… designs that you're going to get from other AI tools without using this front-end skill.”

> “You could create a design system… and then use Claude Code… to design your website following that framework.”

## Open questions / follow-ups

- What does the skill change concretely (prompt template, critique checklist, component library, CSS tokens), and can those ideas be applied without a plugin?
- How robust is the workflow across frameworks (React/Tailwind vs. plain HTML/CSS) and across multi-page apps?
- What review rubric works best for quickly catching “looks good but converts poorly” issues (CTA prominence, scanning order, trust cues)?

## Next steps

- Consider a note on “reference-guided UI iteration with coding agents” (when it works, where it breaks).
- Extract a lightweight “UI critique checklist” suitable for an `AGENTS.md`-style instruction file (hierarchy, contrast, spacing rhythm, interactive states).
- If you use a design system, capture the minimal set of tokens/components that keep agent output consistent (type scale, spacing scale, radii, shadow levels).
- Thoughts about using AI assistance for specifically UI design can be expressed in a separate note. 

## Links

- source: https://www.youtube.com/watch?v=95_NJ-a-CMQ
