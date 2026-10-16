"""Builds paste-ready versions of the three drafts.

- hashnode-post.md: Markdown body for Hashnode's editor (title, subtitle and cover go in their own fields)
- blogger-post.html: HTML body for Blogger's "HTML view" (title goes in the post title field)
- medium-post.html: rendered page to copy from and paste into Medium's editor

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

# Medium: no Markdown import and no tables. Open medium-post.html in a browser, select all the
# text, and paste it into the Medium editor: headings, bold, links, lists and code blocks carry
# over. Images show in the page for reference but must be uploaded in Medium.
medium_md = body_only((CONTENT / "medium-how-to-take-meeting-notes.md").read_text())
medium_html = markdown.markdown(medium_md.replace("](images/", "](../images/"), extensions=["fenced_code"])
page = (
    '<!doctype html>\n<html><head><meta charset="utf-8"><title>Medium paste copy</title>\n'
    '<style>body{font-family:Georgia,serif;max-width:720px;margin:40px auto;padding:0 16px;'
    'line-height:1.6;font-size:19px;color:#151514;background:#fff}img{max-width:100%;height:auto}'
    'pre{background:#f5f5f4;padding:14px;overflow-x:auto;font-size:15px}</style></head><body>\n'
    '<p style="font-family:sans-serif;font-size:14px;background:#fff7ed;padding:10px 14px;border-radius:8px">'
    "Copy from the next line down and paste into Medium. Upload the two images in Medium at the "
    "same spots. Title and subtitle go in Medium's own title fields.</p>\n"
    + medium_html
    + "\n</body></html>\n"
)
(OUT / "medium-post.html").write_text(page)

print("wrote", OUT / "hashnode-post.md")
print("wrote", OUT / "medium-post.html")
print("wrote", OUT / "blogger-post.html")
