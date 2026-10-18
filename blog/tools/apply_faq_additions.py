#!/usr/bin/env python3
"""One-off: extend FAQ answers to the /aeo-score 40-60 word band.

Reads JSON files mapping slug -> list of strings (one per FAQ, in order).
An empty string leaves the answer alone; a string starting with "=" replaces
the answer; anything else is appended as a new sentence. Reports any answer
that ends outside 40-60 words.
"""
import json
import re
import sys
from pathlib import Path

ARTICLES = Path(__file__).resolve().parents[1] / "articles"
sys.path.insert(0, str(Path(__file__).parent))
from aeo_score import words, plain  # noqa: E402


def apply(slug, extras):
    path = ARTICLES / f"{slug}.md"
    raw = path.read_text(encoding="utf-8")
    head, faq_hdr, rest = re.split(r"(^## FAQ\s*$)", raw, maxsplit=1, flags=re.M)
    faq, sep, tail = rest.partition("\n## ")
    if not sep and "<!--" in faq:
        faq, c, comment = faq.partition("<!--")
        sep, tail = "\n", "<!--" + comment
    blocks = re.split(r"(^### .+$)", faq, flags=re.M)
    qi = 0
    for i in range(1, len(blocks), 2):
        if qi >= len(extras):
            break
        extra = extras[qi]
        answer = blocks[i + 1].strip()
        if extra.startswith("="):
            answer = extra[1:]
        elif extra:
            answer = f"{answer} {extra}"
        n = len(words(plain(answer)))
        if not 40 <= n <= 60:
            print(f"  {slug} Q{qi + 1}: {n} words")
        blocks[i + 1] = f"\n\n{answer}\n\n"
        qi += 1
    faq = "".join(blocks).rstrip("\n") + "\n"
    path.write_text(head + faq_hdr + faq + (sep + tail if sep else ""), encoding="utf-8")


for f in sys.argv[1:]:
    for slug, extras in json.load(open(f)).items():
        apply(slug, extras)
