# Lynkk trending AI news bot

Watches Google Trends for AI tool searches that suddenly jump (ChatGPT, Claude, Perplexity,
Gemini, meeting assistant competitors, new AI tools), has Claude research and write a short
sourced news post, and pushes it to the Lynkk news section. Runs every hour on GitHub Actions.

## How it works

```
Google Trends                    Claude                                   Lynkk news section
-------------                    ------                                   ------------------
Trending Now feed (US, IN, GB) ┐
                               ├─> 1. Pick: which spikes are AI news? ─┐
SerpApi watchlist spikes      ─┤   (rejects sports, celebs, repeats)   │
SerpApi rising queries        ┘                                        v
                                 2. Research: live web search, builds a
                                    dated fact sheet with source URLs
                                                                       v
                                 3. Write: 350-650 words, only sourced  ──> markdown / WordPress / webhook
                                    facts, house style, SEO fields           (draft by default)
```

1. **Trend detection** (`newsbot/trends.py`)
   - Google Trends **Trending Now** RSS: free, no key. Every item already spiked in the last hours.
   - **Watchlist spikes** (optional, `SERPAPI_KEY`): checks the AI tools in `config.toml` and flags
     any whose recent interest is 2x its 7-day baseline.
   - **Rising related queries** (optional): finds brand-new AI tool names rising next to seeds like
     "AI note taker". This is how tools you have not heard of yet get picked up.
2. **Selection**: Claude reads all spiking terms and keeps only ones that match the beat in
   `config.toml` (`[topics]`). Anything already posted in the last 5 days is skipped.
3. **Research**: Claude searches the web and writes a fact sheet. If there is no verifiable story,
   nothing gets written.
4. **Writing**: Claude writes the post using only the fact sheet, with title, slug, meta description,
   excerpt, tags and a sources list. Em and en dashes are stripped automatically, and any source URL
   Claude did not actually find in research is dropped.
5. **Publishing**: one of three targets (below). `state.json` remembers what was posted.

## Setup

1. Get an Anthropic API key (console.anthropic.com). Optional: a SerpApi key (serpapi.com) for
   watchlist spikes and new-tool discovery. Without it the bot still runs on Trending Now alone.
2. In GitHub: **Settings > Secrets and variables > Actions**
   - Secrets: `ANTHROPIC_API_KEY`, optional `SERPAPI_KEY`
   - Variable `PUBLISH_TARGET`: `markdown`, `wordpress` or `webhook` (see below)
   - Variable `PUBLISH_STATUS`: `draft` (default, recommended to start) or `publish`
3. Merge to the default branch. GitHub only runs scheduled workflows from the default branch.
4. Test first: **Actions > Lynkk trending AI news > Run workflow** with "dry run" ticked. The articles
   appear in the job log and nothing is published.

## Publishing targets: pick the one that matches how lynkk.ai is built

| Target | Use when the news section is... | Settings |
|---|---|---|
| `markdown` (default) | Markdown files in a git repo (Next.js, Astro, Hugo, Gatsby) | `MARKDOWN_OUT_DIR` (default `output/news`). Point it at the site's content folder, or copy files over in a later step. |
| `wordpress` | WordPress | Variables `WP_URL`, `WP_USER`, optional `WP_CATEGORY_ID` (the "News" category); secret `WP_APP_PASSWORD` (Users > Profile > Application Passwords) |
| `webhook` | A custom backend or headless CMS (Strapi, Sanity, Contentful, Supabase, a Next.js API route) | Variable `NEWS_WEBHOOK_URL`, secret `NEWS_WEBHOOK_TOKEN` (sent as `Bearer`). Receives JSON with `title, slug, excerpt, meta_description, tags, sources, status, body_markdown, body_html, published_at`. |

## Run locally

```bash
cd news-bot
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...          # optional: SERPAPI_KEY=...
python -m newsbot --dry-run           # print articles, publish nothing
python -m unittest discover -s tests  # offline tests, no keys needed
```

## Tuning (`config.toml`)

- `trends.geos`: which countries' Trending Now lists to scan.
- `watchlist.keywords`: AI tools and competitors to watch for spikes. Add new ones any time.
- `topics.include` / `topics.exclude`: plain-English description of the beat. Claude follows it.
- `bot.max_articles_per_run`: cap per hourly run (default 2, so at most ~48 a day; in practice far
  fewer, since most hours have no qualifying AI spike).
- `bot.model` and the `*_effort` settings: quality vs cost per step.

## Cost (rough)

- Claude: a selection call each hour is small. Each article is one research call (with up to 8 web
  searches, billed per search on top of tokens) and one writing call. Check real numbers in the
  Anthropic console after the first day and lower `research_effort` / `max_web_searches` if needed.
- SerpApi: about 8 searches per watchlist check. `watchlist.every_hours = 4` keeps it near 1,500 a
  month. Raise it to check less often.

## Things to know

- **Start in draft mode.** Auto-written news can still get a detail wrong, and Google's spam policies
  penalize mass-produced pages that add little value. A quick human skim before publishing protects
  both rankings and the brand. Switch `PUBLISH_STATUS` to `publish` once the drafts look consistently good.
- The Trending Now RSS feed and SerpApi are not official Google APIs, so Google can change them.
  Failures are logged and the run continues with whatever sources still work. Google has an official
  Trends API in limited alpha; it could replace SerpApi later.
- Every post links its sources, and the writer is told to stay factual and fair about competitors.
