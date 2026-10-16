# Lynkk Use Cases: Keyword & AI-Prompt Research

> Data: Ubersuggest (keyword overview, suggestions, SERP, AI Search Visibility), pulled 2026-10-16.
> Volumes are average monthly Google searches. US = loc 2840, India = loc 2356, Global = no location.
> Intent comes from Ubersuggest: Info = informational, Comm = commercial, Trans = transactional, Nav = navigational.
> SD = SEO difficulty (0-100). CPC in USD.

> **Correction (2026-10-16):** the live lynkk.ai site says Lynkk does **not** sync to a CRM and does not list
> Calendly/Cal.com, SOC 2 or HIPAA. Ignore those claims below. The lynkk.ai-specific plan, with verified product
> facts and the existing /use-cases pages, is in `research/lynkk-use-case-audit-and-plan.md`.


## 1. Key finding: where the volume actually is

People rarely search "AI note taker for [role]". Those modifier phrases are tiny:

| Modifier keyword (US) | Volume |
|---|---|
| ai note taker for in person meetings | 480 |
| ai note taker for teams / zoom / google meet | 590 / 480 / 210 |
| ai note taker for therapists | 90 |
| ai note taker for students | 70 |
| ai note taker for financial advisors | 30 |
| ai note taker for interviews | 10 |
| ai note taker for sales calls / marketing / recruiters / consultants / lawyers | 0 |

The demand sits in **role-level "AI for X" terms** and **job-to-be-done terms** (minutes of meeting,
interview transcription, conversation intelligence). So each use-case page should target a keyword
*cluster* (the role term + the task term + the "ai note taker for X" long tail), not just the long tail.

Category head terms that every use-case page can link back to:

| Keyword | US | India | Global | Intent | CPC (US) | SD (US) |
|---|---|---|---|---|---|---|
| ai note taker | 27,100 | 1,900 | 49,500 | Trans | $13.60 | 48 |
| ai meeting assistant | 4,400 | 1,300 | - | Comm | $18.91 | 60 |
| ai meeting minutes | 1,600 | 210 | - | Info | $10.62 | 49 |
| meeting notes ai | 590 | - | - | Info | $18.98 | 39 |
| meeting transcription | 480 | - | - | Info | $15.99 | 62 |

## 2. Top 10 use cases, ranked

Score = cluster volume x commercial intent x how well Lynkk's real features fit (see `memory/lynkk-brand.md`).

| # | Use case | Cluster volume US | Cluster volume India | Main intent | CPC signal | Lynkk fit |
|---|---|---|---|---|---|---|
| 1 | **Sales teams** (calls, next steps, deal prep) | ~8,600 | ~1,500 | Commercial | Very high ($26-$108) | Excellent |
| 2 | **HR & recruiting interviews** | ~12,200 | ~4,300 | Commercial / Info | High ($40-$94) | Strong |
| 3 | **Meeting minutes (MoM) for ops, admin & boards** | ~5,200 | **~42,100** | Informational | Medium | Excellent |
| 4 | **Project managers, product & engineering** (Jira) | ~2,900 | ~1,300 | Commercial | Medium ($20) | Excellent |
| 5 | **In-person meetings & conversations** | ~670 | low | Transactional | Medium ($15) | Unique differentiator |
| 6 | **Marketing teams** (customer interviews, VoC, content) | ~3,900 | ~2,900 | Commercial | Medium ($22-$29) | Good |
| 7 | **Lawyers & legal teams** (client consultations) | ~2,400 | ~720 | Commercial | High ($43) | Good (data residency) |
| 8 | **Managers & 1:1 meetings** | ~2,400 | - | Informational | Low | Excellent (pre-meeting context) |
| 9 | **Real estate agents** | ~590 | - | Commercial | Medium ($21) | Fair (in-person; no CRM sync) |
| 10 | **Financial advisors & wealth managers** | ~420 | - | Commercial | High ($28-$30) | Fair (data region; no CRM sync) |

Honourable mentions (fold into other pages or build later): customer success (110/mo but $93 CPC,
merge into Sales), consultants & agencies (140/mo, $23 CPC), Mac dictation (dictation software 1,900/mo US,
supports the Mac app). Gated: healthcare (see section 4).

---

## 3. Use case details

### 1. Sales teams

| Keyword | US | India | Global | Intent | CPC | SD |
|---|---|---|---|---|---|---|
| ai for sales | 2,900 | 590 | 5,400 | Comm | $25.81 | 58 |
| ai crm | 2,400 | 880 | - | Info | $60.35 | 43 |
| conversation intelligence | 1,900 | - | - | Comm | $18.00 | 60 |
| ai sales assistant | 590 | - | - | Comm | $64.51 | 39 |
| conversation intelligence software | 390 | - | - | Comm | $38.71 | 40 |
| gong alternatives | 210 | - | - | Info | $80.17 | 31 |
| sales call recording software | 110 | - | - | Comm | $108.65 | 31 |
| best conversation intelligence software | 90 | - | - | Comm | $56.51 | 40 |

- **Why #1:** the highest CPCs in the whole study, which means buyers here pay. "gong alternatives"
  and "sales call recording software" have low SD (31) and are easy wins.
- **Lynkk features to lead with:** context from past calls before every call, live voice answers during
  the call, next steps with owners, decisions and a follow-up email after (no CRM sync).
- **Page angle:** "AI note taker for sales: walk into every call ahead, leave with the next steps already written down."
- **Supporting pages:** Gong alternative, conversation intelligence for SMBs.
- **AI prompts to track (Ubersuggest):**
  - What is the best AI note taker for sales teams with CRM integration?
  - AI note taker for sales teams vs traditional manual note-taking tools, which is better?
  - What is the best AI note taker for customer success teams with integration to CRM?
  - (already tracked, India) What is the best conversation intelligence software for sales teams in India?
  - (already tracked, India) Which conversation intelligence platform offers the best pricing for small businesses in India?

### 2. HR & recruiting interviews

| Keyword | US | India | Global | Intent | CPC | SD |
|---|---|---|---|---|---|---|
| ai recruiting | 3,600 | 1,900 | 12,100 | Nav / Info | $39.68 | 25 |
| ai for hr | 3,600 | 2,400 | - | Comm | $39.94 | 77 |
| ai recruiting platforms | 1,300 | - | - | Comm | $130.03 | 50 |
| interview transcription | 1,300 | - | - | - | $3.76 | 25 |
| ai recruiting tool | 1,000 | - | - | Comm | $54.38 | 74 |
| ai recruiting software | 880 | - | - | Comm | $93.71 | 53 |
| interview notes | 480 | - | - | Info | $15.55 | 19 |
| interview transcription software | 210 | - | - | Comm | $13.02 | 40 |

- **Caveat:** most "ai recruiting" demand is for sourcing and screening tools, so only part of this cluster
  wants interview notes. Also excluded on purpose: "ai interview assistant" (1,900/mo), which is mostly
  candidates looking for interview copilots, not recruiters.
- **Low-difficulty wins:** "interview notes" (SD 19), "interview transcription" (SD 25), "ai recruiting" (SD 25).
- **Lynkk features to lead with:** in-person and online interview capture, structured scorecard-style notes,
  searchable knowledge graph across every candidate, data residency for HR compliance, multilingual.
- **Page angle:** "Stop typing during interviews. Lynkk writes the scorecard while you listen."
- **AI prompts to track (Ubersuggest):**
  - What is the best AI note taker for recruiting interviews with real-time transcription?
  - Which AI note taker is best for HR interviews and candidate evaluation?

### 3. Meeting minutes (MoM) for operations, admin & boards

| Keyword | US | India | Intent | CPC (US) | SD (US / India) |
|---|---|---|---|---|---|
| minutes of meeting | 1,900 | **27,100** | Info | $9.34 | 31 / 26 |
| minutes of meeting format | - | **14,800** | - | $0.85 (IN) | - / 10 |
| ai meeting minutes | 1,600 | 210 | Info | $10.62 | 49 / 22 |
| board meeting minutes | 1,000 | - | Info | $17.42 | 38 |
| ai meeting summary | 170 | - | Info | $16.06 | 37 |

- **Why it matters:** the biggest single opportunity for India by far. "minutes of meeting format" has
  14,800/mo with SD 10, which is very easy to rank for.
- **Intent is informational** (people want a format or template), so the page should be a free MoM template
  plus a "generate MoM automatically with Lynkk" call to action.
- **Lynkk features to lead with:** structured notes plus assigned action items within 30 seconds, for online
  and in-person meetings, in multiple languages.
- **AI prompts to track (Ubersuggest):**
  - What is the best AI meeting minutes generator for remote teams?
  - Which AI meeting minutes generator offers the most accurate transcription?
  - (already tracked, India) Which AI meeting notetaker is best for Indian startups looking to automate meeting summaries?

### 4. Project managers, product & engineering teams

| Keyword | US | India | Intent | CPC (US) | SD (US / India) |
|---|---|---|---|---|---|
| ai for project managers | 2,900 | 1,300 | Comm | $20.10 | 44 / 27 |

- **Lynkk features to lead with:** Jira tickets created from meetings, action items assigned, "what is still
  open" context before standups, MCP to connect other tools.
- **Page angle:** "From standup to Jira ticket without anyone typing."
- **AI prompts to track (Ubersuggest):**
  - What is the best AI note taker for project managers to improve meeting productivity?
  - How does Lynkk compare to other AI note takers for project management?
  - What is the best AI note taker for user research interviews with audio transcription?
  - (already tracked, India) Which automated action item tracking tool is best for project teams in India?

### 5. In-person meetings & conversations

| Keyword | US | India | Intent | CPC | SD |
|---|---|---|---|---|---|
| ai note taker for in person meetings | 480 | 10 | Trans | $14.62 | 40 |
| best ai note taker for in person meetings | 110 | - | Comm / Trans | $9.06 | 65 |
| free ai note taker for in person meetings | 50 | - | Trans | $17.25 | 38 |
| in person meeting notes ai | 30 | - | Info | $11.02 | 74 |

- **Why it ranks this high despite lower volume:** it is the largest "ai note taker for X" long tail, the intent
  is transactional, and most bot-based competitors (Fireflies, Fathom, Gong) cannot do it. The current SERP is
  weak: Zoom, a Medium listicle, a Reddit thread, Plaud (hardware). A focused page can rank.
- **Lynkk features to lead with:** records in-person conversations, offline-first, multilingual.
- **AI prompts to track (Ubersuggest):**
  - What is the best AI note taker for in-person meetings with high accuracy?
  - AI note taker for in-person meetings vs traditional transcription services, which is better?

### 6. Marketing teams

| Keyword | US | India | Intent | CPC (US) | SD |
|---|---|---|---|---|---|
| ai for marketing | 3,600 | 2,900 | Comm | $29.06 | 69 |
| customer interviews | 210 | - | Info | $22.85 | 44 |
| focus group transcription | 110 | - | Info | $22.20 | 16 |

- **Caveat:** "best ai note taker for marketing" has 0 searches and "ai for marketing" is a broad, hard
  (SD 69) term about AI marketing tools in general. Position marketing around *customer research*: customer
  interviews, focus groups, agency client calls, and turning calls into content and messaging.
- **Lynkk features to lead with:** searchable knowledge graph of every customer conversation, ask questions
  across past calls ("what objections did customers raise this month?").
- **AI prompts to track (Ubersuggest):**
  - What is the best AI note taker for marketing teams with collaborative features?
  - Which AI note taker is better for marketing teams: Otter.ai or Lynkk?

### 7. Lawyers & legal teams

| Keyword | US | India | Intent | CPC | SD |
|---|---|---|---|---|---|
| ai for lawyers | 2,400 | 720 | Comm | $43.29 | 60 |
| ai legal transcription | 10 | - | - | $11.11 | 29 |

- Use case: client consultations, case meetings, internal reviews. Lead with **data residency** (pick
  your region) and in-person capture. Confirm security certifications before publishing.
- **AI prompt:** What is the best AI note taker for lawyers handling complex cases?

### 8. Managers & 1:1 meetings

| Keyword | US | Intent | CPC | SD |
|---|---|---|---|---|
| one on one meeting | 2,400 | Info | $8.68 | 38 |

- The cleanest fit for Lynkk's "before the meeting" feature: it surfaces what you discussed last time and
  what is still open. Best built as a 1:1 template or guide page with a product call to action.

### 9. Real estate agents

| Keyword | US | Intent | CPC | SD |
|---|---|---|---|---|
| ai for real estate agents | 590 | Comm | $20.82 | 34 |

- Showings and client calls happen in person and on the phone. Lead with in-person capture, follow-ups
  and follow-up emails. Buyers here expect CRM sync, which Lynkk doesn't offer.

### 10. Financial advisors & wealth managers

| Keyword | US | Intent | CPC | SD |
|---|---|---|---|---|
| ai for financial advisors | 210 | Comm | $29.90 | 43 |
| jump ai for financial advisors | 140 | Comm | $18.75 | 20 |
| best ai for financial advisors | 40 | Comm | $25.63 | 16 |
| ai note taker for financial advisors | 30 | Trans | $28.10 | 30 |

- A small but high-value niche with established vertical players (Jump, Zocks). Lead with compliance-friendly
  notes and data residency. Buyers here expect CRM sync, which Lynkk doesn't offer.
- **AI prompt:** Which AI note taker offers the most accurate transcription for financial advisors?

---

## 4. Not recommended yet (gated or low value)

| Use case | Volume (US) | Why not now |
|---|---|---|
| Healthcare / medical scribe | ai medical scribe 5,400 (6,600 global), ai scribe 2,400, ai therapy notes 590, ai for therapists 480, ai soap notes 110 | Biggest vertical by volume, but buyers require HIPAA compliance and EHR integration. Do not publish until compliance is confirmed (open item in `memory/lynkk-brand.md`). |
| Students & lectures | ai note taker for students 70, lectures 110, lecture transcription 90 | Low volume, low CPC ($3-$9), poor fit with a B2B meeting product. |
| UX "user interview" | 49,500 | Volume looks large but is dominated by unrelated intent (the UserInterviews platform, job "user interview" queries). Use product-research terms inside use case 4 instead. |

## 5. AI search visibility (Ubersuggest AISV, India, 10 prompts)

- **Lynkk visibility: 0%** (0 mentions across 10 ChatGPT answers).
- Brands winning those answers: Fireflies.ai (40% visibility), Avoma (30%), Otter.ai (30%), Fathom (20%), Gong (20%),
  plus Indian players Vaarta, Stenoji, Convin.
- The 20 new use-case prompts above give Lynkk something to track per page. The brand slot allows 10 prompts,
  so pick the highest-priority ones (sales, recruiting, MoM, in-person, project management) when updating the tracker.

## 6. Recommended build order

1. Sales use-case page + "Gong alternative" page (highest commercial value)
2. Minutes of Meeting format/template page + AI MoM generator (biggest India volume, SD 10)
3. Recruiting & HR interviews page + interview notes template (SD 19)
4. In-person meetings page (clear differentiator, weak SERP)
5. Project managers / Jira page
6. Marketing (customer research) page
7. 1:1 meetings template page
8. Legal, real estate, financial advisors (shorter vertical pages)

## Sources

- Ubersuggest keyword, SERP and AI Search Visibility data (project: lynkk.ai), 2026-10-16
- Competitor use-case mapping: [Metaview, Otter.ai alternatives](https://www.metaview.ai/resources/blog/otter-ai-alternatives),
  [Fireflies, best AI notetaker for customer success](https://fireflies.ai/blog/best-ai-notetaker-for-customer-success),
  [Velaris, top AI note-taking apps for customer success](https://www.velaris.io/articles/top-10-ai-note-taking-apps-for-customer-success)
