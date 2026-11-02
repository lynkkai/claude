---
platform: Hashnode
status: draft v1, SKELETON COMPLETE / SCHEMA + CODE REQUIRED
primary_keyword: "knowledge graph rag" (390/mo, SD 51, CPC $12.56)
secondary_keywords: ["graph rag", "entity resolution", "temporal knowledge graph", "rag citations"]
intent: Informational, practitioner
internal_links: [https://lynkk.ai/features/ask-your-meetings]  # ONE commercial link
word_count: ~1,600 as drafted
collision_check: |
  lynkk.ai has /blog/meeting-knowledge-management, but that is a non-technical FAQ page targeting
  "knowledge management tools" queries. This post is purely an engineering piece and does not
  overlap. Keep it technical; if it drifts into "what is knowledge management", it collides.
---

# Turning Meetings Into Account Memory: Schema, Extraction and Retrieval

Chunk the transcripts, embed them, stick them in a vector store, answer questions over the top.
That is the obvious design for "ask questions about your meetings", and it fails on the questions
people actually ask.

This is about why, and what you have to build instead.

I work on Lynkk, a meeting assistant with account-level memory, so this is written from the
shipping side rather than the paper side.

## The queries that break flat RAG

Start from the questions, because the architecture follows from them. In a sales context the real
queries are:

1. "What did this customer say about budget?"
2. **"How has their budget moved across our last three calls?"**
3. **"What have we promised them, and did we deliver it?"**
4. **"Who on their side has gone quiet?"**
5. "What is still open before we can send a proposal?"

Query 1 is fine with flat retrieval. It is a lookup, the answer sits in one passage, and
similarity search finds it.

Queries 2, 3 and 4 are the valuable ones, and flat chunk retrieval cannot answer any of them
correctly. Here is precisely why.

**Query 2 requires ordered comparison.** The answer is a delta across time: $30K in March, $50K in
October. Similarity search returns the three most budget-ish passages in arbitrary relevance order.
Nothing in the representation encodes that one came before another, or that the later one
supersedes the earlier. The model then has two numbers and no reliable basis for which is current,
and it will frequently pick the wrong one or present both as simultaneous.

**Query 3 requires a closed-world join.** "What have we promised and not delivered" is set
subtraction: all commitments, minus the fulfilled ones. Retrieval is open-world and returns the
top-k most similar passages. It cannot tell you that nothing matched, and "no evidence retrieved"
is indistinguishable from "nothing exists". For a commitment ledger, a false negative is the whole
failure mode.

**Query 4 requires reasoning about absence.** Nothing was said, so there is no passage to retrieve.
Embeddings cannot represent a thing that did not happen. This query is unanswerable without
structure, full stop.

The pattern: flat RAG handles **lookup**. Account memory needs **comparison, aggregation and
absence**, all of which need an explicit structure over time.

## The schema, and keeping it small

The instinct is a rich ontology. Resist it. Every node type you add is another extraction task that
can fail, and extraction failures compound. A minimal schema that answers the five queries above:

**Entities**
- `Account` (the company)
- `Person` (belongs to an Account, internal or external)
- `Meeting` (timestamped, has participants, belongs to an Account)
- `Commitment` (who promised what, to whom, by when, fulfilled or not)
- `Decision` (what was agreed, when, and the quote it rests on)
- `Fact` (a typed attribute with a value and a time: budget, timeline, headcount)

**The two edges that do the work**
- `Fact` to `Meeting`: when this value was stated, which gives you ordering.
- `Fact` to `Fact`: supersession, which gives you "current value" versus "history".

That supersession edge is the entire answer to query 2. Without it you have a bag of numbers.
With it, "how has budget moved" is a traversal, not a semantic search.

**Every node carries a citation**: meeting id, timestamp offset, and the literal quote. More on
why below, because this is the single most important design constraint.

> **[ENGINEER INPUT REQUIRED]** Lynkk's actual schema. I have written the schema this problem
> implies, not ours. Replace with the real node and edge types, and say what we left out and why,
> which is usually the most interesting part of a schema post.

## Extraction: the hard part is time, not entities

Pulling "Priya" and "$50,000" out of a transcript is the easy half. Three things are hard.

**Relative time resolution.** "By Friday", "end of next month", "after the security review". These
have to resolve against the meeting's own timestamp to be useful, and "after the security review"
cannot resolve to a date at all, it resolves to a dependency on another entity. Decide up front
whether your `due` field can hold a dependency or only a date, because retrofitting that is
painful.

**Hedging and conditionality.** "We could probably stretch to $50K if IT signs off" is not a budget
of $50,000. It is a conditional ceiling with a named dependency. Flattening it to `budget = 50000`
manufactures certainty that was not in the room, and that false certainty then lands in a forecast.
Model the condition or store the hedge verbatim, but do not drop it.

**Negation and retraction.** "We said November, but that has slipped." The new fact must supersede,
not coexist. Miss this and your current-value query returns a date the customer has explicitly
withdrawn.

Run extraction **per meeting**, write to the graph **incrementally**, and keep each extraction
reproducible from its source. When extraction improves you will want to re-derive, and you cannot
do that if the graph is the only copy.

## Entity resolution: where it actually hurts

Is the "Priya" in this call the `Person` from March? Is "Corvane" the same account as "Corvane
Logistics"?

Company names are tractable with normalisation plus the CRM as an authority. People are harder,
and in a sales context the failure is expensive and asymmetric:

- **Splitting one person into two** loses history. Bad, visible, users report it.
- **Merging two people into one** attributes a commitment to someone who never made it, then
  surfaces it to your rep as fact. Much worse, and quiet.

So bias toward splitting, and make merges confirmable rather than automatic. One click of "this is
the same Priya" turns an unsupervised problem into a supervised one. Where you have a CRM, treat it
as the identity authority instead of inferring from transcripts.

## Retrieval: the citation is the product

This is the part I would argue most strongly for, and it is a product argument with an
architectural consequence.

An answer that says "their budget increased to $50K" is a liability. An answer that says that
**and plays the eleven seconds where the customer said it** is a tool. Sales decisions get made on
these answers, and an uncited paraphrase across three calls is how optimism silently enters a
forecast.

Architecturally this means: **no node may exist without a source quote and an offset.** Not as a
nice-to-have for the UI, as a hard constraint at write time. If extraction cannot attach a
citation, it does not get written. This also gives you a cheap evaluation hook, because a human can
check a cited answer in seconds and cannot check an uncited one at all.

A workable retrieval shape:

1. **Resolve the account** from the query, deterministically.
2. **Classify the query** into lookup, comparison, ledger or absence.
3. **Traverse** for comparison, ledger and absence queries. **Embed-and-search** only for open
   lookup.
4. **Answer from retrieved nodes only**, each carrying its citation.
5. **Say "nothing found"** when the traversal is empty, rather than letting the model fill the gap.

Step 5 is where most systems lose trust. A graph traversal can distinguish "no commitments exist"
from "I did not find any", and that distinction is the thing flat retrieval cannot give you.

> **[ENGINEER INPUT REQUIRED]** Our real query path, the storage choice (actual graph database
> versus relational with graph semantics, which is a legitimate and under-discussed option), and
> latency numbers at realistic account sizes. Also: what we got wrong first. The failed version is
> the part developers will actually read.

## What I would do differently knowing this

- **Start from the queries**, not the ontology. Write the ten questions, then build the smallest
  structure that answers them.
- **Make time first-class on day one.** Supersession is not a later feature, and retrofitting it
  means reprocessing everything.
- **Hard-fail on missing citations** at write time rather than filtering at read time.
- **Keep the transcripts.** The graph is a derived index. Treat it as rebuildable, because your
  extraction will improve and you will want to re-derive.
- **Never silently merge identities.**

Lynkk's [Ask Lynkk](https://lynkk.ai/features/ask-your-meetings) is the user-facing end of this:
questions answered across every call with an account, with the source quote attached.

---

## Publishing notes

**Hashnode compliance:** one commercial link. Space at least a week from H1, H2 and H4. Keep this
post purely technical, since /blog/meeting-knowledge-management already covers the non-technical
framing and the two would compete if this drifts.

**Do not publish without the three engineer input blocks filled.** The schema, the query path and
the "what we got wrong" section are the contribution. As drafted this is a well-reasoned design
essay, which is not the same as a report from production, and Hashnode readers can tell.
