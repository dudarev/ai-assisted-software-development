---
tags:
  - person
  - agentic-coding
  - workflow
  - vibe-coding
  - publish
active: true
created: 2026-02-20
summary: Programmer and blogger; associated with “Landing the Plane”, Beads, Gas Town, and (with Gene Kim) book Vibe coding / FAAFO.
aliases:
  - Steve Yeager
---

# Steve Yegge

Steve Yegge is an American computer programmer and blogger, recognized for his extensive writings on programming languages, productivity, and software culture. Throughout his career, he has held significant engineering leadership roles at major tech companies, including Amazon, Google, Grab, and Sourcegraph.

He is widely known for "Stevey's Blog Rants," which covered developer culture and software engineering practices, as well as his "Google Platforms Rant", which became somewhat legendary in the industry.

More recently, Yegge has emerged as a prominent voice and tool creator in the AI-assisted software development space, specifically advocating for paradigms like "vibe coding."

## Ideas and Work on AI-Assisted Development

Yegge has introduced and popularized several key concepts and tools for modern AI-assisted coding workflows:

### “Landing the Plane” (session termination)
An end-of-session protocol (see [[Landing the Plane]]) designed to help AI agents gracefully wrap up their work. It involves:
- Cleaning up workspace state (e.g., branches, temporary artifacts)
- Syncing task state (e.g., updating issues, ledgers, or task lists)
- Generating a concise “next session prompt” so a future agent session can resume smoothly without re-deriving the entire context.

Related concepts: [[Preflight the Plane]], [[Context Hygiene]].

### Beads (persistent task/memory board)
Beads is a git-native approach for storing task state and “session-to-session memory” outside of an LLM's context window. This allows an agent to persistently save its state and easily re-ingest the current context across separate development sessions.

### “Gas Town” (multi-agent orchestration)
“Gas Town” is an open-source orchestration tool designed for coordinating multiple AI agents against a shared task state. Yegge has demonstrated this as a "vibe coding orchestrator" that was itself initially vibe-coded.

### Vibe coding / FAAFO (with Gene Kim)
Along with Gene Kim, Yegge advocates for "vibe coding" as a shift toward **FAAFO** (Fast, Ambitious, Autonomous, Fun, Optionality), emphasizing independence of action, cheap parallel experimentation, and using chatbots to generate code directly rather than purely writing it by hand.

Related concepts: [[Vibe Coding Is FAAFO]], [[Three Developer Loops of Vibe Coding]].

## Related Notes
- [[Landing the Plane]]
- [[Preflight the Plane]]
- [[Context Hygiene]]
- [[Vibe Coding Is FAAFO]]
- [[Three Developer Loops of Vibe Coding]]

## References
- [Wikipedia: Steve Yegge](https://en.wikipedia.org/wiki/Steve_Yegge)
- [X: @Steve_Yegge](https://x.com/Steve_Yegge)
- [GitHub: steveyegge](https://github.com/steveyegge)
- [YouTube: "Beyond Instructions: How Beads Lets AI Agents Build Like Engineers"](https://www.youtube.com/watch?v=s96O9oWI_tI)
- [Book: *Vibe Coding: Building Production-Grade Software With GenAI, Chat, Agents, and Beyond*](https://itrevolution.com/product/vibe-coding-book/)
- [Article: "The Value Of Vibe Coding (or, the Good FAAFO)"](https://itrevolution.com/articles/the-value-of-vibe-coding-or-the-good-faafo/)
