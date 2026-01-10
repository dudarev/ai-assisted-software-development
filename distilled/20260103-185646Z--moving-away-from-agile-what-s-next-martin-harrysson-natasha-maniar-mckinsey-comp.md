---
title: "Moving away from Agile: What's Next – Martin Harrysson & Natasha Maniar, McKinsey & Company"
source_url: https://www.youtube.com/watch?v=SZStlIhyTCY
captured_at: 2026-01-03T18:56:46Z
distilled_at: 2026-01-04T12:05:00Z
raw_refs:
  - "[[raw/20260103-185646Z--moving-away-from-agile-what-s-next-martin-harrysson-natasha-maniar-mckinsey-comp.md]]"
capture_type: youtube_transcript
status: draft
agent: antigravity
model: gemini-3-pro-high
confidence_notes: Transcript contains some speech-to-text errors (e.g., 'MECI framework' likely refers to Mutually Exclusive Collectively Exhaustive 'MECE'). Interpretation of charts/visuals mentioned in the talk is limited to the spoken descriptions.
tags:
  - agile
  - ai-native
  - software-development
  - organizational-structure
  - productivity
  - management
  - change-management
  - measurement
chats:
  - https://chatgpt.com/c/695a4046-7f90-8326-a5e7-30504a952a3c
  - https://claude.ai/chat/e78fcf12-5111-4096-9a28-0649520737fc
---
## Summary

This talk argues that most enterprises fail to realize the full potential of AI in software development because they graft AI tools onto legacy Agile operating models. While AI tools function well, the surrounding team structures ("two-pizza teams"), roles, and workflows often remain unchanged, limiting productivity gains to ~10%. To achieve outsized returns (5-7x), organizations must shift to "AI-native" models: shrinking team sizes to "one-pizza pods," redefining engineers as orchestrators rather than executors, and moving from story-driven to spec-driven development.

## Key points

- **The "Agile Trap"**: Most companies see only incremental gains (5-15%) from AI because they keep their 8-10 person teams and standard Agile ceremonies, which were designed for human-speed development.
- **Role Transformation**: Engineers must shift from writing code (execution) to dividing work and managing agents (orchestration). Product Managers should move from writing long PRDs to prototyping directly in code or iterating on specs with agents.
- **AI-Native Roles**: "Two-pizza teams" should evolve into smaller "one-pizza pods" (3-5 people) that maintain the same output as larger teams by leveraging AI, effectively increasing the number of productive units.
- **Scaling requires change management basics**: Coaching, "bring your own code" labs, certifications, incentives, and continuous measurement are critical to move beyond initial pilot success.
- **New Bottlenecks**: Faster code generation creates new downstream problems, specifically in manual code review processes and the potential rapid accumulation of technical debt.
- **Review Lag**: Automated coding often results in "fuzzy" outputs that require extensive manual review, negating speed gains if the review process isn't also modernized.
- **Holistic Measurement**: Successful scaling requires measuring not just tool adoption, but inputs (upskilling), outputs (velocity), and economic outcomes (time-to-revenue, customer satisfaction).

## Concepts / principles

**AI-Native Operating Model**
A way of working designed essentially for AI collaboration rather than human-only collaboration. It prioritizes faster feedback loops and flexible roles over rigid Agile ceremonies.

**Orchestrator vs. Executor**
The fundamental shift in the developer's role. An executor writes the logic line-by-line. An orchestrator defines the architecture and constraints, then prompts an agent to implement the details, reviewing the output.

**Spec-Driven Development**
Moving away from "User Stories" (which are often prose-heavy and imprecise) to rigorous "Specs" that agents can interpret and implement. This allows PMs and engineers to iterate on the requirements rather than just the code.

**The "Jagged" Implementation Curve**
The phenomenon where initial AI tool rollout leads to a spike in usage followed by a drop-off, as users encounter friction or lack of proper upskilling. Sustained adoption requires "change management of small things" (incentives, communication, coaching).

## Patterns

**Factory of Agents**
*Context*: Modernizing legacy codebases.
*Approach*: High-context setup where the input (legacy code) and desired output are well-defined. Humans provide initial specs and final review, while agents handle the bulk of translation/refactoring with minimal intervention.

**Iterative Co-Creation Loop**
*Context*: Greenfield or Brownfield development (new features).
*Approach*: Agents act as creative partners providing options and prototypes. The process is non-deterministic and benefits from rapid iteration cycles to explore solutions.

**One-Pizza Pods**
*Context*: Organizational structure.
*Approach*: Consolidating roles (e.g., Full Stack + QA + Ops) into smaller, denser teams of 3-5 highly enabled individuals.
This is in contrast to typical agile two-pizza teams. 

## Case Study: New Operating Model at an International Bank

To address bottlenecks in traditional Agile ceremonies, a leading international bank implemented specific interventions to modernize their operating model:

**Interventions**
*   **AI-Assisted Planning**: Team leads used agents to allocate sprint stories based on historical team velocity data.
*   **Co-Created Specs**: Before coding, teams iterated with agents on acceptance criteria (specifically for security and observability) to ensure consistent artifacts and prevent downstream rework.
*   **Workflow-Based Squads**: Teams were reorganized by work type rather than just feature area:
    *   *Squad 1*: Dedicated to small bug fixes.
    *   *Squad 2*: Focused on greenfield development.
*   **Background Intelligence**: Agents ran in the background to detect potential cross-repository impacts, reducing debugging time.
*   **Direct Feedback Loops**: PMs bypassed traditional data science bottlenecks by using tools to observe real-time customer feedback directly, allowing immediately reprioritization.

**Results**
*   **>60x** increase in agent consumption.
*   **51%** increase in code merges.
*   Significant increase in delivery speed aligned with business priorities.

## Holistic Measurement System

This connects well with [[Measuring AI Assistant's Impact on Software Development Life Cycle]]

The speakers argue for a holistic system that prioritizes **outcomes** (and supports fast course-correction), not just tool adoption. They describe an end-to-end chain of measures:

**1. Inputs (investments)**
*   **Tools**: Spend on coding assistants and other AI tooling across the SDLC.
*   **Enablement**: Time, coaching capacity, and program investment for upskilling and change management.

**2. Outputs (leading indicators + delivery capability)**
*   **Adoption (leading indicator, not the goal)**: Breadth and depth of use across multiple SDLC use cases (not just point solutions like “only code review”).
*   **Speed / delivery**: Capacity and delivery speed improvements (e.g., velocity, throughput, time to market).
*   **Developer experience**: Developer NPS / sentiment (joy of craft vs. frustration).
*   **Quality & security**: Whether code is becoming more secure, higher quality, and more consistent.
*   **Resiliency proxy**: Mean time to resolve priority bugs (used as an indicator of resilience).

**3. Economic outcomes (executive view)**
*   **Time to revenue**: How quickly changes translate into revenue impact.
*   **Value capture**: Price differentials from higher-quality features; ability to serve/expand customers to meet feature demand.
*   **Efficiency**: Cost reduction per pod (reduced human labor in aggregate).
*   **Reinvestment**: How savings and time reclaimed get reinvested into greenfield and brownfield development.

They also highlight a maturity gap: bottom performers often don’t measure speed at all, and only ~10% measure productivity (as reported in their survey). They note that the exact proxies will evolve as tools and workflows evolve, but this structure is a useful starting frame.

## Entities

- **McKinsey & Company**: Identifying the gap between AI potential and enterprise reality.
- **MECE (Mutually Exclusive, Collectively Exhaustive)**: A grouping principle for separating a set of items into subsets that are mutually exclusive (no overlap) and collectively exhaustive (no gaps).
- **Cursor**: Cited as an example of a company that has internalized these AI-native shifts.

## Quotes

> "The reality is that about 70% of the companies that we survey have not changed their roles at all. ... You have this background expectation that people are going to do things differently but the role is still defined in the same way."

> "Engineers are moving away from execution and just simply writing code to being more of orchestrators and thinking through more how to divide up work to agents."

> "Change management is about getting a lot of like small things right. And so the crux to like actually scaling this is often about getting 20, 30, or even more things right at the same time."

> "These enterprises that were bottom performers were not even measuring speed and only 10% were measuring productivity."

> "Moving away from the two pizza structure to one pizza pods of three to five individuals."

## Open questions / follow-ups

- How do "one-pizza pods" handle knowledge sharing and bus factor risks compared to larger teams?
- What specifically does a "holistic measurement system" look like in practice for a non-tech enterprise?
- How does the "spec-driven" approach integrate with non-technical stakeholders who are used to user stories?

## Next steps

- **Audit Team Sizes**: Evaluate if current 8-10 person teams can be split into smaller, more autonomous 3-5 person pods equipped with AI.
- **Redefine Roles**: Draft new role descriptions for "AI-Native" engineers that emphasize orchestration and architecture over syntax and boilerplate.
- **Experiment with Specs**: Try running a pilot where a feature is defined entirely by a technical spec consumed by an agent, rather than a standard Jira story.
- Incorporate **Holistic Measurement System** into [[Measuring AI Assistant's Impact on Software Development Life Cycle]]
