# Lynkk Use-Case Pages: Google-Friendly Content Structure

> Research date: 2026-10-16. Based on Google Search Central documentation (quoted below), Ubersuggest SERP
> analysis of our target keywords, Ubersuggest Google autocomplete questions, and a teardown of competitor
> use-case pages. Keyword volumes are in `research/use-case-keyword-research.md`.

> **Correction (2026-10-16):** the live lynkk.ai site says Lynkk does **not** sync to a CRM and does not list
> Calendly/Cal.com, SOC 2 or HIPAA. Ignore those claims below. The lynkk.ai-specific plan, with verified product
> facts and the existing /use-cases pages, is in `research/lynkk-use-case-audit-and-plan.md`.


---

## Part 1. What Google actually recommends (and what it means for us)

| Google says | Source | What we do on use-case pages |
|---|---|---|
| Create "helpful, reliable, people-first content". Ask: "After reading your content, will someone leave feeling they've learned enough about a topic to help achieve their goal?" | Creating helpful content | Every page must fully answer "how would Lynkk work for *my* job?", with a real walkthrough and sample output, not just a feature list. |
| "Does the content provide original information, reporting, research, or analysis?" and "insightful analysis ... beyond the obvious?" | Creating helpful content | Each page needs something only Lynkk can show: a real sample note, real CRM/Jira output, real numbers from our product. |
| "Does your content clearly demonstrate first-hand expertise and a depth of knowledge (for example, expertise that comes from having actually used a product or service)?" | Creating helpful content | Show the product doing the job: screenshots, a short video, a step-by-step example. Add "Reviewed by [name, role]". |
| "Of these aspects, trust is most important." (E-E-A-T) | Creating helpful content | Security, data residency, real customer quotes, a named author or reviewer, last-updated date. |
| "There's no magical word count target, minimum or maximum." | SEO starter guide | Write as long as the job needs. In practice a complete use-case page lands around 1,200-2,000 words, but never pad. |
| Doorway abuse: "Creating substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy." | Spam policies | **Biggest risk for us.** Do not clone one template and swap "sales" for "HR". Each page needs its own workflow, examples, FAQs and proof. Link all pages from one browsable /use-cases/ hub. |
| Scaled content abuse: "many pages are generated for the primary purpose of manipulating search rankings". | Spam policies | Publish fewer, better pages. Start with the top 5 use cases, not 30 thin ones. |
| Keyword stuffing, for example "blocks of text that list cities and regions". | Spam policies | No "AI note taker for sales, sales calls, sales teams, sales reps..." blocks. Use the keyword naturally in title, H1, intro, one or two H2s. |
| Title should be "unique to the page, clear and concise, and accurately describes the contents". Brand at start or end with a delimiter. Avoid repeated boilerplate. | Title links, SEO starter guide | One unique title per page, formatted `[Use case keyword]: [benefit] \| Lynkk`. |
| Meta description: "short, unique to one particular page, and includes the most relevant points". Google mostly builds snippets from page text. | Snippets | Write a unique meta description, AND make the first paragraph a clear summary, because Google often uses that instead. |
| "Provide headings to help users navigate"; "Use one prominent heading, such as a first `<h1>`". | SEO starter guide, Title links | One H1. H2 per section. H3 for sub-points. |
| Images: "sharp and clear", "near text that's relevant"; alt text "explains the relationship between the image and your content". | SEO starter guide | Every screenshot sits next to the paragraph it proves, with descriptive alt text. |
| Link text should be descriptive; link to related pages. | SEO starter guide | Each page links to the hub, 2-3 related use cases, the matching template or comparison page, and pricing. |
| AI Overviews / AI Mode: "There are no additional requirements ... nor other special optimizations necessary." Make "important content available in textual form", support it with images and video, keep structured data matching visible text. | AI features and your website | Same page structure wins classic results and AI answers. Key facts must be in HTML text, not only inside images or video. Server-render the main content. |
| URLs: "include words in the URL that may be useful for users"; group similar topics in directories. | SEO starter guide | `lynkk.ai/use-cases/sales`, `lynkk.ai/use-cases/recruiting`, and so on. |
| One URL per piece of content; use redirects or `rel="canonical"` for duplicates. | SEO starter guide | No duplicate versions such as /solutions/sales and /use-cases/sales. |
| Ignore: meta keywords ("Google Search doesn't use the keywords meta tag"), heading order for SEO, keywords in domain. | SEO starter guide | Do not spend time on these. |

### Structured data rules (important, easy to get wrong)

| Schema | Use it? | Why |
|---|---|---|
| `Organization` (site-wide) + `WebSite` | Yes | Helps Google understand the brand and site name. |
| `BreadcrumbList` | Yes | Home > Use cases > Sales. Matches the visible breadcrumb. |
| `SoftwareApplication` | Only if we show **real** ratings | Google requires `name`, `offers.price` (use `0` for the free plan), and one of `aggregateRating` or `review`. Ratings must be visible on the page and "based on a genuine experience". If we have no real reviews yet, skip this schema rather than invent ratings. |
| `VideoObject` | Yes, if the page has a demo video | Makes the video eligible for video results. |
| `FAQPage` | Optional, no rich result | Google limited FAQ rich results to authoritative government and health sites in Aug 2023, and per Search Engine Journal is dropping the FAQ feature entirely. Keep the FAQ section for users and AI answers; the markup will not create a rich result. |
| `HowTo` | No | Deprecated in Sept 2023. |

---

## Part 2. What is actually ranking for our keywords (Ubersuggest SERP analysis)

| Keyword | What ranks in the top 10 | Lesson |
|---|---|---|
| ai for sales (US) | Salesforce product page, then guides ("15 proven use cases"), IBM explainer, Zapier listicle | Broad "AI for X" terms want **education**. A product page alone will not rank. |
| ai recruiting software (US) | Metaview "13 best AI hiring tools", Truffle "7 tools compared", Reddit, a few vendor homepages | Listicles and comparisons dominate. Needs a comparison or listicle as supporting content. |
| ai for project managers (US) | PMI, Reddit, Atlassian guide, Coursera, IBM | Informational. Win with a guide, then link to the use-case page. |
| minutes of meeting format (India) | YouTube how-to, WPS template, PDF samples, Grammarly guide, template.net | Wants a **free template plus examples**. |
| ai note taker for in person meetings (US) | AI Overview, Zoom product page, Medium review, Reddit, Plaud blog, Read.ai and Otter homepages | Mixed product and review intent, weak competition. A strong use-case page can rank directly. |
| ai meeting minutes (US) | App Store listings, Fellow templates, small blogs | Product and template mix. Use-case page plus template works. |

**Conclusion: build each use case as a small cluster, not a single page.**

```
/use-cases/                      Hub page: grid of all use cases, short intro to each
  /use-cases/sales               Use-case page (commercial intent)
     supporting: /compare/gong-alternatives        (comparison intent)
     supporting: /blog/ai-for-sales                (informational, links to use-case page)
  /use-cases/recruiting
     supporting: /templates/interview-notes        (template intent, SD 19)
     supporting: /blog/ai-recruiting-tools         (listicle intent)
  /use-cases/meeting-minutes
     supporting: /templates/minutes-of-meeting-format   (14,800/mo India, SD 10)
  /use-cases/in-person-meetings  (can rank on its own)
  ...
```

---

## Part 3. The use-case page template

Order matters: answer the searcher's question in the first screen, prove it in the middle, remove doubts at the end.
Sections marked **UNIQUE** must be written fresh for every use case. That is what keeps us clear of doorway and
scaled-content issues.

### 0. Page metadata

| Element | Rule | Example (Sales) |
|---|---|---|
| URL | `/use-cases/[role]` | `/use-cases/sales` |
| Title tag | Primary keyword + benefit + brand. Keep it short enough not to get cut off (roughly 50-60 characters). Unique per page. | `AI Note Taker for Sales Calls: Next Steps and Owners \| Lynkk` |
| Meta description | One or two sentences, unique, summarise the whole page | `Lynkk records your sales calls, online or in person, and writes the next steps, decisions and open questions with owners and dates. Start free.` |
| H1 | One only. Says what it is, for whom. Can differ from the title. | `The AI note taker for sales teams that preps, joins and follows up` |
| Breadcrumb | Visible + `BreadcrumbList` | Home > Use cases > Sales |
| Byline | "Written by [name] · Reviewed by [name, role] · Updated [date]" | Supports the "Who" in Google's Who/How/Why |

### 1. Hero (above the fold)

- **H1** (above).
- **Subheading, 1-2 sentences:** the outcome for this role, with the primary keyword used naturally. Google often lifts this into the snippet, so make it a real summary.
- **Primary CTA:** "Start free". **Secondary CTA:** "See a sample [sales] note" (anchor link to section 4).
- **Trust line:** real customer logos or a real rating and security badges, only if true. Leave out anything not yet confirmed.
- **Visual:** a real Lynkk screenshot or 30-60s video of *this* use case (for example a sales call note with next steps and owners), not a generic dashboard.

### 2. The problem, in the reader's own words (H2) **UNIQUE**

- H2 example: "Why sales reps spend more time on admin than on selling".
- 3-4 role-specific pains, each 1-2 sentences. Use language from the autocomplete and Reddit research (for example "typing notes while trying to listen", "forgetting what the client said last quarter", "follow-ups slipping after the call").
- If you cite a statistic, link the source. No made-up numbers.

### 3. How Lynkk works for [role]: before, during, after (H2) **UNIQUE content, shared structure**

This is Lynkk's differentiator and should be on every page, but the *examples must be role-specific*.

- **H3 Before the meeting:** what context Lynkk surfaces for this role (sales: last call's objections and open next steps; recruiting: previous interviewer feedback on the candidate).
- **H3 During the meeting:** what the live voice assistant does for this role (sales: "What pricing did we quote them in March?").
- **H3 Within 30 seconds after:** the exact outputs for this role (sales: next steps with owners, decisions, open questions, follow-up email; PM: Jira issues).
- One screenshot per H3, placed next to the text, with descriptive alt text.

### 4. A real example, step by step (H2) **UNIQUE, most important section**

- H2 example: "A discovery call with Lynkk, start to finish".
- Walk through one realistic meeting in 4-6 steps.
- **Show the actual output**: a sample note or summary block in HTML text (not only an image). For sales: the call note with next steps, decisions and open questions, plus the follow-up email. For recruiting: a scorecard-style interview summary. For meeting minutes: a full MoM sample.
- This section is what gives the page "original information" and "first-hand experience" in Google's terms, and it is the part AI Overviews can quote.

### 5. Jobs, features and outcomes table (H2) **UNIQUE**

| What you need to do | How Lynkk does it | Result |
|---|---|---|
| Prep for a renewal call | Surfaces past calls, open items, who said what | Walk in ahead, not cold |
| Follow up after the call | Drafts the follow-up email from the note | Follow-up sent the same day |
| ... | ... | ... |

Keep it to 5-7 rows. Only features that exist today.

### 6. Integrations for this workflow (H2)

- Show only the integrations relevant to the role (sales: Zoom, Meet, Teams, Google Calendar; PM: Jira; everyone: Slack).
- Name specific tools only once confirmed (see "Claims to confirm" below).

### 7. Proof (H2) **UNIQUE**

- One customer quote or mini case study from someone in this role: name, title, company, photo, one specific result.
- If we don't have one yet, use a "How our team uses Lynkk for [role]" story with a real named person. Never invent testimonials.

### 8. Honest comparison (H2)

- H2 example: "Lynkk vs manual notes vs traditional call recorders".
- A 3-column table on 5-6 criteria that matter for this role (in-person capture, no-bot recording, answers during calls, data region, languages, price to start).
- Be accurate about competitors. This section matches the "comparison" intent we saw in the SERPs and links to the full `/compare/` page.

### 9. Security, privacy and compliance (H2)

- Data residency (choose your region, every model processes data in that region).
- Recording consent and notifications, which matter especially for recruiting, legal and finance.
- Certifications only if confirmed (SOC 2, GDPR, and so on).
- This is the "Trust" in E-E-A-T. It is critical for HR, legal and finance pages.

### 10. Get started in 3 steps (H2)

1. Sign up free. 2. Connect your calendar (+ Jira for this role). 3. Join your next meeting or record in person.

### 11. FAQ (H2) **UNIQUE questions per page**

- 5-8 real questions taken from autocomplete, People Also Ask and sales calls (lists per use case in Part 4).
- Answer each in 2-4 sentences, starting with the direct answer.
- `FAQPage` markup is optional (no rich result, see Part 1).

### 12. Final CTA (H2)

- One sentence restating the outcome + "Start free" button.

### 13. Related use cases (H2 or block)

- 3 descriptive internal links, for example "AI note taker for customer success", "AI meeting minutes for operations teams". Plus a link back to /use-cases/.

### What must be different on every page (anti-doorway checklist)

- [ ] Problem section written for this role
- [ ] Before/during/after examples specific to this role
- [ ] A real worked example with real output
- [ ] Role-specific jobs table
- [ ] Role-specific integrations
- [ ] A testimonial or story from this role
- [ ] Role-specific FAQ questions
- [ ] Unique title, meta description, H1, screenshots and alt text

If a page can't fill at least the first four with genuinely different content, merge it into a broader page instead
of publishing it.

---

## Part 4. Page plan for the top 10 use cases

FAQ questions come from Ubersuggest Google autocomplete and question data.

### 1. Sales: `/use-cases/sales`
- **Primary keyword:** ai note taker for sales (calls). **Secondary:** conversation intelligence software, ai sales assistant, sales call recording software.
- **Title:** `AI Note Taker for Sales Calls: Next Steps and Owners | Lynkk`
- **Unique sections:** discovery-call walkthrough with the sample note and follow-up email; asking questions across an account's calls; in-person and offline meetings.
- **FAQ:** Which AI note taker is best for sales calls? Does Lynkk connect to a CRM? (Answer honestly: no.) Can AI take notes for you during a sales call? Are AI note takers accurate? Is Lynkk free to start? Do I need to tell prospects the call is recorded?
- **Supporting pages:** `/compare/gong-alternatives`, blog "AI for sales: practical use cases".

### 2. Recruiting & HR: `/use-cases/recruiting`
- **Primary:** ai note taker for recruiters / for interviews. **Secondary:** interview transcription software, interview notes.
- **Title:** `AI Note Taker for Interviews and Recruiters | Lynkk`
- **Unique sections:** scorecard-style interview summary sample; panel interview flow; comparing candidates in the knowledge graph; consent and HR compliance.
- **FAQ:** Is it OK to take notes during an interview? How do you take good interview notes? Do candidates need to consent to recording? Can Lynkk record in-person interviews? Where is interview data stored?
- **Supporting pages:** `/templates/interview-notes`, blog "Best AI recruiting tools".

### 3. Meeting minutes: `/use-cases/meeting-minutes`
- **Primary:** ai meeting minutes, minutes of meeting generator. **Secondary:** board meeting minutes, ai meeting summary.
- **Title:** `AI Meeting Minutes Generator: MoM in 30 Seconds | Lynkk`
- **Unique sections:** full MoM sample (attendees, agenda, decisions, action items with owners); board vs team meeting formats; multilingual minutes.
- **FAQ:** What should minutes of a meeting include? Who takes minutes in a meeting? Can AI write minutes of meeting? Minutes of meeting vs transcript, what's the difference? When should minutes be sent out? How long should minutes be?
- **Supporting page:** `/templates/minutes-of-meeting-format`, a free Word / Google Docs / Excel template + sample + "generate automatically with Lynkk" (targets 14,800/mo in India).

### 4. Project managers & product teams: `/use-cases/project-managers`
- **Primary:** ai note taker for project managers. **Secondary:** meeting notes to Jira, automated action items.
- **Title:** `AI Note Taker for Project Managers: Meetings to Jira | Lynkk`
- **Unique sections:** standup to Jira ticket walkthrough (show the created ticket); "what's still open" before a sprint review; MCP connections.
- **FAQ:** Can meeting notes create Jira tickets automatically? How does Lynkk assign action items? Does it work for standups and retros?
- **Supporting page:** blog "AI for project managers" (the SERP is informational).

### 5. In-person meetings: `/use-cases/in-person-meetings`
- **Primary:** ai note taker for in person meetings. **Secondary:** best / free ai note taker for in person meetings.
- **Title:** `AI Note Taker for In-Person Meetings, No Bot Needed | Lynkk`
- **Unique sections:** how capture works without a meeting bot; offline-first; multiple speakers in a room; multilingual conversations.
- **FAQ:** Is there an AI note taker for in-person meetings? Do I need a special device? How do AI note takers work offline? Can it tell speakers apart in a room? Is it free?

### 6. Marketing: `/use-cases/marketing`
- **Primary:** ai note taker for marketing teams. **Secondary:** customer interview transcription, focus group transcription.
- **Unique sections:** customer interview to messaging insights; asking questions across all past customer calls; agency client calls.
- **FAQ:** How do marketers use AI meeting notes? Can I search across all customer interviews? Can Lynkk transcribe focus groups?

### 7. Legal: `/use-cases/legal`
- **Primary:** ai note taker for lawyers. **Secondary:** ai for lawyers.
- **Unique sections:** client consultation notes; data residency; confidentiality and consent. Needs confirmed security claims before publishing.

### 8. Managers & 1:1s: `/use-cases/one-on-one-meetings`
- **Primary:** one on one meeting (template / notes). Lead with "before the meeting" context (last 1:1's open items).
- **Supporting page:** `/templates/one-on-one-meeting`.

### 9. Real estate: `/use-cases/real-estate`
- **Primary:** ai note taker for real estate agents. Showings captured in person, client follow-ups. Lower priority: buyers expect CRM sync.

### 10. Financial advisors: `/use-cases/financial-advisors`
- **Primary:** ai note taker for financial advisors. Client review meetings, compliance-friendly notes, data region. Lower priority: buyers expect CRM sync.

---

## Part 5. Technical checklist (per page)

- [ ] Indexable (no `noindex`), allowed in robots.txt, in the XML sitemap
- [ ] Main content in server-rendered HTML (not only loaded by client-side JavaScript)
- [ ] One H1, logical H2/H3s
- [ ] Unique title + meta description
- [ ] Self-referencing `rel="canonical"`
- [ ] Descriptive alt text on every screenshot; images compressed (WebP/AVIF), with width and height set
- [ ] Video: has a thumbnail, is embedded on the page, has `VideoObject` schema
- [ ] `Organization`, `BreadcrumbList` schema; `SoftwareApplication` only with real ratings
- [ ] Good Core Web Vitals on mobile (fast LCP, no layout shift from banners or carousels)
- [ ] Linked from the /use-cases/ hub, main navigation or footer, and 2-3 related pages
- [ ] Byline + last-updated date (update the date only when content actually changes, as Google warns against fake freshness)
- [ ] Track in Search Console (AI Overview and AI Mode traffic shows under "Web")

---

## Part 6. Claims to confirm before publishing

From `memory/lynkk-brand.md` "To confirm": supported meeting platforms (Zoom / Meet / Teams), which CRMs, number of
languages, available data regions, security certifications, pricing and free-tier limits, mobile/Windows apps.
Pages for legal, financial advisors and HR should not go live until the security and consent sections can be stated accurately.

---

## Sources

- Google Search Central: [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- Google Search Central: [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- Google Search Central: [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- Google Search Central: [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- Google Search Central: [Title links](https://developers.google.com/search/docs/appearance/title-link)
- Google Search Central: [Snippets and meta descriptions](https://developers.google.com/search/docs/appearance/snippet)
- Google Search Central: [Software app structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app)
- Google Search Central: [Review snippet guidelines](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)
- Google Search Central blog: [Changes to HowTo and FAQ rich results (2023)](https://developers.google.com/search/blog/2023/08/howto-faq-changes?hl=ko)
- Search Engine Journal: [Google drops FAQ rich results](https://www.searchenginejournal.com/google-drops-faq-rich-results/574429/)
- Competitor teardown: [Fireflies.ai sales page](https://fireflies.ai/sales)
- Ubersuggest SERP analysis and Google autocomplete data, 2026-10-16
