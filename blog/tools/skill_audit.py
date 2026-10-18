#!/usr/bin/env python3
"""Audit articles against the seo-article / aeo-article skill rules the scorers do not gate.

  A1  H1 is one natural sentence of 13-15 words, carries the primary keyword, never says "Official"
  A2  8-14 unique internal (lynkk.ai) links, author page excluded
  A3  every lynkk.ai link is live (in research/live_pages.txt); no not-yet-live sibling slugs
  A4  no anchor text contains the brand name
  A5  2+ external authority links
  A6  every secondary keyword appears at least once
  A7  primary keyword density 0.5-1.5%
  A8  >= 50% of section clips (first ~200 chars) carry a number
  A9  entity definition ("X is a/an ...") in the first 100 words of the body
  A10 Quick answer, Last updated line, disclosure and byline present
  A11 6+ question-format H2s and no dead headings
  A12 handoff records prompts answered, prompt gaps and fan-out sources
  A13 Indian rupees written as ₹ (never Rs or INR)
Refresh the live-page list with --refresh (reads https://lynkk.ai/sitemap.xml).

Usage:
    python3 blog/tools/skill_audit.py [--refresh] [<file> ...] [-v]
"""
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from aeo_score import is_question, plain, words  # noqa: E402
from seo_score import has_kw, norm, nostop  # noqa: E402

LIVE = ROOT / "research/live_pages.txt"
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
DEAD_HEADINGS = re.compile(r"key considerations|what you need to know|understanding the basics|cost drivers|"
                           r"overview|introduction|final thoughts|conclusion$", re.I)


def refresh():
    xml = subprocess.run(["curl", "-sL", "-m", "40", "https://lynkk.ai/sitemap.xml"],
                         capture_output=True, text=True).stdout
    urls = sorted({u.rstrip("/") for u in re.findall(r"<loc>([^<]+)</loc>", xml)})
    if len(urls) < 20:
        sys.exit("sitemap fetch failed; live_pages.txt left unchanged")
    LIVE.write_text("\n".join(urls) + "\n")
    print(f"live_pages.txt: {len(urls)} URLs")


def audit(path, live):
    raw = path.read_text(encoding="utf-8")
    _, fmtext, full = raw.split("---\n", 2)
    fm = yaml.safe_load(fmtext)
    body, _, handoff = full.partition("<!-- HANDOFF")
    kw = fm["primary_keyword"]
    text = plain(body)
    h1 = re.search(r"^# (.+)$", body, re.M).group(1)
    h2 = [h for h in re.findall(r"^## (.+)$", body, re.M) if not re.match(r"FAQ|Frequently", h)]
    links = LINK.findall(body)
    internal = {u.rstrip("/") for _, u in links if "lynkk.ai" in u and "/authors/" not in u}
    external = {u for _, u in links if "lynkk.ai" not in u}
    wc = len(words(text))
    occ = max(norm(text).count(norm(kw)), nostop(text).count(nostop(kw)))
    dens = 100 * occ / max(wc, 1)
    secs = re.split(r"^#{2,3} .+$", body, flags=re.M)[1:]
    clips = [plain(s).strip()[:200] for s in secs if plain(s).strip()]
    clip_pct = 100 * sum(bool(re.search(r"\d", c)) for c in clips) / max(len(clips), 1)
    intro = plain(body.split("*Disclosure")[-1] if "*Disclosure" in body else body)
    first100 = " ".join(words(intro)[:110])
    h1_words = len(words(h1))
    kw_words = {w.rstrip("s") for w in nostop(kw).split()}
    a = {
        "A1 H1 13-15 word sentence": [] if 13 <= h1_words <= 15 and "official" not in h1.lower()
        and kw_words <= {w.rstrip("s") for w in nostop(h1).split()} else [f"{h1_words} words: {h1}"],
        "A2 8-14 internal links": [] if 8 <= len(internal) <= 14 else [f"{len(internal)} unique"],
        "A3 internal links live": sorted(u.replace("https://lynkk.ai", "") for u in internal if u not in live),
        "A4 no brand in anchors": [t for t, u in links if "lynkk" in t.lower() and "/authors/" not in u
                                   and u.rstrip("/") not in ("https://lynkk.ai", "https://lynkk.ai/pricing",
                                                              "https://lynkk.ai/sign-up")],
        "A5 2+ external links": [] if len(external) >= 2 else [f"{len(external)} external"],
        "A6 secondary keywords": [s for s in fm.get("secondary_keywords", []) if not has_kw(text, s)],
        "A7 density 0.5-1.5%": [] if 0.5 <= dens <= 1.5 else [f"{dens:.2f}% ({occ} uses)"],
        "A8 clips with number >= 50%": [] if clip_pct >= 50 else [f"{clip_pct:.0f}%"],
        "A9 definition in first 100 words": [] if re.search(r"\b(is|are) (a|an|the)\b", first100) else ["none"],
        "A10 quick answer, date, disclosure, byline": [n for n, ok in (
            ("quick answer", "**Quick answer:**" in body), ("last updated", "Last updated" in body),
            ("disclosure", "Disclosure" in body), ("byline", "/blog/authors/" in body)) if not ok],
        "A11 6+ question H2s, no dead headings": ([f"{sum(map(is_question, h2))} question H2s"]
                                                  if sum(map(is_question, h2)) < 6 else [])
        + [h for h in h2 if DEAD_HEADINGS.search(h)],
        "A12 handoff complete": [n for n in ("Prompts answered", "Prompt gaps", "Fan-out source")
                                 if n.lower() not in handoff.lower()],
        "A13 rupee symbol": re.findall(r"\bRs\.? ?\d|\bINR\b", body),
    }
    return a


def main(argv):
    if "--refresh" in argv:
        refresh()
        argv = [a for a in argv if a != "--refresh"]
    live = {l.strip().rstrip("/") for l in LIVE.read_text().splitlines() if l.strip()}
    verbose = "-v" in argv
    paths = [Path(a) for a in argv if a != "-v"] or sorted((ROOT / "articles").glob("*.md"))
    bad = 0
    for p in paths:
        a = audit(p, live)
        fails = [k for k, v in a.items() if v]
        bad += bool(fails)
        print(f"{p.stem:42} {'PASS' if not fails else 'FAIL: ' + ' '.join(k.split()[0] for k in fails)}")
        for k, v in a.items():
            if v or verbose:
                print(f"    {'FAIL' if v else 'PASS'} {k}" + (f": {v[:6]}" if v else ""))
    print(f"\n{len(paths)} audited, {bad} with skill-rule failures")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
