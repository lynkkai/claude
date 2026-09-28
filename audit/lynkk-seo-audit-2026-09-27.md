# Lynkk.ai: full SEO audit

**Date:** 2026-09-27
**Site:** https://lynkk.ai
**Method:** Search Console export analysis, SERP reconnaissance, architecture
inference. The automated crawl could not run (see Scope below).

---

## Scope and method: read this first

Two halves to this audit.

**What ran.** A real Search Console export (92 days), SERP reconnaissance across
nine searches, and an analysis of the site architecture the export reveals. Every
finding below marked "Evidence" is traceable to one of those.

Three limits on that evidence, worth holding in mind throughout:

- **The searches were US-only.** India is 35% of Lynkk's AI-surface impressions,
  so the off-site findings in Part 2 describe the US search landscape and may
  not hold for the market that matters most to Lynkk today.
- **`Pages.csv` is headed "Top pages", not "all pages".** It is a ranked list,
  so it shows which URLs were cited most, and cannot prove that no other URL was
  ever cited or that no other page exists.
- **The export covers AI surfaces only.** A page that ranks perfectly well in
  ordinary Search but has never been quoted in an AI answer does not appear here
  at all. Nothing in this report should be read as a statement about a page's
  ordinary Search performance.

**What did not run.** The automated crawl. Outbound HTTPS is blocked for every
host in this Claude cloud environment: the egress proxy answers 403 to CONNECT,
for lynkk.ai and for example.com alike. So nothing that needs to touch the site
was measured:

| Not measured | Why it matters |
|---|---|
| Core Web Vitals (LCP, CLS, TTFB, FCP) | 10% of the SEOmator score, and a ranking factor |
| robots.txt, sitemap.xml, llms.txt | Whether Google and AI crawlers can even reach the pages |
| Canonical tags, noindex, redirect chains | Indexation blockers, the highest-priority class of bug |
| Title and meta description text and lengths | The whole on-page layer |
| Heading structure, word counts, thin-content detection | Content quality signals |
| JSON-LD structured data | Rich results and AI citation eligibility |
| Security headers, HSTS, CSP, mixed content | 8% of the score, plus trust signals |
| Broken links, image alt text, accessibility | 23% of the score combined |
| JS rendering: does the content exist without JavaScript | Suspected root cause of several findings below |

**Do not treat the absence of a technical finding here as a pass.** Those checks
are pending, not clear.

To unblock: open the cloud environment menu in the session title bar, choose
Edit, and under Network access either raise the access level or add `lynkk.ai`
and `www.lynkk.ai` to the allowed domains. Docs:
https://code.claude.com/docs/en/claude-code-on-the-web

Then run `scripts/run-seo-audit.sh`. It is written, tested for syntax, and the
SEOmator CLI (373 rules, 20 categories) is installed and verified in this
session. It will produce the missing half in about ten minutes.

---

## Executive summary

Lynkk's SEO problem is not that the site is broken. It is that the site is
**too small to compete and too thin to be quoted**, in a category where Google
now answers most queries itself.

Health assessment: **early, small, and growing.** 105 AI-surface impressions
across 92 days is close to a standing start in absolute terms. The trend
underneath it is healthy: the daily rate roughly doubled each month, from 0.23
in July to 1.26 in August to 2.46 in September. September is a partial month
(24 days), so compare rates rather than totals. The constraint is not that
growth is failing, it is that the footprint is concentrated on a handful of
pages and there is very little of the site for Google to cite.

### Top five priorities

1. **Only twelve URLs have ever been cited in AI surfaces, and 62% of the
   impressions land on the homepage alone.** The page inventory, not the
   trajectory, is what caps this. Growth is currently strong, so the return on
   adding pages is higher now than it will look later. (Finding C1)

2. **Legal pages outrank product pages in AI answers.** `/terms` pulled more
   impressions than `/how-it-works`, `/features/knowledge-graph`,
   `/features/action-items` and both use-case pages. Terms, privacy and refund
   together take 9.4% of Lynkk's entire AI-surface footprint. Boilerplate is
   being quoted because it is specific and extractable, and the product pages
   are not. (Finding C2)

3. **Lynkk does not appear in a single "best AI meeting assistant 2026"
   listicle, alternatives roundup, or tool directory.** In this category those
   pages own the head terms and are the sources AI Overviews cite. This is the
   highest-leverage off-site work available. (Finding O1)

4. **Lynkk does not own its own brand SERP.** "Lynkk" returns a UK company
   registration, a Nigerian crypto brand, two musicians and an Instagram account
   before the product gets a clear shot. There is no entity disambiguation.
   (Finding O2)

5. **India is 35% of AI-surface impressions and `/features/hinglish-transcription`
   is the second-strongest page on the site.** That is validated product-market
   fit showing up in search data, and it is currently served by exactly one page.
   (Finding C3)

### Quick wins (days, not quarters)

- Ship a `/pricing` page. It does not exist in any data or SERP result found.
  Pricing is the most common commercial query in this category and pricing pages
  are disproportionately cited in AI answers.
- Add Organization + SoftwareApplication JSON-LD with `sameAs` pointing at the
  X, Instagram, Facebook and Companies House profiles. Fixes the brand-entity
  problem at its root.
- Add an FAQ block with real answers to the homepage and each feature page.
  This is the format AI surfaces extract from, and the Search Console export
  proves Lynkk is already eligible for those surfaces.
- Publish `/llms.txt` and confirm AI crawlers are not blocked in robots.txt.
- Submit to AI tool directories. Free, fast, and it is how this category gets
  discovered.

---

## Part 1: Search Console findings

**Source:** `memory/data/gsc-ai-features-2026-09-27/`, filters Search type = Web,
Date = last 3 months (2026-06-25 to 2026-09-24).

### A caveat that changes how you read every number

This export is **"Performance on Search > Generative AI Features"**. It is the AI
Overviews and AI Mode subset, not total Search. It also carries the Impressions
metric only: no clicks, no CTR, no average position, and no query data.

So: 105 is not Lynkk's Search traffic. It is Lynkk's AI-surface impressions. The
full picture needs a second export.

**Action:** export Search Console again with no Generative AI filter, all four
metrics (clicks, impressions, CTR, position) and the Queries tab included, for
the same 3 months and for 16 months. Drop it in `memory/data/`. Without query
data, keyword targeting and cannibalisation checks are guesswork.

---

### Finding C1: the cited surface is tiny and concentrated

| Issue | Only 12 URLs have been cited in AI surfaces at all, and the homepage takes 72 of 117 (62%) |
|---|---|
| **Impact** | High |
| **Evidence** | `Pages.csv` lists 12 URLs; the homepage takes 61.5% of the 117 page-level impressions. Consecutive 14-day totals across the window: 0, 5, 11, 19, 34, 34. Monthly impressions per day: July 0.23, August 1.26, September 2.46. |
| **Diagnosis** | The concentration is the finding. Twelve cited URLs cannot cover a category with hundreds of commercial queries, and one page carrying 62% of the footprint is a single point of failure. The growth trend itself is fine: the daily rate is still climbing sharply month over month. The last two fortnights are flat at 34 each, which is worth watching but is not yet evidence of a plateau. At this volume the expected swing on 34 impressions is roughly plus or minus 6 from chance alone, so a 20% change in the true rate would be invisible. One more fortnight of data will settle it. |
| **Fix** | Treat page creation as the primary growth lever for the next two quarters. The gap list is in Part 3. |
| **Priority** | 1 |

A secondary read: it is also possible that more pages exist but are not
indexable (thin, JS-dependent, noindexed, orphaned, or missing from the
sitemap). The crawl distinguishes these two cases. Run it before committing a
content budget, because the fix is completely different.

### Finding C2: legal boilerplate outranks the product

| Issue | `/terms` is the fourth most-surfaced page on the site. Legal pages take 9.4% of AI-surface impressions |
|---|---|
| **Impact** | High |
| **Evidence** | `Pages.csv`: `/terms` 6, `/privacy` 3, `/refund` 2, totalling 11 of 117. `/terms` alone beats `/features/knowledge-graph` (4), `/how-it-works` (4), `/features/action-items` (3), `/use-cases/sales-calls` (1) and `/use-cases/team-standups` (1). |
| **Diagnosis** | Legal pages are long, specific, declarative and structured. They state facts an extractive model can lift. Marketing pages that lead with a headline and three benefit bullets do not. This is a content-format problem, and it is the single clearest signal in the whole export. |
| **Fix** | Rewrite feature and use-case pages to be answer-shaped: specific numbers, named integrations, explicit limits, comparison tables, and an FAQ block per page. Say "creates Jira tickets with the assignee and due date set from the transcript" rather than "automates your follow-ups". Do not noindex the legal pages: they are doing no harm and they demonstrate exactly the format that works. |
| **Priority** | 1 |

### Finding C3: India is the strongest market and is served by one page

| Issue | India is 35% of impressions (37 of 105), more than seven times the US (5), and the Hinglish page is the joint second-best page on the site |
|---|---|
| **Impact** | High (opportunity) |
| **Evidence** | `Countries.csv`: India 37, Spain 7, UK 7, US 5, Brazil 4, Canada 4, Indonesia 4. `Pages.csv`: `/features/hinglish-transcription` 10, level with `/features/meeting-bot` 10. Independent SERP check confirms real competition for Hinglish and Hindi meeting notes (JotMe, HappyScribe, MeetMinutes, OpenNotetaker, hearlog.ai, 60db.ai, VOMO), which means there is real demand. |
| **Diagnosis** | Lynkk has found a defensible niche by accident and is under-serving it. Code-switched Hinglish transcription is genuinely hard, most global tools treat it as an edge case, and Lynkk has a page ranking for it on a domain with almost no authority. |
| **Fix** | Build out the India and multilingual cluster: Hindi meeting notes, Tamil/Telugu/Kannada if supported, code-switching explainer, India pricing in INR, an India data-region page. Check whether there is a language selector or hreflang at all: if Lynkk ever adds one, get it right the first time, because cross-locale canonicals and missing return tags suppress entire locale sets. |
| **Priority** | 2 |
| **Blocked on** | Number of supported languages, and which Indic languages specifically. Open item in `memory/lynkk-brand.md`. |

### Finding C4: the device split is backwards for the audience

| Issue | Desktop 68%, mobile 30%, with India as the top country |
|---|---|
| **Impact** | Medium |
| **Evidence** | `Devices.csv`: Desktop 71, Mobile 32, Tablet 2. India leads `Countries.csv` at 35%. |
| **Diagnosis** | Two readings, and they need different fixes. Benign: a Mac-desktop work tool skews desktop, which is plausible. Not benign: India is one of the most mobile-first search markets on earth, so 68% desktop alongside 35% India is odd enough to warrant a check for mobile rendering or parity problems suppressing mobile impressions. |
| **Fix** | Run the crawl with `--mobile`. The `mobile-parity-*` rules compare content, title, canonical, structured data and links between the desktop and mobile renders. Google indexes the mobile version, so anything missing there is missing, period. |
| **Priority** | 2 |

### Finding C5: no clicks, no queries, no position data

| Issue | The export has one metric and no query dimension |
|---|---|
| **Impact** | Medium (blocks other work) |
| **Evidence** | `Chart.csv`, `Pages.csv`, `Countries.csv` and `Devices.csv` each carry Impressions only. There is no Queries.csv in the archive. |
| **Diagnosis** | Impressions without clicks cannot tell you whether AI surfaces are sending anyone, and without queries there is no keyword map, no intent check and no cannibalisation check. |
| **Fix** | Re-export as described at the top of this Part. Also confirm Bing Webmaster Tools is set up: Bing feeds Copilot and ChatGPT search, and it is a separate index with separate coverage reporting. |
| **Priority** | 2 |

---

## Part 2: Off-site and SERP findings

**Source:** nine searches run 2026-09-27. These are SERP observations, not a
crawl or a backlink audit.

### Finding O1: absent from every listicle and directory in the category

| Issue | lynkk.ai appears in no "best AI meeting assistant" roundup, no alternatives page, and no AI tool directory found |
|---|---|
| **Impact** | High |
| **Evidence** | Searches for "best AI meeting assistant in-person meetings data residency 2026", "Lynkk.ai alternatives Otter Fireflies Granola comparison", "Lynkk AI meeting assistant pricing features review" and "AI meeting notes India Hindi multilingual notetaker CRM Jira" returned Zapier, Reclaim, Read.ai, Fireflies, Otter, Krisp, HappyScribe, MeetGeek, tl;dv, Sybill, JotMe, MeetMinutes, Tana, Rock, Hedy, Meetily, People Managing People and a Medium 14-tool test. Lynkk appeared in none of them. The only result Lynkk earns is its own homepage on direct brand queries. |
| **Diagnosis** | In this category the head terms are owned by listicles, and AI Overviews cite listicles heavily because they are comparative and structured. Not being in them means being invisible for every non-brand query, regardless of on-site work. |
| **Fix** | Three tracks, in order of speed. (1) Directories: There's An AI For That, Futurepedia, AI tool aggregators, G2, Capterra, Product Hunt. Mostly free, mostly same-week. The Product Hunt copy is already drafted in `launch/producthunt-submission.md`. (2) Outreach to the roundup authors with a specific angle rather than a generic pitch: the in-person capture, the per-region data residency, and the Hinglish support are things most of the listed tools genuinely cannot do. (3) Publish Lynkk's own comparison pages so the brand competes on those queries directly. |
| **Priority** | 1 |

One market note worth acting on. A 2026 roundup summarised the category as
splitting into "notetakers that transcribe and summarize" and "agentic meeting
platforms that turn the conversation into filed tickets, drafted documents, and
follow-ups during the call", and observed that the meaningful differences are now
"data residency, consent, and per-seat cost, not does it transcribe". Lynkk sits
in the second group and leads on data residency. The positioning is right. It is
simply not written down anywhere Google can find it.

### Finding O2: Lynkk does not own the brand "Lynkk"

| Issue | The brand SERP is contested by at least five unrelated entities and there is no entity disambiguation |
|---|---|
| **Impact** | High |
| **Evidence** | A search for "Lynkk" returns, as ranked results: LYNKK LTD on UK Companies House, Instagram @lynkkup, X @LynkkHQ, a Facebook page, the musicians Lynkk da Missin (Apple Music, Spotify) and LYNKK (SoundCloud), and lynkk.ai. A crypto and bill-payment brand of the same name, described as Lagos-based, appeared in a result summary rather than as a ranked result, so treat that one as unconfirmed. Separately, two different titles were returned for the lynkk.ai homepage across searches: "Lynkk: AI Meeting Notes & Conversation Intelligence" and "Lynkk: Record any conversation. Get notes, tasks, and answers." |
| **Diagnosis** | Two problems. Google has no strong entity for Lynkk the software company, so it cannot confidently disambiguate from the namesakes. The two titles have two possible explanations and they need different responses: either Google is rewriting the declared title, which says it does not think that title answers the query, or the title was genuinely changed on the site between crawls and both versions are still cached. Check the live `<title>` before concluding which. `memory/lynkk-brand.md` already warns against confusion with Lynk, Lynk AI, Linnk AI and Link AI: the namesakes found here (LYNKK LTD, the Nigerian fintech, the musicians) are a different and more literal collision, because they share the exact spelling. |
| **Fix** | Add Organization and SoftwareApplication JSON-LD on the homepage with `name`, `url`, `logo`, `description`, `applicationCategory`, and a `sameAs` array listing every owned profile: X, Instagram, Facebook, LinkedIn, Product Hunt, YouTube, and the Companies House entry if LYNKK LTD is in fact the operating company. Build an `/about` page naming the legal entity, founding year, HQ and founders. Keep one title, and make it the one that survives rewriting. |
| **Priority** | 1 |
| **Blocked on** | Company legal name, founding year, HQ, founders, and confirmed social links. All open items in `memory/lynkk-brand.md`. Confirm first whether the X, Instagram and Facebook accounts found are Lynkk's own and not namesakes: putting someone else's profile in `sameAs` actively worsens the disambiguation. |

### Finding O3: product claims in the wild are not in the brand memory

| Issue | SERP snippets surface product facts absent from `memory/lynkk-brand.md` |
|---|---|
| **Impact** | Low (process), Medium (content raw material) |
| **Evidence** | Snippets referenced: conversations are never used to train anyone's model; automatic meeting detection that offers to record; capturing the room and remote participants simultaneously; continuing to work when the window is closed; the ability to start when the Mac starts. |
| **Diagnosis** | These are strong, specific, differentiating claims. "Never used to train anyone's model" in particular is a top-tier trust signal in 2026 and is exactly the kind of declarative statement AI surfaces quote. They are live on the site but absent from the brand file, so every piece of copy written from that file omits them. |
| **Fix** | Add them to `memory/lynkk-brand.md` once verified against the live site. Then use them: they belong in the homepage FAQ, in a security and privacy page, and in the directory submissions. |
| **Priority** | 3 |

---

## Part 3: Content and architecture findings

Confirmed URLs, from the export: `/`, `/how-it-works`, `/download`, `/terms`,
`/privacy`, `/refund`, `/features/hinglish-transcription`,
`/features/meeting-bot`, `/features/knowledge-graph`, `/features/action-items`,
`/use-cases/sales-calls`, `/use-cases/team-standups`.

The URL structure itself is good: lowercase, hyphenated, readable, logically
nested, no parameters or session IDs. Keep it.

### Finding C6: no evidence of the page types this category expects

| Issue | Page types that this category expects could not be confirmed to exist |
|---|---|
| **Impact** | High if the pages are missing, Medium if they exist but are never cited |
| **Evidence** | Nothing resembling `/pricing`, `/blog`, `/about`, `/integrations`, `/security`, or any comparison or alternatives page appeared in 92 days of Search Console data or across nine searches. |
| **Confidence** | **Low, and this is the weakest finding in the report.** The Search Console export lists only pages cited in AI surfaces, so a pricing page could exist and simply never have been quoted in an AI answer. The searches were US-only. **Check the sitemap before acting on this.** If the pages do exist, this finding converts into a much narrower one: they exist but are not being surfaced, which is a quality and linking problem rather than a build problem, and the fix is to improve them rather than to write them. |
| **Diagnosis** | This maps almost exactly onto the known failure mode for SaaS sites: thin feature pages, no comparison or alternatives pages, no educational content, and a blog that is either missing or disconnected from the product pages. |
| **Fix** | Build in this order, highest commercial intent first. |
| **Priority** | 1 |

**Build order.**

1. **`/pricing`.** The highest-intent commercial query for any SaaS brand, a
   frequent AI Overview trigger, and the thing every directory submission asks
   for. Blocked on the paid tier names, prices and free-tier limits, which are
   the first open item in `memory/lynkk-brand.md`.

2. **Comparison pages.** `/vs/otter`, `/vs/fireflies`, `/vs/granola`,
   `/vs/fathom`, `/vs/tldv`, plus `/alternatives/otter` and similar. These rank,
   they convert, and they are cited in AI answers. Write them honestly, including
   where the competitor wins, because that is what makes them credible and
   quotable. The Product Hunt checklist already anticipates the "how is this
   different from Otter/Fireflies?" question: that answer is a page, not a
   comment.

3. **Integration pages**, one each: Jira, Calendly, Cal.com, Google Calendar,
   MCP, and each supported CRM. "[Tool] + [integration]" is a reliable
   long-tail pattern with genuine intent behind it. Blocked on which CRMs and
   which meeting platforms are actually supported, both open items in the brand
   file.

4. **`/security`, or a data residency page.** Lynkk's strongest differentiator
   against tl;dv and HappyScribe, both of which currently own the EU-data story.
   Per-region model processing is a better answer than "we are in the EU", and
   nobody can find it.

5. **`/about`.** Pure E-E-A-T and entity disambiguation: legal entity, founders,
   founding year, HQ, contact. Also fixes Finding O2.

6. **Feature pages for the features that have none.** Four exist. The brand file
   describes at least eight more: the live voice assistant, pre-meeting context,
   in-person recording, dictation, offline-first capture, multilingual capture,
   CRM field updates, data residency.

7. **Use-case pages beyond the two that exist.** The brand file names five
   segments: sales and customer-facing teams, product and engineering, founders
   and consultants, regulated industries, multilingual and global teams. Two are
   built.

8. **A blog or resource hub**, internally linked to the feature pages rather
   than stranded on a subdomain or a separate CMS.

### Finding C7: the two best-performing pages have no cluster around them

| Issue | `/features/hinglish-transcription` and `/features/meeting-bot` each earn 10 impressions and each stands alone |
|---|---|
| **Impact** | Medium |
| **Evidence** | `Pages.csv`. These two pages together earn 17% of the site's AI-surface impressions, versus 62% for the homepage and under 6% each for everything else. |
| **Diagnosis** | Both sit in genuinely competitive niches with real search demand, confirmed by the independent searches. They are the proven demand signal on this site, and neither has supporting content, internal links from related pages, or a topical cluster. |
| **Fix** | Build a cluster around each. For meeting bot: per-platform pages (Zoom, Google Meet, Teams), bot versus bot-free capture, how to record without the bot joining. For Hinglish: per-language pages, code-switching explained, India-specific content. Cross-link the cluster into the hub page with descriptive anchor text. |
| **Priority** | 2 |
| **Blocked on** | Supported meeting platforms, an open item in the brand file. |

### Finding C8: several content fixes are blocked on unanswered product facts

| Issue | `memory/lynkk-brand.md` carries a nine-item "to confirm" list, and most of it blocks SEO work |
|---|---|
| **Impact** | Medium (blocks other work) |
| **Evidence** | The file's own checklist: pricing, platform availability, supported meeting platforms, which CRMs, number of languages, available data regions, company legal name and founders, social links, and logo and screenshot assets. |
| **Diagnosis** | These are not marketing niceties. Pricing blocks the pricing page. Supported platforms block the integration and meeting-bot clusters. Languages and regions block the India cluster and the data residency page. Company details and social links block the entity and schema work. Logo files block the directory submissions. |
| **Fix** | Get the list answered as one task. It is probably an afternoon of internal questions and it unblocks most of the action plan. |
| **Priority** | 1 |

---

## Part 4: AI and generative search readiness

This deserves its own section because the only performance data available is,
literally, the AI features report. Lynkk is already being surfaced there. That
channel is live, and it is the one channel where a small site can beat a large
one, because citation is about being quotable rather than being authoritative.

**What the data proves:** Google is willing to cite lynkk.ai in AI answers, 105
times across 92 days, across 34 countries.

**What the data implies:** it prefers to cite the homepage (62%) and the terms of
service (6 impressions) over the feature pages. That is a statement about which
pages are quotable.

### Checks to run once the crawl is unblocked

The SEOmator `geo` category (13 rules) and the `schema` category (19 rules)
cover most of this.

- **`/llms.txt`.** Cheap, and this category's audience will look for it.
- **AI crawler access in robots.txt.** Check `GPTBot`, `OAI-SearchBot`,
  `ClaudeBot`, `PerplexityBot`, `Google-Extended`, `Applebot-Extended`,
  `CCBot`, `Bytespider`. One nuance worth getting right: blocking
  `Google-Extended` does **not** remove a site from AI Overviews, which run on
  regular Googlebot. Blocking `OAI-SearchBot` or `PerplexityBot` does remove it
  from those products. Decide deliberately rather than by default.
- **Structured data.** Check for Organization, SoftwareApplication, FAQPage,
  BreadcrumbList, and Product or Offer once pricing exists.
- **Semantic HTML.** Real `<h1>`, `<article>`, `<section>`, `<table>`, `<dl>`.
  Extraction depends on it.

**A detection caveat that matters here.** Never conclude "no schema found" from
`curl` or a page fetch. Both strip or skip `<script>` tags, and JSON-LD is
frequently injected by JavaScript. Use a real render. `scripts/run-seo-audit.sh`
pulls JSON-LD from the rendered DOM with Playwright for exactly this reason, and
the Rich Results Test at https://search.google.com/test/rich-results is the
manual equivalent.

### Content changes that increase citation rate

- One FAQ block per page, with questions phrased the way people ask them and
  answers that stand alone in two or three sentences.
- Specific, checkable claims instead of adjectives. "Within 30 seconds" is
  already good. "Powerful AI" is not quotable by anything.
- Comparison tables. AI surfaces lift tables directly.
- Dates on pages, and a visible last-updated stamp.
- Named sources and named integrations rather than "your favourite tools".

---

## Part 5: The technical audit, pending

None of this was measurable. It is the highest-priority block of work because a
single indexation bug can outweigh every content decision above. Run
`scripts/run-seo-audit.sh` and work the output against this list.

**Tier 1, indexation blockers.** Check first, because nothing else matters if
these are wrong.

- `robots.txt`: unintentional `Disallow` rules, sitemap reference present
- `sitemap.xml`: exists, reachable, lists only canonical indexable URLs, no
  404s or redirects inside it, `lastmod` values honest
- `noindex` on anything that should rank
- Canonical tags: present, self-referencing, absolute, https, consistent on
  www versus non-www and on trailing slashes
- Redirect chains and loops, http to https, www consolidation
- Soft 404s and a real 404 page
- Orphan pages: `--crawl` measures click depth and inbound internal links,
  which is the check that would confirm or kill the Finding C1 diagnosis

**Tier 2, rendering.** Suspected root cause of the thin-content pattern.

- Does the main content exist in the raw HTML, or only after JavaScript runs
- Raw versus rendered DOM diff
- Console errors and failed subresource requests. An uncaught exception halts
  the script that threw it, so canonical tags, structured data or copy that
  script would have written never reach a rendering crawler, and static HTML
  analysis cannot see it
- Mobile parity: content, title, canonical, structured data and links, desktop
  render versus mobile render. Relevant to Finding C4

**Tier 3, performance.** 10% of the score and a real ranking factor.

- LCP under 2.5s, CLS under 0.1, TTFB under 800ms, FCP under 1.8s
- INP is never measured by a crawler, because it needs real interaction. Take it
  from CrUX or RUM instead. Do not accept a tool that claims to measure it.
- Image formats and compression, lazy loading, font loading, caching, CDN

**Tier 4, the rest.** Security headers and HSTS and CSP and mixed content;
image alt text; internal link structure and anchor text; broken links;
accessibility; HTML validity; Open Graph and Twitter cards; hreflang, if any
locales exist or are planned.

**How to read the score.** Category weights are in
`.claude/skills/seomator-audit/references/rules.md`. Two traps. First, a check
whose input could not be measured carries weight 0 and quietly leaves the
average, so a high score can hide a large unmeasured gap. Second, a `--no-cwv`
run is not comparable to a full run, because a different rule set produced the
number. The script always runs the full version.

---

## Prioritised action plan

### Now: unblock and measure

1. Allow `lynkk.ai` in the environment's network settings, then run
   `scripts/run-seo-audit.sh`. Fix any Tier 1 indexation finding the same week.
2. Re-export Search Console without the Generative AI filter, with all four
   metrics and the Queries tab, for 3 months and 16 months.
3. Answer the nine open items in `memory/lynkk-brand.md`. Most of the plan below
   is blocked on them.

### Weeks 1 to 2: quick wins

4. Organization and SoftwareApplication JSON-LD with a verified `sameAs` array. (O2)
5. `/pricing`. (C6)
6. FAQ blocks on the homepage and all four feature pages. (C2, Part 4)
7. `/llms.txt`, and an audit of AI crawler rules in robots.txt. (Part 4)
8. Directory submissions: Product Hunt using the drafted copy, There's An AI For
   That, G2, Capterra, Futurepedia. (O1)
9. Settle on one homepage title and stop Google rewriting it. (O2)

### Weeks 3 to 8: close the content gap

10. Rewrite the four feature pages and two use-case pages to be answer-shaped:
    specifics, tables, limits, named integrations. (C2)
11. Comparison pages against Otter, Fireflies, Granola, Fathom and tl;dv. (C6)
12. `/security` or a data residency page. It is the strongest differentiator and
    it is invisible. (C6)
13. `/about` with the legal entity, founders and founding year. (O2, C6)
14. The India and multilingual cluster, starting from the Hinglish page. (C3, C7)
15. The meeting bot cluster: one page per supported platform. (C7)

### Quarter 2 and beyond

16. Integration pages, one per integration. (C6)
17. Feature pages for the eight-plus features that have none. (C6)
18. Use-case pages for the three unserved segments. (C6)
19. A blog or resource hub, internally linked to the product pages. (C6)
20. Outreach to the listicle authors, with the in-person, data residency and
    Hinglish angles as the hook. (O1)
21. Re-audit with `seomator compare lynkk.ai` after each significant deploy, and
    gate CI on `--fail-on-regression`.

---

## Appendix: reproducing this audit

```bash
# Once, per machine
npm install -g @seomator/seo-audit
seomator self doctor

# Full technical audit, writes to audit/raw/<date>/
scripts/run-seo-audit.sh https://lynkk.ai 100

# After a deploy
seomator compare lynkk.ai --json
```

Skills used: `.claude/skills/seo-audit` (framework, on-page, content,
prioritisation) and `.claude/skills/seomator-audit` (the CLI, 373 rules across
20 categories). Both are installed in this repo and described in
`memory/seo-toolkit.md`.

Data: `memory/data/gsc-ai-features-2026-09-27/`.
Findings carried into memory: `memory/lynkk-seo-baseline.md`.

---

## Errata: corrections made 2026-09-28

Re-verified every numeric claim against the source CSVs. Seven corrections,
listed so anyone who read the first version can see what moved.

| # | Was | Now | Why |
|---|---|---|---|
| 1 | "Growth has stalled because Google has run out of Lynkk pages to cite" | "Growth is strong; the footprint is concentrated" | Not supported. Consecutive 14-day totals are 0, 5, 11, 19, 34, 34: five growth periods, one flat. Monthly impressions per day went 0.23, 1.26, 2.46 and is still climbing. One flat fortnight at n=34 is inside the noise, and the original claim inverted the story. |
| 2 | "12 URLs account for 100% of AI-surface impressions" | "Only 12 URLs have been cited in AI surfaces at all" | `Pages.csv` is headed "Top pages". It is a ranked list, so it cannot establish a 100% share or prove no other URL was cited. |
| 3 | Finding C6 asserted the missing pages "are not present" | Reframed as "could not be confirmed to exist", with a Low confidence row | The export lists only AI-cited pages, so a pricing page could exist and simply never have been quoted. The original wording asserted a fact not in evidence. |
| 4 | "more than five times the US" | "more than seven times the US" | 37 divided by 5 is 7.4. |
| 5 | "under 4% each for everything else" | "under 6% each" | `/terms` is 6 of 117, which is 5.1%. |
| 6 | Broken links, images and accessibility "15% of the score combined" | 23% | Links 8% plus images 8% plus accessibility 7%. |
| 7 | Method section listed no limitations | Three limits stated up front | The searches were US-only while India is 35% of impressions; `Pages.csv` is a top-N list; the export covers AI surfaces only, not ordinary Search. |

Also softened: the Lagos crypto namesake is now marked unconfirmed (it came
from a result summary, not a ranked result), and the two-titles observation now
gives both explanations rather than assuming Google rewrote the title.

### Still unverified, because the site is unreachable

Every item in Part 5 remains unchecked, and `robots.txt`, `sitemap.xml` and
`llms.txt` are among them. Outbound web access from this environment is still
denied for every host. No claim about those files, or about anything requiring
a page fetch, appears anywhere in this report.
