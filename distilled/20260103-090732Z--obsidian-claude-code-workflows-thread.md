---
title: Obsidian + Claude Code workflows (thread by @kepano)
source_url: https://x.com/kepano/status/2007223691315499199
captured_at: 2026-01-03T09:07:32Z
distilled_at: 2026-01-03T09:15:59Z
raw_refs:
  - "[[raw/2026-01-03T110732+0200 - Thread by @kepano]]"
capture_type: tweet_thread
status: expressed
agent: codex
model: gpt-5.2
confidence_notes: Captured thread excerpt appears partial (ends mid-conversation); quotes are limited to what’s present in raw.
tags:
  - obsidian
  - claude-code
  - note-taking
  - workflows
  - context-management
  - publishing
---

## Summary

In this thread, **@kepano** asks how people use **Obsidian with Claude Code**, and what they use it for. Replies emphasize practical “vault maintenance” work (backlinks, re-organization, mass metadata edits), and using the vault as a set of reusable **context files** to avoid re-explaining projects. A related tangent highlights the value of converting web pages to Markdown *before* sending them to LLMs (token efficiency + speed), with a note that rules-based conversion beats LLM-based HTML→MD. The thread also restates an Obsidian-aligned premise: plain-text local notes keep data in your control, and let you pick best-in-class AI tools (or none) rather than being locked into cloud-app “built-in agents.”

## Key points

- People use Claude Code + Obsidian for: goal review, trend finding across years, and planning.
- Reusable “master context” files in the vault are passed into Claude Code to reduce repeated explanations.
- Vault maintenance tasks show up repeatedly: backlinks you missed, batch metadata edits, re-organization.
- Web clipping to Markdown is used as a pre-processing step before LLMs to reduce token usage.
- Rules-based HTML→Markdown conversion is described as faster/less wasteful than doing it via an LLM.
- A broader claim: plain-text notes preserve tool choice, privacy options, and reduce “AI buttons everywhere.”

## Concepts / principles

**Vault as an interface**: treating the Obsidian vault (plain text) as the stable substrate, and swapping AI tools around it.

**Reusable context artifacts**: maintaining context files per project/area and reusing them as “inputs” to agentic tools.

**Maintenance leverage**: using AI for high-friction chores (metadata normalization, backlinking, re-org) where automation compounds.

**Pre-processing over tokens**: converting sources to clean Markdown *before* sending them to LLMs to save tokens and time.

## Entities

- People: @kepano, @internetvin, @belindmo, @davidhoang, @jmduke, @DontFearAI, @nexo_v1
- Tools: Obsidian, Claude Code, Obsidian Web Clipper, Defuddle
- Related: “agent sdk” (mentioned), an Obsidian + Claude Code integration plugin (linked in thread)

## Quotes

> "if you're using Obsidian with Claude Code, tell me about your workflow, and what you've used it for"

> "I have started maintaining specific master context files in Obsidian that I repeatedly pass into Claude Code instead of explaining things repeatedly."

> "MD files use way less tokens versus having Claude fetch the websites."

> "LLMs are incredibly slow and wasteful for converting HTML to Markdown, compared to the rules-based approach of Defuddle (the underlying library I built for Obsidian Well Clipper)"

> "AI agents built into cloud apps will always be sub-par compared to state of the art agents that you can use with Obsidian."

## Reply

https://x.com/dudarev/status/2007388736812921290

For example, I use them to learn in public about AI-assisted software development - I keep notes about patterns, principles and workflows at https://ai-assisted-software-development.com

When I want "agentic" help (reviewing notes, summarizing, reorganizing), I point Claude Code (or other tools) at the vault - it's plain text. I also keep reusable Agent Skills so I can reuse the same workflows across different harnesses, not only Claude Code.

I try to stay tool-flexible: Obsidian ↔ Foam + Copilot (VS Code), Claude Code ↔ Codex - whichever fits the task best

The pipeline is basically CODE (Capture → Organize → Distill → Express) from Tiago Forte (@fortelabs)

For capturing, Obsidian Web Clipper is great for pulling web pages into clean Markdown first - many thanks for it!

Publishing: notes live in https://github.com/dudarev/ai-assisted-software-development and the site build/publish pipeline lives in the sister “site” repo https://github.com/dudarev/ai-assisted-software-development-com


## Links

- source: https://x.com/kepano/status/2007223691315499199
