"""Reddit's public RSS feeds as a data source.

Three feeds are used, all read only:
  search    https://www.reddit.com/search.rss?q=...&sort=new&t=week
  thread    https://www.reddit.com/r/<sub>/comments/<id>/.rss   (post + comments)
  comments  https://www.reddit.com/r/<a>+<b>/comments.rss        (latest comments)

Reddit's search does not cover comments, so comments come from threads of
matching posts and from the watched subreddits' latest comments.
"""

from __future__ import annotations

from urllib.parse import quote, urlencode

from ..models import Item
from .http import Http
from .parse import parse_feed, post_url_from_url

BASE = "https://www.reddit.com"
PAGE = 100


class RssSource:
    def __init__(self, http: Http):
        self.http = http

    def search(self, q: str, subreddits: list[str] | None, t: str, after: str = "") -> tuple[list[Item], int, str]:
        """One page of newest posts. Returns items, entries on the page, and the next cursor."""
        params = {"q": q, "sort": "new", "t": t, "limit": PAGE}  # NSFW stays excluded (Reddit default)
        if after:
            params["after"] = after
        if subreddits:
            path = f"/r/{'+'.join(quote(s) for s in subreddits)}/search.rss"
            params["restrict_sr"] = "on"
        else:
            path = "/search.rss"
        body = self.http.get(f"{BASE}{path}?{urlencode(params)}")
        items, _ = parse_feed(body, "search")
        posts = [i for i in items if i.type == "post"]
        next_after = posts[-1].reddit_id if len(items) >= PAGE - 10 and posts else ""
        return posts, len(items), next_after

    def thread(self, post_url: str) -> tuple[Item | None, list[Item]]:
        """The post and its comments (Reddit's feed lists them flat)."""
        url = post_url_from_url(post_url) or post_url
        body = self.http.get(f"{url.rstrip('/')}/.rss?{urlencode({'limit': PAGE})}")
        items, _ = parse_feed(body, "thread")
        post = next((i for i in items if i.type == "post"), None)
        comments = [i for i in items if i.type == "comment"]
        return post, comments

    def latest_comments(self, subreddits: list[str]) -> list[Item]:
        path = f"/r/{'+'.join(quote(s) for s in subreddits)}/comments.rss"
        body = self.http.get(f"{BASE}{path}?{urlencode({'limit': PAGE})}")
        items, _ = parse_feed(body, "comment_feed")
        return [i for i in items if i.type == "comment"]
