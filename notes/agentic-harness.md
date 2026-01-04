---
tags: [publish, context-engineering, tool-use, orchestration, evaluation, harness]
---

# Agentic Harness

An **agentic harness** is the **wrapper around an LLM that turns it into an agent** by running it in a loop, giving it tools, and managing state.

## Working Definition

**Agentic harness = controller loop + tool runtime + context/state management + guardrails + (optional) evaluation.**

In practice, the harness is the part that:

* Calls the model repeatedly (plan → act → observe → update → repeat)
* Executes tools (shell, files, web, APIs, repo ops) on the model's behalf
* Manages context (what to include, summarize, persist, retrieve)
* Enforces constraints (step limits, timeouts, budgets, sandboxing, policy checks)
* Optionally adds evaluation (tests, graders, benchmarks, self-checks)

## Two Common Meanings

* **Runtime harness** - used to build/operate real agents (coding agents, research agents, ops agents).
* **Evaluation harness** - used to run task suites and measure performance across models/variants.

## Why It Matters

Most "agent capability" comes from the harness:

* Better tool schemas and error handling → fewer dead ends
* Better context strategy → less thrashing and hallucination
* Better guardrails → safer automation and fewer expensive loops
* Better eval harness → faster iteration and trustworthy improvements

## Quick Checklist

A good harness usually has:

* Clear step protocol (actions vs observations)
* Tool contracts (schemas, retries, timeouts)
* Memory strategy (short-term summary + retrieval + persistent notes)
* Budgeting (tokens, time, steps, cost caps)
* Evals (unit tests, lint, golden tasks, regression suite)

## References

- [Sean Goedecke - What have we learned about building agentic AI tools?](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/)
- [I think this is a strictly worse name than "agentic harness", ... | Hacker News](https://news.ycombinator.com/item?id=45429410)