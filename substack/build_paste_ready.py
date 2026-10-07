#!/usr/bin/env python3
"""Build paste-ready Substack pages from the article Markdown files.

For each article in substack/articles/, writes substack/paste-ready/<name>.html with:
  1. The Substack settings fields (title, subtitle, SEO, slug...), each with a copy button.
  2. The clean article body (no front matter, title, subtitle, button markers or Notes),
     rendered as rich text so it pastes into the Substack editor with formatting intact.
  3. The promo Notes, each with a copy button.

Usage: python3 substack/build_paste_ready.py [article.md ...]   (default: all articles)
Requires: pip install markdown
"""
import html
import pathlib
import re
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "paste-ready"
BUTTON_RE = re.compile(r"^\*\*\[(Subscribe|Share) button\]\*\*$")
FIELDS = [
    ("title", "Title"),
    ("subtitle", "Subtitle"),
    ("title_b", "A/B test title (optional)"),
    ("seo_title", "SEO title (Settings > SEO)"),
    ("seo_description", "SEO description (Settings > SEO)"),
    ("slug", "URL slug (Settings > SEO)"),
    ("section", "Section"),
    ("tags", "Tags"),
    ("social_image", "Social preview image brief"),
]


def parse(path):
    text = path.read_text()
    _, fm, rest = text.split("---\n", 2)
    meta = {}
    for line in fm.strip().splitlines():
        key, _, value = line.partition(":")
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1].replace('\\"', '"')
        meta[key.strip()] = value.strip("[]") if key.strip() == "tags" else value

    body, _, notes_md = rest.partition("\n## Promo Notes\n")
    lines = body.strip().splitlines()
    # Drop "# Title", the italic subtitle line and the divider under them.
    while lines and (lines[0].startswith("# ") or lines[0].startswith("*") or lines[0] in ("", "---")):
        lines.pop(0)
    # Drop the trailing divider before the Notes section.
    while lines and lines[-1] in ("", "---"):
        lines.pop()

    buttons, kept = [], []
    for line in lines:
        m = BUTTON_RE.match(line.strip())
        if m:
            prev = next((p for p in reversed(kept) if p.strip()), "")
            tail = " ".join(re.sub(r"[*_\[\]()>#]|https?://\S+", "", prev).split()[-8:])
            buttons.append((m.group(1), tail))
        else:
            kept.append(line)
    body_html = markdown.markdown("\n".join(kept), extensions=["fenced_code"])

    notes = []
    for label, block in re.findall(r"\*\*(Note \d+[^*]*)\*\*\n((?:>.*\n?)+)", notes_md):
        notes.append((label, "\n".join(l[2:] if l.startswith("> ") else l[1:] for l in block.strip().splitlines())))
    return meta, body_html, buttons, notes


def copy_row(label, value, idx):
    return (
        f'<div class="field"><div class="field-head"><span class="label">{html.escape(label)}</span>'
        f'<span class="count">{len(value)} chars</span>'
        f'<button data-copy="f{idx}">Copy</button></div>'
        f'<div class="value" id="f{idx}">{html.escape(value)}</div></div>'
    )


def render(meta, body_html, buttons, notes):
    fields = "".join(copy_row(lbl, meta[k], i) for i, (k, lbl) in enumerate(FIELDS) if meta.get(k))
    btn_items = "".join(
        f"<li><strong>{kind} button</strong> after the paragraph ending “…{html.escape(tail)}”</li>"
        for kind, tail in buttons
    )
    note_items = "".join(
        f'<div class="field"><div class="field-head"><span class="label">{html.escape(lbl)}</span>'
        f'<button data-copy="n{i}">Copy</button></div>'
        f'<div class="value note" id="n{i}">{html.escape(txt)}</div></div>'
        for i, (lbl, txt) in enumerate(notes)
    )
    return TEMPLATE.format(
        title=html.escape(meta["title"]),
        fields=fields,
        buttons=btn_items,
        body=body_html,
        notes=note_items,
    )


TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{ --bg:#f7f6f3; --card:#ffffff; --ink:#1d1d1f; --muted:#6b6b70; --line:#e3e1dc; --accent:#ff6719; --code:#f2f1ee; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#141416; --card:#1e1e21; --ink:#ececee; --muted:#9a9aa1; --line:#2e2e33; --accent:#ff7a33; --code:#26262a; }} }}
:root[data-theme="dark"] {{ --bg:#141416; --card:#1e1e21; --ink:#ececee; --muted:#9a9aa1; --line:#2e2e33; --accent:#ff7a33; --code:#26262a; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:16px/1.6 -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }}
main {{ max-width:760px; margin:0 auto; padding:32px 16px 64px; }}
h1.page {{ font-size:22px; margin:0 0 4px; }}
p.lede {{ color:var(--muted); margin:0 0 28px; }}
section {{ background:var(--card); border:1px solid var(--line); border-radius:12px; padding:20px; margin-bottom:24px; }}
section > h2 {{ font-size:13px; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); margin:0 0 14px; display:flex; justify-content:space-between; align-items:center; gap:12px; }}
.field {{ border-top:1px solid var(--line); padding:10px 0; }}
.field:first-of-type {{ border-top:0; }}
.field-head {{ display:flex; align-items:center; gap:10px; }}
.label {{ font-weight:600; font-size:14px; }}
.count {{ color:var(--muted); font-size:12px; margin-left:auto; }}
.value {{ margin-top:4px; overflow-wrap:anywhere; }}
.note {{ white-space:pre-wrap; }}
button {{ font:inherit; font-size:13px; padding:4px 12px; border-radius:999px; border:1px solid var(--accent); background:transparent; color:var(--accent); cursor:pointer; }}
.field-head button {{ margin-left:0; }}
.field-head .label + button {{ margin-left:auto; }}
button.done {{ background:var(--accent); color:#fff; }}
ul.tips {{ margin:0; padding-left:20px; }}
#article {{ font-family: Georgia, "Times New Roman", serif; font-size:18px; line-height:1.65; }}
#article h2 {{ font-family:inherit; font-size:24px; margin:32px 0 8px; display:block; text-transform:none; letter-spacing:normal; color:var(--ink); }}
#article h3 {{ font-family:inherit; font-size:19px; margin:24px 0 6px; }}
#article blockquote {{ border-left:3px solid var(--accent); margin:20px 0; padding:2px 16px; font-style:italic; }}
#article pre {{ background:var(--code); padding:14px; border-radius:8px; overflow-x:auto; font-size:14px; line-height:1.5; }}
#article a {{ color:var(--accent); }}
</style></head>
<body><main>
<h1 class="page">{title}</h1>
<p class="lede">Paste-ready for Substack. Copy the fields into the post editor, then copy the article body into the editor's body area.</p>

<section><h2>1. Substack fields</h2>{fields}</section>

<section><h2>2. Article body <button data-copy="article" data-rich="1">Copy article</button></h2>
<ul class="tips">
<li>Paste below the title and subtitle fields in Substack (the title and subtitle are not in this body).</li>
{buttons}
<li>Select the quote block and switch it to <strong>Pull quote</strong> in the editor.</li>
</ul>
</section>
<section id="article">{body}</section>

<section><h2>3. Promo Notes (post over the following days)</h2>{notes}</section>
</main>
<script>
async function copyEl(btn) {{
  const el = document.getElementById(btn.dataset.copy);
  const rich = btn.dataset.rich === "1";
  let ok = false;
  try {{
    if (rich && window.ClipboardItem) {{
      await navigator.clipboard.write([new ClipboardItem({{
        "text/html": new Blob([el.innerHTML], {{type:"text/html"}}),
        "text/plain": new Blob([el.innerText], {{type:"text/plain"}})
      }})]);
    }} else {{
      await navigator.clipboard.writeText(el.innerText);
    }}
    ok = true;
  }} catch (e) {{
    try {{
      const r = document.createRange(); r.selectNodeContents(el);
      const s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      ok = document.execCommand("copy"); s.removeAllRanges();
    }} catch (e2) {{}}
  }}
  const old = btn.textContent;
  btn.textContent = ok ? "Copied" : "Select and copy manually";
  btn.classList.toggle("done", ok);
  setTimeout(() => {{ btn.textContent = old; btn.classList.remove("done"); }}, 1800);
}}
document.querySelectorAll("button[data-copy]").forEach(b => b.addEventListener("click", () => copyEl(b)));
</script>
</body></html>
"""


def main(paths):
    OUT.mkdir(exist_ok=True)
    targets = [pathlib.Path(p) for p in paths] or sorted((ROOT / "articles").glob("*.md"))
    for path in targets:
        out = OUT / (path.stem + ".html")
        out.write_text(render(*parse(path)))
        print(f"wrote {out.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    main(sys.argv[1:])
