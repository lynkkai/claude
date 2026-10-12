---
name: prompt-led-article
description: Build a blog whose H1 IS the tracked AEO prompt and whose H2s are that prompt's query fan-out. Use when an article must be citable for a specific tracked prompt rather than merely topical — retargeting an off-prompt article, creating one from a prompt list, or auditing whether an existing article actually answers its prompt. Enforces one-prompt-one-H1, fan-out-derived H2s, an answer-first block under every H2, and a link integrity gate that catches raw-paren markdown breakage and dead internal links.
---

# Prompt-Led Article

Most articles are written topic-first and then have prompts assigned to them. That is backwards, and it produces the failure this skill exists to prevent: an article that reads well, scores well, and is **not the answer to the prompt it claims to target**.

Prompt-led inverts it. The prompt is the specification.

## ⛔ HARD RULE — the prompt-led contract

> **The contract.** H1 = the tracked prompt, verbatim. H2s = that prompt's **sourced query fan-out**. Everything else is downstream of those two lines.

Both halves are blocking, not aspirational:
- **H1 must match `targeted_prompts[0]` character-for-character.** No title-casing, no appended year, no added geo qualifier, no tidying of clumsy grammar.
- **Every H2 must be traceable to a fan-out query from a named source** (the cascade in *Sourcing the fan-out* below). Record the source per query.
- **Fewer than 6 sourced fan-out queries → STOP and report.** Never invent headings to reach the count.
- **Dead headings are a FAIL**, and an H2 the research cannot answer gets cut rather than hedged.
- Ship nothing until `scripts/verify_contract.py` passes.

## Why H1 = prompt

An answer engine retrieves a passage and then decides whether the passage answers the user's question. The cheapest, strongest signal that it does is an exact-string match between the question and the page's own top-level claim.

Paraphrasing costs you that match for nothing. "How quickly can a Dubai **brokerage** become RERA compliant?" against a prompt reading "Dubai **company**" is one word of drift, and the exact match is gone. If the prompt is clumsy, you still use it verbatim — the prompt is what people actually ask, and your job is to match it, not to improve it.

**One prompt, one H1.** Two prompts of equal weight means two articles. A prompt that is genuinely a sub-question of another belongs in an H2.

> **Title length — where you still have a say (AM-INSIGHTS / PART G4).** The measured citation sweet spot for
> a title is **13–15 words as one natural sentence**; 24+ words is the worst bin. **The verbatim rule wins
> regardless** — never reshape a tracked prompt to hit a word count. But when you are *registering* or
> *proposing* a prompt, phrase it in the 13–15 word band, and avoid two shapes that measurably cost
> citations: the word **"Official"** (cited 5× less — 13% vs 61%) and **"Best/Top 10" styling** (placed
> higher, cited less at equal position). A prompt written well at registration never needs this trade-off later.

## Why H2s = fan-out

A retrieval engine decomposes a question before it answers it. Fan-out queries are those sub-questions. Making them your H2s means each retrievable chunk is already scoped to one sub-question, with its answer in the first sentence.

Section headings such as "Key considerations" or "Understanding the basics" retrieve for nothing. Every H2 must be a question a real person would type or ask, or a claim that directly answers one.

## Sourcing the fan-out

This cascade is the hard rule's evidence trail. Try in this order and stop when you have 6-9 usable queries. **Record which source produced each query** — an unsourced H2 fails the contract.

| Source | Tool | Reliability |
|---|---|---|
| 1. Query fan-out | `get_chatgpt_qfo` — **never `..._batch`** | Query list frequently empty; the other two fields are the real payload |
| 2. People Also Ask | `search_serp` → `people_also_ask`, **harvested from a PAA-rich market** | Empty in IN and AE; fires normally in US/GB |
| 3. Autocomplete | `get_autocomplete_suggestions` | Reliable but thin; **anchor seeds to the city/country** |
| 4. SERP decomposition | `search_serp` organic titles + H2s of the top 3 | Always available; the dependable fallback |
| 5. GSC | `get_gsc_page_queries`, `get_gsc_top_queries` | Best evidence of real phrasing when the client has history |

> **Measured twice, 2026-08-26 and 2026-08-27 (Aviaan/AE).** QFO returned 0 queries for 3 of 4 prompts, then 0 for **all 4** on the re-run. PAA returned empty for all 4. **But `get_chatgpt_qfo` still earns the call**: even at `qfo_count: 0` it returns `retrieved_urls` (what the engine actually read) and `response_text` (the answer shape it produces). Diff your citations against `retrieved_urls` and your structure against `response_text` — that is the usable fan-out signal when the query list is empty. Bare `rera` autocomplete seeds returned Indian results ("maharashtra", "meaning in hindi") because the acronym collides across markets. Sources 4 and 5 carried the entire job.
>
> **Diagnosed 2026-08-31 (Aviaan/AE, the same 6 prompts).** Both "failures" were method errors, not dead sources. Neither should be recorded as empty again.
>
> **Source 1 — use the single tool, never the batch.** `get_chatgpt_qfo_batch` returns ONLY `qfo_queries`/`qfo_count`; it silently drops `retrieved_urls` and `response_text`. So a batch run reports "0 of 6, nothing usable" while the single tool on the identical prompt returns the retrieval set and the full answer. The batch tool is what makes QFO look dead. Call `get_chatgpt_qfo` once per prompt and read the other two fields.
>
> **Source 2 — PAA is market-specific, not broken.** Verified in one session: `people_also_ask` came back empty for AE on both a long natural-language question AND a short keyword seed, then returned 4 questions for the SAME tool on `country=us`. The parser works. Harvest the question set from `us`/`gb`, then localise the answers — PAA questions are largely market-independent, the answers are not. Never conclude "this prompt has no PAA" from an AE run alone.
>
> **What the recovered fields are worth.** On "how is a business valued for a shareholder exit", `retrieved_urls` named uaelegislation.gov.ae and a Dubai Chamber PDF — the citation targets — and `response_text` carried a six-section answer including two sub-questions no other source surfaced. On a provider-shaped prompt the same call returned a *local business listing with addresses*, and on a listicle prompt a *ranked comparison table* built from third-party directories. That is the answer SHAPE to match, and only the single tool exposes it.
>
> Autocomplete caveat stands: bare seeds cross markets (`rera` → Maharashtra; `liquidation value` → "under ibc", "in marathi" even at `gl=ae`). Geo-anchor every seed.

### Autocomplete seeds must be geo-anchored
`rera compliance` → India. `rera certificate dubai how to` → Dubai. Where an acronym or term collides across markets, never seed it bare, and add a disambiguation block to the article body.

## Structure

```markdown
# <tracked prompt, verbatim>

> **Quick answer.** <40-60 words. Answers the H1 outright, with the decisive figures in bold.>

<2-3 sentences: why the usual answer to this is wrong or incomplete.>

> **<Disambiguation>.** <Only where the term collides across markets.>

## <fan-out query 1>
<Answer in the FIRST sentence. Then evidence.>

## <fan-out query 2>
### <narrower sub-question>

... 6-9 H2s ...

## Frequently asked questions
### <6 questions NOT already used as H2s, 40-60 word answers>

## Speak to our <team> team
<CTA. Then the byline.>
```

### Answer-first is the load-bearing rule
The first sentence after every H2 must answer that H2's question standing alone, with no preceding setup. A reader who sees only that sentence has the answer; the rest is support.

This is what gets quoted. Fail it and the section is unciteable however good the prose is.

**The measured version of this rule — ~200 characters, and it must contain a fact.** ChatGPT clips
**~200 characters, about two lines, from each retrieved page**: the stretch best matching its own search
words. The answer is written from that clip. So "answer-first" is not satisfied by a sentence that merely
*points at* the answer — the clip has to carry the payload.

Every section opens with an **answer paragraph**: ~2 sentences · the section's search words used naturally ·
**one number** · **one concrete claim**.

Measured failure (AM-INSIGHTS, 530 searches). A retrieved page surrendered this clip:

> *"Tired of looking for the best laptop under 60000 and not coming to a conclusion? You have come to the
> right place. We have compiled a list…"*

Retrieved. Never cited. **Blocking:** a section whose first 200 characters hold no number and no concrete
claim fails, and so does any throat-clearing opener. Adding the number in the third sentence does not fix it.
This applies to the Quick answer block, every H2/H3, and every FAQ answer.

**Self-check:** run `python3 ~/.claude/scripts/clip_check.py articles/<slug>.md` — it prints the real ~200-character
clip per section and flags those with no numeral (triage, not a verdict: judge the concrete-claim half
yourself). Then read only the first two lines of each section, in order, ignoring the rest. That sequence is
approximately what ChatGPT will see. If it does not read as a usable set of answers, the article is not
citable yet. Add the clip check to step 8, beside `verify_contract.py` — both are cheap and offline.
Full mechanics: `~/.claude/aeo-best-practices.md` **PART G**.

## Format match comes before writing

Check what Google already rewards for this prompt. If the SERP is ranked lists and provider pages, a prose explainer will not rank no matter how well argued — and the reverse is equally true.

Run `search_serp` on the prompt and classify the top 10. Match the dominant format, then write. Cross-check against the client's own GSC: the format that already earns their clicks beats the format you would prefer.

> **Naming third parties in a "best X" listicle.** When the SERP demands a ranked list but you cannot verify quality claims about named firms, rank **provider types** on traceable dimensions (price band, who signs, turnaround, who accepts the output) rather than inventing a ranking of named companies. This holds the format without shipping a claim you cannot source. Say so in the article. Never include a domain on the client's citation-exclusion list.

## Link integrity gate

Run `scripts/linkcheck.py` before the article ships. It catches three failures, the first of which is invisible in a diff and survives every other check.

**1. Raw parentheses in a markdown URL.** `[Law No. 8 of 2007](https://.../Law%20No.%20(8)%20of%202007.html)` — the first `)` closes the link early. Renders as visibly broken text and a dead href. Percent-encode to `%28` / `%29`.

**2. Dead internal links.** Client service pages get renamed. Verify every one with `check_urls_liveness`; a 404 internal link is worse than no link.

**3. Dead external links.** Same call. **A government 403 is a PASS** — gov sites block automated HEAD requests routinely; treat only 404 and DNS failure as dead.

## Workflow

1. **Confirm the prompt is tracked.** `list_prompts` — capture its `id`. If it is not tracked, create it or stop.
1b. **Screen the prompt for winnability.** ChatGPT searches the web only when the question needs current
   facts — ~100% when it contains a year, 92% for "best/top", 87% for price, 84% when it names a city, but
   **37% for "what is…"/"how to…" and 18% for general informational**. A purely definitional prompt is
   usually answered from memory, and **no article can win it**. This does not stop the work — the prompt may
   be tracked for good reasons and may pay on other platforms — but record the screen in the handoff and do
   not promise ChatGPT citation from a low-winnability prompt. (PART G1.)
2. **Cannibalization.** `get_gsc_keyword_cannibalization`. A client page at position <=20 for the head term means fix that page instead of writing this one.
3. **Format match.** `search_serp` on the prompt. Classify the top 10. Write to that shape.
4. **Fan-out.** Sources 1-5 above until you have 6-9 queries. Record which source each came from.
5. **Volumes.** `research_keywords` on the fan-out. Zero volume does not disqualify a fan-out query — AEO demand is invisible to Google Ads — but it does decide which H2 carries the SEO weight.
6. **Write** to the structure above.
7. **Link gate.** `scripts/linkcheck.py`, then `check_urls_liveness` on what it extracts.
8. **Verify the contract.** `scripts/verify_contract.py` — H1 matches the prompt verbatim, every H2 is a question or a direct claim, answer-first holds under each.
9. **Hand off** to `/aeo-score` + `/seo-score` (Gate A), then the client humanizer, then `/post-humanize-check` (Gate B).

Steps 7-8 are cheap and offline. Run them before the scoring gates, not after — a failure here invalidates the scores.

## Failure modes

**A perfect answer-first sentence with no fact in it.** "The timeline depends on several factors, which we
set out below" answers the H2 in form and surrenders a clip worth nothing. Answer-first is necessary and not
sufficient — the first ~200 characters must carry a number and a concrete claim (PART G3).

**Retargeting by editing frontmatter.** Changing `targeted_prompts` without rewriting H1 and the H2 spine leaves an article that answers its old question under a new label. It will score fine and never be cited. Retargeting means restructuring.

**Prompt-stuffing every H2.** Only H2s that genuinely are fan-out queries of the H1 belong. Padding with near-duplicate phrasings of the same prompt reads as keyword stuffing and dilutes the exact-match signal.

**A fan-out H2 with no real answer.** If the research does not support an answer, cut the H2. An H2 whose section hedges is worse than an absent section.

**Trusting an empty QFO result.** `qfo_count: 0` with `status: "ok"` is a *tool* success and a *research* failure. Check the count, not the status — then check whether you called the batch tool, which reports exactly this while discarding the fields that carry the answer.

**Using `get_chatgpt_qfo_batch` for research.** It returns the query list and nothing else. Convenient for six prompts at once, and it throws away `retrieved_urls` and `response_text` — the two fields that are usable when the query list is empty, which is most of the time. Use the single tool per prompt.

**Reading PAA from one market and calling it absent.** An empty `people_also_ask` in AE or IN says nothing about the prompt; the same tool returns questions for `us`. Re-run in a PAA-rich market before recording a miss, and label harvested questions with the market they came from.
