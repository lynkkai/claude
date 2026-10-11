"""Reply context packages. Claude Code writes the draft; a person posts it."""

from __future__ import annotations

from pathlib import Path

from .config import Config
from .db import DB


def context_package(row) -> str:
    lines = [
        f"# Reply draft for {row['reddit_id']}",
        "",
        "Draft only. A person reads the thread, edits this, and posts it by hand.",
        "",
        "## The conversation",
        "",
        f"- Subreddit: {row['subreddit']}",
        f"- URL: {row['reddit_url']}",
        f"- Type: {row['type']}",
        f"- Username: u/{row['username']}",
        f"- Intent: {row['intent']} ({row['intent_score']})",
        f"- Relevance: {row['relevance_score']}",
        f"- Pain point: {row['pain_point'] or ''}",
        f"- Potential use case: {row['potential_use_case'] or ''}",
        f"- Context: {row['context'] or ''}",
        f"- Why reply: {row['reply_opportunity'] or ''}",
        "",
    ]
    if row["type"] == "comment":
        lines += [
            f"Parent post: {row['parent_post_title'] or ''}",
            f"Parent post URL: {row['parent_post_url'] or ''}",
            "",
            "Parent post excerpt:",
            "",
            _quote(row["parent_excerpt"] or ""),
            "",
            "The comment to reply to:",
            "",
            _quote(row["content"] or ""),
        ]
    else:
        lines += [f"Post title: {row['title']}", "", "Post:", "", _quote(row["content"] or "")]
    lines += ["", "## Draft reply", "", "(Claude Code writes the draft here, following docs/REPLY.md.)", ""]
    return "\n".join(lines)


def _quote(text: str) -> str:
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines()) or "> (empty)"


def write_draft_context(cfg: Config, db: DB, reddit_id: str) -> Path | None:
    row = db.get(reddit_id) or db.get(f"t3_{reddit_id}") or db.get(f"t1_{reddit_id}")
    if not row:
        return None
    cfg.drafts_dir.mkdir(parents=True, exist_ok=True)
    path = cfg.drafts_dir / f"{row['reddit_id']}.md"
    if not path.exists():
        path.write_text(context_package(row), encoding="utf-8")
    return path
