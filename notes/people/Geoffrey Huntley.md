---
tags:
  - person
  - agentic-coding
  - workflow
  - engineering-philosophy
  - publish
active: true
created: 2026-02-04
summary: Australian software engineer and writer; known for the “Ralph” loop framing and for public arguments about agentic coding, context hygiene, and identity in software engineering.
---

# Geoffrey Huntley

Geoffrey Huntley is an Australian software engineer who writes and speaks about software engineering practice and developer tooling. He is known online for a mix of advocacy, demos, and memorable framings that translate messy day-to-day engineering work into simple operator loops and constraints.

More recently, his public work has focused on **agentic coding**: how to structure AI-assisted development as a set of repeatable loops with explicit verification, and how to adapt team and personal practices to the reality that an engineer can “reach” across stacks via agents.

## Ideas and Work on AI-Assisted Development

### “Ralph” / the Ralph Wiggum loop (verification-first iteration)
Huntley coined “**Ralph**” (often “Ralphing”) as a way to describe an iterative loop where an agent attempts a change, then a **verification step** decides whether the loop continues. The point is to move from “chatty progress” to **testable progress** by making the exit condition explicit (tests pass, build succeeds, a checker script returns 0, etc.).

Related: [[Ralph Wiggum Loop – January 2026 Snapshot]].

### “One task per context window” (context hygiene)
He has emphasized **context hygiene** as an operator skill: treat a context window like a scarce resource, keep it focused, and reset frequently rather than letting long, drifting sessions degrade quality.

Related: [[Context Hygiene]], [[Context is a Per-Feature Budget]].

### Identity erasure (stack identity becomes less durable)
Huntley uses “**identity erasure**” to describe a shift where language/framework identity (e.g., “I’m a .NET developer”) becomes less central, because agents make it cheaper to traverse unfamiliar stacks. In this view, advantage comes less from allegiance to a toolchain and more from general engineering judgment: decomposing work, defining checks, and orchestrating loops.

Related: [[Orchestrator vs. Executor]].

### “A ~300-line agent” (demystifying autonomy)
He has argued (often by demonstration) that an effective coding agent can be relatively small: a loop around an LLM plus a handful of primitives (read files, write files, run commands) and a discipline of verification and reset.

## Related Notes
- [[Ralph Wiggum Loop – January 2026 Snapshot]]
- [[Context Hygiene]]
- [[Context is a Per-Feature Budget]]
- [[Orchestrator vs. Executor]]

## References
- [Website: ghuntley.com](https://ghuntley.com/)
- [X: @GeoffreyHuntley](https://x.com/GeoffreyHuntley)
- [GitHub: ghuntley](https://github.com/ghuntley)
- [Article: “Ralph Wiggum as a ‘software engineer’”](https://ghuntley.com/ralph/)
- [YouTube: “Fundamental Knowledge SWE's in 2026 Must Have (Hiring Bar)”](https://www.youtube.com/watch?v=F5wxBoGSWtk)
