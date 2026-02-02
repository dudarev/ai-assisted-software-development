#!/usr/bin/env python3
import argparse
import json
import re
import sys

from youtube_search import YoutubeSearch


def parse_days_ago(publish_time):
    if not publish_time:
        return None
    text = publish_time.strip().lower()
    text = re.sub(r"^streamed\s+", "", text)
    
    # regex for English and Ukrainian
    # English: (\d+)\s+(second|minute|hour|day|week|month|year)s?\s+ago
    # Ukrainian: (\d+)\s+(.+?)\s+тому
    
    match = re.search(r"(\d+)\s+([a-zA-Zа-яА-ЯіІїЇєЄ]+)\s+(ago|тому)", text)
    if not match:
        return None
        
    value = int(match.group(1))
    unit = match.group(2)
    
    # English units
    if unit in ("second", "minute", "hour", "seconds", "minutes", "hours"):
        return 0
    if unit in ("day", "days"):
        return value
    if unit in ("week", "weeks"):
        return value * 7
    if unit in ("month", "months"):
        return value * 30
    if unit in ("year", "years"):
        return value * 365
        
    # Ukrainian units (approximate stems)
    # seconds: секунда, секунди, секунд
    # minutes: хвилина, хвилини, хвилин
    # hours: година, години, годин
    if any(u in unit for u in ["секунд", "хвилин", "годин"]):
        return 0
    
    # days: день, дні, днів
    if any(u in unit for u in ["день", "дні", "днів"]):
        return value
        
    # weeks: тиждень, тижні, тижнів
    if any(u in unit for u in ["тиждень", "тижні", "тижнів"]):
        return value * 7
        
    # months: місяць, місяці, місяців
    if any(u in unit for u in ["місяц"]):
        return value * 30
        
    # years: рік, роки, років
    if any(u in unit for u in ["рік", "рок"]):
        return value * 365
        
    return None


def search_last_days(query, max_results, days, include_unknown):
    results = YoutubeSearch(query, max_results=max_results).to_dict()
    filtered = []
    for item in results:
        days_ago = parse_days_ago(item.get("publish_time"))
        if days_ago is None:
            if not include_unknown:
                continue
        else:
            if days_ago > days:
                continue
        item["publish_days_ago"] = days_ago
        item["url"] = "https://www.youtube.com" + item.get("url_suffix", "")
        filtered.append(item)
    return filtered


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="YouTube search query")
    parser.add_argument("--days", type=int, default=7, help="Only include results from last N days")
    parser.add_argument("--max-results", type=int, default=25, help="Max results to fetch before filtering")
    parser.add_argument(
        "--include-unknown",
        action="store_true",
        help="Include results with unknown publish time",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON (default).",
    )
    args = parser.parse_args()

    items = search_last_days(args.query, args.max_results, args.days, args.include_unknown)

    output = {
        "query": args.query,
        "cutoff_days": args.days,
        "result_count": len(items),
        "results": items,
    }

    if args.json:
        json.dump(output, sys.stdout, ensure_ascii=True, indent=2)
    else:
        json.dump(output, sys.stdout, ensure_ascii=True, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
