# AI Assistant Guidelines for People Notes

When generating, editing, or summarizing notes in the `notes/people/` directory, please follow these guidelines to ensure the content is high-quality, standalone, and ready for publication on a website.

## 1. General Framing
- **Standalone Context:** Many of these notes use the `publish` tag and will be displayed independently on a website. **Do not** write phrases like "In this vault, this person is known for..." or "In these documents, they are mentioned for...". 
- **Broad Overview First:** Always start with a general, well-rounded biographical summary of the person. Who are they? What is their background? (e.g., companies they've worked for, projects they've started, general areas of expertise).
- **Then Specialize:** After establishing their general background, seamlessly transition to why they are specifically relevant to *this knowledge base* (e.g., AI-assisted software engineering, vibe coding, agent orchestration).

## 2. Structure of a Person Note
A good note about a person should generally follow this structure:

1. **Frontmatter:** Include relevant tags (`person`, `publish`, relevant domain tags), an `active` boolean, `created` date, a `summary`, and `aliases` (such as common misspellings found in transcripts).
2. **H1 Header:** The person's name (e.g., `# Steve Yegge`).
3. **General Biography:** 1-2 paragraphs introducing them generally to any reader on the internet.
4. **Domain-Specific Contributions / Ideas:** H2 or H3 sections explaining their specific frameworks, mental models, quotes, or tools that are relevant to AI-assisted coding or related domains.
5. **Transcription Notes (Optional):** A brief note tracking known auto-captioning typos (e.g., "Yeager" instead of "Yegge") to aid in search and synthesis later.
6. **Related Notes:** Internal links to concepts or other people linked to them (e.g., `[[Landing the Plane]]`).
7. **External Links:** A bulleted list of authoritative external references (Wikipedia, personal blog, GitHub, important YouTube talks or articles). Format these cleanly using standard Markdown link syntax `[Link Text](URL)`.

## 3. Formatting Rules
- Use bullet points for distinct ideas, tools, or concepts.
- **Bold** key terms or concepts when they are first introduced to make the document skimmable.
- Standardize the links section under `## References` or `## External Links`. Always try to include a Wikipedia link if one exists.
- Ensure the tone remains objective, professional, and encyclopedic.

## 4. Work Process
- If asked to create a new person note, always use your web search capabilities to pull in their Wikipedia summary or general background before relying solely on internal reference context.
- Create placeholder internal links (`[[Like This]]`) for domain-specific concepts they are associated with, even if that actual concept note does not exist yet.
