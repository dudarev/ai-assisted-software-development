---
title: Executable Specs
tags:
  - specification
  - testing
  - documentation
  - agentic-coding
  - publish
status: draft
distilled:
  - "[[distilled/20260103-172544Z--markdown-test-suites-as-executable-specs-thread|20260103-172544Z--markdown-test-suites-as-executable-specs-thread]]"
---

# Executable Specs

Executable specs are **behavior descriptions that also run as tests**. Instead of treating documentation and tests as separate artifacts, the spec itself is executable, making it the most trusted source of truth for both humans and agents.

## Why it matters

- **Single source of truth:** the spec and the test are the same artifact, reducing drift.
- **Dual audience:** readable narratives for humans and deterministic checks for machines.
- **Agent steering:** a rich corpus of examples becomes the behavioral contract an agent can follow when implementing or refactoring.

## Common forms

- **Markdown-based test suites**: scenarios are written as text with fenced code blocks that a harness executes.
- **Data-driven specs**: inputs and expected outputs are expressed as fixtures with a thin runner.
- **Literate-style specs**: prose describes the intent; code blocks demonstrate behavior.

## Trade-offs and risks

- **Ambiguity risk**: if comments or prose stand in for assertions, behavior can be under-specified.
- **Tooling burden**: you need a runner that executes blocks, reports failures, and keeps the format pleasant to edit.
- **Coverage bias**: specs can emphasize readable cases and miss edge-case rigor.

## Design guidelines

- Keep scenarios small and focused; one behavior per block.
- Use explicit, machine-checkable assertions near the example.
- Make failure output tight and readable so the spec remains a usable debugging surface.
- Treat the spec as the contract for refactors: if the spec passes, the refactor is valid.

## Related notes

- [[Spec-Driven Development]]

## References

- Charlie Marsh, “Markdown test suites as executable specs” (thread). https://x.com/charliermarsh/status/2007117912801427905
- Simon Willison on language-independent test suites (quoted in the same thread). https://x.com/simonw
