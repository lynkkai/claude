"""SQLite storage: searches, reddit_items and keywords."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from .models import Item

SCHEMA = """
CREATE TABLE IF NOT EXISTS searches (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  query TEXT NOT NULL,
  created_at TEXT NOT NULL,
  status TEXT NOT NULL,
  results INTEGER NOT NULL DEFAULT 0,
  new_items INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS keywords (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  keyword TEXT NOT NULL UNIQUE,
  enabled INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS reddit_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  reddit_id TEXT NOT NULL UNIQUE,
  platform TEXT NOT NULL DEFAULT 'reddit',
  type TEXT NOT NULL,
  username TEXT,
  content TEXT,
  title TEXT,
  subreddit TEXT,
  reddit_url TEXT,
  canonical_url TEXT,
  author_url TEXT,
  created_at TEXT,
  parent_post_id TEXT,
  parent_post_title TEXT,
  parent_post_url TEXT,
  parent_excerpt TEXT,
  keyword_matched TEXT,
  matched_keywords TEXT,          -- JSON list
  source TEXT,
  content_hash TEXT,
  rule_score INTEGER,
  rule_signals TEXT,              -- JSON list
  relevance_score INTEGER,
  intent TEXT,
  intent_score INTEGER,
  pain_point TEXT,
  context TEXT,
  potential_use_case TEXT,
  reply_opportunity TEXT,
  is_promotional INTEGER,
  reviewed_by TEXT,               -- 'rules' or 'claude'
  status TEXT NOT NULL,           -- review, skipped, duplicate, reviewed
  duplicate_of TEXT,
  first_seen_at TEXT NOT NULL,
  last_seen_at TEXT NOT NULL,
  reviewed_at TEXT,
  exported_at TEXT,
  thread_fetched_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_items_status ON reddit_items(status);
CREATE INDEX IF NOT EXISTS idx_items_hash ON reddit_items(content_hash);
CREATE INDEX IF NOT EXISTS idx_items_url ON reddit_items(canonical_url);
"""


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class DB:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(path, timeout=30)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    def close(self):
        if self.conn is None:
            return
        self.conn.commit()
        self.conn.close()
        self.conn = None

    # searches -----------------------------------------------------------

    def log_search(self, query: str, status: str, results: int, new_items: int) -> None:
        self.conn.execute(
            "INSERT INTO searches(query, created_at, status, results, new_items) VALUES (?,?,?,?,?)",
            (query, now_iso(), status, results, new_items),
        )
        self.conn.commit()

    def last_search_at(self) -> str | None:
        row = self.conn.execute("SELECT MAX(created_at) FROM searches").fetchone()
        return row[0]

    # keywords -----------------------------------------------------------

    def sync_keywords(self, keywords: list[str]) -> None:
        """Mirrors config.toml: listed keywords enabled, removed ones disabled."""
        stamp = now_iso()
        self.conn.execute("UPDATE keywords SET enabled = 0")
        for k in keywords:
            self.conn.execute(
                "INSERT INTO keywords(keyword, enabled, created_at) VALUES (?,1,?) "
                "ON CONFLICT(keyword) DO UPDATE SET enabled = 1",
                (k, stamp),
            )
        self.conn.commit()

    # items --------------------------------------------------------------

    def get(self, reddit_id: str) -> sqlite3.Row | None:
        return self.conn.execute("SELECT * FROM reddit_items WHERE reddit_id = ?", (reddit_id,)).fetchone()

    def find_by_url(self, canonical: str) -> sqlite3.Row | None:
        if not canonical:
            return None
        return self.conn.execute("SELECT * FROM reddit_items WHERE canonical_url = ?", (canonical,)).fetchone()

    def find_by_hash(self, h: str, exclude_id: str) -> sqlite3.Row | None:
        if not h:
            return None
        return self.conn.execute(
            "SELECT * FROM reddit_items WHERE content_hash = ? AND reddit_id != ? ORDER BY first_seen_at LIMIT 1",
            (h, exclude_id),
        ).fetchone()

    def touch(self, reddit_id: str, extra_keywords: list[str]) -> None:
        """A known item was seen again: merge keywords, skip reprocessing."""
        row = self.get(reddit_id)
        if not row:
            return
        kws = json.loads(row["matched_keywords"] or "[]")
        for k in extra_keywords:
            if k not in kws:
                kws.append(k)
        self.conn.execute(
            "UPDATE reddit_items SET matched_keywords = ?, last_seen_at = ? WHERE reddit_id = ?",
            (json.dumps(kws), now_iso(), reddit_id),
        )

    def upsert(self, it: Item, *, canonical: str, content_hash: str, rule_score: int, signals: list[str],
               relevance: int, intent: str, intent_score: int, status: str, duplicate_of: str = "") -> None:
        stamp = now_iso()
        existing = self.get(it.reddit_id)
        values = dict(
            reddit_id=it.reddit_id, platform=it.platform, type=it.type, username=it.username,
            content=it.content, title=it.title, subreddit=it.subreddit, reddit_url=it.reddit_url,
            canonical_url=canonical, author_url=it.author_url, created_at=it.created_at,
            parent_post_id=it.parent_post_id, parent_post_title=it.parent_post_title,
            parent_post_url=it.parent_post_url, parent_excerpt=it.parent_excerpt,
            keyword_matched=it.keyword_matched, matched_keywords=json.dumps(it.matched_keywords),
            source=it.source, content_hash=content_hash, rule_score=rule_score,
            rule_signals=json.dumps(signals), relevance_score=relevance, intent=intent,
            intent_score=intent_score, reviewed_by="rules", status=status, duplicate_of=duplicate_of,
            last_seen_at=stamp,
        )
        if existing:
            # Re-scan: refresh the data, clear the old review so it is reviewed again.
            values.update(pain_point=None, context=None, potential_use_case=None,
                          reply_opportunity=None, is_promotional=None, reviewed_at=None)
            sets = ", ".join(f"{k} = :{k}" for k in values)
            self.conn.execute(f"UPDATE reddit_items SET {sets} WHERE reddit_id = :reddit_id", values)
        else:
            values["first_seen_at"] = stamp
            cols = ", ".join(values)
            marks = ", ".join(f":{k}" for k in values)
            self.conn.execute(f"INSERT INTO reddit_items({cols}) VALUES ({marks})", values)

    def commit(self):
        self.conn.commit()

    def threads_to_fetch(self, min_score: int, limit: int, recent_since: str, refetch_before: str) -> list[sqlite3.Row]:
        """Posts worth reading the comments of: good score, recent, not read lately."""
        return self.conn.execute(
            """SELECT * FROM reddit_items
               WHERE type = 'post' AND status != 'duplicate'
                 AND COALESCE(relevance_score, rule_score) >= ?
                 AND created_at >= ?
                 AND (thread_fetched_at IS NULL OR thread_fetched_at < ?)
               ORDER BY COALESCE(relevance_score, rule_score) DESC, created_at DESC
               LIMIT ?""",
            (min_score, recent_since, refetch_before, limit),
        ).fetchall()

    def mark_thread_fetched(self, reddit_id: str) -> None:
        self.conn.execute("UPDATE reddit_items SET thread_fetched_at = ? WHERE reddit_id = ?", (now_iso(), reddit_id))

    # review ---------------------------------------------------------------

    def pending_review(self, limit: int) -> list[sqlite3.Row]:
        return self.conn.execute(
            "SELECT * FROM reddit_items WHERE status = 'review' ORDER BY rule_score DESC, created_at DESC LIMIT ?",
            (limit,),
        ).fetchall()

    def count_pending(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM reddit_items WHERE status = 'review'").fetchone()[0]

    def save_review(self, reddit_id: str, r: dict) -> None:
        self.conn.execute(
            """UPDATE reddit_items SET relevance_score = :relevance_score, intent = :intent,
                 intent_score = :intent_score, pain_point = :pain_point, context = :context,
                 potential_use_case = :potential_use_case, reply_opportunity = :reply_opportunity,
                 is_promotional = :is_promotional, reviewed_by = 'claude', status = 'reviewed',
                 reviewed_at = :reviewed_at
               WHERE reddit_id = :reddit_id""",
            {**r, "reddit_id": reddit_id, "is_promotional": int(bool(r["is_promotional"])), "reviewed_at": now_iso()},
        )

    # export -----------------------------------------------------------------

    def exportable(self, min_relevance: int) -> list[dict]:
        rows = self.conn.execute(
            """SELECT * FROM reddit_items
               WHERE status IN ('review', 'reviewed') AND relevance_score >= ?""",
            (min_relevance,),
        ).fetchall()
        return [_row(r) for r in rows]

    def all_items(self) -> list[dict]:
        return [_row(r) for r in self.conn.execute("SELECT * FROM reddit_items").fetchall()]

    def mark_exported(self, reddit_ids: list[str]) -> None:
        stamp = now_iso()
        self.conn.executemany(
            "UPDATE reddit_items SET exported_at = ? WHERE reddit_id = ? AND exported_at IS NULL",
            [(stamp, i) for i in reddit_ids],
        )
        self.conn.commit()

    def status_counts(self) -> dict[str, int]:
        rows = self.conn.execute("SELECT status, COUNT(*) FROM reddit_items GROUP BY status").fetchall()
        return {r[0]: r[1] for r in rows}


def _row(r: sqlite3.Row) -> dict:
    d = dict(r)
    d["matched_keywords"] = json.loads(d.get("matched_keywords") or "[]")
    d["rule_signals"] = json.loads(d.get("rule_signals") or "[]")
    return d
