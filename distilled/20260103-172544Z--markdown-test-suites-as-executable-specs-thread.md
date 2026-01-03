---
title: "Markdown test suites as executable specs (thread by @charliermarsh)"
source_url: "https://x.com/charliermarsh/status/2007117912801427905"
captured_at: "2026-01-03T17:25:44Z"
distilled_at: "2026-01-03T17:28:21Z"
raw_refs:
  - "[[raw/2026-01-03T192544+0200 - Thread by @charliermarsh]]"
capture_type: tweet_thread
status: draft
agent: codex
model: gpt-5.2
confidence_notes: "Thread capture appears partial and references a screenshot without transcribed content; numeric claims (e.g., pass rate) are attributed to replies and not verified."
tags: ["testing", "executable-specs", "markdown", "agentic-coding", "documentation", "literate-programming"]
---

## Summary

This thread highlights a pattern where a project’s test suite is “written” in **Markdown**: fenced code blocks are executed, and surrounding text/comments act as the expected behavior. The result is a corpus of executable examples that doubles as documentation—useful for humans reading intent and for coding agents (e.g., Claude Code) inferring how the system should behave. A related idea (via Simon Willison) is that sufficiently comprehensive, language-independent, data-driven tests can let an agent build a conforming implementation from scratch in a new language. Replies compare the approach to literate programming and BDD/Cucumber, and surface a key trade-off: readability and agent-alignment vs. the risks of encoding “assertions” in informal comments.

## Key points

- Markdown-first tests can act as executable documentation: examples + expectations in one place.
- A large suite of readable examples can function like project-specific “skills” for agents: a behavioral map, not just regressions.
- Data-driven, language-independent test corpora can support “re-implement from spec” workflows (if coverage is strong).
- The same format can serve two audiences: humans (narrative context) and machines (executable checks).
- “Comments as expectations” is powerful but controversial: it blurs spec text and assertion semantics.
- The approach invites a documentation rethink: prompts/specs that are also runnable.
- Tooling matters: ergonomics for authoring, diffing, failure output, and local execution determine whether it scales.

## Concepts / principles

**Executable specs as the canonical behavior contract**: treat the most trusted description of behavior as runnable examples, not prose-only documentation.

**Dual-audience artifacts**: write tests so they remain legible to humans while also being structured enough for agents and harnesses to execute deterministically.

**Spec as training data (within a repo)**: a rich test corpus becomes the “ground truth” that steers agent edits and reduces ambiguity during refactors and feature work.

**Language independence via examples**: when tests describe inputs/outputs and edge cases cleanly, they can outlive (or transcend) any single implementation language.

## Patterns

**Markdown-based test suite**
- Put each scenario in a Markdown file with fenced code blocks.
- Execute each block in a harness and interpret adjacent annotations as expectations.
- Organize files so they read like narrative documentation of behavior and edge cases.

**Documentation-driven coverage growth**
- Add a new Markdown scenario when documenting a behavior change.
- Use the same file as both: “what should happen” and “the regression that enforces it”.

## Entities

- People: Charlie Marsh (@charliermarsh), Simon Willison (@simonw), banteg (@banteg)
- Projects/tools mentioned: Claude Code, Codex (in reply), Cucumber, BDD, Prettier, Jinja
- Project referenced: “ty” (described as having a Markdown-driven test suite; exact scope/context not fully captured)

## Quotes

> "The ty test suite is \"written\" in Markdown. Every code block here gets evaluated, with the comments representing expectations."

> "We have almost 300 of these files that effectively read as detailed documentation for how ty behaves and how the Python typing spec and runtime work."

> "I'm slightly obsessed with language-independent data-driven test suites right now, because it turns out if they are comprehensive enough you can have a coding agent build a conforming implementation from scratch in any programming language you like"
>
> — Simon Willison

> "the markdown-as-tests pattern is sneaky powerful for AI - you're basically writing prompts that happen to also be executable specs."

## Open questions / follow-ups

- What’s the best way to make “comment expectations” precise (assertion syntax, tooling, failure messages) without losing readability?
- How should these suites be structured to stay language-independent (especially around runtime-dependent behavior)?
- Where does this approach break down (performance tests, nondeterminism, multi-process behavior, complex fixtures)?
- What conventions most help agents: file naming, section structure, canonical phrasing, or standardized annotation formats?

## Next steps

- Consider a note on “executable specs as prompts” and how test suites can double as agent steering artifacts.
- Compare this pattern with BDD/Cucumber and snapshot testing: what’s gained/lost in precision vs. readability?
- Capture a lightweight checklist for authoring Markdown tests (structure, assertion conventions, minimal fixtures, deterministic outputs).

## Links

- source: https://x.com/charliermarsh/status/2007117912801427905
