from conftest import fixture

from leads.reddit.parse import canonical_url, html_to_text, parse_feed


def test_search_feed_keeps_posts_and_drops_subreddit_results():
    items, _ = parse_feed(fixture("search.xml"), "search")
    assert items, "fixture should have posts"
    assert all(i.type == "post" and i.reddit_id.startswith("t3_") for i in items)
    zoom = next(i for i in items if "Zoom across two client" in i.title)
    assert zoom.username == "CommissionBorn4257"
    assert zoom.subreddit == "r/Zoom"
    assert zoom.author_url == "https://www.reddit.com/user/CommissionBorn4257"
    assert zoom.reddit_url.startswith("https://www.reddit.com/r/Zoom/comments/1wz5toq/")
    assert zoom.created_at.startswith("2026-10-06T15:39")
    assert "submitted by" not in zoom.content
    assert "[comments]" not in zoom.content
    assert "Two clients asked for Zoom notes" in zoom.content


def test_thread_feed_has_post_then_comments_with_parent():
    items, title = parse_feed(fixture("thread.xml"), "thread")
    assert items[0].type == "post"
    comments = [i for i in items if i.type == "comment"]
    assert comments
    c = comments[0]
    assert c.reddit_id.startswith("t1_")
    assert c.parent_post_id == "t3_1wz5toq"
    assert c.parent_post_url == "https://www.reddit.com/r/Zoom/comments/1wz5toq/"
    assert c.title.startswith("Best AI note taker for Zoom")  # "/u/x on" removed
    assert "Zoom" in title


def test_comment_feed_parses_comments_across_subreddits():
    items, _ = parse_feed(fixture("comment_feed.xml"), "comment_feed")
    assert len(items) > 50
    assert {i.type for i in items} == {"comment"}
    assert len({i.subreddit for i in items}) > 1
    assert all(i.parent_post_id.startswith("t3_") for i in items)


def test_html_to_text_keeps_paragraphs_and_entities():
    html = '<!-- SC_OFF --><div class="md"><p>Hi &amp; hello</p><ul><li>one</li><li>two</li></ul></div><!-- SC_ON --> submitted by'
    assert html_to_text(html) == "Hi & hello\n\n- one\n\n- two"


def test_canonical_url_ignores_slug_host_and_query():
    a = canonical_url("https://old.reddit.com/r/Zoom/comments/1wz5toq/best_ai_note_taker/?utm=x")
    b = canonical_url("https://www.reddit.com/r/zoom/comments/1wz5toq/")
    assert a == b == "https://www.reddit.com/r/zoom/comments/1wz5toq"
    c = canonical_url("https://www.reddit.com/r/Zoom/comments/1wz5toq/best_ai/pe8torw/")
    assert c == "https://www.reddit.com/r/zoom/comments/1wz5toq/comment/pe8torw"


def test_broken_feed_returns_nothing():
    assert parse_feed("<html>blocked</html", "search") == ([], "")
    assert parse_feed("", "search") == ([], "")
