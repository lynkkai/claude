"""Loads config.toml into typed settings."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

TIME_RANGES = {"24h": 1, "7d": 7, "30d": 30, "90d": 90}


@dataclass
class Config:
    keywords: list[str]
    competitors: list[str] = field(default_factory=list)
    search_competitor_alternatives: bool = True
    subreddits: list[str] = field(default_factory=lambda: ["all"])
    time_range: str = "7d"
    since: str = ""
    include_posts: bool = True
    include_comments: bool = True
    max_results: int = 250
    max_threads_per_run: int = 15
    thread_min_score: int = 40
    watch_subreddits: list[str] = field(default_factory=list)
    subreddits_per_request: int = 5
    review_threshold: int = 25
    min_relevance: int = 50
    batch_size: int = 25
    min_seconds_between_requests: float = 2
    max_requests_per_run: int = 45
    user_agent: str = "macos:lynkk-reddit-leads:1.0 (lead research, read only)"
    export_filename: str = "reddit_ai_note_opportunities_{date}.csv"
    export_folder: str = "output"
    root: Path = ROOT

    @property
    def data_dir(self) -> Path:
        return self.root / "data"

    @property
    def db_path(self) -> Path:
        return self.data_dir / "leads.db"

    @property
    def output_dir(self) -> Path:
        return self.root / self.export_folder

    @property
    def work_dir(self) -> Path:
        return self.root / "work"

    @property
    def drafts_dir(self) -> Path:
        return self.root / "drafts"

    @property
    def log_dir(self) -> Path:
        return self.root / "logs"

    def cutoff(self, now: datetime | None = None) -> datetime:
        """Oldest creation time a result may have."""
        now = now or datetime.now(timezone.utc)
        if self.time_range == "custom":
            if not self.since:
                raise ValueError('time_range is "custom" but since is empty in config.toml')
            return datetime.fromisoformat(self.since).replace(tzinfo=timezone.utc)
        if self.time_range not in TIME_RANGES:
            raise ValueError(f"time_range must be one of 24h, 7d, 30d, 90d, custom (got {self.time_range!r})")
        return now - timedelta(days=TIME_RANGES[self.time_range])

    def reddit_time_param(self, now: datetime | None = None) -> str:
        """Reddit's t= filter: the smallest window that covers the cutoff."""
        days = ((now or datetime.now(timezone.utc)) - self.cutoff(now)).total_seconds() / 86400
        for limit, name in ((1, "day"), (7, "week"), (31, "month"), (366, "year")):
            if days <= limit:
                return name
        return "all"

    @property
    def searches_all(self) -> bool:
        return not self.subreddits or [s.lower() for s in self.subreddits] == ["all"]


def load(path: Path | None = None) -> Config:
    path = path or ROOT / "config.toml"
    with open(path, "rb") as f:
        raw = tomllib.load(f)
    s = raw.get("search", {})
    c = raw.get("comments", {})
    sc = raw.get("scoring", {})
    r = raw.get("review", {})
    n = raw.get("network", {})
    e = raw.get("export", {})
    keywords = [k.strip() for k in s.get("keywords", []) if k and k.strip()]
    if not keywords:
        raise ValueError("config.toml has no keywords under [search]")
    cfg = Config(
        keywords=keywords,
        competitors=[x.strip() for x in s.get("competitors", []) if x.strip()],
        search_competitor_alternatives=s.get("search_competitor_alternatives", True),
        subreddits=[x.strip().removeprefix("r/") for x in s.get("subreddits", ["all"]) if x.strip()],
        time_range=s.get("time_range", "7d"),
        since=s.get("since", ""),
        include_posts=s.get("include_posts", True),
        include_comments=s.get("include_comments", True),
        max_results=int(s.get("max_results", 250)),
        max_threads_per_run=int(c.get("max_threads_per_run", 15)),
        thread_min_score=int(c.get("thread_min_score", 40)),
        watch_subreddits=[x.strip().removeprefix("r/") for x in c.get("watch_subreddits", []) if x.strip()],
        subreddits_per_request=max(1, int(c.get("subreddits_per_request", 5))),
        review_threshold=int(sc.get("review_threshold", 25)),
        min_relevance=int(sc.get("min_relevance", 50)),
        batch_size=max(1, int(r.get("batch_size", 25))),
        min_seconds_between_requests=float(n.get("min_seconds_between_requests", 2)),
        max_requests_per_run=int(n.get("max_requests_per_run", 45)),
        user_agent=n.get("user_agent") or Config.user_agent,
        export_filename=e.get("filename", Config.export_filename),
        export_folder=e.get("folder", Config.export_folder),
        root=path.resolve().parent,
    )
    cfg.cutoff()  # validates time_range early
    return cfg
