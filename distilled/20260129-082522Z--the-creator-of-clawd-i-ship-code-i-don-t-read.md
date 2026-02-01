---
title: "The creator of Clawd: \"I ship code I don't read\""
author:
  - Antigravity
date: 2026-01-29
tags:
  - podcast
  - peter-steinberger
  - clawd
  - moltbot
  - pspdfkit
  - agentic-coding
  - testing
  - workflow
  - pragmatic-engineer
source: "[[raw/20260129-082522Z--the-creator-of-clawd-i-ship-code-i-don-t-read.md]]"
---

# The creator of Clawd: "I ship code I don't read"

## Summary
In this episode of The Pragmatic Engineer, Gergely Orosz interviews Peter Steinberger, founder of PSPDFKit and creator of Clawdbot (renamed to Moltbot). Peter discusses his return to software development after a 3-year hiatus, driven by the capabilities of AI agents. He outlines his "Agentic Engineering" workflow, where he manages 5-10 parallel agents acting as a "Builder" or architect rather than a traditional coder. Key themes include the necessity of "closing the loop" (agents testing their own work), the shift from creating code to "weaving" features, and his controversial stance on shipping code he hasn't read by relying on robust verification systems. He also details the architecture of Clawdbot, a hyper-personal local agent, and predicts a future where companies operate with significantly fewer, but higher-agency, engineers.

## Key Points
- **Agentic Engineering vs. Vibe Coding**: Peter distinguishes his professional workflow ("Agentic Engineering") from casual "Vibe Coding". He operates like a manager of multiple agents, paralyzing work across different "cooking" streams (like playing Starcraft or managing a kitchen).
- **Closing the Loop**: The most critical factor for success with AI agents is giving them the ability to verify their own work. This means agents must be able to run build scripts, tests, and debug errors ('CLIs over MCPs'). Verification replaces manual code reading.
- **"I Ship Code I Don't Read"**: Peter admits to not reading every line of AI-generated code. He focuses on system architecture and high-level structure ("weaving"), trusting the agent's output *if* it passes the "Gate" (linting, testing, building).
- **The End of Traditional PRs**: He suggests "Prompt Requests" are more valuable than Pull Requests. Understanding the prompt that generated the code is higher signal than the code diff itself. He often rewrites PRs by asking an agent to "weave this feature in" rather than manually merging.
- **Clawdbot (Moltbot)**: His current project is a personal agent that runs locally but has deep access to his digital life (WhatsApp, email, screen). It relies on a "heartbeat" to be proactive (e.g., waking him up) and uses a bootstrap file to define its "soul".
- **Tooling Preferences**:
    - **CLIs > MCPs**: Finds Command Line Interfaces superior to Model Context Protocols because they are composable (pipeable), keeping the context window clean compared to the JSON overhead of MCPs.
    - **Codex vs. Claude**: Uses Anthropic's Claude for conversation/speed but OpenAI's Codex (o1/o3 implied) for deep thinking/complex tasks that take longer ("cooking").
- **Future of Work**: Predicts companies could run with 30% of current staff. The new ideal engineer is high-agency, infinitely curious, and understands systems enough to delegate to AI, rather than just writing syntax.

## Concepts
- **Agentic Engineering**: A workflow where the developer acts as an architect/manager, dispatching tasks to multiple AI agents in parallel and focusing on system design and verification rather than writing code.
- **Closing the Loop**: The architectural principle where an AI agent has access to execution environments (terminal, browser) to run its code, observe errors, and iteratively fix them without human intervention.
- **Weaving**: The process of integrating a new feature or logic into an existing system's architecture. Peter prefers this term over "writing" or "merging" code.
- **Prompt Request**: A proposed alternative to Pull Requests where the submitter provides the prompt used to generate the solution, allowing the maintainer to regenerate or "weave" the solution using their own agentic workflow.
- **Full Gate**: A rigorous automated check (lint, build, test) that serves as the primary quality barrier, replacing manual code review for correctness.
- **Bootstrap File**: A temporary file used to initialize an agent's persona ("soul") and preferences, which is then converted into persistent memory files (identity.md, soul.md).

## Entities
- **Peter Steinberger**: Creator of PSPDFKit and Clawdbot/Moltbot.
- **Clawdbot (Moltbot)**: A hyper-personal, locally running AI agent/assistant.
- **PSPDFKit**: A PDF SDK company founded by Peter, known for high quality and polish.
- **Claude Code**: An agentic coding tool by Anthropic.
- **Codex**: References OpenAI's reasoning models (likely o1 series), used for complex, long-duration tasks.
- **Pi**: A "shitty" (affectionate) coding agent by Mario (friend/collaborator).
- **Gergely Orosz**: Host of The Pragmatic Engineer podcast.
- **Make-Porter**: A tool Peter built to convert MCPs into CLIs.

## Quotes
- "I ship code I don't read."
- "From the commits, it might appear like it's a company. But it’s not. This is one dude sitting at home having fun."
- "PRs should be called prompt requests."
- "Verification is the way to make things good."
- "I feel like a human merge button."
- "It’s like Starcraft, you have like your main base and you have like your side bases. They give you resources."
- "I don't care much about CI... I have local CI."
- "I write better code now that I don't write code myself anymore."
- "Those little models are ghosts of our collective human knowledge."
