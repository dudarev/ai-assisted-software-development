---
title: Executable Specs
tags:
  - specification
  - testing
  - documentation
  - agentic-coding
  - publish
summary: Behavior descriptions that double as runnable checks, turning the spec itself into a contract for humans and agents.
status: draft
aliases:
  - Executable Documentation
distilled_refs:
  - "[[distilled/20260103-172544Z--markdown-test-suites-as-executable-specs-thread|20260103-172544Z--markdown-test-suites-as-executable-specs-thread]]"
  - "[[distilled/20260114-214550Z--shaping-with-ai-requirements-vs-solutions-ryan-singer|20260114-214550Z--shaping-with-ai-requirements-vs-solutions-ryan-singer]]"
  - "[[distilled/2026-01-08T172359+0200 - Thread by @Shpigford|2026-01-08T172359+0200 - Thread by @Shpigford]]"
  - "[[distilled/20260219-072655Z--how-to-think-about-software-engineering-cto-s-perspective|20260219-072655Z--how-to-think-about-software-engineering-cto-s-perspective]]"
---

# Executable Specs

Executable specs are **behavior descriptions that also run as checks**. Instead of treating documentation and tests as separate artifacts, the same file becomes both explanation and proof. When that works well, the spec becomes the most trusted source of truth for humans and agents alike.

## Why it matters

Executable specs reduce drift because the most readable description of a system is also the thing that verifies behavior. They matter for three related reasons:

- They create a **single source of truth** for behavior instead of splitting intent across docs and tests.
- They serve a **dual audience**: readable enough for humans, strict enough for tools.
- They give agents a **behavioral contract** to follow during implementation, refactoring, or reimplementation.

In AI-assisted development, that dual role matters even more. A good spec corpus does not just catch regressions; it helps shape the work before code is even written.

## What makes a spec executable

A spec becomes executable when examples or scenarios are tied to machine-checkable assertions and a repeatable runner. Prose alone is not enough. The key property is that the same artifact can be read as an explanation and evaluated as a contract. If a scenario looks precise but nothing actually enforces it, it is documentation, not an executable spec.

## Common forms

Executable specs show up in several forms:

- **Markdown-based test suites** place narrative scenarios next to runnable code blocks.
- **Data-driven specs** express inputs and expected outputs in fixtures that can outlive any single implementation language.
- **Behavior-Driven Development (BDD)**, especially Gherkin/Cucumber-style scenarios, states behavior in business-readable language and makes it runnable through step definitions.
- **Literate-style specs** sit nearby, but they are only truly executable when the examples are enforced rather than merely illustrative.

## Executable Specs in AI Workflows

In AI-heavy workflows, executable specs do more than verify completed work. They help shape it. A Markdown test suite, a plain-English E2E check, or a requirements document backed by integration tests can all function as local, versioned behavioral contracts. That makes them useful steering artifacts for agents: they constrain generation, surface ambiguity earlier, and make it easier to trust implementations whose internal steps you did not personally trace. This is one reason repository-local specs, tests, and examples increasingly function as working memory and operational source of truth in agentic development.

## Trade-offs and risks

The main risk is false confidence. A spec can look authoritative while still failing in important ways:

- It can miss edge cases while still appearing complete.
- It can rely on comments or prose that no tool actually checks.
- Natural-language E2E specs can gain flexibility at the cost of determinism.
- BDD can drift into ceremony if the feature file stops being the real contract and the truth moves into opaque step definitions.

Executable specs are strongest when they stay close to observable behavior, fail clearly, and remain small enough to maintain.

## Design guidelines

Write scenarios around observable behavior rather than implementation details. In practice that usually means:

- keeping each example narrow,
- pairing it with explicit assertions,
- making failure output easy to scan,
- and preferring fixtures and examples that can survive implementation rewrites.

If a spec cannot tell you clearly why it failed, it is not yet doing enough work.

## Related notes

- [[Spec-Driven Development]]

## References

- Charlie Marsh, “Markdown test suites as executable specs” (thread). https://x.com/charliermarsh/status/2007117912801427905
- Simon Willison, “language-independent data-driven test suites” (post). https://x.com/simonw/status/2007133682008764853
- Ryan Singer, “Shaping with AI: Requirements vs. Solutions” (thread). https://x.com/rjs/status/2011522235266130087
- Josh Pigford, “plain English + Playwright E2E tests” (thread). https://x.com/Shpigford/status/2009087477013709093
- “How to Think About Software Engineering (CTO's Perspective)” (video). https://www.youtube.com/watch?v=KTt-_W0r1NQ
