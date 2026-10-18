#!/usr/bin/env python3
"""Keep links to not-yet-live sibling posts out of the articles until the target is live.

The aeo-article skill forbids shipping links to "will-be-live-soon" slugs. This tool:
  --strip    turns every lynkk.ai link whose target is not in research/live_pages.txt into plain
             anchor text and records it in review/sibling-links.tsv (article, anchor, target).
  --restore  re-links every recorded anchor whose target is now live (run skill_audit.py --refresh
             first so live_pages.txt is current), and drops it from the tsv.
  (no flag)  prints the pending links and whether each target is live yet.

Usage:
    python3 blog/tools/sibling_links.py [--strip | --restore]
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIVE = ROOT / "research/live_pages.txt"
PLAN = ROOT / "review/sibling-links.tsv"
LINK = re.compile(r"\[([^\]]+)\]\((https://lynkk\.ai/[^)\s]*)\)")


def live_set():
    return {l.strip().rstrip("/") for l in LIVE.read_text().splitlines() if l.strip()}


def load():
    if not PLAN.exists():
        return []
    with PLAN.open() as f:
        return list(csv.DictReader(f, delimiter="\t"))


def save(rows):
    with PLAN.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["article", "anchor", "target"], delimiter="\t")
        w.writeheader()
        w.writerows(rows)


def strip(live):
    rows = load()
    for p in sorted((ROOT / "articles").glob("*.md")):
        raw = p.read_text(encoding="utf-8")
        head, _, rest = raw.partition("\n---\n")
        body, sep, handoff = rest.partition("<!-- HANDOFF")

        def repl(m):
            if m.group(2).rstrip("/") in live:
                return m.group(0)
            rows.append({"article": p.stem, "anchor": m.group(1), "target": m.group(2)})
            return m.group(1)

        new = LINK.sub(repl, body)
        if new != body:
            p.write_text(head + "\n---\n" + new + sep + handoff, encoding="utf-8")
    save(rows)
    print(f"{len(rows)} pending sibling links recorded in {PLAN.relative_to(ROOT)}")


def restore(live):
    keep, done = [], 0
    for r in load():
        p = ROOT / "articles" / f"{r['article']}.md"
        raw = p.read_text(encoding="utf-8")
        head, _, rest = raw.partition("\n---\n")
        body, sep, handoff = rest.partition("<!-- HANDOFF")
        # first plain occurrence of the anchor that is not already inside a link
        m = re.search(rf"(?<!\[){re.escape(r['anchor'])}(?!\]\()", body)
        if r["target"].rstrip("/") in live and m:
            body = body[:m.start()] + f"[{r['anchor']}]({r['target']})" + body[m.end():]
            p.write_text(head + "\n---\n" + body + sep + handoff, encoding="utf-8")
            done += 1
        else:
            keep.append(r)
    save(keep)
    print(f"{done} links restored, {len(keep)} still waiting for their target to go live")


def main(argv):
    live = live_set()
    if "--strip" in argv:
        strip(live)
    elif "--restore" in argv:
        restore(live)
    else:
        for r in load():
            print(f"{'LIVE ' if r['target'].rstrip('/') in live else 'wait '} {r['article']:40} -> {r['target']}")


if __name__ == "__main__":
    main(sys.argv[1:])
