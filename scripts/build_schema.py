"""Generate (or regenerate) the JSON-LD schema block for a Lynkk article from its
frontmatter and FAQ section, so the FAQ schema always matches the body word for word.

Usage: python3 scripts/build_schema.py articles/<slug>.md
Adds Article, FAQPage and BreadcrumbList (plus ItemList if the frontmatter has `itemlist:`).
"""
import json
import re
import sys


def build(path):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r'\n?<script type="application/ld\+json">.*?</script>\n?', "\n", s, flags=re.S)
    fm = s.split("---\n", 2)[1]
    body = re.sub(r"<!-- WRITER-NOTES:START -->.*?<!-- WRITER-NOTES:END -->", "", s.split("---\n", 2)[2], flags=re.S)

    def field(k):
        m = re.search(rf'^{k}: "?(.*?)"?\s*(#.*)?$', fm, re.M)
        return m.group(1).strip() if m else ""

    slug = field("slug")
    url = f"https://lynkk.ai/blog/{slug}"
    h1 = re.search(r"^# (.*)$", body, re.M).group(1)
    faq = body.split("## FAQ")[1].split("\n## ")[0]
    pairs = re.findall(r"### (.*?)\n(.*?)(?=\n### |\Z)", faq, re.S)
    graph = [
        {"@type": "Article", "headline": h1, "description": field("meta_description"),
         "inLanguage": "en-US", "datePublished": field("last_updated"),
         "dateModified": field("last_updated"),
         "author": ({"@type": "Person", "name": field("author"), **({"url": field("author_bio_url")} if field("author_bio_url") else {})}
                    if field("author") else {"@type": "Organization", "name": "Lynkk", "url": "https://lynkk.ai/"}),
         "publisher": {"@type": "Organization", "name": "Lynkk", "url": "https://lynkk.ai/"},
         "mainEntityOfPage": url},
    ]
    items = re.search(r"^itemlist: \[(.*)\]", fm, re.M)
    if items:
        names = [n.strip().strip('"') for n in items.group(1).split(",")]
        graph.append({"@type": "ItemList", "name": h1, "itemListElement": [
            {"@type": "ListItem", "position": i, "name": n} for i, n in enumerate(names, 1)]})
    graph.append({"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q.strip(),
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\s*\[CONFIRM.*?\]", "", a.strip())}}
        for q, a in pairs]})
    graph.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://lynkk.ai/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://lynkk.ai/blog"},
        {"@type": "ListItem", "position": 3, "name": h1, "item": url}]})
    block = '<script type="application/ld+json">\n' + json.dumps(
        {"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False) + "\n</script>\n"
    marker = "\n---\n\n## Handoff note"
    s = s.replace(marker, "\n" + block + marker, 1) if marker in s else s.rstrip() + "\n\n" + block
    open(path, "w", encoding="utf-8").write(s)
    print(f"schema built for {path}: {len(pairs)} FAQs")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        build(p)
