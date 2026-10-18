#!/usr/bin/env python3
"""Pre-score self-check for Lynkk blog articles.

Mirrors the mechanical parts of /seo-score and the seo-article skill so a draft
can be fixed before it is scored: meta lengths, keyword placement and density,
question-format H2s, FAQ presence, link counts, the ~200-character clip rule,
sentence and paragraph length, and the repo writing rules (no em or en dashes,
brand spelled "Lynkk").

Usage:
    python3 blog/tools/check_articles.py                 # every article
    python3 blog/tools/check_articles.py blog/articles/granola-pricing.md
Exit code is 1 if any article has a FAIL.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "articles"

REQUIRED = [
    "title", "meta_title", "meta_description", "slug", "primary_keyword",
    "secondary_keywords", "market", "cluster", "internal_link_target",
    "inbound_links", "tldr", "author", "last_updated", "featured_image_alt",
]
QUESTION_START = re.compile(
    r"^(how|what|which|why|when|where|who|is|are|can|does|do|should|will|"
    r"was|were|did)\b", re.I)
STOP = {"a", "an", "the", "for", "of", "to", "in", "on", "and", "vs", "with"}  # matching is stopword-insensitive


def norm(text):
    """Lowercase and treat dots and hyphens as spaces (hyphen-insensitive)."""
    text = text.lower().replace(".", " ").replace("-", " ")
    return re.sub(r"\s+", " ", text)


def nostop(text):
    """Drop stopwords so "record google meet call" matches "record a Google Meet call"."""
    return " ".join(t for t in norm(text).split() if t not in STOP)


def split(path):
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError("missing frontmatter")
    _, fm, body = raw.split("---\n", 2)
    return raw, yaml.safe_load(fm), body


def strip_md(text):
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`>#|]", " ", text)
    return text


def words(text):
    return re.findall(r"[A-Za-z0-9ऀ-ॿ][\w'ऀ-ॿ%$.,]*", text)


def check(path):
    fails, warns, info = [], [], []
    raw, fm, body = split(path)
    for key in REQUIRED:
        if key not in fm or fm[key] in (None, "", []):
            fails.append(f"frontmatter missing '{key}'")
    kw = norm(fm.get("primary_keyword", ""))

    # Writing rules
    for ch, name in (("—", "em dash"), ("–", "en dash")):
        n = raw.count(ch)
        if n:
            fails.append(f"{n} {name}(es) found")
    if re.search(r"\bLynk\b|\bLinnk\b|\bLink AI\b", raw):
        fails.append("brand misspelled (must be 'Lynkk')")

    # Meta
    mt = fm.get("meta_title", "")
    if len(mt) > 60:
        fails.append(f"meta_title {len(mt)} chars (max 60)")
    if kw and kw not in norm(mt[:50]) and not all(
            t in norm(mt[:50]) for t in kw.split() if t not in STOP):
        warns.append("primary keyword not in first 50 chars of meta_title")
    md = fm.get("meta_description", "")
    if not 150 <= len(md) <= 160:
        warns.append(f"meta_description {len(md)} chars (target 150-160)")
    if kw and not all(t in norm(md) for t in kw.split() if t not in STOP):
        warns.append("primary keyword terms not all in meta_description")
    slug = fm.get("slug", "")
    if len(slug.split("-")) > 7:
        fails.append("slug longer than 7 words")
    if re.search(r"20\d\d", slug):
        fails.append("slug contains a year (keep it evergreen)")
    if slug and slug != path.stem:
        fails.append(f"slug '{slug}' does not match filename")

    # Body structure
    plain_body = strip_md(body)
    wc = len(words(plain_body))
    info.append(f"{wc} words")
    h1 = re.findall(r"^# (.+)$", body, re.M)
    h2 = re.findall(r"^## (.+)$", body, re.M)
    if len(h1) != 1:
        fails.append(f"{len(h1)} H1 headings (need exactly 1)")
    question_h2 = [h for h in h2 if h.strip().endswith("?") or QUESTION_START.match(h)]
    info.append(f"{len(h2)} H2s, {len(question_h2)} question-format")
    if len(question_h2) < 6:
        fails.append(f"only {len(question_h2)} question-format H2s (need 6+)")
    if kw and not any(all(t in norm(h) for t in kw.split() if t not in STOP) for h in h2):
        warns.append("primary keyword not in any H2")
    after_h1 = body.split("\n", 1)[1] if h1 else body
    first100 = " ".join(words(strip_md(after_h1))[:100])
    if kw and kw not in norm(first100) and nostop(kw) not in nostop(first100):
        fails.append("primary keyword not in first 100 words")
    occurrences = max(norm(plain_body).count(kw),
                      nostop(plain_body).count(nostop(kw))) if kw else 0
    density = 100 * occurrences / max(wc, 1)
    info.append(f"keyword x{occurrences} ({density:.2f}%)")
    if density > 1.5:
        warns.append(f"keyword density {density:.2f}% above 1.5%")
    elif density < 0.5 and len(kw.split()) <= 3:
        warns.append(f"keyword density {density:.2f}% below 0.5%")
    if "Quick answer" not in body:
        fails.append("no 'Quick answer' callout")
    if not re.search(r"^## (FAQ|Frequently asked questions)", body, re.M | re.I):
        fails.append("no FAQ section")
    else:
        faq = re.split(r"^## (?:FAQ|Frequently asked questions).*$", body,
                       flags=re.M | re.I)[1]
        faq = re.split(r"^## ", faq, flags=re.M)[0]
        n_q = len(re.findall(r"^### .+\?\s*$", faq, re.M))
        if n_q < 4:
            fails.append(f"FAQ has {n_q} questions (need 4+)")

    # Links
    links = re.findall(r"\]\((https?://[^)\s]+)\)", body)
    internal = [u for u in links if "lynkk.ai" in u]
    external = [u for u in links if "lynkk.ai" not in u]
    info.append(f"{len(internal)} internal / {len(external)} external links")
    if len({u for u in internal if "/blog/" in u}) < 2:
        warns.append("fewer than 2 sibling /blog/ cross-links")
    if len(external) < 2:
        warns.append("fewer than 2 external authority links")
    if len(fm.get("inbound_links") or []) < 1:
        fails.append("no inbound internal links planned")

    # Clip rule: first ~200 chars under each H2 should carry a number
    sections = re.split(r"^## .+$", body, flags=re.M)[1:]
    with_num = 0
    for sec in sections:
        clip = strip_md(sec).strip()[:200]
        if re.search(r"\d", clip):
            with_num += 1
    if sections:
        pct = 100 * with_num / len(sections)
        info.append(f"clip-with-number {pct:.0f}%")
        if pct < 50:
            warns.append(f"only {pct:.0f}% of section clips carry a number (target 50%+)")

    # Readability
    paras = [p for p in re.split(r"\n\s*\n", body)
             if p.strip() and not p.lstrip().startswith(("#", "|", "-", "*", "<", ">", "1."))]
    long_paras = [p for p in paras if len(words(strip_md(p))) > 100]
    if long_paras:
        warns.append(f"{len(long_paras)} paragraph(s) over 100 words")
    sentences = re.split(r"(?<=[.!?])\s+", " ".join(strip_md(p) for p in paras))
    long_sent = [s for s in sentences if len(words(s)) > 40]
    if long_sent:
        warns.append(f"{len(long_sent)} sentence(s) over 40 words")

    return fails, warns, info


def main(argv):
    paths = [Path(p) for p in argv] or sorted(ARTICLES.glob("*.md"))
    bad = 0
    for path in paths:
        try:
            fails, warns, info = check(path)
        except Exception as exc:  # report and keep going
            fails, warns, info = [f"could not parse: {exc}"], [], []
        status = "FAIL" if fails else ("WARN" if warns else "PASS")
        bad += bool(fails)
        print(f"[{status}] {path.name}: {', '.join(info)}")
        for msg in fails:
            print(f"    FAIL  {msg}")
        for msg in warns:
            print(f"    warn  {msg}")
    print(f"\n{len(paths)} checked, {bad} with failures")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
