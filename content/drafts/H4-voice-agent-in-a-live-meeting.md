---
platform: Hashnode
status: draft v1, SKELETON COMPLETE / MEASUREMENTS REQUIRED
primary_keyword: "voice ai agent" (880/mo, SD 47, CPC $28.34)
secondary_keywords: ["how to build an ai agent" (2,900, SD 51), "real time ai meeting assistant" (110), "barge-in detection", "voice activity detection latency"]
intent: Informational with high commercial adjacency
internal_links: [https://lynkk.ai/features/spotter]  # ONE commercial link
word_count: ~1,650 as drafted
constraint: |
  Spotter is IN DEVELOPMENT, early access on Pro by request. This draft must not describe it as
  shipped. Keep that in any edit.
---

# Building a Voice Agent That Speaks Inside a Live Meeting: Latency, Turn-Taking, Interrupts

Post-meeting summarisation is a batch job. You have thirty seconds, nobody is waiting, and if the
first attempt is bad you can retry.

An assistant that participates in a live conversation has none of that. It has roughly two seconds,
one attempt, and a human who will repeat what it says out loud to a customer. Almost every
architectural decision changes.

I work on Lynkk. Our live assistant, Spotter, is **in development with early access on the Mac
app**, so this is a post about building toward this problem rather than a claim to have solved it.
Where I do not have a measured number, I say so.

## The latency budget is the whole design

A natural pause in conversation is somewhere around half a second to two seconds. Past that, the
person waiting for the assistant is visibly waiting, in front of a customer. That is the actual
constraint, and it is social rather than technical.

So budget backwards from two seconds, end to end:

| Stage | Rough budget |
|---|---|
| Audio capture and buffering | 50 to 150 ms |
| Streaming ASR to usable partial | 200 to 500 ms |
| Intent detection: is this for me? | 50 to 100 ms |
| Retrieval over account history | 100 to 400 ms |
| Generation of a short answer | 300 to 800 ms |
| Render to screen | 50 ms |

That totals roughly 750 ms to 2 seconds with nothing going wrong, and it has three implications
that are easy to miss.

**Non-streaming ASR is disqualified.** If you wait for an utterance to end before transcribing, you
have spent your budget before retrieval starts. You need partial hypotheses, and you need to act on
text that may still change.

**Retrieval must be bounded, not best-effort.** A multi-hop agentic retrieval loop that averages
1.5 seconds and occasionally takes six is unusable here, even though the average looks fine. Design
for a hard timeout with a degraded answer, and treat p99 as the number that matters, not p50.

**Generation length is a latency decision.** Tokens cost time. A live assistant should emit one
sentence, not a paragraph, and that is a product constraint before it is a UX preference.

> **[ENGINEER INPUT REQUIRED]** Our actual measured budget per stage, p50 and p99, on real
> hardware. The table above is the shape of the problem, not our numbers. This is the section
> developers will come for.

## Turn-taking: knowing when not to speak

The hard problem is not answering. It is deciding whether to answer at all.

A live assistant that interjects whenever it has something relevant is intolerable within about
four minutes. The default must be silence, and the system needs an explicit gate before it speaks.

Three triggering models, with real trade-offs:

**Explicit invocation.** The user presses a key or says a wake word. Precision is near perfect,
recall is poor, because the user has to notice they need help, which is exactly what they are too
busy to do mid-call. Lynkk's Spotter is designed around an explicit path, with a keyboard shortcut
for help with what is on screen.

**Question detection.** Detect that the far side asked something the user may not be able to answer,
and preload. Better recall, and it introduces false positives, which in a live setting are costly.

**Continuous preloading with silent display.** Keep a panel updated with likely-relevant context,
and never interrupt. The assistant is always "speaking" but never interrupting, because the user
reads when they choose. This is the safest design and probably underrated.

My read: start with explicit invocation plus silent preloading. Question detection that triggers
output is where this gets annoying, and annoying gets uninstalled.

## Voice activity detection and barge-in

Two related problems, often conflated.

**VAD** tells you when speech starts and stops. In a meeting assistant it is cheap and essential:
it gates your ASR, saving both cost and latency. The failure modes are an aggressive threshold that
clips the start of utterances, losing the first word, which is frequently the name, and a permissive
one that burns budget transcribing air conditioning.

**Barge-in** is what happens when someone starts talking while the assistant is producing output.
If the assistant renders to a screen, as Spotter does, barge-in is mild: the text is just there, and
the human arbitrates. If the assistant produces audio into the call, barge-in is critical, and you
need to detect the interruption and stop mid-sentence. This is a large part of why screen-rendered
assistance is substantially easier to build than spoken assistance, and a reasonable place to start.

There is a second argument for rendering to screen, which is not technical: an assistant that
speaks into the call is a participant, and now the other party is talking to your software without
having agreed to. A panel the user reads is a tool. A voice in the call is a disclosure problem.

## Retrieval under a time budget

The valuable queries in a live meeting are not general knowledge, they are retrieval over what was
actually said: what did we quote them in March, what did they say their timeline was, did we ever
send the security document.

That shapes the retrieval design:

- **Pre-scope to the account before the call starts.** You know who the meeting is with from the
  calendar. Narrowing the corpus in advance is the cheapest latency win available.
- **Pre-warm likely queries.** A pre-call brief of what changed, what is open and what to ask
  covers a large share of what gets asked live, computed with no time pressure.
- **Cache the last N turns.** Many live questions refer to the current conversation, not history.
- **Hard timeout with graceful degradation.** Return the three most relevant cited passages rather
  than nothing. A partial answer with citations beats a timeout.

## Being wrong is the real risk

A post-call summary with an error gets caught on reading. A live assistant's error gets repeated
out loud to a customer by a human who trusted it.

That asymmetry should change the confidence threshold, and it leads to design rules I would hold to
regardless of model quality:

**Cite or stay silent.** If the system cannot point to the sentence where something was said, it
should not assert it. Retrieval with a citation is help; generation without one is a liability
aimed at your own customer relationship.

**Prefer quoting to paraphrasing.** "On 20 October she said: we can stretch to $50K for a phased
rollout" is strictly better than "their budget is $50K", because the hedge survives.

**Never guess at numbers.** Prices, dates and headcounts are the highest-cost hallucinations, and
they are the most commonly asked-for facts. Quote or decline.

**Make uncertainty visible, not hidden in prose.** A confidence signal the user can see beats
carefully hedged language they will skim past.

## The disclosure constraint, which is an architecture constraint

One design decision I think is non-negotiable: **the assistant must never be hidden from a screen
share.**

If it disappears when the user shares their screen, the product has been built around concealment,
and the engineering follows the ethics downhill from there. Spotter is built so it is never hidden
from a screen share, and it reads the screen as **text, never sent as an image**, which bounds what
can be incidentally captured.

Both of those are architectural, not cosmetic. Decide them at the start, because retrofitting
"visible during screen share" into a product designed to be invisible is not a UI change.

> **[ENGINEER INPUT REQUIRED]** How the screen-as-text pipeline works, what is excluded, and the
> real invocation path. Also, honestly, what we have found hardest, since that is the content that
> makes this post worth publishing rather than a survey of the problem space.

## Where this actually is

Live meeting assistance is not a solved problem, by us or anyone. The two-second budget and the
false-confidence risk are both genuinely hard, and most of the category has stayed retrospective
for good reasons.

Spotter is [in development with early access](https://lynkk.ai/features/spotter) on the Mac app by
request. If you are building in this area, the two things I would get right first are the hard
retrieval timeout and the cite-or-stay-silent rule. Both are easier to design in than to add later,
and both are what separates a live assistant that gets used from one that gets switched off in
week two.

---

## Publishing notes

**Hashnode compliance:** one commercial link. Space at least a week from H1, H2 and H3.

**Constraints that must survive editing:**
1. **Spotter is in development, not shipped.** Stated twice in the draft. Keep it.
2. The latency table is the **shape** of the problem, explicitly flagged as not our measurements.
   Either fill in real numbers or keep the flag. Do not quietly let the illustrative table read as
   measured data.
3. **Do not publish without the two engineer input blocks filled.** The contribution Hashnode
   requires is the measurements and the "what we found hardest" section.
