"""Find what is jumping on Google Trends right now.

Two sources:
  1. Google Trends "Trending Now" RSS feed (free, no key). Every item is already a
     search that spiked in the last hours, with the news stories driving it.
  2. SerpApi's Google Trends API (optional, needs SERPAPI_KEY). Used to watch a fixed
     list of AI tools for spikes and to pull "rising" related queries, which is how
     brand-new AI tool names get discovered.
"""

from __future__ import annotations

import json
import logging
import os
import statistics
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from dataclasses import dataclass, field

log = logging.getLogger(__name__)

TRENDING_RSS = "https://trends.google.com/trending/rss?geo={geo}&hours={hours}"
SERPAPI_URL = "https://serpapi.com/search.json"
USER_AGENT = "Mozilla/5.0 (compatible; LynkkNewsBot/1.0; +https://lynkk.ai)"


@dataclass
class TrendCandidate:
    keyword: str
    source: str  # "trending_now" | "watchlist_spike" | "rising_query"
    geo: str = ""
    traffic: str = ""
    news: list[dict] = field(default_factory=list)  # [{title, url, source}]


def _get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _local(tag: str) -> str:
    """Strip the XML namespace so we don't depend on Google's exact ht: URI."""
    return tag.rsplit("}", 1)[-1]


def parse_trending_rss(xml_bytes: bytes, geo: str) -> list[TrendCandidate]:
    root = ET.fromstring(xml_bytes)
    out: list[TrendCandidate] = []
    for item in root.iter("item"):
        cand = TrendCandidate(keyword="", source="trending_now", geo=geo)
        for child in item:
            name = _local(child.tag)
            if name == "title":
                cand.keyword = (child.text or "").strip()
            elif name == "approx_traffic":
                cand.traffic = (child.text or "").strip()
            elif name == "news_item":
                story = {_local(c.tag).removeprefix("news_item_"): (c.text or "").strip() for c in child}
                cand.news.append({k: story.get(k, "") for k in ("title", "url", "source")})
        if cand.keyword:
            out.append(cand)
    return out


def fetch_trending_now(geos: list[str], hours: int) -> list[TrendCandidate]:
    out: list[TrendCandidate] = []
    for geo in geos:
        try:
            out.extend(parse_trending_rss(_get(TRENDING_RSS.format(geo=geo, hours=hours)), geo))
        except Exception as exc:  # one bad region should not stop the run
            log.warning("Trending Now feed failed for %s: %s", geo, exc)
    return out


def _serpapi(params: dict) -> dict:
    params = {**params, "engine": "google_trends", "api_key": os.environ["SERPAPI_KEY"]}
    return json.loads(_get(SERPAPI_URL + "?" + urllib.parse.urlencode(params), timeout=60))


def detect_spikes(timeline: list[dict], ratio: float, min_interest: int) -> list[tuple[str, float]]:
    """Return (query, ratio) for queries whose last 3 points jump above their earlier median."""
    series: dict[str, list[float]] = {}
    for point in timeline:
        for v in point.get("values", []):
            series.setdefault(v["query"], []).append(float(v.get("extracted_value") or 0))
    spikes = []
    for query, values in series.items():
        if len(values) < 10:
            continue
        recent = statistics.mean(values[-3:])
        baseline = max(statistics.median(values[:-3]), 1.0)
        if recent >= min_interest and recent / baseline >= ratio:
            spikes.append((query, round(recent / baseline, 1)))
    return spikes


def fetch_watchlist(cfg: dict) -> list[TrendCandidate]:
    if not os.environ.get("SERPAPI_KEY"):
        log.info("SERPAPI_KEY not set, skipping watchlist spikes and rising queries")
        return []
    wl = cfg["watchlist"]
    if datetime.now(timezone.utc).hour % wl["every_hours"]:
        return []
    out: list[TrendCandidate] = []
    keywords = wl["keywords"]
    # Google Trends compares at most 5 terms per request.
    for i in range(0, len(keywords), 5):
        group = keywords[i : i + 5]
        try:
            data = _serpapi({"q": ",".join(group), "data_type": "TIMESERIES", "date": "now 7-d"})
            timeline = data.get("interest_over_time", {}).get("timeline_data", [])
            for query, r in detect_spikes(timeline, wl["spike_ratio"], wl["min_interest"]):
                out.append(TrendCandidate(keyword=query, source="watchlist_spike", traffic=f"{r}x vs 7-day baseline"))
        except Exception as exc:
            log.warning("Watchlist query failed for %s: %s", group, exc)
    for seed in wl["rising_seeds"]:
        try:
            data = _serpapi({"q": seed, "data_type": "RELATED_QUERIES", "date": "now 1-d"})
            for row in data.get("related_queries", {}).get("rising", [])[:10]:
                out.append(TrendCandidate(keyword=row["query"], source="rising_query", traffic=f"{row.get('value', '')} (seed: {seed})"))
        except Exception as exc:
            log.warning("Rising queries failed for %s: %s", seed, exc)
    return out


def collect(cfg: dict) -> list[TrendCandidate]:
    cands = fetch_trending_now(cfg["trends"]["geos"], cfg["trends"]["hours"]) + fetch_watchlist(cfg)
    # Merge duplicates across regions and sources.
    merged: dict[str, TrendCandidate] = {}
    for c in cands:
        key = c.keyword.lower().strip()
        if key in merged:
            m = merged[key]
            m.geo = ",".join(sorted(set(filter(None, (m.geo + "," + c.geo).split(",")))))
            m.news.extend(n for n in c.news if n not in m.news)
        else:
            merged[key] = c
    return list(merged.values())
