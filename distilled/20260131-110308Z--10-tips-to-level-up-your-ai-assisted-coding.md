---
title: "10 tips to level up your ai-assisted coding"
source_url: "https://www.youtube.com/watch?v=z8XWvBpL_EA"
captured_at: "2026-01-31T11:03:08Z"
distilled_at: "2026-01-31T13:03:36Z"
raw_refs:
  - "[[raw/20260131-110308Z--10-tips-to-level-up-your-ai-assisted-coding-aleksander-stensby-ndc-manchester-20.md]]"
capture_type: youtube_transcript
status: draft
agent: antigravity
confidence_notes: "Transcript appears to be high quality with some minor speech disfluencies. The speaker's numbering system for tips was slightly loose/interwoven; extracted primarily based on content clusters."
tags: ["ai-coding", "productivity", "cursor", "claude-code", "context-management", "mcp", "prompt-engineering"]
---

## Summary

In this talk from NDC Manchester 2025, Aleksander Stensby presents a comprehensive guide to maximizing developer productivity with AI coding assistants like Claude Code and Cursor. Moving beyond basic prompting, Stensby advocates for "Compounding Engineering"—a mindset where the developer actively trains their AI "colleague" over time through persistent rule files and context management. He outlines practical workflows for handling context windows, using sub-agents for parallel tasks, leveraging the Model Context Protocol (MCP), and orchestrating background agents. The talk emphasizes that while AI models are powerful, the developer's role shifts to that of an architect and reviewer, ensuring quality through "human in the loop" verification.

## 10 Tips

Here are the **10 tips** he gives (plus his **bonus “tip #0”**).

### 0. Adopt a pair-programming mindset

Treat the AI like an eager junior dev: give feedback, ask “why?”, ask it to **simplify**, and iterate (“make it better” repeatedly).

---

### 1. Context is king

Good results mostly come from giving the *right* context (not too little, not too much). Point the assistant to the relevant files/docs, and be explicit about constraints and desired output shape.

### 2. Use rule files and “compounding engineering”

Create and *actively maintain* repo rules (e.g., `claude.md` / `agents.md` style). Add your preferences, patterns, and “never do X” learnings so the assistant gets better over time instead of repeating the same mistakes.

### 3. Actively manage the context window

Watch context usage, avoid uncontrolled auto-compaction, and reset chats between tasks. When you need continuity, have the AI write a **markdown recap** you can re-inject as clean starter context.

### 4. Make a plan first (plan mode + ask clarifying questions)

For anything non-trivial, switch to plan mode, have it ask questions, and produce a step-by-step plan. Save the plan to a markdown file and update it as you progress.

### 5. Break work into smaller pieces

Chunk features/bugs into smaller tasks. If the assistant surfaces extra ideas mid-stream, capture them (e.g., as issues) and keep the current work focused.

### 6. Be intentional about model choice

Use the best model when needed, cheaper/faster ones for simpler tasks, and switch models/tools when you hit rate limits or need a different speed/quality tradeoff.

### 7. Learn the “agent harness” features (slash commands, sub-agents, hooks, skills)

Turn repeated workflows into **slash commands**, parallelize work with **sub-agents** (with their own context windows), add **hooks** as guardrails/automation (e.g., enforce tests), and package reusable procedures as **skills**.

### 8. Use source control + checkpoints/rewind

Assume the AI will occasionally mess things up: commit often, use checkpoints, rewind/restore when needed, and capture “what went wrong” learnings into rules/docs so it doesn’t recur.

### 9. Use MCP to connect the assistant to tools

Leverage **MCP** (he calls it “USB-C for AI”) to wire the agent to tools like GitHub, docs search, browser/devtools, etc.—but be mindful that MCP tool definitions can bloat context and carry security considerations.

### 10. Release agents… but stay the human in the loop

Use background/sandbox agents to implement issues and open PRs, but always review: verify correctness, ask it to explain changes step-by-step, and keep ownership of architecture and quality.

## Topics

- **Mindset Shift:** Treating AI as a junior partner rather than a simple tool.
- **Context Engineering:** Managing the "precious resource" of the context window.
- **Rule Files:** The importance of active, evolving system prompts (`claude.md`, `.cursorrules`).
- **Context Hygiene:** Techniques for resetting sessions while preserving state.
- **Planning:** Using "Plan Mode" and "Thinking" models to architecture solutions before coding.
- **Work Breakdown:** Decomposing large tasks into GitHub issues or smaller chunks.
- **Model Selection:** Choosing the right model (speed vs. intelligence) for the task.
- **Tooling usage:** Slash commands, Sub-agents, and Hooks.
- **MCP (Model Context Protocol):** Connecting AI to external tools and data.
- **Workflow:** Source control, checkpoints, and background agents.

## Key points

- **Compounding Engineering:** View every interaction as an opportunity to teach the AI your preferences. Don't just fix the code; update the rule file so the AI doesn't make the same mistake again.
- **Active Context Management:** meaningful context is better than large context. Don't rely on auto-compaction. Summarize your current state into a markdown file, clear the chat, and reload the summary to maintain a "clean" but informed workspace.
- **The "Rule File" is a Knowledge Base:** Files like `.cursorrules` or `claude.md` should be dynamic. Ask the AI to "capture learnings" and update its own rules after a difficult debugging session.
- **"Plan Mode" First:** Always ask the AI to create a detailed plan (using reasoning/thinking models) before writing a single line of code. This prevents assumptions.
- **Iterative Refinement:** Use the "Make it better" prompt loop. Ask the AI to simplify and improve its own output before you even review it.
- **Parallelize with Sub-agents:** Use sub-agents (especially in terminal-based tools) to perform tasks like "write tests" or "check documentation" without polluting the main conversation context.
- **Use "Soft Hooks":** Instruct the AI (via rules) to always perform certain actions after a task, such as "write a test" or "update the plan," effectively creating a software lifecycle hook.
- **Standardize with Slash Commands:** Package repetitive prompts or complex instructions into reusable slash commands to ensure consistency across the team.
- **Leverage MCP:** Use the Model Context Protocol to give agents safe, structured access to tools like GitHub, database migrations, or browser dev tools.
- **Human in the Loop:** The developer's primary value add is taste and judgment. Always review the code and challenge the AI's decisions.

## Concepts / principles

- **Compounding Engineering:** The cumulative effect of continuously refining the AI's instructions and context, leading to exponentially better performance over time.
- **Context Hygiene:** The deliberate practice of curating what goes into the LLM's context window to maximize signal and minimize noise (and cost).
- **Progressive Disclosure:** A design pattern (used in Anthropic's Skills) where information or tools are only loaded into context when explicitly needed.
- **The "Junior Developer" Mental Model:** A psychological framing where the user treats the AI with the patience and instructional rigor one would give an intern, resulting in better long-term outputs.
- **Orchestration over Coding:** The shift in the developer's role from writing syntax to coordinating multiple AI agents and processes.

## Patterns

- **Session Reset Pattern:**
    1. Ask AI to summarize current progress/state to a markdown file.
    2. Run `/clear` or restart the session.
    3. Load the markdown file as the new context anchor.
- **Rule Compaction Pattern:**
    - Regularly ask the AI to read the rule file, remove duplicates, consolidate conflicts, and produce a cleaner version.
- **Rabbit Hole Rescue:**
    - When a session goes off-track, explicitly ask the AI to "analyze what went wrong and update the rule file with a 'NEVER DO THIS' instruction" before resetting.
- **Plan-Execute-Verify:**
    - Shift+Tab (Plan Mode) -> Review Plan -> Execute Code -> Verify/Test.
- **Lazy Optimization:**
    - Prompt: "Simplify." -> Prompt: "Make it better." -> (Repeat) -> Final Human Review.

## Entities

- **Tools:**
    - **Claude Code:** Anthropic's CLI-based coding agent (supports sub-agents, deep integration).
    - **Cursor:** AI-first code editor (supports `.cursorrules`, Composer).
    - **Anti-gravity:** A "VS Code clone by Google" mentioned as having advanced browser/recording features (and high memory usage).
    - **Superbase:** Database platform mentioned for its AI-friendly migration rules.
- **Models:**
    - **Opus 4.5:** High-intelligence model for complex planning.
    - **Haiku / Gemini Flash:** Fast models for simple tasks or iteration.
    - **Composer:** Cursor's fast, multi-file editing model.
- **Protocols:**
    - **MCP (Model Context Protocol):** Standard for connecting AI to data/tools.

## Quotes

> "The models we use today are the worst models we're going to use for the rest of our lives."

> "If we treat it as a junior developer... we probably wouldn't fire that intern when they gave us mediocre results. We would probably give them feedback."

> "Context is king... Good context engineering is really about finding that sort of precious level of detail, the minimum amount of tokens that gives us the highest impact."

> "Make it better. Just ask it to make it better. You don't even have to review it first... You're just triggering it to try a bit harder."

> "We become sort of the bottleneck and not the AI."

> "If you sort of just try it a little bit, you're not going to get good results... I think we need to also invest some time in order to get good results."

## Next steps

- **Establish a "Rules" Repository:** Create a central place for team-wide rule files (`.cursorrules` or `claude.md`) that capture best practices.
- **Implement the Session Reset Workflow:** Create a snippet or slash command that summarizes the current sessionstate to a file like `ai-context/session-state.md` and clears the chat.
- **Audit Tooling:** Evaluate if current tools (Cursor, Copilot) support "Plan Mode" or if a CLI tool like Claude Code should be integrated for complex tasks.
- **Explore MCP:** Set up a basic MCP server (e.g., for GitHub or a local database) to test the productivity gains of giving the agent "arms and legs."
- **Review "Anti-gravity":** Keep an eye on the release/stability of the Google "Anti-gravity" tool mentioned for its potential browser automation capabilities.

## Links

- Source: [https://www.youtube.com/watch?v=z8XWvBpL_EA](https://www.youtube.com/watch?v=z8XWvBpL_EA)
