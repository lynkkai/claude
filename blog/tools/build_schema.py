#!/usr/bin/env python3
"""Build JSON-LD (Article + FAQPage + BreadcrumbList) for each Lynkk article.

The FAQPage entries are read from the article's own "## FAQ" section, so the
schema can never drift from the visible FAQ. Re-run after any FAQ edit.

Usage:
    python3 blog/tools/build_schema.py            # writes blog/schema/<slug>.json
"""
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://lynkk.ai"


def plain(md):
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"[*_`]", "", md)
    return re.sub(r"\s+", " ", md).strip()


def faq_pairs(body):
    parts = re.split(r"^## (?:FAQ|Frequently asked questions).*$", body,
                     flags=re.M | re.I)
    if len(parts) < 2:
        return []
    faq = re.split(r"^## ", parts[1], flags=re.M)[0]
    pairs = []
    for block in re.split(r"^### ", faq, flags=re.M)[1:]:
        question, _, answer = block.partition("\n")
        pairs.append((question.strip(), plain(answer)))
    return pairs


def build(path):
    raw = path.read_text(encoding="utf-8")
    _, fm, body = raw.split("---\n", 2)
    fm = yaml.safe_load(fm)
    url = f"{SITE}/blog/{fm['slug']}"
    lang = "en-IN" if fm.get("market") == "India" else "en-US"
    graph = [
        {
            "@type": "Article",
            "headline": fm["title"],
            "description": fm["meta_description"],
            "inLanguage": lang,
            "mainEntityOfPage": url,
            "dateModified": str(fm["last_updated"]),
            "author": {"@type": "Person", "name": fm["author"]},
            "publisher": {"@type": "Organization", "name": "Lynkk", "url": SITE},
            "image": f"{SITE}/blog/images/{fm['slug']}.png",
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog"},
                {"@type": "ListItem", "position": 3, "name": fm["title"], "item": url},
            ],
        },
    ]
    pairs = faq_pairs(body)
    if pairs:
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in pairs
            ],
        })
    return fm["slug"], {"@context": "https://schema.org", "@graph": graph}


def main():
    out = ROOT / "schema"
    out.mkdir(exist_ok=True)
    for path in sorted((ROOT / "articles").glob("*.md")):
        slug, data = build(path)
        (out / f"{slug}.json").write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote schema/{slug}.json")


if __name__ == "__main__":
    main()
