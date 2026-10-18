#!/usr/bin/env python3
"""Rewrite the article index table in blog/README.md with current word counts and gate results.

Replaces everything between the INDEX markers in README.md. Run after any article edit.

Usage:
    python3 blog/tools/build_index.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from aeo_score import plain, score as aeo, words  # noqa: E402
from humanize_verify import metrics, prose, verdict  # noqa: E402
from post_humanize_check import body_paragraphs, check as phc, split  # noqa: E402
from seo_score import depth_results, score as seo  # noqa: E402

START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"


def main():
    paths = sorted((ROOT / "articles").glob("*.md"))
    fms = {p: yaml.safe_load(p.read_text(encoding="utf-8").split("---\n", 2)[1]) for p in paths}
    # keep the topic-plan order already used in the README table (new slugs go last)
    plan = re.findall(r"^\| \d+ \| .*?\| `([a-z0-9-]+)` \|", (ROOT / "README.md").read_text(), re.M)
    paths.sort(key=lambda p: plan.index(p.stem) if p.stem in plan else 999)
    depth = depth_results()
    para_index = defaultdict(set)
    for p in paths:
        for para in body_paragraphs(split(p)[1]):
            para_index[para].add(p.stem)
    rows = ["| # | Title | Slug | Primary keyword | Market | Words | AEO | SEO | Humanize | Post-check |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for i, p in enumerate(paths, 1):
        fm = fms[p]
        body = p.read_text(encoding="utf-8").split("---\n", 2)[2].split("<!-- HANDOFF")[0]
        title = re.search(r"^# (.+)$", body, re.M).group(1)
        a = aeo(p)
        s_total, _, g = seo(p, depth)
        s_ok = s_total >= 85 and all(v[0] for v in g.values())
        h_score, h_label, _ = verdict(metrics(prose(p)))
        c, _ = phc(p, ROOT / "humanize" / "originals", para_index)
        rows.append(f"| {i} | [{title}](articles/{p.name}) | `{p.stem}` | {fm['primary_keyword']} | {fm['market']} | "
                    f"{len(words(plain(body)))} | {a['total']} | {s_total}{'' if s_ok else ' FIX'} | "
                    f"{h_score:.0f}% {h_label} | {'PASS' if not any(c.values()) else 'FAIL'} |")
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    new = f"{START}\n" + "\n".join(rows) + f"\n{END}"
    text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: new, text, flags=re.S)
    readme.write_text(text, encoding="utf-8")
    print(f"index rewritten: {len(paths)} articles")


if __name__ == "__main__":
    main()
