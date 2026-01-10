---
title: Tooling Chaos Monkey
tags:
  - tooling
  - chaos-engineering
  - developer-productivity
  - pattern
status: ideation
chats:
  - https://chatgpt.com/c/695bda6f-a844-832d-8b8b-96f9271d314e
  - https://chatgpt.com/c/695bd593-66f8-8327-b1c9-5a17d0e74dcb
  - https://chatgpt.com/c/695acb41-70e0-8333-ad08-551ec057556e
---
# Tooling Chaos Monkey

## The Concept
Applying the principles of Chaos Engineering to the developer toolchain. Just as Netflix's Chaos Monkey randomly terminates instances to ensure system resilience, a **Tooling Chaos Monkey** involves intentionally and regularly disrupting your own development environment—disabling or swapping out key tools—to ensure workflow independence and adaptability.

## Why Do It?
1.  **Prevent Lock-in**: Deep reliance on a specific tool (e.g., a specific AI coding assistant's proprietary features) creates a vulnerability. If that tool changes pricing, disappears, or degrades, your productivity shouldn't crash.
2.  **Accelerate Learning**: New tools often introduce new paradigms. Regularly switching (e.g., from VS Code to Zed, or Copilot to Claude Sonnet) forces you to learn new capabilities and keeps your "tool plasticity" high.
3.  **Validate Workflow Robustness**: If your workflow breaks because you can't use a specific button in a specific IDE, your workflow is fragile. True productivity comes from patterns that transcend tools.

## Implementation: The "Break One Tool" Drill
Regularly (e.g., once a sprint or simply "on Tuesdays"), simulate a failure of a primary tool:
*   **"No IDE Day"**: Can you survive with just Vim/Neovim or a basic text editor?
*   **"Model Swap"**: Forbid your "daily driver" LLM (e.g., GPT-4o) and force yourself to use a competitor (e.g., DeepSeek or Claude). See [[Discovering New AI Tools]] for how to find new candidates.
*   **"Terminal Only"**: If you rely on a Git GUI, try a week of CLI only.

## Core Principle: Tool-Independent Workflows
**The workflow is the asset; the tool is just the implement.**

*   **Pattern Over Product**: Define your work in terms of patterns (e.g., "Agentic Forking," "Distillation," "TDD") rather than tool features.
*   **Portable Artifacts**: Prefer standard formats (Markdown, shell scripts, standard config files) over tool-specific metadata.
*   **Universal Skills**: Invest in skills that work everywhere (Regular Expressions, Vim motions, CLI proficiency, Prompting logic) rather than memorizing proprietary shortcuts.

## The Goal
To cultivate a development practice where the engineer is the master of the craft, capable of picking up any reasonable set of tools and becoming productive immediately. The tools serve the workflow, not the other way around.
