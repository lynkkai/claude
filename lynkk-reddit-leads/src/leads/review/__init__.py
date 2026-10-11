"""Hand-off to Claude Code: write a batch to review, read the verdicts back."""

from __future__ import annotations

import json
from pathlib import Path

from ..config import Config
from ..db import DB
from ..models import INTENTS

REVIEW_CONTENT_CHARS = 2500
PARENT_EXCERPT_CHARS = 600
# Keep each batch small enough for Claude Code to read in one go.
MAX_BATCH_CHARS = 25_000

FIELDS = {
    "id": str,
    "relevance_score": int,
    "intent": str,
    "intent_score": int,
    "pain_point": str,
    "context": str,
    "potential_use_case": str,
    "reply_opportunity": str,
    "is_promotional": bool,
}


def batch_path(cfg: Config) -> Path:
    return cfg.work_dir / "batch.json"


def results_path(cfg: Config) -> Path:
    return cfg.work_dir / "batch.results.jsonl"


def write_batch(cfg: Config, db: DB, size: int | None = None) -> tuple[Path, int, int]:
    """Writes the next batch for review. Returns path, batch size, total waiting."""
    rows = db.pending_review(size or cfg.batch_size)
    cfg.work_dir.mkdir(parents=True, exist_ok=True)
    items, used = [], 0
    for r in rows:
        content = r["content"] or ""
        if len(content) > REVIEW_CONTENT_CHARS:
            content = content[:REVIEW_CONTENT_CHARS] + " [trimmed for review]"
        item = {
            "id": r["reddit_id"],
            "type": r["type"],
            "subreddit": r["subreddit"],
            "username": r["username"],
            "created_at": r["created_at"],
            "title": r["title"] if r["type"] == "post" else "",
            "content": content,
            "matched_keywords": json.loads(r["matched_keywords"] or "[]"),
            "rule_score": r["rule_score"],
            "rule_signals": json.loads(r["rule_signals"] or "[]"),
        }
        if r["type"] == "comment":
            item["parent_post_title"] = r["parent_post_title"]
            item["parent_post_excerpt"] = (r["parent_excerpt"] or "")[:PARENT_EXCERPT_CHARS]
        size = len(json.dumps(item, ensure_ascii=False))
        if items and used + size > MAX_BATCH_CHARS:
            break
        items.append(item)
        used += size
    path = batch_path(cfg)
    payload = {
        "instructions": "Classify every item using docs/CLASSIFY.md. Write one JSON object per line "
        f"to {results_path(cfg).relative_to(cfg.root)}, then run: uv run leads review apply",
        "items": items,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path, len(items), db.count_pending()


def validate(obj: dict) -> list[str]:
    errors = []
    for name, kind in FIELDS.items():
        if name not in obj:
            errors.append(f"missing {name}")
            continue
        v = obj[name]
        if kind is int and not (isinstance(v, int) and not isinstance(v, bool) and 0 <= v <= 100):
            errors.append(f"{name} must be a whole number 0 to 100")
        elif kind is str and not isinstance(v, str):
            errors.append(f"{name} must be text")
        elif kind is bool and not isinstance(v, bool):
            errors.append(f"{name} must be true or false")
    if obj.get("intent") not in INTENTS:
        errors.append(f"intent must be one of {', '.join(INTENTS)}")
    return errors


def apply_results(cfg: Config, db: DB, path: Path | None = None) -> tuple[int, list[str]]:
    """Saves Claude Code's verdicts. Returns how many were saved and any errors."""
    path = path or results_path(cfg)
    if not path.exists():
        return 0, [f"{path} not found"]
    saved, errors = 0, []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"line {n}: not valid JSON ({e.msg})")
            continue
        problems = validate(obj)
        if not db.get(str(obj.get("id", ""))):
            problems.append(f"unknown id {obj.get('id')!r}")
        if problems:
            errors.append(f"line {n} ({obj.get('id', '?')}): " + "; ".join(problems))
            continue
        db.save_review(obj["id"], obj)
        saved += 1
    db.commit()
    if not errors:
        path.unlink()
        bp = batch_path(cfg)
        if bp.exists():
            bp.unlink()
    return saved, errors
