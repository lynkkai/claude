#!/usr/bin/env python3
"""G3 helper for /seo-score: word count of the top-3 comparable organic pages per keyword.

Reads research/serp_top3.tsv (slug, url1, url2, url3), fetches each page, strips
scripts, styles, nav and footer, counts visible words, and compares the median
with our article. Pages that fail to fetch or render client-side (< 200 words)
are reported and left out of the median rather than counted as thin.
"""
import re
import statistics
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from aeo_score import plain, words  # noqa: E402

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/128 Safari/537.36"


def page_words(url):
    try:
        html = subprocess.run(
            ["curl", "-sL", "-m", "25", "-A", UA, "-H", "Accept: text/html", url],
            capture_output=True, timeout=40).stdout.decode("utf-8", "ignore")
    except Exception:
        return None
    if url.endswith(".pdf"):
        return None
    html = re.sub(r"(?is)<(script|style|noscript|nav|footer|header|svg|aside|form)[^>]*>.*?</\1>", " ", html)
    # Count the article body, not menus, related posts and CTAs, when the page marks it up.
    bodies = re.findall(r"(?is)<(?:article|main)[^>]*>(.*?)</(?:article|main)>", html)
    if bodies:
        html = max(bodies, key=len)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    text = re.sub(r"&\w+;", " ", text)
    n = len(re.findall(r"[A-Za-z]{2,}", text))
    return n if n >= 200 else None


def main():
    rows = [l.split("\t") for l in (ROOT / "research/serp_top3.tsv").read_text().splitlines() if l]
    urls = sorted({u.strip() for r in rows for u in r[1:]})
    with ThreadPoolExecutor(12) as ex:
        counts = dict(zip(urls, ex.map(page_words, urls)))
    print(f"{'article':42} {'ours':>5} {'SERP median':>11} {'ratio':>6}  G3")
    fails = 0
    for slug, *us in rows:
        body = (ROOT / "articles" / f"{slug}.md").read_text().split("---\n", 2)[2]
        visible = body.split("<!-- HANDOFF")[0].replace("```", "")  # templates count, like competitors' do
        ours = len(words(plain(visible)))
        got = [counts[u.strip()] for u in us if counts.get(u.strip())]
        if not got:
            print(f"{slug:42} {ours:>5} {'n/a':>11} {'':>6}  no readable pages")
            continue
        med = statistics.median(got)
        ratio = ours / med
        ok = ratio >= 0.6
        fails += not ok
        print(f"{slug:42} {ours:>5} {int(med):>11} {ratio:>6.2f}  {'PASS' if ok else 'FAIL'}  ({len(got)}/3 pages)")
    print(f"\nG3 failures: {fails}")


if __name__ == "__main__":
    main()
