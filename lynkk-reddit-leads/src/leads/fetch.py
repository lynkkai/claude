"""The fetch step: search, read threads and comment feeds, score, store."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

from .analysis import rules
from .analysis.dedupe import content_hash, dedupe
from .analysis.intent import rule_intent
from .analysis.keywords import Keyword, build_queries, competitor_alternative_keywords, match_keywords
from .config import Config
from .db import DB
from .models import Item
from .reddit.http import BudgetSpent, RedditBlocked
from .reddit.parse import canonical_url

PARENT_EXCERPT_CHARS = 800


@dataclass
class FetchStats:
    requests: int = 0
    found: int = 0
    new: int = 0
    for_review: int = 0
    skipped: int = 0
    duplicates: int = 0
    already_seen: int = 0
    too_old: int = 0
    stopped_early: str = ""
    by_status: dict = field(default_factory=dict)


class Fetcher:
    def __init__(self, cfg: Config, db: DB, source, rescan: bool = False, log=print, now: datetime | None = None):
        self.cfg = cfg
        self.db = db
        self.source = source
        self.rescan = rescan
        self.log = log
        self.now = now or datetime.now(timezone.utc)
        self.cutoff = cfg.cutoff(self.now)
        self.keywords = [Keyword(k) for k in cfg.keywords]
        if cfg.search_competitor_alternatives:
            self.keywords += competitor_alternative_keywords(cfg.competitors)
        self.stats = FetchStats()

    # public -----------------------------------------------------------------

    def run(self) -> FetchStats:
        self.db.sync_keywords(self.cfg.keywords)
        try:
            self._search_posts()
            if self.cfg.include_comments:
                self._read_threads()
                self._read_comment_feeds()
        except BudgetSpent as e:
            self.stats.stopped_early = str(e)
            self.log(f"Stopped early: {e}. The rest is picked up next run.")
        except RedditBlocked as e:
            self.stats.stopped_early = str(e)
            self.log(f"Stopped: {e}")
        self.db.commit()
        self.stats.requests = getattr(getattr(self.source, "http", None), "requests", 0)
        return self.stats

    # steps --------------------------------------------------------------------

    def _search_posts(self) -> None:
        queries = build_queries(self.keywords)
        subs = None if self.cfg.searches_all else self.cfg.subreddits
        t = self.cfg.reddit_time_param(self.now)
        max_pages = max(1, min(10, -(-self.cfg.max_results // 100)))
        where = "all of Reddit" if subs is None else ", ".join(f"r/{s}" for s in subs)
        self.log(f"Searching {where} for {len(self.keywords)} keywords in {len(queries)} searches (t={t})")
        for qi, query in enumerate(queries, 1):
            after, results, new_before = "", 0, self.stats.new
            for page in range(max_pages):
                if self._full():
                    break
                posts, entries, after = self.source.search(query.q, subs, t, after)
                results += len(posts)
                fresh = [p for p in posts if (p.created_at or "") >= self._cutoff_iso]
                for p in fresh:
                    p.matched_keywords = match_keywords(p.text, self.keywords)
                    p.keyword_matched = next(
                        (k for k in query.keywords if k in p.matched_keywords),
                        p.matched_keywords[0] if p.matched_keywords else query.keywords[0],
                    )
                for p in dedupe(fresh):
                    self._process(p)
                self.log(
                    f"  search {qi}/{len(queries)} page {page + 1}: {len(posts)} posts | "
                    f"new {self.stats.new} | for review {self.stats.for_review}"
                )
                if not after or len(fresh) < len(posts):
                    break  # last page, or older than the time range
            self.db.log_search(query.q, "ok", results, self.stats.new - new_before)

    def _read_threads(self) -> None:
        recent = (self.now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S")
        refetch_before = (self.now - timedelta(hours=20)).strftime("%Y-%m-%dT%H:%M:%SZ")
        threads = self.db.threads_to_fetch(
            self.cfg.thread_min_score, self.cfg.max_threads_per_run, max(recent, self._cutoff_iso), refetch_before
        )
        if threads:
            self.log(f"Reading comments in {len(threads)} matching threads")
        for i, row in enumerate(threads, 1):
            if self._full():
                break
            post, comments = self.source.thread(row["reddit_url"])
            excerpt = (post.content if post else row["content"] or "")[:PARENT_EXCERPT_CHARS]
            for c in comments:
                c.parent_post_title = row["title"]
                c.parent_post_url = row["reddit_url"]
                c.parent_post_id = row["reddit_id"]
                c.parent_excerpt = excerpt
                c.matched_keywords = match_keywords(c.text, self.keywords)
                c.keyword_matched = c.matched_keywords[0] if c.matched_keywords else row["keyword_matched"]
                self._process(c, in_relevant_thread=True)
            self.db.mark_thread_fetched(row["reddit_id"])
            self.db.commit()
            self.log(f"  thread {i}/{len(threads)}: {len(comments)} comments | for review {self.stats.for_review}")

    def _read_comment_feeds(self) -> None:
        subs = self.cfg.watch_subreddits
        n = self.cfg.subreddits_per_request
        chunks = [subs[i : i + n] for i in range(0, len(subs), n)]
        if chunks:
            self.log(f"Scanning the latest comments in {len(subs)} watched subreddits")
        for i, chunk in enumerate(chunks, 1):
            if self._full():
                break
            comments = self.source.latest_comments(chunk)
            kept = 0
            for c in comments:
                c.matched_keywords = match_keywords(c.text, self.keywords)
                if not c.matched_keywords and not rules.AI_NOTE.search(c.text):
                    continue  # unrelated chatter is not stored
                c.keyword_matched = c.matched_keywords[0] if c.matched_keywords else ""
                self._process(c)
                kept += 1
            self.db.commit()
            self.log(f"  comments {i}/{len(chunks)} ({', '.join(chunk)}): {len(comments)} read, {kept} on topic")

    # one item ------------------------------------------------------------------

    @property
    def _cutoff_iso(self) -> str:
        return self.cutoff.strftime("%Y-%m-%dT%H:%M:%S")

    def _full(self) -> bool:
        # Counts candidates, not every post read: broad keywords bring in a lot
        # of off-topic posts, and they shouldn't use up the run.
        return self.stats.for_review >= self.cfg.max_results

    def _process(self, it: Item, in_relevant_thread: bool = False) -> str:
        self.stats.found += 1
        canonical = canonical_url(it.reddit_url)
        existing = self.db.get(it.reddit_id) or self.db.find_by_url(canonical)
        if existing and not self.rescan:
            self.db.touch(existing["reddit_id"], it.matched_keywords)
            self.stats.already_seen += 1
            return "seen"
        if (it.created_at or "") < self._cutoff_iso:
            self.stats.too_old += 1
            return "old"
        h = content_hash(it.text)
        dup = self.db.find_by_hash(h, it.reddit_id)
        r = rules.score(
            it.text, it.matched_keywords, self.cfg.competitors,
            is_duplicate=bool(dup), in_relevant_thread=in_relevant_thread, username=it.username,
        )
        intent, intent_score = rule_intent(r)
        allowed = self.cfg.include_posts if it.type == "post" else self.cfg.include_comments
        if dup:
            status = "duplicate"
            self.db.touch(dup["reddit_id"], it.matched_keywords)
            self.stats.duplicates += 1
        elif r.score >= self.cfg.review_threshold and allowed:
            status = "review"
            self.stats.for_review += 1
        else:
            status = "skipped"
            self.stats.skipped += 1
        self.db.upsert(
            it, canonical=canonical, content_hash=h, rule_score=r.score, signals=r.signals,
            relevance=r.score, intent=intent, intent_score=intent_score, status=status,
            duplicate_of=dup["reddit_id"] if dup else "",
        )
        if not existing:
            self.stats.new += 1
        return status
