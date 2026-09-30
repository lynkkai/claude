# SEO Audit: lynkk.ai/features/meeting-notes

- **Page:** https://lynkk.ai/features/meeting-notes
- **Audit date:** 2026-09-30
- **Tools:** Ubersuggest MCP (account marketing@lynkk.ai, tier1), web search
- **Rules followed:** [`memory/seo-data-guardrails.md`](../memory/seo-data-guardrails.md). Every number below has a
  source. Anything the tools did not return is marked **Not available**.
- **Note on quoting:** competitor page titles are quoted with dashes changed to a colon or hyphen, per the repo writing rules.

---

## 1. Summary

| Question | Answer | Confidence |
|---|---|---|
| Does the page rank for anything? | No. Ubersuggest has no ranking keywords and no traffic for this URL. | Verified (tool) |
| Does the page need optimization? | Yes. It has zero organic visibility today. | Verified (tool) |
| Is the problem the content? | **Not determined.** The page HTML could not be read (see Data gaps). Domain signals (DA 1, one nofollow backlink) show authority and indexation are at least part of the problem. | Verified (tool) for DA/backlinks; cause is Hypothesis |
| Who wins this topic? | Dedicated feature pages (Notion, meeting.ai, Krisp, Tactiq, note1), product homepages (Read AI, Otter, Notta), and listicles/UGC (Reddit, Zapier, Medium, app stores). | Verified (tool), US SERPs |

---

## 2. Lynkk baseline (Ubersuggest)

### 2.1 Page level

| Call | Location | Result | Label |
|---|---|---|---|
| `page_overview` | Global | `noData` | Verified (tool) |
| `page_keywords` | Global | 0 ranking keywords | Verified (tool) |
| `page_keywords` | US (2840) | Not available: daily report quota reached | Gap |

### 2.2 Domain level: `domain_overview` lynkk.ai (Global, pulled 2026-09-30)

| Metric | Value |
|---|---|
| Organic keywords | 1 |
| Organic traffic | 0 |
| Domain authority | 1 |
| Backlinks | 1 (0 follow, 1 nofollow) |
| Referring domains | 1 |
| Monthly ranking keywords, 2025-09 to 2026-06 | 0 each month |
| Monthly ranking keywords, 2026-07 and 2026-08 | 1 each month |

The only ranking keyword on the domain:

| Keyword | URL | Position | Volume | SD | PD | CPC | Location |
|---|---|---|---|---|---|---|---|
| zoom meeting bot | /features/meeting-bot | 39 | 20 | 26 | 34 | $21 | en, US (2840) |

### 2.3 Competitor auto-detection

| Call | Location | Result |
|---|---|---|
| `competitors` lynkk.ai | US (2840) | No competitor data (the domain has too little ranking data for Ubersuggest to match competitors) |

Because auto-detection returned nothing, competitors below are taken **from the live SERPs** for the
topic, not from assumptions.

### 2.4 Search index check (web search tool, not Google Search Console)

A `site:lynkk.ai features` search returned only the homepage (https://lynkk.ai/). This does **not**
prove the features page is unindexed (the web search tool is not Google). Confirm in Google Search
Console with URL Inspection. **Label: Third-party / snippet.**

---

## 3. Competitor analysis (Ubersuggest `serp_analysis`, US 2840, English)

`Est. clicks` is Ubersuggest's estimate of clicks to that URL. It is **not** search volume. `-1` means not estimated.

### 3.1 "ai meeting notes" (SERP date 2026-09-08)

| Pos | URL | DA | Est. clicks | Page type |
|---|---|---|---|---|
| 1 | AI Overview | | | SERP feature |
| 2 | notion.com/product/ai-meeting-notes | 65 | 306 | Dedicated feature page |
| 3 | read.ai/ | 47 | 71 | Homepage |
| 4 | otter.ai/ | 66 | 12 | Homepage |
| 5 | People Also Ask | | | SERP feature |
| 6 | reddit.com/r/ProductivityApps (in-person apps test) | 92 | 11 | UGC |
| 7 | apps.apple.com (Minutes: AI Meeting Note Taker) | 99 | 7 | App store |
| 8 | meeting.ai/en/p | 21 | 5 | Homepage |
| 9 | charitydigital.org.uk (best AI tools for meeting notes) | 46 | 4 | Listicle |
| 10 | perfectwikiforteams.com (best AI note takers for Teams) | 17 | 4 | Listicle |
| 13 | tldv.io/blog/free-ai-note-taking | 44 | 1 | Listicle |
| 14 | zapier.com/blog/best-ai-meeting-assistant | 82 | 1 | Listicle |
| 15 | krisp.ai/ai-note-taker | 60 | 3 | Dedicated feature page |
| 19 | notta.ai/en | 50 | 1 | Homepage |
| 22 | openwhispr.com/meeting-notes-software | 28 | 2 | Dedicated feature page |

### 3.2 "ai meeting notes app" (SERP date 2026-09-18)

| Pos | URL | DA | Est. clicks |
|---|---|---|---|
| 1 | AI Overview | | |
| 2 | justtalkingtech.medium.com (tested 14 note takers) | 95 | 69 |
| 3 | reddit.com/r/ProductivityApps (in-person apps test) | 92 | 13 |
| 5 | apps.apple.com (Minutes) | 99 | 21 |
| 6 | simular.ai/alternatives/ai-meeting-note-takers | 24 | 4 |
| 7 | otter.ai/ | 66 | 5 |
| 8 | meeting.ai/en/p | 21 | 3 |
| 9 | read.ai/ | 47 | 2 |
| 10 | zapier.com/blog/best-ai-meeting-assistant | 82 | 2 |
| 13 | plaud.ai (best free AI meeting note takers) | 54 | 2 |
| 15 | notta.ai/en | 50 | 1 |

### 3.3 "ai meeting summary" (SERP date 2026-09-16)

| Pos | URL | DA | Est. clicks |
|---|---|---|---|
| 1 | AI Overview | | |
| 2 | read.ai/ | 47 | 89 |
| 3 | play.google.com (Summary: AI Note Taker) | 99 | 16 |
| 4 | summary.ai/ | 23 | 3 |
| 6 | meeting.ai/en/p | 21 | 2 |
| 8 | support.zoom.com (Meeting Summary with AI) | 88 | 2 |
| 9 | webex.com/us/en/articles/ai-meeting-notes.html | 86 | 2 |
| 10 | tactiq.io/ai-tools/ai-meeting-summary | 43 | 1 |
| 11 | krisp.ai/ai-meeting-summary | 60 | 1 |
| 13 | zapier.com/blog/best-ai-meeting-assistant | 82 | 2 |

### 3.4 "in person meeting notes ai" (SERP date 2026-09-30)

| Pos | URL | DA | Est. clicks |
|---|---|---|---|
| 1 | AI Overview | | |
| 2 | **meeting.ai/en/p/features/notes** | **21** | 20 |
| 3 | shadow.do (AI note takers for students) | 20 | 2 |
| 4 | apps.apple.com (Jamie) | 99 | 0 |
| 5 | People Also Ask | | |
| 6 | Discussions and forums | | |
| 8 | nexusai.asia (notetaker comparison) | 9 | 1 |
| 10 | happyscribe.com (AI note takers for sales teams) | 58 | 1 |

### 3.5 "ai note taker" (SERP date 2026-09-29)

| Pos | URL | DA | Est. clicks |
|---|---|---|---|
| 1 | AI Overview | | |
| 2 | play.google.com (Ai Note Taker: Speech to Text) | 99 | 7,958 |
| 3 | ca.plaud.ai (best AI note taker for in-person meetings) | 54 | 2,005 |
| 5 | apps.apple.com (AI Note Taker: Meeting Minutes) | 99 | 2,227 |
| 6 | speakwiseapp.com/blog/best-ai-note-taker-2026 | 34 | 600 |
| 7 | reddit.com/r/AiNoteTaker (integrations with project tools) | 92 | 196 |
| 8 | **note1.ai/features/ai-note-taker** | **6** | 67 |
| 9 | fieldy.ai (AI note takers for in-person) | 20 | 58 |
| 13 | fabric.so/comparison/best-ai-meeting-note-taker | 27 | 15 |
| 18 | help.fellow.ai (AI meeting note taker) | 46 | 9 |

### 3.6 "multilingual ai note taker" (SERP date 2026-09-30)

All `Est. clicks` returned as `-1` (not estimated).

| Pos | URL | DA |
|---|---|---|
| 1 | circleback.ai (best AI meeting notes tools with multilingual support) | 32 |
| 1 | AI Overview | |
| 2 | apps.apple.com (Note AI) | 99 |
| 4 | flownote.ai (AI note taker for in-person meetings) | 15 |
| 5 | reddit.com/r/productivity | 92 |
| 6 | happyscribe.com/ai-meeting-notetaker/catalan | 58 |

### 3.7 "meeting notes to jira"

`noData` from Ubersuggest.

### 3.8 Patterns in the data (Verified (tool) unless marked)

1. **AI Overview appears at position 1 in all six SERPs with data.** People Also Ask appears in all six.
2. **Low-DA feature pages do rank.** meeting.ai/en/p/features/notes (DA 21) is #2 for "in person meeting notes ai";
   note1.ai/features/ai-note-taker (DA 6) is #8 for "ai note taker". Authority is not the only gate.
3. **The exact phrase sits in the URL slug or title of the ranking feature pages:** /product/ai-meeting-notes,
   /features/notes, /ai-note-taker, /ai-meeting-summary.
4. **Listicles and UGC take a large share of positions** (Reddit, Zapier, Medium, tl;dv, Plaud, Speakwise, fabric,
   simular, charitydigital). lynkk.ai does not appear in any of the six SERPs above.
5. **In-person capture is a recurring SERP theme:** Reddit, Plaud, fieldy, flownote, and meeting.ai all target it.

### 3.9 Competitor positioning (from each competitor's own copy as surfaced by web search)

**Label: Third-party / snippet.** Not verified on the source pages (those hosts are blocked from this environment).

| Competitor | Claims seen in snippets |
|---|---|
| Notion AI Meeting Notes | A block inside any Notion page; real-time transcription and summary; speaker identification; action items become to-dos with owners, priority, and due dates; notes pushed to Slack or email; ask questions across past meetings |
| meeting.ai (Memo) | Works for in-person recordings and a bot for Meet, Zoom, Teams; summary on top, decisions and owners in the middle, transcript below; tap a line to jump to audio; a "Visual Note" infographic per meeting; editable summary and action items |
| Read AI | Zoom, Teams, Meet, and in-person; summary, transcript, playback, action items; engagement and sentiment signals; upload your own recordings; Slack, Zapier, webhook delivery |

---

## 4. Lynkk vs competitors: where the page can differentiate

Lynkk claims come from `memory/lynkk-brand.md` unless marked.

| Lynkk capability | Seen in competitor snippets above? | Use on page |
|---|---|---|
| Before, during, and after meeting in one AI | Not seen | Lead differentiator |
| Joins the meeting and answers by voice | Not seen | Differentiator |
| Notes within ~30 seconds | Notion says notes land "the moment the meeting ends" (no time stated); others not seen | Speed proof point |
| CRM fields updated, Jira tickets created | Notion: to-dos only; Read AI: Zapier/webhooks | Differentiator (name the CRMs once confirmed) |
| Knowledge graph of all meetings | Notion: ask past meetings | Partial overlap, explain the graph concretely |
| In-person and online capture | meeting.ai and Read AI both claim it | Table stakes, must be covered |
| Multilingual, code-switching | Not seen | Differentiator. "15+ languages" and "97% accuracy" appear in lynkk.ai search snippets but "number of languages" is still under **To confirm** in the brand memory. Confirm before publishing |
| Data residency (choose a region) | Not seen | Differentiator for regulated teams (list regions once confirmed) |
| Offline-first | Not seen | Differentiator |
| MCP connections | Not seen | Differentiator for technical buyers |

---

## 5. Content optimization recommendations

All items are **Hypothesis** built from the SERP patterns in section 3. Keyword targets are
**Unvalidated candidates** until the metrics in section 6 are pulled.

### 5.1 Keyword targeting

| Role | Candidate | Why (data basis) |
|---|---|---|
| Primary | ai meeting notes | Notion's dedicated feature page holds #2 with the highest est. clicks in that SERP |
| Secondary | ai meeting summary | Dedicated pages from Tactiq and Krisp rank; matches the page's "structured notes" output |
| Secondary | in person meeting notes ai | A DA 21 feature page ranks #2 |
| Secondary | multilingual ai note taker | Ranking pages are mostly blogs and app listings; no dedicated feature page seen in the top 6 |
| Watch | ai note taker | App stores and listicles dominate; broad intent |
| Drop for now | meeting notes to jira | Ubersuggest returned no data |

### 5.2 On-page changes (run the checklist in 5.3 first to see what already exists)

1. **Title and H1** start with the primary phrase, then the differentiator. Draft, to be adjusted after validation:
   - Title: `AI Meeting Notes in 30 Seconds, Online or In Person | Lynkk` (58 characters)
   - H1: `AI meeting notes for every conversation, online or in person`
2. **Answer-first intro (40-60 words)** that defines what Lynkk's meeting notes are. AI Overviews lead every SERP,
   so a clear, quotable definition near the top matters.
3. **"What your notes look like" section** with a real example: summary, decisions, action items with owners, CRM
   fields, Jira ticket. Competitor snippets describe their output structure explicitly.
4. **Before / During / After sections**, each with its own H2. This is the one angle no competitor snippet shows.
5. **In-person meetings H2** (theme appears across five SERP results).
6. **Multilingual H2** covering code-switching, with the confirmed language count.
7. **Integrations H2:** Calendar, Jira, CRM, Calendly, Cal.com, MCP, each linked to its own page if one exists.
8. **Privacy and data residency H2** with the confirmed regions.
9. **FAQ block** with `FAQPage` schema. The PAA questions were not returned by the tools, so the questions must be
   pulled first (section 6). Do not publish invented questions as "what people ask".
10. **Schema:** `SoftwareApplication` (with the confirmed pricing) and `FAQPage`.
11. **Internal links:** link to this page from the homepage and from /features/meeting-bot (the only Lynkk URL with a
    ranking keyword).

### 5.3 On-page checklist (not yet run: page HTML not reachable)

- [ ] Title tag contains "AI meeting notes" and is under 60 characters
- [ ] One H1, containing the primary phrase
- [ ] Meta description under 160 characters with a clear benefit
- [ ] Main content is in the server-rendered HTML (not only client-side JS)
- [ ] Word count and section coverage vs the Notion and meeting.ai feature pages
- [ ] Canonical tag points to itself
- [ ] Page is in the XML sitemap and not `noindex`
- [ ] Image alt text; product screenshots present
- [ ] Internal links in and out
- [ ] Core Web Vitals (Ubersuggest `pagespeed_audit`)

### 5.4 Off-page (Hypothesis)

The domain has DA 1 and one nofollow backlink. Content changes alone may not move rankings. Parallel actions:

- Pitch inclusion in the listicles already ranking: zapier.com/blog/best-ai-meeting-assistant, tldv.io/blog/free-ai-note-taking,
  speakwiseapp.com, fabric.so, simular.ai, circleback.ai (multilingual), fieldy.ai and flownote.ai (in-person).
- Take part in the Reddit threads that rank (r/ProductivityApps, r/AiNoteTaker), following each subreddit's rules.
- Finish the directory submissions prepared in `launch/`.

---

## 6. Data gaps and next calls

| Gap | Reason | Next call |
|---|---|---|
| Live page content (title, headings, copy, schema) | lynkk.ai is blocked by this environment's network policy | Allow `lynkk.ai` in the environment's network settings, or paste the page HTML, or run Ubersuggest `site_audit` on lynkk.ai |
| Search volume, SD, CPC for all candidate keywords | Ubersuggest daily report quota (150) reached | `keyword_overview` (locId 2840) for each keyword in 5.1 |
| Related keyword ideas | Same quota | `keyword_suggestions` / `match_keywords` with seeds "ai meeting notes", "meeting notes app" |
| US ranking keywords for the page | Same quota | `page_keywords` page=https://lynkk.ai/features/meeting-notes, locId 2840 |
| Competitor page keyword sets | Same quota | `page_keywords` for notion.com/product/ai-meeting-notes and meeting.ai/en/p/features/notes, locId 2840 |
| People Also Ask questions | `serp_analysis` returns the PAA block position but not the questions | Check the SERP manually or use another SERP tool |
| Competitor page structure | Competitor hosts blocked from this environment | Same as first row, or review in a browser |
| Indexation of the page | Web search tool is not Google | Google Search Console URL Inspection |
| Lynkk facts under "To confirm" | Not provided yet | Team to fill in `memory/lynkk-brand.md` |
