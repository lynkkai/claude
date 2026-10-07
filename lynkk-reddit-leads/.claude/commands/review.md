---
description: Review waiting Reddit items and export (no new search)
---

Do not fetch from Reddit. Follow steps 3 to 5 of "Run today's leads" in
CLAUDE.md: run `uv run leads review next`, classify every item in
work/batch.json per docs/CLASSIFY.md into work/batch.results.jsonl, run
`uv run leads review apply`, and repeat until nothing is waiting. Then run
`uv run leads export` and summarise: new items, relevant items, the top five
opportunities (intent, one-line pain point, URL) and where the files are.
