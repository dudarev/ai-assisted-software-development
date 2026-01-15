---
title: Agent and Tool Governance
tags:
  - ai-agents
  - engineering-management
  - scalability
  - tool-design
---

# Agent and Tool Governance

Governance in the context of AI agents is the management framework that ensures tools and agents are secure, reliable, and reusable across an organization. It represents the shift from individual "siloed" experiments to a scalable "agent program."

## The Core Challenge: Silos vs. Horizontal Scale
When an organization moves beyond a single agent team, it inevitably faces the "rebuilding the wheel" problem. Individual teams, focused on their specific business goals, build bespoke tools (e.g., a "CRM Search" tool) that are often slightly different from a tool built by another team.

Without governance, this leads to:
- **Redundant Effort**: Dozens of teams maintaining nearly identical tool logic.
- **Inconsistent Logic**: Different versions of the same business rule being applied across various agents.
- **Security Risks**: Lack of clear visibility into which agents have access to which sensitive backend systems.

## Key Governance Issues

### 1. Ownership and Maintenance
A shared tool introduces a classic organizational problem: **Who owns it?** 
- If a team builds a "shared" CRM tool that 20 other agents depend on, who is responsible for fixing a bug? 
- Who handles the versioning when the underlying CRM API changes?

### 2. Access Control and Policy
Governance must define which agents are allowed to "see" which tools. 
- **Internal vs. External**: An internal HR agent and a customer-facing support agent may both need "employee lookups," but the policy for what information they can access should be centrally managed, not left to individual agent developers.

### 3. Versioning and Downstream Impact
Since a tool definition (name, description, parameters) is effectively a **prompt** that a model interprets, changing it is equivalent to a code change that can break every agent consuming it. Governance requires rigorous evaluation before a shared tool is updated.

### 4. Evaluation at Scale
Shared tools need their own set of base evaluations (Does the tool execute correctly?), but individual agents need **domain-specific evals** (Does the agent use the tool correctly in *this* specific context?). 

## The Maturity Curve
A common mistake is trying to build "the perfect shared tool library" before the first agent is even in production—often referred to as building the "Sistine Chapel of complex agent governance."

The recommended path is:
1. **Go Deep First**: Solve the specific business problem in a siloed way to understand the real-world challenges.
2. **Abstract Out**: Once the patterns are proven, extract common functionality into shared tools or a **Tool Registry**.
3. **Optimize for Sharing**: Shift to a model where developers "pick" existing, governed tools to accelerate the creation of new agents.

## Reference
This concept is extensively discussed in the context of scaling agent programs, notably in conversations regarding the transition from "Tooling as APIs" to "Tooling as Agent Intentions."

**Source**: [Tool definitions are the new Prompt Engineering (MLOps Community)](https://www.youtube.com/watch?v=rMhvSkXbv4A)

> "The moment you start sharing tools... you immediately inherit a bunch of governance challenges... who has access to the tool? Who owns the tool? Who’s in charge of bug fixing it?"
> — *Alex Salazar (Arcade.dev) & Chiara Caratelli (Prosus)*

***

## Suggested Implementation Patterns
- **Tool Registry**: A central catalog where developers can discover existing, approved tools.
- **Shared vs. Domain-Specific Evals**: Maintain a base suite of evals for the tool itself, while allowing agent teams to overlay their own intent-based evals.
- **Governance as an Accelerator**: Reframe governance not as "bureaucracy" but as a "productivity gain"—picking an existing, governed tool is faster than building a new one from scratch.
