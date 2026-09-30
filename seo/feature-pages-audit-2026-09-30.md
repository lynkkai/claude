# Lynkk Feature Pages: Competitor & Content Optimization Audit

**Date:** 2026-09-30 · **Data:** Ubersuggest (US, locId 2840, English) · **Raw data:** [`seo/data/ubersuggest-2026-09-30.md`](data/ubersuggest-2026-09-30.md)
**Rules followed:** [`memory/seo-keyword-guardrails.md`](../memory/seo-keyword-guardrails.md)

Tags: **[DATA]** from a tool response · **[OBSERVED]** seen in a crawl/SERP · **[JUDGMENT]** recommendation built on tagged facts · **[UNVERIFIED]** could not be checked.

---

## What could and could not be checked

- **Lynkk page titles and technical health:** checked via Ubersuggest's site audit crawler (38 pages). [DATA]
- **Lynkk body copy, H1s, meta descriptions, exact word counts:** **not read.** lynkk.ai is blocked by this
  environment's network policy, so on-page copy review is **[UNVERIFIED]**. The audit only tells us these six
  pages did *not* trigger the low-word-count, missing-H1, empty-meta-description, or title-length warnings.
- **Competitor page copy:** notion.com and tldv.io were also blocked. Competitor analysis below uses Ubersuggest
  domain metrics, SERP positions and ranking titles, and page-level ranking keywords only.

---

## 1. Headline findings

1. **None of the six pages rank for anything in Ubersuggest's US data.** lynkk.ai has 1 ranking keyword
   ("zoom meeting bot", position 39, on /features/meeting-bot), DA 1, and 1 nofollow backlink. [DATA]
2. **Technical SEO is not the bottleneck.** Site health score 85; /features/meeting-notes scored 100 in a page
   audit. The only flags on these six pages are "non-SEO-friendly URL" on /features/knowledge-graph and
   /features/chrome-extension (Ubersuggest did not give a reason). [DATA]
3. **The gap is authority and keyword targeting.** Every competitor has DA 44 to 66 and 1,000 to 16,000 ranking
   keywords. [DATA] Content changes alone will not close a DA 1 vs DA 44+ gap; the pages need both on-page
   targeting and links. [JUDGMENT, based on finding 1 and the competitor table]
4. **Two pages target concepts with no measured search demand** (knowledge-graph, parts of slack/workspaces),
   while demand-bearing phrasings exist that the titles do not use. [DATA + JUDGMENT, see per-page sections]

**Verdict: yes, all six pages need content optimization**, at different priorities (table in section 4).

---

## 2. Competitor analysis

Ubersuggest's automatic competitor detection returned **no results** for lynkk.ai (the site has too little
ranking data). The competitors below were chosen two ways: (a) the brands Lynkk already compares itself with
on /compare pages [OBSERVED], and (b) domains that appear in the SERPs pulled for each page's keywords [DATA].

### Domain strength (Ubersuggest `competitors`, US) [DATA]

| Domain | DA | Organic keywords | Est. monthly traffic | Backlinks |
|---|---|---|---|---|
| otter.ai | 66 | 11,594 | 679,963 | 319,488 |
| fireflies.ai | 54 | 16,034 | 56,745 | 108,735 |
| read.ai | 47 | 6,253 | 542,907 | 33,223 |
| granola.ai | 47 | 1,019 | 35,424 | 61,672 |
| wisprflow.ai (dictation) | 47 | 2,289 | 60,041 | 86,164 |
| tldv.io | 44 | 11,318 | 95,116 | 147,719 |
| fathom.video | 46 | 0* | 0* | 37,787 |
| **lynkk.ai** | **1** | **1** | **0** | **1** |

*fathom.video returned 0 keywords/traffic; cause not verified, so do not read this as "Fathom has no SEO". [UNVERIFIED]

### Who actually wins each page's SERP [DATA]

| Lynkk page | Keyword checked | Who ranks top (organic) | SERP type |
|---|---|---|---|
| meeting-notes | ai meeting notes | notion.com product page #2, read.ai #3, otter.ai #4 | Product pages at top, listicles below |
| dictation | ai dictation | substack guide, zapier, **aidictation.com (DA 18) #4**, willowvoice blog, Wirecutter | Mostly listicles, one low-DA product page |
| dictation | wispr flow alternative | reddit #1, saner.ai, getvoibe.com (DA 15), eesel.ai, wisprflow.ai comparison page | All "alternatives" listicles / comparisons |
| chrome-extension | google meet ai note taker | Google owns #2, #4, #5; Chrome Web Store (Scribbl) #6; read.ai #9; tldv.io #10 | Platform-owned + product pages |
| chrome-extension | bot free ai note taker | towardsai, reddit, zoom.com, otter.ai, Chrome Web Store (Scribbl), read.ai, tldv, notta | Mixed |
| slack | slack ai note taker | slack.com holds 6 of the top results; fellow.ai integration page #7 | Platform-owned |
| workspaces | team ai meeting notes | Chrome Web Store (AfterTheCall) #2, reddit (MS Teams), blogs | Mixed, Microsoft Teams intent mixed in |

### Competitor patterns worth copying [DATA → JUDGMENT]

- **Notion's feature page** ranks #2 for "ai meeting notes" (1,000) and also #3 for "ai notes" (5,400) and #9 for
  "meeting ai" (1,900). One feature page is picking up the broader head terms, not just the exact title. [DATA]
  → Lynkk's meeting-notes page should deliberately cover the broader "AI note taker / AI notes" phrasing. [JUDGMENT]
- **tldv.io has a dedicated Google Meet note taker page** that ranks 6 to 13 for about 15 Google Meet
  note-taker variants. Its SERP title is "Free Google Meet AI Note Taker - With or Without a Bot" (dash
  normalized). [DATA] → A platform-specific page is how competitors capture the chrome-extension/bot-free
  demand. [JUDGMENT]
- **Chrome Web Store listings rank on their own**: Scribbl's listing appears in 3 of the SERPs pulled, and
  AfterTheCall's listing is #2 for "team ai meeting notes" with an estimated 230 clicks. [DATA]
  → If Lynkk's extension is on the Chrome Web Store, its listing title/description is an SEO asset. Whether it is
  listed is **[UNVERIFIED]**.
- **fellow.ai has an integration page for Slack** that is the only non-Slack product page in the top 10 for
  "slack ai note taker". [DATA]
- **aidictation.com (DA 18)** ranks #4 for "ai dictation" with a product homepage, so a low-authority product
  page *can* break into this SERP. [DATA]

---

## 3. Page-by-page analysis

### 3.1 /features/meeting-notes
**Current title:** "AI Meeting Notes: Transcript, Summary and Tasks | Lynkk" [DATA]
**Technical:** page audit 100, 0 issues. [DATA] **Ranking keywords:** none. [DATA]

| Keyword | Vol | SD | Note |
|---|---|---|---|
| ai note taker | 27,100 | 48 | Biggest term in the space |
| ai notes | 5,400 | 55 | Notion's page ranks #3 |
| ai meeting notes taker | 3,600 | 49 | |
| meeting ai | 1,900 | 48 | |
| ai meeting notes | 1,000 | 41 | Current title's phrase |
| ai note taker app | 880 | 32 | Lowest SD in this group |
| ai note taker for meetings | 390 | 38 | |

**Assessment:** The title matches "ai meeting notes" (1,000/mo) but not "ai note taker" (27,100/mo), which is 27x
larger by volume. [DATA] **Needs optimization: HIGH priority.** [JUDGMENT]

**Recommendations** [JUDGMENT]
- Title option: "AI Note Taker & Meeting Notes: Transcripts, Summaries, Tasks | Lynkk". Keep "AI meeting
  notes" and add "AI note taker".
- H1/H2s: work in "AI note taker", "AI note taker app", "AI note taker for meetings" naturally.
- Differentiate using claims already in brand memory: before/during/after lifecycle, in-person + online,
  within ~30 seconds, offline-first, Jira/CRM follow-through. Do **not** add claims like "97% accuracy" or
  "15+ languages" (seen in a search snippet of the homepage) until they are added to `memory/lynkk-brand.md`.
- Add an FAQ block targeting question-style terms from the data (for example "ai note taker for in person
  meetings", 480/mo, SD 40). [DATA for the keyword]
- Link to /compare pages and use-case pages to pass internal relevance.
- **To verify first:** current H1, body copy, meta description (blocked here). [UNVERIFIED]

### 3.2 /features/knowledge-graph
**Current title:** "Ask Your Meetings: One Answer Across Every Call | Lynkk" [DATA]
**Technical:** URL flagged "non-SEO-friendly" by Ubersuggest. [DATA]

| Keyword tested | Vol | SD |
|---|---|---|
| meeting knowledge base | 0 | 12 |
| search meeting recordings | 0 | 12 |
| ai meeting search | 0 | 12 |
| chat with meeting transcripts | 0 | 4 |
| search meeting transcripts | No data | No data |
| ai meeting assistant (broader) | 4,400 | 60 |

**Assessment:** Every concept phrasing tested has **0 measured US volume**. [DATA] This page will not win search
traffic as currently framed. **Needs optimization: MEDIUM priority, but as a positioning decision, not a
copy tweak.** [JUDGMENT]

**Recommendations** [JUDGMENT]
- Do not invest in ranking this page for "knowledge graph"/"ask your meetings" phrasing; there is no measured
  demand. (Note: I did not query the generic term "knowledge graph"; it is a broad tech term with unrelated
  intent, so run it before deciding.)
- Option A: frame this page around "AI meeting assistant" (4,400/mo) since "ask for past context, get answers"
  is assistant behavior. SD 60 is the hardest term in this audit, so it is a long-term target.
- Option B: keep it as a conversion/explainer page and point search traffic at it through internal links from
  meeting-notes and use-case pages.
- Only change the URL if you change the page's target keyword; the page has no rankings to lose today. [DATA:
  0 rankings]
- **Next data step:** test more seeds (for example "ai meeting assistant" variants, "meeting memory",
  "ask ai about meetings") before rewriting.

### 3.3 /features/dictation
**Current title:** "AI Dictation for Mac: Speak Instead of Type | Lynkk" [DATA]

| Keyword | Vol | SD | Note |
|---|---|---|---|
| speech to text mac | 1,600 | 25 | Highest volume, low SD |
| speech to text mac os | 590 | 50 | |
| ai dictation | 480 | 31 | SERP mostly listicles |
| ai dictation tool | 480 | 44 | wisprflow.ai homepage #2 |
| wispr flow alternative | 480 | 11 | Rising: 210 (Jul 2025) to 880 (Apr to May 2026), 480 (Jul 2026) |
| speech to text mac app | 320 | 28 | |
| dictation software mac | 260 | 42 | |
| ai dictation app | 210 | 38 | |

**Assessment:** The title already targets "AI dictation" + "Mac". [DATA] It misses "speech to text Mac", which has
3x the volume of "ai dictation" at a lower SD (25 vs 31). [DATA] **Needs optimization: HIGH priority** (best
volume-to-difficulty ratio in this audit). [JUDGMENT]

**Recommendations** [JUDGMENT]
- Title option: "AI Dictation & Speech to Text for Mac: Type With Your Voice | Lynkk".
- Add sections that answer "speech to text Mac app" / "dictation software Mac" intent: works in any app, text at
  your cursor (from brand memory).
- Build a **/compare/wispr-flow** page (Lynkk already has /compare pages for Otter, Fireflies, Granola, Fathom).
  "wispr flow alternative" has SD 11 and its SERP is all listicles plus Wispr's own comparison page. [DATA]
  Only make claims about Wispr Flow that can be verified on their site.
- The "ai dictation" SERP is mostly listicles (zapier, willowvoice, Wirecutter, laxis). [DATA] Outreach to be
  included in those lists is likely worth more than on-page edits for that term. [JUDGMENT]
- **Caution:** SERP for "speech to text mac" returned no data, so we do not know what type of page ranks.
  [UNVERIFIED] Check it before committing.

### 3.4 /features/chrome-extension
**Current title:** "Record Meet, Zoom and Teams Without a Bot | Lynkk" [DATA]
**Technical:** URL flagged "non-SEO-friendly" by Ubersuggest. [DATA]

| Keyword | Vol | SD | Note |
|---|---|---|---|
| how to record google meet | 2,400 | 25 | Informational (how-to) |
| record google meet | 1,300 | 30 | |
| google meet ai note taker | 590 | 40 | Google owns top spots |
| google meet note taker | 390 | 35 | |
| record google meet chrome extension | 140 | 36 | Usually 10 to 30/mo; spiked 590 to 880 (May to Jun 2026) |
| record google meet extension | 140 | 32 | |
| bot free ai note taker | 110 | 59 | |
| ai note taker that doesn't join meetings | 90 | 30 | |
| meeting recorder chrome extension | 10 | 5 | |

**Assessment:** The title says "Without a Bot"; searchers use "bot free" and "doesn't join meetings". The title has
neither "Chrome extension" nor "note taker". [DATA] "Chrome extension" phrasing on its own has very low volume
(10/mo); the demand is in Google Meet recording/note-taker phrasing. [DATA]
**Needs optimization: HIGH priority.** [JUDGMENT]

**Recommendations** [JUDGMENT]
- Title option: "Bot-Free AI Note Taker: Chrome Extension for Google Meet, Zoom, Teams | Lynkk".
- H2s for "record Google Meet with a Chrome extension" and "AI note taker that doesn't join your meeting".
- Consider a separate **Google Meet note taker** page, following the tldv.io pattern that ranks for ~15 variants. [DATA for tldv]
- Write a blog/how-to post for "how to record google meet" (2,400, SD 25). This is informational intent and
  should not be forced onto the feature page.
- If the extension is on the Chrome Web Store, optimize that listing's title and description with the same
  terms. Scribbl's and AfterTheCall's listings rank in these SERPs. [DATA] Whether Lynkk's is listed: [UNVERIFIED]
- **To confirm:** does the extension actually support Zoom and Teams in the browser? The title says so; brand
  memory lists supported meeting platforms as "to confirm".

### 3.5 /slack
**Current title:** "Lynkk for Slack: Ask About Your Meetings in Any Channel | Lynkk" [DATA]

| Keyword | Vol | SD |
|---|---|---|
| slack ai notes | 170 (usually about 30; spike months 1,600 and 170) | 34 |
| slack ai note taking | 50 | 44 |
| slack ai note taker | 30 | 44 |
| slack huddle transcription | 30 | 30 |
| slack meeting notes | 10 | 14 |

**Assessment:** Low total demand (300/mo summed across the six Slack terms in the raw data). [DATA] slack.com holds most of the top
results. [DATA] **Needs optimization: LOW priority.** [JUDGMENT] This page's value is conversion and marketplace
discovery, not organic traffic.

**Recommendations** [JUDGMENT]
- Light edit: add "Slack AI notes" / "AI note taker for Slack" to the title or H1, following fellow.ai's
  integration-page pattern (the only non-Slack product page in the top 10). [DATA for fellow]
- Only target "huddle" terms if Lynkk actually records Slack huddles. This is not in brand memory. [UNVERIFIED]
- Consider moving to /integrations/slack to sit alongside /integrations. This is a structural choice, not
  data-driven.

### 3.6 /features/workspaces
**Current title:** "Workspaces: Team Meeting Notes with Pro for Everyone | Lynkk" [DATA]

| Keyword | Vol | SD | Note |
|---|---|---|---|
| team ai meeting notes | 720 | 25 | Lowest SD among the 700+ terms. Data last updated Dec 2025 |
| team ai note taker | 720 | 27 | SERP: no data. Data last updated Dec 2025; moves with the row above (likely one pool) |
| ai note taker for teams | 590 | 29 | Likely Microsoft Teams intent mixed in |
| team meeting notes | 390 | 43 | Informational; suggestions are mostly templates |
| shared meeting notes | 0 | 12 | |

**Assessment:** The title uses "Team Meeting Notes" (390, SD 43, template-seeking suggestions). [DATA] Adding "AI"
("team AI meeting notes" 720, SD 25) doubles volume at lower difficulty. [DATA]
**Needs optimization: MEDIUM priority.** [JUDGMENT]

**Recommendations** [JUDGMENT]
- Title option: "Team AI Meeting Notes: Shared Workspaces for Your Whole Team | Lynkk".
- Be careful with "for teams": the "team ai meeting notes" SERP includes Microsoft Teams results
  (r/microsoft_365_copilot, learn.microsoft.com). [DATA] Use "team" with "workspace"/"shared" context so the page
  is not read as a Microsoft Teams page.
- "Pro for everyone" is a pricing claim. Brand memory still lists pricing as "to confirm" (the crawl shows
  /pricing titled "Start Free, Pro at $15 a Month"). [OBSERVED] Keep claims consistent with /pricing.

---

## 4. Priority summary

| Page | Needs optimization? | Priority | Main demand-backed target | Vol / SD |
|---|---|---|---|---|
| /features/meeting-notes | Yes | **High** | ai note taker (+ ai meeting notes) | 27,100 / 48 (1,000 / 41) |
| /features/dictation | Yes | **High** | speech to text mac (+ ai dictation) | 1,600 / 25 (480 / 31) |
| /features/chrome-extension | Yes | **High** | google meet ai note taker, bot free ai note taker | 590 / 40, 110 / 59 |
| /features/workspaces | Yes | Medium | team ai meeting notes | 720 / 25 |
| /features/knowledge-graph | Yes (repositioning) | Medium | none found for concept; "ai meeting assistant" as option | 0; 4,400 / 60 |
| /slack | Light touch | Low | slack ai notes | 170 / 34 (usually about 30) |

New pages suggested by the data: **/compare/wispr-flow** (480, SD 11), **Google Meet note taker** page
(590, SD 40), **"How to record Google Meet"** blog post (2,400, SD 25). [DATA for volumes; pages are JUDGMENT]

Off-page, needed for any of this to rank: backlinks (lynkk.ai has 1) and inclusion in the listicles that
dominate the dictation and bot-free SERPs. [DATA for link count and SERP makeup; JUDGMENT for the approach]

---

## 5. Open items before rewriting

- [ ] Allow lynkk.ai in this environment's network settings (or paste page copy) so the on-page review of H1s, body
      copy, meta descriptions and FAQs can be done from the real text.
- [ ] Check Google Search Console: are all six pages indexed, and what queries show impressions? Ubersuggest shows
      no rankings, but that is a third-party estimate.
- [ ] Confirm product facts before using them in copy: supported meeting platforms for the extension, Chrome Web
      Store listing, Slack huddle support, pricing tiers, language count, accuracy claims.
- [ ] Pull SERPs again for "speech to text mac" and "team ai note taker" (no data this session).
- [ ] Test more keyword seeds for the knowledge-graph page before choosing its direction.
