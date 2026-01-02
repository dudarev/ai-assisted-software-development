---
name: get-web-page-raw
description: Capture a web page as raw material (extracted text/Markdown) with metadata, storing it in the raw/ directory for later distillation.
---

# Get Web Page (Raw)

## When to use

Use this skill when:
- The user provides a URL to capture as source material
- You need to store a web page for later distillation
- You're building up raw materials for the distillation pipeline

**Keywords:** capture, web page, URL, fetch, raw

## Inputs

Required:
- `url` (string): The URL of the web page to capture

Optional:
- `title_hint` (string): A human-provided hint for the title if extraction fails

## Outputs

This skill produces:
1. A new file in `raw/` with the naming pattern: `YYYYMMDD-HHMMSSZ--<slug>.md`
2. Metadata returned to the agent:
   - `raw_path`: full path to the created file
   - `title`: extracted or inferred title
   - `canonical_url`: canonical URL if found, otherwise the input URL
   - `captured_at`: ISO timestamp (UTC)

## Procedure

### 1. Generate timestamp and slug

- Get current UTC timestamp in format: `YYYYMMDD-HHMMSSZ`
- Create a slug from the URL or title:
  - Extract meaningful words from the URL path or page title
  - Convert to lowercase
  - Replace spaces/special chars with hyphens
  - Keep it 6-12 words maximum
  - Example: `openai-agent-standards` or `building-agents-with-claude`

### 2. Fetch the web page content

Use one of these methods (in priority order):

**Option A: Browser-based extraction (preferred for complex pages)**
- Use browser tools to navigate to the URL
- Wait for page load
- Extract text content in Markdown format
- Capture `<title>` tag and any `<link rel="canonical">` if present

**Option B: Simple HTTP fetch (good for basic pages)**
- Use `curl` or similar to fetch the HTML
- Extract text and convert to Markdown
- Parse `<title>` and `<link rel="canonical">` from HTML

**Failure handling:**
- If you get 403/blocked: note this in the status and capture what you can
- If redirect occurs: follow it and use the final URL
- If content is too large (>5MB): note this and ask user if they want to proceed

### 3. Build front matter

Create YAML front matter with these required fields:

```yaml
---
title: "<extracted or provided title>"
source_url: "<original URL provided by user>"
captured_at: "<ISO timestamp, e.g. 2026-01-02T14:22:33Z>"
capture_type: web_page
capture_tool: "<browser|curl|manual>"
raw_format: markdown
status: captured
---
```

Optional fields to include when available:
- `canonical_url`: if different from source_url
- `author`: if clearly identifiable
- `published_at`: if clearly identifiable (ISO format)
- `tags`: lightweight labels based on content

### 4. Write the file

- Construct filename: `<timestamp>--<slug>.md`
- Full path: `raw/<filename>`
- Content structure:
  ```
  ---
  <front matter>
  ---
  
  <extracted page content as Markdown>
  ```

### 5. Return metadata

Provide these values to the user/calling agent:
- Path where the file was saved
- Title that was captured
- Confirmation of capture timestamp

## Examples

### Example 1: Blog post capture

**Input:**
```
url: "https://www.anthropic.com/news/building-effective-agents"
```

**Actions:**
1. Fetch page with browser tools
2. Extract title: "Building effective agents"
3. Generate timestamp: `20260102-143000Z`
4. Create slug: `building-effective-agents`
5. Write to: `raw/20260102-143000Z--building-effective-agents.md`

**Output file front matter:**
```yaml
---
title: "Building effective agents"
source_url: "https://www.anthropic.com/news/building-effective-agents"
captured_at: "2026-01-02T14:30:00Z"
capture_type: web_page
capture_tool: browser
raw_format: markdown
status: captured
author: "Anthropic"
published_at: "2024-11-01T00:00:00Z"
tags: [ai-agent, anthropic, best-practices]
---
```

### Example 2: Simple page with manual title hint

**Input:**
```
url: "https://example.com/page-123"
title_hint: "Agent Design Patterns"
```

**Actions:**
1. Fetch page with curl
2. Title extraction fails, use hint: "Agent Design Patterns"
3. Generate timestamp: `20260102-150000Z`
4. Create slug: `agent-design-patterns`
5. Write to: `raw/20260102-150000Z--agent-design-patterns.md`

**Output file front matter:**
```yaml
---
title: "Agent Design Patterns"
source_url: "https://example.com/page-123"
captured_at: "2026-01-02T15:00:00Z"
capture_type: web_page
capture_tool: curl
raw_format: markdown
status: captured
---
```

## Edge cases

**Missing title:**
- Try: `<title>` tag, `<h1>` tag, OpenGraph meta tag
- Fallback: use `title_hint` if provided
- Last resort: use URL path or "Untitled Page"

**Authentication required:**
- Capture what you can from the error page
- Set `status: capture-failed`
- Add `failure_reason` field to front matter
- Ask user if they can provide credentials or alternative access

**Very large pages:**
- Warn if content exceeds 1MB
- Ask user to confirm before storing
- Consider truncating at a reasonable boundary

**Binary/non-HTML content:**
- If URL points to PDF/image/etc., note this
- Ask user if they want to download it or skip
- If proceeding, store the file with appropriate extension

**Rate limiting:**
- If you detect rate limiting (429 status), wait and retry once
- If it persists, inform user and skip

## References

- Parent workflow: `docs/distillation/distillation-pipeline.md`
- Front matter schema: see "Raw file front matter" in distillation-pipeline.md
- Next step after capture: use `make-distilled` skill to process this raw file
