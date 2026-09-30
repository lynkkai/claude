# Lynkk Product Pages: SEO Issues Quick Report

**Date:** 2026-09-30 · **Keyword data:** Ubersuggest, US (locId 2840) unless marked IN = India (locId 2356)
**Rules:** [`memory/seo-keyword-guardrails.md`](../memory/seo-keyword-guardrails.md) · **Raw data:** [`data/ubersuggest-2026-09-30.md`](data/ubersuggest-2026-09-30.md) (section 9)
Tags: **[DATA]** tool output · **[JUDGMENT]** recommendation · **[UNVERIFIED]** could not check

**Scope and limits.** 15 product pages found by Ubersuggest's site crawl (38 pages total). Lynkk's page titles and
technical flags come from that crawl [DATA]. **Body copy, H1s and meta descriptions could not be read**, because
lynkk.ai is blocked from this environment. So "missing keyword" below means *missing from the page title*,
the strongest on-page signal we can verify. Competitor positioning is taken from their search result titles
[DATA], not from their page copy.

---

## 1. Site-wide issues

| # | Issue | Evidence | Why fix it |
|---|---|---|---|
| S1 | **No product page ranks for anything.** | lynkk.ai has 1 ranking keyword in total (position 39, /features/meeting-bot); DA 1; 1 backlink. [DATA] | Everything below is about giving Google clear signals. Without links, even perfect pages will rank slowly. [JUDGMENT] |
| S2 | **Titles lead with slogans, not search terms.** | Title phrases such as "Ask Your Meetings", "Speak Instead of Type", "Pro for Everyone" and "Search, Decisions and Ask Your Notes" match no keyword with measured volume in this audit (knowledge-graph concept terms all returned 0). [DATA: titles + volumes below] | The title is the #1 on-page ranking signal and the blue link people click. Competitors put the category term first (section 3). [JUDGMENT] |
| S3 | **The biggest category term is missing everywhere.** | "ai note taker" 27,100/mo (SD 48) and "ai notetaker" 2,900/mo (SD 42) appear in **zero** Lynkk titles. [DATA] | Every top competitor uses "AI Notetaker/Note Taker" in its title (section 3). Lynkk is invisible for the term buyers actually type. [JUDGMENT] |
| S4 | **"AI meeting notes" is spread across many pages.** | Home, /features/meeting-notes, all 4 /compare pages and /use-cases have "AI Meeting Notes" in their titles. [DATA] | Several pages targeting one phrase split relevance (cannibalization). Pick one owner (meeting-notes) and give others their own term. [JUDGMENT] |
| S5 | **Brand repeated twice in 6 titles.** | /features, /slack, /web-app, /download, /integrations, /how-it-works have "Lynkk" at the start and "\| Lynkk" at the end. /slack is 63 and /download 62 characters. [DATA] | Wastes the characters that should hold keywords; titles over ~60 characters risk being cut off in Google. [JUDGMENT] (Ubersuggest did not flag them as too long.) |
| S6 | **Thin feature hub.** | /features has 94 words and is flagged "low word count". [DATA] | The hub should pass relevance to every feature page. At 94 words it gives Google almost nothing. [JUDGMENT] |
| S7 | **URL flags.** | /features/knowledge-graph and /features/chrome-extension flagged "non-SEO-friendly URL" (no reason given). [DATA] | Low priority. Only change a URL if the page's target keyword changes; add 301 redirects. [JUDGMENT] |

---

## 2. Page-by-page

Vol = US monthly searches, SD = SEO difficulty (0-100).

### Meeting & notes pages

| Page · current title | Missing keyword (Vol / SD) | Issue & why fix | Suggested title [JUDGMENT] |
|---|---|---|---|
| **/** (home) · "Lynkk: AI Meeting Notes & Conversation Intelligence" | ai notetaker (2,900 / 42); ai note taker (27,100 / 48) | "Conversation intelligence" has volume (1,900 / 60) but is the hardest term here. Read.ai's homepage is #2 for "ai notetaker" with ~971 est. clicks. [DATA] The homepage should hold the head term. | Lynkk: AI Note Taker & Meeting Assistant, Before, During, After |
| **/features/meeting-notes** · "AI Meeting Notes: Transcript, Summary and Tasks" | ai meeting summary (170 / 37), ai meeting summarizer (170 / 34), ai note taker app (880 / 32) | Holds "ai meeting notes" (1,000 / 41), which is correct. "Summary" is in the title but not the searched phrasing "AI meeting summary". [DATA] | AI Meeting Notes & Summaries: Transcripts and Tasks \| Lynkk |
| **/features/meeting-bot** · "Meeting Bot for Zoom, Meet & Teams" | ai note taker for zoom (480 / 33), teams ai note taker (590 / 28), google meet ai note taker (590 / 40) | **Search intent mismatch.** "meeting bot" (70/mo) returns developer APIs: GitHub, recall.ai, attendee.dev, meetingbaas. [DATA] Buyers searching for a note taker won't find this page, and developers who find it won't convert. | AI Note Taker for Zoom, Google Meet & Teams \| Lynkk |
| **/features/action-items** · "AI Action Item Tracker for Meetings" | none (good match) | Targets "action item tracker" (320 / 31). ✔ But that SERP is templates and how-tos (Vertex42, Smartsheet, Asana); Read AI ranks #3 with an *article*, not a product page. [DATA] A product page will struggle here. | Keep title. Add a template/how-to section, or a companion blog post, to match intent. |
| **/features/knowledge-graph** · "Ask Your Meetings: One Answer Across Every Call" | no concept term has volume (all tested = 0) | Nothing people search for. Competitors name the feature plainly: "Otter AI Chat for meetings", Read's "Ask Read / Search Copilot". [DATA/WEB] | Treat as a conversion page; link to it from meeting-notes. If retargeting, "AI meeting assistant" (4,400 / 60, hard). |
| **/features/workspaces** · "Workspaces: Team Meeting Notes with Pro for Everyone" | team ai meeting notes (720 / 25), team ai note taker (720 / 27) | Uses the non-AI phrase "team meeting notes" (390 / 43), whose suggestions are template searches. "Pro for Everyone" is a pricing slogan with no search value. [DATA] | Team AI Meeting Notes: Shared Workspaces \| Lynkk |
| **/web-app** · "Lynkk Web App: Search, Decisions and Ask Your Notes" | ai meeting notes app (140 / 46) | Brand + slogan title; no category term. [DATA] Low search value; mostly a navigation page. | Lynkk Web App: AI Meeting Notes App in Your Browser |

### Capture & platform pages

| Page · current title | Missing keyword (Vol / SD) | Issue & why fix | Suggested title [JUDGMENT] |
|---|---|---|---|
| **/features/chrome-extension** · "Record Meet, Zoom and Teams Without a Bot" | bot free ai note taker (110 / 59), record google meet chrome extension (140 / 36), google meet ai note taker (590 / 40) | No "Chrome extension", no "note taker". Competitors' titles say "AI notetaker with no bot" (Scribbl) and "AI Note Taker for Google Meet, Zoom & Teams" (Tactiq). [DATA] | Bot-Free AI Note Taker Chrome Extension for Meet, Zoom, Teams |
| **/features/dictation** · "AI Dictation for Mac: Speak Instead of Type" | speech to text mac (1,600 / 25), speech to text mac app (320 / 28) | Has "ai dictation" (480 / 31), which is good. Misses the biggest, easiest Mac term. [DATA] "Speak Instead of Type" uses up characters with no search value. | AI Dictation & Speech to Text for Mac \| Lynkk |
| **/download** · "Download Lynkk for Mac: Record Calls, Dictate Anywhere" | ai note taker for mac (30 / 46) | Low search demand ("meeting recorder mac" = 0). [DATA] Brand twice, 62 characters. Fine as a navigation page. | Download Lynkk: AI Note Taker & Dictation for Mac |
| **/features/hinglish-transcription** · "Multilingual Meeting Transcription" | IN: hindi transcription (1,900 / 15), hinglish transcription (110 / 28) | **URL says Hinglish, title says Multilingual, and neither Hindi nor Hinglish is in the title.** US demand is near zero ("multilingual transcription" 30), but India has real demand with low difficulty. [DATA] The India SERP for "hinglish transcription" has **no product pages** (freelancer posts, a subtitle blog, and a tweet asking "why can't someone make a hinglish note taker?"). [DATA] This is the easiest opening in the audit. | Hinglish & Hindi Meeting Transcription, AI Notes \| Lynkk |

### Integration pages

| Page · current title | Missing keyword (Vol / SD) | Issue & why fix | Suggested title [JUDGMENT] |
|---|---|---|---|
| **/slack** · "Lynkk for Slack: Ask About Your Meetings in Any Channel" | slack ai notes (170 / 34) | 63 characters, brand twice. Competitor integration titles lead with the keyword: "Slack + Fellow.ai \| AI Meeting Assistant and Notetaker", Read's "Slack Summaries and Meeting Reports". [DATA] | Slack AI Meeting Notes: Ask About Any Call \| Lynkk |
| **/integrations** · "Lynkk Integrations: Jira, Google Calendar & MCP" | jira meeting notes (10 / 19) | Low demand; brand twice. [DATA] Fine as is. Individual integration pages (for example /integrations/jira) would follow the Fellow pattern. | Integrations: Jira, Google Calendar, Slack & MCP \| Lynkk |
| **/how-it-works** · "How Lynkk Works: From Meeting to Notes and Tasks" | not checked | Brand twice. Explainer page, low priority. | Shorten; drop the second "Lynkk". |

---

## 3. How competitors position their product pages

Search result titles, US [DATA]. Dashes normalized per repo rule.

| Competitor | Title | Positioning angle |
|---|---|---|
| Otter | "Otter Meeting Agent - AI Notetaker, Transcription, Insights" | New category ("Meeting Agent") + head keyword |
| Read AI | "Meeting Summaries, Transcripts, AI Notetaker & Enterprise ..." | Stacks 3 searched terms |
| Fireflies | "#1 AI Teammate for Meetings, Email, Chat & CRM" | Leadership claim + breadth beyond meetings |
| Krisp | "The World's #1 AI Meeting Assistant" | Leadership claim + category |
| Notion | "AI Meeting Notes - Perfect Meeting Memory." | Keyword + memory benefit |
| Fellow | "Secure AI Meeting Assistant for Enterprise and Regulated ..." | Security / regulated buyers |
| Notta | "AI Note Taker \| Free AI Meeting Transcription" | Keyword + "Free" |
| Zoom | "AI note taker: Your AI Meeting Assistant" | Two category terms back to back |
| Scribbl | "An AI notetaker with no bot in the call" | Keyword + bot-free differentiator |
| Tactiq | "AI Note Taker for Google Meet, Zoom & Teams" | Keyword + platform names |
| tl;dv | "Free Google Meet AI Note Taker - With or Without a Bot" | Free + platform + bot choice |
| Wispr Flow | "Voice to Text Dictation & AI Notetaker" | Dictation + note taker in one product |
| Superwhisper | "AI Voice to Text for macOS, Windows, iOS ..." | Keyword + platforms |
| Voicy | "The best Dictation App for Mac" | Keyword + platform + "best" |
| AI Dictation | "Mixed-Language Voice Typing & Dictation App" | Multilingual angle |
| Otter (Ask) | "Otter AI Chat for meetings" | Plain feature name |
| Read AI (Ask) | "Ask Read: It's Enterprise Search for Everyone" | Enterprise search framing |
| Fellow (teams) | "AI Note Taker for Fast Moving Teams" | Keyword + audience |

**The pattern** [JUDGMENT, based on the table]:
1. **Category keyword first** ("AI Note Taker", "AI Meeting Assistant", "Dictation App"). Almost every competitor does this; most Lynkk titles don't.
2. **Then one differentiator**: free, #1, secure/enterprise, bot-free, or platform names.
3. **Plain feature names** ("AI Chat", "Search Copilot") instead of metaphors.

**Where Lynkk can stand out** (differentiators from `memory/lynkk-brand.md` that no competitor title above uses):
"before, during and after" the meeting, "speaks in your meeting", in-person + online, offline-first, data
residency, and Hinglish/Hindi. Put these *after* the category keyword, not instead of it. [JUDGMENT]

---

## 4. Fix order

| Priority | Page(s) | Fix | Why first |
|---|---|---|---|
| 1 | /features/hinglish-transcription | Add Hindi/Hinglish to title, H1 and copy; target India | Real demand (IN 1,900 / SD 15), no product competitors in SERP [DATA] |
| 2 | / (home) | Add "AI note taker" / "AI notetaker" | Biggest term (27,100 + 2,900) missing site-wide [DATA] |
| 3 | /features/meeting-bot | Retarget from "meeting bot" to "AI note taker for Zoom / Teams / Meet" | Current keyword has developer intent [DATA] |
| 4 | /features/dictation | Add "speech to text Mac" | 1,600 / SD 25, easiest volume [DATA] |
| 5 | /features/chrome-extension, /features/workspaces | Add "bot-free AI note taker" / "team AI meeting notes" | Demand-backed terms missing from titles [DATA] |
| 6 | /features hub | Expand beyond 94 words, link to every feature with keyword anchor text | Flagged thin [DATA] |
| 7 | 6 double-brand titles, /slack | Drop the second "Lynkk", lead with the keyword | Quick title cleanup |
| 8 | knowledge-graph, web-app, integrations, how-it-works | Leave for search; use as conversion pages | No measured demand [DATA] |

**Before shipping copy:** confirm H1s and body copy match the new titles (not visible from here) [UNVERIFIED],
and confirm product claims (Hindi support level, platforms, bot-free on Zoom/Teams) against `memory/lynkk-brand.md`.
