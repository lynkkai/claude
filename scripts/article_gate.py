#!/usr/bin/env python3
"""Offline article gate for the Unveilr content pipeline.

Stands in for pre_score.py, clip_check.py, link_liveness.py and humanize_verify.py,
which are not installed on this machine. It measures the countable parts of
/aeo-score, /seo-score, /post-humanize-check and /humanize-verify. Qualitative
judgment (answer quality, info gain, positioning) stays with the reviewer.

Usage:
  python3 scripts/article_gate.py articles/<slug>.md                 # Gate A metrics
  python3 scripts/article_gate.py articles/<slug>.md --live          # + link liveness
  python3 scripts/article_gate.py articles/<slug>.md --original articles/<slug>.md.original
                                                                     # Gate B + humanize-verify delta
"""
import argparse
import re
import statistics
import sys
import urllib.error
import urllib.request

BANNED = ['crucial', 'comprehensive', 'delve', 'leverage', 'robust', 'seamless', 'moreover',
          'furthermore', 'additionally', 'underscores', 'multifaceted', 'exquisite',
          'mesmerising', 'enchanting', 'captivating', 'breathtaking', 'intricate',
          'landscape', 'navigate', 'navigating', 'elevate', 'unlock', 'empower',
          'game-changer', 'in today\'s', 'ever-evolving', 'tapestry', 'testament', 'pivotal']
DEAD = ['key considerations', 'understanding the basics', 'what you need to know',
        'cost drivers', 'overview', 'introduction', 'final thoughts']
THROAT = ['in this article', 'you have come to the right place', 'when it comes to',
          'choosing the right', 'understanding ', 'tired of', 'in today']
DRAFT_ARTIFACTS = [r'\(industry estimate\)', r'\(approx\.?\)', r'\(TBD\)', r'\bTODO\b',
                   r'\[source needed\]', r'\(verify\)', r'\(unverified\)', r'\bXX\b', r'\bTK\b']
SPELLED = r'\b(one|two|three|four|five|six|seven|eight|nine|ten|dozen|hundred)\b'
NUM = re.compile(r'\d|' + SPELLED, re.I)
NON_QUESTION_OK = ['faq', 'conclusion', 'at a glance', 'quick answer']


def split(text):
    fm, body = {}, text
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if m:
        fm_raw, body = m.group(1), text[m.end():]
        key = None
        for line in fm_raw.splitlines():
            km = re.match(r'^([a-z_]+):\s*(.*)$', line)
            if km:
                key, val = km.group(1), km.group(2).strip().strip('"')
                fm[key] = val if val else []
            elif line.strip().startswith('- ') and key:
                if not isinstance(fm[key], list):
                    fm[key] = []
                fm[key].append(line.strip()[2:].strip().strip('"'))
    citations = ''
    if '---CITATIONS---' in body:
        body, citations = body.split('---CITATIONS---', 1)
    return fm, body, citations


def words(s):
    return re.findall(r"[A-Za-z0-9$%][A-Za-z0-9$%,.'\-/]*", s)


def strip_md(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    return re.sub(r'[*_`>#|]', ' ', s)


def sentences(s):
    s = strip_md(s)
    s = re.sub(r'\b(e\.g|i\.e|vs|No|Mr|Dr|etc)\.', r'\1', s)
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z"(0-9])', s.strip())
    return [p for p in parts if len(words(p)) > 0]


def blocks(body):
    """Yield (kind, text) where kind is heading/para/list/table/quote."""
    out = []
    for chunk in re.split(r'\n\s*\n', body.strip()):
        c = chunk.strip()
        if not c:
            continue
        if c.startswith('#'):
            for line in c.splitlines():
                if line.startswith('#'):
                    out.append(('heading', line))
                else:
                    out.append(('para', line))
        elif c.startswith('|'):
            out.append(('table', c))
        elif re.match(r'^(\d+\.|-)\s', c):
            out.append(('list', c))
        elif c.startswith('>'):
            out.append(('quote', c))
        else:
            out.append(('para', c))
    return out


def sections(body):
    """List of (level, heading, text_after_heading_until_next_heading_of_any_level)."""
    res, cur = [], None
    for line in body.splitlines():
        m = re.match(r'^(#{1,3})\s+(.*)$', line)
        if m:
            if cur:
                res.append(cur)
            cur = [len(m.group(1)), m.group(2).strip(), []]
        elif cur:
            cur[2].append(line)
    if cur:
        res.append(cur)
    return [(lvl, h, '\n'.join(t).strip()) for lvl, h, t in res]


def first_prose(text):
    for kind, b in blocks(text):
        if kind in ('para', 'quote', 'list'):
            return strip_md(b).strip()
    return ''


def h2_sections(body):
    res, cur = [], None
    for line in body.splitlines():
        if line.startswith('## '):
            if cur:
                res.append(cur)
            cur = [line[3:].strip(), [], False]
        elif cur:
            if line.startswith('### '):
                cur[2] = True
            cur[1].append(line)
    if cur:
        res.append(cur)
    return [(h, '\n'.join(t), has_h3) for h, t, has_h3 in res]


def prose_metrics(body):
    sents, paras = [], []
    for kind, b in blocks(body):
        if kind == 'para':
            paras.append(b)
            sents.extend(sentences(b))
        elif kind == 'list':
            for item in b.splitlines():
                sents.extend(sentences(re.sub(r'^(\d+\.|-)\s+', '', item)))
    lens = [len(words(s)) for s in sents]
    plens = [len(words(strip_md(p))) for p in paras]
    openers = [' '.join(words(s.lower())[:2]) for s in sents if len(words(s)) >= 2]
    rep = 1 - len(set(openers)) / len(openers) if openers else 0
    toks = [w.lower() for w in words(strip_md(body))]
    sample = toks[:1500]
    ttr = len(set(sample)) / len(sample) if sample else 0
    mean = statistics.mean(lens) if lens else 0
    sd = statistics.pstdev(lens) if lens else 0
    return {
        'sentences': len(lens), 'mean_len': round(mean, 1), 'stdev_len': round(sd, 2),
        'burstiness_cv': round(sd / mean, 3) if mean else 0,
        'para_stdev': round(statistics.pstdev(plens), 2) if plens else 0,
        'opener_repeat': round(rep, 3), 'ttr_1500': round(ttr, 3),
        'over_40': [s for s in sents if len(words(s)) > 40],
        'over_22_share': round(sum(1 for l in lens if l > 22) / len(lens), 3) if lens else 0,
    }


def check_links(urls):
    res = {}
    ua = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
          '(KHTML, like Gecko) Chrome/124 Safari/537.36')
    for u in sorted(set(urls)):
        try:
            req = urllib.request.Request(u, headers={'User-Agent': ua})
            with urllib.request.urlopen(req, timeout=25) as r:
                final = r.geturl()
                code = r.status
        except urllib.error.HTTPError as e:
            code, final = e.code, u
        except Exception as e:  # DNS, timeout
            code, final = f'ERR {type(e).__name__}', u
        gov = re.search(r'\.gov(\.[a-z]{2})?/', u) is not None
        live = code == 200 or (code == 403 and gov)
        soft404 = live and final.rstrip('/') in ('https://lynkk.ai', 'http://lynkk.ai') \
            and u.rstrip('/') != 'https://lynkk.ai'
        res[u] = (code, 'LIVE' if live and not soft404 else ('SOFT-404' if soft404 else 'DEAD'))
    return res


def gate_a(path, live):
    text = open(path, encoding='utf-8').read()
    fm, body, cites = split(text)
    rep = {}
    kws = fm.get('keywords', []) if isinstance(fm.get('keywords'), list) else []
    primary = kws[0] if kws else ''
    body_words = len(words(strip_md(body)))
    rep['word_count'] = body_words
    secs = sections(body)
    h1 = [h for l, h, _ in secs if l == 1]
    h2 = [h for l, h, _ in secs if l == 2]
    h3 = [h for l, h, _ in secs if l == 3]
    rep['h1'] = h1
    rep['h1_words'] = len(words(h1[0])) if h1 else 0
    q_h2 = [h for h in h2 if h.endswith('?')]
    counted_h2 = [h for h in h2 if not any(k in h.lower() for k in NON_QUESTION_OK)]
    rep['h2_total'] = len(h2)
    rep['h2_question'] = f"{len(q_h2)}/{len(counted_h2)} non-structural H2s are questions"
    rep['dead_headings'] = [h for h in h2 + h3 if any(d in h.lower() for d in DEAD)]
    faq_mode = False
    faq_answers, clip_rows, first_sent = {}, [], []
    for lvl, h, t in secs:
        if lvl == 2:
            faq_mode = h.lower().startswith('faq') or 'frequently asked' in h.lower()
        prose = first_prose(t)
        if lvl == 3 and faq_mode:
            faq_answers[h] = len(words(prose))
        if lvl >= 2 and prose and not h.lower().startswith(('faq', 'conclusion')):
            clip = prose[:200]
            fs = sentences(prose)[0] if sentences(prose) else ''
            clip_rows.append((h, bool(NUM.search(clip)),
                              any(t_ in clip.lower()[:60] for t_ in THROAT), clip))
            if h.endswith('?'):
                first_sent.append((h, len(words(fs))))
    qa = re.search(r'\*\*Quick answer:\*\*(.*?)(?:\n\n|$)', body, re.S)
    rep['quick_answer_words'] = len(words(strip_md(qa.group(1)))) if qa else 0
    rep['quick_answer_has_number'] = bool(qa and NUM.search(qa.group(1)[:220]))
    rep['clip_with_number'] = f"{sum(1 for r in clip_rows if r[1])}/{len(clip_rows)}"
    rep['clip_throat_clearing'] = [r[0] for r in clip_rows if r[2]]
    rep['clip_no_number'] = [(r[0], r[3]) for r in clip_rows if not r[1]]
    rep['first_sentence_over_29'] = [(h, n) for h, n in first_sent if n >= 29]
    rep['faq_answers'] = faq_answers
    # paragraphs
    paras = [b for k, b in blocks(body) if k == 'para']
    over4 = [p[:70] for p in paras if len(sentences(p)) > 4]
    over80 = [p[:70] for p in paras if len(words(strip_md(p))) > 80]
    rep['paras'] = len(paras)
    rep['paras_over_4_sentences'] = over4
    rep['paras_over_80_words'] = over80
    rep['h2_over_300_no_h3'] = [(h, len(words(strip_md(t)))) for h, t, has3 in h2_sections(body)
                                if len(words(strip_md(t))) > 300 and not has3]
    rep['h2_section_words'] = [(h[:50], len(words(strip_md(t)))) for h, t, _ in h2_sections(body)]
    # dashes / banned / artifacts
    rep['em_en_dashes_file'] = text.count('\u2014') + text.count('\u2013')
    low = strip_md(body).lower()
    rep['banned_hits'] = [w for w in BANNED if re.search(r'\b' + re.escape(w) + r'\b', low)]
    rep['draft_artifacts'] = [p for p in DRAFT_ARTIFACTS if re.search(p, body, re.I)]
    rep['official_in_title'] = 'official' in (fm.get('title', '') + fm.get('meta_title', '')).lower()
    # keywords
    norm = lambda s: re.sub(r'\s+', ' ', s.lower().replace('-', ' '))
    nb = norm(strip_md(body))
    rep['keyword_presence'] = {k: nb.count(norm(k)) for k in kws}
    pc = nb.count(norm(primary)) if primary else 0
    rep['primary_density_pct'] = round(100 * pc * len(primary.split()) / body_words, 2) if body_words else 0
    first100 = ' '.join(words(strip_md(body.split('\n# ', 1)[-1]))[:130]).lower()
    rep['primary_in_first_100'] = norm(primary) in norm(first100)
    rep['primary_in_h1'] = bool(h1) and norm(primary) in norm(h1[0])
    rep['primary_in_an_h2'] = any(norm(primary) in norm(h) for h in h2 + h3)
    rep['meta_title_len'] = len(fm.get('meta_title', ''))
    rep['meta_title_primary_in_50'] = norm(primary) in norm(fm.get('meta_title', '')[:50])
    rep['meta_description_len'] = len(fm.get('meta_description', ''))
    rep['tldr_words'] = len(words(fm.get('tldr', '')))
    slug = fm.get('slug', '')
    rep['slug'] = slug
    rep['slug_ok'] = bool(slug) and len(slug.split('-')) <= 7 and not re.search(r'\d{4}', slug)
    rep['last_updated_visible'] = bool(re.search(r'\d{1,2} \w+ 20\d\d', body[:800]))
    rep['author_url'] = bool(fm.get('author_url'))
    # links
    links = re.findall(r'\]\((https?://[^)\s]+)\)', body)
    internal = [u for u in links if 'lynkk.ai' in u]
    external = [u for u in links if 'lynkk.ai' not in u]
    rep['links_internal'] = len(set(internal))
    rep['links_external'] = len(set(external))
    rep['raw_paren_urls'] = re.findall(r'\]\([^)]*\([^)]*\)', body)
    rep['tables'] = sum(1 for k, _ in blocks(body) if k == 'table')
    rep['table_max_cols'] = max([b.splitlines()[0].count('|') - 1 for k, b in blocks(body) if k == 'table'] or [0])
    rep['lists'] = sum(1 for k, _ in blocks(body) if k == 'list')
    rep['prose'] = prose_metrics(body)
    if live:
        cite_urls = [u.rstrip('.,)"') for u in
                     re.findall(r'https?://\S+', cites.split('---SCHEMA---')[0])]
        rep['liveness'] = check_links(links + cite_urls)
    return rep, fm, body, cites


def gate_b(path, orig):
    cur = open(path, encoding='utf-8').read()
    old = open(orig, encoding='utf-8').read()
    fm_c, b_c, c_c = split(cur)
    fm_o, b_o, c_o = split(old)
    out = {}
    norm = lambda s: re.sub(r'\s+', ' ', s.lower().replace('-', ' '))
    kws = fm_o.get('keywords', [])
    out['C1_missing_keywords'] = [k for k in kws if norm(k) not in norm(strip_md(b_c))]
    h1c = [l for l in b_c.splitlines() if l.startswith('# ')]
    out['C2_primary_in_h1'] = bool(h1c) and norm(kws[0]) in norm(h1c[0])
    h2c = [l[3:] for l in b_c.splitlines() if l.startswith('## ')]
    h2o = [l[3:] for l in b_o.splitlines() if l.startswith('## ')]
    hc = [l for l in b_c.splitlines() if l.startswith('#')]
    ho = [l for l in b_o.splitlines() if l.startswith('#')]
    out['C3_question_h2'] = f"{sum(h.endswith('?') for h in h2c)}/{len(h2c)} (was {sum(h.endswith('?') for h in h2o)}/{len(h2o)})"
    out['headings_identical'] = hc == ho
    lc = set(re.findall(r'\]\((https?://[^)]+)\)', b_c))
    lo = set(re.findall(r'\]\((https?://[^)]+)\)', b_o))
    out['C4_C7_links_missing'] = sorted(lo - lc)
    out['C4_C7_links_added'] = sorted(lc - lo)
    out['C5_dashes'] = cur.count('\u2014') + cur.count('\u2013')
    out['C6_banned'] = [w for w in BANNED if re.search(r'\b' + re.escape(w) + r'\b', strip_md(b_c).lower())]
    out['C8_frontmatter_unchanged'] = fm_c == fm_o
    out['C9_citations_unchanged'] = c_c == c_o
    fig = re.compile(r'\$[\d,]+(?:\.\d+)?|\b\d[\d,]*(?:\.\d+)?%?|\bAES-256-GCM\b|\bRFC \d+\b')
    fo = sorted(set(fig.findall(strip_md(b_o))))
    fc = set(fig.findall(strip_md(b_c)))
    out['C11_numbers_missing'] = [f for f in fo if f not in fc]
    out['C11_numbers_added'] = sorted(fc - set(fo))
    out['C13_artifacts'] = [p for p in DRAFT_ARTIFACTS if re.search(p, b_c, re.I)]
    # FAQ untouched (C9 analogue: FAQ answers feed FAQPage schema)
    def faq(b):
        return b.split('## FAQ', 1)[1].split('## Conclusion', 1)[0] if '## FAQ' in b else ''
    out['C9_faq_unchanged'] = faq(b_c) == faq(b_o)
    pm_c, pm_o = prose_metrics(b_c), prose_metrics(b_o)
    out['humanize_verify'] = {k: (pm_o[k], pm_c[k]) for k in
                              ('burstiness_cv', 'stdev_len', 'mean_len', 'para_stdev',
                               'opener_repeat', 'ttr_1500', 'over_22_share')}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('article')
    ap.add_argument('--live', action='store_true')
    ap.add_argument('--original')
    a = ap.parse_args()
    rep, *_ = gate_a(a.article, a.live)
    for k, v in rep.items():
        if k == 'liveness':
            print('liveness:')
            for u, (c, s) in v.items():
                print(f'   {s:8} {c}  {u}')
        elif k == 'prose':
            for pk, pv in v.items():
                print(f'prose.{pk}: {pv}')
        else:
            print(f'{k}: {v}')
    if a.original:
        print('\n==== GATE B / HUMANIZE-VERIFY ====')
        for k, v in gate_b(a.article, a.original).items():
            print(f'{k}: {v}')


if __name__ == '__main__':
    sys.exit(main())
