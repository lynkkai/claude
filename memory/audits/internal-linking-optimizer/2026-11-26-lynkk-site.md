# Internal Linking Audit: lynkk.ai

**Site**: https://lynkk.ai | **Analysis date**: 2026-11-26 | **Method**: `internal-linking-optimizer` skill (steps 1-7)
**Data**: full crawl of all 143 URLs in `sitemap.xml` (all returned 200). Links were split into
*sitewide* (header nav, footer) and *contextual* (in-body copy, related-post cards, sidebar) zones.
Sign-up, sign-in, the .dmg download and the author byline are treated as boilerplate.

Companion files:
- `2026-11-26-lynkk-link-changes.csv`: **81 prioritized changes** (from, to, anchor, placement, reason). This is the work list.
- `2026-11-26-lynkk-link-backlog.csv`: 785 unlinked keyword mentions found by text scan (for editors, review before use).

---

## Scope

| In scope | Count |
|---|---|
| Core pages (home, pricing, how-it-works, security, download, faq, etc.) | 18 |
| Blog posts | 78 |
| Blog hubs (index, 3 topic pages, author page) | 5 |
| Compare pages | 12 |
| Integration pages | 10 |
| Feature pages | 10 |
| Use case pages | 10 |
| **Total** | **143** |

Out of scope: `/share/*` (disallowed in robots.txt), app pages (`/sign-in`, `/sign-up`, `/upgrade`), downloadable files.

---

## Step 1: Current structure

| Metric | Value | Target (Hub-and-Spoke model) | Status |
|---|---|---|---|
| Internal link instances | 10,263 (72 per page) | n/a | Heavy footer (44 links on every page) |
| Contextual outlinks per page | 16.1 avg | 3-5 per cluster post minimum | Pass |
| Max click depth | 2 | <= 3 | Pass |
| True orphans (0 inlinks) | 0 | 0 | Pass |
| Pages with 0 contextual inlinks | 1 (`/meeting-and-dictation`) | 0 | Fail |
| Pages with <= 2 contextual inlinks | 4 (`/compare/notta`, `/compare/circleback`, `/compare/meetgeek`, `/support`) | 0 money pages | Fail |
| Topic cluster coverage (posts inside a topic hub) | 42 of 78 (54%) | 100% | Fail |

**Structure score: 7/10.** The crawl foundation is good: shallow, no orphans, every post linked from `/blog`,
every post has a related-posts block. The weakness is **where equity goes**: money pages (compare, integrations,
some features) are reached mostly by the footer, and the blog rarely sends contextual links to them.

**Most linked (contextual):** `/blog` 133, `/how-it-works` 92, `/pricing` 82, `/features/meeting-bot` 70,
`/features/chrome-extension` 56, `/blog/is-it-legal-to-record-a-meeting` 53.

**Under-linked important pages (contextual inlinks):**

| Page | Contextual inlinks | Note |
|---|---|---|
| `/meeting-and-dictation` | 0 | Footer only |
| `/compare/circleback`, `/compare/meetgeek` | 1 | Footer only |
| `/compare/notta` | 2 | |
| `/compare/plaud`, `/compare/avoma` | 5 | |
| `/features/workspaces` | 11 | Also a dead end: 1 contextual outlink (`/pricing`) |
| `/integrations/jira` | 7 | Missing from the `/integrations` hub grid |
| All CRM integration pages | 11-12 | No blog post links to them (see blocker below) |

**Blog to money page flow (of 78 posts):** 70 link a feature page, 34 a use case, 28 a compare page,
only **15 an integration page**.

---

## Blocker found during the audit: CRM copy contradiction

9 pages state that **"Lynkk does not connect to a CRM"** while `/integrations/hubspot`, `/salesforce`,
`/pipedrive`, `/attio` and `/zoho-crm` exist and say calls are logged on the deal:

`/blog/sales-conversation-intelligence`, `/blog/sales-enablement-tools`, `/blog/revenue-operations`,
`/blog/lead-qualification`, `/blog/bant-sales-qualification`, `/blog/sales-forecast-template`,
`/compare/gong`, `/compare/fireflies`, `/compare/fathom`.

This also explains why sales posts never link the CRM pages. **Confirm which is true first** (change C0),
fix the copy and FAQ schema, then add the CRM links (C40-C44). Note also that `memory/lynkk-brand.md`
lists "CRM fields updated" as a feature.

---

## Step 2: Orphan pages

No true orphans. Pages that are only reachable through boilerplate:

| Page | Value | Action |
|---|---|---|
| `/meeting-and-dictation` | High (product positioning) | Link from `/features/dictation`, `/features/meeting-notes`, `/download` (C80-C82) |
| `/compare/circleback`, `/compare/meetgeek`, `/compare/notta` | High (bottom-funnel) | Contextual links from listicles and alternatives posts (C15-C20) |
| `/blog/authors/samarth-wagh` | Low | Keep byline links; no action |
| `/demo` | Medium | Add to footer (S3) |

---

## Step 3: Anchor text

| Check | Finding | Risk | Action |
|---|---|---|---|
| Most used anchor | "See every guide" x133, all to `/blog` | Generic, wastes 133 links on one hub | Point each post to its own topic hub with a descriptive anchor (S5) |
| Second most used | "See how it works" x89 (95% of anchors to `/how-it-works`) | Generic, no keyword | Vary anchors (S6) |
| Related cards | Anchors are full post titles, so most posts get 50-80% identical anchors | Low, but repetitive | Add 1-2 in-copy links per key post with partial-match anchors |
| Same anchor, two targets | "AI note taker for Zoom" -> `/integrations/zoom` and `/blog/zoom-note-taker`; same for Microsoft Teams; "Zoom bot", "Google Meet bot", "Teams bot" -> both `/features/meeting-bot` and integration pages; "Lynkk" -> 4 pages | Keyword cannibalization | Give each anchor one owner (S7) |
| Empty / image-only anchors | 0 | None | None |
| Over-optimized exact match | None above 10% sitewide except generic CTAs | Low | Keep |

**Anchor score: 6/10.**

Recommended mix for a money page, using `/compare/otter` as the example:

| Anchor type | Target share | Examples |
|---|---|---|
| Exact match | 10-20% | "Otter alternative" |
| Partial match | 30-40% | "how Lynkk compares with Otter", "Otter vs Lynkk on pricing" |
| Branded | 10-20% | "Lynkk vs Otter" |
| Natural | 20-30% | "this comparison", "see the side-by-side" |

---

## Step 4: Topic clusters

| Cluster | Pillar | Posts | Pillar -> post | Post -> pillar | Sibling links |
|---|---|---|---|---|---|
| Competitors and alternatives | `/compare` | 18 | **Fail** (15 missing) | 16/18 | Pass |
| Zoom / Meet / Teams | `/blog/topic/zoom-meet-teams` | 12 | 10/12 | 10/12 | 11/12 |
| Sales meetings | `/blog/topic/sales-meetings` | 18 | 17/18 (`gong-pricing`) | 17/18 | Pass |
| Meeting templates | `/blog/topic/meeting-templates` | 12 | Pass | Pass | Pass |
| Transcription and dictation | **none** | 12 | **No pillar** | **No pillar** | Pass |
| AI assistant and knowledge | **none** | 8 | **No pillar** | **No pillar** | 7/8 |

Recommended structure: keep Hub-and-Spoke. Add two topic hubs (`/blog/topic/transcription-dictation`,
`/blog/topic/ai-meeting-assistants`) so all 78 posts sit under a pillar, and turn `/compare` into the pillar for
the pricing / vs / alternatives posts. Each topic hub should also link its matching money pages
(e.g. transcription hub -> `/features/multilingual-transcription`, `/features/dictation`, `/compare/notta`).

Bidirectional gaps between money pages and their matching posts (compare page links nothing back):
`/compare/otter` <- otter-ai-pricing, otter-ai-alternatives, read-ai-vs-otter-ai; `/compare/fireflies` <- fireflies-pricing;
`/compare/granola` <- granola-ai-pricing; `/compare/fathom` <- fathom-ai-pricing; `/compare/gong` <- gong-pricing,
call-coaching-software, sales-call-recording-software. Fixes: C3-C14.

---

## Step 5: Top contextual additions (full list in the CSV)

| # | From | To | Anchor | Where | Priority |
|---|---|---|---|---|---|
| C1 | `/blog/sales-conversation-intelligence` | `/compare/gong` | how Lynkk compares with Gong | Intro, "Gong is the best-known enterprise platform" | High |
| C70 | `/blog/is-it-legal-to-record-a-meeting` | `/security` | how Lynkk stores and protects recordings | "data protection duties" sentence | High |
| C2 | `/blog/fireflies-vs-otter` | `/compare/otter` | Lynkk vs Otter | Quick verdict | High |
| C22 | `/compare` | 15 competitor posts | pricing and head-to-head guides | New section under the grid | High |
| C15/16 | `/blog/best-ai-note-takers` | `/compare/circleback`, `/compare/meetgeek` | Lynkk vs Circleback / MeetGeek | "Other tools" line | High |
| C19 | `/blog/transcribe-audio-to-text` | `/compare/notta` | Lynkk vs Notta | Tool list | High |
| C30 | `/integrations` | `/integrations/jira` | Jira | Integrations grid | High |
| C75 | `/features/workspaces` | `/features/ask-your-meetings` | ask questions across your team's meetings | Feature description | High |
| C80 | `/features/dictation` | `/meeting-and-dictation` | meetings and dictation in one app | Intro | High |
| C78 | `/features/ask-your-meetings` | `/features/workspaces` | Enterprise workspace | "Members of an Enterprise workspace get Pro" | Medium |

**Priority addition**
- **From**: `/blog/is-it-legal-to-record-a-meeting` (53 contextual inlinks, the strongest blog page, but only 9 outlinks)
- **To**: `/security`
- **Anchor**: "how Lynkk stores and protects recordings"
- **Where**: after "A business that records people usually has data protection duties on top of the consent rule."
- **Why now**: moves equity from the top authority post to a trust page that legal and finance buyers check before buying.

---

## Step 6: Navigation and footer

| Element | Current | Recommended | Reason |
|---|---|---|---|
| Main nav | Home, How it works, Use cases, Pricing, Blog (+ sign-in, sign-up, download) | Add Features and Integrations (or a Product dropdown) | Both hubs rely on the footer today |
| Footer | 44 links: 12 compare, 10 use cases, 5 of 10 features, 0 integrations | Add an Integrations column (Zoom, Meet, Teams, HubSpot, Salesforce, Jira); complete Features; add Demo | Integration pages get 7-22 inlinks vs 142 for footer pages |
| Sidebar (blog) | Download + Pro CTA, author | Add "Related comparison" slot that maps the post to its compare page | Cheap way to fix compare under-linking at scale |
| Breadcrumbs | Present on blog | Include topic hub level (Blog > Sales meetings > Post) | Reinforces pillar links on every post |

---

## Step 7: Implementation plan

| Metric | Current | Target | Gap |
|---|---|---|---|
| Pages with 0 contextual inlinks | 1 | 0 | 1 |
| Money pages with <= 5 contextual inlinks | 6 | 0 | 6 |
| Blog posts inside a topic hub | 54% | 100% | 36 posts |
| Blog posts linking an integration page | 19% | 40%+ | ~17 posts |
| Generic CTA anchors | 222 | < 10% of contextual anchors | Replace S5/S6 |

| Phase | Timing | Actions (CSV ids) |
|---|---|---|
| Critical | Week 1 | C0 (confirm CRM copy), compare links C1-C24, Jira hub fix C30-C32, security C70-C74, dead-end features C75-C83 |
| Clusters and sitewide | Weeks 2-3 | Topic hub fixes C50-C55, new hubs C56/C62 with links C57-C65, integrations C33-C36, feature links C84-C90, footer and nav S1-S4, CRM links C40-C44 once C0 is resolved |
| Optimization | Week 4+ | Anchor fixes S5-S7, work through `link-backlog.csv`, re-crawl and compare |

**Tracking**
- [ ] Rankings for compare, integration and topic hub target keywords
- [ ] Organic sessions to `/compare/*` and `/integrations/*`
- [ ] Search Console crawl stats and internal links report
- [ ] Re-run this crawl after each phase (contextual inlinks per money page)
- [ ] New posts linked from their topic hub within 48 hours of publishing

---

## Handoff summary

- **Status**: audit complete, no changes made to the live site (site code is not in this repo).
- **Blocking issue**: CRM integration copy contradiction on 9 pages (C0). Needs a product answer.
- **Top 3 fixes**: compare pages under-linked from the blog; 36 posts with no topic hub; integration pages missing from footer and blog.
- **Next best skill**: `on-page-seo-auditor` to check the compare and integration pages after links ship.
