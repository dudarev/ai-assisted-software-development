---
name: make-distilled
description: Transform raw captured content into distilled knowledge by extracting summary, key points, principles, patterns, entities, and quotes, storing the result in the distilled/ directory.
---

# Make Distilled Content

## When to use

Use this skill when:
- The user has a raw file in `raw/` and wants to extract structured insights
- You need to convert unprocessed source material into organized knowledge
- You're preparing content for integration into notes or essays

**Keywords:** distill, extract, summarize, patterns, principles, organize

## Inputs

Required:
- `raw_path` (string): Relative or absolute path to the raw file in `raw/`

Optional:
- `focus` (string): Specific aspect to emphasize (e.g., "patterns", "principles", "practical advice")

## Outputs

This skill produces:
1. A new file in `distilled/` with the same timestamp-slug naming pattern as the raw file
2. Metadata returned to the agent:
   - `distilled_path`: full path to the created distilled file
   - `title`: title of the distilled content
   - `distilled_at`: ISO timestamp (UTC)
   - `status`: initial status (typically "draft")

## Procedure

### 1. Read the raw file

- Use the `read_file` tool to load the entire raw file content
- Parse the front matter to extract:
  - `title`
  - `source_url`
  - `captured_at`
  - `capture_type`
  - `author` (if available)
  - `published_at` (if available)
  - any other relevant metadata

### 2. Generate distilled content structure

Extract and organize the following elements from the raw content:

**Summary** (5-10 lines)
- Concise overview of the main topic and purpose
- What problem/question does this address?
- What approach or solution is presented?

**Key points** (bullet list)
- 5-10 actionable or memorable insights
- Focus on practical takeaways
- Avoid restating the summary

**Concepts / principles**
- Abstract ideas or mental models
- Transferable patterns
- Underlying theory or philosophy
- Trade-offs and decision factors

**Patterns** (if relevant)
- Concrete, reusable approaches
- Workflow patterns
- Code/architectural patterns
- Team/organizational patterns

**Entities** (if relevant)
- Tools, frameworks, libraries mentioned
- People or organizations referenced
- Related projects or initiatives
- Terminology and definitions

**Quotes** (select 3-8 notable ones)
- Verbatim excerpts that are particularly insightful
- Include just enough context to be standalone
- Format as blockquotes with inline attribution if author is known

**Open questions / follow-ups**
- Gaps or areas for deeper research
- Connections to explore
- Uncertainties or ambiguities in the source

**Next steps** (agent-suggested)
- Suggested integration targets in `notes/`
- Related topics to capture or research
- Concepts worth expanding into standalone notes

### 3. Build front matter

Create YAML front matter for the distilled file:

```yaml
---
title: "<original title> (or improved title if clearer)"
source_url: "<from raw file>"
captured_at: "<from raw file>"
distilled_at: "<current ISO timestamp UTC>"
raw_ref: "<relative path from distilled/ to raw file>"
capture_type: "<from raw file>"
status: draft
agent: github-copilot
model: claude-sonnet-4.5
confidence_notes: "<any uncertainty flags, hallucination risks, or missing context>"
tags: ["tag1", "tag2", "tag3"]  # 3-7 relevant tags
---
```

**Critical rules:**
- Use `raw_ref` as a relative path (e.g., `../raw/20260102-095107Z--patterns.md`)
- Be explicit in `confidence_notes` if:
  - Author/date was inferred rather than explicit
  - Content was truncated or unclear
  - You're uncertain about any extraction
- The `status` should be `draft` unless the user specifies otherwise

### 4. Apply the distilled content template

Combine the extracted elements into this structure:

```markdown
---
<front matter from step 3>
---

## Summary

<5-10 line summary>

## Key points

- <point 1>
- <point 2>
- ...

## Concepts / principles

<extracted concepts, one per paragraph or sub-section>

## Patterns

<if relevant: concrete patterns found>

## Entities

<if relevant: tools, people, projects, terms>

## Quotes

> <quote 1>
> 
> — <attribution if known>

> <quote 2>

...

## Open questions / follow-ups

- <question or gap 1>
- <question or gap 2>

## Next steps

- <suggested action 1>
- <suggested action 2>

## Links

- Source: [<source_url>](<source_url>)
- Raw: [<raw filename>](<raw_ref>)
```

### 5. Generate filename and write the file

- Filename: Use the same timestamp and slug from the raw file
  - Example: if raw is `20260102-095107Z--patterns.md`, distilled is also `20260102-095107Z--patterns.md`
- Full path: `distilled/<filename>`
- Content: front matter + blank line + distilled structure
- Use `create_file` tool with the full content

### 6. Confirm to user

Provide a brief confirmation:
- Link to the created distilled file using relative path
- One-sentence summary of what was extracted
- Note any significant `confidence_notes` or gaps

## Quality guidelines

**Preserve intent and nuance**
- Do not "improve" the source's tone or claims
- If something is speculative in the source, preserve that uncertainty
- Avoid marketing language or hype

**Be explicit about uncertainty**
- Use `confidence_notes` front matter for extraction risks
- In the body, flag inferred vs. explicit information
- If author/date is missing, say so

**Favor principles over tools**
- Extract transferable ideas, not tool-specific instructions
- Highlight trade-offs and decision factors
- Patterns should be adaptable across contexts

**Short, precise, reusable**
- Clarity over verbosity
- Make each section independently useful
- Link concepts instead of duplicating them

**Avoid exposing private information**
- Do not include private repository names, local paths, or personal data
- Sanitize examples if they reference non-public systems

## Examples

### Example 1: Blog post about AI agent patterns

**Input:**
```
raw_path: raw/20260102-095107Z--patterns-for-ai-assisted-software-development.md
```

**Process:**
1. Read the raw file and extract metadata
2. Identify main patterns: interview-driven specs, progressive disclosure, etc.
3. Extract key principles: preserve intent, think in systems, avoid hype
4. Select 5-6 notable quotes
5. Note any follow-up questions (e.g., "How do these patterns scale to larger teams?")

**Output:**
- Creates `distilled/20260102-095107Z--patterns-for-ai-assisted-software-development.md`
- Front matter includes `raw_ref: ../raw/20260102-095107Z--patterns-for-ai-assisted-software-development.md`
- Structured summary + key points + concepts + quotes + next steps

### Example 2: YouTube transcript

**Input:**
```
raw_path: raw/20260105-140000Z--building-production-agents.md
```

**Process:**
1. Read the transcript
2. Extract main themes (often less linear than written content)
3. Identify practical advice vs. theoretical discussion
4. Note any tools or frameworks mentioned
5. Flag areas where transcript was unclear or incomplete

**Output:**
- Creates `distilled/20260105-140000Z--building-production-agents.md`
- `confidence_notes` might mention: "Transcript had several unclear segments; some technical terms may be misspelled"
- Entities section lists tools and frameworks discussed

## Failure modes and edge cases

**Truncated or incomplete raw content**
- Note in `confidence_notes`
- Extract what's available
- Suggest follow-up: "Consider re-capturing with full content"

**Highly technical content with domain-specific jargon**
- Preserve technical terms as-is
- Add brief context in Entities section if helpful
- Do not oversimplify at the cost of accuracy

**Opinion pieces vs. technical guides**
- For opinion: focus on arguments, not just conclusions
- For guides: emphasize patterns and principles over step-by-step

**Multiple topics in one source**
- Consider suggesting multiple distilled files focused on different aspects
- Or use clear sub-sections in a single distilled file

## Tools typically used

- `read_file` — to load the raw content
- `create_file` — to write the distilled output
- `run_in_terminal` — to generate UTC timestamp if needed

## References

- Distillation pipeline: [docs/distillation/distillation-pipeline.md](../../docs/distillation/distillation-pipeline.md)
- Agent skills standard: [notes/agent-skills.md](../../notes/agent-skills.md)
- Repository guidance: [AGENTS.md](../../AGENTS.md)
