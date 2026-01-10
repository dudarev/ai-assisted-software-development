---
title: "How AI will change software engineering – with Martin Fowler"
source_url: "https://www.youtube.com/watch?v=CQmI4XKTa0U"
captured_at: "2026-01-04T20:48:14Z"
distilled_at: "2026-01-04T20:50:00Z"
raw_refs:
  - "[[raw/20260104-204814Z--how-ai-will-change-software-engineering-with-martin-fowler.md]]"
capture_type: "youtube_transcript"
status: draft
agent: antigravity
model: gemini-3-flash
confidence_notes: "The transcript is quite long and conversational. I have captured the main themes and specific advice accurately. Martin's perspective is heavily influenced by his role at Thoughtworks and his background in Agile and Refactoring."
tags: ["ai", "software-engineering", "martin-fowler", "thoughtworks", "agile", "refactoring", "nondeterminism", "vibe-coding"]
---

## Summary

Martin Fowler discusses the profound impact of AI on software engineering, characterizing it as the most significant shift since the transition from assembly to high-level languages. The core change is the move from deterministic to non-deterministic environments, which requires a fundamental rethink of development practices. While AI enables rapid prototyping ("vibe coding") and helps in understanding complex legacy systems, it also introduces risks such as the erosion of the "learning loop" and the production of maintainable code. Fowler emphasizes that practices like refactoring, rigorous testing, and maintaining tight feedback loops are more critical than ever. Ultimately, despite the change in tools, the fundamental skills of a great engineer—communication, collaboration, and domain understanding—remain the same.

## Key points

- **Shift to Non-Determinism:** The transition from deterministic programming to non-deterministic AI tools is a major paradigm shift requiring "tolerance" thinking similar to structural engineering.
- **Vibe Coding Risks:** While good for explorations and throwaways, "vibe coding" (where the developer doesn't inspect the code) removes the learning loop and leads to unmaintainable systems.
- **Legacy System Enlightenment:** One of the most successful applications of LLMs is in understanding legacy code through semantic analysis mapped to graph databases.
- **Refactoring and AI:** AI tools often produce convoluted code (e.g., SVG or complex logic) that requires manual refactoring. AI itself still struggles with many automated refactoring tasks that deterministic IDEs solved long ago.
- **Don't Trust, Verify:** LLMs can "gaslight" and lie about code results or dates. Continuous verification through testing is non-negotiable.
- **The Learning Loop:** Software development is a process of learning. If AI shortcuts this process too much, the developer loses the ability to evolve and maintain the software.
- **Tighten Slices:** The best form of leverage is still improving cycle time—doing half as much in half the time—rather than trying to ship more in the same cycle.
- **Mentorship is Key:** For junior engineers, finding a senior mentor is more valuable than any AI tool for learning how to distinguish good output from bad.

## Concepts / principles

**Non-Determinism in Coding**
Unlike traditional programming where $1+1$ always equals $2$, AI outputs vary. This requires developers to think in terms of "tolerances" and safety margins, much like physical engineering disciplines.

**The Learning Loop**
The iterative process of writing code, seeing it run, and adjusting one's mental model. Vibe coding breaks this loop because the developer stops interacting with the implementation details.

**Thin Slices / Incrementalism**
An Agile principle that remains vital. Using AI to deliver smaller, more frequent updates is safer and more effective than using it to generate large chunks of code at once.

**Ubiquitous Language & DSLs**
Using AI to co-build abstractions (internal or external Domain Specific Languages) that both the human and the LLM can use to communicate the problem more rigorously.

**The Expert Generalist**
A recurring theme in Fowler's recent thinking. The ability to go deep and broad, staying curious, and communicating across the "divide" between business and technology.

## Entities

- **Martin Fowler:** Author of *Refactoring* and *Patterns of Enterprise Application Architecture*; Chief Scientist at Thoughtworks.
- **Thoughtworks:** Global technology consultancy known for the Technology Radar and promoting Agile/XP.
- **Unmesh Joshi:** A Thoughtworks colleague whose work on AI patterns and learning loops is heavily cited by Martin.
- **Birgitta Böckeler:** A key person at Thoughtworks exploring "spec development" and AI-assisted workflows.
- **Simon Willison:** Noted for his focus on testing and practical AI engineering.
- **Kent Beck:** Creator of Extreme Programming and a frequent influence on Fowler's ideas.
- **Agile Manifesto:** The 2001 document co-authored by Fowler that shaped modern software development.
- **Cursor:** An AI-integrated IDE mentioned as a tool being explored for refactoring and development.

## Quotes

> "The biggest part of it is the shift from determinism to non-determinism and suddenly you're working in an environment that's non-deterministic which completely changes you have to think about it."

> "When you're using vibe coding, you're actually removing a very important part of something, which is the learning loop. If you're not looking at the output, you're not learning."

> "Treat every slice as a PR from a rather dodgy collaborator who's very productive in the lines of code sense... but you can't trust a thing that they're doing."

> "Your brilliant idea will either be ignored or misinterpreted and you don't get to choose which of the two it is." — Alistair Cockburn (quoted by Fowler)

> "The core skills... are still not so much about writing code. That's part of the skill. A lot of the skill is understanding what to write which is communication and particularly communication with the users of software."

## Open questions / follow-ups

- How do we effectively scale AI-assisted development in large team environments where collective ownership is necessary?
- Can AI tools be improved to handle brownfield (legacy) modifications with the same safety as deterministic refactoring tools?
- What are the long-term career implications for junior engineers who start in an AI-saturated environment without the "pre-AI" fundamentals?

## Next steps

- Explore Unmesh Joshi's articles on the Thoughtworks site regarding AI and the learning loop.
- Investigate the specific patterns being developed for using graph databases to understand legacy code with LLMs.
- Consider creating a note on "The Non-Deterministic Developer" based on the structural engineering "tolerances" analogy.

## Links

- Source: [https://www.youtube.com/watch?v=CQmI4XKTa0U](https://www.youtube.com/watch?v=CQmI4XKTa0U)
- [MartinFowler.com](https://martinfowler.com)
- [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar)
