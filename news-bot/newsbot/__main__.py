"""Run one pass: Google Trends -> Claude picks -> research -> write -> publish.

    python -m newsbot             # full run
    python -m newsbot --dry-run   # show what would be written, publish nothing
"""

from __future__ import annotations

import argparse
import json
import logging
import tomllib
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import ai, publish, trends

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state.json"
log = logging.getLogger("newsbot")


def load_state() -> dict:
    return json.loads(STATE.read_text()) if STATE.exists() else {"posts": []}


def recently_covered(state: dict, days: int) -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    return [p for p in state["posts"] if datetime.fromisoformat(p["at"]) >= cutoff]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="pick and write, but do not publish or save state")
    parser.add_argument("--config", default=str(ROOT / "config.toml"))
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    cfg = tomllib.loads(Path(args.config).read_text())
    state = load_state()
    recent = recently_covered(state, cfg["bot"]["dedupe_days"])
    seen = {p["keyword"].lower() for p in recent}

    cands = [c for c in trends.collect(cfg) if c.keyword.lower() not in seen]
    log.info("%d trending candidates after dedupe", len(cands))

    picks = ai.select(cfg, cands, [p["title"] for p in recent])
    log.info("Claude picked: %s", [p["keyword"] for p in picks])

    done = 0
    for pick in picks:
        if done >= cfg["bot"]["max_articles_per_run"]:
            break
        try:
            notes, sources = ai.research(cfg, pick)
            article = ai.write(cfg, pick, notes, sources)
        except ai.Refused as exc:
            log.warning("Skipped %r, request declined: %s", pick["keyword"], exc)
            continue
        if not article["publishable"] or not article["sources"]:
            log.info("Skipped %r: %s", pick["keyword"], article["skip_reason"] or "no usable sources")
            continue
        article["trend_keyword"] = pick["keyword"]

        if args.dry_run:
            print(f"\n=== {article['title']} ===\n{publish.full_body(article)}")
        else:
            where = publish.publish(article)
            log.info("Published %r -> %s", article["title"], where)
            state["posts"].append(
                {"keyword": pick["keyword"], "title": article["title"], "slug": article["slug"],
                 "where": where, "at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            )
            STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")
        done += 1

    log.info("Done: %d article(s)", done)


if __name__ == "__main__":
    main()
