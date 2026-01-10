---
title: Interview-Driven Specification
tags:
  - publish
  - pattern
  - specification
  - requirements
  - workflow
  - large-features
status: rename
chats:
  - https://chatgpt.com/c/6959f0fb-e97c-8326-9516-77799dda726a
---

A two-phase approach for building large features: specification through structured Q&A, followed by execution in a separate session.

## Pattern

1. **Phase 1: Spec refinement**  
   Start with a minimal spec or prompt. Ask the AI to interview you using interactive questioning to expand and refine the spec.

2. **Phase 2: Execution**  
   Create a new session and implement the refined spec.

## Why separate phases

- **Clarity of intent**: Specification mode focuses on decisions, not code.
- **Deeper exploration**: 40+ questions can surface edge cases, UX details, and trade-offs.
- **Control**: You shape the spec through answers, not by reviewing generated code.
- **Clean context**: Execution session starts with complete requirements, not discovery artifacts.

## Example prompt (Phase 1)

```
read this @SPEC.md and interview me in detail using the 
AskUserQuestionTool about literally anything: technical 
implementation, UI & UX, concerns, tradeoffs, etc. but make 
sure the questions are not obvious

be very in-depth and continue interviewing me continually 
until it's complete, then write the spec to the file
```

## When to use

- Building large features or new projects
- When requirements are incomplete but you know the rough shape
- When you want systematic exploration of edge cases and trade-offs
- When you prefer decision-making over code review as the primary feedback loop

## Trade-offs

- **Overhead**: More upfront time before code is written
- **Question fatigue**: 40+ questions requires sustained attention
- **Assumes good questions**: AI must ask non-obvious, useful questions
- **Two sessions**: Context doesn't flow automatically from spec to execution

## Reference

Thariq Shihipar ([@trq212](https://x.com/trq212)), [December 28, 2024](https://x.com/trq212/status/2005315275026260309):

> my favorite way to use Claude Code to build large features is spec based
> 
> start with a minimal spec or prompt and ask Claude to interview you using the AskUserQuestionTool
> 
> then make a new session to execute the spec
> 
> for big features or new projects Claude might ask me 40+ questions and I end up with a much more detailed spec that I feel I had a lot of control over

## Related

- [[four-modes-of-ai-assistance]] — This pattern uses "Brainstorming" (Phase 1) and "Surgical changes" (Phase 2)
- [[ten-principles-for-coding-with-ai]] — "Separate discovery from delivery"

<!-- 
a two-phase timeline/flow (minimal spec → interview/Q&A → refined spec → new session → execution) would make the “separate sessions” rationale visual.
-->