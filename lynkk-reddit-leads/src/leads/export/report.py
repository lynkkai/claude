"""A single self-contained HTML report: dashboard, filters, sorting, CSV export."""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from ..analysis.intent import rank
from ..models import PRIORITY
from .csv_export import COLUMNS, fields

TEMPLATE = Path(__file__).with_name("report_template.html")


def build_stats(all_items: list[dict], relevant: list[dict]) -> dict:
    kw = Counter()
    for it in relevant:
        for k in it["matched_keywords"] or [it["keyword_matched"]]:
            if k:
                kw[k] += 1
    subs = Counter(it["subreddit"] for it in relevant if it["subreddit"])
    return {
        "total": len(all_items),
        "relevant": len(relevant),
        "high": sum(1 for it in relevant if PRIORITY.get(it["intent"], 3) == 0),
        "medium": sum(1 for it in relevant if PRIORITY.get(it["intent"], 3) == 1),
        "posts": sum(1 for it in relevant if it["type"] == "post"),
        "comments": sum(1 for it in relevant if it["type"] == "comment"),
        "subreddits": len(subs),
        "users": len({it["username"] for it in relevant}),
        "reviewed": sum(1 for it in relevant if it.get("reviewed_by") == "claude"),
        "top_keywords": kw.most_common(8),
        "top_subreddits": subs.most_common(8),
    }


def write_report(path: Path, all_items: list[dict], relevant: list[dict], new_ids: set[str]) -> Path:
    ranked = rank(relevant)
    rows = []
    for it in ranked:
        row = fields(it)
        row["_new"] = it["reddit_id"] in new_ids
        row["_parent_excerpt"] = it.get("parent_excerpt") or ""
        row["_parent_title"] = it.get("parent_post_title") or ""
        rows.append(row)
    data = {
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "stats": build_stats(all_items, relevant),
        "columns": COLUMNS,
        "rows": rows,
    }
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/null", blob)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    return path
