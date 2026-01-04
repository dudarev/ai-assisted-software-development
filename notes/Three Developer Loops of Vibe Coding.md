---
status: ideation
chats:
  - https://chatgpt.com/c/695a93d0-ce68-8325-ad19-35ad00afd2db
---
# Three Developer Loops of Vibe Coding

This note summarizes the “Three Developer Loops” framework from *Vibe Coding* (Gene Kim + Steve Yegge, IT Revolution). The core idea: AI-assisted development happens across three different feedback-loop timescales, and practices (and patterns) should match the loop you’re currently in.

## The three loops (timescales)

- **Inner loop (seconds to minutes)**: rapid, conversational collaboration with an AI assistant (fast iterations).
- **Middle loop (hours to days)**: continuity across sessions, coordination, and multi-agent work.
- **Outer loop (weeks to months)**: architecture, long-term sustainability, team/system-level practices.

Across all three loops, apply the same control logic:

- **Prevent** problems before they occur
- **Detect** problems quickly when they happen
- **Correct** course fast when something goes wrong

## Inner loop (seconds to minutes)

### Prevent
- **Checkpoint and save your game frequently**
- **Keep your tasks small and focused**
- **Get the AI to write specifications**
- **Have AI write the tests**
- **AI is a Git maestro**

### Detect
- **Verify AI’s claims yourself**
- **Always on watch - keeping your AI on the rails**
- **Use test-driven development (TDD)**
- **Learn while watching**
- **Put your sous chef on cleanup duty**
- **Tell your sous chef where the freezer is**

### Correct
- **When things go wrong - fix forward or roll back**
- **Automate linting and correction**
- **When to take back the wheel**
- **Your AI as a rubber duck**

Practical interpretation: inner-loop patterns optimize for speed, but you must keep changes small, keep a recovery path, and verify continuously.

## Middle loop (hours to days)

### Prevent
- **Written rules - because your sous chefs can’t read your mind**
- **The Memento Method**
- **Design for AI manufacturing**
- **Working with two agents at once, and more**
- **Intentional AI coordination**
- **Keeping your agents busy when you’re busy**

### Detect
- **Waking up to eldritch AI-generated horrors**
- **Too many cooks - detecting agent contention**

### Correct
- **Kitchen line stress tests - using tracer bullets**
- **Sharpen your knives - investing in workflow automation**
- **The economics of optionality**

Practical interpretation: middle-loop patterns optimize for continuity and coordination - preserving context, making intent explicit, preventing agent collisions, and building “safe-to-iterate” workflow scaffolding.

## Outer loop (weeks to months)

### Prevent
- **Don’t let your AI torch your bridges**
- **Workspace confusion - avoiding the “stewnami”**
- **Minimize and modularize**
- **Managing fleets of agents - four and beyond**
- **Auditing through or around the kitchen**
- **Channel your inner product manager**
- **Making operations fast, ambitious, and fun**

### Detect
- **When the AI throws everything out**
- **CI/CD in the age of AI**

### Correct
- **Steve’s harrowing merge recovery tale**
- **When you’re stuck with awful processes and architecture**

Practical interpretation: outer-loop patterns optimize for long-term leverage - architecture, guardrails, governance, and reliability systems (CI/CD, review, observability, rollback discipline) that keep AI acceleration from becoming AI chaos.

## How to use this framework (pattern selection)

When you adopt an AI-assisted development pattern, explicitly answer:

1. **Which loop am I in right now (inner, middle, outer)?**
2. **Am I trying to prevent, detect, or correct?**
3. **What is my recovery plan (rollback, checkpoints, tests, CI gate, safe deploy)?**
4. **Where does the human decision happen (what must I verify or approve)?**

Rule of thumb: inner-loop patterns can be “fast and loose,” but anything that ships must eventually satisfy outer-loop validation (CI/CD, tests, review, operational readiness).

## References

- *Vibe Coding* (IT Revolution) - https://itrevolution.com/product/vibe-coding-book/
- IT Revolution article: “The Three Developer Loops: A New Framework for AI-Assisted Coding” - https://itrevolution.com/articles/the-three-developer-loops-a-new-framework-for-ai-assisted-coding/
- “VIBE CODING Audio Supplement” PDF (contains the loop appendix and the Prevent/Detect/Correct checklists) - https://itrevolution.com/wp-content/uploads/2025/02/VIBE-CODING_Audio-Supplement.pdf
- “Three Developer Loops of Vibe Coding” one-page diagram PDF - https://itrevolution.com/wp-content/uploads/2025/02/Three-Developer-Loops-of-Vibe-Coding.pdf
