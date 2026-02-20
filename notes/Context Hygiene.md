---
title: Context Hygiene
tags:
  - concept
  - agentic-workflows
  - best-practices
  - context-management
  - publish
---
# Context Hygiene

**Context Hygiene** is the disciplined practice of managing an LLM's context window to maintain agent performance, accuracy, and efficiency. As context windows grow, the temptation is to "stuff" them, but practical experience shows that "context pollution" degrades reasoning capabilities.

## Core Principles

### 1. One Task Per Context Window
Geoffrey Huntley emphasizes that developers should treat a context window like a small, precious resource (analagous to RAM in early computing). The rule is **"one task per context window"** (also formulated as [[Context is a Per-Feature Budget]]).
*   **Don't mix concerns:** If you switch from "fixing a backend bug" to "rebranding the frontend", you are polluting the context.
*   **Start fresh:** Hit "New Chat" frequently. If a tool isn't performing well, it's often due to context pollution.

### 2. Minimal Toolset
Every registered tool (function/MCP) consumes tokens and "attention" even when not used.
*   Tools are effectively "billboards" in the system prompt yelling "Pick Me!".
*   Overloading an agent with unnecessary MCPs makes it "dumber" as it struggles to select the right tool or gets distracted by irrelevant options.
*   **Practice:** Only enable the specific tools needed for the current task.
*   **Radical Minimalism:** The creator of the **Pi agent** implies that tools are a tax on the context window. He argues that if you "don't stuff your context... and just do the minimal stuff, you can live for a very long time in a single session." He suggests enabling/disabling tools on the fly to keep the footprint small.

### 3. File System as Memory
Instead of relying on the chat history (which gets compacted or truncated), push state to the file system.
*   **"Repo as Memory":** Use files like `progress.md`, `checklists.md`, or architecture decision records (ADRs) to store state.
*   **Durability:** Files persist across sessions; chat history does not.
*   **[[Landing the Plane]]:** [[Steve Yegge]] (creator of **Beads**) formalized this protocol. Before a session ends (due to fatigue or token limits), the agent runs a cleanup script to update state and generate a **"next session prompt"**.

## "Context Pollution" & Compaction
*   **Pollution:** When the context contains irrelevant information (old errors, previous tasks), the model's ability to find the "needle in the haystack" decreases. It may hallucinate or get confused by previous instructions that are no longer valid.
*   **Compaction:** Long-running sessions often "compact" or summarize history to save tokens. This can result in the loss of critical instructions or state if that state isn't preserved in the file system.

## References
*   **Video:** [Fundamental Knowledge SWE's in 2026 Must Have (Hiring Bar)](https://www.youtube.com/watch?v=F5wxBoGSWtk) by [[Geoffrey Huntley]].
*   **Related Note:** [[Ralph Wiggum Loop – January 2026 Snapshot]] - Discusses context hygiene in the context of autonomous loops.
*   **Related Note:** [[Compounding Engineering Loop]] - References the importance of resetting context.
*   **Video:** [pi - a radically minimal, opinionated multi-model coding agent](https://www.youtube.com/watch?v=4p2uQ4FQtis) (Creator of Pi agent).
*   **Video:** [Beyond Instructions: How Beads Lets AI Agents Build Like Engineers](https://www.youtube.com/watch?v=s96O9oWI_tI) ([[Steve Yegge]] on Beads).
