#!/usr/bin/env python3
"""Verify the inbound links in review/inbound-links.md are live on the source pages.

The seo-article skill requires every article to receive 1-2 inbound links from live pages and the
links to be verified on the source pages before the task is done. For each row of the sheet:
  WAITING  the target article is not live yet (not in research/live_pages.txt): nothing to add yet
  ADD      the target is live but the source page does not link to it yet: paste the sentence
  LINKED   the source page links to the target: the row is ticked when run with --mark
Run `python3 blog/tools/skill_audit.py --refresh` first so live_pages.txt is current.

Usage:
    python3 blog/tools/inbound_verify.py           # report
    python3 blog/tools/inbound_verify.py --mark    # also tick LINKED rows in the sheet
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from inbound_sheet import fetch  # noqa: E402

SHEET = ROOT / "review/inbound-links.md"
ROW = re.compile(r"^\| \[( |x)\] \| (/\S+) \| (.+?) \| (.+\]\((https://lynkk\.ai/blog/[a-z0-9-]+)\).+) \|$")


def main(argv):
    live = {l.strip().rstrip("/") for l in (ROOT / "research/live_pages.txt").read_text().splitlines() if l.strip()}
    lines = SHEET.read_text(encoding="utf-8").splitlines()
    pages, status = {}, Counter()
    for i, line in enumerate(lines):
        m = ROW.match(line)
        if not m:
            continue
        _, source, section, _, target = m.groups()
        if target not in live:
            state = "WAITING"
        else:
            if source not in pages:
                pages[source] = fetch("https://lynkk.ai" + source)
            path = target.replace("https://lynkk.ai", "")
            state = "LINKED" if re.search(rf'href="(?:https://lynkk\.ai)?{re.escape(path)}/?"', pages[source]) else "ADD"
        status[state] += 1
        if state != "WAITING":
            print(f"{state:7} {source:45} -> {target.replace('https://lynkk.ai', '')}  [{section}]")
        if state == "LINKED" and "--mark" in argv:
            lines[i] = line.replace("| [ ] |", "| [x] |", 1)
    if "--mark" in argv:
        SHEET.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n{status['LINKED']} linked, {status['ADD']} to add now, {status['WAITING']} waiting for the target to go live")
    return 1 if status["ADD"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
