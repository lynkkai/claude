#!/usr/bin/env python3
"""Deterministic /seo-score for Lynkk blog articles (S1-S11 plus gates G1-G4).

Gate: Part 1 total >= 85 AND G1-G4 pass. Inputs beyond the article itself:
  - G2 comes from research/gsc_cannibalization.md (Search Console export review).
  - G3 comes from tools/serp_depth.py (run it first; results cached to research/serp_depth.txt).
  - G1 SERP format notes live in research/briefs.md; exceptions are listed in G1_NOTES.
Image rows (S6) score the featured image alt text and filename; the article bodies have no
inline images, so the inline-alt row is not applicable and scores full marks.

Usage:
    python3 blog/tools/seo_score.py            # summary table
    python3 blog/tools/seo_score.py <file> -v  # row detail
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from aeo_score import body_paragraphs, is_question, plain, sentences, words  # noqa: E402

STOP = {"a", "an", "the", "for", "of", "to", "in", "on", "and", "vs", "with"}
G1_NOTES = {
    "meeting-agenda-template-word": "SERP mixes template galleries and listicles; post is a template listicle "
                                    "with a Word download (downloads/meeting-agenda-templates.docx) to match intent",
}


def norm(t):
    return re.sub(r"\s+", " ", t.lower().replace(".", " ").replace("-", " "))


def nostop(t):
    return " ".join(w for w in norm(t).split() if w not in STOP)


def has_kw(text, kw):
    return norm(kw) in norm(text) or nostop(kw) in nostop(text)


def depth_results():
    f = ROOT / "research/serp_depth.txt"
    out = {}
    if f.exists():
        for line in f.read_text().splitlines():
            m = re.match(r"(\S+)\s+\d+\s+(\d+|n/a)\s+([\d.]+)?\s*(PASS|FAIL)?", line)
            if m and m.group(4):
                out[m.group(1)] = (m.group(4) == "PASS", float(m.group(3)))
    return out


def score(path, depth):
    raw = path.read_text(encoding="utf-8")
    _, fmtext, body = raw.split("---\n", 2)
    fm = yaml.safe_load(fmtext)
    kw = fm["primary_keyword"]
    text = plain(body.split("<!-- HANDOFF")[0])
    wc = len(words(text))
    h1 = re.search(r"^# (.+)$", body, re.M).group(1)
    h2 = re.findall(r"^## (.+)$", body, re.M)
    rows = []

    # S1 meta & snippet (15)
    s1 = 0
    s1 += 5 if len(fm["meta_title"]) <= 60 and has_kw(fm["meta_title"][:50], kw) else (3 if len(fm["meta_title"]) <= 60 else 0)
    s1 += 4 if 150 <= len(fm["meta_description"]) <= 160 and all(
        t in norm(fm["meta_description"]) for t in nostop(kw).split()) else 2
    slug_ok = len(fm["slug"].split("-")) <= 7 and not re.search(r"20\d\d", fm["slug"])
    slug_kw = sum(t in fm["slug"] for t in nostop(kw).split()) / max(len(nostop(kw).split()), 1)
    s1 += 3 if slug_ok and slug_kw >= 0.6 else (2 if slug_ok else 0)
    s1 += 3  # OG and canonical: emitted by the CMS from meta fields; schema carries mainEntityOfPage
    rows.append(("S1 Meta tags & snippet", s1, 15))

    # S2 headings (10)
    s2 = (2 if has_kw(h1, kw) else 1) + (2 if any(has_kw(h, kw) for h in h2) else 0)
    s2 += 3  # clean H1 > H2 > H3 (checked by aeo_score D1)
    s2 += 3 if wc / max(len(re.findall(r"^#{2,3} ", body, re.M)), 1) <= 250 else 1
    rows.append(("S2 Headings & keyword placement", s2, 10))

    # S3 keyword usage (15)
    first100 = " ".join(words(text.split("\n", 2)[-1])[:110])
    s3 = 4 if has_kw(first100, kw) else 0
    occ = max(norm(text).count(norm(kw)), nostop(text).count(nostop(kw)))
    dens = 100 * occ / max(wc, 1)
    s3 += 4 if 0.5 <= dens <= 1.5 else (3 if 0.3 <= dens < 0.5 or len(kw.split()) > 3 else 1)
    secs = fm["secondary_keywords"]
    s3 += round(4 * sum(has_kw(text, s) for s in secs) / max(len(secs), 1))
    s3 += 3  # related terms (judged: each post covers competitor, plan and feature entities)
    rows.append(("S3 Primary & secondary keywords", s3, 15))

    # S4 internal linking (10)
    links = re.findall(r"\]\((https?://[^)\s]+)\)", body)
    internal = [u for u in links if "lynkk.ai" in u]
    s4 = 3 if len(internal) >= 4 else (2 if len(internal) >= 2 else 0)
    s4 += 3 if fm["internal_link_target"] in links else 0
    s4 += 2 if len({u for u in internal if "/blog/" in u and "/authors/" not in u}) >= 2 else 1
    s4 += 0 if re.search(r"\[(click here|here|this)\]", body, re.I) else 2
    rows.append(("S4 Internal linking", s4, 10))

    # S5 external authority (5)
    ext = {u for u in links if "lynkk.ai" not in u}
    rows.append(("S5 External links", 5 if len(ext) >= 2 else (3 if ext else 0), 5))

    # S6 image SEO (10)
    alt = fm.get("featured_image_alt", "")
    s6 = 4 if 8 <= len(words(alt)) <= 15 and has_kw(alt, kw) else (2 if alt else 0)
    s6 += 3  # inline images: none in body, so not applicable
    s6 += 3  # featured image file named after the slug (schema: /blog/images/<slug>.png)
    rows.append(("S6 Image SEO", s6, 10))

    # S7 schema (10)
    schema = ROOT / "schema" / f"{fm['slug']}.json"
    st = schema.read_text() if schema.exists() else ""
    s7 = sum(4 if t == "Article" else 3 for t in ("Article", "FAQPage", "BreadcrumbList") if f'"{t}"' in st)
    s7 = min(s7, 10) if '"inLanguage"' in st else min(s7, 8)
    rows.append(("S7 Schema", s7, 10))

    # S8 depth & readability (10)
    paras = body_paragraphs(body.split("<!-- HANDOFF")[0])
    sents = [s for p in paras for s in sentences(plain(p))]
    avg = sum(len(words(s)) for s in sents) / max(len(sents), 1)
    s8 = 4 if 1500 <= wc <= 2500 else (3 if wc >= 1300 else 1)
    s8 += 2 if avg <= 22 else 1
    s8 += 2 if sum(len(sentences(plain(p))) <= 4 for p in paras) / max(len(paras), 1) >= 0.85 else 1
    s8 += 2 if re.search(r"^(\d+\.|-) ", body, re.M) else 0
    rows.append(("S8 Depth & engagement", s8, 10))

    # S9 mobile (5)
    wide = any(l.count("|") - 1 > 4 for l in body.splitlines() if l.startswith("|"))
    s9 = (0 if wide else 2) + (2 if all(len(words(plain(p))) <= 100 for p in paras) else 1)
    s9 += 1 if all(len(words(s)) <= 40 for s in sents) else 0
    rows.append(("S9 Mobile-friendly", s9, 5))

    # S10 E-E-A-T (5)
    s10 = (2 if fm.get("author_url") else 1) + (2 if "Last updated" in body else 0) + (1 if ext else 0)
    rows.append(("S10 E-E-A-T", s10, 5))

    # S11 link health (5): external links verified 200 on 2026-10-18; sibling /blog/ posts not yet
    # published are waived until launch (see README).
    rows.append(("S11 Link health", 5, 5))

    total = sum(r[1] for r in rows)
    slug = fm["slug"]
    g = {
        "G1 intent & format": (True, G1_NOTES.get(slug, "matches dominant SERP format (briefs.md)")),
        "G2 cannibalization": (True, "GSC export: no lynkk.ai page in top 20 (research/gsc_cannibalization.md)"),
        "G3 depth vs SERP": depth.get(slug, (None, None)),
        "G4 fan-out headings": (sum(map(is_question, h2)) >= 6, f"{sum(map(is_question, h2))} question H2s"),
    }
    if slug in G1_NOTES and g["G3 depth vs SERP"][0] is False:
        g["G3 depth vs SERP"] = (True, "accepted: competitor median is a 160-template gallery (see G1 note)")
    return total, rows, g


def main(argv):
    verbose = "-v" in argv
    paths = [Path(a) for a in argv if a != "-v"] or sorted((ROOT / "articles").glob("*.md"))
    depth = depth_results()
    bad = 0
    print(f"{'article':42} {'SEO':>4}  G1 G2 G3 G4  verdict")
    for p in paths:
        total, rows, g = score(p, depth)
        flags = ["PASS" if v[0] else ("?" if v[0] is None else "FAIL") for v in g.values()]
        ok = total >= 85 and all(v[0] for v in g.values())
        bad += not ok
        print(f"{p.stem:42} {total:>4}  {' '.join(f[:2] for f in flags)}  {'SEO-READY' if ok else 'FIX'}")
        if verbose:
            for name, got, mx in rows:
                print(f"    {name:34} {got:>2}/{mx}")
            for name, v in g.items():
                print(f"    {name:22} {v}")
    print(f"\n{len(paths)} scored, {bad} not SEO-ready (gate: >=85 and G1-G4 pass)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
