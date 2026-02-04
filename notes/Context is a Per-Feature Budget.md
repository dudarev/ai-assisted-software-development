---
title: Context is a Per-Feature Budget
tags:
  - principle
  - context-hygiene
  - agentic-workflows
  - best-practices
  - publish
distilled_refs:
  - "[[distilled/20260204-203833Z--ai-techniques-distilled-from-thousands-of-hours-of-real-work.md]]"
  - "[[distilled/20260203-004709Z--fundamental-knowledge-swe-s-in-2026-must-have-before-i-will-even-consider-hiring.md]]"
---
# Context is a Per-Feature Budget

**Context is a Per-Feature Budget** is the operational principle that treats an LLM's context window not as a persistent workspace, but as a finite, depleting resource allocated to a single unit of work (e.g., a feature, a bug fix, or a distinct task).

## The Core Concept

Long-running chat sessions suffer from **Context Decay**. As a conversation grows, the model's adherence to initial system instructions, quality bars, and specific constraints degrades. The model becomes "forgetful" or "lazy," often silently dropping requirements (measured at ~40% drop rate in some experiments).

To combat this, you must **reset the context** (start a new chat) for every new unit of work.

## The Rule: One Unit of Work = One Context

1.  **Scope the Work:** Define a single feature or task.
2.  **Spend the Budget:** Use the context window solely to execute that task.
3.  **Reset:** Once the task is complete (or if the context heavily degrades), end the session.
4.  **Repeat:** Start a fresh context for the next unit of work.

> "A new unit of work gets a fresh context." — *AI Techniques Distilled*

## The Prerequisite: External Memory

You cannot safely reset context if the chat history is your only memory. This principle **requires** shifting state from chat to durable artifacts (files).

*   **Before Resetting:** Ensure all progress, decisions, and next steps are captured in files (e.g., `PRD.md`, `todo.md`, `user_requests/feature_A.md`).
*   **Rehydrating:** When starting the new context, read in only the relevant files needed for the new task.

## Relation to [[Context Hygiene]]

This principle is a specific, actionable rule within the broader practice of [[Context Hygiene]].
*   **Context Hygiene** is the discipline (don't pollute, keep it clean).
*   **Per-Feature Budget** is the tactic (reset on every feature boundary).

## References

*   [**AI Techniques Distilled From Thousands of Hours of Real Work**](https://www.youtube.com/watch?v=kf6h6DOPjpI): Identifies "Silent Requirement Dropping" as the failure mode and "Clear Context" as the fix.
*   [**Fundamental Knowledge SWEs in 2026 Must Have**](https://www.youtube.com/watch?v=F5wxBoGSWtk): Geoffrey Huntley emphasizes "One task per context window" and "Hit new chat all the time."
