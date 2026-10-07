# Lynkk Reddit lead finder

Finds Reddit posts and comments where people are asking about AI note takers,
meeting notes, transcription and meeting assistants, keeps the ones worth a
reply, and gives you a CSV (plus a report you can filter in the browser) to
work through each morning. You read the thread and reply yourself. **Nothing
is ever posted to Reddit by this tool.**

It runs on your Mac with **Claude Code**. No Reddit account, API key or other
AI key is needed: Python reads Reddit's public feeds, and Claude Code (your
normal Claude login) reads each candidate and judges it.

## Setup (once, about 2 minutes)

You need a Mac, [Claude Code](https://claude.com/claude-code) installed and
logged in, and Homebrew or uv.

```bash
cd lynkk-reddit-leads
scripts/setup.sh
```

Then run `claude` in the folder once and accept the "trust this folder"
prompt, so the folder's permissions and `/leads` command load. (Or open the
folder in Claude Code first and say "set this up".)

## Every day

**By hand:** open the folder in Claude Code and type

```
/leads
```

Claude Code searches Reddit, reviews what it found, exports, and tells you
the top opportunities. The search takes up to about 45 minutes because
Reddit's free feeds allow roughly one request a minute; leave it running.

**Automatically:** schedule it once, and every morning the CSV is waiting:

```bash
scripts/install-daily.sh 08:00       # any time you like
```

It runs at that time (or when the Mac next wakes up), shows a notification
when the CSV is ready, and logs to `logs/daily.log`. To test it right away:
`launchctl kickstart gui/$(id -u)/ai.lynkk.reddit-leads`. To stop it:
`scripts/uninstall-daily.sh`.

## What you get

In `output/`:

| File | What |
|---|---|
| `reddit_ai_note_opportunities_<date>.csv` | Today's new opportunities, best first |
| `all_opportunities.csv` | Everything relevant found so far |
| `report.html` | Dashboard, filters, sorting, "Export CSV" and "Copy reply context" buttons. Open it in a browser |

The CSV opens in Google Sheets, Excel, Numbers and pandas
(`pd.read_csv(path, encoding="utf-8-sig")`). Columns: `id, type, username,
content, title, subreddit, reddit_url, author_url, created_at,
keyword_matched, matched_keywords, relevance_score, intent, intent_score,
pain_point, context, potential_use_case, reply_opportunity`, then
`parent_post_url, reviewed_by, first_seen_at`.

- `intent` is one of `high_purchase_intent`, `tool_recommendation`,
  `comparison` (the best ones), `problem_seeking_solution`,
  `workflow_problem`, `general_discussion` or `low_relevance`.
- `reviewed_by` says `claude` once Claude Code has judged the row, or
  `rules` if only the keyword scorer has (for example if a review was
  interrupted).
- Text that starts with `=`, `+`, `-` or `@` gets a leading `'` so
  spreadsheets don't treat it as a formula.

## Replying

1. Open `reddit_url` and read the whole thread first.
2. In Claude Code: `/draft t3_abc123` (the `id` from the CSV). It writes a
   draft to `drafts/t3_abc123.md` following `docs/REPLY.md`: answer the
   question first, mention Lynkk only if it really fits, say you work on it,
   no made-up experience, facts only from `docs/LYNKK.md`.
3. Edit it, check the subreddit's rules, and post it yourself.

## Changing what it looks for

Edit `config.toml` (or ask Claude Code to). The useful knobs:

- `keywords`: phrases to search. Many are packed into one search, so adding
  more is cheap.
- `competitors`: other note takers; "alternative to X" posts score as
  comparisons.
- `subreddits`: `["all"]` for the whole of Reddit, or a list.
- `time_range`: `24h`, `7d`, `30d`, `90d`, or `custom` with `since`.
- `watch_subreddits`: subreddits whose latest comments are scanned every run.
- `min_relevance`: the export cut (default 50).
- `max_requests_per_run`: how long a run may take (one request is about a
  minute).

## How it works

```
fetch    Reddit search (posts) ─┐
         comments under the     ├─ dedupe (id, url, text) ─ skip already seen ─ rule score
         best matching posts    │                                                  │
         latest comments in     ┘                          below 25: dropped ──────┤
         watched subreddits                                                        │
review   Claude Code reads each candidate: intent, scores, pain point, context ◄───┘
export   ranked CSVs + report.html
```

Everything seen is kept in `data/leads.db` (SQLite), so each run only
processes new conversations. `uv run leads fetch --rescan` re-processes old
ones. Every Reddit request is logged in `logs/requests.log`.

## Honest limits

- **Speed.** Without a Reddit API key, Reddit allows about one request a
  minute. A full run is about 45 requests. The tool waits as long as Reddit's
  headers say, and never tries to get around the limit.
- **Comments.** Reddit's search doesn't search comments. Comments are found
  in threads of matching posts and in the latest comments of the watched
  subreddits (the most recent 100 per request). A comment in an unrelated
  thread elsewhere on Reddit won't be found.
- **Parent comments.** Reddit's feeds list a thread's comments flat, so the
  CSV gives the parent post (title, link and excerpt) but not which comment
  a reply was answering. Open the link to see the conversation.
- **Reddit's rules.** Reddit's terms limit commercial use of its data, and
  most subreddits ban self-promotion. Use this to find people to help, keep
  replies genuinely useful, and disclose that you work on Lynkk.

## Troubleshooting

- *"Reddit answered 403 (blocked)"*: your network or VPN is blocked by
  Reddit. Try another network, or later.
- *A run stops early*: it hit `max_requests_per_run`. Whatever it found is
  saved, and the next run carries on.
- *Rows say `reviewed_by: rules`*: run `/review` in Claude Code to finish
  the review, then the CSV is rewritten.
- *Nothing in the CSV*: `uv run leads status` shows what was found; lower
  `min_relevance` or widen `time_range` in `config.toml`.

## Commands

```bash
uv run leads fetch [--quick] [--rescan]
uv run leads review next | apply | status
uv run leads export [--all]
uv run leads draft <id>
uv run leads status
uv run pytest            # tests (uses recorded Reddit feeds, no network)
```
