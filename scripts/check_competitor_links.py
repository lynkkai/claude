"""Guardrail: fail if a Lynkk article links to a competitor site.
Usage: python3 scripts/check_competitor_links.py articles/*.md
"""
import re, sys

COMPETITORS = [
    "otter.ai", "fireflies.ai", "fathom.ai", "fathom.video", "granola.ai",
    "meetjamie.ai", "read.ai", "plaud.ai", "heypocket.com", "tldv.io",
    "krisp.ai", "tactiq.io", "notta.ai", "gong.io", "avoma.com", "fellow.app",
    "meetgeek.ai", "bluedothq.com", "zoom.com", "zoom.us", "microsoft.com",
    "workspace.google.com", "gemini.google.com", "riverside.fm", "descript.com",
    "rev.com", "sonix.ai", "chorus.ai", "salesloft.com", "nuance.com",
]
URL = re.compile(r"https?://[^\s)\"'>\]]+", re.I)

failed = False
for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    for n, line in enumerate(text.splitlines(), 1):
        for url in URL.findall(line):
            host = re.sub(r"^https?://", "", url.lower()).split("/")[0]
            if any(host == c or host.endswith("." + c) for c in COMPETITORS):
                print(f"FAIL {path}:{n} competitor link: {url}")
                failed = True
print("FAIL: competitor links found" if failed else "PASS: no competitor links")
sys.exit(1 if failed else 0)
