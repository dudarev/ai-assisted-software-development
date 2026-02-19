---
title: Claude Code
tags:
  - tool
  - agentic-coding
  - anthropic
  - publish
summary: Anthropic's terminal-based agentic coding tool that operates through the command line, capable of reading codebases, running commands, browsing the web, and iteratively completing complex software tasks.
status: published
---

# Claude Code

**Claude Code** is Anthropic's terminal-first agentic coding assistant. Unlike IDE plugins or chat-based assistants, it runs in the terminal with direct access to the file system, shell commands, and browser—operating more like a **collaborating developer** than an autocomplete tool.

> "People are opening the IDE only 5% of the time anymore and all the changes are made within your CLI." — Andrej Karpathy

## What it is

Often described as a "coding agent," Claude Code is better understood as **Terminal 2.0** ([@denissexy](https://t.me/denissexy/11114)): the terminal interface for anything that runs in a shell, not just code. It can:

- Read, write, and refactor code across an entire codebase
- Run shell commands, tests, build tools, and migrations
- Browse the web and read documentation
- Connect to a live Chrome browser session (`--chrome` flag) to inspect and manipulate running UIs
- Install and use **skills** (plugins) that extend its capabilities

## Key capabilities

**Configuration over generation**: The biggest insight from experienced users (Arvid Kahl, Uncle Bob) is that the value of Claude Code comes not from raw code generation but from *how you configure and constrain it* — system prompts, permissions, loops, and browser access.

> "Most of the value of Claude Code is in the code it doesn't generate, so you don't have to throw it away." — Arvid Kahl

**The Chrome integration**: Connecting Claude Code to a live browser with `--chrome` allows it to visually inspect apps, fix display bugs by taking screenshots, and manipulate the DOM — replacing guesswork with direct observation.

**Permission system (`allow`/`deny`)**: Commands can be explicitly allowed (to run without confirmation) or denied (to block dangerous operations like database wipes). Careful permission management is what makes long, unattended runs viable.

**Skills/Plugins**: Claude Code has an official plugin marketplace (`/plugin`). Skills let you extend Claude's capabilities modularly—loading domain-specific knowledge only when needed, preserving context.

**`CLAUDE.md` / project memory**: A special markdown file in the project root that functions as the agent's persistent context — goals, architecture, constraints, and pointers to deeper docs.

## How it's used in practice

- **[[Ralph Wiggum Loop – January 2026 Snapshot|Ralph Wiggum Loop]]**: The dominant pattern for autonomous operation — a stop-hook plugin that keeps Claude iterating until a completion promise is satisfied.
- **System prompt layering**: Start with a quality-oriented base prompt (e.g., the Oxer prompt), then add project context (product description + ideal user).
- **Feature-first, tests-second**: Build the feature shape first; then have Claude write tests. Going test-first creates interference loops.
- **Multi-agent via git worktrees**: Run parallel Claude Code sessions on separate branches, then merge.

## Risks and limitations

- **[[Comprehension Debt]]**: Claude builds a transient theory of the code for each session and discards it completely on exit. The human must serve as the persistent "theory anchor."
- **Context rot**: Performance degrades as the context window fills. Explicit context hygiene (compaction, handoffs, `CLAUDE.md` management) is needed for long sessions.
- **Permission circumvention**: Claude may try to bypass denied commands by wrapping them in scripts — the allow/deny system requires careful design.
- **Rapidly evolving**: Claude Code releases new versions every few days; rules and workflows may need frequent updates.

## Related concepts

- [[Agentic Coding]]
- [[Ralph Wiggum Loop – January 2026 Snapshot|Ralph Wiggum Loop]]
- [[Comprehension Debt]]
- [[Context Hygiene]]
- [[Spec-Driven Development]]
- [[Agent Memory Systems]]
- [[Sandboxing AI Agents]]

## References

- [Claude Code product page](https://claude.com/product/claude-code)
- [Arvid Kahl – "How to Actually Use Claude Code to Build Serious Software"](https://www.youtube.com/watch?v=0eI1NgXWxA0) (Feb 2026)
- [@denissexy – "Claude Code as Terminal 2.0"](https://t.me/denissexy/11114) (Jan 2026)
- [Sankalp – "A Guide to Claude Code 2.0"](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)