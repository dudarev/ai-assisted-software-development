---
title: "Shaping with AI: Requirements vs. Solutions"
source: "https://x.com/rjs/status/2011522235266130087"
author:
  - "@rjs"
published: 2026-01-14
created: 2026-01-14
description: "Ryan Singer describes an 'inversion' in his shaping process where project concepts are stored in LLM-maintained Markdown files instead of his head, using R x S (Requirements vs. Solutions) fit checks."
tags:
  - "shaping"
  - "ai-assisted-software-development"
  - "claude-code"
  - "product-management"
  - "spec-driven-development"
---

# Shaping with AI: Requirements vs. Solutions

Ryan Singer (@rjs) explores a fundamental shift in how he "shapes" software projects when using AI tools like Claude Code. He describes an "inversion" where the project concept—previously held mostly in the mind—is now externalized into LLM-managed Markdown files as a living source of truth.

## Summary
The "shaping" phase of a project is being transformed by AI. Instead of concepts living in the shaper's head and requiring a massive effort to document at the end, the conceptual work is now stored in Markdown files maintained by the LLM as the work happens. By teaching Claude Code specific skills for "binning" information—specifically separating **Requirements (R)** from **Solution Ideas (S)**—Singer can perform automated "fit checks" (R x S) to evaluate how different solution options address specific needs.

## Key Points
- **Externalized Concept:** The conceptual "source of truth" has moved from the developer's head into AI-maintained Markdown files.
- **R x S Matrix:** A formal method for evaluating project "fit" by checking Requirements (R) against Solution Ideas (S).
- **Automated Fit Checks:** Claude Code can identify when a requirement is not met by any current solution or existing code (turning the R from ❌ to ✅).
- **Iterative Shaping:** New solution ideas (e.g., "Solution B") can be quickly summarized by the AI as "deltas" from previous solutions, with automated updates to the fit check matrix.
- **Shaping vs. Build:** "Shaping" focuses on the mechanism (endpoints, data flow, UI components) rather than the concrete implementation details, which remain in the "build" phase.
- **The Socialization Gap:** While highly effective for a solo "F1 driver" workflow, it is currently difficult to share or conduct traditional whiteboard sessions with this AI-native process.

## Concepts & Patterns
- **Concept Inversion:** Moving the primary mental model of a project into an external, LLM-synced text structure.
- **Requirement/Solution Binning:** A structured way of prompting or instructing an AI to categorize incoming information as either a constraint/need (R) or a proposed fix/feature (S).
- **Fit Check Matrix (R x S):** A table-based representation of which solutions satisfy which requirements, used to visualize project progress and gaps.
- **Delta-based Solutioning:** Describing a new solution variant by its differences from an existing one, allowing the AI to infer the full structure.
- **F1 Driver Workflow:** A metaphor for a high-performance, solo-optimized setup that provides "superpowers" to an individual but doesn't yet scale to collaborative team environments.

## Entities
- @rjs (Ryan Singer): Former Head of Product Strategy at Basecamp and author of *Shape Up*.
- **[[Claude Code]]:** An agentic coding tool from Anthropic.
- **[[tl;draw]]:** A collaborative whiteboarding tool mentioned as a potential path for socializing AI-shaping.
- **[[Kiro]]:** A platform mentioned by Dragos Ilinca in the context of executable specs.

## Notable Quotes
> "It used to be that the *concept* was mainly in my head. And then it was a huge lift at the end to make a *document* that spelled it all out... Now the concept... is now stored as a ton of information in Markdown files maintained by the LLM."

> "Key to doing this is giving Claude Code skills for how to bin the information I’m giving it. The core is teaching it to untangle requirements (R) from solution ideas (S)."

> "The word 'spec' still scares me."

> "It feels very F1 right now -- superpowers for one driver. It doesn't translate over to whiteboard sessions."
