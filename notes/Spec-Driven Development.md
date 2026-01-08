---
title: Spec-Driven Development
tags:
  - concept
  - specification
  - workflow
  - agentic-coding
  - publish
summary: A development methodology where high-level technical specifications, rather than manual code entry, serve as the primary driver for implementation by AI agents.
status: published
---
# Spec-Driven Development

**Spec-Driven Development (SDD)** is a workflow pattern where the developer's primary role shifts from writing implementation logic to defining, refining, and verifying technical specifications. In this model, the "source of truth" for a feature is a structured document (the spec) that an AI agent uses as its execution plan.

## Core concept

As AI models become more capable of autonomous execution, the bottleneck in software development shifts from **typing speed** to **clarity of intent**. SDD decouples "what to build" (human-led) from "how to build it" (agent-led).

![[Spec-Driven Development.svg]]

1.  **Specification**: The human defines the requirements, architecture, and success criteria in a technical specification document (e.g., `SPEC.md`), often using AI help to make sure the document is clear and complete.
2.  **Execution**: An AI agent reads the spec and implements the changes across the codebase.
3.  **Verification**: The human (or specialized sub-agents) verifies the implementation against the original spec using tests, visual reviews, or logs.

## Why it matters

-   **Reduces Mental Energy**: Developers focus on high-level system thinking rather than details of syntax and boilerplate.
-   **Enables Parallelism**: Clear specs allow multiple agents to work on different parts of a system simultaneously without goal drift.
-   **Self-Documenting**: The spec remains as a permanent record of *why* decisions were made, making future maintenance easier.
-   **Tool Portability**: A well-written spec can be handed to different models or agents (Claude, Gemini, GPT) to see which implementation is superior.

## Related Patterns & Techniques

- [[Interview-Driven Specification]]: Using an AI agent to "interview" you to extract the necessary details for a complete spec.
- **Burn and Rebuild**: If a part of the codebase is too messy for an agent to fix, use SDD to describe the desired state and have the agent rewrite the module from scratch. Often triggered when the system passes a certain [[Rebuild Threshold]].
- **Executable Specs**: Writing expectations directly into the spec so that the agent can self-verify its work.

## References

- Chip Huyen, [**"Coding with AI"**](https://www.youtube.com/watch?v=xY1FcjIbErQ) (2025)  
  *Highlights the shift from AI as an IDE assistant to autonomous agents. Introduces **Interruption Rate** as the key metric: the goal of SDD is to minimize human intervention during the "execution" phase.*

- Sankalp, [**"Claude Code 2.0 & Knowledge Extraction"**](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/) (2025)  
  *Discusses specialized sub-agents like **Explore** (for discovery) and **Plan** (for architecture). Emphasizes that "Context Engineering" is the primary skill of the SDD era.*

- Charlie Marsh, [**"Markdown test suites as executable specs"**](https://x.com/charliermarsh/status/2007117912801427905) (2025)  
  *Presents a pattern where Markdown files containing code blocks and comments act as both documentation and the test suite. This makes the spec "executable" and prevents it from going stale.*