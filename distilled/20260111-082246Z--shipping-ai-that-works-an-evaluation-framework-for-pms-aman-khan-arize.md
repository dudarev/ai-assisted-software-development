---
title: "Shipping AI That Works: An Evaluation Framework for PMs – Aman Khan, Arize"
source_url: "https://www.youtube.com/watch?v=2HNSG990Ew8"
captured_at: "2026-01-11T08:22:46Z"
distilled_at: "2026-01-11T09:28:22Z"
raw_refs:
  - "[[raw/20260111-082246Z--shipping-ai-that-works-an-evaluation-framework-for-pms-aman-khan-arize.md]]"
capture_type: "youtube_transcript"
status: draft
agent: codex
model: gpt-5.2
confidence_notes: "This distillation is based on an auto-transcribed talk; some phrases may be mistranscribed and parts of the live demo/slides are not captured as runnable artifacts here. The core framing and examples (LLM-as-judge anatomy, dataset iteration loop, production sampling) are repeated clearly in the transcript and likely reliable."
tags: ["llm-evaluation", "ai-product-management", "llm-as-judge", "acceptance-criteria", "observability", "datasets"]
---

## Summary

Aman Khan (Arize) argues that “vibe checks” don’t scale to production GenAI, and that PMs need a practical evaluation (eval) workflow that functions like software testing—while accounting for LLM non-determinism and data-dependence. The talk centers on LLM-as-judge evals: building a judge prompt that produces discrete labels (not raw numeric scores), validating it against human labels, and iterating by curating better datasets (especially “hard” borderline cases). A core mental shift is to treat evals as requirements/acceptance criteria: instead of shipping a PRD, ship an eval dataset + eval spec the team can run repeatedly in development and on production data.

## Key points

- **Evals are like tests, but harder**: LLM systems are non-deterministic, can take multiple paths, and are strongly shaped by your data (especially in enterprise/RAG/agent settings).
- **Anatomy of an LLM-as-judge eval**: define the judge’s role, provide context (the text/output to judge), specify the goal, and constrain outputs via terminology/labels + examples.
- **Prefer labels over numeric scores**: have the judge output discrete labels (e.g., toxic/not toxic) and map labels to scores downstream if needed; scoring directly can be unreliable.
- **Human labels as calibration**: compare judge labels to human annotations to find failure modes and drive prompt iteration.
- **Dataset iteration loop (dev → prod → dev)**: start with a small development dataset, iterate until the team is confident enough to ship, then continuously run evals on production data to sample disagreements and feed “hard examples” back into the dataset.
- **Evals as requirements**: use an eval dataset + eval prompt as acceptance criteria when handing off to engineering.

## Concepts / principles

**From “vibe coding” to “thrive coding”**
Keep fast iteration, but ground decisions in repeatable measurements rather than gut feel.

**Golden dataset of hard examples**
Over time, curate a set of borderline/ambiguous cases (where humans and the judge disagree, or the label is subjective) to guide iteration and prevent regressions.

**Production representativeness**
A static dataset won’t stay representative; plan to continuously sample production outputs and refresh datasets as usage and distributions shift.

## Practical checklist (PM-oriented)

- Define what “works” means in labels users/business care about (e.g., helpful, correct, safe, on-policy).
- Write a first-pass judge prompt: role + context + goal + allowed labels, with a few examples.
- Create a small dataset (10–50 examples) from realistic usage; get human labels for at least the ambiguous cases.
- Run evals, inspect mismatches, iterate the judge prompt and dataset (don’t optimize on a single aggregate score).
- Before shipping: agree on thresholds/acceptance criteria with engineering and stakeholders.
- After shipping: run evals on production data, sample disagreements, and add them back as hard examples.

## Entities

- **Aman Khan**: AI product manager at Arize (talk speaker).
- **Arize**: tooling focused on evaluation/observability for ML, GenAI, and agent systems.
- **Cruise / Waymo**: used as analogies for dataset curation via “edge case” scenarios (e.g., left turns).
- **Spotify**: mentioned as prior work context and as an Arize customer.

## Quotes

> I kind of view eval like the new type of requirement stock… instead of giving them a PRD, you give them an eval as requirements…

> I should note that this is… LLM as a judge eval… there’s other types of evaluations as well like code-based eval… and human annotations.

> …why can’t I just tell the agent to give me a score… they’re still really bad at numbers… give a text label that you can map to a score…

## Next steps

- Extract a reusable “LLM-as-judge eval prompt” template from the role/context/goal/labels structure.
- Define a minimal set of acceptance criteria labels for your current product surface (correctness, safety, tone, tool-use).
- Set up a lightweight loop to sample production outputs, label disagreements, and promote hard examples into a golden dataset.

