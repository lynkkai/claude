#!/usr/bin/env python3
"""Pull competitor ads from the official Meta Ad Library API and summarize them.

Needs a Meta access token in META_AD_LIBRARY_TOKEN (see ads/scripts/README.md).

The API only returns non-political ads that were delivered in the EU, so the default
countries are EU markets. For those ads Meta also returns targeting (age, gender,
locations) and EU reach broken down by age, gender and country.

Usage:
    python3 ads/scripts/meta_ad_library.py                      # run ads/scripts/queries.json
    python3 ads/scripts/meta_ad_library.py --terms "AI note taker" --countries DE,FR
"""

import argparse
import collections
import datetime as dt
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_QUERIES = HERE / "queries.json"
DEFAULT_OUT = HERE.parent / "research"

EU_COUNTRIES = ["DE", "FR", "NL", "ES", "IT", "IE", "SE", "PL", "BE", "AT", "DK", "FI", "PT"]

FIELDS = [
    "id",
    "page_id",
    "page_name",
    "ad_creation_time",
    "ad_delivery_start_time",
    "ad_delivery_stop_time",
    "ad_creative_bodies",
    "ad_creative_link_titles",
    "ad_creative_link_descriptions",
    "ad_creative_link_captions",
    "publisher_platforms",
    "languages",
    "target_ages",
    "target_gender",
    "target_locations",
    "eu_total_reach",
    "age_country_gender_reach_breakdown",
    "beneficiary_payers",
]


def ssl_context():
    bundle = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")
    return ssl.create_default_context(cafile=bundle) if bundle else ssl.create_default_context()


def get_json(url, ctx, retries=3):
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(url, context=ctx, timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            # 613 / 4 / 17 are Graph API rate limits; back off and retry.
            if attempt < retries and any(f'"code":{c}' in body for c in (4, 17, 613)):
                time.sleep(2 ** (attempt + 2))
                continue
            sys.exit(f"Meta API error {e.code}: {body[:500]}")
        except urllib.error.URLError as e:
            if attempt < retries:
                time.sleep(2 ** (attempt + 1))
                continue
            sys.exit(f"Network error: {e}")


def fetch_ads(query, token, api_version, ctx):
    params = {
        "access_token": token,
        "ad_type": "ALL",
        "ad_active_status": query.get("active_status", "ACTIVE"),
        "ad_reached_countries": json.dumps(query.get("countries", EU_COUNTRIES)),
        "fields": ",".join(FIELDS),
        "limit": 100,
    }
    if query.get("terms"):
        params["search_terms"] = query["terms"]
        params["search_type"] = query.get("search_type", "KEYWORD_UNORDERED")
    if query.get("page_ids"):
        params["search_page_ids"] = json.dumps(query["page_ids"][:10])
    if query.get("days"):
        since = dt.date.today() - dt.timedelta(days=int(query["days"]))
        params["ad_delivery_date_min"] = since.isoformat()

    url = f"https://graph.facebook.com/{api_version}/ads_archive?" + urllib.parse.urlencode(params)
    ads, max_ads = [], int(query.get("max_ads", 300))
    while url and len(ads) < max_ads:
        page = get_json(url, ctx)
        ads.extend(page.get("data", []))
        url = page.get("paging", {}).get("next")
    return ads[:max_ads]


def first_line(ad):
    bodies = ad.get("ad_creative_bodies") or []
    text = bodies[0].strip() if bodies else ""
    return re.split(r"(?<=[.!?])\s|\n", text, maxsplit=1)[0][:140]


def hook_type(line):
    low = line.lower()
    if not line:
        return "no body text"
    if line.endswith("?") or low.startswith(("what", "why", "how", "are you", "do you", "tired")):
        return "question"
    if re.match(r"^[\d$€£₹]", line):
        return "number / price"
    if re.search(r"\bfree\b", low):
        return "free offer"
    if re.search(r"\b(stop|never|no more|forget)\b", low):
        return "pain / stop doing X"
    return "statement"


def summarize(name, query, ads):
    lines = [f"## {name}", ""]
    terms = query.get("terms") or f"page ids {query.get('page_ids')}"
    lines.append(
        f"Query: `{terms}` | countries: {','.join(query.get('countries', EU_COUNTRIES))} | "
        f"status: {query.get('active_status', 'ACTIVE')} | "
        f"window: {'last ' + str(query['days']) + ' days' if query.get('days') else 'all time'} | "
        f"pulled {dt.date.today().isoformat()} | ads: {len(ads)}"
    )
    lines.append("")
    if not ads:
        lines += ["No ads returned.", ""]
        return lines

    pages = collections.defaultdict(list)
    for ad in ads:
        pages[ad.get("page_name", "?")].append(ad)

    lines += ["### Top advertisers", "", "| Page | Ads | EU reach | Platforms | Newest start | Example headline |", "|---|---|---|---|---|---|"]
    ranked = sorted(pages.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    for page, items in ranked[:15]:
        reach = sum(a.get("eu_total_reach") or 0 for a in items)
        plats = collections.Counter(p for a in items for p in a.get("publisher_platforms") or [])
        newest = max((a.get("ad_delivery_start_time") or "") for a in items)[:10]
        titles = [t for a in items for t in a.get("ad_creative_link_titles") or [] if t]
        example = titles[0].replace("|", "/")[:60] if titles else ""
        lines.append(
            f"| {page} | {len(items)} | {reach:,} | {', '.join(p for p, _ in plats.most_common(3))} | {newest} | {example} |"
        )
    lines.append("")

    hooks = collections.Counter(hook_type(first_line(a)) for a in ads)
    lines += ["### Hook types (first line of body)", "", "| Hook | Ads | Example | Library URL |", "|---|---|---|---|"]
    for hook, count in hooks.most_common():
        ex = next(a for a in ads if hook_type(first_line(a)) == hook)
        lines.append(f"| {hook} | {count} | {first_line(ex).replace('|', '/')} | https://www.facebook.com/ads/library/?id={ex.get('id')} |")
    lines.append("")

    ages, genders = collections.Counter(), collections.Counter()
    countries = collections.Counter()
    for ad in ads:
        for row in ad.get("age_country_gender_reach_breakdown") or []:
            for bucket in row.get("age_gender_breakdowns") or []:
                total = sum(bucket.get(k) or 0 for k in ("male", "female", "unknown"))
                ages[bucket.get("age_range", "?")] += total
                countries[row.get("country", "?")] += total
                for k in ("male", "female", "unknown"):
                    genders[k] += bucket.get(k) or 0

    if ages:
        total = sum(ages.values()) or 1
        lines += ["### Who actually saw these ads (EU reach, all advertisers)", ""]
        lines.append("Age: " + ", ".join(f"{k} {v / total:.0%}" for k, v in sorted(ages.items())))
        gtotal = sum(genders.values()) or 1
        lines.append("Gender: " + ", ".join(f"{k} {v / gtotal:.0%}" for k, v in genders.most_common()))
        lines.append("Top countries: " + ", ".join(f"{k} {v / total:.0%}" for k, v in countries.most_common(6)))
        lines.append("")

    target_ages = collections.Counter(
        f"{a['target_ages'][0]}-{a['target_ages'][-1]}" for a in ads if a.get("target_ages")
    )
    target_gender = collections.Counter(a.get("target_gender") for a in ads if a.get("target_gender"))
    if target_ages or target_gender:
        lines += ["### What advertisers targeted", ""]
        lines.append("Age ranges set: " + ", ".join(f"{k} ({v})" for k, v in target_ages.most_common(5)))
        lines.append("Gender set: " + ", ".join(f"{k} ({v})" for k, v in target_gender.most_common()))
        lines.append("")

    recent = sorted(ads, key=lambda a: a.get("ad_delivery_start_time") or "", reverse=True)[:8]
    lines += ["### Most recently launched", "", "| Page | Started | Headline | Hook | Library URL |", "|---|---|---|---|---|"]
    for ad in recent:
        title = ((ad.get("ad_creative_link_titles") or [""])[0] or "").replace("|", "/")[:50]
        lines.append(
            f"| {ad.get('page_name')} | {(ad.get('ad_delivery_start_time') or '')[:10]} | {title} | "
            f"{first_line(ad).replace('|', '/')[:80]} | https://www.facebook.com/ads/library/?id={ad.get('id')} |"
        )
    lines.append("")
    return lines


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queries", type=Path, default=DEFAULT_QUERIES, help="JSON file of named queries")
    ap.add_argument("--terms", help="Run one keyword query instead of the queries file")
    ap.add_argument("--countries", help="Comma-separated ISO codes (EU only for non-political ads)")
    ap.add_argument("--days", type=int, help="Only ads delivered in the last N days")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--api-version", default=os.environ.get("META_GRAPH_API_VERSION", "v23.0"))
    args = ap.parse_args()

    token = os.environ.get("META_AD_LIBRARY_TOKEN")
    if not token:
        sys.exit("Set META_AD_LIBRARY_TOKEN first (see ads/scripts/README.md).")

    if args.terms:
        queries = {args.terms: {"terms": args.terms}}
    else:
        queries = json.loads(args.queries.read_text())
    for q in queries.values():
        if args.countries:
            q["countries"] = args.countries.split(",")
        if args.days:
            q["days"] = args.days

    ctx = ssl_context()
    stamp = dt.date.today().isoformat()
    args.out.mkdir(parents=True, exist_ok=True)
    raw_path = args.out / f"meta-ad-library-{stamp}.jsonl"
    report = [f"# Meta Ad Library pull, {stamp}", "", "Source: official Meta Ad Library API (ads delivered in the EU).", ""]

    with raw_path.open("w") as raw:
        for name, query in queries.items():
            ads = fetch_ads(query, token, args.api_version, ctx)
            print(f"{name}: {len(ads)} ads", file=sys.stderr)
            for ad in ads:
                raw.write(json.dumps({"query": name, **ad}) + "\n")
            report += summarize(name, query, ads)

    report_path = args.out / f"meta-ad-library-{stamp}.md"
    report_path.write_text("\n".join(report))
    print(f"Wrote {report_path} and {raw_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
