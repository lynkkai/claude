# Lynkk.ai: Targeting the USA

Prepared 2026-11-03. Revises the priorities in `lynkk-content-plan-2026-11.md`,
`lynkk-low-hanging-fruit.md` and `lynkk-blog-titles.md` for a US-first target.

Sources: GSC export (last 3 months), Ubersuggest domain overview and live US SERP analysis
(locId 2840) on six priority keywords.

---

## Read this first: one thing I cannot tell you from this export

The GSC zip has `Queries.csv` and `Countries.csv` as **separate** files with no cross-tab. So I can
see which queries rank well, and I can see that the US averages position 30.2, but I cannot see
**which queries rank well in the US specifically.**

That matters, because the inference runs the wrong way for us:

| Market | Clicks | Impressions | CTR | Avg position |
|---|---|---|---|---|
| India | 65 | 2,192 | 2.97% | **13.18** |
| United States | 11 | 13,966 | 0.08% | **30.21** |
| Canada | 8 | 921 | 0.87% | 13.07 |
| United Kingdom | 4 | 1,636 | 0.24% | 21.87 |

**The 270 top-10, zero-click queries I found in the low hanging fruit document are almost certainly
not US rankings.** The US average is position 30. Those page-one positions are being produced
largely by India, Canada, Australia, Singapore and the smaller markets, many of which average
positions 6 to 13. I built that analysis before you said the US was the target, and for a US goal
its conclusions need to be treated as unverified.

**To fix this properly, pull one more export:** Search Console, Performance, filter
Country = United States, then export Queries. That gives the real US striking-distance list and I
can redo the Tier 1 and Tier 2 work against it in a single pass. Everything below is what I can
establish without it, which is most of the strategy but not the page-level click targets.

---

## The constraint that decides the whole US plan

Ubersuggest domain overview for lynkk.ai:

| Metric | Value |
|---|---|
| Domain authority | **1** |
| Backlinks | 9 |
| Follow backlinks | **0** |
| Referring domains | 5 |
| Ranking organic keywords (US) | **3** |

Nine backlinks, every one of them nofollow. Zero follow links. Three ranking keywords in the US,
all deeper than position 39.

Second piece of context, from `Chart.csv`: US impressions did not exist until recently. Daily
impressions ran at 10 to 40 through August and September, then jumped from 49 on 6 October to 1,058
by 13 October and about 2,000 by late October. **The site is roughly four weeks into being indexed
at scale.** Positions in the high teens to thirties on brand-new pages are normal, not broken.

So the honest read: Lynkk is a four-week-old domain with no link equity trying to enter the most
competitive English-language SERP set in the category. That does not make the US unreachable. It
does mean the US plan cannot be the same plan as the global one, and the sequencing has to change.

---

## What the US SERPs actually look like

I ran live US SERP analysis on six priority keywords. The domain authority of the ranking pages is
the whole story.

### Not winnable at DA 1, do not start here

**`ai note taker for in person meetings`** (480/mo, SD 40). This was my number one recommendation in
the original plan. In the US the top 10 is: zoom.com (DA 87), medium (DA 95), reddit (DA 92),
plaud.ai (DA 54), otter.ai (DA 66), read.ai (DA 48), notta.ai (DA 51), play.google.com (DA 99). The
only sub-30 site is simular.ai at DA 26, position 7. **Correction to my earlier advice: this is a
strong global play and a poor US starting point.**

**`teams meeting transcript`** (390/mo, SD 38). This was my number two recommendation. The US SERP is
Microsoft's own documentation and university IT pages: google.com aggregations (DA 94) in five
positions, learn.microsoft.com (DA 98), systems-training.its.uq.edu.au (DA 87), youtube (DA 100),
uctoday (DA 57). **Correction: Microsoft owns this SERP, and the intent is "show me Microsoft's
docs", not "sell me a tool". Drop it from the US plan entirely.** It stays valid for India and the
rest of the world, where you already rank 11.9.

**`does zoom have an ai note taker`** (140/mo, SD 16). The SD score of 16 is misleading. Google's own
aggregated results hold positions 2, 5, 7, 8, 9, 11 and 14 at DA 94. The only small sites are
anarlog.so (DA 15) at position 12 and meetjamie.ai (DA 38) at 15. Low difficulty score, almost no
room.

### Winnable at DA 1, and this is the surprise

**`ai note taker for therapists`** (90/mo, SD 35, **CPC $50.63**). The US top 10:

| Position | Domain | DA |
|---|---|---|
| 2 | getfreed.ai | **35** |
| 4 | reddit.com | 92 |
| 5 | simplepractice.com | 51 |
| 7 | upheal.io | **23** |
| 8 | mentalyc.com | **42** |
| 9 | autonotes.ai | **21** |
| 10 | therapro.ai | **7** |

**A DA 7 domain ranks on page one.** Four of the seven organic results are under DA 43.

**`hipaa compliant ai note taker`** (260/mo, SD 31, **CPC $31.04**). Same pattern: upheal.io (DA 23)
at position 2, getfreed.ai (DA 35) at 6, trytwofold.com (**DA 27**) at 9, jotme.io (**DA 27**) at 11,
heyberries.com (**DA 18**) at 14. Fireflies' own HIPAA page sits at 8 with DA 54.

**`ai note taker that doesn't join meetings`** (90/mo, SD 30). Middle case: tactiq.io (DA 42) at 7,
towardsai (DA 49) at 3, tldv.io (DA 44) at 9, happyscribe (DA 59) at 14, meetjamie (DA 38). No
sub-30 domains, so this is reachable but not immediately. Park it until links exist.

### The pattern

US horizontal terms ("best AI note taker", "AI note taker for X platform") are held by DA 50 to 100
incumbents and by Google and Microsoft themselves. **US vertical and compliance terms are held by
DA 7 to 42 specialists.** At DA 1 with zero follow links, the vertical and compliance SERPs are the
only ones where content quality alone can place you. They also carry the highest CPCs on the entire
keyword map, which is not a coincidence.

---

## The US plan: three plays, in order

### Play 1: A healthcare and compliance beachhead (the only near-term organic win)

This is the single US recommendation I hold with confidence, because I verified the SERP.

| Keyword | Vol | SD | CPC |
|---|---|---|---|
| hipaa compliant ai note taker | 260 | 31 | $31.04 |
| ai note taker for therapists | 90 | 35 | $50.63 |
| hipaa compliant ai note taker for therapists | 40 | 40 | $56.87 |
| therapy ai note taker | 30 | 52 | $40.10 |
| simple practice ai note taker | 390 | 15 | $5.46 |
| ai note taker for financial advisors | 30 | 30 | $28.10 |

Roughly 840/mo at a blended CPC above $30, in SERPs where DA 7 to 35 sites rank page one.

The honest caveat: this requires Lynkk to actually be defensible on HIPAA. Region-pinned processing
is in the product, but a BAA, retention controls and a named subprocessor list are what this audience
checks, and `/security` currently draws 22 impressions. **If Lynkk cannot sign a BAA, do not run this
play.** Writing compliance content you cannot back is worse than not ranking. Confirm that with the
team before commissioning anything here.

Secondary vertical note: `ai note taker for lawyers` and `ai note taker for real estate agents` both
return **zero** Google volume, despite your having `/use-cases/lawyers` and
`/use-cases/real-estate-agents`. Those are AI-prompt plays, not SEO plays. Do not write blog posts
targeting them for US search.

### Play 2: Links, because nothing else unlocks without them

Zero follow backlinks is the ceiling on every other US ambition. No amount of content fixes a
0-follow-link profile against DA 50+ incumbents. From the citation-gap data in the main plan, the
targets are already identified and most are reachable:

| Target | DA | Why |
|---|---|---|
| notta.ai | 51 | cited in 33% of the AI answers you miss |
| help.fathom.video | 47 | cited, competitor-owned, low odds but high value |
| spotsaas.com | 41 | listicle, accepts submissions |
| dupple.com | 32 | two cited pages |
| cleverly.co | 30 | listicle |
| knowledgesense.in | 15 | easiest win, India listicle |
| comparecrest.com | 5 | easiest tier |
| aitoolwise.com, aitoolbriefing.com, aicentralresources.com, stratilyze.com | 1 to 10 | easiest tier |

Eleven of the fourteen cited pages are under DA 35. Also note that **Reddit ranks in the top 6 on
three of the six SERPs I checked**, and `discussions_and_forums` appears as a SERP feature on two of
them. For a DA 1 domain, earning a genuine Reddit mention in r/therapists, r/ProductivityApps or
r/ChatGPTPro is worth more US visibility than a blog post, and it is also what feeds the AI engines.

### Play 3: AI visibility, which is where the US is actually reachable now

This is the strategic point. Google weights domain authority heavily, which is why Lynkk sits at
position 30 in the US. **AI answer engines do not weight it the same way**, and your own GSC data
proves it: on long conversational queries, a DA 1 domain is ranking at positions 2.3 to 6.9.

- "zoom ai companion gives us summaries but nothing in our crm..." 102 impressions, **position 3.0**
- "which notetakers offer searchable meeting history with source-linked answers?" **position 3.3**
- "which third-party llm providers get to see prospect call transcripts...?" **position 3.6**
- "how do founders keep track of everything said in investor and team meetings?" **position 3.9**
- "rolling out an ai notetaker to 300 reps: which plans include sso, scim...?" **position 6.9**
- "which ai notetakers work with mcp-compatible assistants...?" **position 2.5**

A four-week-old domain with no links does not rank at position 3 in classic search. It can in AI
surfaces. These queries are also overwhelmingly enterprise-buyer language (SSO, SCIM, 300 reps,
subprocessors, audit trails) which skews US and heavily outweighs a lecture-notes visitor.

Meanwhile Ubersuggest shows Lynkk at **0% visibility and 0 mentions** in ChatGPT across 10 tracked
prompts. Google's AI surfaces already find you. ChatGPT does not, because it cites listicles you are
absent from. That is Play 2's job, which is why the two are coupled.

**For a US target, Set B in the title document stops being secondary and becomes the main channel.**
Reweight the India-specific items: B1 (Indian startups) and B2 (Hindi and Hinglish) should drop out
of a US-first calendar, and the five prompts in the main plan should be re-run at locId 2840 rather
than 2356.

---

## Revised title priority for a US target

Changes from `lynkk-blog-titles.md`, with reasons.

### Promoted

| Rank | Title | Why |
|---|---|---|
| 1 | HIPAA-Compliant AI Note Takers for Therapists: 6 Options Reviewed | verified DA 7 to 35 SERP, $31 to $57 CPC. The only verified near-term US organic win |
| 2 | From Summary to CRM: AI Notetakers That Actually Update Your Pipeline | your highest-impression prompt query, 102 impressions at position 3.0 |
| 3 | Who Can See Your Meeting Transcripts? Subprocessors, LLM Providers and Data Residency | position 3.6, US enterprise buyers, no competitor publishes this |
| 4 | Rolling Out an AI Notetaker to 300 Seats: SSO, SCIM and Admin Controls Explained | position 6.9, unambiguously US enterprise language |
| 5 | AI Notetakers That Work With MCP: Query Your Past Calls From Claude or ChatGPT | position 2.5, near-zero competition, first-mover |
| 6 | Which AI Notetakers Give Source-Linked Answers Across All Your Past Meetings? | position 3.3 |
| 7 | Enterprise-Grade vs Individual AI Notetakers: SSO, SCIM and Audit Logs Compared | position 2.6 and position 1 on a variant |
| 8 | AI Note Takers for Financial Advisors: What Compliance Teams Require | $28.10 CPC, vertical pattern, thin volume (30/mo) but same winnable profile |

### Demoted or dropped for the US

| Title | Was | Now | Reason |
|---|---|---|---|
| AI Note Taker for In-Person Meetings | A1, rank 1 | keep for global, not US priority | US SERP is DA 54 to 99 |
| Where to Find Your Microsoft Teams Meeting Transcript | A3, rank 2 | **drop from US plan** | Microsoft and university IT own it at DA 87 to 98; wrong intent |
| Does Zoom, Teams or Google Meet Have a Built-In AI Note Taker? | Tier 3, rank 3 | demote | SD 16 is misleading; Google holds 7 of 14 positions at DA 94 |
| Best AI Meeting Notetakers for Indian Startups (INR Pricing) | B1 | **drop from US plan** | India-specific |
| AI Notetakers With Hindi and Hinglish Support | B2 | **drop from US plan** | India-specific |
| Best AI Note Taker for Lectures | A11 | drop | not US ICP, and it was already flagged as a traffic-only play |
| AI Note Takers That Don't Join Your Meeting | A2, rank 4 | park until links exist | DA 42 to 59 SERP, no sub-30 domains. Reachable later, not now |

### Unchanged

A4 HIPAA (now rank 1), A6 cost per seat, A14 SSO, A15 data residency, A5 Copilot, B3, B4, B5, B7,
B8, B9, B10. The retitles in the low hanging fruit document are still worth doing, but **treat their
click projections as unverified for the US** until the US-filtered export confirms which of those
pages rank in the US at all.

---

## What I would do in the next 30 days

1. **Pull the US-filtered GSC query export.** One click, and it converts the entire low hanging fruit
   analysis from inference to fact. Nothing else should be prioritised ahead of this.
2. **Confirm whether Lynkk can sign a BAA and state its subprocessors.** This gates Play 1, the only
   verified US organic opening. If the answer is no, Play 1 is off and the US plan becomes Plays 2
   and 3 alone.
3. **Start link acquisition on the eleven sub-DA-35 cited pages.** Zero follow links is the real
   ceiling, and this is slow work, so it should start before the content, not after.
4. **Re-run the brand prompts at US location (2840, not 2356)** and track Lynkk as a brand, which is
   currently off. Without this there is no US AI-visibility baseline to measure against.
5. **Publish titles 1 through 5 above**, in that order.

One expectation to set plainly: with DA 1 and zero follow links, meaningful US organic traffic is a
two-to-three-quarter project, and the vertical and compliance niches are the only place it starts
earlier. The fastest genuine US visibility available to Lynkk right now is AI answer engines, where
your data shows you already compete at position 3 despite the authority gap. I would weight the US
plan accordingly rather than fighting DA 87 domains for head terms.
