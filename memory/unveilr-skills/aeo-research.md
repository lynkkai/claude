---
name: aeo-research
description: Deep AEO topical research for a client. Discovers article opportunities, AI prompt gaps, keyword volumes, cannibalization risks, competitor coverage, and user journey patterns. Outputs a prioritized article plan with prompt tracking recommendations.
---

<!-- Provenance: Unveilr platform registry · category=research · version=1 · scope=global · synced 2026-08-25 -->

# AEO Topical Research

You are an AEO research specialist. Your job is to perform exhaustive topical research for a client's content pillar and output a prioritized article plan with AI prompt mapping.

**Read these files before starting:**
- `.claude/aeo-best-practices.md` - AEO scoring rubric and citation factors
- `.claude/api-keys.md` - DataForSEO, Serper, Jina credentials
- Client context file (e.g., `.claude/clients/vakilsearch.md`) - GSC access, competitors, brand voice


## ⛔ HARD RULE A — Resolve the market from the project. Never assume India.

This skill was written India-first and still shows `location_code: 2356` / `gl=in` in its examples. **Those are examples, not defaults.** Before any API call, resolve the client's market and use it everywhere — search volume, related_keywords, SERP, autocomplete.

| Client market | `location_code` | `gl` | `language_code` |
|---|---|---|---|
| India | 2356 | in | en |
| **UAE (Aviaan)** | **2784** | **ae** | **en** |

Running an AE client at 2356 returns Indian demand for UAE topics and silently invalidates the whole brief. Where an MCP tool exposes `country`, pass it explicitly rather than relying on the project default, and check `resolved_market` in every response before trusting a number.

**Acronym collision.** Geo-anchor every autocomplete seed. Bare seeds cross markets: `rera` returns Maharashtra results, and `difference between bookkeeping and accounting` returns Indian syllabus queries (*class 11, TS Grewal, CA Foundation*) even at `gl=ae`. A seed that returns the wrong country's intent is a discarded seed, not a finding.

## ⛔ HARD RULE B — Step 2 must output a QUERY FAN-OUT, not just a keyword list

Keyword volumes alone do not produce an article outline. The deliverable of Step 2 is a **fan-out of 6–9 question-form sub-queries per topic**, because those become the H2s under the `prompt-led-article` contract (H1 = tracked prompt verbatim, H2s = its fan-out). Load `prompt-led-article` and follow its source ladder:

| # | Source | Tool | Reliability |
|---|---|---|---|
| 1 | Query fan-out | `get_chatgpt_qfo` — **never `_batch`** | Query list often empty; `retrieved_urls` + `response_text` are the payload |
| 2 | People Also Ask | `search_serp` → `people_also_ask`, **harvested from `us`/`gb`** | Empty in IN and AE; fires normally in US/GB |
| 3 | Autocomplete | `get_autocomplete_suggestions` | Reliable but thin; short geo-anchored stems only |
| 4 | SERP decomposition | `search_serp` organic titles + top-3 H2s | Always available; the dependable fallback |
| 5 | GSC | `get_gsc_page_queries`, `get_gsc_top_queries` | Best evidence of real phrasing |

> **Superseded 2026-08-31 — both "failures" were method errors.** The 27 Aug run (QFO 0/6, PAA 0/6) was re-diagnosed on the same six prompts:
>
> - **QFO:** `get_chatgpt_qfo_batch` returns ONLY the query list and silently drops `retrieved_urls` and `response_text`. The single `get_chatgpt_qfo` on an identical prompt returns both. Batch is what made QFO look dead — never use it for research.
> - **PAA:** the parser is fine. Empty for AE on both a long question AND a short keyword seed, then 4 questions from the SAME tool at `country=us`. Harvest from `us`/`gb`, localise the answers, and tag each question with the market it came from.
>
> Autocomplete caveat stands: long seeds return "No Search Results"; use short geo-anchored stems. DataForSEO also rejects keywords over 10 words.

A brief is **not green** unless every topic in it carries a sourced fan-out of at least 6 question-form sub-queries, each tagged with the source that produced it. Dead headings ("Key considerations", "Cost drivers") are not fan-out queries and must never enter the brief.

## ⛔ HARD RULE C — A prompt is a sourced, screened, deduped artifact. Never a template fill.

Step 6 used to be the only step in this skill with no tool call: volumes were audited to the API while the
prompts — the actual deliverable — were invented from seven templates. **No prompt enters the brief without
all five fields below recorded against it.** A brief carrying an unscreened prompt is 🔴 RED, not amber.

| # | Field | How it is obtained | Fails if |
|---|---|---|---|
| C1 | **Provenance** | one of: `get_chatgpt_qfo` (single) `response_text` / `retrieved_urls` · PAA harvested at `us`/`gb` · `get_autocomplete_suggestions` · a GSC query · a live client service page | no source named → drop the prompt |
| C2 | **Winnability class** | `/topic-score` G5 shape table (below) | unlabelled → drop |
| C3 | **Answer shape** | single `get_chatgpt_qfo`, read `response_text` + `retrieved_urls` | not probed → drop |
| C4 | **Collision** | normalized fuzzy match against every tracked prompt for the project (Step 1 already fetched them) | near-duplicate → drop, name the incumbent |
| C5 | **Hygiene** | `client-prompt-set-report` R5 + R6 | any breach → rewrite or drop |

### C2 — the winnability screen (`aeo-best-practices.md` PART G1, 530 measured searches)

ChatGPT searches the web only when the question smells like it needs current facts. If it answers from memory,
**no page can be cited — the contest never happens.**

| Prompt shape | ChatGPT searches | Class |
|---|---|---|
| contains a year ("…in 2026") | ~100% | `winnable` |
| "best…" / "top…" | 92% | `winnable` |
| price / cost / fees | 87% | `winnable` |
| names a city | 84% | `winnable` |
| "what is…" / "how to…" | **37%** | `low-winnability` |
| general informational | **18%** | `low-winnability` |

`low-winnability` prompts are **not killed** — they may be excellent SEO targets. What is killed is the
*promise*: never carry one into a client deck, a coverage metric or a prompt-tracking recommendation as an
AI-visibility play. Offer the re-angle instead — give the definitional prompt a year, a price, a city or a
superlative, where the client fence allows it.

### C3 — the answer-shape probe decides whether an article is even the right instrument

Read `response_text` from the single QFO call and classify what the engine actually returns:

| Answer shape returned | Instrument |
|---|---|
| Prose explainer | ✅ on-domain page can win — brief it |
| **Local business listing** (names + street addresses) | ⚠️ citation is going to entity/local signals — GBP, address, structured data. **An article will not win this.** Route accordingly and say so. |
| **Ranked third-party comparison table** (directories, "top 10" pages) | ⚠️ retrieval set is third-party *ranking* pages, not vendor service pages (G7: own domain loses ~2 of 3 head-to-heads unbranded). Route to earned media / getting named in the pages already cited. |

*Measured on Aviaan, 31 Aug 2026: P2 "which firm carries out a liquidation valuation" returned a local
listing; P6 "top valuation companies" returned a ranked table built from Clutch.co and a competitor's
screening guide. Aviaan appeared in none of the three answers. Retargeting the pages could not have won
either — a structural fact no amount of writing quality changes.*

Also capture, per prompt, the **G2 rewritten search line** — the query ChatGPT actually typed, which drops
~half the human's words and adds "2026", the country, "official", "reviews", "fees". Titles get written
against that line, not the human phrasing. It is the strongest controllable lever measured (top-3 chance
~15% → ~35%).

### C4 — prioritisation order (highest value first)

1. **Tracked · not cited · page already exists** → retarget via `/prompt-led-article`. Cheapest win in the file; Step 1 already fetched `is_cited` / `is_mentioned` per platform, so use it.
2. **Untracked · `winnable` · no page** → new article + `create_prompt`.
3. **Untracked · `winnable` · answer shape is listing/ranked-table** → earned-media route, no article commissioned.
4. **`low-winnability`** → SEO column only, labelled, never sold as AI visibility.

Check the project's plan entitlement (market scope and tracked-prompt quota) before recommending additions.
Proposing prompts the plan cannot track is a wasted recommendation.


---

## Input

$ARGUMENTS

Parse for:
- **client**: Client name (required) — determines which `.claude/clients/<client>.md` to read
- **pillar**: Topical pillar to research (required) — e.g., "trademark", "GST", "company registration"
- **project_id**: Unveilr project UUID (optional) — for fetching tracked prompts from prod DB
- **depth**: "quick" (3-4 batches, ~30 min) or "deep" (8-12 batches, ~60 min). Default: "deep"

## Research Workflow (8 Steps)

### Step 1: Context Gathering
- Read client context file (`.claude/clients/<client>.md`)
- Read topical map if it exists (e.g., `VakilSearch_Topical_Map.md`)
- Read any existing research docs for this pillar
- Fetch tracked prompts from prod DB (if project_id provided):
  ```bash
  kubectl config use-context gke_astroyaar_asia-south1_astroyaar-autopilot
  PROD_POD=$(kubectl get pods -n unveilr -l app=backend --no-headers | grep Running | head -1 | awk '{print $1}')
  kubectl exec -n unveilr $PROD_POD -c backend -- timeout 15 python3 -c "
  from app.database import SessionLocal
  from app.models.prompt import Prompt
  db = SessionLocal()
  prompts = db.query(Prompt).filter(Prompt.project_id == '<project_id>').all()
  for p in prompts:
      print(p.prompt_text)
  db.close()
  "
  ```
- **Check AI citation status for relevant prompts** — this is critical for identifying where the client is/isn't being cited:
  ```bash
  kubectl exec -n unveilr $PROD_POD -c backend -- timeout 60 python3 -c "
  from app.database import SessionLocal
  from app.models.prompt import Prompt
  from app.models.ai_query_result import AIQueryResult
  from sqlalchemy import desc
  db = SessionLocal()
  # Models: Prompt (id, prompt_text), AIQueryResult (prompt_id, platform, is_mentioned, is_cited, query_date)
  # AIMention (prompt_id, brand_name, brand_key, mention_type, citation_urls)
  # Filter prompts by relevant keywords, then check latest AIQueryResult per platform
  prompts = db.query(Prompt).filter(Prompt.project_id == '<project_id>').all()
  relevant = [p for p in prompts if any(kw in p.prompt_text.lower() for kw in ['<topic_keywords>'])]
  for p in relevant:
      results = db.query(AIQueryResult).filter(AIQueryResult.prompt_id == p.id).order_by(desc(AIQueryResult.query_date)).limit(4).all()
      platforms = {}
      for r in results:
          if r.platform not in platforms: platforms[r.platform] = r
      cited = [pl for pl, r in platforms.items() if r.is_cited]
      absent = [pl for pl, r in platforms.items() if not r.is_mentioned]
      print(f'{'CITED' if cited else 'ABSENT'} | {p.prompt_text[:75]}')
      if cited: print(f'  Cited: {cited}')
      if absent: print(f'  Absent: {absent}')
  db.close()
  "
  ```
  **Note:** The model is `AIQueryResult`, NOT `PromptRun` (which does not exist). Columns: `id, project_id, prompt_id, platform, query_text, location, query_date, is_mentioned, is_cited, mention_snippet, response_text, citations, citation_count, sentiment, sentiment_score, model_name, input_tokens, output_tokens, cost, created_at`. AIMention columns: `id, ai_query_result_id, project_id, prompt_id, query_date, brand_name, brand_key, mention_type, mention_context, position_in_text, citation_urls, created_at`.

### Step 2: Question-Form Keyword Discovery (DataForSEO)
Run 8-12 keyword batches (10 keywords each) to discover what people search/ask:

**Batch categories** (adjust to the pillar topic):
1. "how to [pillar action]" — process questions
2. "what is [pillar concept]" — definitional questions
3. "difference between [X] and [Y]" — comparison questions
4. "can I / do I need / is it mandatory" — yes/no decision questions
5. "[pillar] for [industry/entity type]" — use-case questions
6. "[pillar] fees / cost / charges" — pricing questions
7. "[pillar] class / category / type" — classification questions
8. "section [N] [relevant act]" — legal section questions (for legal topics)
9. "[pillar] [post-action: renewal, transfer, amendment]" — lifecycle questions
10. "[pillar] [problem: objection, opposition, infringement]" — problem-aware questions

**For each batch**, use:
```bash
curl -s -X POST "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live" \
  -H "Authorization: Basic <credentials from api-keys.md>" \
  -H "Content-Type: application/json" \
  -d '[{"keywords": [...], "location_code": <RESOLVED>, "language_code": "en"}]'  # 2784 for Aviaan/AE — see Hard Rule A
```

**Also run related_keywords** for top 5 seeds (highest volume keywords from batches):
```bash
curl -s -X POST "https://api.dataforseo.com/v3/dataforseo_labs/google/related_keywords/live" \
  -H "Authorization: Basic <credentials>" \
  -H "Content-Type: application/json" \
  -d '[{"keyword": "<seed>", "location_code": <RESOLVED>, "language_code": "en", "limit": 20}]'
```

**Max 10 keywords per batch** (DataForSEO fails with larger batches on some accounts).

### Step 2b: Google Autocomplete Expansion (PAA Substitute)

**PAA is market-specific, not unavailable — corrected 2026-08-31.** It is reliably empty for **India** (`2356`/`in`) and the **UAE** (`2784`/`ae`), and reliably present for **US/GB** through the same `search_serp` tool. The earlier "PAA is not available" finding was drawn from AE/IN runs only and is wrong as a general statement.

**Method:** run the PAA pass in `us` (or `gb`), harvest the question set, then localise every answer to the client's market and re-validate volumes at the client's `location_code`. PAA questions are largely market-independent; the answers are not. Tag each harvested question with its source market in the brief.

**Worked example (Aviaan, 31 Aug 2026):** `how to value a business` at `country=us` returned *"Is a business worth 3 times profit?"*, *"How much is a business worth with $500,000 in sales?"*, *"How many times earnings is a business worth?"*, *"How much is a business worth that makes $300,000 a year?"* — four of Aviaan's own tracked prompts, near-verbatim. That is also the likely provenance of those prompts, and it explains why they carry US phrasing and no UAE search volume.

Autocomplete remains a useful *supplement* to PAA, not a substitute for it. DataForSEO `keyword_suggestions` does still return empty keyword strings for India.

**Use Google Autocomplete API instead** — it reliably returns 8 suggestions per query for India:

```python
import urllib.request, json
url = f'https://suggestqueries.google.com/complete/search?client=firefox&q={urllib.request.quote(seed)}&gl=<RESOLVED>&hl=en'  # ae for Aviaan — see Hard Rule A
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
suggestions = json.loads(resp.read())[1]
```

**Use question-prefix seeds to discover PAA-equivalent questions.** These patterns work especially well for discovering high-AI-query keywords with zero Google volume:

| Prefix Pattern | What It Discovers | Example |
|---|---|---|
| `"do i need a [service] for"` | Decision questions → gateway to service | "do i need a lawyer for consumer court" |
| `"which [service] for"` | Selection questions → service page traffic | "which lawyer for property" |
| `"can i [verb] without [service]"` | DIY vs hire questions → conversion content | "can i send legal notice without lawyer" |
| `"how to check [service provider]"` | Trust/verification questions | "how to check lawyer registration" |
| `"[service] for [specific situation]"` | Situational needs → high commercial intent | "lawyer for cheque bounce case" |
| `"[service] near me"` | Local intent | "lawyer for property registration near me" |

**After collecting autocomplete suggestions**, batch them through DataForSEO search volume endpoint for actual volumes. Many will show 0 Google volume but have 10-20x AI query volume — still worth creating content for.

**This step typically discovers 30-50 additional keyword candidates that DataForSEO's related_keywords endpoint misses entirely.**

### Step 3: GSC Cannibalization Check
Fetch a fresh GSC token from dev pod, then check which keywords the client already ranks for:

```bash
# For each major keyword cluster, check GSC
curl -s "https://searchconsole.googleapis.com/webmasters/v3/sites/<encoded_site>/searchAnalytics/query" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "startDate":"<90_days_ago>",
    "endDate":"<today>",
    "dimensions":["query","page"],
    "dimensionFilterGroups":[{
      "filters":[{"dimension":"query","operator":"contains","expression":"<keyword_stem>"}]
    }],
    "rowLimit":25
  }'
```

**Rules**:
- If service page ranks at pos <10 for a keyword → mark keyword as CANNIBALIZED, do NOT create blog article for it
- If service page ranks at pos 10-20 → consider AEO-optimizing the service page instead of creating new content
- If NO page ranks → GREEN, safe to create new content
- Check each keyword cluster separately, not just the head term

### Step 4: Competitor Coverage Audit
For each topic cluster, check what competitors have:

```bash
# Use Serper API
curl -s -X POST "https://google.serper.dev/search" \
  -H "X-API-KEY: <key from api-keys.md>" \
  -H "Content-Type: application/json" \
  -d '{"q": "site:<competitor_domain> <topic>", "gl": "in", "num": 5}'
```

Check all competitors listed in client context file. For each topic, record:
- Does competitor have content? (YES/NO)
- How many articles?
- Depth (thin/moderate/deep)
- Unique angles they cover that client doesn't

### Step 5: User Journey Analysis
Think through the ICP personas (from client context file) and map their search behavior:

**For each ICP**:
1. What is their trigger event? (starting a business, facing a problem, platform requirement)
2. What do they search first? (upstream query)
3. What do they search when ready to buy? (transactional query)
4. What do they search after buying? (post-purchase query)

**Identify journey patterns** like:
- Platform-Unlock: "Amazon Brand Registry" → needs trademark
- Which-Class: knows they need TM but stuck on classification
- Brand Confusion: searches "brand registration" instead of "trademark"
- Problem-Aware: brand got copied, searching for remedies
- How-to-Start-X: planning a business, doesn't know TM is needed

**Validate patterns with DataForSEO** — check volumes for the upstream/downstream keywords each ICP would search.

### Step 6: AI Prompt Mapping — gated by HARD RULE C

For each content opportunity identified, produce a prompt row carrying **all** of:

| Field | Content |
|---|---|
| Prompt | the exact string, R5-clean (no em/en dash, **no country qualifier** — the scan sets location, no competitor name, no job-seeker token) |
| Google keywords | with DataForSEO volumes, at the resolved market (Hard Rule A) |
| Provenance (C1) | QFO `response_text` / `retrieved_urls` · PAA(`us`/`gb`) · autocomplete · GSC query · client service page — name it |
| Winnability (C2) | `winnable` or `low-winnability`, with the shape that classified it |
| Answer shape (C3) | prose / local listing / ranked third-party table → and therefore the instrument |
| Rewritten search line (G2) | what ChatGPT actually typed — the title gets written against this |
| Tracking status | already tracked (id) · near-duplicate of tracked (name it, drop) · NEW |
| Citation status | from Step 1's `is_cited` / `is_mentioned` per platform — `CITED` / `MENTIONED-NOT-CITED` / `ABSENT` |
| Route | retarget existing page · new article · earned media · SEO-only |

**Do not start from a template list.** Prompts are harvested from C1 sources and then screened; they are not
generated and then justified. The seven India-hardcoded templates that used to sit here (`"How to [action] in
India?"`) were removed on 2026-09-04: they violated Hard Rule A, breached R5's country-qualifier ban outright,
and every one of the seven sat in the 18–37% search-rate band — the skill was manufacturing low-winnability
prompts by construction.

**Where to harvest, in order of yield:**

1. **US/GB PAA on the pillar's head question.** The single richest source of real prompt phrasing. *(Aviaan,
   31 Aug: `how to value a business` at `country=us` returned four of the client's own tracked prompts
   near-verbatim — that is where they had come from.)* Localise the answers, never the question set blindly.
2. **QFO `retrieved_urls` + `response_text`** on prompts you already track — reveals both the sub-questions and
   the answer shape, and surfaces authority sources SERP decomposition misses.
3. **GSC queries at position 11–40 with impressions** — demonstrated demand in the client's own market,
   already in the client's phrasing.
4. **Autocomplete on short geo-anchored stems.**
5. **The client's live service pages** (R6) — a prompt may only claim a capability the site actually publishes;
   regulated designations must appear verbatim on the site first.

**Coverage arithmetic to report:** tracked prompts with no mapped topic in this plan = the uncovered-prompt gap.
That number, not the count of new prompts proposed, is what the client is buying.

### Step 7: Revenue Scoring
Score each opportunity by:

**Revenue Score** = Volume × Purchase Intent Multiplier × (1 + CPC)

Where Purchase Intent Multiplier:
- 1.0 = TRANSACTIONAL (person is ready to buy — "trademark class for restaurant", "register brand name")
- 0.7 = COMMERCIAL (person needs a service — "trademark hearing", "trademark opposition")
- 0.3 = MIXED (some buyers, some researchers — "trademark infringement")
- 0.1 = INFORMATIONAL (mostly educational — "passing off meaning", "section 9 trademark act")

### Step 8: Output Document
Save to `<client>_<pillar>_article_topics_and_prompts.md` with:

1. **Methodology summary** (data sources, batches run)
2. **Complete keyword data** (all batches, organized by tier)
3. **25-30 article topics** ranked by revenue score, each with:
   - AEO-optimized title
   - Target keywords with volumes
   - AI prompts it covers — the **Step 6 table, all nine fields**, Hard Rule C complete
   - Which tracked prompts it maps to, and each one's current citation status
   - NEW prompts to add to tracking (screened + deduped; never a template fill)
   - Competitor coverage status
   - Cannibalization status
   - Action type (CREATE NEW / AEO-OPTIMIZE EXISTING)
   - **Query fan-out: 6–9 question-form sub-queries that will become the H2s, each tagged with the source that produced it (QFO / PAA / autocomplete / SERP / GSC)** — required for the brief to be green (Hard Rule B)
4. **Prompt tracking plan** — current prompts, new prompts to add, and the **uncovered-prompt gap** (tracked
   prompts with no topic in this plan). Split every proposal by route: retarget / new article / earned media /
   SEO-only. Show the `winnable` vs `low-winnability` split honestly — never total them into one
   "AI visibility" number. Check the plan's market scope and prompt quota before proposing additions.
5. **Production schedule** — suggested waves of 5 articles each. Earned-media and SEO-only rows do not enter
   the article schedule; they are separate lines of work.

**Brief status:** 🔴 RED if any prompt in it is missing a Hard Rule C field, 🟡 AMBER if fan-out (Rule B) or
market resolution (Rule A) is incomplete, 🟢 GREEN only when A, B and C are all clean.

## API Keys

Read from `.claude/api-keys.md`:
- DataForSEO: `Authorization: Basic <value>` (use the askstellar credentials if unveilr credits are exhausted)
- Serper: `X-API-KEY: <value>`
- Jina: for page scraping if needed

## Important Rules

- **Never fabricate keyword volumes** — every volume must come from a DataForSEO API call
- **Never fabricate a prompt either** — Hard Rule C applies the same evidentiary standard to prompts that this rule applies to volumes. An unsourced, unscreened prompt is the same defect as an invented volume, and it costs more, because a wrong volume wastes a decision while a wrong prompt wastes a month of production
- **Screen before you commit** (`/topic-score` G5) — a prompt the engine answers from memory cannot be won by any page; check the shape before the budget is spent, not after
- **Always check cannibalization** — a high-volume keyword is worthless if the service page already ranks for it
- **Question-form keywords are the signal** — Google volume for "how to X" is a proxy for 5-10x more AI queries on the same topic
- **Zero-volume keywords can still be valuable** — "Should I register my brand name or logo or both?" has 0 Google volume but is asked thousands of times on ChatGPT
- **Revenue scoring must be honest** — don't inflate informational content as "transactional"
- **Check existing content before recommending new articles** — scrape client's existing pages on the topic via Jina to understand what's already covered
- **Audit ALL existing pages on the topic** — use Serper `site:domain.com/article/ <topic>` to discover existing blog articles, AND `site:domain.com <topic>` for service pages. Then scrape the top ones via Jina to assess content depth (word count, heading structure, FAQ presence). This prevents recommending "create new" when the client already has 5 articles on the topic that just need AEO-optimization.
- **Check for self-cannibalization** — multiple live pages with self-canonicals competing for the same keyword is a common issue. Flag it when found (e.g., 3 live pages for "lawyer consultation" with different pricing).
- **Use `/usr/bin/curl`** — on macOS with zsh, `curl` may resolve to a shell builtin or alias. Always use the full path `/usr/bin/curl` for HTTP calls to avoid "command not found" errors in loops.
