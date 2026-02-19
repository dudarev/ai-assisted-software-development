# Scripts

Small utilities for this repository. These are optional and not required for reading the docs.

Install deps:
1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r scripts/requirements.txt`

Run a script:
1. `python scripts/<script>.py`

YouTube raw stats:
- `python scripts/analyze_youtube_raw.py` (offline; channel stats require `--enrich` + `yt-dlp`)
- Enrichment tips: use `--timeout 25` (or higher on slow networks); failures are cached (skip unless `--retry-failures`); `--refresh-cache` forces re-fetch
