"""Command line: uv run leads <command>."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import config as config_mod
from .analysis.intent import rank
from .db import DB
from .drafts import write_draft_context
from .export.csv_export import write_csv
from .export.report import write_report
from .fetch import Fetcher
from .reddit.http import Http
from .reddit.ratelimit import Throttle
from .reddit.source import RssSource
from .review import apply_results, batch_path, results_path, write_batch


def _open(args) -> tuple[config_mod.Config, DB]:
    cfg = config_mod.load(Path(args.config) if args.config else None)
    return cfg, DB(cfg.db_path)


def cmd_fetch(args) -> int:
    cfg, db = _open(args)
    budget = 12 if args.quick else cfg.max_requests_per_run
    http = Http(
        cfg.user_agent,
        Throttle(cfg.min_seconds_between_requests),
        max_requests=budget,
        log_path=cfg.log_dir / "requests.log",
    )
    print(f"Searching Reddit... up to {budget} requests. Reddit's free feeds allow about one a minute,", flush=True)
    print(f"so this can take up to {budget} minutes. Leave it running.", flush=True)
    stats = Fetcher(cfg, db, RssSource(http), rescan=args.rescan, log=lambda m: print(m, flush=True)).run()
    print()
    print(f"Done. {stats.requests} requests.")
    print(f"  results read: {stats.found}")
    print(f"  new items: {stats.new} ({stats.for_review} for review, {stats.skipped} off topic, {stats.duplicates} duplicates)")
    print(f"  already seen: {stats.already_seen}")
    if stats.stopped_early:
        print(f"  note: {stats.stopped_early}")
    print(f"  waiting for review in total: {db.count_pending()}")
    db.close()
    return 0


def cmd_review(args) -> int:
    cfg, db = _open(args)
    if args.action == "next":
        path, n, waiting = write_batch(cfg, db, args.size)
        if n == 0:
            print("No items waiting for review.")
            if path.exists():
                path.unlink()
        else:
            print(f"Wrote {n} items to {path.relative_to(cfg.root)} ({waiting} waiting in total).")
            print(f"Classify them per docs/CLASSIFY.md into {results_path(cfg).relative_to(cfg.root)},")
            print("then run: uv run leads review apply")
    elif args.action == "apply":
        saved, errors = apply_results(cfg, db, Path(args.path) if args.path else None)
        print(f"Saved {saved} reviews. {db.count_pending()} still waiting.")
        if errors:
            print("Fix these lines and run apply again (saved lines are safe to re-apply):")
            for e in errors:
                print(f"  {e}")
            db.close()
            return 1
    else:  # status
        print(f"{db.count_pending()} items waiting for review.")
        if batch_path(cfg).exists():
            print(f"An unfinished batch is in {batch_path(cfg).relative_to(cfg.root)}.")
    db.close()
    return 0


def _local_date(utc_stamp: str) -> str:
    """'2026-10-06T19:05:01Z' (stored in UTC) as the local calendar date."""
    dt = datetime.strptime(utc_stamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return dt.astimezone().strftime("%Y-%m-%d")


def cmd_export(args) -> int:
    cfg, db = _open(args)
    today = datetime.now().strftime("%Y-%m-%d")
    relevant = db.exportable(cfg.min_relevance)
    if args.all:
        todays = relevant
    else:
        todays = [it for it in relevant if not it["exported_at"] or _local_date(it["exported_at"]) == today]
    new_ids = {it["reddit_id"] for it in relevant if not it["exported_at"]}
    out = cfg.output_dir
    daily = write_csv(out / cfg.export_filename.format(date=today), rank(todays))
    master = write_csv(out / "all_opportunities.csv", rank(relevant))
    report = write_report(out / "report.html", db.all_items(), relevant, new_ids)
    db.mark_exported(list(new_ids))
    pending = db.count_pending()
    print(f"Today's CSV: {daily.relative_to(cfg.root)} ({len(todays)} rows, {len(new_ids)} new)")
    print(f"All time CSV: {master.relative_to(cfg.root)} ({len(relevant)} rows)")
    print(f"Report: {report.relative_to(cfg.root)} (open it in a browser)")
    if pending:
        print(f"Note: {pending} items are not reviewed yet; they are scored by rules only.")
    db.close()
    return 0


def cmd_draft(args) -> int:
    cfg, db = _open(args)
    path = write_draft_context(cfg, db, args.id)
    db.close()
    if not path:
        print(f"No item {args.id}. Use the id column from the CSV, like t3_abc123.")
        return 1
    print(f"Context written to {path.relative_to(cfg.root)}. Write the draft under '## Draft reply'.")
    return 0


def cmd_status(args) -> int:
    cfg, db = _open(args)
    counts = db.status_counts()
    total = sum(counts.values())
    print(f"Items stored: {total}")
    for k in ("review", "reviewed", "skipped", "duplicate"):
        print(f"  {k}: {counts.get(k, 0)}")
    print(f"Exportable now (score >= {cfg.min_relevance}): {len(db.exportable(cfg.min_relevance))}")
    print(f"Last search: {db.last_search_at() or 'never'}")
    db.close()
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="leads", description="Find Reddit conversations about AI meeting notes.")
    p.add_argument("--config", help="path to config.toml (default: the project's)")
    sub = p.add_subparsers(dest="command", required=True)

    f = sub.add_parser("fetch", help="search Reddit and store new items")
    f.add_argument("--rescan", action="store_true", help="re-process items seen before")
    f.add_argument("--quick", action="store_true", help="at most 12 requests (about 12 minutes)")
    f.set_defaults(fn=cmd_fetch)

    r = sub.add_parser("review", help="hand items to Claude Code and read its verdicts back")
    r.add_argument("action", choices=["next", "apply", "status"])
    r.add_argument("path", nargs="?", help="results file for apply")
    r.add_argument("--size", type=int, help="batch size (default from config)")
    r.set_defaults(fn=cmd_review)

    e = sub.add_parser("export", help="write the CSVs and the HTML report")
    e.add_argument("--all", action="store_true", help="today's CSV gets every relevant item, not just new ones")
    e.set_defaults(fn=cmd_export)

    d = sub.add_parser("draft", help="write a reply context file for one item")
    d.add_argument("id")
    d.set_defaults(fn=cmd_draft)

    s = sub.add_parser("status", help="counts and last run")
    s.set_defaults(fn=cmd_status)

    args = p.parse_args(argv)
    try:
        return args.fn(args)
    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
