# Internal linking work order

Derived from a full crawl of all 115 sitemap URLs on 2026-11-02, cross-referenced with
Search Console data for the 3 months to 2026-11-01.

## Why this matters

Header and footer links appear on 90% or more of pages. Google discounts them heavily,
because a link present on every page carries no editorial signal. Only contextual links
(written inside body copy) transfer meaningful relevance.

Measured contextual inlinks today:

| Section | Pages | Contextual inlinks received | Pages with zero |
|---|---|---|---|
| blog | 55 | 696 | 1 |
| features | 11 | 191 | 5 |
| integrations | 11 | 127 | 1 |
| compare | 13 | 14 (all to the hub) | 12 of 12 children |
| use-cases | 11 | 0 | 11 of 11 |

The blog sends 516 of its 622 contextual links (83%) to other blog posts. Links from
blog posts to `/compare/*` and `/use-cases/*`: **zero**. Verified, not estimated.

Every link below is a new link. None of these already exist, so there is nothing to
de-duplicate.

## Priority 1: compare pages

All 12 compare child pages have zero contextual inlinks. The pricing posts are the most
natural donors, because someone reading about a competitor's pricing is already comparing.

| Add link from | To | Suggested anchor text |
|---|---|---|
| /blog/otter-ai-pricing | /compare/otter | Lynkk vs Otter.ai |
| /blog/otter-ai-alternatives | /compare/otter | Otter.ai alternative |
| /blog/fireflies-pricing | /compare/fireflies | Lynkk vs Fireflies |
| /blog/fathom-ai-pricing | /compare/fathom | Lynkk vs Fathom |
| /blog/granola-ai-pricing | /compare/granola | Lynkk vs Granola |
| /blog/gong-pricing | /compare/gong | Lynkk vs Gong |
| /blog/read-ai-vs-otter-ai | /compare/read-ai, /compare/otter | Lynkk vs Read AI, Lynkk vs Otter.ai |
| /blog/zoom-ai-companion-alternatives | /compare/otter, /compare/fireflies, /compare/granola | the relevant product name each time |
| /blog/ai-note-taker-microsoft-teams | /compare/otter, /compare/fireflies, /compare/fathom | the relevant product name each time |
| /blog/zoom-note-taker | /compare/otter, /compare/fireflies, /integrations/zoom | AI note taker for Zoom for the integration link |

Then use the two listicles as distribution hubs. These are the strongest internal pages
on the site and currently pass nothing to the commercial section:

- **/blog/best-ai-note-takers** (39 contextual inlinks, 935 impressions): link every tool
  it reviews to its matching compare page. That is up to 12 links from one post.
- **/blog/best-free-ai-note-takers** (23 inlinks): same treatment.
- **/blog/ai-powered-meeting-assistants** (18 inlinks, 879 impressions): same treatment.

Four compare pages have no natural blog donor at all: `/compare/avoma`,
`/compare/clari-copilot`, `/compare/meetgeek`, `/compare/notta`, `/compare/plaud`,
`/compare/circleback`. They depend on the three listicles above, so those links are not
optional for them.

## Priority 2: use-case pages

All 10 use-case child pages and the `/use-cases` hub have zero contextual inlinks.

| Add link from | To | Suggested anchor text |
|---|---|---|
| /blog/recruiting-interview-transcription | /use-cases/user-interviews | AI notes for user interviews |
| /blog/daily-standup-meeting | /use-cases/team-standups | AI notes for team standups |
| /blog/legal-transcription-service | /use-cases/lawyers | meeting notes for lawyers |
| /blog/is-it-legal-to-record-a-meeting | /use-cases/lawyers | meeting notes for lawyers |
| /blog/one-on-one-meeting | /use-cases/one-on-one-meetings | AI notes for one-on-ones |
| /blog/transcribe-audio-to-text | /use-cases/lectures | lecture transcription |
| /blog/ai-voice-recorders | /use-cases/lectures, /use-cases/field-interviews | the use case name |
| /blog/voice-memo-transcription | /use-cases/field-interviews | in-person interview notes |
| /blog/meeting-knowledge-management | /use-cases/customer-research | customer research notes |

### The sales methodology cluster has one legitimate path

The 11 sales methodology posts (SPIN, MEDDIC, BANT, lead qualification, mutual action
plan, key account planning, QBR template, sales forecast template, revenue operations,
sales enablement tools, sales conversation intelligence) have earned 2 clicks in three
months and no path to the product. They do have exactly one: `/use-cases/sales-calls`.

Link all 11 to `/use-cases/sales-calls`, with anchor text along the lines of
"AI notes for sales calls" or "record and log your sales calls". That converts a cluster
currently returning nothing into 11 contextual inlinks for the highest-intent use-case
page on the site. This is the cheapest single change in this document.

`/blog/sales-conversation-intelligence` is worth doing first: it has 25 contextual
inlinks, making it the third strongest internal page on the site.

## Priority 3: the hub pages

| Page | Contextual outbound links today | Children to link |
|---|---|---|
| /use-cases | 1 | 10 |
| /compare | 5 | 12 |
| /features | 5 | 10 |

Each hub should link to every child in body copy, with the child's target query as the
anchor text. Right now these hubs rely on the footer to reach their own children, which
is the same discounted-signal problem.

## Priority 4: trim the global navigation

Header and footer currently link to 46 URLs sitewide, including all 12 compare children
and all 10 use-case children. When every page is one click from every other page, nothing
is signalled as important and Google has to guess the hierarchy.

Reduce the global nav to: Home, Features, Integrations, Use cases, Compare, Pricing, Blog,
Download. Move the 22 children behind their hub pages, where Priority 3 now links them
contextually.

Do Priority 3 before Priority 4, so the children are never orphaned.

## Content gaps this exposes

Three use-case pages have no topically matching blog post to link from, so they cannot be
fixed by linking alone:

- `/use-cases/financial-advisors`
- `/use-cases/real-estate-agents`
- `/use-cases/customer-research` (only one weak donor)

And one existing post has no matching use-case page:
`/blog/medical-transcription-software` (472 impressions, 0 clicks) should point to a
medical or healthcare use-case page, which does not exist yet.

## Expected result

43 pages currently have zero contextual inlinks. Completing Priorities 1 to 3 takes that
to zero, using authority that is already on the site. No new content and no new backlinks
are required.

Target for the 90-day review: clicks from `/compare/*` and `/use-cases/*` combined move
from 2 per quarter to 40 or more.
