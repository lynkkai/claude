#!/usr/bin/env python3
"""Apply exact-match (old, new) edits to an article body (everything before ---SCHEMA---),
asserting each old string occurs exactly once. Usage: apply_edits.py <article> <edits.json>"""
import json, sys
p, ep = sys.argv[1], sys.argv[2]
s = open(p, encoding='utf-8').read()
head, sep, tail = s.partition('\n---SCHEMA---')
for a, b in json.load(open(ep, encoding='utf-8')):
    n = head.count(a)
    if n != 1:
        sys.exit(f'FAIL ({n} matches): {a[:80]}')
    head = head.replace(a, b)
open(p, 'w', encoding='utf-8').write(head + sep + tail)
print('edits applied')
