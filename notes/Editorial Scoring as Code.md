---
title: "Editorial Scoring as Code"
tags:
  - publish
  - ranking
  - evaluation
  - workflow
  - personalization
status: seedling
summary: Encode editorial judgment as an explicit scoring rubric so prioritization is consistent, inspectable, and tunable.
distilled_refs:
  - "[[distilled/20260202-210255Z--screensharing-kevin-rose-s-ai-workflow-new-app.md]]"
---

# Editorial Scoring as Code

**Editorial Scoring as Code** is the practice of encoding subjective judgment as an explicit, repeatable scoring rubric. Instead of relying on vague intuition, you define criteria, assign weights, and compute a composite score that ranks items according to your priorities.

This turns “taste” into a small, inspectable system you can tune over time.

## Why it matters

- **Consistency**: every item is judged against the same criteria.
- **Debuggability**: you can see *why* something ranked higher or lower.
- **Tuning**: weights can be adjusted as goals change (e.g., more novelty, less hype).
- **Personalization**: two people can share the same rubric but set different weights.

## Typical structure

1. **Define criteria**
   Examples: novelty, impact, technical depth, relevance, PR-fluff risk.
2. **Score each criterion**
   Manual, heuristic, or model-assisted (0–5, 0–10).
3. **Weight criteria**
   Example: `score = 0.35*novelty + 0.30*impact + 0.20*relevance + 0.10*depth - 0.15*pr_fluff`.
4. **Rank by total score**
   Items float to the top according to your rubric.

## Where it applies

- **News/idea feeds**: prioritize what’s worth attention.
- **Backlog triage**: rank features by impact and leverage.
- **Bug queues**: combine severity, frequency, and customer impact.
- **PR review**: rank change risk vs. value.

## Pitfalls

- **Overfitting**: too many criteria makes it opaque and fragile.
- **False precision**: treat scores as relative signals, not exact truths.
- **Stale rubrics**: weights should evolve with your goals.

## Related notes

- [[Competitive Agentic Forking]]
- [[Maker-Checker Pattern]]
- [[Spec-Driven Development]]
- [[Disposable Software]]
- [[Tooling Chaos Monkey]]

## References

- Kevin Rose interview: https://www.youtube.com/watch?v=QPAy9R9V1rA
- Sean McBride (Intercom), “RICE: Simple prioritization for product managers” (2018): https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/
- Johan Galtung & Mari Holmboe Ruge, “The Structure of Foreign News” (1965): https://doi.org/10.1177/002234336500200104
- Monika Bednarek & Helen Caple, “News values” in *The Discourse of News Values* (2017): https://doi.org/10.1093/acprof:oso/9780190653934.003.0002
- Al Jazeera Media Institute, “How do we determine ‘newsworthiness’?”: https://institute.aljazeera.net/en/ajr/article/2270
