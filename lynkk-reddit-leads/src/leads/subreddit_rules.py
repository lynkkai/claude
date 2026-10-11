"""Subreddit rules: read once a month per subreddit, summarized for review and export.

Rules come from Reddit's public about/rules.json (read only, one request per
subreddit). A keyword check flags rules that limit self-promotion; Claude Code
reads the rules themselves and makes the actual call on mentioning Lynkk.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone

from .config import Config
from .db import DB
from .reddit.http import BudgetSpent, RedditBlocked

PROMO_RULE = re.compile(
    r"self[\s-]?promo|promot|advertis|\bspam|affiliate|referral|solicit|marketing|\b10 ?%|shill"
    r"|no links|link to your|your own (product|app|business|startup|tool|service)|vendor|sales ?pitch",
    re.I,
)

POLICY_LABELS = {
    "restricts": "self-promotion restricted",
    "none_found": "no self-promotion rule found",
    "unavailable": "rules unavailable (private, banned or blocked)",
    "": "rules not fetched yet",
}

SUMMARY_CHARS = 900


def parse_rules(body: str) -> list[dict]:
    """Reddit's rules.json as [{"title", "text"}]. Empty on anything unexpected."""
    try:
        data = json.loads(body or "{}")
    except json.JSONDecodeError:
        return []
    out = []
    for r in data.get("rules") or []:
        title = (r.get("short_name") or "").strip()
        text = re.sub(r"\s+", " ", (r.get("description") or "")).strip()
        if title or text:
            out.append({"title": title, "text": text})
    return out


def promo_policy(rules: list[dict]) -> str:
    if not rules:
        return "none_found"
    hit = any(PROMO_RULE.search(f"{r['title']} {r['text']}") for r in rules)
    return "restricts" if hit else "none_found"


def summary(rules: list[dict], policy: str, limit: int = SUMMARY_CHARS) -> str:
    """One line per rule, promotion rules first, cut to fit a spreadsheet cell."""
    label = POLICY_LABELS.get(policy, policy)
    if not rules:
        return f"[{label}]"
    promo = [r for r in rules if PROMO_RULE.search(f"{r['title']} {r['text']}")]
    ordered = promo + [r for r in rules if r not in promo]
    parts = []
    for n, r in enumerate(ordered, 1):
        text = r["text"]
        if r in promo:
            text = text[:300]
        else:
            text = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0][:120]
        parts.append(f"{n}. {r['title']}" + (f": {text}" if text else ""))
    out = f"[{label}] " + " | ".join(parts)
    return out if len(out) <= limit else out[: limit - 3] + "..."


def fetch_rules(cfg: Config, db: DB, source, log=print, limit: int | None = None) -> tuple[int, int]:
    """Reads rules for subreddits that have candidates and no fresh rules.
    Returns (fetched, unavailable)."""
    refresh_before = (datetime.now(timezone.utc) - timedelta(days=cfg.rules_refresh_days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    subs = db.subreddits_needing_rules(cfg.review_threshold, refresh_before, limit or cfg.rules_max_per_run)
    if not subs:
        log("All subreddits with candidates have fresh rules.")
        return 0, 0
    log(f"Reading rules for {len(subs)} subreddits (about one a minute).")
    fetched = unavailable = blocked_in_a_row = 0
    for sub in subs:
        name = sub.removeprefix("r/")
        try:
            body = source.rules(name)
            blocked_in_a_row = 0
        except RedditBlocked:
            # A private or banned subreddit answers 403 too. Two in a row means
            # the network is blocked, so stop instead of spending the budget.
            blocked_in_a_row += 1
            if blocked_in_a_row >= 2:
                log("  Reddit refused twice in a row; stopping. Try again later.")
                break
            body = None
        except BudgetSpent:
            log("  request budget spent; the rest are read next run.")
            break
        if not body:
            db.save_rules(sub, [], "unavailable")
            unavailable += 1
            log(f"  {sub}: unavailable")
            continue
        rules = parse_rules(body)
        policy = promo_policy(rules)
        db.save_rules(sub, rules, policy)
        fetched += 1
        log(f"  {sub}: {len(rules)} rules, {POLICY_LABELS[policy]}")
    return fetched, unavailable
