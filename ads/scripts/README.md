# Meta Ad Library API puller

`meta_ad_library.py` pulls competitor ads from Meta's official Ad Library API
(`graph.facebook.com/<version>/ads_archive`) and writes a summary report to `ads/research/`:
top advertisers, hook types, who saw the ads (age, gender, country), what age and gender
advertisers targeted, and the most recently launched ads.

## What the API can and can't see

- **Non-political ads are only returned if they were delivered in the EU.** Ads that ran only in
  India, the US or the UK will not show up. The default countries are therefore EU markets.
- For EU ads, Meta also returns **targeting (age, gender, locations)** and **EU reach by age,
  gender and country**. That's the most useful audience data you can get about competitors.
- The API does **not** return CTA button text or the creative image / video files. Use the
  Ad Library link in the report to view the creative.
- For India / US creative, check the Ad Library website by hand, or use the `meta-ads-library`
  skill once Hyper MCP + Apify are connected.

## One-time setup (about 15 minutes, plus Meta's ID review)

1. Confirm your identity and location for ads at https://www.facebook.com/ID (Meta can take a
   day or two to approve).
2. Create an app at https://developers.facebook.com/apps (type "Business" or "Other").
3. Accept the Ad Library API terms at https://www.facebook.com/ads/library/api.
4. Open the Graph API Explorer (https://developers.facebook.com/tools/explorer), choose your app,
   and generate a **User access token**. No extra permissions are needed for `ads_archive`.
5. For a token that lasts about 60 days instead of 1-2 hours, exchange it at
   https://developers.facebook.com/tools/debug/accesstoken ("Extend Access Token").
6. Add the token to the Claude Code cloud environment as a secret named
   **`META_AD_LIBRARY_TOKEN`** (environment menu in the session title bar, then Edit, then
   Network secrets / environment variables). Start a new session so it's picked up.
   Never paste the token into chat or commit it.

## Run

```bash
python3 ads/scripts/meta_ad_library.py                         # every query in queries.json
python3 ads/scripts/meta_ad_library.py --terms "AI note taker" --countries DE,FR,NL --days 30
```

Options: `--queries <file>`, `--countries`, `--days`, `--out <dir>`, `--api-version`
(default `v23.0`, or set `META_GRAPH_API_VERSION`).

Output: `ads/research/meta-ad-library-<date>.md` (report) and `.jsonl` (raw rows).

## Editing queries

`queries.json` maps a name to a query:

| Key | Meaning |
|---|---|
| `terms` | Search text |
| `search_type` | `KEYWORD_UNORDERED` (default) or `KEYWORD_EXACT_PHRASE` |
| `page_ids` | Up to 10 Facebook page IDs, for exact advertiser lookups |
| `countries` | ISO codes, default 13 EU markets |
| `days` | Only ads delivered in the last N days |
| `active_status` | `ACTIVE` (default), `INACTIVE` or `ALL` |
| `max_ads` | Cap per query, default 300 |

Brand keyword searches also catch other advertisers who mention the brand (for example,
"Fathom alternative" ads). To pull one advertiser exactly, put its page ID in `page_ids`
(the page ID is shown in the raw `.jsonl` output and on the Ad Library page).
