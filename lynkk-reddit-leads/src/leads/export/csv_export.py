"""CSV export that opens cleanly in Google Sheets, Excel, Numbers and pandas.

- UTF-8 with a byte order mark, so Excel shows emoji and accents correctly
  (pandas: read_csv(path, encoding="utf-8-sig"); plain "utf-8" also works and
  leaves the mark on the first column name).
- Every field quoted; commas, quotes and newlines inside Reddit text are safe.
- Text that starts with = + - @ gets a leading apostrophe so spreadsheets
  don't run it as a formula.
- Excel cells hold at most 32,767 characters; longer posts are cut there with
  a note (the full text stays in the database and on Reddit).
"""

from __future__ import annotations

import csv
from pathlib import Path

COLUMNS = [
    "id", "type", "username", "content", "title", "subreddit", "reddit_url", "author_url",
    "created_at", "keyword_matched", "matched_keywords", "relevance_score", "intent",
    "intent_score", "pain_point", "context", "potential_use_case", "reply_opportunity",
    # extras, after the required columns
    "parent_post_url", "reviewed_by", "first_seen_at",
]

EXCEL_CELL_LIMIT = 32_000
FORMULA_START = ("=", "+", "-", "@", "\t", "\r")


def _cell(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        value = "; ".join(str(v) for v in value)
    s = str(value).replace("\x00", "")
    if len(s) > EXCEL_CELL_LIMIT:
        s = s[:EXCEL_CELL_LIMIT] + " [cut for spreadsheet limits, open reddit_url for the rest]"
    if s.startswith(FORMULA_START):
        s = "'" + s
    return s


def fields(item: dict) -> dict:
    """The CSV columns for one stored item, unescaped."""
    return {
        "id": item["reddit_id"],
        "type": item["type"],
        "username": item["username"],
        "content": item["content"],
        "title": item["title"] if item["type"] == "post" else (item.get("parent_post_title") or item["title"]),
        "subreddit": item["subreddit"],
        "reddit_url": item["reddit_url"],
        "author_url": item["author_url"],
        "created_at": item["created_at"],
        "keyword_matched": item["keyword_matched"],
        "matched_keywords": item["matched_keywords"],
        "relevance_score": item["relevance_score"],
        "intent": item["intent"],
        "intent_score": item["intent_score"],
        "pain_point": item.get("pain_point"),
        "context": item.get("context"),
        "potential_use_case": item.get("potential_use_case"),
        "reply_opportunity": item.get("reply_opportunity"),
        "parent_post_url": item.get("parent_post_url"),
        "reviewed_by": item.get("reviewed_by"),
        "first_seen_at": item.get("first_seen_at"),
    }


def to_csv_row(item: dict) -> dict:
    row = fields(item)
    return {k: v if k in ("relevance_score", "intent_score") and isinstance(v, int) else _cell(v) for k, v in row.items()}


def write_csv(path: Path, items: list[dict]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
        w.writeheader()
        for it in items:
            w.writerow(to_csv_row(it))
    return path
