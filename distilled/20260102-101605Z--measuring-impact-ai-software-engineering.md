---
title: "Measuring the impact of AI on software engineering"
source_url: https://newsletter.pragmaticengineer.com/p/measuring-the-impact-of-ai-on-software
captured_at: 2026-01-02T10:16:05Z
distilled_at: 2026-01-02T10:18:08Z
raw_ref: ../raw/20260102-101605Z--measuring-impact-ai-software-engineering.md
capture_type: podcast-transcript
status: draft
agent: github-copilot
model: claude-sonnet-4.5
confidence_notes: "Transcript-based extraction; some technical details may have transcription errors. Data percentages and study results preserved as stated but represent July 2025 snapshot."
tags: ["ai-impact", "developer-productivity", "measurement", "developer-experience", "ai-adoption", "case-studies"]
---

## Summary

Laura Tacho (CTO at DX) discusses findings from 180+ companies on how AI tools are actually impacting software development productivity. The conversation challenges oversimplified media headlines and provides data-driven insights on AI adoption patterns, actual time savings, and measurement frameworks. Key findings: only 65% of developers at well-supported organizations use AI tools weekly, the biggest time savings come from stack trace analysis (not code generation), and developers are often less satisfied when AI accelerates only the parts of work they enjoy. The episode emphasizes measuring developer experience holistically rather than focusing on narrow metrics like lines of code or acceptance rates.

## Key points

- Media headlines about AI replacing developers are oversimplified and often vendor-driven; engineering leaders must educate stakeholders to counter unrealistic expectations
- Structured, deliberate rollouts (common in regulated industries) yield better AI adoption results than ad-hoc deployment
- Acceptance rate and lines of code are insufficient measures of AI impact; need to track utilization, impact on developer experience, and cost
- Developers save most time on stack trace analysis and refactoring, not mid-loop code generation (contrary to popular assumption)
- Only ~50% of developers use AI tools weekly industry-wide; even well-supported organizations reach only 65% adoption
- Source code is a liability—AI making it trivial to generate more code doesn't necessarily improve business outcomes
- Measuring developer experience *before* rolling out AI is essential for establishing baseline and proving impact
- Time savings from coding tasks are limited because developers only spend 20-25% of their time coding
- AI may reduce developer satisfaction if it only accelerates enjoyable work, leaving more toil and administrative tasks
- Roadmaps may become obsolete in favor of experiment portfolios and rapid iteration

## Concepts / principles

**Code as liability, not asset**  
The ease of generating large amounts of code with AI doesn't translate to productivity gains. More code means more maintenance burden, more potential bugs, and larger batch sizes—all of which slow delivery. The focus should be on business impact and developer experience, not output volume.

**Developer experience as the primary AI success metric**  
AI tools should be evaluated as enablers of better developer experience, not as standalone productivity multipliers. Companies with established developer experience measurement have clearer baselines and can demonstrate AI impact more effectively. An 11% improvement in developer experience (as seen at WorkHuman) is more meaningful than acceptance rates or lines of code.

**The coding time constraint**  
Since developers spend only 20-25% of their time actually coding, even significant time savings in coding tasks (10%) translate to modest overall productivity gains (2-3%). This mathematical constraint limits the direct business impact of AI coding assistants and suggests broader organizational inefficiencies are the real bottleneck.

**Structured rollout outperforms hype-driven adoption**  
Highly regulated industries (finance, insurance, pharma) achieve better AI results because they're forced to be deliberate about acceptable use policies, licensing allocation, enablement, and measurement. "Slow is smooth, smooth is fast" applies to AI adoption.

**AI effectiveness spectrum**  
AI excels at tasks with high structure and pattern density (YAML, Terraform, migrations, refactoring) but struggles with novel, greenfield work requiring deep contextual understanding. Organizations should identify use cases along this spectrum rather than assuming uniform effectiveness.

**The batch size paradox**  
AI enables larger code changes, but larger batch sizes are inherently riskier and slower to deliver. DORA research predicts a 7.2% reduction in delivery stability with 25% increase in AI adoption, suggesting teams may sacrifice long-term quality for short-term speed gains.

**Experimentation over roadmaps**  
With reduced cost of building features, the constraint shifts from "can we build it?" to "should we build it?" Organizations that treat development as experiment portfolios rather than sequential roadmaps can iterate faster and discover what actually delights users.

**Documentation for AI agents vs. humans**  
AI-first documentation differs from human documentation: no visual dependencies, must include code examples, optimized for in-editor retrieval. Companies like Vercel and Clerk benefit from a documentation flywheel where good AI-accessible docs improve developer success, which generates better training data for AI tools.

**Enablement drives adoption**  
Training developers on non-obvious use cases (stack trace analysis, brainstorming, documentation) increases utilization more than simply providing licenses. Many developers default to mid-loop code generation because it's most visible, missing higher-value applications.

## Patterns

**DX AI Measurement Framework (three-pillar approach)**
- **Utilization**: Daily/weekly active users as percentage of total population; license availability analysis
- **Impact**: Developer experience index, velocity, throughput, complexity of work
- **Cost**: Consumption-based pricing allocation; ROI per developer segment

This framework avoids tunnel vision on speed metrics and captures quality, stability, and developer satisfaction.

**Cohort-based tool evaluation**  
Indeed's approach: segment developer groups, trial multiple AI tools, compare results across cohorts, then select best-fit tools. This controlled experiment method reduces risk of committing to suboptimal vendor before understanding organizational needs.

**Migration-first prompt engineering**  
For migration tasks: manually complete one example migration, provide both before/after files to AI model, ask it to generate a prompt that would reproduce the transformation for similar files. This produces more accurate results than generic "upgrade this file" instructions.

**Baseline-then-experiment workflow**  
Establish developer experience and productivity baselines *before* AI rollout, even if data is incomplete. Then treat AI as an organizational experiment with clear hypotheses (e.g., "AI code review will reduce feedback latency for distributed teams").

**AI for closing feedback loops**  
Use AI to provide preliminary code review when human reviewers are in different time zones, unblocking developers earlier even if AI feedback is less thorough. Prioritize reducing wait time over perfect quality in first pass.

## Entities

**People**
- Laura Tacho — CTO at DX, researcher on developer productivity
- Gergely Orosz — The Pragmatic Engineer, podcast host
- Abi Noda — Co-founder of DX
- Jesse Adametz — Leads developer platform at Twilio

**Organizations**
- DX — Developer experience measurement company
- Booking.com — Case study: achieved 65% weekly AI adoption (above 60% industry P75)
- WorkHuman — Case study: 11% developer experience improvement, 15% velocity gain for AI users
- Indeed — Structured rollout with cohort-based tool evaluation

**Frameworks & Tools**
- DORA (DevOps Research and Assessment) — Research on software delivery performance
- SPACE framework — Multi-dimensional developer productivity measurement
- DevEx framework — Developer experience measurement
- DX Core 4 — Four core measurements of productivity: speed, effectiveness, quality, impact
- GitHub Copilot — AI coding assistant (most commonly mentioned)
- Cursor — AI-enhanced code editor
- Cody — AI coding assistant
- Granola — AI meeting note-taker

**Concepts**
- Developer experience index — Composite metric of 14 research-backed drivers
- Acceptance rate — Percentage of AI suggestions accepted by developers (insufficient metric alone)
- Utilization rate — Percentage of developers using AI tools daily/weekly
- Batch size — Amount of work shipped at once (larger = riskier)
- Consumption-based pricing — Pay-per-use model (vs. fixed license costs)

## Quotes

> "One of my more controversial opinions is that source code is a liability. It sounds controversial — but then when people think about it, they realize, yeah, it actually is a liability! We're in a world where it is trivially easy to produce a tremendous amount of source code."
> 
> — Laura Tacho

> "Do we really want to measure AI impact in terms of lines of code generated? I certainly don't. We did not include acceptance rate in our framework for good reason. When we're looking at broadly measuring business impact and the impact on developer experience, acceptance rate is just such a tiny part of the story."
> 
> — Laura Tacho

> "Typing speed has never been the bottleneck in development. Now we have all this code generated faster than we can type. That's great. But it still takes me time to review that code! It's not that we're saving time because we don't have to type. A lot of that time, we're just reallocating to reviewing or other parts of code authoring that's not typing."
> 
> — Laura Tacho

> "The industry average [of spending time on coding] is like 25%. There was a study at AWS that an average AWS engineer only spends 20% of their time coding. And so when we apply AI to the coding tasks, we're only working with 20% of that time to begin with. And when we save 10% of that time, that actually doesn't amount to, 'we can, you know, ship 10 new product lines overnight!'"
> 
> — Laura Tacho

> "When Dora researched this question, what they found was that many developers were actually feeling less satisfied because AI is accelerating the parts that they enjoy. And so what was left over was more stuff that they didn't enjoy, the toil, the meetings, the administrative work."
> 
> — Laura Tacho

> "I think roadmaps are on their way out in the age of AI. Companies that are going to win with AI are not ones that think about things in roadmap sequential form, but think about it more as experiment portfolios."
> 
> — Laura Tacho

> "Data beats hype every time. AI to work on an organizational scale needs to be thought about as an organizational problem and you need to have really solid organizational hygiene when it comes to measuring your performance, treating AI as an experiment, trying to figure out what's the impact of AI."
> 
> — Laura Tacho

> "AI is a tool to improve developer experience. When you improve developer experience, you have better outcomes. It follows like that. It's the same pattern in every single company. AI isn't this magic bullet that's going to solve everything. We're talking about improving developer experience."
> 
> — Laura Tacho

## Open questions / follow-ups

- How do different organizational sizes (startup vs. enterprise) experience AI impact differently?
- What is the long-term effect of AI on junior developer growth and learning trajectories?
- How can organizations balance AI-accelerated feature development with avoiding feature bloat and thrashing?
- What specific metrics indicate whether AI is helping or hindering flow state maintenance?
- How does AI impact reduce over time as models plateau vs. compound as developers become more skilled at using tools?
- What are the security and compliance implications of consumption-based pricing for sensitive codebases?
- How do highly novel/greenfield projects measure AI impact when traditional patterns don't apply?
- Can AI effectiveness be predicted based on codebase characteristics (age, language, architecture style)?

## Next steps

- Integrate measurement framework concepts into [notes/measuring-ai-assistance-impact.md](../notes/measuring-ai-assistance-impact.md)
- Extract "code as liability" principle as a standalone concept note
- Connect to existing [notes/four-modes-of-ai-assistance.md](../notes/four-modes-of-ai-assistance.md) with stack trace analysis as primary use case
- Consider creating pattern note on "baseline-then-experiment" workflow for organizational AI adoption
- Link case studies (Booking.com, WorkHuman, Indeed) to practical adoption patterns
- Explore tension between "roadmaps becoming obsolete" and need for organizational coordination
- Research DORA's prediction of 7.2% delivery stability reduction — connect to quality/velocity trade-offs
- Document "documentation for AI vs. humans" as a specific pattern with examples (Vercel, Clerk)

## Links

- Source: [The Pragmatic Engineer Podcast](https://newsletter.pragmaticengineer.com/p/measuring-the-impact-of-ai-on-software)
- YouTube: [Video episode](https://www.youtube.com/watch?v=xHHlhoRC8W4)
- Raw: [20260102-101605Z--measuring-impact-ai-software-engineering.md](../raw/20260102-101605Z--measuring-impact-ai-software-engineering.md)
- DX AI Measurement Framework: https://getdx.com/research/measuring-ai-code-assistants-and-agents/
- Guide to AI-Assisted Engineering: https://getdx.com/guide/ai-assisted-engineering/
- DORA AI Impact Report: https://dora.dev/research/ai/gen-ai-report/
