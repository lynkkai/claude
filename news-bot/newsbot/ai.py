"""Claude steps: pick relevant trends, research them on the web, write the article."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import asdict
from datetime import date

import anthropic

from .trends import TrendCandidate

log = logging.getLogger(__name__)

client = anthropic.Anthropic()

# Server-side refusal fallback: if a request is declined, the API retries it on
# Anthropic's recommended fallback model inside the same call.
FALLBACK = {"betas": ["server-side-fallback-2026-07-01"], "fallbacks": "default"}

BRAND = (
    "Lynkk (https://lynkk.ai, always spelled with a double k) is an AI meeting assistant. "
    "It surfaces context before meetings, joins and speaks when needed during them, and within "
    "about 30 seconds after produces structured notes, action items, CRM updates and Jira tickets, "
    "all searchable in a knowledge graph. It records online and in-person conversations, is "
    "multilingual and offline-first, and offers regional data residency."
)

STYLE_RULES = (
    "Never use em dashes or en dashes. Use commas, colons, parentheses or separate sentences, "
    "and a plain hyphen for ranges. Always spell the brand as Lynkk."
)


class Refused(Exception):
    pass


def _create(cfg: dict, effort: str, **kwargs):
    resp = client.beta.messages.create(
        model=cfg["bot"]["model"],
        output_config={"effort": effort, **kwargs.pop("output_config", {})},
        **FALLBACK,
        **kwargs,
    )
    if resp.stop_reason == "refusal":
        raise Refused(str(resp.stop_details))
    return resp


def _json(resp) -> dict:
    return json.loads(next(b.text for b in resp.content if b.type == "text"))


def _strict(schema: dict) -> dict:
    return {"format": {"type": "json_schema", "schema": schema}}


# --------------------------------------------------------------------------- select

SELECT_SCHEMA = {
    "type": "object",
    "properties": {
        "picks": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "keyword": {"type": "string"},
                    "angle": {"type": "string", "description": "The specific news story behind the spike, one sentence."},
                    "score": {"type": "integer", "description": "1-10 newsworthiness for Lynkk readers."},
                },
                "required": ["keyword", "angle", "score"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["picks"],
    "additionalProperties": False,
}


def select(cfg: dict, cands: list[TrendCandidate], recent_titles: list[str]) -> list[dict]:
    if not cands:
        return []
    listing = "\n".join(
        json.dumps({k: v for k, v in asdict(c).items() if v}, ensure_ascii=False) for c in cands
    )
    prompt = f"""You are the news editor for the Lynkk blog. Below are search terms that are spiking on Google Trends right now.

Pick only the ones that are genuinely about this beat:
{cfg["topics"]["include"]}
Reject:
{cfg["topics"]["exclude"]}
Also reject anything already covered by these recent Lynkk posts:
{chr(10).join("- " + t for t in recent_titles) or "- (none)"}

Merge terms that refer to the same story into one pick. Return an empty list if nothing fits; it is fine to pick nothing.

Trending terms (JSON lines):
{listing}"""
    resp = _create(
        cfg,
        cfg["bot"]["select_effort"],
        max_tokens=4000,
        output_config=_strict(SELECT_SCHEMA),
        messages=[{"role": "user", "content": prompt}],
    )
    picks = sorted(_json(resp)["picks"], key=lambda p: -p["score"])
    return [p for p in picks if p["score"] >= 6]


# --------------------------------------------------------------------------- research


def research(cfg: dict, pick: dict) -> tuple[str, list[dict]]:
    """Use web search to build a dated fact sheet. Returns (notes, sources)."""
    today = date.today().isoformat()
    messages = [
        {
            "role": "user",
            "content": f"""Today is {today}. "{pick["keyword"]}" is spiking on Google Trends. Likely story: {pick["angle"]}

Search the web and find out what actually happened. Prefer primary sources (company blogs, official announcements) and established tech press. Focus on the last 72 hours.

Write a plain fact sheet: what happened, when, who is involved, key numbers, official quotes (verbatim, attributed), and what is still unconfirmed. Mark anything you could not verify. If there is no real, verifiable news story, say NO_STORY on the first line.""",
        }
    ]
    tools = [{"type": "web_search_20260209", "name": "web_search", "max_uses": cfg["bot"]["max_web_searches"]}]
    blocks = []
    for _ in range(5):  # resume server-side loop on pause_turn, bounded
        resp = _create(cfg, cfg["bot"]["research_effort"], max_tokens=16000, tools=tools, messages=messages)
        blocks.extend(resp.content)
        if resp.stop_reason != "pause_turn":
            break
        messages = messages[:1] + [{"role": "assistant", "content": blocks}]

    notes = "\n".join(b.text for b in blocks if b.type == "text").strip()
    sources: dict[str, str] = {}
    for b in blocks:
        if b.type == "text":
            for c in b.citations or []:
                if getattr(c, "url", None):
                    sources.setdefault(c.url, getattr(c, "title", "") or c.url)
    if not sources:  # fall back to raw search results
        for b in blocks:
            if b.type == "web_search_tool_result" and isinstance(b.content, list):
                for r in b.content[:6]:
                    sources.setdefault(r.url, r.title)
    return notes, [{"title": t, "url": u} for u, t in sources.items()]


# --------------------------------------------------------------------------- write

ARTICLE_SCHEMA = {
    "type": "object",
    "properties": {
        "publishable": {"type": "boolean", "description": "False if the facts are too thin or unverified to publish."},
        "skip_reason": {"type": "string"},
        "title": {"type": "string", "description": "Headline, under 70 characters, no clickbait."},
        "slug": {"type": "string", "description": "lowercase-hyphenated URL slug"},
        "meta_description": {"type": "string", "description": "SEO description, under 155 characters."},
        "excerpt": {"type": "string", "description": "Two-sentence summary for the news list page."},
        "tags": {"type": "array", "items": {"type": "string"}},
        "body_markdown": {"type": "string", "description": "Article body in Markdown, ## subheadings, no H1, no sources list."},
        "source_urls": {"type": "array", "items": {"type": "string"}, "description": "URLs from the source list actually used."},
    },
    "required": ["publishable", "skip_reason", "title", "slug", "meta_description", "excerpt", "tags", "body_markdown", "source_urls"],
    "additionalProperties": False,
}

WRITER_SYSTEM = f"""You write short, accurate AI industry news for the Lynkk blog.

About Lynkk: {BRAND}

Rules:
- Use only facts from the research notes. Never invent numbers, dates, quotes, features or prices. Attribute claims ("according to The Verge", "OpenAI said").
- Be fair and factual about every company, including Lynkk competitors. No disparaging or speculative claims about them.
- 350-650 words. Lead with the news in the first sentence, then context, then why it matters.
- End with a short section "What it means for teams that live in meetings". Mention Lynkk at most once, only if it is genuinely relevant, and never as a hard sell.
- {STYLE_RULES}
- If the notes start with NO_STORY or the facts are thin, set publishable to false and explain in skip_reason."""


def write(cfg: dict, pick: dict, notes: str, sources: list[dict]) -> dict:
    src = "\n".join(f"- {s['title']}: {s['url']}" for s in sources) or "- (none)"
    resp = _create(
        cfg,
        cfg["bot"]["write_effort"],
        max_tokens=16000,
        system=WRITER_SYSTEM,
        output_config=_strict(ARTICLE_SCHEMA),
        messages=[
            {
                "role": "user",
                "content": f"Trending keyword: {pick['keyword']}\nStory angle: {pick['angle']}\nToday: {date.today().isoformat()}\n\n"
                f"<research_notes>\n{notes}\n</research_notes>\n\n<sources>\n{src}\n</sources>\n\nWrite the article.",
            }
        ],
    )
    article = _json(resp)
    known = {s["url"]: s["title"] for s in sources}
    article["sources"] = [{"url": u, "title": known.get(u, u)} for u in article.pop("source_urls") if u in known]
    article["slug"] = re.sub(r"[^a-z0-9]+", "-", article["slug"].lower()).strip("-")
    for key in ("title", "meta_description", "excerpt", "body_markdown"):
        article[key] = clean_text(article[key])
    article["tags"] = [clean_text(t) for t in article["tags"]]
    return article


def clean_text(text: str) -> str:
    """Enforce the house style even if the model slips: no em or en dashes."""
    text = re.sub(r"(\d)\s*[\u2013\u2014]\s*(\d)", r"\1-\2", text)  # ranges like 2024-2025
    text = re.sub(r"(?m)^(\s*)[\u2014\u2013]\s*", r"\1- ", text)  # dash used as a list bullet
    return re.sub(r"\s*[\u2014\u2013]\s*", ", ", text)
