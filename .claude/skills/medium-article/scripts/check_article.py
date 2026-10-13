#!/usr/bin/env python3
"""Pre-publish checks for a Lynkk Medium draft.

Usage: python3 check_article.py content/medium/NN-slug.md

The file must start with a publishing-notes table, then a line containing only
'---', then the article. Exits 1 if any check FAILs.
"""
import re
import sys

STOPWORDS = {"a", "an", "the", "to", "of", "for", "and", "in", "on", "with", "how", "what", "is", "vs"}
MISSPELLINGS = re.compile(r"\b(Lynk|Linnk|Link AI|Lynkk AI|lynk\.ai|Lynkk\.AI)\b")


def field(notes, name):
    m = re.search(r"^\|\s*" + re.escape(name) + r"[^|]*\|\s*(.+?)\s*\|\s*$", notes, re.M)
    return m.group(1) if m else None


def tokens(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower().replace("-", " ")) if w not in STOPWORDS]


def main(path):
    text = open(path, encoding="utf-8").read()
    parts = re.split(r"^---\s*$", text, maxsplit=1, flags=re.M)
    if len(parts) != 2:
        print("FAIL  no '---' line separating publishing notes from the article")
        return 1
    notes, article = parts
    results = []

    def check(ok, msg, warn=False):
        results.append(("PASS" if ok else ("WARN" if warn else "FAIL"), msg))

    dashes = [c for c in text if c in "–—"]
    check(not dashes, f"no em/en dashes (found {len(dashes)})")

    words = len(article.split())
    check(1200 <= words <= 1800, f"article length 1,200-1,800 words (is {words})", warn=True)

    kw_field = field(notes, "Primary keyword") or ""
    kw = re.sub(r"\s*\(.*$", "", kw_field).strip()
    if kw:
        head = set(tokens(" ".join(article.split()[:130])))
        missing = [t for t in tokens(kw) if t not in head]
        check(not missing, f"primary keyword '{kw}' near the top (missing: {missing or 'none'})", warn=True)
        title = next((l for l in article.splitlines() if l.startswith("# ")), "")
        tmiss = [t for t in tokens(kw) if t not in set(tokens(title))]
        check(not tmiss, f"primary keyword in title (missing: {tmiss or 'none'})", warn=True)
    else:
        check(False, "Primary keyword row found in publishing notes")

    links = len(re.findall(r"https?://(www\.)?lynkk\.ai", article))
    check(links == 1, f"exactly one lynkk.ai link in the article (found {links})")
    check("I work on Lynkk" in article, "affiliation disclosure ('I work on Lynkk') present")

    bad = MISSPELLINGS.findall(text)
    check(not bad, f"brand spelled 'Lynkk' (bad: {sorted(set(bad)) or 'none'})")

    table_rows = [l for l in article.splitlines() if re.match(r"^\s*>?\s*\|.*\|\s*$", l)]
    check(not table_rows, f"no tables in the article body (found {len(table_rows)} table lines)")

    seo_title = field(notes, "SEO title") or ""
    check(0 < len(seo_title) <= 60, f"SEO title 60 chars or less (is {len(seo_title)})")
    seo_desc = field(notes, "SEO description") or ""
    check(0 < len(seo_desc) <= 156, f"SEO description 156 chars or less (is {len(seo_desc)})")

    tags = [t for t in (field(notes, "Tags") or "").split(",") if t.strip()]
    check(len(tags) == 5, f"5 tags (found {len(tags)})", warn=True)

    # Brackets are fine inside email templates, but not in the notes table or headings.
    unfilled = [l for l in notes.splitlines() if l.startswith("|") and "[" in l]
    unfilled += [l for l in article.splitlines() if l.startswith("#") and "[" in l]
    check(not unfilled, f"no unfilled placeholders in notes or headings (found {len(unfilled)})")

    for status, msg in results:
        print(f"{status:5} {msg}")
    return 1 if any(s == "FAIL" for s, _ in results) else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
