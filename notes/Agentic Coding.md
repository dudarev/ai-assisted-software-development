---
title: "Agentic Coding"
tags: [publish, agents]
---

# Agentic Coding

Working with AI agents that plan, execute and refine code collaboratively, far beyond simple autocomplete.

## What is agentic coding?

Agentic coding involves AI systems that can:
- Break down complex tasks into steps
- Execute multi-step workflows autonomously
- Read and understand existing code
- Make decisions about implementation approaches
- Iterate and refine based on feedback or errors

This is distinct from autocomplete or chat-based assistance. The agent operates with more autonomy and context awareness.

## Key characteristics

**Planning**: Agents can decompose a request into a sequence of actions before executing.

**Tool use**: Agents interact with development tools — file systems, terminals, search, refactoring tools — not just generate text.

**Context gathering**: Agents actively seek information they need rather than relying only on what's provided upfront.

**Iteration**: Agents can test, observe results, and adjust their approach.

## When to use agentic coding

- Implementing features across multiple files
- Refactoring with systematic changes
- Debugging issues that require investigation
- Tasks requiring repeated patterns across a codebase

## When not to use agentic coding

- Quick edits or single-line changes
- Highly novel or experimental work where exploration matters more than execution
- When the cost of supervision exceeds the cost of doing it yourself

## Trade-offs

**Autonomy vs. control**: More agent autonomy can mean faster execution but requires trust and clear constraints.

**Speed vs. understanding**: Agents can move quickly, but you may lose learning opportunities if you don't engage with the process.

**Scope creep**: Without clear boundaries, agents may implement more than requested or take approaches you wouldn't choose.

## Patterns for effective collaboration

- **Define clear success criteria** before starting
- **Set explicit boundaries** on what files or systems the agent should touch
- **Review incrementally** rather than waiting for complete solutions
- **Maintain decision authority** on architectural choices
- **Treat agent output as a draft**, not final code

## Open questions

- How do we maintain code coherence when multiple agents contribute?
- What review practices scale for agent-generated code?
- How do we balance efficiency gains with skill development?

---

*This is a living document. Expect refinements as practices evolve.*
