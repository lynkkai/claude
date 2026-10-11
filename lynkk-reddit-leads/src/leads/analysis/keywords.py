"""Keyword matching and Reddit search query building."""

from __future__ import annotations

import re
from dataclasses import dataclass

# Reddit rejects very long queries; stay well under its 512 character limit.
MAX_QUERY_CHARS = 400


def normalize(text: str) -> str:
    """Lowercase, hyphens and underscores as spaces, 'notetaker' as 'note taker'."""
    t = text.lower().replace("’", "'")
    t = re.sub(r"[-_/]+", " ", t)
    t = re.sub(r"\bnote(tak|mak)", r"note \1", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def _contains(norm_text: str, norm_phrase: str) -> bool:
    if not norm_phrase:
        return False
    # A trailing s or es counts, so "note taker" also finds "note takers".
    return re.search(rf"(?<![a-z0-9]){re.escape(norm_phrase)}(?:e?s)?(?![a-z0-9])", norm_text) is not None


@dataclass(frozen=True)
class Keyword:
    """A configured keyword: an exact phrase, or a combination like '"meeting notes" AI'."""

    raw: str

    @property
    def is_combination(self) -> bool:
        return '"' in self.raw

    @property
    def terms(self) -> list[str]:
        if not self.is_combination:
            return [normalize(self.raw)]
        quoted = re.findall(r'"([^"]+)"', self.raw)
        rest = re.sub(r'"[^"]+"', " ", self.raw).split()
        return [normalize(t) for t in quoted + rest if normalize(t)]

    def matches(self, norm_text: str) -> bool:
        return all(_contains(norm_text, t) for t in self.terms)

    @property
    def query(self) -> str:
        return self.raw if self.is_combination else f'"{self.raw}"'


def match_keywords(text: str, keywords: list[Keyword]) -> list[str]:
    """Configured keywords found in the text. Spelling variants ("AI notetaker",
    "AI note taker") count once, under the first one listed."""
    norm = normalize(text)
    found, seen = [], set()
    for k in keywords:
        key = tuple(k.terms)
        if key not in seen and k.matches(norm):
            found.append(k.raw)
            seen.add(key)
    return found


def competitor_alternative_keywords(competitors: list[str]) -> list[Keyword]:
    """Plain phrases, so they pack into a few OR queries."""
    out: list[Keyword] = []
    for c in competitors:
        out += [Keyword(f"{c} alternative"), Keyword(f"{c} alternatives"), Keyword(f"alternative to {c}")]
    return out


@dataclass
class SearchQuery:
    q: str
    keywords: list[str]  # the configured keywords this query covers


def build_queries(keywords: list[Keyword]) -> list[SearchQuery]:
    """Packs phrases into OR queries; combinations get one query each."""
    queries: list[SearchQuery] = []
    group: list[Keyword] = []

    def flush():
        if group:
            queries.append(SearchQuery(" OR ".join(k.query for k in group), [k.raw for k in group]))
            group.clear()

    for k in keywords:
        if k.is_combination:
            queries.append(SearchQuery(k.query, [k.raw]))
            continue
        candidate = " OR ".join(x.query for x in group + [k])
        if group and len(candidate) > MAX_QUERY_CHARS:
            flush()
        group.append(k)
    flush()
    return queries
