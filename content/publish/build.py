"""Builds paste-ready versions of the three drafts.

- hashnode-post.md: Markdown body for Hashnode's editor (title, subtitle and cover go in their own fields)
- blogger-post.html: HTML body for Blogger's "HTML view" (title goes in the post title field)
- medium-post.html: Medium-safe page to copy from and paste into Medium's editor

The drafts in content/ stay the single source of truth; re-run this after editing them:
    python3 content/publish/build.py
"""
import re
from pathlib import Path

import markdown

CONTENT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent


def body_only(text: str) -> str:
    """Drop the draft header comment and the H1 (both platforms take the title in a separate field)."""
    text = re.sub(r"<!--.*?-->\s*", "", text, count=1, flags=re.S)
    text = re.sub(r"^# .*\n+", "", text, count=1)
    return text.strip() + "\n"


def image_placeholders(text: str) -> str:
    """Local image paths become IMAGE_URL placeholders to swap for the uploaded image URL."""
    return re.sub(r"\]\(images/([\w-]+)\.png\)", r"](IMAGE_URL_\1)", text)


# Hashnode: Markdown is pasted as-is.
hashnode = body_only((CONTENT / "hashnode-ai-meeting-notes-transcript-prompt.md").read_text())
(OUT / "hashnode-post.md").write_text(image_placeholders(hashnode))

# Blogger: convert to HTML with light inline styles, since Blogger themes often leave
# tables and code blocks unstyled.
blogger_md = image_placeholders(
    body_only((CONTENT / "blogger-meeting-minutes-template-action-items.md").read_text())
)
html = markdown.markdown(blogger_md, extensions=["tables", "fenced_code"])
styles = {
    "<table>": '<table style="border-collapse:collapse;width:100%;margin:16px 0;">',
    "<th>": '<th style="border:1px solid #e0e3e9;padding:8px 10px;text-align:left;background:#f5f5f4;">',
    "<td>": '<td style="border:1px solid #e0e3e9;padding:8px 10px;vertical-align:top;">',
    "<pre>": '<pre style="background:#f5f5f4;border:1px solid #e0e3e9;border-radius:8px;padding:16px;overflow-x:auto;font-size:14px;line-height:1.5;">',
}
for tag, styled in styles.items():
    html = html.replace(tag, styled)
html = re.sub(
    r'<img alt="([^"]*)" src="([^"]*)" />',
    r'<img src="\2" alt="\1" title="\1" width="1200" style="max-width:100%;height:auto;" />',
    html,
)

# The drafts are hard-wrapped. Blogger can turn raw newlines into <br>, so unwrap everything
# outside <pre> blocks and put one block element per line.
parts = re.split(r"(<pre.*?</pre>)", html, flags=re.S)
for i, part in enumerate(parts):
    if not part.startswith("<pre"):
        part = part.replace("\n", " ")
        part = re.sub(r"(</(?:p|h2|h3|ul|ol|li|table|thead|tbody|tr)>|<hr />)\s*", r"\1\n", part)
        parts[i] = part
html = "".join(parts)
(OUT / "blogger-post.html").write_text(html.strip() + "\n")

# Medium: its editor has no Markdown import, no tables, no raw HTML and only two heading levels,
# and pasted multi-line code blocks and local images often break. So the Medium page only uses
# what the editor accepts on paste: paragraphs, 2 heading levels, bold, italic, links, lists and
# a separator.
#   - code blocks become plain paragraphs with line breaks (ALL CAPS section lines in bold)
#   - images become a visible "upload image here" marker
#   - placeholder links become valid URLs (Medium drops links that aren't real URLs)
# Open medium-post.html in a browser, select all, copy, and paste into a new Medium story.
def medium_block(code: str) -> str:
    lines = []
    for line in code.strip("\n").split("\n"):
        line = line.rstrip().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        lines.append(f"<strong>{line}</strong>" if line.isupper() and len(line) > 3 else line)
    paras = "<br>".join(lines).split("<br><br>")
    return "\n".join(f"<p>{p}</p>" for p in paras if p)


medium_md = body_only((CONTENT / "medium-how-to-take-meeting-notes.md").read_text())
blocks = re.findall(r"```\n(.*?)```", medium_md, flags=re.S)
for i in range(len(blocks)):
    medium_md = re.sub(r"```\n.*?```", f"MEDIUMBLOCK{i}", medium_md, count=1, flags=re.S)
medium_html = markdown.markdown(medium_md)
for i, block in enumerate(blocks):
    medium_html = medium_html.replace(f"<p>MEDIUMBLOCK{i}</p>", medium_block(block))
medium_html = re.sub(
    r'<p><img alt="[^"]*" src="images/([\w-]+\.png)" /></p>',
    r"<p><strong>[ Upload image here: \1 ]</strong></p>",
    medium_html,
)
medium_html = medium_html.replace("BLOGGER_POST_URL", "https://replace-with-blogger-post-url.example")
medium_html = medium_html.replace("HASHNODE_POST_URL", "https://replace-with-hashnode-post-url.example")
disclosure = (
    "<p><em>This article was drafted with AI assistance, then reviewed, edited and fact-checked "
    "by the Lynkk team.</em></p>\n"
)
page = (
    '<!doctype html>\n<html><head><meta charset="utf-8"><title>Medium paste copy</title>\n'
    '<style>body{font-family:Georgia,serif;max-width:720px;margin:40px auto;padding:0 16px;'
    'line-height:1.6;font-size:19px;color:#151514;background:#fff}</style></head><body>\n'
    + medium_html.replace("medium-banner.png ]</strong></p>", "medium-banner.png ]</strong></p>\n" + disclosure, 1)
    + "\n</body></html>\n"
)
(OUT / "medium-post.html").write_text(page)

print("wrote", OUT / "hashnode-post.md")
print("wrote", OUT / "medium-post.html")
print("wrote", OUT / "blogger-post.html")
