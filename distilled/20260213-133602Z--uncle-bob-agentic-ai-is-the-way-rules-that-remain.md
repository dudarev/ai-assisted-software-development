---
title: "Uncle Bob: Agentic AI Is the Way — Rules That Remain"
source_url: "https://x.com/unclebobmartin/status/2021209931400040526"
captured_at: "2026-02-13"
distilled_at: "2026-02-13T11:40:24Z"
raw_refs:
  - "[[raw/2026-02-13T133602+0200 - Thread by @unclebobmartin.md]]"
capture_type: "Thread"
status: draft
agent: antigravity
model: claude-sonnet-4.6
confidence_notes: "Transcript is clear and complete. Thread replies are occasionally truncated by the capture tool (Twitter character limits). Some replies are tangential (dog comments, jokes)."
tags: ["uncle-bob", "agentic-coding", "testing", "clean-code", "context-management", "tdd", "bdd"]
---

## Transcript Summary (bullet points)

Uncle Bob's "morning bath robe rant" — a video monologue posted alongside the thread:

- **Agentic AI is the way** — DHH is right, the game has changed, and there is no doubt that agent-based AI coding is the future direction.
- **Most rules stay the same** — Some rules will change, but probably most will remain; the fundamentals of software engineering endure.
- **Testing is absolutely essential** — Not necessarily the three laws of TDD (which are a "human thing"), but having a suite of unit tests is critical because AI will do anything it wants if unconstrained.
- **Unit tests are insufficient** — An additional level of acceptance testing is needed (Gherkin, FitNesse, or similar) to provide a statement of facts that can drive the AI to repeatedly and repeatably create viable software.
- **Keep the code clean — for AI consumption** — Clean code still matters, but the audience shifts from humans to AI. Good names help the AI, short functions help the AI; most of the same rules apply.
- **Optimize for token management** — Use AI to refactor code so it can manage tokens well and delay context compressions; this is a new optimization target.
- **AI memory is fragile** — AIs have long short-term memories, but once blown, they get amnesia fast and often don't remember the right things.
- **Don't build lots of code without tests** — It will come back and bite you.
- **Don't let code pile up** — Keep it refactored. The AI gets just as confused as any human would with messy code.
- **Don't get bitter** — It's a new day, a little scary, but still good news. Take advantage of it.

## Summary

Uncle Bob Martin endorses DHH's stance that agentic AI coding is the new paradigm. In a video monologue and extended thread, he argues that while the development model is shifting, the core disciplines — testing, clean code, and refactoring — remain essential, just reframed for AI consumption. The key new concern is **token management**: code should be optimized so AI agents can work within context windows without losing critical information. He advocates for BDD/acceptance tests as the human-managed contract that keeps AI honest, since unit tests alone are insufficient and AI-generated tests often provide a false sense of coverage. The thread draws rich community discussion on abstraction layers for AI, functional paradigms, the "code as black box" risk, and practical experience reports from full-time agentic coding practitioners.

## Topics

- Endorsement of agentic AI as the future of coding
- Testing discipline: TDD vs. BDD vs. acceptance tests for AI
- Clean code reframed for AI readability / token efficiency
- AI context window management and "amnesia"
- Abstraction layers: human vs. AI memory boundaries
- AI-generated tests and false confidence
- Human role: setting context, contracts, and constitutions for AI
- Coding will persist — but the language shifts to natural language + formal specs
- Experience reports from full-time agentic coding
- Functional paradigm advantages for AI-driven development
- Context compression strategies (docs folders, markdown files)

## Key points

- **Testing remains non-negotiable**, but the type matters: unit tests constrain AI; acceptance tests (BDD/Gherkin) provide the human-managed ground truth.
- **AI happily generates useless tests** — this is a recognized trap. Human oversight of test quality is critical.
- **Token management is the new optimization target** — refactor code to fit context windows, not just for human readability.
- **Abstraction layers serve AI differently** — AI has a bigger short-term memory than humans but a "sudden and much more severe loss of memory." Abstractions must account for this different boundary.
- **Coding isn't going away** — even if Elon predicts AI will bypass coding, Uncle Bob argues we will always be coding; the language just shifts to natural language in formal specs and informal conversations.
- **The next era will be better** — businesses will still need highly skilled individuals to wrestle these "cantankerous machines" to deliver value.
- **Context compression strategies are emerging** — practitioners use root-level docs folders with markdown files describing systems at a high level, accepting the "single source of truth" violation as a pragmatic trade-off.
- **Red/Green/Refactor works with AI** — forcing AI through TDD cycles produces better results than unconstrained "Leroy Jenkins vibe-coding."
- **Humans must set context, draw up contracts, and draft constitutions** for AI behavior throughout the development process.

## Concepts / principles

**Token-Aware Clean Code**
Clean code principles (good names, short functions, modularity) apply to AI consumption, but with a new dimension: optimizing for token efficiency and delaying context compression. Code structure is now partly an information-density problem.

**AI Amnesia Cliff**
Unlike human memory that degrades gradually, AI has a catastrophic forgetting pattern — a large working memory that, once exceeded, leads to sudden and severe information loss. This shapes how code and context should be structured.

**Acceptance Tests as AI Contracts**
BDD/acceptance tests serve as the human-authored "statement of facts" that constrain AI behavior. They are the guardrails that prevent AI from drifting into technically-passing but semantically-wrong implementations.

**Test Quality over Test Quantity**
AI can produce voluminous tests that create an illusion of coverage. The discipline shifts from "write more tests" to "ensure tests are meaningful" — a human judgment call.

**Abstraction Boundaries Shift**
Human abstraction layers manage human cognitive limits. AI abstraction layers must manage different limits: larger short-term capacity but catastrophic loss at the boundary. The same principle, different parameters.

## Patterns

- **BDD-driven AI development**: Use Gherkin or similar acceptance test frameworks as the primary human→AI contract, with unit tests as a secondary constraint layer.
- **Context compression via docs**: Maintain a root-level markdown docs folder describing system architecture at a high level, trading "single source of truth" purity for AI context efficiency.
- **TDD with AI agents**: Force AI through Red/Green/Refactor cycles rather than allowing unconstrained code generation.
- **Human review of AI-generated tests**: Engineer must review tests before the agent continues building, preventing the "useless test" accumulation problem.

## Entities

- **Uncle Bob Martin (@unclebobmartin)**: Author; advocate for Clean Code, SOLID principles, and software craftsmanship.
- **DHH**: Referenced as having the right take on agentic AI being the future.
- **Claude Code**: Mentioned by practitioners as a primary agentic coding tool.
- **Gherkin / FitNesse**: Acceptance testing frameworks suggested for AI-driven development.
- **@bstewartny**: Full-time agentic AI coder (almost a year with Claude Code), confirms "this is the way."
- **@simonw (Simon Willison)**: Referenced by @vadimcomanescu as having a relevant take.
- **@ian_builds**: Shares context compression strategy using root-level docs folders.

## Quotes

> "The agent AI thing is going to be the way. There is no doubt about this in my mind." — Uncle Bob Martin

> "The AI will do anything it wants if it's not constrained. And it turns out that unit tests are insufficient." — Uncle Bob Martin

> "One of the things you will want to optimize your code for is token management." — Uncle Bob Martin

> "The AIs have long short-term memories, but boy, once that short-term memory is blown, they get amnesia fast." — Uncle Bob Martin

> "Abstraction layers help humans avoid their own version of context compression. The same is true for the AIs, but the boundaries are different." — Uncle Bob Martin (reply)

> "This is a big problem. The AI is happy to write scads of useless tests; and it makes you feel like something is being tested. My solution to this is BDD acceptance tests, written in something like Gherkin, and managed by the humans." — Uncle Bob Martin (reply)

> "There is zero doubt this is the way, and only way, to build software now. There is a whole different engineering skillset to use these tools though, its not yet an out-of-the-box solution." — @bstewartny

> "Tests are the chains with which we must bind this giant if we would make him serve us." — Paul DeGoes

## Open questions / follow-ups

- What makes code specifically more "readable" or efficient for AI models? (raised by @MartinWickman)
- Could you regenerate an app/game from just acceptance tests and unit tests (no source code) using different models? (raised by @helmutkan)
- How should embedded/real-time software teams adapt, given their existing E2E timing and IO testing suites? (raised by @TGatliff)
- How does the functional paradigm (Clojure, etc.) compare for token efficiency and AI-friendliness? (raised by @faircall)
- What happens when practitioners treat AI-generated code as a "black box" — is that viable long-term? (raised by @duginabox)

## Next steps

- Cross-reference with [[distilled/20260126-215711Z--clean-code-in-the-age-of-ai-uncle-bob]] — Uncle Bob's earlier thread on clean code vs. context windows.
- Explore the concept of **Token-Aware Clean Code** as a standalone note in `notes/`.
- Investigate BDD/acceptance testing patterns specifically designed for AI agent workflows.
- Connect to [[notes/Context Hygiene]] — overlap with context compression strategies discussed in the thread.

## Links

- Source: [https://x.com/unclebobmartin/status/2021209931400040526](https://x.com/unclebobmartin/status/2021209931400040526)
- Related earlier thread: [https://x.com/unclebobmartin/status/2015766232062951585](https://x.com/unclebobmartin/status/2015766232062951585)
