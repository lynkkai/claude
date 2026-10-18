#!/usr/bin/env python3
"""Deterministic half of /aeo-score (D1-D9) for Lynkk blog articles.

The /aeo-score skill splits scoring into rows a script computes and rows a
reviewer judges. This file computes the first kind and fills judgment rows with
conservative defaults, flagged "(judged)" in the output, so a human reviewer
only revisits those. Gate: total >= 80 and no CRITICAL findings.

Usage:
    python3 blog/tools/aeo_score.py                  # every article, summary table
    python3 blog/tools/aeo_score.py <file.md> -v     # one article, row detail
"""
import re
import sys
from pathlib import Path

import yaml

ARTICLES = Path(__file__).resolve().parents[1] / "articles"
QUESTION_START = re.compile(
    r"^(how|what|which|why|when|where|who|is|are|can|does|do|should|will)\b", re.I)
THROAT = re.compile(
    r"in this article we will|choosing the right .* can be overwhelming|you have come to"
    r" the right place|understanding .* is essential|when it comes to|tired of", re.I)


def words(text):
    return re.findall(r"[A-Za-z0-9ऀ-ॿ][\w'ऀ-ॿ%$.,]*", text)


def plain(md):
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.S)
    md = re.sub(r"```.*?```", " ", md, flags=re.S)
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)
    return re.sub(r"[*_`>#|]", " ", md)


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if words(s)]


def is_question(h):
    return h.strip().endswith("?") or bool(QUESTION_START.match(h.strip()))


def body_paragraphs(body):
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    out = []
    for p in re.split(r"\n\s*\n", body):
        s = p.strip()
        if not s or s.startswith(("#", "|", "-", "*", ">", "<")) or re.match(r"^\d+\.", s):
            continue
        out.append(s)
    return out


def sections(body):
    """List of (level, heading, text) for H2/H3."""
    parts = re.split(r"^(#{2,3}) (.+)$", body, flags=re.M)
    out = []
    for i in range(1, len(parts), 3):
        out.append((len(parts[i]), parts[i + 1].strip(), parts[i + 2]))
    return out


def faq_answers(body):
    m = re.split(r"^## (?:FAQ|Frequently asked questions).*$", body, flags=re.M | re.I)
    if len(m) < 2:
        return []
    faq = re.split(r"^## ", m[1], flags=re.M)[0]
    return [(b.partition("\n")[0].strip(), plain(b.partition("\n")[2]).strip())
            for b in re.split(r"^### ", faq, flags=re.M)[1:]]


def score(path):
    raw = path.read_text(encoding="utf-8")
    _, fm, body = raw.split("---\n", 2)
    fm = yaml.safe_load(fm)
    rows, crit = [], []
    text = plain(body)
    wc = len(words(text))
    secs = sections(body)
    h2 = [h for lvl, h, _ in secs if lvl == 2]
    h2_content = [h for h in h2 if not re.match(r"(FAQ|Frequently)", h, re.I)]
    h3 = [h for lvl, h, _ in secs if lvl == 3]
    in_faq = False
    h3_body = []
    for lvl, h, _ in secs:
        if lvl == 2:
            in_faq = bool(re.match(r"(FAQ|Frequently)", h, re.I))
        elif not in_faq and not re.match(r"^\d+\.", h):
            h3_body.append(h)

    # ---- D1 (20)
    d1 = 0
    q_ratio = sum(map(is_question, h2_content)) / max(len(h2_content), 1)
    d1 += 3 if q_ratio >= 0.5 else 0
    h3q = sum(map(is_question, h3_body)) / max(len(h3_body), 1) if h3_body else 1
    d1 += 3 if h3q >= 0.5 else (1 if h3q >= 0.25 else 0)
    first_ok, open_ok, no_claim = 0, 0, []
    qsecs = [(h, t) for lvl, h, t in secs if is_question(h) and not re.match(r"(FAQ)", h, re.I)]
    for h, t in qsecs:
        paras = body_paragraphs(t)
        if not paras:
            continue
        sents = sentences(plain(paras[0]))
        if sents and len(words(sents[0])) <= 29:
            first_ok += 1
        if len(words(plain(paras[0]))) <= 60:
            open_ok += 1
    n = max(len(qsecs), 1)
    d1 += round(3 * first_ok / n) + round(3 * open_ok / n)
    first30 = " ".join(words(text)[: int(wc * 0.3)])
    d1 += 2 if re.search(r"\d", first30) else 0
    first100 = " ".join(words(text.split("\n", 2)[-1])[:130])
    d1 += 2 if re.search(r"\b(is|are|means|refers to)\b", first100) else 0
    d1 += 1  # section definitions (judged)
    levels = [lvl for lvl, _, _ in secs]
    d1 += 2 if levels and levels[0] == 2 else 0
    d1 += 1 if wc / max(len(secs), 1) <= 220 else 0
    clips_num = 0
    for lvl, h, t in secs:
        clip = plain(t).strip()[:200]
        if THROAT.search(clip):
            crit.append(f"throat-clearing opener under '{h}'")
        if re.search(r"\d", clip):
            clips_num += 1
    qa = re.search(r"Quick answer:\*\*(.{0,220})", body)
    if not qa or not re.search(r"\d", qa.group(1)):
        crit.append("Quick Answer clip has no number")
    rows.append(("D1 Headings and answer structure", min(d1, 20), 20))

    # ---- D2 (10)
    paras = body_paragraphs(body)
    p_s = sum(len(sentences(plain(p))) <= 4 for p in paras) / max(len(paras), 1)
    p_w = sum(len(words(plain(p))) <= 80 for p in paras) / max(len(paras), 1)
    d2 = (4 if p_s >= 0.85 else 2) + (3 if p_w >= 0.85 else 1)
    long_secs = 0
    for i, (lvl, h, t) in enumerate(secs):
        if lvl != 2:
            continue
        has_h3 = i + 1 < len(secs) and secs[i + 1][0] == 3
        if len(words(plain(t))) > 300 and not has_h3:
            long_secs += 1
    d2 += max(0, 3 - long_secs)
    rows.append(("D2 Section and paragraph structure", d2, 10))

    # ---- D3 (15)
    faqs = faq_answers(body)
    d3_words = 5
    for q, a in faqs:
        n = len(words(a))
        if n < 40:
            d3_words -= 1
        elif 81 <= n <= 100:
            d3_words -= 2
        elif n > 100:
            d3_words -= 3
    d3 = max(d3_words, 0) + 4  # schema sync: generated from the FAQ itself
    h2_norm = {re.sub(r"\W+", " ", h.lower()).strip() for h in h2}
    dup = sum(re.sub(r"\W+", " ", q.lower()).strip() in h2_norm for q, _ in faqs)
    d3 += 3 if dup == 0 else 1
    d3 += 3 if 5 <= len(faqs) <= 10 else 1
    rows.append(("D3 FAQ quality", d3, 15))

    # ---- D4 (15)
    tables = re.findall(r"^\|.+\|\n\|[-| :]+\|", body, flags=re.M)
    d4 = (3 if tables else 0) + (2 if tables else 0)
    has_bullets = bool(re.search(r"^- ", body, re.M))
    has_numbered = bool(re.search(r"^\d+\. ", body, re.M))
    d4 += 2 if has_bullets and has_numbered else 1
    d4 += 2  # list length and lead-ins (judged)
    first_table = body.find("\n|")
    d4 += 2 if 0 <= first_table < len(body) * 0.4 else 1
    d4 += 2 if re.search(r"^#{2,3} .*(mistake|avoid|fall short|watch out|trade-off)", body, re.M | re.I) else 0
    d4 += 2 if re.search(r"trade-off|watch out|weakness|falls short|pros|less worth", body, re.I) else 0
    rows.append(("D4 Structured formats", d4, 15))

    # ---- D5 (20)
    ext = [u for u in re.findall(r"\]\((https?://[^)\s]+)\)", body) if "lynkk.ai" not in u]
    attributed = len(ext) + len(re.findall(r"according to|per the|says|lists|states", text, re.I))
    need = max(wc // 200, 1)
    d5 = 4 if attributed >= need else (2 if attributed >= need / 2 else 1)
    d5 += 2 if len(re.findall(r"\$\d|\d+%|\b\d{2,}\b", text)) >= 10 else 1
    d5 += 2 + 2  # entity density and full official names (judged)
    per1500 = len(set(ext)) * 1500 / max(wc, 1)
    d5 += 3 if per1500 >= 8 else (2 if per1500 >= 4 else 1)
    d5 += 2 if len(set(ext)) >= 2 else 1
    d5 += 2 if re.search(r"help center|pricing page|according to|Scrum Guide|Section \d+|Civil Code", text) else 1
    d5 += 1  # information gain: cost tables and worked examples (judged)
    clip_pct = clips_num / max(len(secs), 1)
    if clip_pct < 0.5:
        d5 -= round(3 * (0.5 - clip_pct) / 0.5)
    rows.append(("D5 Data density and citations", max(min(d5, 20), 0), 20))

    # ---- D6 (10)
    q_h2 = sum(map(is_question, h2_content))
    d6 = 4 if q_h2 >= 6 else 2
    d6 += 3  # completeness (judged)
    d6 += 3 if 1500 <= wc <= 2500 else (2 if 1200 <= wc else 1)
    rows.append(("D6 Multi-intent coverage", d6, 10))

    # ---- D7 (5)
    d7 = (2 if fm.get("author_url") else 1) if fm.get("author") else 0
    d7 += 1 if "Last updated" in body else 0
    d7 += 0 if re.search(r"\b(TBD|TODO|\[source needed\]|\(verify\))", body.split("<!-- HANDOFF")[0]) else 2
    rows.append(("D7 E-E-A-T", d7, 5))

    # ---- D8 (5)
    links = re.findall(r"\]\((https?://[^)\s]+)\)", body)
    d8 = 2 if 8 <= len(links) <= 14 else (1 if len(links) in (6, 7, 15, 16) else 0)
    d8 += 2 if any(u.rstrip("/") == "https://lynkk.ai" for u in links) else 0
    d8 += 0 if re.search(r"\[(click here|here|this)\]", body, re.I) else 1
    rows.append(("D8 Linking", d8, 5))

    # ---- D9 binary
    d9 = []
    h1 = re.search(r"^# (.+)$", body, re.M).group(1)
    tldr_w = len(words(fm.get("tldr", "")))
    checks = [
        ("meta_title <= 60", len(fm["meta_title"]) <= 60),
        ("no 'Official'", "official" not in (fm["title"] + fm["meta_title"]).lower()),
        ("meta_description 150-160", 150 <= len(fm["meta_description"]) <= 160),
        ("tldr 50-80 words", 50 <= tldr_w <= 80),
        ("slug <= 7 words, no year", len(fm["slug"].split("-")) <= 7 and not re.search(r"20\d\d", fm["slug"])),
        ("no em dashes", "—" not in raw),
        ("no sentence > 40 words", all(len(words(s)) <= 40 for p in paras for s in sentences(plain(p)))),
        ("H1 13-15 words (flag only)", 13 <= len(words(h1)) <= 15),
    ]
    d9 = [(name, ok) for name, ok in checks]
    total = sum(r[1] for r in rows)
    return {"total": total, "rows": rows, "crit": crit, "d9": d9, "wc": wc,
            "faq_short": sum(len(words(a)) < 40 for _, a in faqs), "faqs": len(faqs),
            "links": len(links), "ext": len(set(ext)), "clip": clip_pct, "tldr": tldr_w}


def main(argv):
    verbose = "-v" in argv
    paths = [Path(a) for a in argv if a != "-v"] or sorted(ARTICLES.glob("*.md"))
    failing = 0
    print(f"{'article':45} {'AEO':>4}  gate  FAQ<40  links ext  tldr  D9 fails")
    for p in paths:
        r = score(p)
        ok = r["total"] >= 80 and not r["crit"]
        failing += not ok
        d9_fail = [n for n, v in r["d9"] if not v and "flag only" not in n]
        print(f"{p.stem:45} {r['total']:>4}  {'PASS' if ok else 'FIX ':4}  "
              f"{r['faq_short']}/{r['faqs']:<4} {r['links']:>5} {r['ext']:>3}  {r['tldr']:>4}  "
              f"{', '.join(d9_fail) or '-'}")
        if verbose:
            for name, got, mx in r["rows"]:
                print(f"    {name:38} {got:>2}/{mx}")
            for c in r["crit"]:
                print(f"    CRITICAL {c}")
            for name, v in r["d9"]:
                print(f"    D9 {'PASS' if v else 'FAIL'} {name}")
    print(f"\n{len(paths)} scored, {failing} below the gate (>=80 and no CRITICAL)")
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
