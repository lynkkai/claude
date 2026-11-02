# Lynkk: 12-Topic Plan for Medium, Hashnode and Substack

**Prepared:** 2026-11-02
**Scope:** 12 topics total, 4 per platform (Medium, Hashnode, Substack), each mapped to a keyword
cluster, a search intent, a content format, and an internal link back into the lynkk.ai blog.
**Data source:** Ubersuggest (US, locId 2840), pulled 2026-11-02 on the lynkk.ai account.
All volume / SD (SEO difficulty) / CPC figures below are from that pull.

---

## 0. Two things to settle before we write

1. **"444" read as 4 + 4 + 4 = 12 topics**, four per platform. If you meant 4 articles of 444 words
   each, or 12 per platform, say so and I will re-cut the plan. Everything below assumes 4 per platform.

2. **Google Search Console is not connected to this session.** There is no GSC connector available
   here, so nothing in this document comes from lynkk.ai's own query data. To layer that in, either
   connect Search Console as a connector, or export **Performance > Queries** and **Pages**
   (last 6 months, CSV) and drop the files in this repo. Once I have it I can do the parts keyword
   tools cannot: find queries where lynkk.ai already shows impressions but ranks 8 to 30
   (the fastest wins), and make sure these 12 posts do not cannibalise pages that already rank.

---

## 1. What the demand actually looks like

### 1.1 Intent split in the "AI meeting" market

Ubersuggest returns an intent code per keyword: 1 = informational, 2 = navigational,
3 = commercial, 4 = transactional. Reading the full suggestion set for "ai meeting notes",
"ai note taker" and "meeting assistant" (426 keywords), the pattern is clear:

| Intent | Share of the cluster | What the query looks like | What it wants to read |
|---|---|---|---|
| Transactional (4) | Largest share | "ai note taker for zoom", "free ai note taker app", "ai note taker for in person meetings" | A tool that does exactly this, pricing, a free tier |
| Navigational (2) | Heavy | "otter ai note taker", "fathom ai note taker", "granola ai meeting notes", "jamie ai note taker" | A named competitor, by brand |
| Commercial (3) | Strong | "best ai note taker", "best ai note taker for meetings", "what is the best ai note taker" | A ranked list with real testing |
| Informational (1) | Steady | "what is ai note taker", "how to add ai note taker to teams", "meeting minutes vs notes" | An explainer or a how-to |

**The strategic read:** the head terms are owned by brand queries. A new brand does not win
"ai note taker" (27,100/mo, SD 48). It wins on the **qualifier**: the platform (Zoom, Teams,
Meet), the constraint (bot-free, in-person, offline, HIPAA, data region), the job (CRM, Jira,
sales calls), and the comparison (X vs Y, alternatives to X). Every one of the 12 topics below
sits on a qualifier, not a head term.

### 1.2 Good-intent queries worth owning (high CPC = real buyers)

CPC is the honest signal of buyer intent here. These are the ones advertisers pay most for,
which means they convert:

| Keyword | Volume/mo | SD | CPC | Intent |
|---|---|---|---|---|
| ai note taker for therapists | 90 | 35 | $50.63 | Transactional |
| hipaa compliant ai note taker for therapists | 40 | 40 | $56.87 | Commercial |
| hipaa compliant ai note taker | 260 | 31 | $31.04 | Navigational / informational |
| best ai note taker for zoom | 40 | 12 | $31.27 | Commercial |
| ai note taker for google meet | 210 | 39 | $29.73 | Transactional |
| best ai note taker for microsoft teams | 50 | 21 | $29.32 | Commercial |
| free ai note taker for google meet | 50 | 38 | $25.55 | Transactional |
| meeting ai note taker | 260 | 45 | $22.44 | Mixed |
| in person meeting ai note taker | 90 | 44 | $22.39 | Transactional |
| google meet ai note taker | 590 | 40 | $21.91 | Mixed |
| ai note taker that doesn't join meetings | 90 | 30 | $21.61 | Transactional |
| ai note taker for meetings | 390 | 38 | $21.56 | Transactional |
| ai note taker for zoom | 480 | 33 | $20.41 | Transactional |

### 1.3 Low-competition openings that match Lynkk's actual differentiators

These are the gaps. Low SD, real volume, and Lynkk is genuinely built for them:

| Keyword | Volume/mo | SD | CPC | Why it fits Lynkk |
|---|---|---|---|---|
| ai note taker for in person meetings | 480 | 40 | $14.62 | Records in-person conversations, not just calls |
| ai note taker that doesn't join meetings | 90 | 30 | $21.61 | No bot in the room |
| bot free ai note taker | 110 | 59 | $8.54 | Same angle, different phrasing |
| bot free ai meeting assistant | 40 | 64 | $16.20 | Same angle |
| free ai note taker for in person meetings | 50 | 38 | $17.25 | Freemium "Start free" |
| in person ai note taker | 50 | 52 | $14.75 | Same angle |
| live ai meeting assistant | 170 | 51 | $19.42 | Speaks live in the meeting |
| real time ai meeting assistant | 110 | 59 | $19.07 | Same, the clearest Lynkk-only claim |
| live ai note taker | 30 | 24 | $20.46 | Same |
| open source ai note taker | 40 | 26 | $4.96 | Adjacent, dev audience, Hashnode |
| ai note taker no subscription | 40 | 47 | $7.93 | Price-sensitive, freemium entry |

### 1.4 The developer-side demand (this is where Hashnode wins)

Hashnode's audience is engineers, and the volume on that side is an order of magnitude larger
than the note-taker market:

| Keyword | Volume/mo | SD | CPC | Intent |
|---|---|---|---|---|
| mcp server | 60,500 | **23** | $15.69 | Navigational |
| model context protocol | 14,800 | 75 | $17.52 | Informational |
| how to build an ai agent | 2,900 | 51 | $19.78 | Informational |
| whisper transcription | 2,400 | 65 | $5.97 | Informational |
| ai agents for business | 1,000 | 36 | $39.35 | Commercial |
| speaker diarization | 880 | 54 | $23.86 | Informational |
| voice ai agent | 880 | 47 | $28.34 | Informational |
| knowledge graph rag | 390 | 51 | $12.56 | Informational |

"mcp server" at 60,500/mo with SD 23 is the single largest low-difficulty opening in this whole
research set, and Lynkk's "connect anything via MCP" is a real, credible claim against it.

### 1.5 The adjacent "meeting minutes" market (big, mostly template-seeking)

"meeting minutes" is 9,900/mo and the cluster runs to 311 keywords, but read it carefully:
the volume is dominated by **template and format** queries (form for meeting minutes 22,200;
meeting minutes sample 5,400; example meeting minutes 4,400) and by **Fed / FOMC minutes**,
which are irrelevant noise. The useful slice is the AI-adjacent tail:

| Keyword | Volume/mo | SD | CPC |
|---|---|---|---|
| ai meeting minutes | 1,600 | 49 | $10.62 |
| software for meeting minutes | 1,600 | 47 | $31.09 |
| meeting minutes app | 880 | 36 | $12.17 |
| free app to record and transcribe meeting minutes | 320 | 40 | $7.11 |
| ai meeting minutes generator | 140 | 30 | $11.07 |
| ai for meeting minutes | 140 | 33 | $16.74 |
| ai tools for meeting minutes | 70 | 41 | $19.67 |

Treat this as a **secondary** cluster: it brings volume but a weaker buyer. One Substack essay
points at it; the money topics stay on the note-taker and platform-qualifier side.

### 1.6 One data caveat, stated plainly

Ubersuggest reports "ai powered meeting assistant" at **40,500/mo with competition 0.01**, which
is larger than its own head term "ai note taker" (27,100) and larger than "ai meeting assistant"
(4,400). That is almost certainly a clustering artifact in their data, not real standalone demand.
I have **not** built a topic on it, and I would not put it in a report to anyone else without the
caveat. Verify against GSC or Keyword Planner before anyone quotes it.

### 1.7 What performs well on each platform

Keyword tools do not measure Medium, Hashnode or Substack engagement, and I am not going to
invent numbers for it. What the SERP data **does** show is which of these platforms Google
actually surfaces for this market, and that plus how each platform's own feed behaves gives a
reliable format rule. Flagging this section as editorial judgment, not measured data:

- **Medium** gets distribution from Google and from its own topic feeds on
  *comparison and "best of" content with a first-person testing angle*. Google rewards Medium for
  commercial-investigational queries ("best", "alternative", "vs") because the domain carries
  authority the query does not otherwise have good answers for. Format: numbered list, screenshots,
  an explicit "how I tested" section, a verdict table. Length 1,500 to 2,500 words.
- **Hashnode** gets distribution from the dev community feed, newsletters and Google long-tail on
  *implementation* content: code, architecture, a problem you actually hit. It does badly with
  marketing copy. Format: a stated problem, a diagram, real code, the failure modes, a repo link.
  Length 1,200 to 2,000 words. Canonical tags matter here: Hashnode lets you set a canonical URL,
  so cross-posting from the lynkk.ai blog is safe.
- **Substack** gets almost no Google distribution and all of its reach from subscription, email
  forwarding and Notes. It rewards *opinion with a thesis*: a claim someone could disagree with,
  argued from operator experience. Format: essay, no H2 soup, one strong idea, 900 to 1,500 words.
  Do not write SEO posts on Substack; write the POV that makes people quote Lynkk.

---

## 2. The 12 topics

### MEDIUM: commercial-intent, comparison-led

**M1. "The Best AI Note Takers for Meetings in 2026: 9 tools, tested on the same 5 calls"**
- Primary: best ai note taker (1,900 / SD 36). Secondary: best ai note taker for meetings (260,
  CPC $12.73), what is the best ai note taker (170), best ai note taker app (140), best ai note
  taker reddit (50), best meeting ai note taker (70).
- Intent: commercial. Reader is choosing, not learning.
- Angle: run the same five recordings (a Zoom call, a Teams call, an in-person 1:1, a multilingual
  call, a noisy room) through all nine tools and publish the diffs. Include the tools that beat
  Lynkk on something. The credibility is the product.
- Internal link: lynkk.ai/blog hub + the Lynkk comparison or pricing page.

**M2. "AI Note Takers That Don't Join Your Meeting: how bot-free capture works"**
- Primary: ai note taker that doesn't join meetings (90 / SD 30 / CPC $21.61). Secondary: bot free
  ai note taker (110), bot free ai meeting assistant (40, CPC $16.20), ai note taker no
  subscription (40).
- Intent: transactional, and the CPC says these people buy.
- Angle: why the "a bot joined the call" pattern breaks (client-facing calls, consent optics,
  platform lockouts, external attendees), and what device-side or offline-first capture does
  instead. This is a Lynkk-native argument.
- Internal link: the Lynkk capture / offline-first feature page.

**M3. "AI Note Taker for In-Person Meetings: what actually works when there is no Zoom link"**
- Primary: ai note taker for in person meetings (480 / SD 40 / CPC $14.62). Secondary: in person
  meeting ai note taker (90, CPC $22.39), in person ai note taker (50), free ai note taker for in
  person meetings (50, CPC $17.25), best ai note taker for conferences (30), wearable ai note
  taker (720).
- Intent: transactional.
- Angle: most of this market only exists on calls. Cover the in-person reality: mic distance,
  overlapping speakers, diarization without separate audio channels, interviews, site visits,
  consent in a room. Mention the hardware options (Plaud, wearables) honestly, then make the
  software case.
- Internal link: the in-person capture page + the multilingual page.

**M4. "Otter vs Fireflies vs Granola vs Lynkk: choosing a note taker by workflow, not feature list"**
- Primary: otter ai alternative (480 / SD 34). Secondary: granola vs otter (90, SD 17, spiked to
  320 in March), fireflies ai alternative (70, CPC $11.63, intent Commercial), notion ai meeting
  notes vs granola (30), notta / tactiq / meetgeek alternative tails.
- Intent: commercial, late-stage. These people are already shopping.
- Angle: four workflows (sales rep updating a CRM, PM filing Jira tickets, consultant billing
  against interviews, regulated team with a data-region requirement) and which tool wins each.
  Lynkk does not win all four in the piece. That is why it gets read.
- Internal link: the Lynkk integrations page (CRM, Jira, Calendly, Cal.com).

---

### HASHNODE: implementation-led, developer audience

**H1. "Wiring a meeting assistant into your stack with MCP: a working build"**
- Primary: mcp server (60,500 / **SD 23** / CPC $15.69). Secondary: model context protocol
  (14,800 / SD 75), plus "mcp server" long-tails.
- Intent: navigational / informational. The biggest low-difficulty opening in this entire dataset.
- Angle: real code. Expose meeting context (transcripts, action items, the knowledge graph) over
  MCP, then have an agent query it. Show the server, the tool definitions, the auth, the failure
  modes. Lynkk's "connect anything via MCP" earns the right to this post.
- Internal link: the Lynkk MCP / integrations docs page. Set the canonical to lynkk.ai if the post
  also lives on the Lynkk blog.

**H2. "Speaker diarization in production: who said what, and the five ways it breaks"**
- Primary: speaker diarization (880 / SD 54 / CPC $23.86). Secondary: whisper transcription
  (2,400 / SD 65), meeting transcription accuracy (near-zero volume but high topical relevance).
- Intent: informational, engineer evaluating an approach.
- Angle: single-mic in-person audio, crosstalk, speaker re-identification across sessions, accents
  and code-switching in multilingual calls, and what the error does downstream when you attribute
  an action item to the wrong person. Include benchmark numbers you can defend.
- Internal link: the Lynkk accuracy / multilingual page.

**H3. "Turning meetings into a knowledge graph: schema, extraction and retrieval"**
- Primary: knowledge graph rag (390 / SD 51 / CPC $12.56). Secondary: graph rag, entity resolution,
  "searchable meeting history" tails.
- Intent: informational.
- Angle: the actual modelling problem. Entities (people, accounts, projects, decisions, open
  items), edges across meetings, resolving "the pricing thing we discussed" to a node, and why
  flat transcript embeddings fail at "what is still open with this client". This is Lynkk's
  knowledge-graph claim, shown rather than asserted.
- Internal link: the Lynkk knowledge graph / search feature page.

**H4. "Building a voice agent that speaks inside a live meeting: latency, turn-taking, interrupts"**
- Primary: voice ai agent (880 / SD 47 / CPC $28.34). Secondary: how to build an ai agent
  (2,900 / SD 51 / CPC $19.78), real time ai meeting assistant (110, CPC $19.07), live ai meeting
  assistant (170, CPC $19.42).
- Intent: informational, high commercial adjacency (note the CPCs).
- Angle: the hard part is not transcription, it is knowing when to speak. Cover the latency budget,
  barge-in handling, VAD, and retrieval fast enough to answer a question mid-sentence. This is the
  single most defensible Lynkk capability and almost nobody writes about it well.
- Internal link: the Lynkk live assistant feature page.

---

### SUBSTACK: POV essays, built for forwarding not for Google

**S1. "The meeting is the database"**
- Thesis: notes are the wrong unit of work. The useful object is the state of a relationship across
  every conversation, which is why "summarise the call" tools plateau. Argues the full-lifecycle
  position (before, during, after) without reading like a product page.
- Keyword relevance (secondary only): ai meeting minutes (1,600), meeting minutes vs notes (110).
- Internal link: the Lynkk blog pillar post on the meeting lifecycle.

**S2. "Nobody reads the recap"**
- Thesis: AI note takers solved capture and did nothing about follow-through, so we traded unread
  notes for unread summaries. The work after the work is the actual product.
- Keyword relevance: too many meetings (140 / SD 26), meeting fatigue (110 / SD 46), action items
  for meeting minutes (90).
- Internal link: the Lynkk action items / Jira + CRM automation page.

**S3. "Where does your meeting audio go?"**
- Thesis: consent and data residency are the questions buyers in regulated markets ask first and
  that the category answers worst. Covers two-party consent, retention, sub-processors, model
  training on your calls, and what "pick a region" has to actually mean to count.
- Keyword relevance: hipaa compliant ai note taker (260 / CPC $31.04), hipaa compliant ai note
  taker for therapists (40 / CPC $56.87), ai note taker for therapists (90 / CPC $50.63), is it
  legal to record a meeting (20). The volume is small, the CPC is the highest in the entire
  dataset, which tells you exactly how valuable these readers are.
- Internal link: the Lynkk data residency / security page. **Blocker:** this one needs the
  compliance facts from the "To confirm" list in memory/lynkk-brand.md (available regions, SOC 2 /
  GDPR status, retention policy, whether customer audio trains models). I will not write
  compliance claims from inference. Get me those and this becomes the highest-value piece here.

**S4. "From note taker to teammate: what changes when the AI speaks"**
- Thesis: the category's next step is not better summaries, it is an agent that acts during the
  meeting, and that changes meeting etiquette, trust and who owns the decision record.
- Keyword relevance: ai agents for business (1,000 / SD 36 / CPC $39.35), live ai meeting assistant
  (170), ai meeting assistant (4,400).
- Internal link: the Lynkk live assistant page + the MCP integrations page.

---

## 3. Internal linking plan (lynkk.ai blog <-> external posts)

Each external post carries **two** links into lynkk.ai and no more, so it reads as editorial:

| Post | Link 1 (deep, exact-match anchor) | Link 2 (contextual) |
|---|---|---|
| M1 | /blog pillar: "AI meeting notes" | Pricing / Start free |
| M2 | Bot-free capture feature | /blog "how Lynkk records" |
| M3 | In-person capture feature | Multilingual feature |
| M4 | Integrations (CRM, Jira) | Comparison page |
| H1 | MCP / integrations docs | Knowledge graph feature |
| H2 | Accuracy / multilingual | /blog pillar |
| H3 | Knowledge graph feature | Search feature |
| H4 | Live assistant feature | MCP docs |
| S1 | /blog lifecycle pillar | Homepage |
| S2 | Action items + Jira/CRM automation | /blog lifecycle pillar |
| S3 | Data residency / security | Homepage |
| S4 | Live assistant feature | MCP docs |

**Reciprocal side, on the lynkk.ai blog:** build one pillar post, "AI meeting notes: the complete
guide", and link out from it to M1, M4, H1 and S1 as further reading. That gives the pillar the
topical breadth signal and sends the external posts the engagement signal, in both directions.

**Anchor text rules:** vary it. Use the exact keyword on at most one link per post
("ai note taker for in person meetings"), and partial or branded anchors everywhere else
("how Lynkk handles in-person capture", "Lynkk's MCP integration"). All-exact-match anchors
across 12 posts is a footprint.

**Canonicals:** Hashnode and Medium both support canonical URLs. If a post also lives on the
lynkk.ai blog, publish on lynkk.ai first, then cross-post with the canonical pointing home, so
lynkk.ai keeps the ranking. For the four Medium posts, which are written to rank **on Medium's**
authority for commercial queries lynkk.ai cannot yet win, publish Medium-first with no canonical
and keep them off the Lynkk blog. That is a deliberate split.

---

## 4. Suggested publishing order

Ordered by (opening size x how credibly Lynkk can claim it):

1. **H1** MCP build (60,500/mo at SD 23, the largest opening)
2. **M3** In-person note taker (480/mo, SD 40, core differentiator)
3. **M2** Bot-free capture (CPC $21.61, low SD, Lynkk-native)
4. **H4** Live voice agent (the most defensible claim in the product)
5. **M1** Best-of 2026 (needs real testing time, so start it early, ship fourth or fifth)
6. **S1** The meeting is the database (POV anchor the others can cite)
7. **H3** Knowledge graph
8. **M4** Otter vs Fireflies vs Granola vs Lynkk
9. **S2** Nobody reads the recap
10. **H2** Speaker diarization
11. **S4** From note taker to teammate
12. **S3** Where does your meeting audio go (gated on the compliance facts)

---

## 5. What I need from you to start writing

1. **GSC data**: connect the connector, or export Queries + Pages CSV (6 months) into this repo.
   Without it I am optimising blind to what lynkk.ai already ranks for.
2. **The lynkk.ai blog URL list** (existing posts and slugs), so the internal links above point at
   real pages instead of placeholders, and so we do not cannibalise.
3. **The compliance facts** for S3: data regions, SOC 2 / GDPR status, retention, whether customer
   audio is used for training.
4. **Product access or recordings** for M1 and M4: the testing is what makes those two work, and
   I will not fabricate test results.
5. **Confirm the "444" reading**: 4 per platform, 12 total.

Say which topic to start with and I will write it.
