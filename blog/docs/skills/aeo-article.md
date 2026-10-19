---
name: aeo-article
description: Create a deeply researched, AEO-optimized article for any Unveilr project. Handles keyword research (DataForSEO), cannibalization checks (GSC), deep topic research, and article writing with full metadata.
---

<!-- Provenance: Unveilr platform registry · category=content · version=2 · scope=global · synced 2026-08-25 -->

## ⛔ HARD RULE — Every article MUST earn 1–2 INBOUND internal links (not just outbound)

Outbound links from the article are NOT enough. Every article we publish MUST also receive **at least 1–2 INBOUND internal links** — existing, live, topically-relevant pages on the SAME domain that link **TO** this article. Otherwise it launches as an internal-link orphan with ~0 internal PageRank and loses to in-house/competitor pages that sit inside the site's link mesh (diagnosed on the VS CIN cannibalization case, 2026-07-22: our page got 0 GSC impressions vs the in-house page's ~602, decided by inbound links 1 vs 4 — schema was identical on both). This is the INBOUND complement to the outbound link cap and is counted separately.

At/after publish you MUST:
1. Find 1–2 existing, live, topically-adjacent pages on the same domain (sibling cluster pages, the mapped service/collection page, or a related guide).
2. Add a natural, contextual link from EACH of those pages TO this article — descriptive anchor, never "click here", never a duplicate of an anchor already on that source page.
3. Verify the inbound links are live on the source pages (check_urls_liveness / fetch the source) before marking the task done.

If no relevant sibling exists to link from, FLAG it — do NOT silently publish an orphan.


# AEO Article Creator

> **⛔ `~/.claude/scripts/nuyug_catalog_truthcard.py` does not exist on this machine** (verified 4 Sep 2026). Nuyug product claims cannot be machine-verified against the catalog. Verify each spec claim against the live product page by hand, or omit the claim.

You are an AEO (Answer Engine Optimization) article specialist. Your job is to create deeply researched, factually accurate articles that AI engines (ChatGPT, Perplexity, Gemini, Google AI Overviews) will cite.

**Always read `.claude/aeo-best-practices.md` before starting** — it contains the latest scoring rubric and AEO rules.

## ⛔ HARD RULE — NEVER use hyperlinks or URLs that are not live (no 404s, no soft-404s)

Every URL in the article (internal links, external citations, image src, author bio, JSON-LD fields) MUST return HTTP 200 AND must not soft-404 to a generic page. Do NOT bake in "will-be-live-soon" sibling slugs. Before saving the .md, verify every URL via `mcp__unveilr-<brand>__check_urls_liveness` (batches of 20) or HEAD curl. If any URL is dead: replace with a verified-live alternative on the same domain, OR strip the link entirely and convert the anchor to plain text — NEVER ship a `[anchor](dead-url)`. Soft-404 traps: VakilSearch `/blog/*` → homepage (use `/article/...` only); Nuyug unpublished `/blogs/news/<slug>` — forbidden; Care Dale archived product URLs — re-verify each push.

## ⛔ HARD RULE — H2s MUST come from a SOURCED query fan-out, never invented

An answer engine decomposes a question into sub-queries before it answers. Those sub-queries are the **query fan-out**. Making them your H2s means every retrievable chunk is already scoped to one sub-question with its answer in the first sentence. Headings that are not fan-out queries retrieve for nothing, however good the prose beneath them.

**Before you write a single heading you MUST source 6–9 fan-out queries.** Work this cascade in order, stop when you have enough, and record which source produced each query in the handoff:

| # | Source | Tool | Reliability |
|---|---|---|---|
| 1 | Query fan-out | `get_chatgpt_qfo` / `get_chatgpt_qfo_batch` | **Frequently empty — check `qfo_count`, never `status`** |
| 2 | People Also Ask | `search_serp` → `people_also_ask` | Empty outside the US (AE and IN measured empty) |
| 3 | Autocomplete | `get_autocomplete_suggestions` | Reliable but thin; **geo-anchor every seed** |
| 4 | SERP decomposition | `search_serp` organic titles + the H2s of the top 3 | Always available; the dependable fallback |
| 5 | GSC | `get_gsc_page_queries`, `get_gsc_top_queries` | Best evidence of how real users phrase it |

**Blocking conditions — any one of these stops the draft:**
- **Fewer than 6 sourced fan-out queries → STOP and report.** Never invent headings to reach the count.
- **`qfo_count: 0` with `status: "ok"` is a tool success and a research failure.** Fall through to the next source; never record it as "this topic has no fan-out".
- **An empty `people_also_ask` array is normal outside the US.** Fall through to sources 4–5 rather than concluding the fan-out is empty.
- **Bare autocomplete seeds return the wrong market** (`rera compliance` → Maharashtra/Hindi results). Anchor every seed to the client's city/country, and add a disambiguation block to the body where a term collides across markets.
- **Dead headings are a FAIL.** "Key considerations", "Cost drivers and what to expect", "Understanding the basics", "What you need to know" — if it is not a query a real person would type, it does not ship.
- **An H2 the research cannot actually answer gets CUT, not hedged.** A hedging section is worse than an absent one.
- **No near-duplicate padding.** Re-phrasings of the same query stuffed in as separate H2s read as keyword stuffing and dilute the exact-match signal.


## ⛔ HARD RULE — every section's first ~200 CHARACTERS must be citable (the clip rule)

ChatGPT does not read your page. It **clips ~200 characters — about two lines — from each retrieved page:
the stretch that best matches its own search words**, then writes its answer from those clips. A page can be
retrieved, rank well, and still never be cited because the two lines it surrendered contained no facts.

Measured failure (AM-INSIGHTS, 530 recorded searches). A laptop-review page was retrieved; the clip taken was:

> *"Tired of looking for the best laptop under 60000 and not coming to a conclusion? You have come to the
> right place. We have compiled a list…"*

Retrieved, never cited. The page did the hard part and fumbled the last two lines.

**The contract — an "answer paragraph" opening every section:**

> ~2 sentences · carries the section's search words naturally · **one number** · **one concrete claim**.

> *"Private limited company registration in India takes 10–14 days in 2026: name approval, DSC, and
> incorporation via SPICe+; government fees start around ₹1,500, professional fees ₹6,000–15,000."*

**Blocking conditions:**
- **Any section whose first 200 characters contain no number and no concrete claim is a FAIL.** Rewrite the
  opening; do not add a stat lower down and call it fixed.
- **Throat-clearing openers are clip-killers** and do not ship: "In this article we will explore…",
  "Choosing the right X can be overwhelming…", "Let us start with the basics…", "You have come to the right
  place…". This holds even when the section beneath is excellent.
- The existing 40–60 word answer-first capsule satisfies this **only if its own first ~200 characters carry
  the number and the claim** — a capsule that winds up for a sentence and then delivers has already lost the clip.
- Applies to the Quick Answer, every H2/H3 section, and every FAQ answer.

**Self-check before scoring:**

```bash
python3 ~/.claude/scripts/clip_check.py articles/<slug>.md
```

It prints the actual ~200-character clip for every section, flags clips with no numeral and hard-flags
throat-clearing openers. **The numeral flag is triage, not a verdict** — read every clip it prints and judge
the concrete-claim half yourself. Target: **≥50% of section clips carry a number** (median across our shipped
corpus is 36%, so this is a real target, not a formality). Then read only the first two lines of each section,
in order, ignoring everything else — if that sequence does not read as a usable set of answers, the article is
not citable yet.

Full mechanics, bounds and the other nine findings: **`~/.claude/aeo-best-practices.md` PART G**
(first-party, 530 ChatGPT searches, position-controlled). Read PART G before writing.


## ⛔ HARD RULE — screen the topic for winnability BEFORE research (it may be unwinnable)

ChatGPT searches the web only when a question smells like it needs current facts. If it answers from memory,
**no article can win the prompt, however good** — and the month spent writing it is the most common wasted
month in AEO.

| Question shape | ChatGPT searches |
|---|---|
| contains a year ("…in 2026") | ~100% |
| "best…" / "top…" | 92% |
| price / cost / fees | 87% |
| names a city | 84% |
| **"what is…" / "how to…"** | **37%** |
| general informational | **18%** |

A target that is purely definitional — no year, price, city or superlative — is **low-winnability for
ChatGPT citation**. That does not kill it: it may still be a strong SEO or Google-AIO target. But say so in
the handoff and **do not promise AI visibility from it**. `/topic-score` gate G5 enforces this upstream; if
you are writing without a `/topic-score` pass, run the screen here.


## Input

$ARGUMENTS

Parse for:
- **project_id**: Unveilr project UUID (required)
- **topic**: Article topic (required)
- **word_count**: Target word count (optional, default 1800)
- **article_type**: topic-guide / how-to-guide / comparison / ranked-list (optional, auto-inferred from topic)

If project_id is missing, ask for it.

## API Keys

- **Global keys** (DataForSEO, Jina, OpenAI, Novita, Pexels, Serper): All pre-decoded and ready to use in `.claude/api-keys.md`. Do NOT grep from secrets files or ask the user.
- **Client-specific keys** (WordPress, GSC): In `.claude/clients/<brand>.md`
- **GSC access**: Fetch OAuth tokens from dev DB via kubectl — see client context file for exact commands.

---

## PHASE 1: Project Context

Pull brand context from the Unveilr project. Find the running backend pod first:

```bash
kubectl get pods -n unveilr -l app=backend --no-headers | grep Running | head -1 | awk '{print $1}'
```

Then fetch project details (adjust container name - dev pods have `-c backend`, prod pods have `-c backend`):

```bash
kubectl exec -n unveilr <POD> -c backend -- timeout 15 python3 -c "
from app.database import SessionLocal
from app.models.project import Project
db = SessionLocal()
p = db.query(Project).filter(Project.id == '<project_id>').first()
if p:
    print(f'NAME: {p.name}')
    print(f'DOMAIN: {p.domain}')
    print(f'BRAND_NAME: {p.brand_name}')
    print(f'TARGET_LOCATION: {p.target_location}')
    print(f'BRAND_CONTEXT: {(p.brand_context or \"\")[:1000]}')
    print(f'COMPETITORS: {p.competitors}')
    print(f'WRITING_STYLE: {p.writing_style}')
    print(f'CUSTOM_INSTRUCTIONS: {p.custom_instructions}')
    bd = p.brand_details or {}
    print(f'ICP: {bd.get(\"icp\",\"\")}')
    print(f'ICP_AGE: {bd.get(\"icp_age\",\"\")}')
    print(f'CORE_OFFERINGS: {bd.get(\"core_offerings\",[])}')
    print(f'VALUE_PROP: {bd.get(\"value_proposition\",\"\")}')
    print(f'GTM: {bd.get(\"gtm\",\"\")}')
db.close()
"
```

Use this data to build the brand voice context. Also fetch 1-2 existing pages from the brand's site via Jina to understand their writing style:

```bash
JINA_KEY=$(grep JINA_API_KEY Backend/k8s/base/02-secret.yaml | awk '{print $2}')
# Decode if base64: echo "$JINA_KEY" | base64 -d
curl -s "https://r.jina.ai/https://<domain>/<relevant-page>" -H "Authorization: Bearer $JINA_KEY" -H "Accept: text/markdown"
```

---

## PHASE 2: Keyword Research (DataForSEO)

Research keywords using DataForSEO. Determine location_code from project's target_location (India=2356, US=2840, UK=2826).

```bash
# Get creds from codebase
grep DATAFORSEO_CREDENTIALS Backend/k8s/base/02-secret.yaml | awk '{print $2}'
# Decode: echo "<value>" | base64 -d
```

Use Python stdlib (urllib.request) — do NOT use requests library:

```python
import urllib.request, json
CREDS = "<base64 creds>"
BASE = "https://api.dataforseo.com/v3"

# Step 1: Search volumes for 10-15 seed keywords
payload = json.dumps([{"keywords": [...seeds...], "location_code": 2356, "language_code": "en"}]).encode()
req = urllib.request.Request(f"{BASE}/keywords_data/google_ads/search_volume/live",
    data=payload, headers={"Authorization": f"Basic {CREDS}", "Content-Type": "application/json"})
data = json.loads(urllib.request.urlopen(req, timeout=60).read())

# Step 2: Related keywords for top seed
payload2 = json.dumps([{"keyword": "<top seed>", "location_code": 2356, "language_code": "en", "depth": 2}]).encode()
req2 = urllib.request.Request(f"{BASE}/dataforseo_labs/google/related_keywords/live",
    data=payload2, headers={"Authorization": f"Basic {CREDS}", "Content-Type": "application/json"})
```

**Output**: Present keyword table to user with volume + competition. Select:
- 1 primary keyword (highest volume, matches article intent)
- 3-4 secondary keywords (for H2 headings)
- 4-5 long-tail keywords (for H3s and body)

**Wait for user confirmation before proceeding.**

---

## PHASE 3: Cannibalization Check

### 3a. GSC Data (if connected)

```bash
kubectl exec -n unveilr <POD> -c backend -- timeout 45 python3 -c "
from app.database import SessionLocal
from app.models.gsc import GSCProperty, GSCAccount
from app.integrations.gsc.client import GSCClient
from datetime import datetime, timedelta

db = SessionLocal()
prop = db.query(GSCProperty).filter(GSCProperty.project_id == '<project_id>').first()
if not prop:
    print('NO_GSC_CONNECTION')
    exit()
acc = db.query(GSCAccount).filter(GSCAccount.id == prop.account_id).first()
client = GSCClient()
creds = client.get_credentials(acc)
db.commit()

end_date = datetime.utcnow().strftime('%Y-%m-%d')
start_date = (datetime.utcnow() - timedelta(days=90)).strftime('%Y-%m-%d')

data = client.fetch_data(credentials=creds, property_identifier=prop.site_url or prop.property_uri,
    start_date=start_date, end_date=end_date, dimensions=['query','page'], row_limit=2000)

# Filter for topic-related queries and show which pages rank
for row in data.get('rows', []):
    q = row['keys'][0].lower()
    if any(kw in q for kw in [<topic keywords>]):
        print(f'{row.get(\"impressions\",0):>6}imp {row.get(\"clicks\",0):>4}clk pos={row.get(\"position\",0):.1f} {row[\"keys\"][0][:50]} -> {row[\"keys\"][1].replace(\"https://\"+\"<domain>\",\"\")[:45]}')
db.close()
"
```

### 3b. Existing Page Scrape
If GSC shows an existing page ranking for target keywords, scrape it via Jina to understand what it covers. Map ALL headings and content focus.

### 3c. Keyword-Level Cannibalization Decision

**For EACH selected keyword individually** (not just the primary keyword):
1. Check GSC: which existing pages rank for this exact keyword? At what position? How many impressions?
2. If a **service/transactional page** ranks for a keyword → **DROP that keyword** from the article's selected keywords. The blog article should not compete with lead-gen pages. Instead, internally link TO the service page for that keyword.
3. If an **existing blog post** ranks at pos <20 for a keyword → **DROP that keyword** unless the new article covers a fundamentally different angle (e.g., "2026 reforms" vs "general overview")
4. If **multiple existing pages** already compete for a keyword (fragmentation) → **DROP that keyword** to avoid making fragmentation worse
5. If no existing page ranks, or existing pages rank at pos 50+ with near-zero clicks → **SAFE to target**

**After dropping cannibalizing keywords**, find replacement keywords:
- Use DataForSEO related keywords and search volume endpoints
- Look for long-tail variants, "X for Y" queries, year-specific queries
- Prioritise keywords where the brand has ZERO existing coverage (content gaps)

**Update the article's keyword targeting** — frontmatter, H1, title tag, meta description, JSON-LD keywords, and natural body placements — to use only non-cannibalizing keywords.

### 3d. Existing Blog Content Audit
Beyond GSC data, also **web search for existing blog posts** on the same topic:
- `site:<domain>/blog <topic>` to find all existing coverage
- Map what each existing post covers
- Ensure the new article's angle, structure, and keywords are differentiated

Present findings clearly and get user confirmation before proceeding.

---

## PHASE 3.5: Brand Catalog Fact-Verification (E-COMMERCE — MANDATORY, blocks writing)

**Applies to any article that makes a product, material, or price claim about the client brand** — especially "best [category] brands" listicles, brand comparisons, and buying guides. This phase prevents the most damaging error class: stating the brand sells a material / category / price band it does not.

**Hard rules:**
1. **Never inherit a product claim from an existing draft, and never infer it from the brand's headline identity.** "Brand X is known for American Diamond" does NOT mean every category (bracelets, mangalsutra, rings…) is American Diamond. Brand-level USP ≠ per-category truth. Store-wide price range ≠ category price band.
2. **Pull the FULL live catalog (paginate to the very end) before writing the brand's own entry.** A partial / first-page sample is a primary cause of wrong conclusions — a 250-row sample of a 900-product store will misrepresent any category.
3. For **Nuyug**, run the ready-made gate (read-only):
   ```bash
   python3 scripts/nuyug_catalog_truthcard.py --lint <article.md>
   ```
   It paginates all products, prints a per-`product_type` truth card (SKU count, real price band, materials actually present), and flags any material claimed in the brand entry that exists in 0 live categories. Write the brand entry strictly against the truth card for the article's category.
4. For **other e-commerce clients**, query the store API the same way (Shopify Admin `products.json` with `since_id` pagination, or the platform equivalent), grouped by product_type, before writing.

**Gate:** if the brand entry asserts a material, category, or price the live catalog does not support → FIX before writing the rest of the article. This is ALSO a pre-push gate — every `*_push.py` must block on catalog mismatch.

**Output:** paste the category truth card (SKU count, price band, dominant materials) into your working notes, and confirm the brand entry matches it line-for-line.

## PHASE 4: Deep Topic Research

Do comprehensive web research using WebFetch and WebSearch tools. This is the MOST IMPORTANT phase — article quality depends on research depth.

**Minimum research:**
1. 5-7 authoritative web sources on the topic
2. Official government/regulatory portal pages for factual data (fees, forms, deadlines)
3. The brand's own existing content on related topics (for interlinking and voice matching)
4. Competitor articles ranking for target keywords (understand what to beat)
5. Cross-verify ALL facts across multiple sources

**Research standards:**
- Every statistic must have a verifiable source
- Legal/regulatory references must include exact section/rule numbers
- Government fees must be verified against official .gov sources
- Timelines must reflect real-world current processing times, not textbook answers
- Form/document references must be exact (official form numbers, not descriptions)
- If sources disagree, note both versions and use the more authoritative one

**Research quality gate (MANDATORY):**
After research is complete, evaluate whether you have enough data for the article's CORE claims:
- If the topic requires specific pricing/fee data and research finds NONE → **STOP and report to user**. Do not invent pricing. (Example: "CA Fees for Tax Filing" — if no source publishes actual CA fees, abort.)
- If core factual data is missing for >50% of planned sections → **STOP and report**
- If research only found competitor content and zero authoritative/government sources → **flag to user** before proceeding

**Organize research as:**
- Factual anchors (verified data points with sources)
- Content gaps (what competitors miss that this article should cover)
- Interlinking opportunities (brand's existing pages to link to)

---

## PHASE 5: Article Writing

Write the article yourself based on all research. This is NOT a summary — it's a comprehensive, deeply researched piece.

**Follow ALL rules from `.claude/aeo-best-practices.md`**, especially:

### Structure
- H1: Primary keyword + year + geographic qualifier
- **H2s: the sourced fan-out queries from the Fan-Out Hard Rule, 6–9 of them, in question format. No dead headings.**
- Every H2/H3: Opens with direct answer in first 2 sentences (40-60 words)
- Sections: 120-200 words, self-contained (Information Island test)
- Paragraphs: 2-3 sentences max
- Tables for comparisons/fees/timelines, bullets for lists, numbered lists for processes
- If outline promises N stages/steps, body MUST deliver all N (no gaps)

### Content
- ANSWER-FIRST mandatory for every section
- Cite sources with inline [N] markers
- Unsourced quantitative claims get "(industry estimate)"
- Brand mentions: 1-2 times MAX in body, never in FAQs
- Include "what happens after" / post-completion section (commonly missed)

### Internal Linking (MANDATORY — 8-14 links for ~2500 word articles)
Every article must include **8-14 internal links** to related pages on the same domain. This is critical for both SEO (topical authority signals) and AEO (clustered content receives 3.2x more AI citations than standalone posts). 4-5 links is NOT enough for a comprehensive guide.

**Three categories of internal links (all required):**

**Category 1: Cross-links to sibling articles (HIGHEST PRIORITY)**
Every article in a topic cluster MUST link to its sibling articles. If you are creating Article 4 in a set of 7, it must link to at least 2-3 of the other 6. Check the client's "Articles Created" table and the topical map for siblings.
- Read the client context file's "Articles Created" table to find all published/pending articles
- For each sibling article, find a natural phrase in the body where a cross-link fits
- Use topic-descriptive anchor text: "types of lawyers in India" not "our other article"
- These links create a content cluster that AI engines recognise as topical authority

**Category 2: Links to service/pillar pages**
- Link to the **pillar/parent page** at least once (e.g., "trademark registration" → `/trademark-registration`)
- Link to **2-3 related service pages** where the reader might convert (e.g., `/lawyers/property-lawyers`, `/mutual-divorce`, `/send-legal-notice`)
- Use `site:<domain> <topic>` via Serper to discover existing service pages

**Category 3: Links to existing blog articles**
- Link to **existing blog articles** that cover sub-topics mentioned in your article
- Use `site:<domain>/article/ <topic>` via Serper to discover existing blog posts
- E.g., if mentioning "legal notice", link to the existing `/article/how-to-send-a-legal-notice-in-india/`

**How to implement:**
- Use natural descriptive anchor text, not "click here" or bare URLs
- Weave links into existing sentences — do not create new sentences just for links
- Place links where the reader would naturally want more detail on a sub-topic
- Check the project's topical map (if available) to identify sibling articles
- Anchor text must NOT contain the brand name — use topic descriptions only
- **After writing, verify the cross-link matrix:** does this article link to every sibling article at least once? If not, add the missing links.

**Self-check after writing:**
- [ ] Links to pillar page: at least 1
- [ ] Cross-links to sibling articles: at least 2-3
- [ ] Links to service pages: at least 2-3
- [ ] Links to existing blog articles: at least 1-2
- [ ] Total internal links: 8-14 range
- [ ] No anchor text contains brand name
- [ ] No broken links to pages that don't exist

### Formatting Rules (MANDATORY)
- **Acronyms**: ALL acronyms must be fully capitalised — DPIIT, LLP, OPC, EMD, SIDBI, CBDT, PAN, ITR, NSWS, AIF, FSSAI, FoSCoS, MSME, WIPO, GST, etc. Never write lowercase acronyms in prose (exception: SEO keyword anchors like "dpiit recognition" that are deliberately lowercase for keyword matching).
- **Currency**: Indian Rupees must ALWAYS use the ₹ symbol, never "Rs" or "Rs." or "INR". No space between ₹ and the number: ₹4,500, ₹10,000 crore, ₹100 per day. This applies to body text, tables, FAQs, and JSON-LD schema.

### Brand Voice
- Use project's writing_style and custom_instructions from Phase 1
- Match tone from the sample page fetched via Jina
- Default: professional yet approachable, active voice, short sentences, no jargon without context

### FAQs

**FAQ questions must be driven by real search data, not invented.** Before writing FAQs:
1. Use DataForSEO related keywords endpoint for the article's primary keyword to find what people actually search
2. Use DataForSEO search volume endpoint to check volumes for candidate FAQ questions (e.g., "trademark class for restaurant", "fssai license for cloud kitchen", "dpiit certificate download")
3. Prioritise high-volume question-format queries and "X for Y" queries (e.g., "trademark class for food" at 720 SV >> "how many trademark classes" at 0 SV)
4. **Use Google Autocomplete for PAA-equivalent questions** (DataForSEO SERP and Serper do NOT return PAA for India). Run question-prefix seeds through autocomplete to discover what people actually ask:
```python
import urllib.request, json
seeds = ["do i need a [topic] for", "can i [verb] without [topic]", "which [topic] for", "how to choose [topic]"]
for seed in seeds:
    url = f'https://suggestqueries.google.com/complete/search?client=firefox&q={urllib.request.quote(seed)}&gl=in&hl=en'
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    suggestions = json.loads(urllib.request.urlopen(req).read())[1]
```
These autocomplete questions often have zero Google volume but massive AI query volume — they are ideal FAQ candidates.

**FAQ answers must surface information not already covered in the body.** Do not restate, paraphrase, or summarise what the body already explains in full. Each FAQ answer should either:
- Address an angle or edge case the body does not cover (e.g., what happens when X fails, whether rule Y applies to entity type Z)
- Provide a specific actionable answer to a practical question a first-time reader would ask after reading the body
- Clarify a common misconception not addressed elsewhere
- Answer a high-volume search query that the body structure does not directly address

**Self-check: for each FAQ, ask "Is this answer already in the body?"** If the answer is substantially covered in any body section, REPLACE that FAQ with a different question. Common violations:
- FAQ restating the fee table that already exists in body
- FAQ summarising a "types" section already covered in full
- FAQ repeating processing timeline data from a dedicated section
- FAQ paraphrasing eligibility criteria already in a table

FAQs that merely echo body content in shorter form add no value and will be flagged during quality review.

- 6-8 Q&A pairs
- Each answer: 40-80 words, self-contained, leads with direct answer (AI extracts first 50-60 words)
- Include at least 1 specific data point per answer
- NO brand mentions in answers
- Cover: direct-answer, comparison/decision, process/how-to question types

### Metadata (generate alongside article)
- **meta_title**: Max 60 chars, lead with primary keyword + year, include geographic qualifier

> **⚠️ REFINED 2026-09-02 (AM-INSIGHTS / PART G4) — the on-page title and `meta_title` are different contests.**
> The ≤60-char rule above is a *Google-rewrite* heuristic and stands for `meta_title`. The **on-page title /
> H1** is what ChatGPT matches, and there the measured sweet spot is **13–15 words** (24+ words is the worst
> bin) written as **one natural sentence**, not a keyword chain.
>
> Also measured, and binding on both fields:
> - **Never put "Official" in a title.** Pages saying "official" are cited **5× less** (13% vs 61%).
> - **"Best/Top 10" styling** is placed higher but **cited less at equal position** — use it only when the
>   SERP format genuinely demands a ranked list.
> - **The year is a trade-off, not a free win** — it helps discovery on recency-flavoured prompts and
>   slightly hurts citation. Keep it on contested/recency prompts; on an evergreen prompt, dropping it from
>   the H1 is defensible. `meta_title` keeps the year per client rule. **Slugs stay evergreen regardless.**
> - **Write the title against the search ChatGPT types, not the question the human typed.** ChatGPT drops
>   ~half the user's words and adds its own ("2026", the country, "reviews", "fees"). Matching the *rewritten*
>   line moves top-3 chances **~15% → ~35%** — worth roughly as much as brand fame. Capture the line with
>   `get_chatgpt_qfo` (the single tool, never `_batch`) during research and write the title against it.
- **meta_description**: 150-160 chars, first 70 chars = answer/value prop, include 1 data point
- **suggested_url**: SEO slug, max 7 words, lowercase, hyphenated
- **tldr**: 2-3 sentences (50-80 words), captures key value + main takeaways

### Schema
Plan the JSON-LD:
- Article (+ LearningResource for educational content)
- FAQPage (matching visible FAQ section)
- HowTo (for step-by-step — include step array with position, name, text)
- BreadcrumbList (Home → Article)
- Organization (publisher)
- Service + OfferCatalog (if article mentions pricing)
- Use proper entity @types: GovernmentOrganization, Legislation, Service, DefinedTerm
- Include `teaches` array, `about`/`mentions` entities
- **NEVER nest `@type: Product` inside Article's `about` / `mentions` / `isPartOf` arrays.** Google parses every nested `Product` node independently and the Product structured-data validator demands `offers`, `review`, or `aggregateRating` — which an Article page legitimately lacks. Result: GSC Product Snippets report flags the page (real incident: Care Dale `postpartum-hair-fall-hard-water-cities-india`, May 2026). Use `@type: Thing` (preferred) or `@type: Brand` with the same `name` instead. Reserve `@type: Product` for actual product PDP pages where `offers` + `aggregateRating` exist.
- datePublished = dateModified = today's date
  > **⚠️ REFINED 2026-09-02 (PART G8).** Correct for a genuinely new article. On a **refresh**, move
  > `dateModified` only when the content actually changed — a visible "Updated…" line on a page that is
  > really old is the **worst measured combination**: at equal position, stale-dated pages are cited *less
  > than undated ones*. Refresh the content and the date together, or move neither.
- inLanguage based on target market

---

## PHASE 5.5: Multi-Round Factual Verification (MANDATORY — 3 rounds, do not skip any)

After writing, run THREE mandatory verification rounds. Each round catches errors the previous one missed or introduced. Combining or skipping rounds defeats the purpose.

**Why 3 rounds?** In testing, single-round verification introduced new errors 40% of the time — verifiers trusted secondary sources that contradicted the primary source, or "corrected" correct data to wrong data. Multi-round catches these loops.

---

**ROUND 1 — Primary Source Verification**

For every factual claim, fetch the PRIMARY source and compare directly. Do NOT rely on secondary sources (blog posts, law firm summaries, news articles) — they copy each other's errors and create contradiction loops.

**CRITICAL: You MUST actually fetch and read the source page — do NOT rely on your training data.** Your training data is stale and frequently wrong on:
- Government programme statistics (beneficiary counts, scheme details change quarterly)
- Helpline numbers and which organisation operates them
- Legal section text (you often hallucinate what a section says vs what it actually says)
- "Percentage increase" claims (you round up for dramatic effect — 217% becomes "over 300%")
- Count statistics ("1.7 million lawyers" was correct in 2013, wrong by 2023)

**For EVERY claim, you must do one of:**
1. Fetch the official page via Jina: `/usr/bin/curl -s "https://r.jina.ai/<url>" -H "Authorization: Bearer <jina_key>" -H "Accept: text/markdown"`
2. Fetch via WebFetch tool if available
3. Search via WebSearch for the latest figure and verify against 2+ sources

**Never write "VERIFIED" based on your training data alone.** If you cannot fetch a source, mark the claim as "COULD NOT VERIFY" and flag it for manual review. It is better to flag 20 claims as unverified than to rubber-stamp one wrong number.

| Claim Type | Primary Source | How to Verify |
|---|---|---|
| Government fees | Official government fee schedule page | Jina scrape of the actual .gov.in page |
| Legal section text | India Code (indiacode.nic.in) or Indian Kanoon | Jina scrape → search for exact section number → read the actual text |
| Programme statistics | Programme's own website (e.g., tele-law.in, nalsa.gov.in) | Jina scrape → look for "beneficiaries" or "total" or latest annual figure |
| Helpline numbers | Official programme page or .gov.in source | Jina scrape → confirm which organisation operates the number |
| "X% increase" claims | NCRB, RBI, or relevant authority's data report | Jina scrape or WebSearch → find the base year and current year numbers, calculate yourself |
| Company/entity counts | Official annual report, ministry data, BCI for lawyers | WebSearch for latest year's figure → verify against 2 sources |
| Platform features | Platform's own official page (e.g., sell.amazon.in) | Jina scrape of the actual feature page |

**Rules:**
- If primary source is down, try `r.jina.ai/<url>`. If still down, use 2+ independent secondary sources that directly quote the primary, and note this in the verification output.
- If a secondary source contradicts the primary source, **PRIMARY WINS. Always.**
- If two secondary sources disagree and primary is unavailable, DO NOT pick a side — mark the claim as "(unverified — primary source unavailable)" in the article body.
- Every number, section reference, class description, fee, and timeline gets checked individually.
- **For legal section references: read the ACTUAL section text, not a summary.** "Section 35(1) permits self-representation" is wrong if Section 35(1) actually lists who can file complaints. Read the words of the section.

Output: table of VERIFIED / ERROR / UNVERIFIABLE for each claim.
**Fix all ERRORs immediately before proceeding to Round 2.**

---

**ROUND 2 — Completeness and Nuance Check**

This round does NOT re-verify Round 1 claims. It asks: "Is the article misleading by omission?"

- For every **rule or policy change**, search for **exceptions and edge cases**
- For every **edition/version** referenced, verify ALL relevant changes are captured
- For every **categorical statement** ("all X belong to Y"), verify no sub-categories break the rule
- For every **fee table**, verify all applicant types are covered (individual, startup, MSME, company, LLP, physical vs e-filing)
- Ask: *"What does the source say that my article does NOT say?"*

Output: list of MISSING items. Add them to the article.

---

**ROUND 3 — Internal Contradiction Scan**

Read the article top-to-bottom one final time. Check:

- **Body vs body**: Does the article state different numbers for the same fact in different sections? (e.g., "6-18 months" in one place, "8-12 months" in another without qualification)
- **Table vs prose**: Does a comparison table contradict the paragraph below it?
- **FAQ vs body**: Does a FAQ answer contradict or conflict with a body section?
- **Schema vs body**: Do JSON-LD FAQ answers match visible FAQ answers word-for-word?
- **Stale corrections**: If Round 1 fixed a number, is it fixed in ALL occurrences (body, tables, FAQs, schema, citations)?

Output: list of contradictions. Fix all.
**If Round 3 produces fixes, re-run Round 3** to verify the fix did not create new contradictions.

---

**ROUND 4 — Heading Keyword Cannibalization Check (GSC)**

For every H1/H2/H3 heading, extract the primary keyword phrase and check GSC to see if an existing client page already ranks for it:

```bash
curl -s "https://searchconsole.googleapis.com/.../searchAnalytics/query" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"startDate":"...","endDate":"...","dimensions":["query","page"],"dimensionFilterGroups":[{"filters":[{"dimension":"query","operator":"contains","expression":"<heading_keyword>"}]}],"rowLimit":3}'
```

| GSC Result | Risk | Action |
|---|---|---|
| Service page ranks pos <10 | RED | Differentiate heading — add "Do You Need" / "How to Choose" / "Guide to" prefix to avoid competing with service page |
| Blog/article ranks pos <10 | RED | Consider AEO-optimizing existing article instead of creating new |
| Directory/city pages rank pos <10 | YELLOW | Usually different intent (transactional vs informational) — safe if heading is clearly informational |
| WRONG page ranks (0 clicks) | GREEN | New article will capture this properly — good opportunity |
| No page ranks | GREEN | Safe to publish |

**Common false positives:** Service pages (/trademark-registration, /mutual-divorce) ranking for head terms do NOT cannibalize with blog articles that target "How to [verb]" or "Do I need [noun] for [situation]" — the intent is different. Only flag when the article heading targets the SAME intent as the ranking page.

**IMPORTANT: Always verify "wrong page" claims by scraping.** When GSC shows a page ranking for an apparently unrelated query, do NOT assume it is a wrong page based on the URL alone. Scrape the page via Jina and read its headings/content. Sometimes a page titled "Legal Drafting" actually contains a section about types of lawyers. Verify before asserting.

---

---

**ROUND 5 — Grammar, Language, and Readability Check**

Read the entire article as a native English reader would. Check for:

**Grammar and syntax:**
- Subject-verb agreement errors
- Dangling modifiers and misplaced clauses
- Run-on sentences (split any sentence over 50 words into two)
- Comma splices (two independent clauses joined by comma without conjunction)
- Incorrect prepositions ("eligible to" vs "eligible for", "comply to" vs "comply with")
- Wrong tense (article should be present tense for current rules, past tense for historical events)

**Clarity and meaning:**
- Ambiguous pronoun references ("it", "this", "they" — what does each refer to?)
- Double negatives that obscure meaning
- Sentences that require 2+ readings to understand — rewrite for clarity
- Technical jargon used without context (first use must define the term)

**Brand voice compliance (if client context specifies):**
- Zero contractions if specified
- No questions in body if specified
- Formal register if specified
- Correct Act/form name formatting (e.g., "Trade Marks Act, 1999" not "Trademark Act")

**Consistency:**
- Same term used throughout (not "legal aid" in one place and "free legal help" in another for the same concept)
- Numbers formatted consistently (spell out one-ten, digits for 11+, or all digits — pick one and stick)
- Date format consistent (DD Month YYYY for UK English)

Output: list of corrections. Fix all.

---

**After all 5 rounds, update:**
- [ ] JSON-LD schema `citation` array matches the ---CITATIONS--- section
- [ ] FAQ answers in schema match corrected FAQ body text word-for-word
- [ ] Any new sources from verification are added to citations

**Output:** Present a verification summary table to the user (claim / source / status) before proceeding.

---

## PHASE 6: Quality Review

Before saving, review against these checks:

- [ ] Every H2/H3 opens with answer-first (40-60 word capsule)
- [ ] **6–9 H2s, every one traceable to a sourced fan-out query (source recorded per query)**
- [ ] **Zero dead headings — no "Key considerations" / "Understanding the basics" / "What you need to know"**
- [ ] No section exceeds 300 words
- [ ] All data points sourced or marked "(industry estimate)"
- [ ] Tables used for 3+ data point comparisons
- [ ] FAQ answers don't mention the brand
- [ ] FAQ answers add depth beyond the body (not just repeating)
- [ ] Pillar/parent page linked at least once
- [ ] No cannibalization with existing pages
- [ ] Brand product/material/price claims verified against the FULL live catalog (paginated to the end), not a sample or brand-level assumption
- [ ] Brand's category price band matches the catalog for that category (not the store-wide range)
- [ ] All stages/steps present (no numbering gaps)
- [ ] All regulatory references include section/rule numbers
- [ ] Government fees verified against official source
- [ ] Word count within 10% of target
- [ ] meta_title includes current year and primary keyword
- [ ] meta_description starts with answer/value in first 70 chars
- [ ] tldr captures key takeaway in 2-3 sentences
- [ ] Schema includes all required types

Rate the article using the scoring rubric from `aeo-best-practices.md`.

---

## PHASE 7: Generate Blog Banner Image

Generate a professional blog banner using Seedream 4.5 via Novita API.

**Step 1: Check client's image dimensions**
If a client context file exists (`.claude/clients/<brand>.md`), check for documented featured image dimensions. If not documented, fetch an existing post from the client's WordPress to check:
```bash
curl -sL "<SITE_URL>/wp-json/wp/v2/posts?per_page=1&_fields=featured_media" -u "<USER>:<PASS>"
# Then fetch the media item to get dimensions
curl -sL "<SITE_URL>/wp-json/wp/v2/media/<media_id>?_fields=media_details" -u "<USER>:<PASS>"
```

**Step 2: Generate with Seedream 4.5**

```bash
# If client has a logo, encode it as base64 and pass as reference image
LOGO_B64=$(python3 -c "
import base64
with open('<logo_path>', 'rb') as f:
    print('data:image/png;base64,' + base64.b64encode(f.read()).decode())
")

curl -s -X POST "https://api.novita.ai/v3/seedream-4.5" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <NOVITA_KEY>" \
  -d "$(python3 -c "
import json, base64
payload = {
    'size': '2560x1440',  # Min 3,686,400 pixels. Generate large, resize later.
    'prompt': '<descriptive prompt for the banner - topic-relevant icons, brand colors, clean design, no text>',
    'watermark': False,
    'optimize_prompt_options': {'mode': 'standard'},
    'sequential_image_generation': 'disabled'
}
# If logo exists, pass as reference image so AI naturally integrates it
# Do NOT manually composite logos after generation - pass to AI instead
logo_b64 = '<base64 data URI>'  # or None
if logo_b64:
    payload['image'] = [logo_b64]
print(json.dumps(payload))
")"
```

**Key rules:**
- **Logo = reference image**: If the client has a logo, ALWAYS pass it in the `image` array so the AI integrates it naturally. Never manually overlay/composite after generation.
- **Minimum resolution**: 3,686,400 pixels (e.g., 2560x1440). Seedream rejects smaller sizes.
- **Response format**: Returns image URLs in `images[0]` (NOT base64). Download with curl.
- **Resize after**: Use `sips -z <height> <width> <file>` (macOS) to resize to the client's target dimensions.
- **Prompt tips**: Request abstract/flat design icons relevant to the topic. Explicitly say "no text overlays, no photographs of people or landmarks" to avoid AI-generated text artifacts.
- **Alt text**: Generate descriptive alt text for the image based on article topic (used when uploading to WordPress).

**Step 3: Download and resize**
```bash
# Download from URL returned by Seedream
curl -sL "<image_url>" -o /tmp/banner-raw.png
# Resize to client dimensions
sips -z <target_height> <target_width> /tmp/banner-raw.png
```

Save the final image path in the article frontmatter as `featured_image_path`.

---

## PHASE 8: Humanize Content (AI Detection Avoidance)

AI detectors (Quetext, GPTZero, Originality.ai) work by measuring token-level probability distributions — how predictable each word is to a language model. Clean, well-structured AI writing has LOW variance and LOW burstiness across paragraphs. The goal of humanization is to INCREASE token-level variance and paragraph-level burstiness.

**What works: Paragraph-by-paragraph rewrite with deliberate imperfections.**

The key insight (proven by testing): a single LLM rewriting its own output does NOT change the probability distribution. Multi-model rewriting (different LLMs per paragraph) increases variance somewhat but still gets detected. What actually reduces AI detection scores is introducing deliberate writing imperfections that create unpredictable (low-probability) token sequences.

**Step 1: Rewrite each body paragraph with these techniques:**

- **Verbose/wordy phrasing**: "DPIIT recognition is formal acknowledgement" → "So when people talk about DPIIT recognition, what they are referring to is basically a formal acknowledgement"
- **Redundant filler**: Add sentences that over-explain obvious things. "One thing that a lot of people get confused about is that..." — humans writing casually do this.
- **Slightly wrong word choices**: "fail to explain" instead of "cannot explain". "Getting around to" instead of "completing". These are lower-probability tokens that break the AI signature.
- **Casual connectors**: "So", "Now", "Basically", "Honestly", mixed with formal language.
- **Over-explanation**: Add context that a skilled editor would cut. "which stands for the Small Industries Development Bank of India" — unnecessary but human-like.
- **Run-on structures**: Long sentences with multiple clauses joined by "and" and "because" and parenthetical asides.
- **Second person**: Mix "you", "your", "you will need to" with formal third-person passages.
- **Vary paragraph density wildly**: Some paragraphs 2 sentences (30 words), others 8+ sentences (150+ words). This increases burstiness.

**Step 2: Preserve all facts and keywords**
After rewriting, verify:
- [ ] All target keywords still appear in headings and body text
- [ ] All numbers, legal references, section numbers, form names are unchanged
- [ ] All URLs and links are intact
- [ ] Pillar page link still present

**Step 3: Re-sync schema and FAQs**
If FAQ answers changed during humanization, update the JSON-LD FAQPage and FAQ_JSON to match the new wording.

**What does NOT work (tested and failed):**
- Stylistic parameter checklist (sentence starters, comma density) — detectors don't measure this
- LLM rewriting with "write more human" prompts — same probability distribution
- Multi-model paragraph rotation without imperfections — each model still writes cleanly
- NLP synonym swaps (NLTK) — changes <5% of tokens, invisible to detectors
- Backtranslation — produces "translationese" that detectors catch

---

## PHASE 9: Save to File

Save the complete article package to: `articles/<slug>.md`

Format:

```markdown
---
title: "<title>"
meta_title: "<meta_title>"
meta_description: "<meta_description>"
suggested_url: "<slug>"
tldr: "<tldr>"
word_count: <count>
article_type: "<type>"
keywords: [<list>]
selected_keywords: [<list>]
citations_count: <N>
aeo_score: <X>/10
project_id: "<project_id>"
brand: "<brand_name>"
featured_image_url: "<url or empty>"
generated_date: "<YYYY-MM-DD>"
---

<full article content in markdown>

---CITATIONS---
[1] Source Name — URL
[2] Source Name — URL
...

---SCHEMA---
<complete JSON-LD schema>

---FAQ_JSON---
[
  {"question": "...", "answer": "..."},
  ...
]
```

Also tell the user where the file was saved and show:
1. Article title + word count
2. AEO score (/10) with brief justification
3. Keyword coverage (which targets appear in headings)
4. Citation count + source quality summary
5. Cannibalization verdict
6. File path

---

## Important Notes

- Always get user confirmation at Phase 2 (keywords) and Phase 3 (cannibalization) before proceeding
- If GSC connection doesn't exist, skip Phase 3a and note it — proceed with caution
- The skill is brand-agnostic — adapt voice, terminology, and references to whatever brand/industry the project is in
- For legal services brands: reference exact act names, section numbers, form numbers
- For tech/SaaS brands: reference product versions, API endpoints, integration names
- Read `.claude/aeo-best-practices.md` for the latest scoring rubric, AEO rules, AI detection parameters, and GEO research findings
- Check `.claude/clients/` for a client-specific context file matching the project's brand. If one exists, use it for: credentials, brand voice, writing fingerprint, author mapping, WordPress field mapping, competitor exclusion list, and any client-specific rules
- If you discover a new AEO best practice or AI detection parameter during research, add it to the best practices file
- The humanization step (Phase 7) is MANDATORY - never skip it. An article that scores 90%+ on AI detectors will not be published by any client.

## Lessons Learned (Mistakes to Never Repeat)

### Brand-Product Claim Accuracy (E-commerce) — June 2026
- **The "AD bracelet" error.** A Nuyug "Best bracelet brands" article (already LIVE on Shopify) claimed the brand sold AAA American Diamond bracelets at ₹1,499–₹15,000. Root cause 1: the claim was inherited from an older draft and never checked. Root cause 2: brand-level inference — Nuyug IS known for American Diamond in earrings/necklaces, so "bracelets = AD" was assumed, and ₹1,499–46,000 (whole store) was used as the bracelet band.
- **The second error proves the rule.** The first "correction" queried only the first 250 of 902 products (no pagination), found 6 Kundan/pearl bracelets, and wrongly concluded "Kundan/pearl only, ₹2,499–₹3,499." The FULL catalog showed Bracelets = 124 SKUs, ₹1,499–₹5,999, dominated by American Diamond (79) + CZ (53). Incomplete data caused BOTH errors.
- **The fix is mechanical, not attentional.** Phase 3.5 + `scripts/nuyug_catalog_truthcard.py` paginate the entire catalog and lint the brand entry. NEVER write a brand product claim from memory, brand identity, or an unpaginated sample. Run the gate every time, and block the push on mismatch.

### Cannibalization
- **NEVER skip GSC data check.** The first time we created articles, we relied on the topical map's cannibalization map alone. It was insufficient. Always pull LIVE GSC query+page data to see what actually ranks.
- **"No existing page" is not enough.** Even if the cannibalization map says "create fresh," the service page may be ranking for related queries. Always check GSC for the EXACT keywords you plan to target.
- **GST was a near-miss.** Article 3.8 (GST Number) targeted keywords where the service page had 117K impressions. Only caught by running GSC data. Always verify.
- **Check adjacent queries too.** A service page ranking for "gst registration" at pos 7 will likely also capture "how to get gst number" traffic. Do not assume different keywords mean different pages.

### Validation Theatre (April 2026) — The Root Cause
- **Agents rubber-stamped claims as "VERIFIED" without fetching any source.** All 3 articles in the lawyer consultation batch passed "Round 1 verification" during creation, but a separate validation pass found 7 factual errors. The creation agents said "VERIFIED" based on training data, not by actually scraping the primary source.
- **The fix: Round 1 now REQUIRES a Jina/WebFetch call for every claim.** "VERIFIED" without a source URL is not valid. If you cannot fetch the source, write "COULD NOT VERIFY" — that is an honest answer. "VERIFIED (based on my knowledge)" is dishonest and must never be used.
- **Grammar was never checked.** No round existed for grammar, sentence clarity, or readability. Articles had run-on sentences, ambiguous pronouns, and inconsistent formatting. Round 5 now covers this.
- **FAQs were invented, not researched.** Agents wrote FAQ questions that seemed relevant but didn't match what people actually search. Google Autocomplete data revealed that the most-searched questions (e.g., "can I get divorce without lawyer", "do I need lawyer for power of attorney") were completely absent from the FAQs.

### Fact-Check Failures (April 2026)
- **Government programme statistics go stale fast.** Tele-Law beneficiary count was written as "fifty lakh" when the actual number (per tele-law.in) was 1.12 crore — off by 2x. Always fetch the LATEST figure from the programme's own website, not from secondary sources or older articles.
- **Section number misattribution.** Article cited "Section 35(1) of the Consumer Protection Act permits self-representation" — but Section 35(1) lists who can FILE complaints, not who can appear without a lawyer. Always read the actual section text, not a summary of it.
- **NCRB crime statistics overstated.** Article claimed "over 300% increase in cyber crimes" when actual NCRB data showed 217%. Never round up statistics for dramatic effect.
- **Helpline number conflation.** Two different services (Delhi SLSA and Tele-Law) were both attributed to the same number 1516. Always verify which organisation operates each helpline from the official source.
- **Outdated counts.** "1.7 million enrolled advocates" was from 2013; actual 2023 figure is ~2 million. For any "count of X" statistic, always check the most recent year available.

### Content & Schema
- **Keywords get stripped by humanization.** After humanizing, the primary keyword "trademark status check" (8,100 vol) was completely absent from the article. ALWAYS re-verify keyword presence in headings + body after ANY rewrite.
- **FAQ word count matters.** Initial FAQs were 90-140 words. AI engines extract first 50-60 words only. Keep to 40-80 words. Every word over 80 is wasted.
- **Schema FAQs must match body FAQs word-for-word.** After humanizing body FAQs, the schema still had old versions. Always re-sync schema after ANY edit.
- **Double quotes break WordPress shortcodes.** The `[sc_fs_multi_faq]` shortcode uses `question-N="..."` attributes. Double quotes inside the text (`"Formalities Check Fail"`) break the attribute boundary. Replace with single quotes.
- **`&quot;` does NOT work in WordPress shortcodes.** WordPress decodes HTML entities before parsing shortcodes. Only single quotes work.

### FAQs
- **FAQs were 100% body-restating.** In three VakilSearch articles (FSSAI, DPIIT, Trademark), every single FAQ answer restated content already in the article body — "what are the types" repeating the types section, "what are the fees" repeating the fee table, "how long does it take" repeating the timeline section. Zero new information. These FAQs add no value for RAG extraction because the body already contains the same answer.
- **FAQs must be driven by real search data.** Use DataForSEO related keywords + search volume to find what people ACTUALLY search for. "trademark class for restaurant" (1,000 SV) is far more valuable than "how many trademark classes in india" (0 SV). "fssai license for cloud kitchen" (2,900 SV) is far more valuable than "what is fssai basic registration" (0 SV). High-SV questions that the body does NOT cover = ideal FAQ candidates.
- **Self-check each FAQ.** Before finalising, literally ask: "Is this answer already in the body?" If yes → replace with a different question. Common violations: restating fee tables, summarising "types" sections, paraphrasing eligibility criteria, rewording processing timelines.

### Internal Linking (April 2026)
- **4-5 links is NOT enough.** In a batch of 4 lawyer consultation articles (~2500 words each), articles were created with only 5-7 internal links. An audit found 9 missing cross-links between sibling articles alone, plus 10+ missing service page links. A ~2500 word article should have 8-14 internal links.
- **Sibling article cross-links are the #1 gap.** Only 1 of 4 articles linked to any sibling article. The other 3 had zero cross-links. AI engines treat interlinked article clusters as topical authority — isolated articles get fewer citations. Cross-links to sibling articles are MORE important than links to service pages.
- **Check the "Articles Created" table.** Before writing, read the client context file's Articles Created table to know which articles exist. After writing, verify: does this article link to every relevant sibling?
- **Use `site:domain.com/article/ <topic>` to discover existing blog posts.** The client may have existing articles on related topics that you don't know about. Search before writing.
- **"Do You Need a Lawyer" had 15 sections but only 6 links.** Each section discussed a different legal situation (divorce, trademark, company registration, legal notice, etc.) — all of which have dedicated VakilSearch service pages. The article should have linked to at least 8-10 of them.

### Cannibalization (Keyword-Level)
- **Head terms cannibalize service pages.** "fssai license" (90.5k SV) and "fssai registration" (49.5k SV) were in the article's selected keywords while the service page /fssai-registration had 429+ impressions across 10+ state pages. Similarly, "startup india registration" (12.1k SV) competed with /startup-india-registration service page.
- **Check EACH keyword individually against GSC.** Not just the primary keyword. Each selected keyword needs its own cannibalization verdict.
- **Replace cannibalizing keywords with long-tail gaps.** After dropping "fssai license" and "fssai registration", we found "fssai central license" (880 SV), "fssai state license" (590 SV), "fssai documents required" (590 SV) — all with zero existing coverage. These are better targets for a blog article.
- **Also audit existing blog posts via web search.** GSC shows what ranks, but `site:domain.com/blog <topic>` reveals all existing content even if it does not rank. A topic with 10+ existing blog posts creates fragmentation risk even if none rank well.

### AI Detection
- **Generic humanization advice is WRONG for formal brands.** "Write short punchy sentences with contractions" is the opposite of what VakilSearch's actual writing looks like. Always analyze the brand's REAL published content first.
- **Sentence starters matter more than sentence length.** Starting 48% of sentences with "The" is the single biggest AI tell. Keep under 30%.
- **The humanizer over-corrects.** It added 53 parentheticals (human baseline: 9-30). Over-correction creates its own detectable pattern.

### Customer Systems
- **NEVER write to customer production systems without explicit approval.** We accidentally wrote test meta to a live WordPress post. Always ask first, show what will change, wait for "yes."
- **Draft previews don't render shortcodes.** WordPress shortcodes only execute for authenticated users or published posts. Do not panic if schema is missing on draft preview.

### API & Credentials
- **DataForSEO credential is already base64.** Do not decode it. Use directly in Authorization header.
- **Kimi K2.5 burns tokens on reasoning.** With 12K max_tokens, it used all tokens thinking and produced 0 output chars. Use K2 (non-reasoning) for rewrites, or set max_tokens=32768 for K2.5.
- **Novita API rejects urllib requests.** Cloudflare blocks Python urllib. Use curl for Novita API calls.
- **GSC tokens expire hourly.** Fetch fresh access tokens from the dev DB before each GSC query session. The refresh token is long-lived.
- **gcloud auth expires frequently.** Run `gcloud auth login` before any kubectl commands to prod.