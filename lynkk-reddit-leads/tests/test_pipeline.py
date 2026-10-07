"""Fetch to review to export, with recorded Reddit feeds instead of the network."""

import json

import pandas as pd
from conftest import fixture

from leads.cli import main
from leads.fetch import Fetcher
from leads.reddit.parse import parse_feed
from leads.review import apply_results, results_path, write_batch


class FakeSource:
    def __init__(self):
        self.searches = 0
        self.threads = 0
        self.feeds = 0

    def search(self, q, subreddits, t, after=""):
        self.searches += 1
        items, _ = parse_feed(fixture("search.xml"), "search")
        return [i for i in items if i.type == "post"], len(items), ""

    def thread(self, url):
        self.threads += 1
        if "1wz5toq" not in url:
            return None, []
        items, _ = parse_feed(fixture("thread.xml"), "thread")
        return items[0], [i for i in items if i.type == "comment"]

    def latest_comments(self, subs):
        self.feeds += 1
        items, _ = parse_feed(fixture("comment_feed.xml"), "comment_feed")
        return items


def test_fetch_dedupes_across_searches_and_skips_seen(cfg, db):
    src = FakeSource()
    stats = Fetcher(cfg, db, src, log=lambda *_: None).run()
    assert src.searches >= 2  # several OR queries return the same posts
    total = len(db.all_items())
    posts = [i for i in db.all_items() if i["type"] == "post"]
    assert len(posts) == len({p["reddit_id"] for p in posts}) == 10
    assert stats.new == total
    assert db.count_pending() > 0

    # Second run: everything is already known, nothing is reprocessed.
    stats2 = Fetcher(cfg, db, FakeSource(), log=lambda *_: None).run()
    assert stats2.new == 0
    assert stats2.already_seen > 0
    assert len(db.all_items()) == total


def test_keywords_from_every_query_are_merged(cfg, db):
    Fetcher(cfg, db, FakeSource(), log=lambda *_: None).run()
    zoom = db.get("t3_1wz5toq")
    kws = json.loads(zoom["matched_keywords"])
    assert "AI note taker" in kws and "Zoom notes" in kws
    assert zoom["keyword_matched"]


def test_comments_get_parent_context(cfg, db):
    Fetcher(cfg, db, FakeSource(), log=lambda *_: None).run()
    comments = [i for i in db.all_items() if i["type"] == "comment" and i["source"] == "thread"]
    assert comments
    c = comments[0]
    assert c["parent_post_url"].startswith("https://www.reddit.com/r/Zoom/comments/1wz5toq")
    assert c["parent_post_title"].startswith("Best AI note taker for Zoom")
    assert "Two clients asked" in c["parent_excerpt"]


def test_off_topic_feed_comments_are_not_stored(cfg, db):
    Fetcher(cfg, db, FakeSource(), log=lambda *_: None).run()
    feed = [i for i in db.all_items() if i["source"] == "comment_feed"]
    assert len(feed) < 10  # the fixture is 100 general productivity/sales comments


def test_rescan_reprocesses(cfg, db):
    Fetcher(cfg, db, FakeSource(), log=lambda *_: None).run()
    stats = Fetcher(cfg, db, FakeSource(), rescan=True, log=lambda *_: None).run()
    assert stats.already_seen == 0
    assert stats.for_review > 0


def test_review_round_trip_and_export(cfg, db, capsys):
    Fetcher(cfg, db, FakeSource(), log=lambda *_: None).run()
    path, n, waiting = write_batch(cfg, db, 100)
    batch = json.loads(path.read_text(encoding="utf-8"))["items"]
    assert n == len(batch) == waiting

    # Pretend to be Claude Code: one verdict per item, one bad line.
    lines = []
    for it in batch:
        good = it["id"] == "t3_1wz5toq"
        lines.append(json.dumps({
            "id": it["id"], "relevance_score": 92 if good else 20,
            "intent": "high_purchase_intent" if good else "low_relevance", "intent_score": 90 if good else 10,
            "pain_point": "Needs one note taker for two clients' Zoom calls." if good else "",
            "context": "Consultant with two clients." if good else "", "potential_use_case": "Call notes" if good else "",
            "reply_opportunity": "Asks for an AI note taker." if good else "Skip.", "is_promotional": False,
        }))
    lines.append('{"id": "t3_1wz5toq", "intent": "maybe"}')
    results_path(cfg).write_text("\n".join(lines), encoding="utf-8")
    saved, errors = apply_results(cfg, db)
    assert saved == len(batch)
    assert len(errors) == 1 and "intent must be one of" in errors[0]
    assert db.count_pending() == 0

    db.close()
    assert main(["--config", str(cfg.root / "config.toml"), "export"]) == 0
    out = capsys.readouterr().out
    assert "Today's CSV" in out
    daily = next(cfg.output_dir.glob("reddit_ai_note_opportunities_*.csv"))
    df = pd.read_csv(daily, encoding="utf-8-sig")
    assert df.iloc[0]["id"] == "t3_1wz5toq"
    assert df.iloc[0]["pain_point"].startswith("Needs one note taker")
    assert (df["relevance_score"] >= cfg.min_relevance).all()
    html = (cfg.output_dir / "report.html").read_text(encoding="utf-8")
    assert "t3_1wz5toq" in html and "/*__DATA__*/" not in html

    # Exporting again: nothing new, but today's file keeps today's rows.
    assert main(["--config", str(cfg.root / "config.toml"), "export"]) == 0
    assert "0 new" in capsys.readouterr().out


def test_draft_context(cfg, db, capsys):
    Fetcher(cfg, db, FakeSource(), log=lambda *_: None).run()
    db.close()
    assert main(["--config", str(cfg.root / "config.toml"), "draft", "1wz5toq"]) == 0
    text = (cfg.drafts_dir / "t3_1wz5toq.md").read_text(encoding="utf-8")
    assert "Best AI note taker for Zoom" in text and "## Draft reply" in text
