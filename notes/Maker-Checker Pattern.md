---
title: Maker-Checker Pattern
status: ideation
tags:
  - review
  - four-eyes
  - segregation-of-duties
  - agentic-workflows
  - guardrails
  - publish
summary: A workflow where an AI “maker” proposes changes and a human “checker” verifies them with tests, review, and explicit approval.
---
# Maker-Checker Pattern

The **Maker-Checker pattern** (derived from the financial "Four Eyes" principle) is a primary operational model for reliable AI-assisted software development.

> **Definition:** Maker–checker (or Maker and Checker or 4-Eyes) is one of the central principles of authorization in the information systems of financial organizations. The principle of maker and checker means that, for each transaction, there must be at least two individuals necessary for its completion. While one individual may create a transaction, the other individual should be involved in confirmation/authorization of the same. ([Wikipedia](https://en.wikipedia.org/wiki/Maker-checker))

In the context of AI-assisted development, this principle is adapted such that an AI agent acts as the **Maker** (proposing changes, writing code, or suggesting architectures), while a human expert acts as the **Checker** (validating, reviewing, and approving).

## Core Dynamics

- **AI as the Maker:** The agent leverages its ability to generate high volumes of technical output at "inference speed." It handles the administrative and repetitive tasks of coding, allowing for rapid exploration of solutions.
- **Human as the Checker:** The human developer shifts focus from *implementation* to *curation and verification*. Their primary responsibility is to ensure quality, and guard against low-signal output (“slop”).

## Prerequisites for Success

For the Maker-Checker loop to function without becoming a bottleneck or a safety risk, several structures must be in place:

1.  **Shift-Left Security & Quality:** Guardrails (automated test suites, security scanners, and style checkers) must be integrated into the loop *before* the agent starts making changes. If the "Checker" has to manually verify every line of code without automated aid, the speed gains of the "Maker" are neutralized by the review bottleneck.
2.  **Modular Context Management:** The Maker needs clear, scoped instructions (e.g., `Cursor Rules`, `Claude memory`) to produce high-confidence suggestions.
3.  **The "New Teammate" Mindset:** Treating the AI as a collaborative partner with "anterograde amnesia" requires the Checker to actively manage the agent's context and "working memory."

## Checker Protocol (Practical)

When the Maker is generating patches fast, the Checker needs a repeatable protocol:

- **Constrain scope:** Keep diffs small; prefer one intent per change.
- **Require evidence:** Ask for exact test/lint outputs, logs, and repro steps.
- **Read the diff like risk:** Focus on boundaries, invariants, and failure modes—not line count.
- **Prefer automation:** Push as much checking as possible into runnable guardrails.
- **Escalate early:** If verification exceeds implementation effort, rebuild or restart.

## Evolutionary Path: The Solution Consultant

The Maker-Checker pattern enables the emergence of the **Solution Consultant**—a high-agency generalist who can handle the entire software delivery lifecycle (analysis, design, implementation, and deployment) by orchestrating multiple AI agents as "Makers" while they maintain the "Checker" role across the whole stack.

## Trade-offs and Risks

- **Intellectual Laziness:** There is a constant risk that the Checker becomes fatigued or over-confident in the Maker's output, leading to a breakdown in critical thinking.
- **The Review Bottleneck:** If the Maker generates code ~10x faster than before, the human Checker must adopt "Parallel Review" patterns or rely more heavily on [[agentic-harness|Agentic Harnesses]] to assist in checking.
- **Verification vs. Implementation:** As tools improve, the effort required to *verify* a solution can sometimes exceed the effort it would have taken to *implement* it manually, specifically in complex or subtle logic.

## The Confidence Gap

As implementation gets delegated, confidence shifts from authorship (“I wrote this”) to validation (“I can show this works”).

- The Checker didn’t “live through” the edge cases while writing, so mental models are weaker by default.
- The practical mitigation is to tighten the loop: smaller changes, stronger specs, more executable checks, and better observability.

## Related Concepts

- [[Vibe Coding Is FAAFO|Vibe Coding]] – The high-level, intent-driven mode of the Maker role.
- [[Spec-Driven Development]] – Converting intent into a checkable contract before implementation.
- [[Executable Specs]] – Turning requirements into runnable tests.
- [[Three Developer Loops of Vibe Coding]] – Selecting practices based on the feedback-loop timescale.
- [[Orchestrator vs. Executor]] – A framing for how the human role shifts as implementation becomes cheaper.

## Sources and Observations

- **[Maker-checker - Wikipedia](https://en.wikipedia.org/wiki/Maker-checker)** – The original financial principle involving the segregation of duties and the "4-Eyes" principle.
- **[Thread by @ctatedev (X.com)](https://x.com/ctatedev/status/2007338520395039197)** – Discusses the "unreal" productivity leap in early 2026. *Observation:* A widening performance gap between "Copilot users" and those "pair programming with agents running commands." The latter moves 3x faster, fundamentally shifting the human's role toward high-level orchestration.
- **[Patterns for AI assisted software development (Karun Japhet)](https://dev.to/javatarz/patterns-for-ai-assisted-software-development-4ga2)** – Explicitly introduces the "Maker-Checker" term in the context of AI-generated guardrails. *Observation:* Even when AI plans and creates guardrails, they must be "thoroughly reviewed by someone who has expertise... to catch the small bugs that can have disastrous consequences."
- **[How AI will change software engineering (Martin Fowler)](https://www.youtube.com/watch?v=CQmI4XKTa0U)** – Highlights the risk of breaking the "learning loop." *Observation:* Treat AI-generated code like a PR from a "dodgy collaborator" who is highly productive but untrustworthy. The human "Checker" must prevent "vibe coding" from becoming "blind acceptance."
- **[The Value Of Vibe Coding (Gene Kim & Steve Yegge)](https://itrevolution.com/articles/the-value-of-vibe-coding-or-the-good-faafo/)** – Explores the "independence of action." *Observation:* AI reduces the "mind-reading tax" often found in human-human collaboration. The Maker-Checker loop is most efficient when contained within a single high-agency individual (the "Solution Consultant").
