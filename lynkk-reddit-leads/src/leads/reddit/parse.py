"""Turns Reddit Atom feeds into Items."""

from __future__ import annotations

import html
import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

from ..models import Item

NS = {"a": "http://www.w3.org/2005/Atom"}

_THREAD_URL = re.compile(
    r"https?://(?:www\.|old\.|new\.)?reddit\.com/r/([^/]+)/comments/([a-z0-9]+)(?:/[^/?#]*)?(?:/([a-z0-9]+))?",
    re.I,
)


class _Text(HTMLParser):
    BLOCK = {"p", "br", "li", "div", "blockquote", "pre", "h1", "h2", "h3", "h4", "h5", "h6", "tr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.BLOCK:
            self.parts.append("\n")
        if tag == "li":
            self.parts.append("- ")

    def handle_endtag(self, tag):
        if tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        self.parts.append(data)


def html_to_text(fragment: str) -> str:
    """Reddit's HTML body to plain text, without the 'submitted by' footer."""
    if "<!-- SC_ON -->" in fragment:
        fragment = fragment.split("<!-- SC_ON -->", 1)[0]
    elif "submitted by" in fragment:
        fragment = fragment.split("submitted by", 1)[0]
    p = _Text()
    p.feed(fragment)
    text = html.unescape("".join(p.parts)).replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def canonical_url(url: str) -> str:
    """One URL per post or comment, whatever slug or host Reddit used."""
    m = _THREAD_URL.match(url or "")
    if not m:
        return (url or "").split("?")[0].split("#")[0].rstrip("/").lower()
    sub, post, comment = m.group(1).lower(), m.group(2).lower(), (m.group(3) or "").lower()
    base = f"https://www.reddit.com/r/{sub}/comments/{post}"
    return f"{base}/comment/{comment}" if comment else base


def post_id_from_url(url: str) -> str:
    m = _THREAD_URL.match(url or "")
    return f"t3_{m.group(2).lower()}" if m else ""


def post_url_from_url(url: str) -> str:
    m = _THREAD_URL.match(url or "")
    if not m:
        return ""
    return f"https://www.reddit.com/r/{m.group(1)}/comments/{m.group(2)}/"


def parse_feed(xml_text: str, source: str) -> tuple[list[Item], str]:
    """Returns the posts and comments in a feed, and the feed's title."""
    if not xml_text.strip():
        return [], ""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return [], ""
    feed_title = root.findtext("a:title", "", NS) or ""
    items: list[Item] = []
    for entry in root.findall("a:entry", NS):
        item = _entry(entry, source)
        if item:
            items.append(item)
    return items, feed_title


def _entry(e: ET.Element, source: str) -> Item | None:
    fullname = (e.findtext("a:id", "", NS) or "").strip()
    if not (fullname.startswith("t3_") or fullname.startswith("t1_")):
        return None  # subreddit or user results
    link_el = e.find("a:link", NS)
    url = link_el.get("href", "") if link_el is not None else ""
    name = (e.findtext("a:author/a:name", "", NS) or "").strip()
    username = name.removeprefix("/u/").removeprefix("u/")
    author_url = (e.findtext("a:author/a:uri", "", NS) or "").strip()
    cat = e.find("a:category", NS)
    sub = (cat.get("label") or f"r/{cat.get('term')}") if cat is not None else ""
    if not sub:
        m = _THREAD_URL.match(url)
        sub = f"r/{m.group(1)}" if m else ""
    created = e.findtext("a:published", "", NS) or e.findtext("a:updated", "", NS) or ""
    content = html_to_text(e.findtext("a:content", "", NS) or "")
    title = html.unescape(e.findtext("a:title", "", NS) or "").strip()
    is_post = fullname.startswith("t3_")
    if not is_post:
        # Comment titles look like "/u/name on <post title>"
        title = re.sub(r"^/u/\S+ on ", "", title)
    return Item(
        reddit_id=fullname,
        type="post" if is_post else "comment",
        username=username or "[deleted]",
        content=content,
        title=title,
        subreddit=sub,
        reddit_url=url,
        author_url=author_url or (f"https://www.reddit.com/user/{username}" if username else ""),
        created_at=created,
        parent_post_id="" if is_post else post_id_from_url(url),
        parent_post_title="" if is_post else title,
        parent_post_url="" if is_post else post_url_from_url(url),
        source=source,
    )
