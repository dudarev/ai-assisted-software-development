---
title: "Agent Skills"
tags: [publish, standard, ai-agent, skills, context-engineering, interoperability]
---

# Agent Skills

Agent Skills is an **open standard** for packaging reusable agent capabilities (instructions + resources) in a folder that tools can discover and load on demand. The format was originally developed by **Anthropic** and released publicly as an open specification in October 2025 ([announcement](https://claude.com/blog/skills), [engineering blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)). Treat the spec as **actively evolving**: implementations and best practices may change as more clients adopt it.

Canonical definition:

> A simple, open format for giving agents new capabilities and expertise.
>
> Agent Skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently.

Source: https://agentskills.io/home

**Working definition:** An agent skill is a *portable capability package* that an agent can discover and load on demand. Practically, a skill is a folder that contains a required instruction file (`SKILL.md`) with minimal metadata and the operational playbook, plus optional supporting materials (scripts, references, templates/assets) that make execution more reliable.

The point is not “more prompt.” The point is *repeatable procedure + local context* packaged in a way that agents can:
1) notice it exists, 2) pull it in only when relevant, and 3) use it consistently.

## Why skills exist (the problem they solve)
Agents are often strong at general reasoning but weak at:
- team-specific conventions ("how we do code review"),
- domain procedure ("how we run a legal check"),
- environment reality (tools available, constraints, required steps),
- and organizational memory (what matters / what to avoid).

Skills are a way to store those “how we do things here” instructions in version control so they can be reused across tasks and (often) across agent products.

## How skills are used (progressive disclosure)
A typical skills workflow is:

1. **Discovery (lightweight)**
   - Agent loads only each skill’s `name` and `description`.
   - Goal: decide whether a skill is relevant without spending context budget.

2. **Activation (selective)**
   - If a task matches, the agent loads the full `SKILL.md` body.

3. **Execution (as-needed resources)**
   - The agent follows the instructions and only opens referenced files or runs scripts when needed.

This pattern is a context-management strategy: keep startup cheap, load depth only when warranted.

## Skill package shape
Minimum viable skill:

```
<skill-root>/
  SKILL.md
```

Common optional additions:

```
<skill-root>/
  SKILL.md
  scripts/
  references/
  assets/
```

- `scripts/`: executable helpers (bash/python/node/etc.)
- `references/`: deeper docs you don’t want in the main instruction file
- `assets/`: templates, example configs, static data

## The `SKILL.md` contract
### Required frontmatter
`SKILL.md` starts with YAML frontmatter and then Markdown instructions.

Required fields:
- `name`: short identifier for the skill (should match the folder name)
- `description`: what the skill does *and when to use it*

A minimal example (illustrative):

```yaml
---
name: incident-triage
description: Triage production incidents by collecting logs/metrics, narrowing scope, and producing a short incident summary.
---
```

### Naming constraints (practical)
If you want compatibility with common validators/clients, treat `name` as:
- lowercase letters / digits / hyphens only
- length-bounded (keep it short)
- no leading/trailing hyphen; avoid double hyphens
- equal to the parent folder name

### Optional metadata (use when it adds clarity)
Common optional frontmatter fields:
- `license`: license name or pointer to bundled terms
- `compatibility`: environment requirements (tooling, network access, target agent runtime)
- `metadata`: arbitrary key/value pairs (author, version, etc.)
- `allowed-tools`: allowlist of tools the skill expects to use (support varies)

## Writing good skills (authoring heuristics)
A skill is useful when it reduces ambiguity and failure modes.

Good `SKILL.md` bodies usually include:
- **When to use**: triggers and keywords that should cause activation
- **Inputs/outputs**: what the agent should ask for; what it should produce
- **Procedure**: numbered steps with decision points
- **Examples**: at least one realistic example input and the expected output format
- **Edge cases**: what to do when prerequisites are missing or data is incomplete

Keep the main instructions relatively short; push deep reference material into `references/`.

## Referencing additional files
When `SKILL.md` points to other material, prefer:
- relative paths from the skill root
- shallow reference chains (avoid “references that reference references”)

Example:
- `references/REFERENCE.md`
- `scripts/triage.sh`

## How to use this note in an agent prompt
If you want a local agent to *use* skills from this repo, a simple protocol is:

- At startup: load only skill `name` + `description` from each `SKILL.md`.
- For a given task: choose relevant skills based on description keyword match.
- After choosing: load the full `SKILL.md` and follow it exactly.
- Only open referenced files or execute scripts when the instructions require it.

This is a concrete way to keep the agent’s context small while still enabling high-fidelity workflows.

## References
- https://agentskills.io/home
- https://github.com/agentskills/agentskills
