"""Dedupe by Reddit ID, then canonical URL, then a content hash."""

from __future__ import annotations

import hashlib
import re

from ..models import Item
from ..reddit.parse import canonical_url

MIN_HASH_CHARS = 60  # short replies like "thanks!" repeat naturally


def content_hash(text: str) -> str:
    t = re.sub(r"https?://\S+", " ", text.lower())
    t = re.sub(r"[^a-z0-9]+", " ", t).strip()
    if len(t) < MIN_HASH_CHARS:
        return ""
    return hashlib.sha1(t.encode("utf-8")).hexdigest()


def merge_keywords(a: list[str], b: list[str]) -> list[str]:
    out = list(a)
    for k in b:
        if k not in out:
            out.append(k)
    return out


def dedupe(items: list[Item]) -> list[Item]:
    """Collapses repeats within one fetch, keeping every matched keyword."""
    by_id: dict[str, Item] = {}
    by_url: dict[str, str] = {}
    for it in items:
        key = it.reddit_id
        url = canonical_url(it.reddit_url)
        if key not in by_id and url and url in by_url:
            key = by_url[url]
        if key in by_id:
            kept = by_id[key]
            kept.matched_keywords = merge_keywords(kept.matched_keywords, it.matched_keywords)
            kept.keyword_matched = kept.keyword_matched or it.keyword_matched
            if not kept.content and it.content:
                kept.content = it.content
            if not kept.parent_excerpt and it.parent_excerpt:
                kept.parent_excerpt = it.parent_excerpt
            continue
        by_id[key] = it
        if url:
            by_url[url] = key
    return list(by_id.values())
