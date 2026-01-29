---
title: Discovery Rituals for AI Tools
tags:
  - tooling
  - discovery
  - pattern
  - chaos-engineering
  - publish
status: evergreen
---

# Discovery Rituals for AI Tools

In the rapidly shifting landscape of AI-assisted development, your current stack is always decaying. To remain at the frontier, you must transition from "using tools" to "maintaining a discovery ritual." 

This ritual is the engine behind the [[Tooling Chaos Monkey]]—it provides the candidates for your regular tool swaps.

## The Strategy: Models vs. Harnesses

To do effective discovery, you must distinguish between the **Model** (the brain) and the **Harness** (the body/agent/IDE).

*   **[[agentic-harness|Harness]]**: Tools like Claud Code, Cline, Roo Code, OpenHands, or Droid. 
    They provide the tool-use logic, environment access, and UI.
*   **Models**: The underlying LLMs (Claude 3.5, GPT-4o, Gemini 1.5).

A breakthrough can happen in either. A great model can fail in a poor harness, and a clever harness can make a mediocre model shine.

### Recipe 1: Quantitative Performance (The Leaderboards)

#### For Harness & Agent Discovery
Use these to find new *tools* and autonomous systems that are successfully orchestrating models.
*   **[Terminal Bench](https://www.tbench.ai/leaderboard/terminal-bench/2.0)**: **Crucial for Harness Discovery.** It shows how diverse harnesses (like Droid, Junie, or Warp) perform across different models. Use this to see which *agentic architectures* are currently winning.

#### For Raw Model Discovery
Use these to find which *brain* you should be plugging into your preferred harness.
*   **[LiveCodeBench (GSO)](https://livecodebench.github.io/gso.html)**: **The "Model-in-a-Harness" Test.** This ranks different models using a *fixed harness* (currently OpenHands). It tells you which model is the most capable "brain" when given a standard set of tools.
*   **[LMSYS Chatbot Arena (Coding)](https://chat.lmsys.org/?leaderboard)**: Best for finding models that are good at direct chat-based code generation and explanation, rather than autonomous agentic loops.

### Recipe 2: Usage-Based Discovery (The OpenRouter "Trending" Loop)
Raw benchmarks don't tell you about the UX. To find the next "Cline" or "Roo Code," look at where the tokens are flowing.

1.  **Navigate to [OpenRouter Rankings](https://openrouter.ai/rankings#categories)**.
2.  **Filter by Category**: Select "Programming" or "Software Development."
3.  **Identify the Top Models**: Pick the top 2-3 models by token volume (this shows what the pros are using).
4.  **Drill Down into Apps**: Click on a model and look for the **"Trending Apps"** or **"Popular Integrations"** section.
    *   *Why this works*: If a massive amount of tokens for a top-tier model (like Claude Sonnet) is coming from a new app you haven't heard of, that app has likely solved a UX or capability problem that others haven't.

### Recipe 3: The "Successor Search" Prompt
Use your current AI agent to find its competitors. Agents are often better at parsing technical documentation and GitHub star growth than humans.

**Prompt Template:**
> "I am currently using [Tool X] for [Specific Workflow]. My stack is [Language/Framework]. Analyze the current trending AI coding agents on GitHub and OpenRouter. Look for emerging tools that specialize in [Specific Pain Point, e.g., long-context maintenance or terminal autonomy]. Compare them to my current tool and highlight any architectural shifts (e.g., transition from chat-based to agentic)."

### Recipe 4: The Curated Curator (Meta-Discovery)
Instead of drinking from the firehose, subscribe to high-signal curators who filter for *utility* rather than just *novelty*.
*   **[Lev Selector](https://www.youtube.com/@levselector) (AI Updates Weekly)**: Focuses heavily on *practical* tools (Cline, VS Code extensions) and agentic workflows.

## The Execution: The Discovery Loop

1.  **Passive Discovery**: Keep a "Candidates" list in your notes. Whenever you see a high-signal mention in a repo or a leaderboard, add it.
2.  **Active Testing**: Once a month (or during a [[Tooling Chaos Monkey]] drill), pick the top candidate from your list.
3.  **The "Hell Project" Test**: Don't test a new tool on a simple "Hello World." Try to use it to refactor a complex, messy part of your actual codebase. If it survives, it's a keeper.

## Core Principle: Portability is Power
The goal of discovery isn't just to find a better tool; it's to ensure your workflow is robust enough to survive the death of any single tool. By regularly discovering and testing new candidates, you verify that your patterns remain tool-agnostic.
