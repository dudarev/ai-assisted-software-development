---
status: ideation
tags:
  - patterns
  - feedback-loops
chats:
  - https://chatgpt.com/c/695a93d0-ce68-8325-ad19-35ad00afd2db
---
# Loop-aware patterns and principles for AI-assisted software development

Goal: When I learn or invent a pattern/principle for AI-assisted software development, I want to tag it by the iteration loop (time scale) where it primarily applies. This helps me avoid applying the right idea at the wrong time scale, and it helps me build a coherent toolbox across technical, workflow, and organizational patterns.

This note is MY organizing layer. The Vibe Coding “Three Developer Loops” note is a reference source, but my classification scheme is independent.

## The loops (time scales)

- Inner loop - seconds to minutes (interactive iteration)
- Middle loop - hours to days (multi-session continuity, coordination, integration)
- Outer loop - weeks to months (architecture, governance, maintenance, operations)

## How I classify a new pattern (flexible, not all fields required)

For each pattern/principle, capture what’s relevant:

- Name:
- One-liner (what it is / why it exists):
- Primary loop: Inner / Middle / Outer
- Secondary loop(s): (optional)

- Pattern type: (optional)
  - technical / workflow / organizational / socio-technical / product / research

- Where the human is in the loop: (optional)
  - What must be decided/approved by a human?
  - What can be delegated safely?

- Context + assumptions: (optional)
  - Preconditions, constraints, “this works when…”

- Implementation shape: (optional)
  - Could be a prompt, a checklist, a habit, a meeting format, a role split, a team policy, a CI gate, etc.

- Evidence / evaluation: (optional, broader than “validation”)
  - How do I judge if this pattern is helping?
  - What signals/metrics or qualitative cues matter?
  - How do I notice it’s failing or causing harm?

- Costs / tradeoffs / risks: (optional)
  - What it makes better, what it makes worse

- Example(s): (optional)
- References: (optional)

## Mapping heuristics by loop

### Inner loop patterns tend to optimize for
- speed of iteration
- clarity of intent at function/module level
- cheap reversibility (small diffs, easy rollback)
- tight feedback (quick checks, minimal friction)

### Middle loop patterns tend to optimize for
- continuity across sessions (handoffs, reproducibility, memory)
- coordination (parallel work, multiple models/agents, collision avoidance)
- reducing rework (recording intent, making assumptions explicit)
- integration friction (keeping the workspace coherent)

### Outer loop patterns tend to optimize for
- long-term maintainability and architecture
- safety and governance (review, CI/CD, security, compliance)
- operational readiness (observability, incident response, ownership)
- avoiding compounding chaos (modularity, standards, deliberate process)

## Optional: purpose tags (if useful)

Instead of a fixed “mode” model, I can tag patterns by their primary purpose. A pattern can have 1–2 primary purposes.

Suggested purpose tags:
- purpose/exploration
- purpose/specification
- purpose/implementation
- purpose/evaluation
- purpose/integration
- purpose/coordination
- purpose/learning
- purpose/hardening
- purpose/operations
- purpose/organization

(If this feels heavy, skip it and rely on loop + short one-liner.)

## A simple tagging scheme (for Obsidian)

Minimal tags:
- loop/inner, loop/middle, loop/outer

Optional tags:
- type/technical, type/workflow, type/organizational, type/socio-technical
- purpose/<...>
- hil/required, hil/recommended, hil/optional

## Pattern registry (table-of-contents stub)

- [[pattern - fan-out and fuse]] - loop/? - type/?
- [[pattern - competitive forking]] - loop/? - type/?
- [[pattern - interview-first]] - loop/? - type/?
- [[Spec-Driven Development]] ([[pattern - spec-first prompting]]) - loop/middle - type/workflow
- [[pattern - checkpointing]] - loop/? - type/?
- [[pattern - AI-assisted PR review]] - loop/? - type/?
- [[pattern - CI as an AI gate]] - loop/? - type/?

(Each pattern gets its own note using the template below.)

## Pattern note template (minimal-first)

### Pattern: NAME

- One-liner:
- Primary loop:
- Secondary loop(s):
- Type:
- Where the human is in the loop:
- Context + assumptions:
- How it shows up in practice:
- Evidence / evaluation:
- Costs / tradeoffs / risks:
- Examples:
- Related patterns:
- References: