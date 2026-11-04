#!/usr/bin/env python3
"""Rebuild the ---SCHEMA--- and ---FAQ_JSON--- blocks from the article body so the
visible FAQ, the FAQPage JSON-LD and the Article JSON-LD stay word-for-word in sync."""
import json, re, sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
s = re.split(r'\n---SCHEMA---', s)[0].rstrip() + '\n'
fm = dict(re.findall(r'^([a-z_]+): "(.*)"$', s.split('\n---\n', 1)[0], re.M))
body = s.split('\n---\n', 1)[1].split('---CITATIONS---')[0]
faq = body.split('\n## FAQ\n', 1)[1].split('\n## ', 1)[0]
pairs = re.findall(r'^### (.+?)\n\n(.+?)(?=\n\n### |\n*\Z)', faq.strip() + '\n', re.S | re.M)
clean = lambda t: re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t.strip())
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q.strip(),
     "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in pairs]}
url = fm['canonical']
article = {"@context": "https://schema.org", "@type": "Article", "headline": fm['title'],
           "description": fm['meta_description'], "inLanguage": "en",
           "author": {"@type": "Person", "name": fm['author'], "url": fm['author_url']},
           "publisher": {"@type": "Organization", "name": "Lynkk", "url": "https://lynkk.ai/"},
           "datePublished": fm['generated_date'], "dateModified": fm['generated_date'],
           "mainEntityOfPage": url}
crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://lynkk.ai/"},
    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://lynkk.ai/blog"},
    {"@type": "ListItem", "position": 3, "name": fm['title'], "item": url}]}
s += ('\n---SCHEMA---\n```json\n' + json.dumps([article, crumbs], indent=2, ensure_ascii=False) +
      '\n```\n\n---FAQ_JSON---\n```json\n' + json.dumps(faq_ld, indent=2, ensure_ascii=False) + '\n```\n')
open(p, 'w', encoding='utf-8').write(s)
print(f'{len(pairs)} FAQ pairs synced')
