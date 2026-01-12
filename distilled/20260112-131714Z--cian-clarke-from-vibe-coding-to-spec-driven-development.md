---
title: "Distilled: Cian Clarke - From Vibe Coding to Spec-Driven Development"
source_url: "https://www.youtube.com/watch?v=13EDVjfWKJM"
captured_at: "2026-01-12T13:17:14Z"
distilled_at: "2026-01-12T15:22:08Z"
raw_ref: "[[raw/20260112-131714Z--cian-clarke-from-vibe-coding-to-spec-driven-development.md]]"
tags:
  - spec-driven-development
  - vibe-coding
  - ai-native-engineering
  - context-engineering
  - agentic-workflows
---

# Cian Clarke - From Vibe Coding to Spec-Driven Development

## Summary
Cian Clarke (Nearform) advocates for "Spec-Driven Development" (SDD) as a superior alternative to "Vibe Coding." SDD uses structured documents (PRDs, architecture designs, and task backlogs) to guide AI agents, significantly reducing non-deterministic errors and hallucinations while improving productivity for enterprise projects. The methodology emphasizes role specialization for agents and the upcoming shift toward "multiplayer" human-agent collaboration.

## Key Points
- **Limitations of Vibe Coding**: Unplanned, one-shot prompting leads to "busy work" (e.g., arbitrary retooling), "over-eagerness" (unasked features), and "under-completeness" (missing requirements).
- **The SDD Workflow**: 
    1. **PRD**: Defines the *what* and *why*.
    2. **Architecture Doc**: Defines the *how* (technology choice, patterns).
    3. **Decomposed Backlog**: Breaks the plan into small, context-bounded tasks.
    4. **Task-Specific Context**: Each task is executed in a fresh context window grounded by the relevant specs.
- **Agentic Roles**: Nearform replaces generalist agents with specialized roles (Technical Director, QA, Back-end/Front-end Engineer) to improve reliability.
- **Context Bounding**: High-quality outputs depend on providing the "least sufficient" context, preventing the model from becoming overwhelmed or distracted.
- **Multiplayer Mode**: Future scaling involves multiple human contributors driving parallel agentic workflows coordinated via Git and MCP.
- **Usage Specs**: Essential for teaching models about library versions or proprietary code not present in their training data.
- **Strategic Fit**: Best for MVPs, greenfield projects, and legacy modernization. Currently less effective for large brownfield projects or niche/legacy languages.

## Concepts
- **Spec-Driven Development (SDD)**: A methodology where structured specifications are the primary interface for instructing AI agents.
- **Vibe Coding**: Fragmented, iterative AI interaction without a formal plan or architecture document.
- **Agentic Roles**: Codified, specialized personas for AI agents with specific toolsets and success criteria.
- **Single-player vs. Multiplayer AI Dev**: The shift from individual AI-assisted coding to team-wide coordination of agents and humans.
- **Comparative Advantage (in AI coding)**: Delegating tasks where AI is "good enough" (boilerplate, docs, tests) to free humans for higher-level architecture and requirements.

## Patterns
- **Backlog Decomposition**: Converting a technical spec into a series of independent, verifiable tasks.
- **Work Logs**: Forcing agents to document their changes within task specs to provide context for subsequent agents.
- **Staging Gates**: Mandatory commit/sync points in agentic lifecycles to prevent merge conflicts in high-velocity parallel development.
- **Role-Based Provisioning**: Assigning task types to specialized agent roles (Front-end vs. DevOps) to minimize architectural overlap and conflicts.

## Entities
- **Cian Clarke**: Head of AI at **Nearform**.
- **Nearform**: Software consultancy focusing on Node.js and AI native engineering.
- **Kiro (Kyber?)**: An IDE mentioned for its support of spec-driven workflows and architecture documents.
- **BMAD method**: A toolset/framework for agentic delivery used at Nearform.
- **MCP (Model Context Protocol)**: Protocol used to synchronize agent backlogs with PM tools like Jira or GitHub.

## Quotes
- *"I think [SDD] tends to remove that ceiling of what you can accomplish with AI models."*
- *"What does a model do in VibeCoding mode stuck every single time... time to retool the test runner."*
- *"By virtue of being grounded in the specs, the model is producing a much more deterministic output on our behalf."*
- *"We no longer having teams of 12 or 15 people building on an agentic project. It might be three or four, so tiny teams."*
