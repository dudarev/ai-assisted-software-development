---
title: "State of Agentic Coding with Armin and Ben #2"
author: [Antigravity]
date: 2026-01-25
tags: [agentic-coding, podcast, claude-code, cursor, amp, open-code, meta-agentic-programming, harness]
source: "[[raw/20260125-111244Z--state-of-agentic-coding-with-armin-and-ben-2.md]]"
chats:
    - https://chatgpt.com/c/6975fa72-bb48-8330-a14c-7755cc2ca590
---

# State of Agentic Coding with Armin and Ben #2

## Summary
In this episode, Armin and Ben discuss the state of agentic coding as of early 2026, focusing on a "mass hallucination" of adoption that occurred over the holidays. This surge was driven by "guest passes" and free time, leading many to break their lock-in to existing tools and try new ones like Claude Code and Open Code. They debate the evolving landscape of tools, distinguishing between the models (Opus 4.5 vs Codex) and the "harnesses" (wrappers) like Amp and Pi. Key themes include the shift away from traditional IDEs, the importance of "harness" features like context handoffs and branching, and the emergence of "Meta Agentic Programming," where agents are used to reprogram their own tools on the fly.

## Key Points
<!-- In some other documents it's also mentioned that around this point happened a phase transition and probably in the thread with Andrey Karpaty .  -->
- **Holiday Adoption Spike**: A significant uptake in agentic tools occurred over the holidays, fueled by "guest passes" (e.g., from Claude) and developers having free time to experiment. This event helped break the "lock-in" of employer-paid tools like Cursor.
- **Vibes-Based Model Evaluation**: Users are forming strong preferences around models based on interaction style rather than just benchmarks. **Opus 4.5** is described as more conversational and interactive, while **Codex** is seen as a "lucky draw" deep thinker that works for long periods without interruption but is harder to steer.
- **Harness Innovation**: The "harness" (the interface/wrapper around the model) is becoming a critical differentiator.
    - **Amp** is praised for its "handoff" feature, which allows users to curate context for a new session instead of relying on opaque "compaction" or restarting from scratch.
    - **Pi** (a minimal agent) is highlighted for its "branching" capability, allowing users to rewind a session to a previous state to retry a failed approach, saving tokens and time.
- **Pricing Dynamics**: High subscription costs ($200/mo) for pro plans act as a barrier but offer massive value for heavy users (e.g., millions of tokens for a flat fee). There is a perception that **Cursor** is becoming relatively more expensive for power users compared to direct provider subscriptions (Anthropic/OpenAI) that bundle API usage.
- **Shift from IDEs**: Armin notes a personal shift away from IDEs (like VS Code) towards terminal-based agents and "blank canvas" interfaces, finding traditional features like tab-complete less relevant when an agent writes the bulk of the code.
- **[[Meta Agentic Programming]]**: A powerful new pattern where users instruct the agent to modify its own environment. Armin describes using Pi to build its own plugins, debugging tools, and UI extensions during a session to better solve the immediate problem.

## Concepts
- **Meta Agentic Programming**: The practice of instructing an AI agent to modify its own source code, tools, or interface during a session to add capabilities needed for the current task.
- **Harness**: The software environment wrapping the LLM that provides tools, context management, and the user interface. Innovation is shifting from the model itself to these harnesses.
- **Context Handoff**: A feature (specifically in Amp) that allows a user to explicitly choose what information to pass from an exhausting context window into a fresh session, ensuring continuity without carrying over "garbage."
- **Branching**: The ability to revert the agent's conversation history to a specific prior point to explore a different solution path.
- **Guest Pass Viral Loop**: A growth mechanism where existing heavy users distribute free access to premium models, lowering the barrier for others to try high-end agentic workflows.

## Entities
- **Armin**: Podcast host.
- **Ben**: Podcast host.
- **Claude Code**: Anthropic's command-line agentic coding tool.
- **Cursor**: The dominant AI-powered code editor, viewed as the incumbent being challenged.
- **Amp**: A curated, "Porsche-like" agentic editor focused on high-quality UX and features like handoffs.
- **Open Code**: An open-source terminal-based agent that benefited from the holiday surge.
- **Pi**: A minimal, "blank canvas" coding agent created by Mario (Techna?), praised for its flexibility and branching features.
- **Codex**: OpenAI's model/tool, characterized as a "deep thinker" that requires long, uninterrupted runtimes.
- **Opus 4.5**: Anthropic's model, preferred for interactive, conversational coding.
- **Boris Cherny**: Creator of Claude Code, noted for engaging directly with the community.
- **Clawdbot**: Predicted to be a trend in the coming month (personal agents/daemons).

## Predictions
- **Monthly Predictions**: The hosts decide that yearly predictions are too slow for the current pace of AI, shifting to monthly predictions.
- **Rise of Personal Agents**: A prediction that "personal agents" (like Clawdbot) that act as always-on remote controls for one's digital life will be the next trend in the coming month.
- **More Harnesses**: Despite consolidation fears, the hosts bet there will be *more*, not fewer, coding harnesses/agents in the near future as innovation continues.
- **Skill Usage**: Widespread adoption of "Skills" (MCP-like tools) is expected to increase.

## Quotes
- "The answer is you write continue enter continue enter continue enter because it will always you always send one message." — *On keeping agents running overnight.*
- "I drive an automatic. I'd like an automatic in my coding editor."
- "It’s like handing a junior programmer a really intense task and then they come back 20 minutes later and you’re like, 'you haven't done the homework.'" — *On Codex's sometimes shallow fast responses.*
- "I literally go to pi and say like pi build an extension to yourself." — *On Meta Agentic Programming.*
- "There's a huge difference between Opus and Codex... Codex to me I would describe as it's a lucky draw."

## References
- [buildwithpi.ai](https://buildwithpi.ai/)