---
title: "Team Collaboration with AI Agents for Knowledge Work"
source_url: "https://x.com/petergyang/status/2009022922510487593"
captured_at: "2026-01-08"
distilled_at: "2026-01-08T15:35:00Z"
raw_refs:
  - "[[raw/2026-01-08T172702+0200 - Thread by @petergyang]]"
capture_type: "twitter_thread"
status: draft
agent: antigravity
model: gemini-3-flash
confidence_notes: "None"
tags: ["ai-agents", "collaboration", "knowledge-work", "claude-code", "mcp"]
---

## Summary

<!-- TODO: These are thoughts that AI tools are mostly not collaborative at the moment and there is divide between tools for collaboration with people and tools for collaboration with AI. and the ways to connect them. More thoughts are needed how to connect them on my side. -->

The thread explores the friction between local-first AI coding tools (like Claude Code) and the collaborative needs of knowledge work such as specs, roadmaps, and PRDs. While AI tools excel at editing local Markdown files, they often bypass the real-time collaboration, commenting, and "one-click share" capabilities of platforms like Google Docs or Notion. Participants discuss various strategies to bridge this gap, ranging from using MCP (Model Context Protocol) servers for cloud tools to "embracing Git" for all documentation, highlighting a significant transition in how teams manage their shared source of truth in an agent-led workflow.

## Key points

- **Local Documentation vs. Collaboration:** Local Markdown files for product specs do not natively solve the team collaboration problem compared to established tools like Google Docs.
- **Git as Documentation Engine:** Using Git for specs and roadmaps is a viable solution for technical teams, but can be perceived as "overkill" and high-friction for non-technical members.
- **MCP as the Bridge:** Model Context Protocol (MCP) servers for Google Workspace, Notion, Jira, and Confluence are the primary mechanism for giving CLI-based agents access to collaborative cloud environments.
- **Notion as the Middle Ground:** Notion is frequently cited as a superior middle ground, combining Markdown familiarity with robust collaboration and integrated AI (Notion AI).
- **Hybrid Sync Workflows:** Many practitioners use "bridges" like Google Drive for Desktop or custom sync scripts to expose cloud-hosted documentation as local files for AI processing.
- **The "Share Button" Moat:** The ubiquitous "blue share button" and the ability to leave granular comments remain critical advantages of cloud tools over pure file-based AI workflows.

## Concepts / principles

- **Tooling Bifurcation:** A growing divide between developer-centric AI tools (CLI, Git) and human-centric collaboration tools (Google Docs, Notion), creating friction in cross-functional work.
- **Source of Truth Conflict:** Teams face a dilemma over whether the "final" spec lives in the repository (for agent context) or in a collaborative doc (for stakeholder discussion).
- **Multiplayer AI:** The evolution of AI agents from single-file "editors" to participants in "multiplayer" environments that require awareness of comments, history, and shared permissions.
- **Revision Control for Everything:** As AI handles more documentation, the need for Git-like features (history, rollback, diffs) in traditionally "soft" documents like PRDs becomes essential to avoid "invisible edits."

## Patterns

- **Spec-in-PR:** Treating documentation exactly like code, where all collaboration, discussion, and approvals happen via GitHub Pull Requests.
- **Local Drive Bridge:** Installing cloud storage apps (Google Drive for Desktop, Dropbox) so that shared cloud folders appear as local directories, allowing AI agents to read/write shared files directly.
- **Bidirectional Syncing:** Implementing scripts or specialized tools (e.g., TaskletAI, custom Go CLIs) that keep local Markdown files in sync with Google Docs or Notion.
- **MCP Integration:** Configuring agents with MCP servers to provide API-level access to cloud knowledge bases without moving files to the local system.

## Entities

- **Core Tools:** Claude Code, Cursor, Google Docs/Sheets, Notion, Linear, Obsidian, Jira, Confluence, Asana.
- **Emerging Solutions:** [TaskletAI](https://tasklet.ai), [LumifyHub](https://lumifyhub.io), [Prodmoh](https://prodmoh.com), [TabTabTab](https://tabtabtab.ai), [Recapped.io](https://recapped.io), [Momental](https://momental.so), [WithMargin](https://withmargin.com), [Anytype](https://anytype.io).
- **Protocols/Platforms:** MCP (Model Context Protocol), GitHub, Google Drive for Desktop, [GitBook](https://www.gitbook.com).
- **Key People:** @petergyang (Thread author), @ChanduThota, @thomasrice_au, @EyalToledano, @pitachoi, @dmwlff.

## Quotes

> Local md files for specs and roadmaps don't solve the collaboration problem—unless the answer is storing them in a GitHub repo and having teammates submit PRs to change a spec?
> 
> — @petergyang

> If you're letting AI modify your files, I think it's really important to have a clear sense of what it's modifying and the ability to unwind it.
> 
> — @thomasrice_au

> Docs are still the shared source of truth for non devs, but once you let Claude touch them you need repo style history, review, and rollback or you end up arguing over invisible edits instead of decisions.
> 
> — @anayatkhan09

> None of these general AI solutions have solved collaboration... it is and will be a dev tool first and foremost for this reason.
> 
> — @marcfdupuis

> everything is a markdown file in a repo. change to a doc == PR.
> 
> — @0xRaduan

## Open questions / follow-ups

- Which MCP servers provide the most reliable write access to Google Docs without destroying formatting?
- What are the specific friction points when asking non-technical stakeholders to use Git-based documentation workflows?
- Are there emerging "AI-native" document formats that combine the collaboration of GDocs with the machine-readability of Markdown?

## Next steps

- **Research:** Evaluate the current state of Google Workspace MCP servers for stable "edit" capabilities.
- **Experiment:** Test a "Local Drive Bridge" workflow using Claude Code and a shared Google Drive folder for project specs.
- **Integration:** Consider if a Notion-based workflow with an MCP bridge would serve as a better "source of truth" for this project than pure Markdown files.

## Links

- Source: [https://x.com/petergyang/status/2009022922510487593](https://x.com/petergyang/status/2009022922510487593)
- [TaskletAI](https://tasklet.ai)
- [LumifyHub](https://lumifyhub.io)
- [Prodmoh](https://prodmoh.com)
- [TabTabTab](https://tabtabtab.ai)
- [Recapped.io](https://recapped.io)
- [Momental](https://momental.so)
- [WithMargin](https://withmargin.com)
- [Anytype](https://anytype.io)
- [gogcli (GitHub)](https://github.com/steipete/gogcli)
- [GitBook](https://www.gitbook.com)
- **Relevant MCP Servers:**
  - [Google Drive / Docs MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/googledrive) (Official)
  - [Notion MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/notion) (Official)
  - [GitHub MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/github) (Official)
  - [Atlassian (Jira/Confluence) MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/atlassian) (Official)
  - [Linear MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/linear) (Official)
  - [Slack MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) (Official)
  - [Asana MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/asana) (Community/Reference)
