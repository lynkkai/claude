import csv

import pandas as pd

from leads.export.csv_export import COLUMNS, write_csv

REQUIRED = [
    "id", "type", "username", "content", "title", "subreddit", "reddit_url", "author_url", "created_at",
    "keyword_matched", "matched_keywords", "relevance_score", "intent", "intent_score", "pain_point",
    "context", "potential_use_case", "reply_opportunity",
]

NASTY = 'Line one, with "quotes", commas\nline two 😅 naïve café — dash\r\nline three'


def item(**kw):
    base = dict(
        reddit_id="t3_abc", type="post", username="john123", content=NASTY, title="AI tool, for \"client\" calls?",
        subreddit="r/sales", reddit_url="https://www.reddit.com/r/sales/comments/abc/x/", author_url="https://www.reddit.com/user/john123",
        created_at="2026-10-06T15:39:36+00:00", keyword_matched="AI meeting notes",
        matched_keywords=["AI meeting notes", "meeting transcription"], relevance_score=95, intent="high_purchase_intent",
        intent_score=94, pain_point="Manual note taking is hard", context="", potential_use_case="Notes", reply_opportunity="Asks",
        parent_post_url="", reviewed_by="claude", first_seen_at="2026-10-06T16:00:00Z", parent_post_title="",
    )
    base.update(kw)
    return base


def test_required_columns_come_first_in_order():
    assert COLUMNS[: len(REQUIRED)] == REQUIRED


def test_round_trip_with_pandas(tmp_path):
    p = write_csv(tmp_path / "out.csv", [item(), item(reddit_id="t1_def", type="comment", content="- starts with a dash")])
    df = pd.read_csv(p, encoding="utf-8-sig")
    assert list(df.columns) == COLUMNS
    assert df.loc[0, "content"] == NASTY
    assert df.loc[0, "matched_keywords"] == "AI meeting notes; meeting transcription"
    assert df.loc[0, "relevance_score"] == 95
    assert df.loc[1, "content"] == "'- starts with a dash"  # not run as a formula in spreadsheets


def test_file_is_utf8_with_bom_and_fully_quoted(tmp_path):
    p = write_csv(tmp_path / "out.csv", [item()])
    raw = p.read_bytes()
    assert raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    rows = list(csv.reader(text.splitlines(keepends=True)))
    assert rows[0][0] == "id"
    assert text.splitlines()[0].startswith('"id","type"')


def test_huge_content_is_cut_for_excel(tmp_path):
    p = write_csv(tmp_path / "out.csv", [item(content="x" * 40_000)])
    df = pd.read_csv(p, encoding="utf-8-sig")
    assert len(df.loc[0, "content"]) < 32_767
    assert df.loc[0, "content"].endswith("open reddit_url for the rest]")
