---
title: "The Renaissance of Local Context: Why Claude Code and Obsidian are Replacing SaaS"
source_url: "https://x.com/dannypostma/status/2011065092843139291"
captured_at: "2026-01-14T23:33:50+02:00"
distilled_at: "2026-01-14T23:40:00Z"
raw_refs:
  - "[[raw/2026-01-14T233350+0200 - Thread by @dannypostma.md]]"
capture_type: twitter_thread
status: draft
agent: antigravity
model: gemini-3.0-flash
confidence_notes: "The thread contains many individual perspectives confirming a shared trend. The distillation captures the consensus while highlighting specific tools and technical justifications mentioned."
tags: ["local-first", "context-engineering", "claude-code", "obsidian", "saas-unbundling", "data-ownership"]
---

## Summary

A viral thread initiated by Danny Postma highlights a significant shift in developer workflows: moving away from scattered cloud SaaS tools (Notion, Google Docs, Figma) back to local file systems. The primary driver is the "context bottleneck" of AI agents like Claude Code. When files are local, agents can browse, grep, and coordinate information with a bandwidth and depth that API-based integrations (MCP, cloud connectors) cannot yet match. This trend reinforces the "File over App" philosophy, positioning tools like Obsidian and the local terminal as the central workspace for "vibe coding" and advanced AI orchestration.

## Topics

- **The Context Bottleneck**: Why AI agents perform significantly better when they have direct, high-bandwidth access to a local file system compared to cloud APIs.
- **File over App Philosophy**: Re-emergence of the concept that data should live in universal formats (Markdown) on the user's device rather than being trapped in SaaS silos.
- **SaaS Unbundling**: Developers migrating away from Notion, Asana, and Google Docs in favor of local Markdown repos.
- **Obsidian as an Agent Vault**: The role of Obsidian as the primary "source of truth" for personal and project knowledge that AI agents can easily consume.
- **Local Tooling Renaissance**: The return of CLI tools (grep, find, etc.) as the powerful primitives that agents use to manage context.
- **Data Sovereignty**: The shift from "someone else's computer" back to personal control as a competitive advantage.

## Key points

- **Bandwidth is King**: Local file access is the fastest, unencumbered interface. No API limits, no auth flows, no latency—just raw speed for agents to "know" everything.
- **Coordination beats Tool-Hopping**: Having project specs, docs, and code in a single local repo allows agents to coordinate across domains without manual copy-pasting.
- **SaaS Moats are now Dead Weight**: Tools that don't allow easy "export all" to local Markdown are becoming liabilities in an AI-native world.
- **Obsidian's Prescience**: Obsidian's focus on local Markdown files (File over App) was perfectly timed for the rise of coding agents that need local context.
- **MCP vs. Local**: While Model Context Protocol (MCP) helps, local access is consistently preferred for reliability, speed, and the ability to use standard CLI tools.
- **Competitive Advantage**: Owning your context locally is becoming a moat; whoever has the most comprehensive, agent-accessible knowledge base builds faster.

## Concepts / principles

**File over App**
The principle that the file (the data) is more important than the application used to create it. If files are stored in open formats (like Markdown) on a local drive, they outlive the tools and are easily accessible by any agent.

**Context Ownership**
The idea that controlling the "source of truth" locally is the new competitive advantage. Instead of querying 8 different SaaS tabs, the agent works within a unified local workspace.

**Local Tooling Renaissance**
A revival of local-first, open-source tools driven by the realization that agents are exceptionally good at using terminal-based utilities (grep, find, sed) to manage large amounts of data.

**The "It Just Knows" Effect**
The qualitative difference in experience when an agent like Claude Code has repo-wide context; it eliminates the friction of "context engineering" (explaining things to the AI) because the agent can verify truth on its own.

## Patterns

- **The "SaaS to Markdown" Migration**: Exporting Notion pages, Figma specs, and emails (via IMAP/offlineIMAP) into local Markdown folders for AI consumption.
- **Sync-Back Pattern**: Using tools like SyncThing, iCloud, or Tailscale to keep local files synchronized across devices while maintaining local-first access for agents.
- **The "Spec Folder" Pattern**: Keeping a dedicated `/specs` folder containing project requirements and architecture in local Markdown. This allows agents to "orchestrate" files and environments autonomously by providing them with a high-level roadmap and "source of truth" they can browse directly.
- **Local RAG (No Vector Store)**: Using simple file-based searches (grep) over Markdown files instead of complex vector databases, leveraging the large context windows of modern models.

## Entities

- **Danny Postma (@dannypostma)**: The instigator of the thread, focused on the power of Claude Code + local context.
- **Claude Code**: The primary agentic tool discussed, noted for its ability to browse local folders.
- **Obsidian**: The primary PKM (Personal Knowledge Management) tool cited as the ideal vault for local context.
- **Kepano (@kepano)**: CEO of Obsidian, credited for the "File over App" philosophy.
- **SyncThing / Tailscale**: Tools mentioned for maintaining local-first synchronicity.
- **offlineIMAP / mu**: Tools used to bring email context into the local file system.

## Quotes

> "The longer I work with Claude Code, the more I realise I should start to have all my files locally... Claude just browsing your folders is so much more powerful for context."
> — Danny Postma

> "File over app... Obsidian’s idea of file > app was prescient."
> — Nick Dobos

> "The real moat was always your local file system, not someone else's api."
> — Victor (@victor_explore)

> "It’s kinda ironic that what is effectively making local first mainstream isn't privacy concerns, but the need for high bandwidth context for agents."
> — Peter Choi

> "SaaS tools built moats to keep users in, now those moats are just blocking the agents. if an app doesn't have a clean 'export all' to local, it's dead weight."
> — Filip Sekan

## Quotes on Spec Folders and Folder Patterns

> "You can orchestrate files and environments if you have a good spec folder. All the LLM needs is the right context."
> — hårkl (@harkl_)

> "this is the real unlock. moved my notion docs, figma exports, and project specs to local markdown. claude code with full folder context = completely different experience. no more copy-pasting snippets. it just knows."
> — Timur Yessenov (@Timur_Yessenov)

> "Claude just browsing your folders is so much more powerful for context."
> — Danny Postma (@dannypostma)

> "Yep i even let Claude Code load them al in folders as markdown files and add specific yaml tags at the top. This is perfect for RAG. No vector store needed lol all locally. Insane"
> — Guido Schmitz (@guidsen)

> "local files + a good folder structure changed everything. context windows feel way bigger when you actually own your stuff. syncing is the pain now"
> — Steve grins (@stevegsn)

> "Suddenly my laziness... to avoid file and folder structure clearly... has evaporated... Because then half the work is done I imagine as far efficient context and token usage is set."
> — Tushar Chugh (@TusharChugh_)

## Open questions / follow-ups


- **Collaboration at Scale**: How do teams maintain "local-first" context ownership while coordinating across multiple employees? (Conflicts with centralized cloud storage).
- **The "Memory" Limit**: Will large local repos eventually hit the limits of what a single agent can maintain in its context window without falling back to specialized RAG?
- **Mobile Access**: How to maintain this "local context" advantage on devices that don't have a traditional file system or CLI (iOS/Android)?

## Next steps

- Explore the `obsidian-claude-pkm` github repo mentioned in the thread for better Obsidian integration.
- Evaluate `offlineIMAP` for bringing email historical context into the project's knowledge base.
- Consider moving existing Notion docs to the `nodes/` or `raw/` folders for better agent reach.

## Links

- Original Thread: [https://x.com/dannypostma/status/2011065092843139291](https://x.com/dannypostma/status/2011065092843139291)
- Alan Kay Paper (cited): [Kay1977.pdf](https://augmentingcognition.com/assets/Kay1977.pdf)
- Obsidian-Claude PKM: [https://github.com/ballred/obsidian-claude-pkm](https://github.com/ballred/obsidian-claude-pkm)
- OfflineIMAP: [https://offlineimap.org](https://offlineimap.org)
