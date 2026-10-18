#!/usr/bin/env python3
"""Print an article's prose paragraphs with index and sentence lengths (rewrite helper)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aeo_score import body_paragraphs, plain, sentences, words  # noqa: E402

for f in sys.argv[1:]:
    body = Path(f).read_text().split("---\n", 2)[-1]
    body = body.split("<!-- HANDOFF")[0]  # FAQ answers included; schema is rebuilt from them
    for i, p in enumerate(body_paragraphs(body)):
        if p.startswith("*By ") or p.startswith("*Disclosure") or p.startswith("**More on Lynkk"):
            continue
        ss = sentences(plain(p))
        lens = [len(words(s)) for s in ss]
        heads = [words(s)[0] for s in ss if words(s)]
        print(f"[{i}] {lens} {heads}\n{p}\n")
