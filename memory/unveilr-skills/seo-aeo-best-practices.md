---
name: seo-aeo-best-practices
description: "Evidence-graded knowledge base of SEO, AEO and GEO best practices, plus the workflows for growing and maintaining it. Three modes. (1) INTAKE \u2014 paste a Slack thread, LinkedIn post, newsletter, or URL; it atomizes the source into individual falsifiable claims, dedupes against what's on file, traces each to a primary source, and rules accept/provisional/quarantine/reject. Every claim is graded T1 (official docs) to T4 (LinkedIn). (2) CONSULT \u2014 ask whether a tactic works or a claim is true; answers come with the evidence tier attached, checked against a 30+ row rejected-myths table first. (3) AUDIT \u2014 on request, re-verify entries against primary sources to catch silent deprecations and stale statistics; runs in both directions, since rejected claims can revive. Deliberately biased toward rejection: precision over size. Notable current findings \u2014 the KDD 2024 GEO paper failed replication at NeurIPS 2025, \"noindex privacy/T&C pages\" is contradicted by Google on record, FAQ rich results died 2026-05-07, llms.txt is inert, and the 155-160 / 60 character meta limits do not exist."
---

<!-- Pulled from the Unveilr platform registry (scope=global, version=1) on 27 Aug 2026. -->

---
name: seo-aeo-best-practices
description: Curated, evidence-graded knowledge base of SEO, AEO (Answer Engine Optimization), and GEO (Generative Engine Optimization) best practices — plus the workflows for growing and maintaining it. Use in three situations. (1) INTAKE — the user pastes a Slack conversation, a LinkedIn post, a newsletter, a conference takeaway, a screenshot of a thread, or a URL, and wants the SEO/AEO/GEO practices extracted, fact-checked against primary sources, deduped against what's already here, and added. Triggers: "add this to the SEO skill", "is this worth adding", "read this URL and pull out the AEO practices", "someone posted this on LinkedIn", "from our Slack thread", "fact-check this SEO claim". (2) CONSULT — the user asks what the current best practice is, whether a tactic actually works, whether a claim is true, how to structure content for ChatGPT/Perplexity/AI Overviews/Gemini, or wants a claim graded for evidence quality. Triggers: "does X actually work for AEO", "what's the best practice for", "is llms.txt worth it", "should we add FAQ schema", "how do we get cited by ChatGPT", "is this an SEO myth". (3) AUDIT — re-verify the knowledge base against primary sources to catch silent deprecations, stale statistics, failed replications, and practices that are no longer good practice. Triggers: "audit the SEO skill", "check if anything changed", "is this still true", "refresh the best practices", "has Google changed anything", any scheduled/recurring maintenance run, or CONSULT hitting an entry past its re-verify window.
---

# SEO / AEO / GEO Best Practices

A curated knowledge base with an evidence bar. Everything here is graded by how well it is
actually supported. The point of this skill is **not** to collect tips — it is to keep
unsupported tips **out**, because the SEO/AEO information environment is heavily polluted.

Three modes: **INTAKE** (add new practices), **CONSULT** (answer using what's here), and
**AUDIT** (re-verify what's here against primary sources, because it rots).

---

## Why the bar is high

Verified during the July 2026 build of this skill, and it should shape your instincts:

- The foundational GEO paper (KDD 2024) **substantially failed independent replication** at
  NeurIPS 2025. Most published GEO tactics were ineffective or *negative*.
- Google now publishes an **explicit list of debunked AI-optimization tactics** that names
  most of what the AEO industry sells.
- Multiple widely-cited "studies" are vendor marketing with **no sample size, no methodology,
  and incoherent statistics** (one reports a brand appearing in "176.89% of queries").
- There is a **self-reinforcing AI-slop layer** of SEO blogs that manufactures specific,
  confident, false technical claims — fake dates, fake threshold changes — and cross-cites
  itself into apparent consensus.
- **LinkedIn is the single worst source in this space.** AEO content there is dominated by
  people selling AEO. Treat every LinkedIn claim as T4 until proven otherwise.

So: assume an incoming claim is wrong until evidence says otherwise. Rejecting a plausible
claim costs almost nothing. Accepting a false one poisons every downstream article,
audit, and client recommendation that reads this file.

---

## Evidence tiers

| Tier | Meaning | Examples |
|---|---|---|
| **T1** | Official platform documentation or on-record statement | developers.google.com, web.dev, OpenAI/Anthropic/Perplexity docs, Google Search Central blog, sworn testimony |
| **T2** | Peer-reviewed, or large-scale independent study with published methodology | NeurIPS/KDD papers, arXiv with real methods sections, court records, Pew |
| **T3** | Vendor/practitioner study with published methodology and sample size | Ahrefs DiD studies, Semrush index studies — usable, but check for range restriction and vendor incentive |
| **T4** | Anecdote, conference hearsay, unsourced vendor claim, LinkedIn post | Default tier for anything arriving via Slack/LinkedIn |

**Tier is about the evidence, not the source's fame.** A famous SEO's unsourced assertion is T4.
An obscure researcher's pre-registered study is T2.

**T1 caveat — interested testimony.** Google is authoritative on *mechanism* (which crawler
does what, which controls exist) and *interested* on *strategy* ("nothing has changed, keep
doing SEO" conveniently discourages optimizing for competitors). Weight T1 mechanism claims
heavily. Weight T1 strategy claims as strong-but-motivated, and prefer them when T2
independently corroborates — which, as of now, it largely does.

---

## MODE A — INTAKE

### Step 0. Identify the source and its channel

| Channel | How to ingest | Default suspicion |
|---|---|---|
| **URL** | `WebFetch` it. If it fails or returns a shell, say so and ask for pasted text — never guess at contents | Depends on publisher |
| **LinkedIn post** | LinkedIn blocks automated fetching. Ask the user to paste the text | **Very high** — assume marketing |
| **Slack conversation** | User pastes. Note who said it and whether they were asserting or speculating | Medium — colleagues speculate out loud |
| **Screenshot** | Read it directly | Depends on what it shows |
| **Newsletter / conference takeaway** | Paste or URL | High — conference talks have no transcript and become "confirmed" via a single LinkedIn recap |

Record the source URL/author/date. An entry with no traceable source cannot be accepted above T4.

### Step 1. Atomize into individual claims

Do not evaluate a post as a unit. A LinkedIn post usually contains 5–10 claims of wildly
different quality, and accepting or rejecting wholesale is how bad claims sneak in on the back
of good ones.

Split into atomic, falsifiable claims. Rewrite each as a testable proposition:

> "Structured data helps AI find you" → **"Adding schema.org JSON-LD to a page increases
> its citation rate in AI answer engines."**

Discard anything unfalsifiable ("you need to think entity-first"), and say you discarded it.

### Step 2. Dedupe against this file — BEFORE verifying

Read the Baseline sections, the Ledger, and the Quarantine below. Cheaper to find a duplicate
than to research it. Match **semantically**, not by keyword — "add stats to get cited" and
"statistics increase attribution" are the same claim.

Classify each claim:

| Outcome | Meaning | Action |
|---|---|---|
| **DUPLICATE** | Already covered at equal or better evidence | Skip. Report it as already-known and cite where |
| **STRENGTHENS** | Same claim, but this source is a *higher tier* than what's on file | Verify, then upgrade the existing entry's tier and add the source |
| **REFINES** | Narrows, bounds, or adds a condition to an existing entry | Verify, then edit the existing entry — do not add a second one |
| **CONTRADICTS** | Conflicts with an existing entry | **Highest-value case.** Go to Step 3 with extra rigor. If the new claim wins, revise the old entry and log the reversal in the Changelog |
| **NEW** | Genuinely not covered | Verify normally |

Never let this file hold two entries that disagree. Reconcile or reject.

### Step 3. Verify against primary sources

Search out from the claim. Do not stop at the first agreeing blog post — agreement between
SEO blogs is nearly worthless, because they cite each other in a loop.

For each claim, in order:

1. **Find the primary source.** Trace every claim back to its origin. If a claim is "Google
   confirmed X", find Google saying X. If it's "the study showed Y", read the study's methods
   and numbers — not the vendor's summary of it.
2. **Check the chain of custody.** A shocking number of "confirmed" industry facts trace to a
   headline about a conference talk with no transcript, propagated via LinkedIn. If the chain
   dead-ends in hearsay, it is T4 regardless of how universally repeated it is.
3. **Check for the debunk.** Search for the claim *plus* "debunked", "myth", "doesn't work",
   "failed to replicate". Search Google's AI optimization guide and spam policies. Many live
   claims were killed by an official doc note with no blog post.
4. **Read the methodology if there is a study.** Look specifically for the failure modes in
   the checklist below.
5. **Check freshness.** This field rots in months, not years. A 2025 statistic about AI
   citation behavior is probably already false. Always find the date.

**Search the primary domains directly:** `developers.google.com/search`, `web.dev`,
`developer.chrome.com`, `status.search.google.com`, `developers.openai.com`,
`docs.perplexity.ai`, `support.claude.com`, `blogs.bing.com/webmaster`, `arxiv.org`.

### Step 3b. Methodology red flags — the bullshit detector

Apply to any study backing a claim. Any hit caps the tier at T3; multiple hits mean reject.

- **Fixed-context bias.** Measures effect *conditional on already being retrieved*, then sells
  it as visibility. The single most common error in GEO research. Ask: does this measure
  getting *found*, or getting *quoted once already found*? They are different products.
- **Missing denominator.** "Cited in 60% of responses" — of responses that had citations at
  all? Out of how many queries?
- **Range restriction.** Filtered the sample (e.g. only DR>40 sites, only pages with 100+
  citations), which mechanically deflates or inflates correlations. Very common in vendor
  correlation studies, and never acknowledged by them.
- **Common cause / near-tautology.** Correlating two proxies for brand size and calling it a
  finding. If "branded mentions" predicts "brand visibility", you have measured that big
  brands are big.
- **LLM-judge circularity.** The same model family generates, answers, and scores.
- **Single-shot measurement.** AI engines return **Jaccard 0.34–0.42 across identical repeated
  queries**. One run is noise. Any tool reporting a visibility score without a confidence
  interval is selling you variance.
- **No downstream validation.** Traffic/revenue claims with no causal design.
- **Fabricated precision.** "AI favors 134–167 word passages", "the L3 gate uses XGBoost at
  threshold 0.7". Suspiciously specific numbers with no primary source are the signature of
  hallucinated content. Verified fabrications in the wild.
- **Vendor incentive.** Does the study's conclusion happen to be "buy our product"?
- **Correlation sold as causation.** Nearly universal. Note when the authors themselves
  disclaim it — many do, and vendors then drop the disclaimer.

### Step 3c. The adoption-decay test — unique to GEO

C-SEO Bench (NeurIPS 2025) found GEO gains **decay as adoption rises** — it is zero-sum. So ask:

> If this tactic is published, sold, and widely adopted, does it still work?

If a tactic only works while rare, it is self-annihilating and cannot be a durable practice.
It may still be worth logging as a **time-boxed arbitrage** in the Quarantine, with an explicit
expiry — but never as a baseline practice. This test alone kills most "AEO playbook" content.

### Step 3d. The usefulness test — true is not sufficient

Truth is the first gate, not the last. This file is a working database, not a trivia
collection: an entry earns its place only if it **changes what someone does**. Ask which of the
two ways it is useful:

- **Prescriptive** — it tells you what to do. ("Allow `OAI-SearchBot`." "Deindex via
  `noindex`, not robots.txt.")
- **Corrective** — it stops you doing something wrong, or redirects effort that's being
  wasted. ("Schema is not an AI-citation lever." "Blocking Google-Extended does nothing to AI
  Overviews.")

Corrective entries are often the most valuable here, because this field's main failure mode is
confident spending on tactics that don't work. That is why "site-level notability beats
page-level tactics" belongs in the file despite not being directly actionable — it reallocates
budget away from markup toward PR.

**Reject as not-useful even when true:**

- **No decision changes.** True, but nobody would do anything differently knowing it.
- **Effect too small to matter.** Real but sub-noise; it will lose to every competing priority.
- **Already implied** by a more general entry on file. Don't add the special case.
- **Trivially obvious.** "Write helpful content." Costs a read, teaches nothing.
- **Describes a state, not a lever, and corrects nothing.** "Big brands get cited more" — with
  no misconception being fixed, it's just an observation.

If a claim passes truth but fails usefulness, say so explicitly in the report. "True, but it
doesn't change anything you'd do" is a legitimate and useful verdict — and it protects the file
from bloating into something nobody reads.

### Step 4. Assign tier and verdict

| Verdict | Criteria |
|---|---|
| **ACCEPT** | Passes **both** gates: (a) **true** — T1 or T2 support, or T3 with sound methodology, not contradicted by anything higher, survives the adoption-decay test; and (b) **useful** — prescriptive or corrective per Step 3d |
| **ACCEPT AS PROVISIONAL** | Directionally plausible, cheap, low-risk, no contradicting evidence — but under-evidenced. Goes in with an explicit `PROVISIONAL` tag and what would confirm/kill it |
| **QUARANTINE** | Interesting and not disprovable with available evidence, but unverified — or a time-boxed arbitrage. Logged separately. **Not to be acted on or repeated to clients** |
| **REJECT** | Fails **either** gate: contradicted by higher-tier evidence, unfalsifiable, fabricated, chain-of-custody dead-end, fails adoption-decay — **or** true but useless per Step 3d. Log false claims in the Rejected table so nobody re-litigates them; true-but-useless ones just get reported, not filed |

**Bias toward REJECT and QUARANTINE.** This file's value is its precision, not its size. A
skill with 30 true practices beats one with 200 practices of which 60 are wrong, because the
second one cannot be trusted at all and must be re-verified from scratch on every use.

### Step 5. Write it in

- **ACCEPT** → the relevant Baseline section, or the Ledger if it's a sharper/newer practice
  than the baseline covers.
- **PROVISIONAL / QUARANTINE** → Quarantine table.
- **REJECT** → Rejected/Myths table, with the reason. This is not waste — it stops the same
  LinkedIn post from being re-researched in three months.
- Any change to an existing entry → note it in the Changelog.

Edit **this file only**. This skill is deliberately a single self-contained `SKILL.md` so it
can be dropped into any global skills directory with no sidecar files. Do not create
`references/`, `scripts/`, or data files. If the file gets unwieldy, prune low-value entries —
don't split it.

### Step 6. Report back

Tell the user, per claim: the claim, the verdict, the tier, the deciding evidence, and where
it landed. Lead with anything that **contradicted** an existing entry or **debunked** something
they believed — that is the highest-value output. Be direct when a source is bad; if a
LinkedIn post is entirely marketing, say so plainly rather than finding one salvageable crumb.

### Entry format

```
- **[T1|T2|T3|PROVISIONAL] Claim stated as an actionable practice.**
  Evidence: what specifically supports it (study design, sample, the actual number).
  Source: URL (date).
  Bounds: where this stops being true / what it does NOT claim.
  Volatility: volatile | semi-stable | stable  (see the AUDIT volatility table)
  Added: YYYY-MM-DD from <source>. Verified: YYYY-MM-DD.
```

`Bounds` is mandatory on accepted entries. Most bad SEO advice is true advice applied outside
its range.

`Verified` is mandatory and is what makes AUDIT possible. It means *a human or agent re-fetched
the primary source on that date and it still said this*. It is not the date you last looked at
the entry.

---

## MODE B — CONSULT

Answer from the Baselines, Ledger, and Rejected list. Rules:

1. **Always give the tier.** "Yes, T1 — Google documents this" and "maybe, T4 — one agency
   blog claims it" are different answers and the user needs to know which they got.
2. **Check the Rejected/Myths table first** when asked "should we do X". The answer is often
   "no, and here's the primary source saying so".
3. **Check freshness before you answer.** Look at the entry's `Verified` date against its
   volatility class (see AUDIT). If it's past its window and the question is consequential,
   run a spot-AUDIT on that entry *before* answering, then say you did. Answering from a stale
   volatile entry is how this skill would start doing harm — the citation statistics in here
   have a half-life of months, not years.
4. **Don't fabricate to fill a gap.** If this file doesn't cover it and you haven't verified
   it, say so and offer to research it. An honest "unknown" is a valid deliverable — several
   of the most important questions in this field are genuinely open, and they're listed below.
5. **Distinguish mentioned from cited.** Being *recommended* in an answer and being *linked*
   as a source are different outcomes with different levers. Most tools conflate them. Ask
   which one the user actually wants.

---

## MODE C — AUDIT (self-maintenance)

Everything in this file has an expiry date, and most of it will expire without anyone
announcing it. **Google now deprecates structured-data types via silent doc notes with no blog
post** — FAQ rich results died that way on 2026-05-07. **AI citation statistics move in
months** — top-10 citation share went 76% → 37.9% in six months. An unaudited knowledge base
in this field becomes actively harmful faster than it becomes merely old, because it keeps
answering with the same confidence after the facts move.

**Triggers:** the user asks to audit / refresh / update / "check if anything changed"; CONSULT
hits an entry past its re-verify window on a consequential question (spot-audit just that
entry); a scheduled run; or before any client-facing deliverable leaning on a volatile entry.

### Step 1. Select by volatility — never audit top-to-bottom

| Class | Re-verify | What's in it |
|---|---|---|
| **Volatile** | ~monthly | Dated statistics (citation share, ranking overlap), platform/model changes, the crawler table, the structured-data gallery, Quarantine expiries |
| **Semi-stable** | ~quarterly | T3 studies and correlations, PROVISIONAL entries, CWV thresholds, spam policy list |
| **Stable** | ~annually | T1 mechanism claims, myths with primary-source debunks, the open-questions list |

A full audit is rarely the right move. Audit the volatile set monthly and you catch ~90% of
real change for ~10% of the work. The **Audit Watchlist** near the end of this file names the
specific highest-rot entries — start there.

### Step 2. Check the silent-change sources FIRST — highest yield per minute

1. **[developers.google.com/search/updates](https://developers.google.com/search/updates)** —
   **the single highest-value source.** It catches doc-note deprecations that never get a blog
   post. If you check one thing, check this.
2. **The AI optimization guide's "last updated" date** — if it moved since our last audit, diff
   it. It is the densest T1 document in the field and it is being actively revised.
3. [status.search.google.com ranking history](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history) — authoritative core/spam update dates.
4. [developers.google.com/search/blog](https://developers.google.com/search/blog)
5. Crawler docs: [OpenAI](https://developers.openai.com/api/docs/bots), [Google](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), [Perplexity](https://docs.perplexity.ai/guides/bots), [Anthropic](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) — new user-agents appear here first.
6. [blogs.bing.com/webmaster](https://blogs.bing.com/webmaster) — currently the only platform shipping real fan-out data.
7. **arXiv** — search for replications or critiques of anything cited here. The most important
   entry in this file (the GEO replication failure) came from exactly this check.
8. [web.dev/blog](https://web.dev/blog) + the [Chrome INP changelog](https://chromium.googlesource.com/chromium/src/+/main/docs/speed/metrics_changelog/inp.md) — for CWV.

**Do not audit by searching the open SEO web.** That layer is polluted with AI-generated blogs
that fabricate specific technical claims and cross-cite each other into apparent consensus. It
will "confirm" things that never happened. Go to primary domains.

### Step 3. Per entry — re-fetch, compare, classify

| Outcome | Action |
|---|---|
| **UNCHANGED** | Bump `Verified`. Nothing else. |
| **REVISED** | Fact shifted within the same claim (a threshold, a number, a date). Edit in place, update `Verified`, log it. |
| **DEMOTED** | Evidence got weaker — a study failed replication, a "confirmation" turned out to be hearsay. Drop the tier. If it falls below the bar, move to Quarantine or Rejected. |
| **PROMOTED** | Evidence got stronger. Raise the tier; Quarantine → Baseline if it now clears the gate. |
| **DEAD** | No longer true. Move to **Rejected** with the date it died and what killed it. Do not delete — a dead practice that's still circulating needs a row so it gets rejected on sight. |
| **REVERSED** | See Step 4. |

### Step 4. Audit the Rejected table in reverse — this is not optional

The Rejected table is the part most likely to go quietly wrong, because nobody re-checks a
"no". Rejections are claims about the world at a point in time, and the world moves.

Named revival candidates to check each audit:
- **llms.txt** — currently dead on T1 + a 97%-never-fetched study. Revives instantly if any
  major engine announces support. Check the crawler docs, not the SEO blogs.
- **Schema for AI citation** — the rejection rests on a DiD that only sampled already-famous
  pages. If someone runs the new-entity experiment, this could split into "no for established
  brands, yes for unresolved entities."
- **Site reputation abuse enforcement** — currently "manual only" per the last verifiable
  statement. Watch for a primary source on algorithmic enforcement, and for the EU DMA probe
  changing the policy outright.
- **AI Overview / ranking overlap statistics** — these are the fastest-moving numbers here and
  each model swap (e.g. Gemini 3, 2026-01-27) can move them by tens of points.

If a rejection reverses, that is the highest-value output an audit can produce. Lead the report
with it.

### Step 5. Expire the Quarantine

Every Quarantine entry has an expiry. Past it, force a decision: **promote** (evidence arrived),
**reject** (it didn't), or **extend once** with a written reason. Nothing sits in Quarantine
indefinitely — that's just a slush pile with extra steps. Time-boxed arbitrage entries expire
hard; per the adoption-decay test, a tactic that only worked while rare is worthless once it's
in a file like this.

### Step 6. Report a diff, not a summary

Lead with reversals, then deaths, then demotions, then revisions. State what is *newly*
uncertain. **If nothing changed, say so plainly** — a clean audit is a real result, and padding
it with restated known facts trains the reader to skim the one that matters.

Log every change in the Changelog with the date and what triggered it.

### The one hard rule

**Never bump `Verified` without actually re-fetching the primary source.** A fresh date on an
unchecked entry is worse than a stale one: it launders staleness as freshness and removes the
only signal that would have caught it. If you couldn't reach the source, say so and leave the
date alone.

---

## BASELINE — Universal (applies to SEO and AEO alike)

- **[T1/T2] Good SEO is the dominant lever for AI visibility. There is no separate AEO
  discipline that outperforms it.**
  Evidence: Google — *"From Google Search's perspective, optimizing for generative AI search is
  optimizing for the search experience, and thus still SEO."* Independently corroborated by
  C-SEO Bench (NeurIPS 2025), which benchmarked GEO tactics head-to-head against traditional
  SEO and found *"traditional SEO strategies... are significantly more effective"* — GEO methods
  were *"not only largely ineffective but also frequently have a negative impact."*
  Source: [Google AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) (updated 2026-07-10); [arXiv:2506.11097](https://arxiv.org/abs/2506.11097).
  Bounds: Google has an incentive to say this. But the T2 replication is independent and agrees.
  Retrieval into the context window precedes every page-level trick.
  Added: 2026-07-16.

- **[T2/T3] Site-level notability beats every page-level tactic.**
  Evidence: Across 55,936 queries and 6 LLM search engines, the top predictor of citation was
  **Tranco rank (ρ=0.923)** — raw global domain popularity — then outlink count (0.799).
  Consistent with Ahrefs' 75K-brand study where branded web mentions (ρ=0.664) beat backlinks
  (ρ=0.218) for AI Overview visibility.
  Source: [arXiv:2512.09483](https://arxiv.org/abs/2512.09483) (Dec 2025); [Ahrefs](https://ahrefs.com/blog/ai-overview-brand-correlation/) (2025-05-26).
  Bounds: **Correlation, and partly tautological** — popularity is a confounder for both
  variables. The Ahrefs study also filtered to DR>40, which mechanically deflates the backlink
  number. The honest causal statement: be a genuinely notable brand covered by sources these
  engines retrieve. That is PR and product, not markup. Google explicitly pre-empts the exploit:
  *"Seeking inauthentic 'mentions' across the web isn't as helpful as it might seem."*
  Added: 2026-07-16.

- **[T1] Content quality policy is keyed to *purpose*, not production method.**
  Evidence: The spam policy is **scaled content abuse** — *"when many pages are generated for
  the primary purpose of manipulating search rankings and not helping users."* AI-generated
  content is not per se a violation; mass-produced ranking-bait is.
  Source: [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies) (updated 2026-05-15).
  Bounds: This is not permission to scale AI content. The policy catches it by intent.
  Added: 2026-07-16.

- **[T2] Measure across 5–10 runs per prompt, or don't report a number.**
  Evidence: Commercial answer engines return **Jaccard 0.34–0.42 across identical repeated
  queries**. Single-shot measurement reports noise as signal.
  Source: [arXiv:2604.07585](https://arxiv.org/pdf/2604.07585) (2026); corroborated by the July 2026 critical survey.
  Bounds: Applies to every AI visibility dashboard, including ones we build. Report confidence
  intervals or report nothing.
  Added: 2026-07-16.

---

## BASELINE — SEO

### Ranking and quality
- **[T1] E-E-A-T is NOT a ranking factor.** Verbatim from the starter guide: *"E-E-A-T as a
  ranking factor: No, it's not."* It is a rater-guideline evaluation concept describing what
  Google's systems try to approximate. Raters *"never change any individual site's ranking."*
  Of the four, **trust is the most important**; the others contribute to trust.
  Source: [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) (2025-12-10).
  Bounds: The underlying signals are real targets. "E-E-A-T optimization" as a product is not.

- **[T1] The Helpful Content Update no longer exists as a separate system.** Folded into core
  ranking in March 2024; listed under *retired* systems with Panda and Penguin. There is no
  discrete HCU classifier to recover from.
  Source: [Ranking Systems Guide](https://developers.google.com/search/docs/appearance/ranking-systems-guide) (2025-12-10).

- **[T2] Click data is used in live ranking (NavBoost).** Sworn testimony (Pandu Nayak, US v.
  Google, 2023): NavBoost exists, dates to ~2005, retains ~13 months of click data per query,
  and is among Google's most important signals. `Glue` is the analogue for other SERP features.
  Source: [Search Engine Land trial summary](https://searchengineland.com/how-google-search-ranking-works-pandu-nayak-435395).
  Bounds: **"NavBoost is real" ≠ "CTR manipulation works."** `badClicks` and
  `lastLongestClicks` exist; machine-generated traffic is an explicit spam policy violation.
  This is the most abused inference in SEO. Also note what it really established: Google's
  public statements are PR-managed and must be read as interested testimony, not documentation.

### Meta tags, titles and snippets
- **[T1] Give every page a unique, descriptive `<title>`. But the documented consequence of
  duplicate titles is that Google *rewrites* them — not a ranking penalty.**
  Evidence: *"Avoid repeated or boilerplate text in `<title>` elements... Titling every page on
  a commerce site 'Cheap products for sale', for example, makes it impossible for users to
  distinguish between two pages."* Google's title-rewriting doc lists *"Some use the same titles
  on every page regardless of the page's actual content"* as a trigger for replacement. **The
  word "rank" appears zero times in the entire title-link document.**
  Source: [Title link](https://developers.google.com/search/docs/appearance/title-link); [More info about titles](https://developers.google.com/search/blog/2021/09/more-info-about-titles) (2021-09-17).
  Bounds: This is a **SERP-control and CTR problem, not a ranking problem.** Real and worth
  fixing — five pages sharing a homepage title is a genuine bug — but fix it to control what
  users see, and don't expect ranking movement. Do **not** call it cannibalization (see Rejected).
  Volatility: stable. Added: 2026-07-16 from Slack (unveilrai.com meta audit). Verified: 2026-07-16.

- **[T1] There is no character limit on titles or meta descriptions. Truncation is
  device-width based.**
  Evidence: *"There's **no limit on how long a meta description can be**, but the snippet is
  truncated in Google Search results as needed, **typically to fit the device width**."* Same
  language for titles: *"While there's no limit on how long a `<title>` element can be, the
  title link is truncated... typically to fit the device width."*
  Source: [Snippet docs](https://developers.google.com/search/docs/appearance/snippet); [Title link](https://developers.google.com/search/docs/appearance/title-link).
  Bounds: **Pixel/viewport-based, not character-based** — so 155–160 and 60 are folklore
  approximations, not limits (see Rejected). The one empirically useful number is T3: titles of
  **51–60 characters get rewritten least (~39–42%)**, vs >70 chars at **99.9%**. Use that as a
  heuristic, not a rule. Front-loading the important text is right for the right reason —
  truncation is real, the specific number isn't.
  Volatility: stable. Added: 2026-07-16 from Slack (unveilrai.com meta audit). Verified: 2026-07-16.

- **[T3] Google rewrites roughly two-thirds of meta descriptions and ~62% of titles. Budget
  your effort accordingly.**
  Evidence: Meta descriptions — Portent: **71% mobile / 68% desktop** rewritten (30,000
  keywords, 2020-09-10); Ahrefs: **62.78%** (20,000 keywords / 192,656 pages, 2020-10-09).
  Titles — Zyppy: **61.6%** rewritten (80,959 titles / 2,370 sites, early 2022). Google's own
  T1 framing: title elements are *"used around 87% of the time."*
  Source: [Portent](https://www.portent.com/blog/seo/google-rewrites-meta-descriptions-over-70-of-the-time-study.htm); [Ahrefs](https://ahrefs.com/blog/meta-description-study/); [Zyppy](https://zyppy.com/seo/google-title-rewrites/).
  Bounds: **The 61.6% and Google's 87% are not contradictory** and people cite the gap as if it
  catches Google lying. Google's "used" means used *as the basis* including minor edits; Zyppy
  counts any character difference. Both vendor studies, both ~2020 — semi-stable at best.
  Also, per Zyppy: *"Simply because Google doesn't display certain words from your title tag...
  doesn't always mean that those words aren't helping you to rank. These are two separate
  processes."* Write descriptions for the ~30% of the time they're used; don't agonize.
  Volatility: semi-stable. Added: 2026-07-16 from Slack (unveilrai.com meta audit). Verified: 2026-07-16.

- **[T1] The meta description is not a ranking factor — but the citation is 17 years old.**
  Evidence: *"while accurate meta descriptions can improve clickthrough, they won't affect your
  ranking within search results"* (2007); *"we still don't use the description meta tag in our
  ranking"* (2009).
  Source: [2007 post](https://developers.google.com/search/blog/2007/09/improve-snippets-with-meta-description); [2009 post](https://developers.google.com/search/blog/2009/09/google-does-not-use-keywords-meta-tag).
  Bounds: **Both posts carry Google's own "some of the information may be outdated" banner, and
  the current snippet docs contain no ranking statement at all.** Uncontradicted and universally
  accepted, but anyone citing it is citing a 2009 blog post. Hold as true, know the footing.
  Volatility: semi-stable. Added: 2026-07-16 from Slack (unveilrai.com meta audit). Verified: 2026-07-16.

### Trust and legal pages
- **[T1] For stores and YMYL sites, what matters is contact and customer-service information —
  and it must *exist and be findable*, not be indexed.**
  Evidence: Quality Rater Guidelines (2025-09-11, 182pp) §5.5: *"Pages that offer payment
  functionality or process other types of financial transactions **should receive a Low rating
  if there is an unsatisfying amount of customer service information or contact information**."*
  §2.5.3: *"Contact information and customer service information are extremely important for
  websites that handle money."* For shopping sites specifically: *"the store's policies on
  payment, exchanges, and returns."*
  Source: [QRG PDF](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf) (2025-09-11).
  Bounds: **Three things get conflated here, and all three matter.** (1) **Scope** — the QRG
  says contact / customer service / About Us, and for stores payment-exchange-return policies.
  It says **nothing** about privacy policies or T&C: *"privacy policy" appears zero times in 182
  pages*, and the only two "terms of service" hits use the ToS to *catch a site being deceptive*
  (an AI-generated parenting site whose ToS admitted it → rated **Lowest**). (2) **Indexing ≠
  existence** — raters browse the site like a person ("Be a detective!"), so a `noindex` page
  fully satisfies this. The QRG never discusses indexing; "noindex" appears zero times. (3)
  **Instrument ≠ algorithm** — rater scores don't move rankings, and E-E-A-T isn't a ranking
  factor.
  Volatility: semi-stable. Added: 2026-07-16 from Slack (unveilrai.com meta audit). Verified: 2026-07-16.

### Technical
- **[T1] robots.txt disallow ≠ noindex, and they conflict.** *"If a page is disallowed from
  crawling through the robots.txt file, then any information about indexing or serving rules
  will not be found and will therefore be ignored."* To deindex: **allow crawling + serve
  `noindex`.** Blocking in robots.txt to deindex actively causes the problem it claims to solve
  — the URL can still be indexed URL-only via external links.
  Source: [Robots meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) (2026-03-24).

- **[T1] rel=canonical is a hint, not a directive.** Google may pick a different canonical.
  Other signals: HTTPS preference, internal linking, sitemaps, redirects, reciprocal hreflang.
  Source: [Consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) (2026-07-10).

- **[T1] Crawl budget is a non-issue below ~10k pages.** Google's own thresholds: worry only at
  **1M+ pages changing weekly**, or **10k+ pages changing daily**, or a large share of URLs in
  "Discovered - currently not indexed."
  Source: [Crawl budget](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget) (2025-12-19).
  Bounds: Most crawl-budget consulting sold to SMBs is unnecessary.

- **[T1] Googlebot renders JS, but the render queue has no SLA** — *"may stay on this queue for
  a few seconds, but it can take longer."* Google still recommends SSR/prerender because
  *"not all bots can run JavaScript."*
  Source: [JS SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) (2026-03-04).
  Bounds: This is now **more** load-bearing for AEO than SEO — most AI crawlers do not render
  JS at all. If your content requires JS, AI engines may see nothing.

- **[T1] Core Web Vitals: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1** at the **75th percentile** of real
  users, split mobile/desktop. INP replaced FID on 2024-03-12.
  Source: [web.dev/articles/vitals](https://web.dev/articles/vitals).
  Bounds: **Small ranking effect.** Google: *"Google Search always seeks to show the most
  relevant content, even if the page experience is sub-par"* and *"trying to get a perfect score
  just for SEO reasons may not be the best use of your time."* Justify CWV work on conversion
  and UX, not ranking. Lighthouse is lab data; ranking uses field/CrUX data.

### Structured data
- **[T1] FAQPage rich results are DEAD as of 2026-05-07.** Filter, Search Console report, and
  Rich Results Test support dropped June 2026; API support removed August 2026. Announced via a
  quiet doc note, **no blog post**.
  Source: [SEJ](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/) (2026-05-10).
  Bounds: Google killed the *rich result*, not the *markup*. The schema is still valid and may
  aid comprehension. Don't rip it out urgently; do stop selling it as a SERP-visibility tactic.
  **HowTo** is likewise fully deprecated (2023). Also removed: practice problems (2026-01),
  course info / estimated salary / learning video / special announcement / vehicle listing
  (2025-09).

- **[T1] Google is now deprecating structured data types via silent doc notes, not blog posts.**
  This section will rot without warning. Monitor
  [developers.google.com/search/updates](https://developers.google.com/search/updates) directly.

---

## BASELINE — AEO / GEO

### Crawler control — the most consequential and most-botched config
- **[T1] Retrieval bots and training bots are independent decisions. Decouple them.**

  | User-agent | Owner | Function | robots.txt |
  |---|---|---|---|
  | `OAI-SearchBot` | OpenAI | **Indexes for ChatGPT search citations — the one that matters** | Respects |
  | `GPTBot` | OpenAI | Model training only | Respects |
  | `ChatGPT-User` | OpenAI | User-triggered live fetch | rules *"may not apply"* |
  | `Googlebot` | Google | Search index — **feeds AI Overviews + AI Mode** | Respects |
  | `Google-Extended` | Google | **Gemini training/grounding only — not a crawler** | Usage token |
  | `PerplexityBot` | Perplexity | Search indexing/citation | Respects |
  | `Perplexity-User` | Perplexity | User-triggered fetch | *"generally ignores"* |
  | `ClaudeBot` | Anthropic | Training | Respects |
  | `Claude-SearchBot` | Anthropic | Search-quality indexing | Respects |
  | `Claude-User` | Anthropic | User-initiated retrieval | Respects |

  Source: [OpenAI](https://developers.openai.com/api/docs/bots), [Google](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), [Perplexity](https://docs.perplexity.ai/guides/bots), [Anthropic](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler).
  Bounds: **Verify bots by published IP range, not user-agent string** (`openai.com/searchbot.json`,
  `perplexity.com/perplexitybot.json`). And note: robots.txt is **not an access control** — the
  user-triggered agents don't honor it. Only IP/WAF blocking does.

- **[T1] Google-Extended does NOT control AI Overviews.** Google: *"Google-Extended does not
  impact a site's inclusion in Google Search nor is it used as a ranking signal."* AI Overviews
  ride **Googlebot** via the core Search index. The only exits are `nosnippet` / `max-snippet` /
  `data-nosnippet`, or leaving Search entirely. Blocking Google-Extended to escape AI Overviews
  is a **null action** — common and expensive.

### What actually moves AI visibility
- **[T1/T3] Optimize for the fan-out sub-questions, not the head query.**
  Evidence: Google officially defines query fan-out as *"a set of concurrent, related queries
  generated by the model to request more information and fetch additional relevant search
  results."* The empirical fallout: AI Overview citations coming from the top 10 collapsed from
  **76% (Jul 2025) to 37.9% (Jan 2026)** — with **31% now from outside the top 100** — attributed
  to Gemini 3 (2026-01-27) increasing fan-out reliance. Citations increasingly come from
  *sub-query* SERPs, not the original query's SERP.
  Source: [Ahrefs, 863K SERPs / 4M URLs](https://ahrefs.com/blog/ai-overview-citations-top-10/) (2026-03-02).
  Bounds: T3 for the numbers, T1 for the mechanism. This is the biggest *real* change in the field.

- **[T1] Mine Bing's grounding queries — the only free, official window into fan-out.**
  Bing Webmaster Tools' AI Performance report exposes the **actual phrases AI used to retrieve
  your cited content.** Real fan-out data, from the platform, free, and badly underused.
  Source: [Bing Webmaster blog](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) (2026-02-10).
  Bounds: Google's equivalent (Generative AI performance reports, 2026-06-03) is
  **impressions-only — no clicks, CTR, or query data.** Bing's is the useful one.

- **[T3] Ranking #1 in Google does not get you cited by ChatGPT.** Overlap between Google top-10
  and AI citations, by platform: **ChatGPT 8%**, Gemini 8.2%, Copilot 8.6%, **Perplexity 28.6%**
  — average 12%. Perplexity is the outlier; it aligns with search rankings by design.
  Source: [Ahrefs, 15K long-tail queries](https://ahrefs.com/blog/ai-search-overlap/) (Jul 2025).
  Bounds: Per-platform strategy is real. Do not treat "AI search" as one surface.

- **[PROVISIONAL, T2-contested] Extractable evidence — statistics, direct answers, definitions,
  citations — helps you get *quoted once retrieved*, not *retrieved*.**
  Evidence: The GEO paper measured quotation addition +41% and statistics +33% on
  *position-adjusted word count*. The 2026 critical survey grants extractable evidence
  *"moderate support"*. But C-SEO Bench found these tactics failed to improve *ranking* and were
  often negative.
  Bounds: **This is the most important bound in the file.** The GEO paper's metric is
  *attribution share within a fixed 5-document context* — i.e. conditional on already being
  retrieved. It is not discovery, retrieval, ranking, or traffic. Every deck rendering this as
  "+40% AI visibility" is committing a category error. Worth doing anyway because it's cheap,
  low-risk, and identical to just writing well. Not worth doing as a visibility strategy.
  What would kill it: a clean study measuring total effect rather than conditional attribution.

- **[T2] Recency/freshness helps for time-sensitive and commercial queries.** One of the few
  levers surviving the critical survey alongside topical relevance and context position.

- **[T3] Schema: implement for rich results and genuine entity disambiguation only. It is not
  an AI-citation lever.**
  Evidence: Ahrefs ran a **difference-in-differences** on 1,885 pages that added JSON-LD vs
  4,000 matched controls — the strongest design in the field. Result: Google AI Mode **+2.4%**,
  ChatGPT **+2.2%** (both indistinguishable from zero), AI Overviews **−4.6%** (a small
  significant *decline*). Google: *"Structured data isn't required for generative AI search."*
  Mechanism evidence: a fake address placed only inside deliberately **invalid** JSON-LD was
  still returned by ChatGPT and Perplexity — they **tokenize** JSON-LD as text, they don't
  **parse** it as schema. Pretraining pipelines also strip `<script>` blocks.
  Source: [Ahrefs DiD](https://ahrefs.com/blog/schema-ai-citations/) (2026-05-11); [Williams-Cook](https://markwilliamscook.substack.com/p/schema-llms-and-the-low-bar-for-evidence) (2026-05-28).
  Bounds: The DiD sampled pages **already receiving 100+ citations** — a selection effect. It
  shows schema won't lift already-visible pages; it **cannot** speak to whether schema helps
  unknown entities get resolved. Cost is low and downside negligible, so keep it for rich
  results and new-brand disambiguation. Just don't sell it as AI visibility.

### The business reframe
- **[T2] The click may simply not exist.** Pew (900 US adults, 68,879 searches, Mar 2025):
  clicks fall from **15% → 8%** when an AI summary appears, and **only 1%** click a link inside
  the summary. Google disputes it.
  Source: [Pew](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/).
  Bounds: This reframes AEO — you are competing for *influence within an answer*, not traffic.
  Corollary: **mentions and citations are different products.** Only 6–27% of the most-mentioned
  brands are also top cited sources. Decide which one you're buying before you measure it.

---

## REJECTED / MYTHS — do not re-litigate

Checked before answering any "should we do X". If a Slack/LinkedIn source repeats one of these,
reject it immediately and cite the row.

| Claim | Status | Evidence |
|---|---|---|
| "Noindex / don't crawl privacy and T&C pages" | **Contradicted — not merely unsupported** | T1 — Mueller, [Bluesky 2024-12-17](https://bsky.app/profile/johnmu.com/post/3ldiu2qc2us2p): *"**IMO it makes no sense to block them**, but it's also not a big enough deal to freak people out about."* And when a user blocked a privacy policy that outranked their homepage: *"this kind of change usually means that our systems aren't convinced of the other page, so **blocking the privacy policy page is just going to make the site less-visibile overall**."* **No evidence at any tier that indexing legal pages harms a site.** Crawl budget doesn't apply below ~10k pages. Hold loosely in both directions — per Mueller it's genuinely low-stakes |
| "Legal pages (privacy/T&C) help E-E-A-T / trust" | **False** | T1 — E-E-A-T isn't a ranking factor, **and** "privacy policy" appears **zero times in the 182-page QRG**. The two "terms of service" hits use the ToS to *catch deception*, not award trust. The real QRG requirement is **contact/customer-service info for stores and YMYL** — about existence and findability, not indexing (see Baseline). The Bluesky thread where Mueller says not to block is *literally SEO practitioners mocking this exact LinkedIn claim* |
| "Duplicate meta titles cause keyword cannibalization" | **Two errors stacked** | T1 — (1) **Wrong term.** "Cannibalization" appears **zero times** in Google Search Central docs (only in the *Ads* API docs, different meaning). It means multiple pages competing for the same *query*; duplicate titles are a *labelling* defect. They're orthogonal — you can have identical titles on pages targeting unrelated queries. (2) **Wrong consequence.** The documented result is Google **rewrites your title**. "Rank" appears zero times in the title-link doc. The fix is right; the reasoning isn't |
| "Meta descriptions have a ~155–160 character limit" | **Folklore** | T1 — *"There's **no limit** on how long a meta description can be... truncated **typically to fit the device width**."* Pixel-based and variable, not a character count. Front-loading is still right — just not because of a magic number |
| "Titles have a ~60 character limit" | **Folklore (as a limit)** | T1 — *"no limit on how long a `<title>` element can be"*; truncation is device-width based. *Usable T3 heuristic:* 51–60 chars get rewritten least (~39–42%); >70 chars → 99.9% |
| "More content + schema + heading tags = quicker/better ranking" | **Three myths chained into a velocity claim** | T1 — all three are in Google's *"Things we believe you shouldn't focus on"* list. Word count: *"no magical word count target."* Headings: *"it doesn't matter if you're using them out of order."* Schema: every documented benefit is **rich results/CTR**, never rank. **No source at any tier** connects these to *speed* of ranking. Google on timing is content-agnostic: *"some changes might take effect in a few hours, others could take several months"* |
| "Block Google-Extended to stay out of AI Overviews" | **False** | T1 — training-only token; AI Overviews ride Googlebot |
| "llms.txt improves AI visibility" | **False** | T1 Google ignores it — *"neither help nor harm"*; Mueller compares it to meta keywords and notes server logs show bots never even check for it. T3: of 137,210 domains, **97% of llms.txt files got zero requests**; the top requesters are **SEO audit tools (21.7%)** checking whether you have one |
| "Anthropic confirmed Claude honors llms.txt" | **Fabricated** | No such statement. Anthropic publishes one *for its own docs* — a publisher act, not a consumer commitment. Vendors inverted it |
| "Chunk your content so AI can index chunks" | **False as stated** | T1 — Danny Sullivan: *"We are not indexing passages. Period."* Google's 2026 guide: *"There's no requirement to break your content into tiny pieces."* Passage *ranking* is real; passage *indexing* is not |
| "Add schema to get cited by AI" | **Unsupported** | T3 DiD: +2.2%/+2.4% ≈ 0, −4.6% on AIO |
| "Microsoft confirmed Copilot uses schema for its LLMs" | **Contested / unsourced** | Traces to a headline about a conference talk with **no transcript, no slides, no primary source**, propagated via LinkedIn. A headline is doing load-bearing work for an entire industry practice |
| "The GEO paper proves +40% AI visibility" | **Category error** | It measures attribution share within a fixed 5-doc context |
| "GEO tactics (stats/quotes) reliably lift visibility" | **Failed replication** | T2 NeurIPS: only **3 of 54** method–domain combos significantly positive; **none** in QA; often negative |
| "76% of AI Overview citations come from the top 10" | **Stale** | Was true Jul 2025. Now **37.9%** (Jan 2026) |
| "Rank #1 → get cited by ChatGPT" | **False** | Only **8%** of ChatGPT citations rank top-10 |
| "Keyword stuffing works on LLMs" | **False** | −9% in the original GEO paper; null-to-negative in every benchmark since |
| "E-E-A-T is a ranking factor" | **False** | T1 — *"No, it's not"* |
| "Fix your HCU hit" | **Stale framing** | T1 — folded into core ranking March 2024; no discrete system exists |
| "FAQ schema wins SERP real estate" | **Dead** | T1 — rich results stopped 2026-05-07 |
| "Block it in robots.txt to deindex it" | **Backwards** | T1 — prevents `noindex` discovery |
| "Domain Authority is a Google metric" | **False** | T1 — Illyes: *"we don't really have 'overall domain authority'"*. DA/DR are vendor scores. *Nuance:* the API leak shows a `siteAuthority` field exists — but it is **not** DA and its production use is unconfirmed |
| "LSI keywords" | **Don't exist** | T1 — a 1980s IR technique irrelevant to neural retrieval. Google uses BERT/MUM/neural matching |
| "Bounce rate is a ranking factor" | **False** | T1 — Mueller: *"that's definitely not the case."* Google has no access to your Analytics. *Nuance:* NavBoost click-satisfaction signals exist; they are **not** GA bounce rate |
| "Ideal word count / longer = better" | **False** | T1 — *"There's no magical word count target, minimum or maximum"* |
| "Meta keywords tag" | **Dead since 2009** | T1 |
| "Keyword density has an optimal %" | **False** | T1 — no such metric; stuffing is a spam violation. Mueller on TF-IDF: an *"artificial metric"* |
| "Exact-match domains help" | **False** | T1 — *"hardly any effect"*; the EMD system exists to *demote* abuse |
| "Strict H1→H2→H3 order is required" | **False** | T1 — not required for search performance |
| "Subdomain vs subfolder is an SEO decision" | **False** | T1 — choose on business needs |
| "AI content violates Google's rules" | **False** | T1 — the policy is *scaled content abuse*, keyed to purpose |
| "Perfect CWV/Lighthouse scores help ranking" | **Overstated** | T1 — *"may not be the best use of your time"*; Lighthouse is lab, ranking uses field data |
| "AI traffic converts 4.4x, so prioritize it" | **True but misleading** | Real ratio, but ~0.2–1% of sessions. Tiny denominators, self-selected samples |
| "AI favors 134–167 word passages" / "Perplexity's L3 XGBoost gate at 0.7" | **Fabricated** | No primary source. Fabricated precision — the signature of AI-generated SEO slop |
| "The March 2026 spam update targeted scaled AI content and parasite SEO" | **Unsourced** | Google publishes update *dates*, not *targets*. Inference sold as fact |
| "Site reputation abuse enforcement is algorithmic now" | **Unconfirmed** | Last verifiable statement (Sullivan): *"We have not gone live with algorithmic actions."* 2026 blog claims lack primary sources |

---

## QUARANTINE — unverified, do not act on or repeat to clients

*(empty — add PROVISIONAL and time-boxed-arbitrage entries here with an explicit expiry and
what evidence would confirm or kill them)*

---

## GENUINELY OPEN QUESTIONS

Resist both the hype and the debunk on these. If a source claims to have settled one, that is
a strong signal to scrutinize it — but also potentially the most valuable thing to add.

- **Does schema help *new, unresolved* entities get disambiguated and retrieved?** The Ahrefs
  DiD can't answer it — it only sampled already-famous pages. Nobody has run the right
  experiment. The single biggest gap.
- **Do AI Overviews / AI Mode use a ranking path distinct from core Search?** Google says
  they're "rooted in core Search ranking and quality systems", but the retrieval/citation layer
  is opaque — and the 76%→38% overlap collapse suggests something meaningful diverged.
- **Is `siteAuthority` live in production, and how is it weighted?** Field exists; nothing else
  is known. No leak, trial, or doc reveals weights for *any* signal — so any "X is the #3
  ranking factor" claim is fabricated by construction.
- **Does a sandbox for new domains exist?** `hostAge` exists; Google has denied a sandbox. Contested.
- **Exact "Crawled – currently not indexed" criteria.** Not published. Every confident cause-list
  in every agency blog is inference. The honest read: usually a *site-level* quality judgment,
  not a page-level bug.
- **Whether FAQ markup retains non-rich-result value.** Google removed the rich result and said
  nothing about comprehension value.

---

## AUDIT WATCHLIST — the highest-rot entries

**All baselines below were seeded and verified 2026-07-16.** Anything without its own
`Verified` date inherits that. Start every audit here, in this order.

| # | Entry | Class | What specifically to re-check | Kill/change signal |
|---|---|---|---|---|
| 1 | Structured-data gallery + FAQ/HowTo deprecations | **Volatile** | [search/updates](https://developers.google.com/search/updates) doc notes | Google kills types silently, no blog post. **Assume rot here by default** |
| 2 | AI Overview top-10 citation share (37.9%, Jan 2026) | **Volatile** | Newer Ahrefs/independent runs | Moved 76%→37.9% in 6 months. Any model swap can move it again |
| 3 | Per-platform overlap (ChatGPT 8%, Perplexity 28.6%) | **Volatile** | Newer studies | Sourced Jul 2025 — **already over a year old, treat as suspect** |
| 4 | Crawler/user-agent table | **Volatile** | All four vendors' bot docs | New agents appear silently; robots.txt behavior gets revised |
| 5 | Google AI optimization guide claims | **Volatile** | Its "last updated" date vs 2026-07-10 | Densest T1 doc in the field, actively revised |
| 6 | Quarantine expiries | **Volatile** | Every entry's expiry date | — |
| 7 | Gemini 3 as AI Overviews default (2026-01-27) | **Volatile** | Model changes | Each swap re-rolls citation behavior |
| 8 | llms.txt rejection | **Semi-stable** | Vendor bot docs only | Revives if any engine announces support |
| 9 | Schema-for-AI rejection | **Semi-stable** | arXiv, Ahrefs | Splits if anyone runs the new-entity experiment |
| 10 | GEO tactics / C-SEO Bench replication | **Semi-stable** | arXiv for re-replications | Field's central finding — a counter-replication would be huge |
| 11 | Site reputation abuse: manual vs algorithmic | **Semi-stable** | Google statements; EU DMA probe | Policy may change by regulation, not by Google |
| 12 | CWV thresholds + soft navigations in CrUX | **Semi-stable** | web.dev, Chrome INP changelog | Soft-nav reporting is officially "to be determined" |
| 13 | Spam policy list (16 items) | **Semi-stable** | [spam policies](https://developers.google.com/search/docs/essentials/spam-policies) | Grew recently (back-button hijacking, Jun 2026) |
| 14 | Crawl budget thresholds; robots/noindex; canonical-as-hint | **Stable** | Annually | T1 mechanism, rarely moves |
| 15 | Myths with primary-source debunks (meta keywords, LSI, density…) | **Stable** | Annually | Debunked for years; safe to leave |

**Read row 3 as an instruction, not a note:** it is the oldest data in this file and it is
already outside its window. It should be the first thing the next audit re-checks.

---

## LEDGER — intake history

Accepted practices are filed in the Baseline section they belong to (with `Added: … from
<source>` provenance on each entry), not duplicated here. This is the log of what was ingested,
so an audit can trace where things came from and how a source performed. Newest first.

- **2026-07-16 — Internal Slack, unveilrai.com meta title/description audit.**
  11 claims atomized → **5 accepted** (unique titles→rewriting not ranking;
  no char limits/device-width truncation; Google rewrite rates; meta desc not a ranking factor;
  QRG contact-info requirement for stores/YMYL) · **6 rejected** (noindex legal pages; legal
  pages→E-E-A-T; duplicate titles=cannibalization; 155–160 char limit; 60 char limit;
  content+schema+headings→faster ranking) · 1 already covered (case studies as extractable
  evidence → the existing PROVISIONAL entry).
  **Source quality note:** the thread's *decisions* were mostly sound while its *reasoning* was
  mostly folklore — both sides of the noindex debate were wrong, and the one action it was about
  to ship (noindex privacy/terms) is contradicted by the only on-record Google statement. Useful
  precedent: **internal Slack is a good source of live decisions and a poor source of
  justifications.** Atomize per-speaker; never accept a conclusion because of who endorsed it —
  seniority is not evidence, and in this thread the most senior call was the wrong one.

---

## CHANGELOG

- **2026-07-16** — **First intake** (Slack, unveilrai.com meta audit). Added a *Meta tags,
  titles and snippets* subsection and a *Trust and legal pages* entry to Baseline SEO; added 6
  rows to Rejected. Headline: **"noindex privacy/T&C pages" is contradicted, not merely
  unsupported** — Mueller on record that blocking *"makes no sense"* and can make a site *"less
  visible overall"*. Also killed the 155–160 and 60 character "limits" (no limits exist;
  truncation is device-width based) and the framing of duplicate titles as "cannibalization"
  (Google never uses the term in Search docs; the real consequence is title rewriting).
- **2026-07-16** — Added the usefulness gate (Step 3d). Truth is now necessary but not
  sufficient: an entry must also be prescriptive (tells you what to do) or corrective (stops
  wasted effort). True-but-useless claims are reported and dropped, not filed. Keeps the
  database a working tool rather than a trivia collection.
- **2026-07-16** — Added AUDIT mode (self-maintenance), the volatility classes, per-entry
  `Verified` dates, and the Audit Watchlist. Rationale: two facts found during the build make
  an unaudited file dangerous rather than merely dated — Google now deprecates structured-data
  types via silent doc notes with no blog post, and AI citation statistics moved 76%→37.9% in
  six months. Audit runs in **both directions**: rejected claims can revive (named candidates
  in Step 4), not just accepted ones dying.
- **2026-07-16** — Skill created. Baselines seeded from a primary-source research pass across
  Google Search Central, web.dev, OpenAI/Anthropic/Perplexity crawler docs, Bing Webmaster,
  the KDD 2024 GEO paper, C-SEO Bench (NeurIPS 2025), the July 2026 critical survey, Ahrefs
  DiD/correlation studies, the 2024 API leak, US v. Google testimony, and Pew. Notable: the
  GEO replication failure and Google's AI optimization guide (updated 2026-07-10) invalidated
  most of the popular AEO playbook, which is reflected in the Rejected table rather than the
  Baselines.
