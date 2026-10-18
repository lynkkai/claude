#!/usr/bin/env python3
"""Re-check every competitor price quoted in the blog against the vendor's pricing page.

Reads research/prices.yaml. For each vendor, fetches the source page and confirms each
expected figure still appears. A missing figure means the price may have changed: re-verify
by hand and update both prices.yaml and every article listed under `used_in`.
Pages that render prices with JavaScript return little text; those are reported as
"check by hand" rather than as changes.

Usage:
    python3 blog/tools/price_check.py            # all vendors
    python3 blog/tools/price_check.py otter read-ai
"""
import html
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/128 Safari/537.36"


def page_text(url):
    raw = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, url],
                         capture_output=True).stdout.decode("utf-8", "ignore")
    raw = re.sub(r"(?is)<(style|svg)[^>]*>.*?</\1>", " ", raw)
    text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", raw))
    return re.sub(r"(\d)\s+\.(\d)", r"\1.\2", text)  # "$16 .99" when markup splits the cents


def main(only):
    data = yaml.safe_load((ROOT / "research/prices.yaml").read_text())
    changed = 0
    print(f"Price check {date.today()}\n")
    for vendor, spec in data.items():
        if only and vendor not in only:
            continue
        text = page_text(spec["source"])
        if len(text.split()) < 150:
            print(f"[MANUAL ] {vendor:10} page rendered client-side; open {spec['source']}")
            continue
        missing = [e for e in spec["expect"] if not re.search(rf"(?<![\d.]){re.escape(e)}(?![\d])", text)]
        if missing:
            changed += 1
            print(f"[CHANGED?] {vendor:10} not found on page: {', '.join(missing)}")
            print(f"           re-verify {spec['source']} and update: {', '.join(spec['used_in'])}")
        else:
            print(f"[OK     ] {vendor:10} all {len(spec['expect'])} figures still on {spec['source']}")
        if spec.get("note"):
            print(f"           note: {spec['note']}")
    print(f"\n{changed} vendor(s) need a manual re-check")
    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
