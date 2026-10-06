# Lynkk competitor growth audit and plan: SEO, content, social, backlinks, Reddit, AEO/GEO

> Prepared 2026-10-06. Covers Otter, Fireflies, Fathom, Granola, Read AI, tl;dv, Jamie, and the new
> "AI that speaks in your meeting" entrants (Otter Meeting Agent, Talk to Fireflies, Mina).
> Data sources: Ubersuggest (US organic estimates, Sep 2026 snapshot), live web search, public press.
> All traffic numbers are tool estimates. Use them for direction and relative size, not as exact figures.
> See "Data notes" at the end for caveats.

---

## 1. TL;DR

1. **Lynkk is starting from zero in search and AI answers.** Domain authority 1, 3 backlinks (all nofollow),
   1 ranking keyword ("zoom meeting bot", position 39), roughly 0 organic visits. A web search for "lynkk.ai AI meeting"
   returns other companies (Lynq, Lynk, a Linktree clone also called "Lynkk"). AI engines cannot recommend
   what they cannot find or disambiguate. Fixing indexability and entity identity is step one.
2. **Generic blog SEO is collapsing for everyone in this category.** Since late 2024 / early 2026, ranking keyword counts fell
   about 80-90% at Fireflies (96K to 18.6K), Otter (126K to 14K), Read AI (97K to 9K) and tl;dv (58K to 13.6K).
   The off-topic posts that used to pull traffic ("team name ideas", "how to download YouTube audio",
   "WFH meaning") are exactly what got hit. Lynkk should not copy that playbook.
3. **What still works: brand demand, tool pages, comparisons, and being in other people's lists.**
   Fathom gets about 154K US organic visits a month, nearly all from people searching "fathom" (90,500 searches/mo).
   Granola grew from about 4K to 39K-88K monthly organic visits with almost only branded keywords.
   Otter's best non-brand pages are free tools (audio-to-text, AI transcription).
4. **AI answers are decided by third parties.** In ChatGPT/Perplexity/AI Overviews, the category leaders by share of voice are
   Otter (~53%), Fireflies (~51%), Fellow (~28%), Fathom (~24%) (Parse, Oct 2025 to Apr 2026, 6,235 answers).
   Those engines lean heavily on Reddit, G2, LinkedIn, YouTube, Wikipedia and editorial "best of" lists
   (editorial lists drive roughly 41% of ChatGPT recommendations per Parse). The Google top 10 for
   "best ai note taker" is a Medium post, a Reddit thread, Zapier, PCMag, Wired and four competitor blogs.
5. **Lynkk's headline differentiator is now contested.** Otter shipped a voice-activated Meeting Agent (2025),
   Fireflies shipped "Talk to Fireflies" with Perplexity (2025), and **Mina** won #1 Product of the Day on
   Product Hunt (June 2026) with almost the same pitch as Lynkk: "speaks during calls, before, during and after meetings."
   Lynkk needs to lead with the combination nobody else owns (see section 6).
6. **The opening:** privacy backlash (class actions against Otter and Fireflies over auto-joining bots), demand for
   in-person capture (growing search demand), data residency (only small EU players like Jamie own it today),
   and "meetings that do the work" (Jira tickets, CRM fields). Lynkk can be the clear answer for these in both Google and AI engines
   within 6 months, while the big players fight over "best AI note taker."

---

## 2. Lynkk baseline (Sep/Oct 2026)

| Metric | Lynkk | What "good" looks like in 6 months |
|---|---|---|
| Domain authority (Ubersuggest) | 1 | 20+ |
| Referring domains | 3 (all nofollow) | 150+ (with 30+ dofollow from relevant sites) |
| Ranking keywords (US) | 1 | 300+ |
| Est. organic visits / mo | ~0 | 3,000-5,000 |
| Indexed in web search for brand query | No (other "Lynk/Lynq/Lynkk" brands appear) | Lynkk owns page 1 for "Lynkk" and "Lynkk AI" |
| G2 / Capterra reviews | Not found | 50+ reviews, 4.7+ |
| Mentions in AI answers for category prompts | Not found | Mentioned in 10-20% of tracked prompts |

Known pages: `/features/meeting-bot` is the only URL ranking for anything.
The site could not be fetched directly from this environment, so on-site items in section 7.1 are a checklist to verify.

**Name collision is a real AEO problem.** Search results confuse Lynkk with: Lynq AI (relationship manager),
Lynk AI (data modeling), LynkAI (Shopify app), Lynkt (company brain / MCP), and a "Lynkk" Linktree alternative on Peerlist.
LLMs merge entities with similar names. Every profile, schema block and description must say
"Lynkk, the AI meeting assistant (lynkk.ai)" consistently.

---

## 3. Competitive landscape

### 3.1 Who matters and why

| Tier | Company | Why they matter to Lynkk |
|---|---|---|
| Incumbents | **Otter.ai** | Biggest SEO footprint, $100M ARR (Mar 2025), 25M+ users, has a voice "Meeting Agent." Facing consent lawsuits. |
| | **Fireflies.ai** | $1B+ valuation (Jun 2025), 20M users, most cited in some AI answer studies, "Talk to Fireflies" voice + Perplexity. Facing BIPA suits. |
| | **Fathom** | #1 on G2 (5.0, thousands of reviews), free unlimited recording, $1M to $30M ARR 2023-2025. Brand-search juggernaut. |
| | **Read AI** | 5M MAU, viral meeting reports, "zero media spend" growth, digital twin "Ada", MCP + meeting agent. |
| Fast riser | **Granola** | $125M Series C at $1.5B (Mar 2026). Bot-free, loved on Reddit, brand-led (rebrand + OOH in SF/NYC/London). MCP since Feb 2026. |
| SEO challengers | **tl;dv**, **Jamie**, **Lindy**, **Bluedot**, **Notta**, **MeetGeek** | Publish heavy comparison/listicle content that ranks and gets cited. Jamie owns EU/GDPR. |
| Direct pitch overlap | **Mina**, Otter Meeting Agent, Talk to Fireflies, Read AI meeting agent | All claim "AI participant that speaks in meetings." |

### 3.2 Scorecard (Ubersuggest, US, Sep 2026)

| Domain | DA | Referring domains | Backlinks | Est. US organic visits/mo | Ranking keywords (peak to now) | Brand search volume (US) |
|---|---|---|---|---|---|---|
| otter.ai | 66 | 29,146 | 330,847 | 431K (peak ~1.09M Feb 2026) | 126K to 14.2K | high ("otter ai" variants) |
| read.ai | 47 | 3,429 | 33,861 | 606K (inflated: ~145K from the word "read") | 97K to 9.4K | medium |
| fathom.ai | 45 | 5,667 | 31,557 | 154K (almost all brand) | 23K to 1.3K | "fathom" 90,500; "fathom note taker" 8,100 |
| tldv.io | 44 | 6,356 | 150,613 | 83K (was 187K Oct 2024) | 58.7K to 13.6K | "tldv" 2,400 |
| fireflies.ai | 53 | 14,782 | 109,749 | 71K (was 404K Oct 2024) | 96K to 18.6K | "fireflies ai notetaker" 4,400 |
| granola.ai | 47 | 5,139 | 70,579 | 39K (was ~4K Oct 2024; peak 89K May 2026) | 29.6K to 1.8K | "granola app" 4,400 |
| **lynkk.ai** | **1** | **3** | **3** | **~0** | **1** | **not measurable** |

**How to read this:** the losers lost long-tail blog traffic; the winners kept or grew branded demand.
Fathom and Granola have small keyword footprints but strong, growing traffic because people search for them by name.

### 3.3 AI answer share of voice (AEO/GEO)

| Source | Finding |
|---|---|
| Parse (6,235 ChatGPT + Google AI answers, Oct 2025 to Apr 2026) | Otter 53.1%, Fireflies 51.0%, Fellow 28.4%, Fathom 24.3% share of voice for AI meeting assistant prompts |
| AnswerPeek (12 buying questions, ChatGPT + Perplexity) | Fireflies 12.2% (named in 15 of 24 answers), Fathom 8.9%, Otter 8.1%, Fellow 5.7%, Granola 5.7% |
| Citation studies 2026 (Peec, 5W, Contently) | Reddit is the #1 cited domain across ChatGPT, AI Mode, Gemini, Perplexity, AI Overviews. Perplexity also leans on LinkedIn and G2 for B2B. ChatGPT leans on Wikipedia, Reddit, LinkedIn, Forbes, Medium. |

Note that **Fellow** punches far above its SEO weight in AI answers. Its "26 Best AI Meeting Assistants" guide and
ChatGPT-plugin roundups are cited often. This is the clearest proof that a few deep, frequently updated listicles can win AEO.

### 3.4 Google SERP for "best ai note taker" (US, Jul 2026)

1. Medium / Towards AI: "I ranked the 5 best free AI note-takers"
2. Reddit r/AI_Agents: "What is actually the best AI note taking app for meetings?"
3. Zapier: "The 11 best AI meeting assistants in 2026"
4. PCMag: "Best AI note-taking apps we've tested"
5. Video carousel
6. voicetonotes.ai blog
7. Wired: "5 best AI notetakers (2026)"
8. lindy.ai blog
9. meetjamie.ai blog
10. "What people are saying" (Reddit/forum perspectives)
12. tldv.io blog

Takeaway: the head term is won by **publishers, Reddit and competitor listicles**, not by product homepages.
Lynkk's job is to get **into** those pages (and the Reddit thread), not to outrank them in year one.

---

## 4. Competitor playbooks (what each one actually does)

### Otter.ai
- **Website/SEO:** strongest link profile in the category (29K referring domains). Top non-brand pages are **free tool landing pages**:
  `/audio-to-text`, `/free-ai-transcription`, `/video-to-text`, `/speech-to-text`, `/podcast-transcription`, `/mp4-to-text`.
  Each targets a high-volume utility query ("audio to text" is 12,100/mo, "ai transcription" 5,400/mo).
- **Content:** "Is it illegal to record someone without permission?" pulls ~1,300 visits/mo. Writes competitor pieces
  ("5 best Granola AI alternatives") to intercept rival brand demand.
- **Product/PR:** big launch moments (Meeting Agent, $100M ARR announcement) generate press links.
- **Weak spots:** lost ~90% of ranking keywords in 2026; reputational risk from consolidated class action (Brewer v. Otter.ai,
  consolidated Oct 2025) over auto-joining and recording without consent; visible bot is its top Reddit complaint.

### Fireflies.ai
- **Content:** historically a volume machine. Its #2 page is still "200+ Team Name Suggestions"; others include
  YouTube download guides, memes, quotes. This drove 400K visits/mo in 2024 and is now mostly gone (71K).
- **Social/creators:** runs a structured influencer program across YouTube, TikTok, LinkedIn and Instagram,
  and converts power users into affiliates/ambassadors (per its hiring posts).
- **Partnerships for PR + AEO:** Perplexity partnership (voice web search in meetings, Fireflies data inside Perplexity),
  $1B valuation story. Official MCP server. First-party Claude connector.
- **Founder story as marketing:** the "Fred from Fireflies" origin (founders manually took notes pretending to be AI) went viral on X.
- **Weak spots:** BIPA class actions (Cruz v. Fireflies.AI, Dec 2025); AI credits capped per tier; visible bot.

### Fathom
- **Growth engine:** product-led, free unlimited recording forever. Absorbed ~$50/user/mo losses early to buy goodwill.
  Started as one of ~50 apps in the **Zoom App Marketplace**.
- **Reviews as moat:** #1 on G2 with a perfect 5.0 across thousands of reviews. G2 is a core Perplexity source.
- **SEO:** tiny keyword footprint but huge branded demand. Clean `/vs/fireflies` comparison pages that rank #2.
  Moved domain from fathom.video to fathom.ai (signal: "AI" in the entity).
- **Lesson for Lynkk:** reviews + a generous free tier + marketplace distribution beat blogging.
- **Update (Sep 14, 2026): acquired by Superhuman** (formerly Grammarly) to feed its Go assistant and agents with meeting context.
  400K+ monthly users. The free plan is unchanged "for now," with no long-term statement. Fireflies published a
  "what it means for Fathom users" post within days. Expect switching questions on Reddit and in AI answers ("Fathom alternative").

### Granola
- **Brand-led growth:** distinctive, warm, "human" brand; rebrand + first OOH campaign; Ramp data showed it as the
  second-fastest-growing software brand the month after. Founder-led LinkedIn content (founder stories, behind the scenes);
  hiring a Content Lead specifically for that.
- **Community:** strongest organic Reddit sentiment in the category, driven by "no bot joins your call."
- **Content:** few but high-intent posts: pricing comparison vs Fireflies/Fathom/Otter (ranks for "granola vs fireflies"),
  enterprise data residency explainer, how-to guides for its own product.
- **Ecosystem:** Granola MCP (Feb 2026) for Claude, ChatGPT, Cursor; expanded to v0, Lovable, Attio, ChatPRD.
  Gets listed in every "MCP for meetings" roundup.
- **Weak spots:** free tier runs out fast (common Reddit complaint); note-pad first, no live voice assistant.

### Read AI
- **Viral loop:** every meeting produces a shareable report that non-users see; claims 100K new accounts/week at peak with
  zero media spend.
- **SEO:** ranks #2 for "ai powered meeting assistant" (40,500/mo) and #4 for "ai notes taker" (27,100/mo) with the homepage.
  `/articles` hub publishes rival-intercept content: "Fireflies alternatives" (#2), "Granola pricing alternatives".
- **Product narrative:** "Ada" email digital twin, MCP server, dispatchable meeting agent.

### tl;dv
- **Comparison factory:** "honest review of Fathom" ranks for "fathom note taker" (8,100/mo); also Gong, Notta, Fyxer, Vomo,
  Tactiq reviews and alternatives. Landing page owns "meeting recorder" (#1, 1,900/mo).
- **Legal-news content:** "TL;DR of the Otter.ai lawsuit" explainer turns a competitor's problem into traffic.
- **Weak spots:** off-topic posts (WFH meaning, Zoom backgrounds) are decaying; traffic down ~55%.

### Jamie (meetjamie.ai)
- Owns the **EU / GDPR / bot-free** content cluster ("European AI meeting assistants", "GDPR note takers in Europe",
  "European note takers for Zoom"). Ranks #9 for "best ai note taker." Frankfurt processing, ISO 27001, DORA-ready.
- **Lesson for Lynkk:** a narrow, trust-based niche can be owned with ~10 strong pages. Lynkk's "pick any region" claim is
  broader than Jamie's EU-only story.

### Mina (new, direct overlap)
- #1 Product of the Day on Product Hunt (June 1, 2026, ~400-450 upvotes). Pitch: "AI teammate that responds and executes
  during your calls... before, during, and after meetings." This is Lynkk's pitch almost word for word.
- **Implication:** "joins and speaks" is no longer enough on its own. Lynkk needs proof (demos, numbers) and the extra
  pillars: in-person + offline, data residency, Jira/CRM execution in 30 seconds.

---

## 5. Cross-cutting patterns (what is working, what is not)

| Working in 2026 | Fading in 2026 |
|---|---|
| Branded demand (Fathom, Granola) | Off-topic traffic posts (team names, memes, YouTube downloaders) |
| Free utility tool pages (Otter transcription tools) | Thin "ultimate guide" content written for keywords |
| Honest "vs" and "alternatives" pages (Fathom, Read AI, tl;dv, Granola) | Listicles that rank yourself #1 with no tradeoffs (AI engines skip them) |
| Reviews on G2/Capterra (Fathom) | Paid search on head terms ("ai note taker" paid difficulty 100, CPC ~$14) |
| Reddit presence and sentiment (Granola) | Undisclosed promotion on Reddit (gets called out, hurts sentiment) |
| Marketplace distribution (Zoom, MCP directories) | |
| Product viral loops (Read AI reports, shared notes) | |
| Founder-led LinkedIn + creator videos | |
| Trust narratives (consent, residency) amid lawsuits | |

---

## 6. Where Lynkk can win (positioning for search and AI answers)

AI engines answer by matching a prompt's constraints to brands that are **repeatedly described** with those constraints
across many sources. Lynkk should pick 4 constraint combos that competitors do not own and repeat them everywhere.

| Wedge | Prompt it should win | Who is weak there today | Lynkk proof needed |
|---|---|---|---|
| **1. Data residency, any region** | "AI note taker that keeps data in the EU / India / my region", "GDPR compliant meeting assistant", "AI notetaker for regulated industries" | Otter, Fireflies (US-centric, lawsuits); Jamie only EU | List of regions, which models run where, DPA, subprocessor list, security page |
| **2. In-person + offline-first** | "AI note taker for in-person meetings" (480 to 720/mo, rising), "record meetings without internet", "AI notes for interviews / field visits" | Bot-first tools (Fathom, tl;dv, Read) | Mac + mobile capture demo, offline mode explainer |
| **3. Meetings that do the work** | "Turn meeting notes into Jira tickets automatically", "AI that updates CRM after calls", "meeting to Jira" | Mostly generic integrations pages | 30-second video: meeting ends, Jira tickets + CRM fields appear |
| **4. Live voice context in the meeting** | "AI assistant that answers questions during meetings", "live AI meeting assistant" (170/mo, Otter #2) | Otter, Fireflies, Mina compete here | Side-by-side demo, latency numbers, "speaks only when asked" consent design |

**Umbrella line for all four (use everywhere, including schema and profiles):**
"Lynkk is the AI meeting assistant for the whole meeting: context before, a voice assistant during, and notes, Jira tickets
and CRM updates within 30 seconds after. Online or in person, offline-first, with your data processed in the region you choose."

Also lean into **consent-first** design as a brand value (clear disclosure when Lynkk joins, easy opt-out for guests).
Given the Otter and Fireflies lawsuits, this is both ethical and a differentiator AI engines will repeat if it is written down clearly.

---

## 7. Plan by channel

### 7.1 Website and technical foundations (weeks 1-3, do first)

Search and AI crawlers must be able to read the site. Lynkk is barely indexed today.

- [ ] Verify Google Search Console **and Bing Webmaster Tools** (ChatGPT search and Copilot draw on Bing's index). Submit sitemap.
- [ ] Confirm pages render as HTML without JavaScript (SSR/SSG). If the marketing site is a client-side SPA, AI crawlers see an empty page.
- [ ] `robots.txt`: allow Googlebot, Bingbot, `OAI-SearchBot`, `ChatGPT-User`, `GPTBot`, `PerplexityBot`, `ClaudeBot`, `Google-Extended`, `Applebot`. Decide on training bots deliberately, but never block the search/retrieval bots.
- [ ] Add `/llms.txt` with a plain summary of Lynkk, key pages, pricing, regions and integrations.
- [ ] Schema: `Organization` (with `sameAs` to LinkedIn, X, YouTube, G2, Crunchbase, Product Hunt, Wikidata), `SoftwareApplication` (with `offers`, `operatingSystem`, `applicationCategory`), `FAQPage` on key pages, `BreadcrumbList`.
- [ ] Title tag and H1 that include the entity: "Lynkk: AI Meeting Assistant & Notes" (avoid a bare "Lynkk").
- [ ] **Pricing page in plain HTML** with plan names, prices and free-tier limits. "How much is X" and "is X free" are top AI and Google queries for every competitor (Granola, Otter, Fireflies all rank #1-2 for these).
- [ ] **Facts page** (`/about` or `/press`): founding year, HQ, founders, product list, platforms, regions, certifications, logos. AI engines quote these pages.
- [ ] **Trust/security page:** data regions, which models run where, retention, consent behavior, subprocessors, DPA, certifications (or roadmap).
- [ ] Core Web Vitals pass on mobile.
- [ ] Page architecture to build (each is a landing page, not a blog post):
  - `/features/*` (before, during, after, dictation, in-person, offline, knowledge graph)
  - `/integrations/*` (jira, hubspot, salesforce, google-calendar, outlook, calendly, cal-com, zoom, google-meet, teams, mcp)
  - `/use-cases/*` (sales, product, engineering, consulting, recruiting, founders, regulated industries)
  - `/vs/*` and `/alternatives/*` (see 7.2)
  - `/regions/*` or `/data-residency` (EU, UK, US, India, others confirmed)
  - `/tools/*` (free tools, see 7.2)
  - `/changelog` (fresh dated content AI engines see as recency signals)

### 7.2 Content (start week 2, ongoing)

Rule: **every piece must be something only a meeting-assistant company could credibly publish.** No team-name lists.

**A. Comparison and alternatives pages (highest ROI, highest AEO value)**
Write honest pages with a TL;DR, a comparison table, "who should pick which," and real tradeoffs (AI engines skip pages that claim to win everything).

| Page | Target query (US vol) |
|---|---|
| /alternatives/otter | otter ai alternative (480) |
| /alternatives/granola | granola alternative (320, CPC $20.94) |
| /alternatives/fireflies | fireflies alternatives (110) |
| /alternatives/fathom | fathom alternative |
| /vs/otter, /vs/fireflies, /vs/granola, /vs/fathom, /vs/read-ai, /vs/mina | "[x] vs [y]" (fathom vs fireflies: 110, CPC $43.71) |
| /blog/fathom-vs-fireflies-vs-otter-vs-lynkk | multi-way buyer comparisons |
| /alternatives/bot-free-note-takers | bot-free / no-bot prompts (low search, high AI prompt use) |

**B. Wedge landing pages + supporting guides (section 6)**
- "AI note taker with data residency: how regions work" + one page per region
- "GDPR-compliant AI meeting assistant: checklist" (compete with Jamie, broader than EU)
- "AI note taker for in-person meetings" (480 to 720/mo, SD 40)
- "How to turn meeting notes into Jira tickets automatically"
- "Auto-update HubSpot / Salesforce after sales calls"
- "Live AI meeting assistant: ask questions during the call"

**C. Free tools (link magnets + utility traffic)**
- **Recording consent law checker** by country and US state (Otter's single legal post gets ~1,300 visits/mo; global coverage fits the residency story and the lawsuit news cycle).
- **Meeting cost calculator** (attendees x salary x duration) with "save X hours with Lynkk."
- **Meeting notes / action items template generator** (one-page, no signup).
- Optional later: free audio-to-text upload (12,100/mo, but Otter dominates; only if cheap to run).

**D. Original data (digital PR + AEO citations)**
- Quarterly "State of Meetings" report from aggregated, anonymized, consented usage data: % of meetings with open action items, follow-up latency, in-person vs online share, language mix. Journalists and LLMs cite numbers.
- A short survey (500+ respondents) on "AI notetaker consent and privacy" timed with lawsuit news.

**E. Product-led content**
- Public, shareable meeting-note templates (sales discovery, sprint retro, 1:1, interview) that are also SEO pages.
- Customer stories with numbers ("CRM fields updated per rep per week").

**Cadence (lean team):** 2 landing/comparison pages + 1 guide per week for 12 weeks, then 2 per week. Refresh every comparison page quarterly with a visible "Updated" date.

### 7.3 Backlinks and listings (start week 1)

Target: 150+ referring domains in 6 months, prioritizing sources AI engines read.

**Tier 1: marketplaces (links + distribution + trust)**
- Zoom App Marketplace (Fathom's original growth channel), Google Workspace Marketplace, Microsoft AppSource/Teams store
- Atlassian Marketplace (Jira) and HubSpot App Marketplace, Salesforce AppExchange (when ready)
- Calendly and Cal.com app directories
- MCP directories: mcpservers.org, Glama, Smithery, PulseMCP, and the Claude/ChatGPT connector directories if eligible. Granola and Fireflies are in every "MCP for meetings" roundup; Lynkk should be too.

**Tier 2: review and software directories**
- G2, Capterra, GetApp, Software Advice, TrustRadius, SaaSworthy, AlternativeTo, Product Hunt, Peerlist, There's An AI For That, Futurepedia, Toolify, AI Agent Store, Crunchbase, Wellfound
- Use the copy already in `memory/lynkk-brand.md`. Add Lynkk as an alternative to Otter/Fireflies/Granola/Fathom on AlternativeTo.

**Tier 3: listicle inclusion outreach (the pages that win "best ai note taker")**
- Zapier, PCMag, Wired, TechRepublic, Towards AI/Medium authors, rock.so, zackproser.com, meetingnotes.com, fast.io, aiagentrank.io,
  till-freitag.com, guideflow, jotform, rework, dupple, wisprflow, scribbl, Fellow's "26 best" guide (yes, competitors update theirs too).
- Pitch angle: "the only one that does in-person + offline + region choice," with a free extended trial for reviewers.

**Tier 4: earned media**
- Founder podcast guesting (SaaS, sales, product management, AI shows), Qwoted / Featured / Help a B2B Writer expert quotes,
  guest posts on product-management and sales-ops blogs, launch coverage (Product Hunt, Hacker News "Show HN" for the offline/MCP angle).

**Avoid:** bought link packages, PBNs, link exchanges with unrelated sites. They do nothing for AEO and risk penalties.

### 7.4 Reddit and discussion platforms (start week 1, slow and honest)

Reddit is the #1 cited source in AI answers, and a Reddit thread is #2 on Google for "best ai note taker."

**Setup**
- 1-2 real team accounts (founder + product), flair/bio says "I work on Lynkk." Always disclose. No sockpuppets, no paid fake reviews (communities detect them, and it damages AI sentiment, which reads those threads).
- Monitoring alerts for: "note taker", "notetaker", "meeting notes", "otter", "fireflies", "granola", "fathom", "read ai", "Lynkk" (F5Bot, Syften or Brand24).

**Where**
- Buyer intent: r/sales, r/salesops, r/ProductManagement, r/projectmanagement, r/jira, r/consulting, r/Entrepreneur, r/startups, r/smallbusiness, r/AI_Agents, r/productivity, r/macapps
- Trust wedge: r/gdpr, r/privacy, r/europe tech threads, r/LocalLLaMA (offline angle), r/sysadmin and r/msp (IT buyers evaluating bots)
- Our own: r/Lynkk for support and changelog (helps AI engines find first-party answers).

**How**
- 90/10 rule: 90% genuinely helpful answers (consent laws, how to run better meetings, Jira hygiene), 10% mentions where Lynkk truly fits.
- Answer old high-ranking threads ("best AI note taker for in-person meetings", "Otter alternatives") with honest comparisons that name tradeoffs.
- Host an AMA after the Product Hunt launch (r/SaaS or r/ProductManagement rules permitting).
- Encourage happy users (not employees) to share experiences; never script their posts.

**Other discussion platforms:** Hacker News (Show HN for offline-first + MCP), Indie Hackers (build-in-public), Quora (still cited by some engines), Stack Exchange / Atlassian Community (Jira automation answers), Product Hunt discussions, LinkedIn groups for RevOps and PMs.

### 7.5 Social media (start week 2)

| Channel | What competitors do | Lynkk plan |
|---|---|---|
| LinkedIn (primary, B2B + heavily cited by Perplexity/AI Mode) | Granola: founder stories, behind the scenes. Fireflies: creators + ambassadors. | Founder posts 3x/week (build story, meeting-culture opinions, data from the report). Company page 3x/week. Employee advocacy. |
| YouTube (cited by Google AI Mode/Gemini) | Fireflies creator partnerships; competitor "honest review" videos | Short demos per wedge: "Meeting to Jira in 30 seconds", "Ask Lynkk mid-meeting", "In-person + offline". Tutorials per integration. Pay 5-10 productivity/sales creators for honest reviews. |
| Short-form video (TikTok, Reels, Shorts, LinkedIn video) | Fireflies runs creator campaigns | The "AI speaks up in the meeting" moment is inherently visual and shareable. Clip it weekly. |
| X / Twitter | Fireflies founder story went viral; Granola founder presence | Build-in-public, product drops, AI/MCP community. |
| Product Hunt | Mina #1 of the day with the same pitch | Launch with the differentiators Mina lacks (in-person, offline, regions, Jira/CRM in 30s). Copy is ready in `launch/producthunt-submission.md`. |

### 7.6 AEO / GEO program (start week 1, measure monthly)

**Goal:** when someone asks an AI engine for a meeting assistant with any of Lynkk's wedge constraints, Lynkk is named, described correctly and linked.

**1. Entity clarity (fixes the Lynk/Lynq/Lynkk confusion)**
- Same name, same one-line description, same logo on every profile: website, LinkedIn, X, YouTube, G2, Capterra, Crunchbase, Product Hunt, GitHub (MCP server), app stores.
- Create a **Wikidata** item (Lynkk, instance of software/company, official website lynkk.ai, category AI meeting assistant). Wikipedia only later when there is independent press coverage.
- `Organization` schema `sameAs` links to all of the above.

**2. Answerable pages**
- Each key page opens with a 2-3 sentence direct answer, then a table of facts (price, platforms, regions, integrations, languages).
- FAQ blocks with the literal questions people ask ("Is Lynkk free?", "Does Lynkk join as a bot?", "Where is my data processed?", "Does Lynkk work offline?", "Does Lynkk work for in-person meetings?").
- Keep facts consistent across pages (AI engines penalize contradictions by ignoring the source).

**3. Get into the sources AI engines read**
- Editorial "best of" lists (7.3 tier 3), Reddit (7.4), G2 reviews (aim for 50 in 90 days via in-app prompts after a positive moment), YouTube reviews, LinkedIn posts, Medium/Towards AI posts by real users.

**4. Prompt tracking (monthly)**
Track across ChatGPT (search on), Perplexity, Google AI Overviews / AI Mode, Gemini, Claude and Copilot.
Record: mentioned (y/n), position, how Lynkk is described, which URLs are cited.

Starter prompt set (30):
1. What is the best AI note taker?
2. Best AI meeting assistant for sales teams
3. Best AI meeting assistant for product managers
4. AI meeting assistant that creates Jira tickets automatically
5. AI tool that updates HubSpot after sales calls
6. AI note taker for in-person meetings
7. AI note taker that works offline
8. AI note taker that keeps data in the EU
9. GDPR compliant AI meeting assistant
10. AI meeting assistant with data residency in India
11. AI note taker for regulated industries (finance, healthcare, legal)
12. AI assistant that can answer questions during a meeting
13. AI that speaks in Zoom meetings
14. Best Otter.ai alternative
15. Best Fireflies alternative
16. Best Granola alternative
17. Best Fathom alternative
18. Otter vs Fireflies vs Lynkk
19. AI note taker without a bot joining the call
20. Multilingual AI meeting notes
21. AI meeting notes for Mac
22. AI meeting assistant with MCP support
23. How to prepare for a meeting using past meeting notes
24. Tool to search all my past meetings
25. Best AI meeting assistant for consultants
26. Best AI note taker for interviews
27. Is it legal to record meetings with an AI note taker?
28. What is Lynkk?
29. Is Lynkk free?
30. Lynkk reviews

Tooling: the Ubersuggest account connected here has an **AI Search Visibility** feature (brand prompts and visibility overview) that can track these prompts; Parse, Peec, Profound or Otterly are alternatives.

### 7.7 Product-led loops (with product team)

The fastest-growing competitors grew through the product, not the blog.
- **Shareable notes page** for every meeting (Read AI's growth engine). Guests see a clean summary with a light "Made with Lynkk" link (each one is a backlink and brand impression).
- **Transparent join message** that doubles as education ("Lynkk is taking notes for Alex. Learn more / opt out") (consent-first + awareness).
- **Generous free tier for individuals**, monetize teams (Fathom model). If limits are tight, say so clearly; "free tier runs out fast" is Granola's top Reddit complaint.
- **Referral credits** and a **reviewer program** (G2 review prompts after a "wow" moment such as first Jira ticket created).
- **Ship and list the MCP server** publicly (GitHub + directories). It is table stakes now and an easy source of developer-community links.

---

## 8. 90-day roadmap

| Weeks | Focus | Deliverables |
|---|---|---|
| 1-2 | Foundations + identity | GSC + Bing set up; SSR/robots/llms.txt/schema check; pricing, facts and security pages; unified profiles (LinkedIn, X, YouTube, G2, Capterra, Crunchbase, PH, Wikidata); Reddit accounts + monitoring; baseline AI prompt audit (30 prompts) |
| 3-4 | Comparisons + directories | 4 alternatives pages (Otter, Granola, Fireflies, Fathom) + 2 vs pages; 25 directory listings; Zoom/Google/Microsoft marketplace submissions; first 3 demo videos |
| 5-6 | Wedge pages + launch prep | Data residency page set, in-person/offline page, Jira and HubSpot integration pages, consent-law checker tool v1; G2 review campaign starts (target 20) |
| 7-8 | Launch | Product Hunt launch (with Mina-proof differentiators), Show HN, Reddit AMA, LinkedIn founder series, 5 creator reviews live |
| 9-10 | Digital PR | "AI notetaker consent and privacy" survey report; listicle outreach to 40 publishers/authors; 3 podcast appearances booked |
| 11-12 | Measure + double down | Re-run 30-prompt audit; refresh comparisons; expand to use-case pages (sales, PM, consulting, recruiting); plan Q2 "State of Meetings" report |

---

## 9. KPIs and targets

| KPI | Baseline | Day 90 | Month 6 | Month 12 |
|---|---|---|---|---|
| Referring domains | 3 | 60 | 150 | 400 |
| Domain authority (Ubersuggest) | 1 | 10-15 | 20 | 30+ |
| Ranking keywords (US) | 1 | 100 | 300 | 1,000+ |
| Organic visits / mo | ~0 | 500 | 3,000-5,000 | 15,000+ |
| Branded searches ("lynkk") | n/a | measurable | 500/mo | 2,000+/mo |
| G2 reviews | 0 | 20 | 50 | 150 |
| Listicle inclusions (third-party "best of") | 0 | 5 | 15 | 30 |
| AI prompt mention rate (30 prompts) | 0% | 10% | 25% | 40% (wedge prompts 70%+) |
| Reddit: helpful answers posted / threads where Lynkk is recommended by non-employees | 0 / 0 | 60 / 3 | 150 / 15 | 300 / 50 |
| Signups from organic + AI referrals | n/a | track | 20% of signups | 35% of signups |

Track AI referral traffic separately in analytics (referrers such as chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai).

---

## 10. Keyword targets (US, Ubersuggest)

| Keyword | Volume/mo | SEO difficulty | CPC | Who ranks now | Lynkk approach |
|---|---|---|---|---|---|
| ai note taker | 27,100 | 48 | $13.60 | Read AI #4, publishers | Long-term; win via listicle inclusion first |
| ai powered meeting assistant | 40,500 | 50 | $2.49 | Read AI #2, Otter #6 | Homepage + features long-term |
| note taker | 14,800 | 61 | $9.09 | Otter #10 | Not a priority |
| audio to text | 12,100 | 39 | $4.49 | Otter tool pages | Optional free tool later |
| ai meeting assistant | 4,400 | 60 | $18.91 | Read AI #3, Otter #6 | Homepage title + listicles |
| meeting assistant | 4,400 | 59 | $11.53 | Read AI #2, Otter #3 | Homepage title |
| ai notetaker | 2,900 | 42 | $16.80 | Read AI #2 | Homepage + listicles |
| meeting recorder | 1,900 | 32 | $15.25 | tl;dv #1 | Feature page |
| ai meeting notes | 1,000 | 41 | $15.18 | Read AI #3 | Feature page |
| meeting notes ai | 590 | 39 | $18.98 | Read AI #1 | Feature page |
| ai note taker for in person meetings | 480-720 | 40 | $14.62 | open | **Wedge page, priority** |
| otter ai alternative | 480 | 34 | $5.76 | competitor blogs | **Alternatives page, priority** |
| granola alternative | 320 | 28 | $20.94 | competitor blogs | **Alternatives page, priority** |
| live ai meeting assistant | 170 | 51 | $19.42 | Otter #2 | **Wedge page, priority** |
| ai meeting summarizer | 170 | 34 | $17.63 | Read AI #1 | Feature page |
| ai meeting minutes generator | 140 | 30 | $11.07 | open | Free tool / template page |
| fathom vs fireflies | 110 | 32 | $43.71 | Fathom /vs page #2 | Multi-way comparison post |
| fireflies alternatives | 110 | 14 | $40.21 | Read AI #2 | **Alternatives page, priority** |
| is it illegal to record someone without their permission (and variants) | 1,600+ | 32-44 | low | Otter blog | Consent-law checker tool |

Wedge queries such as "meeting notes to Jira" or "AI note taker without bot" show near-zero Google volume but appear constantly as
AI prompts and Reddit questions. Build them for AEO and conversion, not for Google traffic.

---

## 11. What not to do

- **Don't chase off-topic traffic.** Fireflies, Otter, Read AI and tl;dv lost 55-90% of their non-brand footprint doing this.
- **Don't astroturf Reddit or fake reviews.** It is detectable, against platform rules, and the sentiment it creates is what AI engines read.
- **Don't publish self-serving listicles that rank Lynkk #1 at everything.** Honest tradeoffs get cited; puffery gets skipped.
- **Don't lead with "AI that speaks in your meeting" alone.** Otter, Fireflies and Mina already claim it. Lead with the combination.
- **Don't make unverifiable claims** (certifications, regions, language counts) before they are confirmed. See "To confirm" in `memory/lynkk-brand.md`. Inconsistent facts reduce AI trust.
- **Don't let the bot auto-join without clear disclosure.** That is the exact behavior behind the Otter and Fireflies lawsuits.

---

## 12. Open questions for the team

1. Which data regions are live today, and which models run in each? (Needed for the residency wedge.)
2. Is there a mobile app for in-person capture, or Mac only? How does offline mode work exactly?
3. Is the MCP server public, and can it be listed in directories?
4. Free tier limits and paid pricing (needed for the pricing page and AI answers to "is Lynkk free").
5. Any security certifications in progress (SOC 2, ISO 27001)?
6. Can we use aggregated, anonymized usage data for a public report (consent and privacy review)?
7. Budget for creators (5-10 videos) and for Product Hunt / launch promotion?

---

## Data notes

- Ubersuggest figures are US estimates from its Sep 2026 snapshot (some keyword data from Jul to Sep 2026). Monthly history is from the same tool.
  Absolute numbers differ between tools (Semrush, Ahrefs, Similarweb); trends and relative sizes are the useful part.
- Read AI's organic estimate is inflated by ranking #2 for the generic word "read" (301K searches/mo).
- fathom.ai figures exclude the legacy fathom.video domain.
- G2 review counts come from third-party 2026 roundups and vary by source; verify on G2 before quoting.
- Similarweb snippets seen in search: Otter ~6M monthly visits with ~72% direct; Fathom ~99% organic share; Fireflies ~31% organic. Months vary by snippet.
- lynkk.ai and several research pages (AnswerPeek, Parse, YipitData) could not be fetched directly from this environment due to network policy; their figures come from search-result summaries.

## Sources

- Ubersuggest domain, backlink, keyword and SERP data (accessed 2026-10-06)
- [AnswerPeek: Which AI note-takers do ChatGPT and Perplexity recommend?](https://www.answerpeek.com/ranking/ai-note-takers)
- [Parse: Best AI meeting assistant & transcription tools, according to AI](https://parse.gl/rankings/productivity-tools/ai-meeting-assistant-transcription-tools)
- [Search Engine Land: AI search engines cite Reddit, YouTube, and LinkedIn most](https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138)
- [5W AI Platform Citation Source Index 2026](https://www.prnewswire.com/news-releases/5w-releases-ai-platform-citation-source-index-2026-the-50-websites-that-now-decide-what-brands-are-visible-inside-chatgpt-claude-perplexity-gemini-and-google-ai-overviews-302759804.html)
- [Contently: Top 10 sources LLMs cite most in 2026](https://contently.com/2026/04/29/top-sources-llms-cite/)
- [YipitData: Is Granola the new leader in AI notetaking?](https://www.yipitdata.com/resources/blog/granola-vs-fathom-otter-fireflies-ai-notetaking)
- [BusinessWire: Otter.ai breaks $100M ARR, launches AI Meeting Agent suite](https://www.businesswire.com/news/home/20250325249430/en/Otter.ai-Breaks-$100M-ARR-Barrier-and-Transforms-Business-Meetings-Launching-Industry-First-AI-Meeting-Agent-Suite)
- [UC Today: Otter's AI agent speaks up during calls](https://www.uctoday.com/unified-communications/otter-revolutionises-meetings-with-ai-agent-that-speaks-up-during-calls/)
- [Fireflies: $1B valuation and Perplexity partnership](https://fireflies.ai/blog/fireflies-1-billion-valuation/)
- [Fireflies: Introducing Talk to Fireflies](https://fireflies.ai/blog/talk-to-fireflies-perplexity/)
- [Fireflies influencer and social media manager role](https://jobs.khoslaventures.com/companies/fireflies-ai/jobs/58862449-influencer-social-media-manager)
- [UC Today: Otter.ai lawsuit over meeting bot recording](https://www.uctoday.com/security-compliance-risk/otter-ai-lawsuit-meeting-bot-recording-after-call/)
- [tl;dv: TL;DR of the Otter.ai lawsuit](https://tldv.io/blog/ai-meeting-recorder-lawsuits/)
- [AI notetaker lawsuits 2026](https://tooldirectory.ai/blog/ai-notetaker-lawsuits-2026)
- [Superframeworks: How Fathom out-grew VC-backed rivals](https://superframeworks.com/case-study/fathom)
- [Latka: Fathom founder interview](https://getlatka.com/interviews/fathomai-richard-white-2026)
- [Ragged Edge: Granola partnership / rebrand](https://raggededge.com/partnerships/granola)
- [Granola launches new brand and OOH campaign](https://www.createwith.com/tool/granola/updates/granola-launches-new-brand-and-ooh-campaign)
- [Granola: Content Lead job](https://granola.ai/jobs/content-lead)
- [Granola: Data residency and deployment models](https://www.granola.ai/blog/ai-notetaker-data-residency-deployment-models)
- [Granola MCP updates](https://www.createwith.com/tool/granola/updates/granola-mcp-seamlessly-connect-meeting-notes-to-ai-apps)
- [Fireflies MCP server](https://guide.fireflies.ai/articles/3039542843-learn-about-fireflies-mcp-server-connect-your-ai-tool)
- [GeekWire: Read AI raises $50M](https://www.geekwire.com/2024/seattle-startup-read-ai-raises-50m/)
- [TechCrunch: Read AI launches email-based digital twin](https://techcrunch.com/2026/02/26/read-ai-launches-an-email-based-digital-twin-to-help-you-with-schedules-and-answers/)
- [Jamie: European AI meeting assistants](https://www.meetjamie.ai/blog/european-ai-meeting-assistants)
- [Jamie: GDPR note takers in Europe](https://www.meetjamie.ai/en/blog/gdpr-note-takers-in-europe)
- [Mina Meeting Assistant on Product Hunt](https://www.producthunt.com/p/mina-meeting-assistant)
- [Granola AI Reddit review 2026](https://www.aitooldiscovery.com/guides/granola-ai-reddit)
- [Rowan Cheung on the "Fred from Fireflies" origin story](https://x.com/rowancheung/status/1988218743952916537)
- [Fathom AI review and G2 standing](https://www.outdoo.ai/blog/fathom-ai-review-alternatives)
- [Fast.io: Best AI meeting assistants 2026 (G2 counts)](https://fast.io/resources/best-ai-meeting-assistants-2026/)
- [Laxis: State of meeting note taking 2026](https://laxis.com/blog/state-of-meeting-note-taking-2026)
- [Exploding Topics: AI notetaker](https://explodingtopics.com/topic/ai-notetaker)
- [Similarweb: fathom.video](https://www.similarweb.com/website/fathom.video/), [fireflies.ai](https://www.similarweb.com/website/fireflies.ai/), [otter.ai](https://www.similarweb.com/website/otter.ai/)
