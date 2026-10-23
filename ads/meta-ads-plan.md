# Lynkk: Meta Ads (Facebook + Instagram) Plan

Research date: 2026-10-23. Built with the `meta-ads-library` skill workflow
(`.claude/skills/meta-ads-library`). The skill's live Ads Library tools need the Hyper MCP
plus an Apify connection, which were not connected in this session, and facebook.com/ads/library
blocks direct fetches. So the competitor section below is built from public reviews and pricing
pages, not from scraped ads. Section 9 lists the exact Ads Library pulls to run once Hyper MCP is
connected, so the creative angles can be checked against what competitors actually run.

---

## 1. What we are selling (verified on lynkk.ai, 2026-10-23)

The live site has moved from "AI meeting assistant for everyone" to **AI meeting notes and
conversation intelligence for revenue teams**.

- **Headline:** "Your revenue lives in your conversations. Don't lose it."
- **Who it's for (site):** sales reps (call prep, follow-ups, action items), sales leaders (deal
  visibility, coaching), RevOps (consistent records, connected workflows).
- **Capture:** meeting bot (Zoom, Google Meet, Microsoft Teams), Mac app (also WebEx, WhatsApp,
  FaceTime calls), Chrome extension, in-room / offline recording.
- **Output:** transcript, summary, decisions, action items. Summary formats: Sales Call, General
  Meeting, Customer Interview.
- **Account memory:** all calls for an account grouped and searchable.
- **Ask Lynkk (Pro):** answers across all calls with source citations, also in Slack.
- **Follow-ups:** drafts follow-up emails from call context.
- **Tasks:** action items across meetings with a Kanban board, send to Jira.
- **Cue (beta, Mac, invite only):** live assistant panel during calls.
- **Languages:** 17 languages plus **Hinglish** (mixed Hindi + English), on every plan.
- **Integrations:** Google Calendar, Outlook Calendar, Slack, Jira, custom MCP servers.
- **Pricing:**
  - **Free:** $0 forever, no card. Unlimited notes (up to 2 hours each), first 5 hours of AI summaries.
  - **Pro:** $15/month or $117/year (about $9.75/month). Unlimited summaries, Ask Lynkk, Slack
    answers, meeting video, weekly digest.
  - **Enterprise:** custom, workspace for up to 10 people, admin controls. Demo booking required.
- **Platforms:** web app, Mac app, Chrome extension. **No iOS, Android or Windows desktop app listed.**
- **Privacy:** GDPR and India DPDP Act referenced. Processing may occur in India and the US.
  AES-256-GCM, TLS 1.2+. No SOC 2 / ISO 27001 stated.

### Claims we must NOT make in ads (not supported by the site today)

| Claim | Status on site | Use instead |
|---|---|---|
| "Updates your CRM automatically" | No direct CRM sync yet; briefs copy into Salesforce / HubSpot | "CRM-ready call briefs" |
| "Choose your data region" / data residency | Not stated | Leave out until confirmed |
| SOC 2 / ISO certified | Not stated | "Encrypted with AES-256" |
| "Live AI that speaks in your meeting" for everyone | Cue is beta, Mac, invite only | Label it "beta" or leave it out of cold ads |
| "Notes in 30 seconds" | Not re-verified on the current site | Confirm with product before using |

Meta reviews ads against landing pages. A claim the page doesn't back up can get the ad rejected,
and it also damages trust after signup.

---

## 2. Competitor landscape

### Global AI notetakers (the comparisons buyers read)

| Competitor | Positioning | Free plan | Paid (approx., verify) | Where Lynkk wins |
|---|---|---|---|---|
| **Fathom** | Best free notetaker, Zoom-first | Unlimited recordings + summaries | Premium ~$16-20/mo, Team ~$15-19/user | Hinglish, in-person + WhatsApp calls, account memory |
| **Fireflies.ai** | Sales + integrations, many languages | Limited storage | ~$10-18 Pro, ~$19-29 Business | Hinglish works on Free (Fireflies' mixed Hindi-English is a beta on Business, per one comparison) |
| **Otter.ai** | Live transcription, archives | 300 min/mo, 30 min per conversation | ~$8.33-16.99/mo | 2-hour notes on Free, sales-specific summaries |
| **Granola** | Bot-free notepad, Mac-first | 25 meetings lifetime | ~$14 Business | Bot *and* bot-free, sales focus, Free has no meeting cap |
| **Read AI** | Meeting + email analytics | 5 transcripts/mo | ~$15-20/mo | Unlimited notes on Free |
| **tl;dv** | Privacy, EU storage | Limited | ~$18/mo | Indian languages, price |

### Sales conversation intelligence (the "Gong tax" alternatives)

| Competitor | Price (approx., verify) | Where Lynkk wins |
|---|---|---|
| **Gong** | ~$100-250/user/mo + $15K-65K implementation, 3-6 months | $15/mo, self-serve, live in minutes |
| **Avoma** | ~$19-79+/user/mo | Free forever plan, Hinglish |
| **Attention, AskElephant, Clari Copilot, Salesloft** | ~$59-399/user/mo | Price, no sales-call required to start |

### India-first notetakers (direct competitors for the Hinglish angle)

| Competitor | Angle | Price | Where Lynkk wins |
|---|---|---|---|
| **MeetNotes** | Hindi, Hinglish, Gujarati, in-person, sales & distribution teams | n/a | Zoom/Meet/Teams bot, Jira, Slack, MCP, Ask across calls |
| **MeetMinutes** | "No.1 note taker for Indian languages" | ₹1,299-2,499/mo | Free forever plan; Pro at $15 is in the same range |
| **JotMe, Noter AI** | Hindi notes, bot-free / phone recording | n/a | Sales workflow (account memory, follow-ups, tasks) |

### Positioning gap Lynkk can own

> **The sales-call notetaker that understands Hinglish, works on WhatsApp and in-person calls,
> and is free to start.**

No global player owns Hinglish, and the India-first players aren't built around a sales workflow.
For English-only markets, the angle is **"Gong-level call memory at a notetaker price"**.

---

## 3. Who to target: audience personas

| # | Persona | Market | Pain | Hook | Offer |
|---|---|---|---|---|---|
| P1 | **Indian B2B sales rep / AE / BDM** (SaaS, fintech, edtech, real estate, pharma, distribution) | India + UAE | Calls in Hinglish, notes in English for the manager, CRM never updated | "Your calls are in Hinglish. Your notes shouldn't be a mess." | Free forever |
| P2 | **Founder-led sales / startup founder** | India, US, UK, SG | Back-to-back calls, forgets follow-ups, no sales team yet | "You're the sales team. Lynkk is your memory." | Free, then Pro |
| P3 | **Sales leader / manager** (team of 3-10) | India, US, UK | No visibility into deals without listening to calls | "Know what was said on every deal without sitting in on calls." | Enterprise demo (10-seat workspace) |
| P4 | **Agency / consultant / account manager** | All | Client calls across Zoom, Meet, WhatsApp; promises get lost | "Every client promise, tracked." | Free |
| P5 | **Gong-curious SMB** | US, UK, CA, AU | Want call intelligence, can't justify Gong | "Call intelligence without the Gong bill." | Pro $15 |
| P6 | **Retargeting: free users who used up the 5 summary hours** | All | Notes still record but no summaries | "Your last 3 calls have no summary yet." | Pro upgrade |

Start with **P1 + P2 in India** and **P2 + P5 in English Tier 1**. P3 runs once we have 20+ team
signups to build lookalikes. P6 is always on.

---

## 4. Targeting settings

### 4.1 Location

| Pod | Countries / cities | Why |
|---|---|---|
| **India (primary)** | Bengaluru, Mumbai, Delhi NCR (incl. Gurugram, Noida), Pune, Hyderabad, Chennai. Phase 2: Ahmedabad, Kolkata, Jaipur, Chandigarh, Kochi, Indore | Hinglish edge, CPMs around $1-3 (vs $16-23 US), weak competitor coverage, DPDP Act already in the privacy policy |
| **Gulf** | UAE (Dubai, Abu Dhabi), Saudi Arabia (Riyadh) | Large Indian-origin sales workforce, Hinglish works there too, mid CPMs |
| **English Tier 1** | United States, United Kingdom, Canada, Australia, Singapore | High value per user, where Fathom / Fireflies / Gong buyers are |

- Location type: **"People living in or recently in this location"** (default). Don't use "traveling in".
- Keep India and English Tier 1 in **separate campaigns**. CPMs differ by roughly 10x, and a
  combined budget will drain toward the cheap geo.

### 4.2 Age

- **Minimum age: 22** (this is a hard limit in Meta).
- Suggested range: **24-55**, core 25-44. Under Advantage+ Audience, the maximum age is only a
  suggestion, so Meta can go past it.
- Sales-leader ads (P3): suggest 28-55.

### 4.3 Gender

- **All genders.** Don't split ad sets by gender. Gender isn't a buying signal for this product,
  and splitting just shrinks the learning pool.
- Watch the breakdown report (Breakdown > Delivery > Gender). If one gender converts at 2x+ lower
  CPA after 100+ signups, adjust the **creative** (presenter, setting) rather than the targeting.
- Cast both men and women as presenters in UGC and demo videos.

### 4.4 Language

- **Don't set language targeting for India.** Most Indian professionals run Facebook in English,
  so a Hindi language filter would cut out the very people we want. Reach Hinglish speakers through
  **India geo + Hinglish creative**.
- English Tier 1: leave blank.

### 4.5 Detailed targeting (signals, not hard limits)

Since early 2026, interests and demographics in Meta act as **suggestions** that Meta can widen,
and detailed-targeting exclusions have been removed. Use these as starting signals for Advantage+
Audience. Check each name in Ads Manager, because Meta has merged many interests.

**Sales tools and CRMs:** Salesforce, HubSpot, Zoho CRM, Freshworks / Freshsales, Pipedrive,
LinkedIn Sales Navigator, Apollo.io, Outreach, Gong, Salesloft.

**Meeting / work tools:** Zoom, Google Meet, Microsoft Teams, Google Workspace, Slack, Jira /
Atlassian, Notion, Calendly.

**Topics:** Sales, Business-to-business, Business development, Account management, Customer
success, Lead generation, Software as a service, Startup company, Entrepreneurship, Productivity.

**Demographics / behaviours (if still available in your account):** Small business owners,
Business page admins, Job titles such as Sales Manager, Account Executive, Business Development
Manager, Founder, Co-founder, Head of Sales, Key Account Manager.

**Competitor interests:** Meta rarely exposes Otter.ai / Fireflies / Fathom as interests. Use
them if they show up, but don't count on it. Go after competitor users through **creative and
comparison landing pages** instead (section 6).

### 4.6 Custom audiences (these are the real control lever now)

| Audience | Source | Window | Use |
|---|---|---|---|
| All website visitors | Pixel | 30 / 90 d | Retargeting |
| Pricing page visitors | Pixel, URL contains `/pricing` | 30 d | Retargeting with the Pro offer |
| Signed up, not activated (no meeting recorded) | CAPI event / customer list | 14 d | Onboarding ads ("connect your calendar") |
| Free users past 5 summary hours | Customer list from product DB, synced weekly | rolling | P6 upgrade campaign |
| Pro customers | Customer list | all | **Exclude** from acquisition, seed lookalikes |
| Video viewers 50%+ | FB / IG video | 30 d | Retargeting |
| IG / FB profile engagers | Engagement | 60 d | Retargeting |
| Employees / team | Customer list | all | **Exclude** everywhere |

### 4.7 Lookalikes

- Seed: **activated users** (recorded 1+ meeting) is better than raw signups, and **Pro + Enterprise** is best.
- Meta needs a minimum of 100 people in the seed country; aim for 1,000+.
- India: 1%, then 1-3%. US / UK: 1-3% (the 1% pool is small and expensive).
- Run lookalikes as an Advantage+ Audience **suggestion**, alongside the broad ad set.

### 4.8 Exclusions

- Custom-audience exclusions still work: exclude Pro customers, employees, and signups from the
  last 7 days in prospecting campaigns.
- Detailed-targeting exclusions (for example "students") are **gone**. Filter students and job
  seekers through creative ("for sales teams") and the landing page instead.

---

## 5. Campaign structure and ad settings

### 5.1 Account setup (do this before spending)

1. **Business Manager:** verify the business and the `lynkk.ai` domain.
2. **Pixel + Conversions API (CAPI)** on lynkk.ai and the app, with server-side events deduplicated by `event_id`.
3. **Events to send:**

| Event | Trigger | Used for |
|---|---|---|
| `PageView` | every page | audiences |
| `ViewContent` | pricing page, comparison pages | audiences |
| `CompleteRegistration` | account created | **optimization, phase 1** |
| `Activated` (custom) | first meeting recorded or calendar connected | **optimization, phase 2** |
| `Subscribe` (value: 15 or 117 USD) | Pro payment via Paddle webhook | ROAS, phase 3 / P6 |
| `Lead` | Enterprise demo booked | P3 campaign |

4. **UTMs on every ad:**
   `utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}`
5. Connect the signup form to store `fbclid` / `_fbc` / `_fbp` so CAPI events match.

### 5.2 Campaigns

| Campaign | Objective | Conversion location | Optimize for | Budget type | Audience |
|---|---|---|---|---|---|
| **C1 IN Prospecting** | Leads (or Sales) | Website | `CompleteRegistration`, switch to `Activated` once 50+/week | CBO (Advantage+ campaign budget) | Ad set A: Advantage+ Audience with sales-tool signals. Ad set B: lookalike 1-3% (once seed exists) |
| **C2 T1 Prospecting** (US, UK, CA, AU, SG) | Leads | Website | `CompleteRegistration`, then `Activated` | CBO | Same two ad sets |
| **C3 Gulf Prospecting** (AE, SA) | Leads | Website | `CompleteRegistration` | CBO | Advantage+ Audience |
| **C4 Retargeting, all geos** | Sales | Website | `Subscribe` (fall back to `CompleteRegistration` if volume is low) | ABO | Visitors 30d, pricing 30d, video 50% 30d, minus signups |
| **C5 Pro upgrade (P6)** | Sales | Website | `Subscribe` | ABO, small | Free users past 5 hours (customer list) |
| **C6 Team demo (P3), phase 2** | Leads | **Instant form** or website | `Lead` | ABO | Sales leaders, lookalike of Enterprise accounts |

### 5.3 Ad set settings

- **Performance goal:** Maximize number of conversions.
- **Bid strategy:** Highest volume first. After 2-3 weeks of stable data, add a **Cost per result
  goal** at about 1.2x the actual CPA.
- **Attribution:** 7-day click + 1-day view (default). For reporting to the team, also read the
  7-day click column, because view-through inflates numbers for B2B.
- **Placements:** Advantage+ placements. Priority surfaces are Instagram Reels, Facebook / IG Feed
  and Stories. Watch Audience Network in the placement breakdown; if it drives junk signups, move
  budget to a manual-placement ad set (check whether placement exclusions are still available in
  your account, since one source reports they were removed in August 2026).
- **Devices:** all. About 90%+ of delivery will be mobile. See section 5.5 for the mobile gap.
- **Schedule:** run all day. Only add a weekday schedule (needs a lifetime budget) if weekend CPA
  is 30%+ worse after 4 weeks.
- **Advantage+ creative enhancements:** keep *visual touch-ups* and *brightness/contrast*.
  **Turn off** text improvements, music, image expansion, and "add overlays". These can rewrite
  claims, add dashes, or misspell the brand.
- **Frequency:** keep retargeting under about 4 per week. If prospecting frequency goes over 2.5
  per week while CTR drops, refresh the creative.
- **Learning phase:** each ad set needs about 50 optimization events per week. With a small
  budget, use **fewer ad sets** rather than many starved ones.

### 5.4 Budget (directional, recheck against your own data)

Planning assumptions from public 2026 benchmarks (vendor blogs, not B2B-specific): India CPM
~$1.5-3, US ~$16-23, UK ~$10-12. CTR 0.8-1.5%. Landing page to free signup 10-20%.

| Geo | Est. CPC | Est. cost per free signup | Starter daily budget | Monthly |
|---|---|---|---|---|
| India | $0.15-0.40 | $1-4 (₹85-330) | $25 (~₹2,100) | ~$750 |
| Gulf | $0.50-1.20 | $4-10 | $10 | ~$300 |
| English Tier 1 | $1.50-3.00 | $10-30 | $40 | ~$1,200 |
| Retargeting + upgrade | n/a | n/a | $10 | ~$300 |
| **Total** | | | **$85/day** | **~$2,550** |

- If budget is tight, run **India + retargeting only** (~$35/day) for the first 4 weeks, then add
  Tier 1 using the winning creative.
- **Expect CPMs to rise 30-60% in Q4 (Oct-Dec)**. We're launching in late October, so judge CPAs
  against that seasonal lift.
- The metric that counts is **cost per activated user** and **free to Pro rate**, not cost per
  signup. A $2 signup who never records a meeting is worth nothing.

### 5.5 The mobile gap (fix this before scaling)

Most Meta clicks come from phones, but Lynkk works on the web, Mac and Chrome only. On the landing page:

1. Let people **sign up and connect Google / Outlook calendar on mobile web**. The bot can then join
   their next Zoom / Meet / Teams call without a desktop.
2. Show a mobile-only prompt: "We'll send the desktop link to your email" and send a reminder email.
3. Make sure **in-room recording works on mobile web**, or don't promise it in mobile ads.
4. Send Mac-only features (Cue, WhatsApp / FaceTime call capture) only in Mac-angle creatives.

---

## 6. Content structure

### 6.1 Video structure (Reels / Stories / Feed video, 15-30 s)

| Time | Beat | What's on screen |
|---|---|---|
| 0-2 s | **Hook** (pattern break, pain line as on-screen text) | Rep finishing a call, staring at an empty notes doc |
| 2-6 s | **Problem** | "3 calls, 0 notes, CRM not updated, manager asking for an update" |
| 6-18 s | **Demo** | Bot joins Zoom, then the summary, action items and drafted follow-up email appear |
| 18-24 s | **Proof / differentiator** | Hinglish transcript shown cleanly in English, or "Ask Lynkk: what did Ravi say about pricing?" with the cited answer |
| 24-30 s | **CTA** | "Free forever. No card." plus logo, lynkk.ai |

- Burn in captions (most people watch muted). Keep text inside the 9:16 safe zone (leave the top
  14% and bottom 20-35% clear).
- Show the logo by second 3 and spell it **Lynkk** on screen.
- Use a real product screen recording, not stock footage.

### 6.2 Formats to produce (first batch: 8 concepts)

Creative variety is now what drives audience discovery in Meta, so test **different concepts**,
not five versions of one headline.

| # | Concept | Format | Persona | Geo |
|---|---|---|---|---|
| 1 | **Hinglish demo:** rep talks in Hinglish, notes come out clean | 9:16 UGC video | P1 | IN, Gulf |
| 2 | **"3 calls, 0 notes"** day-in-the-life of a sales rep | 9:16 UGC video | P1, P2 | All |
| 3 | **Before / after:** messy notebook vs Lynkk summary | 4:5 static | P1, P4 | All |
| 4 | **Before / during / after the call** | 4:5 carousel (3 cards + CTA card) | P2, P4 | All |
| 5 | **Gong tax:** "$15 vs $1,200+ per seat per year" | 4:5 static, price comparison | P5 | T1 |
| 6 | **Ask Lynkk:** typed question, answer with citation | 9:16 screen recording | P2, P3 | All |
| 7 | **WhatsApp + in-person:** "Your best deals don't happen on Zoom" (Mac app) | 9:16 video | P1, P4 | IN, Gulf |
| 8 | **Founder talking head:** why we built Lynkk | 9:16 video, 30-45 s | P2 | All |
| 9 (P6) | **"Your last calls are waiting for a summary"** | 1:1 / 4:5 static | P6 | Retargeting |

### 6.3 Copy bank (no em or en dashes, brand always "Lynkk")

Primary text: keep the first 125 characters strong (that's all most people see before "more").
Headline: 40 characters or fewer. CTA buttons: **Sign up** (prospecting), **Get offer** / **Subscribe** (P6), **Book now** (P3).

**Concept 1, Hinglish (India / Gulf)**
- Primary: `Client se baat Hinglish mein, manager ko update English mein. Lynkk joins your call and writes clean notes, action items and the follow-up email. Free forever.`
- Headline: `AI notes that get Hinglish`
- Description: `17 languages + Hinglish. No card.`

**Concept 2, "3 calls, 0 notes"**
- Primary: `Back-to-back calls and zero notes? Lynkk records your Zoom, Meet and Teams calls, then gives you the summary, next steps and a drafted follow-up. Free to start.`
- Headline: `Never write call notes again`

**Concept 3, before / after**
- Primary: `Left: what you remember after a sales call. Right: what Lynkk gives you. Summary, decisions, action items, and every call for the account in one place.`
- Headline: `Your call notes, done for you`

**Concept 4, carousel**
- Card 1: `Before the call: see what was said last time`
- Card 2: `During: Lynkk records, online or in the room`
- Card 3: `After: notes, tasks, follow-up email drafted`
- Card 4: `Free forever. No card needed.`
- Primary: `One AI for the whole sales call, before, during and after. Works with Zoom, Google Meet and Microsoft Teams.`

**Concept 5, Gong tax (Tier 1)**
- Primary: `Call intelligence shouldn't need a 6 month rollout. Lynkk gives your reps notes, account memory and answers across every call for $15 a month. Start free today.`
- Headline: `Call intelligence, minus the bill`
- Only name Gong with accurate, sourced pricing on the landing page; otherwise say "enterprise call tools".

**Concept 6, Ask Lynkk**
- Primary: `"What did the client say about budget?" Ask Lynkk and get the answer from your calls, with the exact quote. No more rewatching recordings.`
- Headline: `Search every sales call`

**Concept 7, WhatsApp / in-person (Mac)**
- Primary: `Your best deals happen on WhatsApp calls and across the table, not just on Zoom. The Lynkk Mac app captures them all and turns them into notes and next steps.`
- Headline: `Notes for every call, not just Zoom`

**P6 upgrade**
- Primary: `You've used your 5 free summary hours. Your recordings are safe, and Pro writes summaries and action items for every call for $9.75 a month, billed yearly.`
- Headline: `Unlock unlimited summaries`

### 6.4 Creative specs

| Placement | Ratio | Size | Notes |
|---|---|---|---|
| Reels / Stories | 9:16 | 1080 x 1920 | Safe zone for text, captions burned in, max 60 s (aim for 15-30 s) |
| Feed (FB / IG) | 4:5 | 1080 x 1350 | Best feed real estate |
| Feed / carousel | 1:1 | 1080 x 1080 | Carousel 2-10 cards |
| File | MP4 / MOV, H.264; JPG / PNG | | Under 4 GB video, under 30 MB image |

Upload 9:16 + 4:5 versions of each concept so Meta doesn't auto-crop.

---

## 7. Landing pages (match ad to page)

| Ad concept | Landing page | Must show above the fold |
|---|---|---|
| 1, 7 | `lynkk.ai/hinglish` (TODO: create) | Hinglish transcript example, "Free forever", Google / Outlook sign-in |
| 2, 3, 4, 6 | `lynkk.ai` or `lynkk.ai/sales` | Sales call summary screenshot, Zoom / Meet / Teams logos |
| 5 | `lynkk.ai/vs/gong` (TODO) | Accurate side-by-side table with date and sources |
| P6 | `lynkk.ai/pricing` with `?plan=pro` | Pro price, 7-day refund |
| P3 | Demo booking page or Instant Form | 10-seat workspace, admin controls |

---

## 8. Testing plan and KPIs

**Weeks 1-2:** 4 concepts (1, 2, 3, 5) x India + Tier 1. Don't touch anything for the first 3-4 days
of learning.
**Weeks 3-4:** turn off the bottom half by cost per signup, add concepts 4, 6, 7, switch the winning
ad set to `Activated` optimization if it reaches 50 events per week.
**Month 2:** turn on lookalikes from activated users, launch P3 team demo, refresh the creative
every 2-3 weeks.

| KPI | Healthy target (starting point) | Action if missed |
|---|---|---|
| Thumbstop (3 s views / impressions) | 25%+ | New hook, first 2 seconds |
| Hold rate (15 s views / 3 s views) | 30%+ | Tighten the middle, show the product sooner |
| CTR (link) | 1%+ | New angle / offer |
| LP to signup | 15%+ | Fix landing page, mobile flow |
| Signup to activated | 40%+ | Onboarding, calendar connect on mobile |
| Free to Pro (60 d) | 3-5% | P6 campaign, pricing page |
| Kill rule | Ad spent 3x target CPA with 0 signups | Pause |

---

## 9. Ads Library research to run (once Hyper MCP + Apify are connected)

These map straight onto the skill's `meta_ad_library_ads_search` tool. Use `active_status="active"`,
`period="last30d"`, `count=40`.

| Query / advertiser | Countries | Why |
|---|---|---|
| `AI note taker` | US, IN, GB | Category hooks and CTAs |
| `AI meeting assistant` | US, IN | Category hooks |
| `sales call notes` / `call recording` | US, IN | Sales-specific angles |
| `Hinglish` / `Hindi meeting notes` | IN | Is anyone running the Hinglish angle yet? |
| Fathom, Fireflies.ai, Otter.ai, Granola, Read AI, tl;dv | US, IN | Top-advertiser snapshot, offers, formats |
| Gong, Avoma, Attention | US, GB | Sales leader messaging |
| MeetNotes, MeetMinutes | IN | Direct India rivals |

Then follow the skill's Phase 4 output: top advertisers table, common CTAs and hooks, recently
launched ads, each with its `ad_library_url`. Update sections 2 and 6 with what's actually running.

To check by hand in a browser now:
`https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q=AI%20note%20taker&search_type=keyword_unordered`
(change `country` and `q` as needed).

---

## 10. Open items for the team

- [ ] Confirm "notes within 30 seconds" is still true before using it in ads.
- [ ] Confirm the data residency claim (memory says users can pick a region; the site doesn't say so).
- [ ] Build `/hinglish` and `/vs/gong` landing pages.
- [ ] Install Pixel + CAPI with the events in 5.1.
- [ ] Confirm mobile-web signup + calendar connect works end to end.
- [ ] Record 3 UGC videos (one in Hinglish) and 1 founder video.
- [ ] Connect Hyper MCP + Apify, then run section 9 and update this plan.
- [ ] Update the Product Hunt copy: it currently says "CRM updates", which the site doesn't support yet.

## Sources

- Lynkk site: [lynkk.ai](https://lynkk.ai/), [pricing](https://lynkk.ai/pricing), [privacy](https://lynkk.ai/privacy)
- Listings: [GetApp](https://www.getapp.com/all-software/a/lynkk/), [Slashdot](https://slashdot.org/software/p/Lynkk/)
- Notetaker comparisons: [Rock](https://www.rock.so/blog/best-ai-meeting-assistants), [Meetily](https://meetily.ai/blog/best-meeting-notes-software-2026), [Alfred](https://get-alfred.ai/blog/best-ai-meeting-notetakers), [TechRepublic](https://www.techrepublic.com/article/news-best-ai-meeting-note-takers-2026/), [Zapier](https://zapier.com/blog/best-ai-meeting-assistant/)
- Sales tools / Gong alternatives: [Claap](https://www.claap.io/blog/gong-alternatives), [Docket](https://www.docket.io/resources/research/gong-alternatives), [AskElephant](https://www.askelephant.ai/blog/top-gong-alternatives-for-revenue-teams), [Shadow](https://www.shadow.do/blog/best-gong-alternatives-2026)
- India / Hinglish: [MeetNotes](https://getmeetnotes.com/ai-meeting-notes-india/), [MeetMinutes](https://www.meetminutes.in/gad/your-ai-note-taker-wcc), [JotMe](https://www.jotme.io/tool/ai-meeting-notes/hindi), [Noter AI](https://www.noterai.net/best/hindi-meeting-transcription-app)
- Meta targeting 2026: [Conversios](https://www.conversios.io/blog/meta-advantage-audience-vs-detailed-targeting-2026-guide/), [Hawky](https://hawky.ai/blog/meta-ads-updates-2026), [Common Thread Co.](https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026), [LeadSync](https://leadsync.me/blog/facebook-ads-targeting-guide/), [Adligator](https://adligator.com/blog/meta-broad-targeting-advantage-plus-audiences-2026), [Karb](https://karb.ai/blog/meta-ads-targeting-2026)
- Cost benchmarks: [AdManage](https://admanage.ai/blog/how-much-does-it-cost-to-advertise-on-facebook), [Lebesgue](https://lebesgue.io/facebook-ads/facebook-cpm-by-country), [Upgrowth](https://upgrowth.in/meta-ads-price-benchmarks/), [Adamigo](https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026)

Competitor prices come from third-party, often vendor-written, comparisons that disagree with
each other. Check each vendor's pricing page before putting a number in an ad.
