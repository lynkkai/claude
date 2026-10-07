"""Push finished articles to the Lynkk news section.

Pick a target with PUBLISH_TARGET:
  markdown  - write .md files with front matter (Next.js / Astro / Hugo sites kept in git)
  wordpress - WordPress REST API (WP_URL, WP_USER, WP_APP_PASSWORD)
  webhook   - POST JSON to any backend or headless CMS (NEWS_WEBHOOK_URL, NEWS_WEBHOOK_TOKEN)

PUBLISH_STATUS=draft (default) keeps posts unpublished for a human check; set it to
"publish" to go fully automatic.
"""

from __future__ import annotations

import base64
import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import markdown as md


def full_body(article: dict) -> str:
    body = article["body_markdown"].rstrip()
    if article["sources"]:
        body += "\n\n## Sources\n\n" + "\n".join(f"- [{s['title']}]({s['url']})" for s in article["sources"])
    return body + "\n"


def _post_json(url: str, payload: dict, headers: dict) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read()
    return json.loads(raw) if raw else {}


def to_markdown(article: dict, status: str) -> str:
    out_dir = Path(os.environ.get("MARKDOWN_OUT_DIR", "output/news"))
    out_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    path = out_dir / f"{now:%Y-%m-%d}-{article['slug']}.md"
    front = {
        "title": article["title"],
        "slug": article["slug"],
        "date": now.isoformat(timespec="seconds"),
        "description": article["meta_description"],
        "excerpt": article["excerpt"],
        "tags": article["tags"],
        "draft": status != "publish",
        "trend_keyword": article["trend_keyword"],
    }
    lines = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in front.items()] + ["---", ""]
    path.write_text("\n".join(lines) + full_body(article), encoding="utf-8")
    return str(path)


def to_wordpress(article: dict, status: str) -> str:
    auth = base64.b64encode(f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}".encode()).decode()
    payload = {
        "title": article["title"],
        "slug": article["slug"],
        "status": status,
        "excerpt": article["excerpt"],
        "content": md.markdown(full_body(article)),
    }
    if os.environ.get("WP_CATEGORY_ID"):
        payload["categories"] = [int(os.environ["WP_CATEGORY_ID"])]
    res = _post_json(os.environ["WP_URL"].rstrip("/") + "/wp-json/wp/v2/posts", payload, {"Authorization": f"Basic {auth}"})
    return res.get("link", "")


def to_webhook(article: dict, status: str) -> str:
    payload = {
        **{k: article[k] for k in ("title", "slug", "excerpt", "meta_description", "tags", "sources", "trend_keyword")},
        "status": status,
        "body_markdown": full_body(article),
        "body_html": md.markdown(full_body(article)),
        "published_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    headers = {}
    if os.environ.get("NEWS_WEBHOOK_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['NEWS_WEBHOOK_TOKEN']}"
    res = _post_json(os.environ["NEWS_WEBHOOK_URL"], payload, headers)
    return res.get("url", "")


TARGETS = {"markdown": to_markdown, "wordpress": to_wordpress, "webhook": to_webhook}


def publish(article: dict) -> str:
    target = os.environ.get("PUBLISH_TARGET", "markdown")
    status = os.environ.get("PUBLISH_STATUS", "draft")
    return TARGETS[target](article, status)
