# Lynkk.ai: Volume and Traffic Estimates Per Topic

Prepared 2026-11-03. Numbers for every topic in `lynkk-blog-titles.md`, scoped to the USA.

**Method.** Volume is the sum of the US monthly Ubersuggest volumes for every keyword variant in the
cluster (locId 2840). Traffic is modelled with Ubersuggest's own click estimator, which returns these
effective CTRs for an ads-present SERP: **position 3 = 7.9%, position 5 = 4.3%, position 8 = 1.9%.**
Value is modelled clicks at position 5 multiplied by the cluster's blended CPC, which is the Google
Ads spend the traffic replaces.

**Why I model position 5 and 8 rather than position 1.** lynkk.ai is DA 1 with zero follow backlinks.
Position 1 to 2 against DA 50+ incumbents is not a realistic near-term outcome, so quoting it would
inflate every row. Position 5 to 8 inside a verified low-authority SERP is achievable. Treat
position 3 as the ceiling, not the plan.

---

## Set A: Google search topics

| ID | Topic | US vol | SD | CPC | Clicks @3 | Clicks @5 | Clicks @8 | Value @5 | US winnable? |
|---|---|---|---|---|---|---|---|---|---|
| A13 | AI note taker device vs app | **2,110** | 34 | $6.59 | 166 | 90 | 41 | $594 | **No** |
| A3 | Microsoft Teams meeting transcript | **1,690** | 38 | $5.30 | 133 | 72 | 33 | $382 | **No** |
| A1 | AI note taker for in-person meetings | **950** | 40 | $14.62 | 75 | 41 | 18 | $593 | **No** |
| A11 | Best AI note taker for lectures | 640 | 23 | $9.71 | 50 | 27 | 12 | $265 | Maybe |
| T3 | Does Zoom/Teams/Meet have a built-in note taker | 530 | 16 | $10.00 | 42 | 23 | 10 | $226 | **No** |
| A4 | HIPAA-compliant AI note takers for therapists | 420 | 31 | **$37.00** | 33 | 18 | 8 | **$664** | **Yes** |
| A2 | AI note takers that do not join your meeting | 370 | 30 | $21.61 | 29 | 16 | 7 | $341 | Later |
| A8 | Best AI note taker for phone and sales calls | 290 | 34 | $12.00 | 23 | 12 | 6 | $149 | Maybe |
| A9 | Meeting notes in Notion | 280 | 41 | $12.36 | 22 | 12 | 5 | $148 | Maybe |
| A6 | What an AI note taker costs per seat | 190 | 30 | $5.50 | 15 | 8 | 4 | $45 | Maybe |
| A5 | Copilot in Teams vs standalone notetaker | 180 | 30 | $6.33 | 14 | 8 | 3 | $49 | Maybe |
| A7 | Meeting transcripts without recording | 170 | 30 | $4.91 | 13 | 7 | 3 | $36 | Maybe |
| A12 | AI note takers for Webex, Slack, Discord | 140 | 24 | $8.14 | 11 | 6 | 3 | $49 | **Yes** |
| A10 | Open-source and on-device AI note takers | 60 | 26 | $4.96 | 5 | 3 | 1 | $13 | **Yes** |
| A4b | AI note takers for financial advisors | 30 | 30 | **$28.10** | 2 | 1 | 1 | $36 | **Yes** |
| A14 | SSO, SCIM and admin controls | **0** | n/a | n/a | n/a | n/a | n/a | n/a | AI only |
| A15 | Who can see your transcripts (data residency) | **0** | n/a | n/a | n/a | n/a | n/a | n/a | AI only |

**Totals.** 8,050 US monthly searches across the whole set. If every single topic reached position 5,
that is **344 clicks per month**. At position 8, **155 clicks per month**.

**The number that actually matters.** Filtering to the SERPs I verified as winnable at DA 1 to 35
(A4, A4b, A10, A12) leaves **650 monthly searches, about 28 clicks per month at position 5, worth
roughly $761 per month in equivalent ad spend.**

That is the honest near-term US organic ceiling from this content set. It is small in clicks and
respectable in value, because the winnable SERPs are the expensive ones. If someone presents the
8,050 figure as the opportunity, that is the volume of SERPs you mostly cannot rank in yet.

### Where the volume is versus where the winnability is

The three largest clusters are the three I have marked "No":

- **A13 devices, 2,110 searches.** Largest cluster on the map. US SERP is Plaud (DA 54), Otter
  (DA 66), Reddit (DA 92), Medium (DA 95), Google Play (DA 99). It was already flagged for
  cannibalizing `/blog/ai-voice-recorders`. Both reasons point the same way.
- **A3 Teams transcript, 1,690 searches.** Second largest. Microsoft's own docs (DA 98) and Google
  aggregations (DA 94) hold it. Still a good India and rest-of-world play where you already rank 11.9.
- **A1 in-person, 950 searches.** DA 54 to 99 throughout.

So 4,750 of the 8,050 searches, 59% of the total volume, sit in SERPs Lynkk cannot enter at DA 1.
That is the core problem with a volume-led US plan.

### A reality check from the live SERPs

Modelled CTRs are averages. Here is what the sites in your target SERPs actually earn, from
Ubersuggest's per-URL click data:

**`hipaa compliant ai note taker`** (260/mo): upheal.io at position 2 gets 117 clicks per month.
Position 6 (getfreed.ai) gets 11. Positions 8 to 11 get 3 to 4 each.

**`ai note taker for therapists`** (90/mo): getfreed.ai at position 2 gets 24. Position 5 gets 7.
Positions 7 to 10 get 2 each.

**Read that carefully.** Landing at position 8 in the therapist SERP is worth about 2 clicks a month.
Landing at position 2 is worth 24 to 117. In small vertical SERPs the entire prize concentrates in
the top three, so a page that only reaches position 8 here is close to worthless, while the same
position in A13's 2,110-search cluster would be worth 41. The vertical play is only worth running if
you commit to winning the top three, which the DA 7 to 35 competition makes plausible.

---

## Set B: AI visibility topics

These have **zero or near-zero Google search volume**, so volume and click models do not apply. Their
demand metric is GSC impressions over the last 3 months, which is real measured demand from Google's
AI surfaces, plus the position Lynkk already holds.

| ID | Topic | GSC impressions (3mo) | Queries | Best position |
|---|---|---|---|---|
| A15 | Who can see your transcripts: LLM providers, residency, retention | **172** | 3 | **3.6** |
| B4 | Source-linked answers across past meetings | **124** | 5 | **2.3** |
| B3 | Enterprise-grade vs individual: SSO, SCIM, audit logs | **115** | 9 | **1.0** |
| B8 | From summary to CRM | **111** | 2 | **3.0** |
| B6 | Online plus in-person coverage | 92 | 6 | 4.8 |
| A14 | Rolling out to 300 seats | 78 | 1 | 6.9 |
| B9 | Volume discounts and rollout pricing | 66 | 5 | 4.0 |
| B7 | OpenAI note-taker alternatives | 31 | 2 | **1.0** |
| B10 | All-hands and retrospectives | 30 | 3 | **1.0** |
| B5 | MCP-compatible assistants | 6 | 1 | 2.5 |
| B1 | Indian startups, INR pricing | n/a | n/a | India only, drop for US |
| B2 | Hindi and Hinglish support | n/a | n/a | India only, drop for US |

**Total measured demand across Set B: 825 impressions in 3 months, at an average best position of
about 3.** That is roughly 275 impressions per month at page-one positions, on a domain with zero
follow links.

### How Set B compares to Set A on a US basis

| | Set A (US-winnable only) | Set B |
|---|---|---|
| Monthly demand | 650 searches | about 275 impressions |
| Current position | not ranking (3 US keywords total, all below 39) | **about 3** |
| Authority needed | DA 20 to 35 | **demonstrably none, you rank there now at DA 1** |
| Clicks today | 0 | 0 |

Set B's impressions are smaller than Set A's search volume, and that comparison understates Set B in
two ways.

First, **Lynkk already ranks at position 1 to 4 on Set B queries and does not rank at all on Set A
queries.** Set A requires link building that has not started. Set B requires content against
rankings you already hold.

Second, **the queries are qualitatively different.** Set B's language is "300 reps", "SSO and SCIM
with Okta or Entra", "which subprocessors see our transcripts", "volume discounts as we roll out
company-wide". That is a procurement conversation at an enterprise account. Set A's largest winnable
cluster is lecture notes for students. One B8 or A14 reader converting is worth more than the entire
A11 cluster at position 3.

The caveat I will not hide: **Set B currently produces zero clicks**, same as Set A. Position 3 in an
AI-mode result does not reliably generate a click the way position 3 in classic search does, because
the answer is often synthesised above the link. So Set B's value is influence over what the engine
says about Lynkk, plus citation, rather than a clean click forecast. I cannot give you a click number
for Set B because the data does not support one.

---

## The single most useful number in this document

Across the whole top-1,000 query export, non-brand performance is **10,777 impressions, 9 clicks,
0.08% CTR**. Brand is **323 impressions, 53 clicks, 16.4% CTR**.

Any traffic model above assumes normal CTR at the modelled position. Lynkk is not currently achieving
normal CTR at any position. Until that is fixed, **every projection in this document should be
discounted**, because a page at position 5 earning 0.1% instead of 4.3% delivers one click, not
eleven.

That is why the retitle work in `lynkk-low-hanging-fruit.md` sits ahead of all new content, and why
the US-filtered GSC export is still the first thing to pull: it tells you whether the CTR problem is
US-specific or global, and the fix differs.

---

## Summary, in plain terms

- **Total US volume across all 15 Set A topics: 8,050 searches per month.**
- **59% of that volume (4,750 searches) is in SERPs Lynkk cannot enter at DA 1.**
- **Realistic near-term US organic ceiling: about 28 clicks per month, worth roughly $761 per month
  in equivalent ad spend**, from the four verified winnable clusters.
- **Set B has no meaningful Google volume but 825 measured impressions in 3 months at an average
  position of 3**, which is the only place Lynkk currently competes in the US.
- **Neither set produces clicks today**, because non-brand CTR is 0.08%.

The practical conclusion has not changed from the US strategy document. Volume is not Lynkk's
constraint, authority is. Chasing the 2,110-search and 1,690-search clusters will produce
impressions and no clicks, exactly as the last four weeks already demonstrate. The compliance
vertical is small but winnable and expensive, the AI surfaces are where you already rank, and links
are what unlocks everything else.
