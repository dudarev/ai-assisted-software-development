---
title: Landing the Plane
tags:
  - workflow
  - agentic-coding
  - context-management
  - beads
  - publish
---
# Landing the Plane

**Landing the Plane** is a session termination protocol for AI agents, formalized by Steve Yegge (creator of the **Beads** framework). It addresses the "amnesia" problem where agents lose context between sessions and leave "crap" (temporary artifacts) behind.

## The Problem
Without a disciplined shutdown process:
1.  **Context Loss:** The next session starts fresh ("50 First Dates"), leading to repetitive re-explanation.
2.  **Repo Pollution:** Abandoned git branches, stashes, and debugging artifacts clutter the workspace.
3.  **State Drift:** The issue tracker (or mental model) falls out of sync with the actual code state.

## The Protocol
When a user says "Land the plane," the agent executes a scripted checklist to safely close the session:

1.  **Sync Issues:** Update the issue tracker (e.g., Beads, GitHub Issues) with the latest progress, closing completed tasks and updating status.
2.  **Clean Git State:**
    *   Commit or stash pending changes.
    *   Delete temporary/experiment branches.
    *   Remove debugging artifacts.
3.  **Generate Handoff:** Create a **"Next Session Prompt"**. This is a concise summary of:
    *   What was just accomplished.
    *   The immediate next step (e.g., "Continue working on issue #44").
    *   Current known problems (e.g., "Map rendering is broken").

This prompt effectively "bridges" the context gap, allowing the next session to pick up exactly where the last one left off without re-reading the entire history.

## Application
This pattern is critical for **Context Hygiene**, allowing developers to run shorter, focused sessions ("one task per context window") without losing momentum.

## References
*   **Source:** [[distilled/20260203-223342Z--beads-session-memory-task-management-for-agents.md]]
*   **Related Note:** [[Context Hygiene]]