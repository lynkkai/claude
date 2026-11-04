#!/usr/bin/env python3
"""Validate articles/INBOUND-LINKS.md against the live lynkk.ai pages.

For every planned inbound link it checks three things:
  1. the host sentence still appears verbatim on the source page,
  2. the proposed anchor text is not already used as a link on that page
     (the no-duplicate-anchor hard rule), and
  3. the source page does not already link the target.

Usage: python3 -I scripts/spec_check.py
Exits non-zero if any row fails, so it can gate a publish.
"""
import html
import os
import re
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inbound_spec import SPEC  # noqa: E402

UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/124 Safari/537.36')
_cache = {}


def fetch(path):
    if path in _cache:
        return _cache[path]
    url = f'https://lynkk.ai/{path}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read().decode('utf-8', 'ignore')
    except (urllib.error.HTTPError, Exception) as e:  # noqa: BLE001
        print(f'  !! could not fetch {url}: {e}')
        body = ''
    body = re.sub(r'<script.*?</script>|<style.*?</style>|<svg.*?</svg>', '', body, flags=re.S)
    _cache[path] = body
    return body


def plain(path):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', fetch(path))))


def anchors(path):
    out = []
    for m in re.finditer(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', fetch(path), flags=re.S):
        txt = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(2)))).strip()
        out.append(txt.lower())
    return out


def main():
    failed = 0
    for slug, rows in SPEC:
        for src, kind, host, anchor in rows:
            page, text, anc = fetch(src), plain(src), anchors(src)
            anchor_clean = anchor.split('  [')[0].strip().lower()
            flags = []
            if not page:
                flags.append('PAGE-UNREACHABLE')
            else:
                if kind != 'related' and re.sub(r'\s+', ' ', host) not in text:
                    flags.append('HOST-SENTENCE-NOT-FOUND')
                if kind != 'retarget' and anchor_clean in anc:
                    flags.append('ANCHOR-ALREADY-ON-PAGE')
                if f'/blog/{slug}' in page:
                    flags.append('ALREADY-LINKS-TARGET (done?)')
            failed += bool(flags)
            print(f"{'ok  ' if not flags else 'FAIL'} {slug[:30]:30} <- {src:42} "
                  f"{kind:8} {','.join(flags)}")
    print(f"\n{len([r for _, rs in SPEC for r in rs])} rows checked, {failed} need attention")
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
