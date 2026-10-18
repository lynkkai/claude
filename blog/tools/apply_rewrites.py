#!/usr/bin/env python3
"""Apply paragraph rewrites by index (humanize step helper).

Input JSON: {"slug": {"<paragraph index from paras.py>": "new paragraph text"}}.
Refuses a rewrite that drops a number, a link or a bolded term from the original
paragraph, so facts cannot silently disappear during the rewrite.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from aeo_score import body_paragraphs  # noqa: E402

ARTICLES = Path(__file__).resolve().parents[1] / "articles"


def facts(text):
    nums = set(re.findall(r"\$?\d+(?:,\d{3})*(?:\.\d+)?%?", text))
    links = set(re.findall(r"\]\((https?://[^)]+)\)", text))
    return nums, links


for f in sys.argv[1:]:
    for slug, rewrites in json.load(open(f)).items():
        path = ARTICLES / f"{slug}.md"
        raw = path.read_text(encoding="utf-8")
        body = raw.split("---\n", 2)[-1].split("<!-- HANDOFF")[0]
        paras = body_paragraphs(body)
        for idx, new in rewrites.items():
            old = paras[int(idx)]
            (on, ol), (nn, nl) = facts(old), facts(new)
            lost = (on - nn) | (ol - nl)
            if lost:
                print(f"  SKIP {slug}[{idx}]: would drop {sorted(lost)}")
                continue
            faq_start = raw.find("## FAQ")
            in_faq = faq_start != -1 and raw.find(old) > faq_start
            n = len(new.split())
            if in_faq and not 40 <= n <= 62:
                print(f"  SKIP {slug}[{idx}]: FAQ answer would be {n} words (keep 40-60)")
                continue
            if raw.count(old) != 1:
                print(f"  SKIP {slug}[{idx}]: paragraph not unique")
                continue
            raw = raw.replace(old, new, 1)
        path.write_text(raw, encoding="utf-8")
