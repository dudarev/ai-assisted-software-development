---
name: youtube-search
description: Search YouTube for recent videos using the python youtube_search library, especially when you need last-7-days results or want to filter by publish time without the YouTube Data API.
---

# YouTube Search (Last 7 Days)

## Prerequisites

- `python3`
- `youtube-search` library installed (pip package name is typically `youtube-search`)

## Quick start

```bash
python3 scripts/search_youtube_last_week.py "your query" --days 7 --max-results 25 --json
```

## Notes

- The script filters results by parsing the human publish time (e.g., "2 days ago").
- If publish time cannot be parsed, results are excluded unless `--include-unknown` is set.
- Output is JSON with `results[]` entries and a computed `url` field.
