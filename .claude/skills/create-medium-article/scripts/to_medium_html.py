#!/usr/bin/env python3
"""Convert an article.md into paste-ready HTML for the Medium editor.

Usage: python3 -I to_medium_html.py <article.md> [<out.html>]

Medium has no Markdown import, but it keeps formatting when rich text is pasted
into a new story. Open the output in a browser, select all, copy, and paste.

Mapping follows Medium's own export format: title -> h1 (Medium "big T"),
subtitle -> h4 (Medium "small T" directly under the title), section headings
-> h3 (big T), ### headings -> h4 (small T). Supports the subset Medium can
render: paragraphs, bold, italic, inline code, links, flat bullet and numbered
lists, blockquotes, fenced code blocks and separators. Tables and nested lists
are reported as errors because Medium cannot display them.
"""

import html
import re
import sys


def parse_frontmatter(lines):
    meta = {}
    if lines and lines[0].strip() == "---":
        end = lines.index("---", 1)
        for raw in lines[1:end]:
            m = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', raw)
            if m:
                meta[m.group(1)] = m.group(2)
        lines = lines[end + 1:]
    return meta, lines


def inline(text):
    text = html.escape(text, quote=False)
    codes = []

    def stash(m):
        codes.append(f"<code>{m.group(1)}</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)


def convert(md_text):
    meta, lines = parse_frontmatter(md_text.splitlines())
    out, errors = [], []
    title, subtitle = meta.get("title", ""), meta.get("subtitle", "")
    if title:
        out.append(f"<h1>{inline(title)}</h1>")
    if subtitle:
        out.append(f"<h4>{inline(subtitle)}</h4>")

    i, para, list_tag = 0, [], None

    def flush_para():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def close_list():
        nonlocal list_tag
        if list_tag:
            out.append(f"</{list_tag}>")
            list_tag = None

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("```"):
            flush_para(); close_list()
            block = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            out.append("<pre>" + html.escape("\n".join(block), quote=False) + "</pre>")
        elif not s:
            flush_para(); close_list()
        elif s.startswith("# "):
            flush_para(); close_list()
            # Article H1 duplicates the frontmatter title; skip it and an
            # italic subtitle line that directly follows.
            if title:
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and re.fullmatch(r"\*[^*].*\*", lines[j].strip()):
                    i = j
            else:
                out.append(f"<h1>{inline(s[2:])}</h1>")
        elif s.startswith("## "):
            flush_para(); close_list()
            out.append(f"<h3>{inline(s[3:])}</h3>")
        elif s.startswith("### "):
            flush_para(); close_list()
            out.append(f"<h4>{inline(s[4:])}</h4>")
        elif re.fullmatch(r"-{3,}|\*{3,}", s):
            flush_para(); close_list()
            out.append("<hr>")
        elif s.startswith("|"):
            errors.append(f"line {i + 1}: table (Medium cannot display tables)")
        elif re.match(r"^\s{2,}([-*]|\d+\.)\s", line):
            errors.append(f"line {i + 1}: nested list (Medium cannot display nested lists)")
        elif re.match(r"^[-*]\s", s) or re.match(r"^\d+\.\s", s):
            flush_para()
            tag = "ul" if re.match(r"^[-*]\s", s) else "ol"
            if list_tag != tag:
                close_list()
                out.append(f"<{tag}>")
                list_tag = tag
            out.append(f"<li>{inline(re.sub(r'^([-*]|\d+\.)\s+', '', s))}</li>")
        elif s.startswith(">"):
            flush_para(); close_list()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
            continue
        else:
            close_list()
            para.append(s)
        i += 1
    flush_para(); close_list()
    return meta, "\n".join(out), errors


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{ --bg: #fff; --fg: #242424; --muted: #6b6b6b; --code: #f2f2f2; --link: #1a8917; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg: #121212; --fg: #e6e6e6; --muted: #a0a0a0; --code: #262626; --link: #6fcf72; }}
  }}
  body {{ background: var(--bg); color: var(--fg); margin: 0; padding: 32px 16px; }}
  main {{ max-width: 680px; margin: 0 auto; font: 20px/1.6 Georgia, "Times New Roman", serif; }}
  h1 {{ font: 700 40px/1.2 -apple-system, "Helvetica Neue", Arial, sans-serif; margin: 0 0 8px; }}
  h3 {{ font: 700 26px/1.3 -apple-system, "Helvetica Neue", Arial, sans-serif; margin: 40px 0 8px; }}
  h4 {{ font: 400 22px/1.4 -apple-system, "Helvetica Neue", Arial, sans-serif; color: var(--muted); margin: 0 0 32px; }}
  a {{ color: var(--link); }}
  code {{ background: var(--code); padding: 2px 4px; font-size: 16px; }}
  pre {{ background: var(--code); padding: 16px; font-size: 15px; line-height: 1.5; overflow-x: auto; }}
  blockquote {{ border-left: 3px solid var(--fg); margin: 0; padding-left: 20px; font-style: italic; }}
  hr {{ border: 0; text-align: center; margin: 40px 0; }}
  hr::after {{ content: "* * *"; color: var(--muted); letter-spacing: 1em; }}
</style>
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    src = argv[1]
    dst = argv[2] if len(argv) > 2 else re.sub(r"\.md$", "", src) + ".medium.html"
    with open(src, encoding="utf-8") as f:
        meta, body, errors = convert(f.read())
    for e in errors:
        print("ERROR", e)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(PAGE.format(title=html.escape(meta.get("title", "Article")), body=body))
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    print(f"wrote {dst} ({words} words, about {round(words / 265)} min read)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
