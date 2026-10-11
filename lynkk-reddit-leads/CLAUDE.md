# Reddit lead finder: instructions for Claude Code

This folder finds Reddit posts and comments where people need what Lynkk (an
AI meeting assistant, lynkk.ai) does, and exports them to CSV so a person can
read each conversation and reply by hand. Python does the fetching, scoring,
dedupe and export. **You** do the judgement: classifying each item and
drafting replies.

## Hard rules

- **Never post, comment, vote or message on Reddit**, and never try to log in
  to Reddit. Replies are drafts for a human.
- Reddit data comes only through `uv run leads fetch`, which reads Reddit's
  public feeds and waits as long as Reddit's rate limit asks. Never fetch
  Reddit any other way (no curl, no WebFetch, no browser, no scraping
  pages), and never shorten the waits.
- Claims about Lynkk only from `docs/LYNKK.md`.
- No em dashes in anything you write (classifications, drafts, summaries).
- Don't change code in `src/` unless the person asks. Changing `config.toml`
  (keywords, subreddits, time range, thresholds) is fine when they ask.

## Commands

```bash
uv run leads fetch            # search Reddit, store new items (slow: ~1 request a minute)
uv run leads fetch --quick    # at most 12 requests
uv run leads fetch --rescan   # re-process items seen before
uv run leads review next      # write the next batch to work/batch.json
uv run leads review apply     # save work/batch.results.jsonl
uv run leads export           # output/ CSVs + output/report.html
uv run leads draft <id>       # drafts/<id>.md with the conversation
uv run leads status           # counts and last run
```

## "Run today's leads" (or /leads)

1. `uv run leads status`. If the last search was within the past 12 hours,
   skip to step 3 unless the person asked for a fresh search.
2. `uv run leads fetch`. It can take 45 minutes because Reddit's free feeds
   allow about one request a minute. Run it in the background and wait for it
   to finish; don't poll with sleep and don't stop it early. Tell the person
   it's running and roughly how long it takes.
3. Review loop, until `review next` says nothing is waiting:
   - `uv run leads review next`
   - Read `work/batch.json` and classify every item per `docs/CLASSIFY.md`.
   - Write `work/batch.results.jsonl` (one JSON object per line).
   - `uv run leads review apply`. Fix any lines it rejects and apply again.
4. `uv run leads export`.
5. Report back in a few lines: how many new items, how many relevant, the top
   five opportunities (intent, one-line pain point, URL), and where the files
   are (`output/reddit_ai_note_opportunities_<date>.csv`,
   `output/all_opportunities.csv`, `output/report.html`). Offer to open the
   report (`open output/report.html`) or draft replies.

Don't run `scripts/daily.sh` from inside Claude Code: it starts its own Claude
Code session, which can't run inside this one. The steps above do the same job.

## "Draft a reply to <id>" (or /draft <id>)

Follow `docs/REPLY.md`: run `uv run leads draft <id>`, read `drafts/<id>.md`,
write the reply under `## Draft reply`, add `## Notes for the poster`, and
show the draft in chat. Never post it.

## Files

| Path | What |
|---|---|
| `config.toml` | Keywords, subreddits, time range, thresholds, limits |
| `docs/CLASSIFY.md` | How to classify an item (intent, scores, pain point) |
| `docs/REPLY.md` | How to draft a reply |
| `docs/LYNKK.md` | What Lynkk really does; the only source for product claims |
| `data/leads.db` | SQLite: every item seen, so nothing is processed twice |
| `work/` | Review batches (temporary) |
| `output/` | CSVs and the HTML report |
| `drafts/` | Reply drafts |
| `logs/` | `requests.log` (every Reddit request), `daily.log` (scheduled runs) |
| `src/leads/` | The code: `reddit/` (feeds, rate limit), `analysis/` (keywords, rules, intent, dedupe), `review/`, `export/` |
