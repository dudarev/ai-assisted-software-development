---
title: "StrongDM’s software factory: scenarios + digital twin universe"
source_url: "https://simonwillison.net/2026/Feb/7/software-factory/"
captured_at: "2026-02-22T16:11:31Z"
distilled_at: "2026-02-22T16:19:02Z"
raw_refs:
  - "[[raw/20260222-161131Z--strongdm-software-factory]]"
  - "[[raw/2026-02-22T201156+0200 - Thread by @simonw]]"
capture_type: web_page
status: draft
agent: codex
model: gpt-5.2
skills_used: ["capture-tab", "make-distillation"]
confidence_notes: "Raw capture is DOM text + extracted link list; formatting is lossy (e.g., blockquote/list structure), but key terms and referenced URLs are preserved. The X thread capture includes selected replies visible at capture time and may not represent the full conversation."
tags: ["coding-agents", "software-factories", "scenario-testing", "evaluation", "digital-twins", "non-interactive-development"]
---

## Summary

<!-- TODO: I already mentioned somewhere that the concept of dark software factory should be captured. That's another note that should be referenced in that document and maybe ideas from here can enrich it. -->

StrongDM’s AI team describes a “Software Factory” workflow: humans provide specs and scenarios, and agents write and run code without humans writing or reviewing it. The core risk is obvious—LLMs make mistakes—so their argument hinges on *evaluation*: keeping scenario tests outside the agent-visible codebase (as holdout sets) and validating behavior at high volume against a “Digital Twin Universe” of cloned third-party services (Okta/Jira/Slack/etc.). They also point at supporting tooling: spec-driven agents (Attractor) and an immutable context store (cxdb).

The interesting move is not “agents write tests”, but “agents run against an environment that makes large-scale behavioral validation cheap”: cloned SaaS APIs, no rate limits, plus a satisfaction/trajectory-based notion of correctness.

## Key points

- **Two rules:** “Code must not be written by humans” and “Code must not be reviewed by humans”.
- **Scenarios as holdout sets:** end-to-end user stories stored outside the codebase to reduce agent overfitting.
- **From boolean to probabilistic:** success becomes “satisfaction” over many trajectories through scenarios, not just “the test suite is green”.
- **Digital Twin Universe (DTU):** agent-built, high-fidelity clones of external dependencies to enable high-volume validation without production constraints.
- **Compatibility target insight (Jay Taylor):** use popular reference SDK client libraries as the yardstick for DTU fidelity.
- **Tooling artifacts:** `strongdm/attractor` is a spec-only repo meant to be fed to an agent; `strongdm/cxdb` stores histories/tool outputs in an immutable DAG.
- **Cost + strategy question:** ~$1,000/day/engineer in tokens is a forcing function on whether this becomes a niche practice or widely adopted.

## Reactions / comments (X thread)

The thread is useful as a quick “objection and reflection” index:

- **The clones are the real unlock:** multiple replies converge on “full-fidelity local clones become economically viable”, possibly more important than “no human reviews code”.
- **Terminology pushback:** at least one commenter calls “digital twin” a misappropriation; Simon counters that it’s not far off.
- **Cost skepticism + “90% value for $200”:** Simon agrees that a cheaper version capturing most of the value is more interesting than a $20k/month/engineer regime.
- **Governance / attribution concerns:** one reply argues that without a named human reviewer, incident reconstruction and liability become difficult (even if tests are strong).
- **Reality checks on coordination:** “no human resolves merge conflicts between 10 concurrent agents” gets flagged as a practical unsolved problem.
- **Code quality decay:** questions show up about whether “converge until tests pass” leads to codebase expansion/implosion without explicit “contraction phases”.

My take: these reactions mostly reinforce the idea that *evaluation and control planes* are the hard part. The most promising sub-idea here is not “agents write code”, but “agents can cheaply build and exercise a high-coverage simulation harness” (DTU + scenarios). The scariest gap is still unsolved: preventing “passing the harness” from diverging from “robust, maintainable, secure system”.

## Concepts / principles

**Evaluation is the product**
In a “no-review” world, the engineering work shifts toward building the harness + environment that can falsify bad behavior cheaply (DTU, scenarios, and coverage via high-volume runs).

**Holdout testing for agents**
Keeping scenarios outside the agent’s working context parallels ML holdout sets: you want tests that reflect “unseen” behavior so the system can’t overfit to them during generation.

**Behavioral fidelity beats interface parity**
A DTU is useful only if edge cases and observable behaviors match reality closely enough that passing scenarios means something.

**Economic feasibility as a constraint**
If validation requires constant spend (token-heavy swarms), the limiting factor becomes business model, not engineering ambition.

## Quotes

> “Code must not be reviewed by humans”

> “We built a Software Factory: non-interactive development where specs + scenarios drive agents… without human review.”

> “Use… reference SDK client libraries as compatibility targets…”

## Open questions / follow-ups

- What are the failure modes of scenario holdout sets (e.g., scenario drift, incomplete threat models, hidden coupling to DTU behavior)?
- How do you decide which parts of a third-party service must be cloned for meaningful coverage?
- What guardrails detect “evaluation cheating” (agents exploiting DTU weaknesses vs. producing robust implementations)?

## Links

- Source: [https://simonwillison.net/2026/Feb/7/software-factory/](https://simonwillison.net/2026/Feb/7/software-factory/)
- StrongDM: [https://factory.strongdm.ai/](https://factory.strongdm.ai/)
- Techniques: [https://factory.strongdm.ai/techniques](https://factory.strongdm.ai/techniques)
- Attractor: [https://github.com/strongdm/attractor](https://github.com/strongdm/attractor)
- cxdb: [https://github.com/strongdm/cxdb](https://github.com/strongdm/cxdb)
