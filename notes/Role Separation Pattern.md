---
title: Role Separation Pattern
status: draft
tags:
  - pattern
  - role-separation
  - context-management
  - specialization
  - publish
summary: A way to get higher-quality, more reliable agent output by explicitly separating “generalist/orchestrator” work from “specialist” work, and by scoping each role to its own context, constraints, and feedback loop.
---
# Role Separation Pattern

The **Role Separation pattern** is a practical way to reduce “generic” outputs, missed constraints, and muddled reasoning when working with AI assistants. Instead of asking one agent/thread to *do everything*, you explicitly separate the work into **roles** (generalist vs specialist), give each role a clear **scope and interface**, and often run them in **separate contexts** (threads).

This draws on Lada Kessler’s framing of **generalist vs. specialist** behavior: generalist prompts tend to produce broad coverage with uneven reliability, while specialist prompts can produce higher confidence output when the task is narrow, concrete, and checkable.

## The Problem It Solves

When one agent is asked to:

- explore options,
- decide what to do,
- implement,
- review,
- and explain,

…it tends to **blend mindsets** and **skip steps**. The most common failure mode is not “wrong code,” but *role confusion*: the agent starts optimizing for speed or completion, and silently relaxes constraints that would have been obvious to a dedicated reviewer or investigator.

## The Pattern

1. **Name the roles** (what job is being done).
2. **Separate contexts when the job changes** (thread per role).
3. **Specialize prompts** (tight scope + explicit deliverables).
4. **Route outputs through a checker role** (verification is a first-class step).
5. **Use handoff artifacts** to keep the system coherent (specs, diffs, checklists, test results).

## Core Roles (Generalist ↔ Specialist)

### Generalist (Orchestrator)

- Owns the system-level outcome.
- Defines the goal, non-goals, constraints, and acceptance criteria.
- Breaks work into specialist-shaped tasks.
- Decides sequencing, merges outputs, and resolves trade-offs.

### Specialists

Own narrow jobs with crisp deliverables. Common specialist roles:

- **Implementer**: produce a patch meeting a spec.
- **Investigator**: isolate root cause; propose the smallest viable fix.
- **Reviewer/Checker**: attempt to falsify; run tests; focus on boundaries and failure modes (see [[Maker-Checker Pattern]]).
- **Explainer/Doc**: translate into user-facing docs, changelogs, or onboarding notes.

The key design choice: each specialist should have **one primary axis of optimization** (speed, safety, clarity, minimal diff, etc.).

## Concrete Example

**Scenario: fixing a production bug.**

| Step | Role | Mindset | Output |
|------|------|---------|--------|
| 1 | Investigator | "Prove what's wrong" | Minimal repro + root cause |
| 2 | Implementer | "Make it pass" | Smallest patch + tests |
| 3 | Reviewer | "Break the patch" | Go/no-go + boundary notes |

Each role runs in a **fresh context** seeded only with the artifact from the previous step — not the full conversation history.

**The engineering team parallel.** This maps directly onto how software teams are structured: developers optimize for construction; QA engineers optimize for finding failure. These mindsets actively conflict — a developer finishing a feature naturally wants to believe it works; a QA engineer's job is to prove it doesn't. A single person can embody both roles *sequentially* (build first, then shift into adversarial-tester mode) and capture most of the benefit with none of the handoff overhead. The same applies to AI roles within a session: switching context and re-prompting as a Reviewer after finishing as an Implementer is enough.

## Operating Protocol

### 1. Generalist creates a “role card”

Write a short, copy-pastable role card:

- **Purpose**: what this role is optimizing for.
- **Inputs**: what artifacts it can use.
- **Constraints**: rules it must not violate.
- **Deliverables**: what it must return.
- **Stop conditions**: when to escalate or hand back.

If you find critical constraints being dropped, use an **instruction sandwich**: embed the constraint as an explicit **to-do step** inside the task sequence — not just a preamble — so the model encounters it mid-execution rather than only at the prompt boundary. For example, instead of "always run tests," add a `[ ] Run tests` step between each refactoring step in the to-do list. Lada Kessler observed this raised compliance from near-zero to ~95%: the constraint appears inside the model's working flow, not just the framing.

### 2. Run “thread per role” (task-scoped contexts)

Switch context when the **job changes** (build vs review vs investigate), not merely when you feel stuck.

This is a direct application of [[Context Hygiene]] (“one task per context window”), but expressed in team/role terms.

### 3. Handoff via artifacts, not vibe

Prefer passing:

- a short spec or checklist,
- a diff/patch,
- and evidence (tests, logs, screenshots),

…over passing long conversational history. Treat context as an asset: version it, scope it, keep it readable.

## Variants

### Adversarial collaboration (Expand vs Critique)

Assign two specialist roles explicitly:
- **Expander**: generate options; push breadth.
- **Critic**: find holes; enumerate failure modes; demand evidence.

This creates productive tension and reduces premature convergence.

### “Specialization as differentiation”

If you routinely get bland or “average” output, increase specialization:
- narrower task,
- tighter interface,
- more explicit evaluation criteria,
- stronger boundaries.

The goal is not “more agents,” but **more distinct jobs**.
In practice: a pipeline of scout → planner → builder → reviewer → red team outperforms a single "do everything" agent not because it uses more compute, but because each role has one thing to optimize. Lada Kessler observed that a dedicated committer agent in a separate context window began catching constraint violations that a general-purpose coding agent *never* caught — same rules, different focus.
## Trade-offs and Failure Modes

- **Overhead**: role separation adds coordination cost; mitigate with lightweight role cards and reuse.
- **Thrash**: too much context-switching; mitigate by separating *jobs*, not micro-steps.
- **Inconsistent world models**: specialists disagree; mitigate with shared acceptance criteria and a single generalist decision-maker.
- **False confidence**: specialists can still be wrong; mitigate by designing fast feedback (tests, linters, runtime checks) into the loop.

Also note the organizational mirror: as AI lowers implementation cost, human roles can blur (engineering/design/PM), with “builder” as an umbrella identity and specialization moving from people → *tasks*.

## Related Notes

- [[Maker-Checker Pattern]]
- [[Orchestrator vs. Executor]]
- [[Context Hygiene]]
- [[Separate Discovery from Delivery]]

## References

- Video: [Lada Kessler patterns (generalist vs specialist; task-scoped contexts; instruction sandwich)](https://www.youtube.com/watch?v=M-zOSEJFNos)
- Video: [OpenClaw vs Claude Code (split roles; autonomy vs isolation)](https://www.youtube.com/watch?v=9f38h_GooA8)
- Video: [Claude Code agent teams (adversarial collaboration)](https://www.youtube.com/watch?v=y_W3486ccfI)
- Video: [Pi coding agent (specialization as differentiation)](https://www.youtube.com/watch?v=f8cfH5XX-XU)
- Video: [Agentic coding workflow (task-scoped contexts)](https://www.youtube.com/watch?v=goOZSXmrYQ4)
