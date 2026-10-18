#!/usr/bin/env python3
"""/post-humanize-check equivalent: confirm the humanize rewrite kept the article intact.

Compares each article with its pre-rewrite backup in humanize/originals/<slug>.md.
  C1  primary keyword, and every secondary keyword the original contained, still in the body
  C2  primary keyword (all its words) in the H1, or H1 identical to the original
  C3  at least 50% of H2s are questions
  C4  every internal (lynkk.ai) link from the original is still present
  C5  no em or en dashes
  C6  no AI-tell words (list shared with humanize_verify.py)
  C7  every external link from the original is still present
  C8  frontmatter unchanged
  C9  headings unchanged (same H1/H2/H3 text, same order)
  C10 FAQ answers 40-60 words
  C11 every number from the original body is still present
  C12 no sentence over 40 words
  C13 no new draft artifacts (TODO, [insert, lorem, "as an AI"); template placeholders
      such as [link] that were already in the original are intended
  C14 brand spelled "Lynkk"
  C15 no paragraph duplicated across the batch
  C16 tables, lists and code blocks unchanged
  C17 AEO re-score still >= 80 with no CRITICAL finding
Any failure blocks publishing.

Usage:
    python3 blog/tools/post_humanize_check.py            # every article
    python3 blog/tools/post_humanize_check.py <file> -v  # one article, every check listed
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from aeo_score import body_paragraphs, faq_answers, is_question, plain, score as aeo, sentences, words  # noqa: E402
from humanize_verify import AI_TELLS  # noqa: E402
from seo_score import has_kw, nostop  # noqa: E402

NUM = re.compile(r"\$?\d+(?:,\d{3})*(?:\.\d+)?%?")
LINK = re.compile(r"\]\((https?://[^)\s]+)\)")
DRAFT = re.compile(r"\bTODO\b|\[insert|lorem ipsum|\bTBD\b|\bXXX\b|as an AI\b|\[(?:link|source|citation)\]", re.I)
MISSPELL = re.compile(r"\b(?:Lynk|Linnk|Link AI)\b")


def split(path):
    _, fm, body = path.read_text(encoding="utf-8").split("---\n", 2)
    return fm, body.split("<!-- HANDOFF")[0]


def structure(body):
    """Lines that the rewrite must not touch: tables, list items and code blocks."""
    out, code = [], False
    for line in body.splitlines():
        if line.startswith("```"):
            code = not code
        if code or line.startswith(("```", "|", "- ", "* ")) or re.match(r"\d+\. ", line):
            out.append(line.rstrip())
    return out


def check(path, originals, para_index):
    fm_text, body = split(path)
    fm = yaml.safe_load(fm_text)
    orig = originals / path.name
    o_fm, o_body = split(orig) if orig.exists() else (fm_text, body)
    text = plain(body)
    heads = re.findall(r"^(#{1,3}) (.+)$", body, re.M)
    h2 = [h for lvl, h in heads if lvl == "##"]
    links, o_links = set(LINK.findall(body)), set(LINK.findall(o_body))
    sents = [s for p in body_paragraphs(body) for s in sentences(plain(p))]
    lost_nums = set(NUM.findall(o_body)) - set(NUM.findall(body))
    a = aeo(path)
    o_text = plain(o_body)
    kws = [fm["primary_keyword"]] + [k for k in fm.get("secondary_keywords", []) if has_kw(o_text, k)]
    kw_words = {w.rstrip("s") for w in nostop(fm["primary_keyword"]).split()}
    c = {
        "C1 keywords present": [k for k in kws if not has_kw(text, k)],
        "C2 keyword in H1": [] if kw_words <= {w.rstrip("s") for w in nostop(heads[0][1]).split()}
                            or f"# {heads[0][1]}\n" in o_body
                            else [heads[0][1]],
        "C3 question H2s >= 50%": [] if sum(map(is_question, h2)) * 2 >= len(h2) else [f"{sum(map(is_question, h2))}/{len(h2)}"],
        "C4 internal links kept": sorted(u for u in o_links - links if "lynkk.ai" in u),
        "C5 no em/en dashes": ["dash"] * (body.count("—") + body.count("–")),
        "C6 no AI-tell words": [t for t in AI_TELLS if t in text.lower()],
        "C7 external links kept": sorted(u for u in o_links - links if "lynkk.ai" not in u),
        "C8 frontmatter unchanged": [] if fm_text == o_fm else ["frontmatter differs"],
        "C9 headings unchanged": [] if heads == re.findall(r"^(#{1,3}) (.+)$", o_body, re.M) else ["headings differ"],
        "C10 FAQ answers 40-60 words": [q for q, ans in faq_answers(body) if not 40 <= len(words(ans)) <= 60],
        "C11 numbers kept": sorted(lost_nums),
        "C12 sentences <= 40 words": [s[:50] + "..." for s in sents if len(words(s)) > 40],
        "C13 no draft artifacts": sorted(set(DRAFT.findall(body)) - set(DRAFT.findall(o_body))),
        "C14 brand spelling": MISSPELL.findall(body),
        "C15 no duplicate paragraphs": [f"also in {', '.join(sorted(para_index[p] - {path.stem}))}"
                                        for p in body_paragraphs(body)
                                        if len(words(p)) >= 15 and len(para_index[p]) > 1],
        "C16 tables/lists/code unchanged": [] if structure(body) == structure(o_body) else ["structure differs"],
        "C17 AEO >= 80, no CRITICAL": [] if a["total"] >= 80 and not a["crit"] else [f"AEO {a['total']}"],
    }
    return c, a["total"]


def main(argv):
    verbose = "-v" in argv
    all_paths = sorted((ROOT / "articles").glob("*.md"))
    paths = [Path(p) for p in argv if p != "-v"] or all_paths
    para_index = defaultdict(set)
    for p in all_paths:
        for para in body_paragraphs(split(p)[1]):
            para_index[para].add(p.stem)
    originals = ROOT / "humanize" / "originals"
    bad = 0
    print(f"{'article':42} {'AEO':>4}  result")
    for p in paths:
        c, total = check(p, originals, para_index)
        fails = {k: v for k, v in c.items() if v}
        bad += bool(fails)
        print(f"{p.stem:42} {total:>4}  {'PASS' if not fails else 'FAIL: ' + ', '.join(k.split()[0] for k in fails)}")
        for k, v in c.items():
            if v or verbose:
                print(f"    {'FAIL' if v else 'PASS'} {k}" + (f": {v[:5]}" if v else ""))
    print(f"\n{len(paths)} checked, {bad} failing (C1-C17)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
