---
status: published
chats:
  - https://chatgpt.com/c/695a93d0-ce68-8325-ad19-35ad00afd2db
tags:
  - vibe-coding
  - workflow
  - productivity
  - feedback-loops
  - framework
  - publish
---
# Three Developer Loops of Vibe Coding

This note summarizes the “Three Developer Loops” framework from the book [*Vibe Coding*](https://itrevolution.com/product/vibe-coding-book/) by Gene Kim and Steve Yegge.

The core idea: AI-assisted development happens across three different feedback-loop timescales. Practices (and patterns) must match the loop you’re currently in to maintain speed without sacrificing quality.

## The three loops (timescales)

- **Inner Loop (seconds to minutes)**: Rapid, conversational collaboration with an AI assistant for constant, fast iterations.
- **Middle Loop (hours to days)**: Continuity across multiple sessions, coordination between agents, and context management.
- **Outer Loop (weeks to months)**: Long-term architecture, system-level sustainability, and organizational governance.

Across all three loops, apply the same control logic:
- **Prevent** problems before they occur (Guardrails & Constraints).
- **Detect** problems quickly when they happen (Verification & Observability).
- **Correct** course fast when something goes wrong (Recovery & Refactoring).

---
## Inner loop (seconds to minutes)

*Practical interpretation: Inner-loop patterns optimize for speed. Keep changes small, ensure a recovery path, and verify continuously to stay in the [[vibe-coding-is-faafo|Flow]].*

### Prevent
- **Decompose and Subdivide**: Break every task into the smallest possible steps to maintain clarity and prevent the AI from generating "creative" but unmanageable messes.
- **Checkpoint Frequently**: Commit code every few minutes. A 4x increase in commit frequency over traditional development is recommended to make "rolling back" trivial.
- **Specifications First**: Have the AI write detailed specs or documentation *before* it writes any code. This ensures a shared mental model.

### Detect
- **Verify All Claims**: Never trust an AI saying "all tests pass." Independently verify results and have the AI prove its work with specific outputs.
- **Practice Active Vigilance**: Watch for "context drift"—signs the AI is forgetting instructions or heading down a rabbit hole. Redirect the moment you see confusion.
- **Drive with Tests**: Use [[maker-checker-pattern|TDD-style]] feedback; write (or have AI write) failing tests before implementation to create immediate signal.

### Correct
- **Fix Forward or Roll Back**: Decide in seconds whether to debug or revert. If the AI is stuck in a "debugging loop," favor rolling back to your last clean checkpoint.
- **Apply Automated Cleanup**: Use automated linting, style enforcement, and "sous chef" cleanup tasks to remove debug code and technical debt immediately.
- **Take the Wheel**: Recognize when the AI has hit a wall. Manually step in to simplify the logic or use a debugger before delegating the next small step.

## Middle loop (hours to days)

*Practical interpretation: Middle-loop patterns optimize for continuity and coordination—preserving context, making intent explicit, and preventing agent collisions in [[agentic-harness|multi-agent workflows]].*

### Prevent
- **Establish "Tattoos" (External Memory)**: Before ending a session, have the AI document progress, current plans, and critical context in persistent files (like `ACCOMPLISHMENTS.md` or a log).
- **Maintain Golden Rules**: Keep an `AGENTS.md` file with project-specific instructions that are injected into every session to prevent repeated mistakes.
- **Design for AI Manufacturing**: Structure your codebase to be "AI-legible"—modularize files, choose popular frameworks with high training data density, and simplify interfaces.

### Detect
- **Monitor for Systemic Drift**: Audit for "eldritch horrors"—accumulated technical debt or modularity breaches that occur when AI modifies the same code across multiple sessions.
- **Detect Agent Contention**: In multi-agent environments, watch for collisions where agents compete for the same ports, files, or database connections.
- **Context Integrity Checks**: Periodically ask the AI to summarize the project goals to ensures its "working memory" hasn't diverged from your actual intent.

### Correct
- **Fire "Tracer Bullets"**: When struggling with a complex integration, implement a minimal "end-to-end" path to prove the concept before committing to full automation.
- **Invest in Workflow Scaffolding**: Automate the "coordination tax." If you're manually syncing state between agents, build a tool to do it for you.
- **Protocol-Based Recovery**: Have established protocols for untangling multi-agent conflicts, such as designating one agent as the "Master" to resolve merge issues.

## Outer loop (weeks to months)

*Practical interpretation: Outer-loop patterns optimize for long-term leverage—architecture, guardrails, and governance that keep AI acceleration from becoming architectural chaos.*

### Prevent
- **Preserve Bridges (API First)**: Enforce strict API boundaries. AI should optimize implementations but never "torch the bridge" by breaking existing interfaces without explicit approval.
- **Partition the Workspace**: Establish "Clean Room" boundaries between system components to prevent agents from creating "stewnamis" (cross-system dependencies that break modularity).
- **Optimize for Option Value**: Lean into modularity. The more decoupled your system, the more [[vibe-coding-is-faafo|Optionality]] you have to replace entire modules at "inference speed."

### Detect
- **Augment CI/CD with AI Gates**: Use AI-powered review bots to enforce architecture standards, security rules, and "drift detection" during the merge process.
- **Monitor Operational Telemetry**: Connect AI agents to production logs and error tracking so they can proactively detect issues that escaped the inner loops.
- **Audit the "Vibe"**: Regularly perform deep "white-box" reviews on critical paths to ensure AI-generated code isn't hiding subtle logic bugs under a clean surface.

### Correct
- **Leverage AI for Modernization**: Use the productivity surplus to refactor legacy monoliths or upgrade aging infrastructure that previously felt "too expensive" to fix (see [[Rebuild Threshold]]).
- **Automated Incident Response**: Use agents to triage production issues, generate initial post-mortems, and suggest "fix-forward" patches during outages.
- **Process Liquidation**: Use AI velocity to identify and bypass bureaucratic bottlenecks (like slow manual QA) by replacing them with high-confidence automated harnesses.

## How to use this framework (pattern selection)

When you adopt an AI-assisted development pattern, explicitly answer:

1. **Which loop am I in right now (inner, middle, outer)?**
2. **Am I trying to prevent, detect, or correct?**
3. **What is my recovery plan (rollback, checkpoints, tests, CI gate, safe deploy)?**
4. **Where does the human decision happen (what must I verify or approve)?**

Rule of thumb: inner-loop patterns can be “fast and loose,” but anything that ships must eventually satisfy outer-loop validation (CI/CD, tests, review, operational readiness).

## References

- *Vibe Coding* (IT Revolution) - [https://itrevolution.com/product/vibe-coding-book/](https://itrevolution.com/product/vibe-coding-book/)
- IT Revolution article: [“The Three Developer Loops: A New Framework for AI-Assisted Coding”](https://itrevolution.com/articles/the-three-developer-loops-a-new-framework-for-ai-assisted-coding/)
- [“VIBE CODING Audio Supplement” PDF](https://itrevolution.com/wp-content/uploads/2025/02/VIBE-CODING_Audio-Supplement.pdf) (contains the loop appendix and checklists)
- [“Three Developer Loops of Vibe Coding” one-page diagram PDF](https://itrevolution.com/wp-content/uploads/2025/02/Three-Developer-Loops-of-Vibe-Coding.pdf)
