"""Trend sheets: which subreddits and keywords bring the conversations, and
what each subreddit's rules allow."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from ..models import PRIORITY
from ..subreddit_rules import POLICY_LABELS, summary
from .csv_export import _cell

SUBREDDIT_COLUMNS = [
    "subreddit", "relevant_items", "high_intent", "posts", "comments", "last_7_days",
    "top_keywords", "self_promotion_rule", "brand_mention_verdicts", "rules_summary",
]
KEYWORD_COLUMNS = ["keyword", "relevant_items", "last_7_days", "last_30_days", "high_intent", "top_subreddits"]


def _recent(created_at: str, days: int, now: datetime) -> bool:
    try:
        dt = datetime.fromisoformat((created_at or "").replace("Z", "+00:00"))
    except ValueError:
        return False
    return dt >= now - timedelta(days=days)


def _keywords(it: dict) -> list[str]:
    return [k for k in (it["matched_keywords"] or [it["keyword_matched"]]) if k]


def subreddit_rows(relevant: list[dict], rules: dict[str, dict], now: datetime) -> list[dict]:
    by_sub: dict[str, list[dict]] = defaultdict(list)
    for it in relevant:
        if it["subreddit"]:
            by_sub[it["subreddit"]].append(it)
    rows = []
    for sub, items in by_sub.items():
        kw = Counter(k for it in items for k in _keywords(it))
        verdicts = Counter(it["brand_mention"] for it in items if it.get("brand_mention"))
        known = rules.get(sub)
        policy = known["policy"] if known else ""
        rows.append({
            "subreddit": sub,
            "relevant_items": len(items),
            "high_intent": sum(1 for it in items if PRIORITY.get(it["intent"], 3) == 0),
            "posts": sum(1 for it in items if it["type"] == "post"),
            "comments": sum(1 for it in items if it["type"] == "comment"),
            "last_7_days": sum(1 for it in items if _recent(it["created_at"], 7, now)),
            "top_keywords": "; ".join(f"{k} ({n})" for k, n in kw.most_common(4)),
            "self_promotion_rule": POLICY_LABELS.get(policy, policy),
            "brand_mention_verdicts": "; ".join(f"{k} ({n})" for k, n in verdicts.most_common()),
            "rules_summary": summary(known["rules"], policy) if known else summary([], ""),
        })
    return sorted(rows, key=lambda r: (-r["high_intent"], -r["relevant_items"], r["subreddit"]))


def keyword_rows(relevant: list[dict], now: datetime) -> list[dict]:
    by_kw: dict[str, list[dict]] = defaultdict(list)
    for it in relevant:
        for k in _keywords(it):
            by_kw[k].append(it)
    rows = []
    for k, items in by_kw.items():
        subs = Counter(it["subreddit"] for it in items if it["subreddit"])
        rows.append({
            "keyword": k,
            "relevant_items": len(items),
            "last_7_days": sum(1 for it in items if _recent(it["created_at"], 7, now)),
            "last_30_days": sum(1 for it in items if _recent(it["created_at"], 30, now)),
            "high_intent": sum(1 for it in items if PRIORITY.get(it["intent"], 3) == 0),
            "top_subreddits": "; ".join(f"{s} ({n})" for s, n in subs.most_common(5)),
        })
    return sorted(rows, key=lambda r: (-r["relevant_items"], r["keyword"]))


def _write(path: Path, columns: list[str], rows: list[dict]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columns, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: v if isinstance(v, int) else _cell(v) for k, v in r.items()})
    return path


def write_trends(folder: Path, relevant: list[dict], rules: dict[str, dict], now: datetime | None = None) -> tuple[Path, Path]:
    now = now or datetime.now(timezone.utc)
    return (
        _write(folder / "subreddit_trends.csv", SUBREDDIT_COLUMNS, subreddit_rows(relevant, rules, now)),
        _write(folder / "keyword_trends.csv", KEYWORD_COLUMNS, keyword_rows(relevant, now)),
    )
