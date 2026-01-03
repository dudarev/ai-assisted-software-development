---
title: How I Start EVERY Claude Code Project
source_url: https://www.youtube.com/watch?v=aQvpqlSiUIQ&t=1078s
captured_at: 2026-01-03T15:01:43Z
distilled_at: 2026-01-03T18:45:09Z
raw_refs:
  - "[[raw/20260103-150143Z--how-i-start-every-claude-code-project|20260103-150143Z--how-i-start-every-claude-code-project]]"
capture_type: youtube_transcript
status: draft
agent: codex
model: gpt-5.2
confidence_notes: Transcript-derived; specific product names, plugin recommendations, and claims about Claude Code capabilities (web search, hooks, permissions) may be version-dependent or phrased informally in the transcript.
tags:
  - agent-instructions
  - documentation
  - git
  - planning
  - project-setup
  - workflows
---

## Summary

A three-phase “PSB” workflow for starting coding-agent projects: **Plan** (clarify goal + milestones, produce a spec that includes product requirements and technical design), **Setup** (create the repo, project memory, automation, and integrations that reduce friction), and **Build** (use a repeatable development workflow, including issue-based and multi-agent variants). The emphasis is on making constraints and intent explicit (stack, UX rules, repo etiquette), keeping long-term context in docs that are easy to refresh, and using “plan first” plus automation (slash commands, hooks) to reduce regressions and stalled sessions.

My thoughts. Here the fourth step for compounding engineering is missing. See [[Compounding Engineering Loop]].

My thoughts are similar to that interviewing pattern. [[interview-driven-specification]]

## Key points

- Plan starts with two prompts: “what is the goal?” and “what milestones define v1/v2/etc.?”
- Use AI as a planning partner by asking it to ask you clarifying questions, not just generate a solution.
- Write a lightweight “project spec” that combines product requirements (who/what/why, user flows) and engineering requirements (stack, architecture, schema/API, infra provisioning).
- In setup, treat `CLAUDE.md` as finite “project memory”: keep it small, include goals/architecture, UX rules, constraints, and link to deeper docs.
- Maintain “automated documentation” (architecture, changelog, status, feature references) and have the agent keep it updated as work proceeds.
- For building: default to “plan mode” before implementation; scale from single-feature work to issue-based development and multi-agent workflows via git worktrees.

## Concepts / principles

**Clarity buys leverage**: the more explicit you are about goals, constraints, UX, and stack, the less the agent has to guess (and the fewer unwanted defaults you’ll get).

**Spec as agent interface**: a project spec is not “bureaucracy”; it’s a compact contract that helps an agent produce the right first version and reduces rework.

**Memory is curated, not exhaustive**: treat `CLAUDE.md` like an index (the essentials + pointers), and keep larger context in separate docs the agent can read on demand.

**Automation reduces idle time**: preconfigured permissions, hooks, and slash commands are framed as ways to prevent sessions from stalling on approvals or forgotten steps (tests/docs).

## Patterns

**Planning loop: brainstorm → clarifying questions → spec**
- Dump a brainstorm into a markdown file.
- Ask the agent “what are the three most important questions I must answer to build an MVP?”
- Turn answers into product + engineering requirements.

**`CLAUDE.md` as “routing”**
- Put only high-frequency, high-impact guidance (goals, constraints, repo etiquette, key commands).
- Link out to `architecture.md`, the spec doc, and other reference docs instead of repeating them.

**Automated docs + a post-feature update command**
- Keep a small set of living documents (architecture, changelog, status, feature refs).
- Update them after features, either via an instruction in `CLAUDE.md` or a custom slash command.

**Three build workflows**
- General workflow: research (optional) → plan → implement → test.
- Issue-based workflow: GitHub issues as the “source of truth”; optionally generate issues from the spec.
- Multi-agent workflow: run multiple agent sessions on separate git worktrees/branches, then merge.

**Regression prevention via “capture-the-rule”**
- When a mistake repeats, convert the fix into a persistent instruction that ends up in `CLAUDE.md` (rather than only patching code once).

## Entities

- `CLAUDE.md` (project memory file)
- GitHub repo, issues, GitHub CLI, GitHub Actions
- Git worktrees (parallel working copies on different branches)
- “Plugins”, slash commands, subagents (agent workflow automation concepts)
- MCP servers (integrations; examples mentioned: MongoDB/Supabase, Playwright/Puppeteer, Vercel, Mixpanel, Linear)
- Example web stack mentioned: Next.js, Tailwind, shadcn/ui, Vercel, Supabase/MongoDB, Clerk, Stripe, Resend, DigitalOcean, Cloudflare R2
- Hooks and notifications (example: Slack)

## Quotes

> “I call it the PSB system for plan, setup, and build.”

> “tell it to ask you questions.”

> “the most common mistake I see people make with Claude Code is not using plan mode enough.”

> “Hooks, let you insert determinism into your Claude Code workflow.”

> “Remember, code is cheap… don’t be afraid to throw away work.”

## Open questions / follow-ups

- What is the minimal viable set of “automated docs” that still meaningfully improves continuity across sessions?
- What rules belong in `CLAUDE.md` vs. separate docs (to avoid bloat while keeping guidance discoverable)?
- What does a good “hook set” look like for a small project (tests, formatting, docs, notifications) without creating brittle automation?

## Next steps

- Convert PSB into a publishable note focused on durable patterns (separating tool-specific details from reusable practice).
- Define a `CLAUDE.md` template and a lightweight doc set (`architecture.md`, `status.md`, `changelog.md`) that fits your typical project size.
- If you use multi-agent workflows, capture a “worktree merge + test” checklist to reduce integration conflicts.

## Links

- source: https://www.youtube.com/watch?v=aQvpqlSiUIQ&t=1078s
