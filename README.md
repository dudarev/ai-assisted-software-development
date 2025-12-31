# AI-Assisted Software Development

This repository is the public working area behind **ai-assisted-software-development.com**.

Its purpose is to collect, systematize, and evolve knowledge about **AI-assisted software development** — across the full software lifecycle: thinking, planning, design, implementation, testing, deployment, and maintenance.

The project is built **in public**. Ideas are refined over time, documents change, and assumptions are revisited. The history of the repository is part of the content.

## Repository roles

This repository is the **knowledge base** (source content).

The website is published from a separate “site” repository (`ai-assisted-software-development-com`) that pulls this content and builds/deploys it.

## Publishing workflow (content → site)

The publishing repo is `dudarev/ai-assisted-software-development-com` (Hugo + Cloudflare Pages).

The workflow follows [a simple principle](https://dev.dudarev.com/publishing-obsidian-notes-to-a-public-site-overview/): mark what should be published, then export/build from a clean, publish-ready directory.

Minimal loop:

1. Write notes under `notes/` with a `publish` tag in frontmatter.
2. Commit and push to `main`.
3. A GitHub Action dispatches an update to the site repo.
4. The site repo updates its `content` submodule and Cloudflare Pages rebuilds; the site build filters to `publish`-tagged pages.

### One-time setup (GitHub)

To enable the cross-repo trigger, add a secret in this repo:

- `SITE_REPO_DISPATCH_TOKEN`: a GitHub token that can call `repository_dispatch` on `dudarev/ai-assisted-software-development-com` (a classic PAT with `repo` scope is sufficient).

## What this repository is

- A growing **knowledge base / wiki**
- A place to **publish notes, patterns, and mental models**
- A record of **experiments and workflows** for using AI in software development
- A companion to newsletters, talks, and short videos

## What this repository is not

- A polished course
- A static reference
- A collection of generic AI prompts

Clarity and usefulness matter more than completeness.

## How to read this repository

- Start with high-level concepts and principles
- Follow links to concrete examples and experiments
- Treat documents as snapshots of thinking at a given time

## Status

This repository is intentionally minimal at the beginning.  
Structure, conventions, and content will evolve as understanding deepens.

## License

Content is shared openly unless stated otherwise. Reuse with attribution is encouraged.
