"""Mechanical rule audit for Lynkk articles (seo-article / seo-score / aeo-score + Lynkk rules).

Usage: python3 scripts/audit_article.py articles/<slug>.md
Exit code 0 = every mechanical rule passes, 1 = at least one fails.
Items that need humans (author, tests, images, link click-tests) are not checked here.
"""
import json
import re
import subprocess
import sys

COMPETITOR_CHECK = "scripts/check_competitor_links.py"
OFFICIAL = (".gov", "uscode.house.gov", "leginfo.legislature.ca.gov", "nist.gov",
            "eur-lex.europa.eu", "europa.eu", "w3.org", "section508.gov", "ada.gov")
TELLS = ["delve", "crucial", "seamless", "robust", "moreover", "furthermore", "leverage",
         "landscape", "game-changer", "unlock", "elevate", "streamline", "in today",
         "comprehensive", "empower", "harness", "cutting-edge", "ever-evolving", "tapestry"]
DEAD = ["key considerations", "cost drivers", "understanding the basics", "what you need to know"]
STRUCTURAL = {"FAQ", "Conclusion", "Our quick picks", "Quick picks"}


def main(path):
    raw = open(path, encoding="utf-8").read()
    s = re.sub(r"<!-- WRITER-NOTES:START -->.*?<!-- WRITER-NOTES:END -->\n*", "", raw, flags=re.S)
    fails, notes = [], []
    fm = s.split("---\n", 2)[1]
    body = s.split("---\n", 2)[2].split("<script")[0]
    body = body.split("\n## Handoff note")[0]

    def field(k):
        m = re.search(rf'^{k}: "?(.*?)"?\s*(#.*)?$', fm, re.M)
        return m.group(1).strip() if m else ""

    def check(ok, msg):
        (notes if ok else fails).append(("PASS " if ok else "FAIL ") + msg)

    primary = re.search(r"^keywords:\n\s+- (.+?)\s+#", fm, re.M).group(1).strip()
    secondaries = re.findall(r"^\s+- (.+?)\s+#", fm.split("keywords:")[1].split("keywords_added:")[0], re.M)[1:]
    mt, md, slug = field("meta_title"), field("meta_description"), field("slug")
    h1 = re.search(r"^# (.*)$", body, re.M).group(1)

    check(len(mt) <= 60, f"meta_title {len(mt)} chars (<=60)")
    kpos = mt.lower().find(primary.split()[0])
    check(0 <= kpos < 50, f"meta_title contains primary near start (pos {kpos})")
    check(150 <= len(md) <= 160, f"meta_description {len(md)} chars (150-160)")
    check(primary.lower() in md.lower(), "meta_description contains primary keyword")
    check("official" not in (mt + h1).lower(), "no 'Official' in title/H1")
    check(13 <= len(h1.split()) <= 15, f"H1 {len(h1.split())} words (13-15)")
    check(not re.search(r"20\d\d", slug) and len(slug.split("-")) <= 7, f"slug '{slug}' evergreen, <=7 words")

    plain = re.sub(r"\]\([^)]*\)", "]", body)
    plain = re.sub(r"[#>*|`\[\]()]", " ", plain)
    words = plain.split()
    low = re.sub(r"(\w)\.(ai|io)\b", r"\1 \2", " ".join(words).lower()).replace("-", " ")
    template = field("template")[:1]
    minimum = {"A": 2500, "B": 1800, "C": 1200, "D": 1500}.get(template, 1500)
    check(len(words) >= minimum, f"word count {len(words)} (template {template or '?'} minimum {minimum})")
    check(primary.lower() in " ".join(words[:120]).lower(), "primary keyword in first 100 words")
    dens = 100 * low.count(primary.lower()) / len(words)
    check(0.5 <= dens <= 1.5, f"primary density {dens:.2f}% (0.5-1.5)")
    for k in secondaries:
        check(k.lower() in low, f"secondary present: {k}")

    h2 = re.findall(r"^## (.*)$", body, re.M)
    q = [h for h in h2 if h.strip().endswith("?")]
    check(len(q) >= 6, f"question H2s {len(q)} (>=6)")
    check(any(primary.lower() in h.lower().replace("-", " ") for h in h2), "primary keyword in at least one H2")
    dead = [h for h in h2 if any(d in h.lower() for d in DEAD)]
    check(not dead, f"no dead headings {dead}")

    for sec in re.split(r"^#{2,3} ", body, flags=re.M)[1:]:
        title, content = sec.split("\n", 1)
        if title.strip() in STRUCTURAL:
            continue
        c = re.sub(r"\]\([^)]*\)", "]", content)
        c = re.sub(r"^\|.*$", "", c, flags=re.M)
        clip = re.sub(r"\s+", " ", c).strip()[:200]
        check(bool(re.search(r"\d", clip)), f"200-char clip has a number: {title[:50]}")
    for sec in re.split(r"^## ", body, flags=re.M)[1:]:
        title, content = sec.split("\n", 1)
        if "### " not in content and title.strip() != "FAQ":
            n = len(content.split())
            check(n <= 300, f"section <=300 words without H3: {title[:40]} ({n})")

    paras = [p for p in re.split(r"\n\s*\n", body)
             if p.strip() and not re.match(r"\s*([#|>\-!*]|\d+\.)", p)]
    for p in paras:
        n = len(p.split())
        pp = re.sub(r"\b(U\.S\.C|U\.S|e\.g|i\.e|vs|etc|Inc|No)\.", "ABBR", p)
        sents = len(re.findall(r"[.!?](\s|$)", pp))
        if n > 80 or sents > 4:
            fails.append(f"FAIL paragraph {n} words / {sents} sentences: {p[:60]}...")

    faq = body.split("## FAQ")[1].split("\n## ")[0] if "## FAQ" in body else ""
    pairs = re.findall(r"### (.*?)\n(.*?)(?=\n### |\Z)", faq, re.S)
    check(5 <= len(pairs) <= 10, f"FAQ count {len(pairs)} (5-10)")
    for qq, a in pairs:
        n = len(re.sub(r"\s*\[CONFIRM.*?\]", "", a).split())
        check(40 <= n <= 60, f"FAQ answer {n} words (40-60): {qq[:40]}")

    for line in body.splitlines():
        if line.startswith("|---"):
            check(line.count("|") - 1 <= 4, f"table columns {line.count('|') - 1} (<=4)")

    links = re.findall(r"\]\((https?://[^)]+)\)", body)
    internal = [l for l in links if "lynkk.ai" in l]
    external = [l for l in links if "lynkk.ai" not in l]
    check(8 <= len(links) <= 14, f"links {len(links)} (8-14)")
    check(len(internal) >= 3, f"internal lynkk.ai links {len(internal)} (>=3)")
    check(len(external) >= 2 and all(any(o in l for o in OFFICIAL) for l in external),
          f"external links {len(external)} all official gov/standards (>=2)")
    check(not any("/blog/" in l for l in links), "no links to unpublished /blog/ posts")
    check("/features/" in " ".join(internal) or "/use-cases/" in " ".join(internal),
          "links to a lynkk.ai feature or use-case page")

    check(raw.count("\u2014") + raw.count("\u2013") == 0, "no em or en dashes (incl. writer notes)")
    check(not re.search(r"\[(CONFIRM|TODO|TBD|PLACEHOLDER)", s, re.I), "no placeholders like [CONFIRM] in the article")
    check("WRITER-NOTES:START" in raw and raw.index("WRITER-NOTES:START") < raw.index("\n# "), "writer notes block present at the top")
    check(not re.search(r"!\[[^\]]*\]\(\s*\)", body), "no empty image links")
    tells = [t for t in TELLS if t in low]
    check(not tells, f"no AI-tell words {tells}")
    check("Lynkk" in body and "Lynk " not in body and "Lynk." not in body, "brand spelled Lynkk")

    if "<script" in s:
        js = json.loads(s.split('application/ld+json">')[1].split("</script>")[0])
        types = [x["@type"] for x in js["@graph"]]
        check({"Article", "FAQPage", "BreadcrumbList"} <= set(types), f"schema types {types}")
        sch = {x["name"]: x["acceptedAnswer"]["text"] for t in js["@graph"] if t["@type"] == "FAQPage" for x in t["mainEntity"]}
        body_faq = {qq.strip(): re.sub(r"\s*\[CONFIRM.*?\]", "", a.strip()) for qq, a in pairs}
        check(sch == body_faq, "FAQ schema matches body word for word")
    else:
        fails.append("FAIL no JSON-LD schema")

    r = subprocess.run([sys.executable, COMPETITOR_CHECK, path], capture_output=True, text=True)
    check(r.returncode == 0, "zero competitor links")

    print(f"== {path} ({len(words)} words, primary '{primary}') ==")
    for f in fails:
        print(f)
    print(f"{len(notes)} checks passed, {len(fails)} failed")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(max(main(p) for p in sys.argv[1:]))
