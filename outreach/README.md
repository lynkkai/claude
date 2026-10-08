# Lynkk backlink outreach: free guest posts, listicle inclusions, directories

Researched 2026-10-08 with Ubersuggest (competitor backlink gap: otter.ai, fireflies.ai,
fathom.video, tldv.io, read.ai vs lynkk.ai) and web search.

## Files

| File | What it is | Rows |
|---|---|---|
| `guest-post-prospects.csv` | Sites with a "write for us" / contributor program in SaaS, AI, sales, CRM, productivity, remote work, HR, PM, knowledge management | 86 sites, 20 with a published email |
| `competitor-listicle-targets.csv` | Pages that already link to Otter / Fireflies / Fathom / tl;dv / Read.ai (from Ubersuggest). Ask the editor to add Lynkk | 43 pages |
| `ai-directories.csv` | Free AI tool directories and marketplaces to list Lynkk on | 16 |
| `outreach-emails.csv` | One row per email (deduplicated), with `source_url` and `last_checked`. Columns: email,website,submission_url,source_url,niche,opportunity,notes,last_checked | 504 emails (472 free, 32 paid only) |
| `best-fit-send-queue.csv` | The 225 "best fit" rows from `outreach-mail-merge.csv`, with the site name in the subject and opening line ("I came across HelpDesk") instead of the domain. Signed Samarth Wagh, Co-founder, Lynkk, with no URLs in the body (the Gmail connector rewrites every link into a google.com/url redirect). Split into 9 batches of 25 (`batch`), with a `status` column to track sends | 225 emails |

Emails in the CSV were taken from the site's own write-for-us page as shown in search
results. Pages were not opened directly (the research environment could not load
websites), so confirm each address on the live page before sending.
Rows with no email use a contact form, or the email was not visible in the search snippet.

## Priority order (highest return for zero cost)

1. **Listicle inclusion** (`competitor-listicle-targets.csv`). These editors already
   cover AI meeting assistants. A short "please consider adding Lynkk" note with one
   differentiator (live voice assistant in the meeting, data residency, Jira + CRM
   automation) converts far better than a cold guest post pitch.
2. **Free listings** (`ai-directories.csv`, plus AlternativeTo, Product Hunt, the
   `awesome-generative-ai` GitHub list, Zoom / Teams / Webex / HubSpot marketplaces).
   No outreach needed, just submit.
3. **Guest posts** (`guest-post-prospects.csv`). Best fits: RingCentral, Sales Enablement
   Collective, Userlist, Kayako, HelpDesk, Callbox, NetHunt, Flowlu, Helpjuice, Remote Clan,
   buildd, scoocs (hybrid events), ZPlatform, ToolJunction.

## About the 1,000-email target

Status on 2026-10-08: **504 unique emails** in `outreach-emails.csv` (20 from the first
pass plus 484 new). Breakdown:

| Group | Count | How to read it |
|---|---|---|
| Free, relevant niche | 225 | SaaS, AI, sales, CRM, productivity, remote work, HR, CX, marketing, tech. Start here |
| Free, SEO template network | 68 | Same-template "X Write For Us" sites (contact@ inboxes). Low editorial value |
| Free, off-niche | 179 | Health, travel, home, pets, fashion, etc. Kept to reach the count; low fit for Lynkk |
| Paid only | 32 | Flagged `paid only`; skip for free outreach |

Filter by the `notes` column ("Off-niche", "SEO template network") to focus the list.

Method for this pass: the environment's network policy still blocked every outbound
website (proxy returned 403 on CONNECT, and WebFetch could not resolve hosts), so no page
could be opened or scraped. Emails were collected from web search result text for about
200 niche queries ("write for us" plus SaaS, AI, sales, CRM, sales enablement,
productivity, remote and hybrid work, meetings, customer success, CX, contact center, HR,
recruiting, project management, knowledge management, startups, small business,
marketing, automation, data science). Only addresses printed in the result text for a
specific page were kept; none were guessed or constructed. Addresses the search flagged
as typos, placeholders or unrelated embedded data were dropped.

Every new row says "not yet confirmed on live page". Open `source_url` and confirm the
address before sending. Search-only harvesting yields about 1-5 emails per query and was
falling to about 1, which is why the total is far below 1,000.

Ubersuggest: `backlink_opportunity` returned nothing for the competitor set, and
`backlinks` for fireflies.ai returned mostly DA 88+ news, university and app store pages,
not realistic free guest post targets. No emails come from Ubersuggest.

To reach 1,000, run a fresh session after setting Network access to Full (or allowing
the needed domains), then:

- Scrape `https://guestpostlive.com/free-guest-post-sites-2026/` (116 sites with emails),
  `https://serpforge.io/blog/link-building/free-guest-posting-sites/`,
  `https://blog.linkforce.io/free-guest-posting-sites/` and the mentionagent.ai lists.
- Fetch write-for-us, contact and about pages for every site in all CSVs and extract
  printed emails (mailto links and "name [at] domain [dot] com" forms).
- In the Ubersuggest web app, export the full Backlink Opportunity report for the five
  competitors and filter to DA 20-70 blogs.

Quality beats volume here: 50 well-fitted pitches will likely earn more links than 1,000
generic ones.

## Rules to stay safe

- **Link exchanges:** Google's spam policies treat "excessive link exchanges" and
  paid links as link schemes. Keep any exchange occasional and editorially relevant, and
  never pay for a dofollow link without `rel="sponsored"`.
- **Cold email law:** Pitch only addresses published for contributor contact, send
  individually (no bulk blasts), include who you are and an easy opt-out, and stop on any
  "no". This keeps you within CAN-SPAM and GDPR legitimate-interest norms.
- Several sites in the list also sell sponsored posts. Ask for their free editorial track.

## Pitch templates

**Listicle inclusion**

> Subject: A tool for your "[article title]" roundup
>
> Hi [Name],
>
> I read your [article title] and liked how you compared [Otter / Fireflies] on [detail].
> I work on Lynkk (lynkk.ai), an AI meeting assistant that joins the call and answers
> questions by voice during the meeting, then turns it into notes, CRM updates and Jira
> tickets within 30 seconds. It also lets teams choose the region where their data is
> processed.
>
> If you update the piece, would you consider adding it? Happy to set up a free account
> or send screenshots.
>
> Thanks,
> [Name], Lynkk

**Guest post**

> Subject: Guest post idea: [specific title]
>
> Hi [Name],
>
> I'd like to contribute an original article to [blog] on [topic]. Three angles:
>
> 1. [e.g. How sales teams cut post-call admin from 20 minutes to zero]
> 2. [e.g. Data residency for AI note takers: what legal teams ask before approving one]
> 3. [e.g. Running in-person meetings that are as searchable as Zoom calls]
>
> Each would be [1,200-1,500] words, written from first-hand experience, with no
> promotional copy. Samples: [link], [link].
>
> Best,
> [Name], Lynkk (lynkk.ai)
