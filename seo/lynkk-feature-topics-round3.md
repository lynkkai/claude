# Lynkk.ai: Topics for Ask Lynkk, Slack and Workspaces

Prepared 2026-11-03. I read all three feature pages before researching. US volumes from Ubersuggest,
locId 2840.

**The short version: one of these three directions has a real keyword cluster and two do not.** Ask
Lynkk maps onto a 2,500-search cluster at SD 19 to 24. Slack and Workspaces both look promising from
the product side and turn out to be dead ends in search, for different reasons. Details and the
exact zero-volume seeds are below.

---

## What each feature does (for the record)

**Ask Lynkk** (`/features/ask-your-meetings`, Pro): ask a question and get one synthesized answer
drawn from every call where the topic came up, with each sentence linked to its source minute. Thread
view per company, person or project. No manual tagging. Can book calendar events, create Jira issues,
share notes, with a confirmation card per action. **Answers only from your own notes, not
teammates'.** Headline: "Ask your meetings. One answer from every call."

**Lynkk for Slack** (`/slack`): mention `@Lynkk` in a channel and it replies in-thread with sources,
from the asker's own notes. Reads only the message that mentions it, its DMs and `/lynkk`. "The
channel sees everything. Lynkk sees one message." Install on any plan, answering requires Pro.

**Workspaces** (`/features/workspaces`): shared company account up to 10 people, Pro for all members.
Notes default to "Admins can see this note"; members can mark a note "Personal" to block admin
access. Admin reads are logged. Admins get summary and transcript but never audio or video. SCIM
available. The page's framing question is "Can my boss read my notes?"

---

## Ask Lynkk: the one real cluster

| # | Title | Vol | SD | CPC | Risk |
|---|---|---|---|---|---|
| A1 | Personal Knowledge Management: Systems, Tools and What Actually Sticks | **2,500** | **20** | $4.19 | Medium |
| A2 | Best Second Brain Apps: 8 Compared | 360 | **19** | $14.86 | Low |

The cluster: `personal knowledge management system` **590 (SD 36)**, `personal knowledge management`
**480 (SD 23)**, `personal knowledge management app` 480 (SD 39), `personal knowledge management
systems` 260 (SD 52), `personal knowledge management tool` **210 (SD 20)**, `personal knowledge
management tools` 70 (SD 29), `ai personal knowledge management` 30 (SD 32), `personal knowledge
management pkm` 30 (SD 23). Plus `second brain app` **260 (SD 24)** and `best second brain app` 90
(**SD 19**) for A2.

**Why this fits Ask Lynkk.** PKM is the established category name for "one searchable brain of
everything you know", and Ask Lynkk is that for meetings specifically, with the source-citation
feature being the thing most PKM tools lack. Entry difficulty is SD 19 to 24.

**Medium risk, worth handling carefully:** `/blog/meeting-knowledge-management` already exists (90
impressions, position 7.5, which is a good position). PKM is *personal and individual*; that post is
*organizational*. Keep "personal knowledge management", "PKM" and "second brain" phrasing in A1 and
A2 only, and leave the organizational framing where it already ranks. Cross-link rather than overlap.

**One product constraint to respect in the copy.** Ask Lynkk answers only from your own notes. Do not
write A1 or A2 in a way that implies a shared team brain, because that is Workspaces territory and
the feature page is explicit about the limit.

---

## Slack: not viable as an SEO target

The volume is there and it is the wrong volume.

| Keyword | Vol | SD | Problem |
|---|---|---|---|
| what is slack bot | **18,100** | 48 | people asking what Slack's own Slackbot is |
| slack bot | **8,100** | 57 | mostly developers building one |
| slack bot ai | 880 | 58 | same |
| slack bot token | 720 | 29 | developer setup |
| slack bot create / how to create | 1,110 | 37 to 46 | developer tutorials |
| slack ai assistant | 140 | 53 | $32.68 CPC but SD 53 |
| best slack bot | 40 | **16** | the only soft commercial term |
| slack bot knowledge base | **0** | n/a | the Lynkk-relevant phrasing |
| slack bot answer questions | 10 | 5 | the Lynkk-relevant phrasing |

**The pattern:** this cluster is `token`, `python`, `api`, `oauth`, `webhook`, `bolt`, `github`,
`how to build`. It is engineers building Slack apps, plus a very large block of people who typed
"what is slack bot" because Slackbot messaged them. Neither buys a meeting assistant.

The two keywords that actually describe Lynkk for Slack, `slack bot knowledge base` and `slack bot
answer questions`, carry **0 and 10** searches respectively.

**Recommendation: no blog post.** Keep `/slack` as a product page, and get Lynkk listed in the Slack
App Directory, which is where this category's discovery actually happens. If you want one keyword
from this space, `best slack bot` at 40 searches and SD 16 is the only soft one, and it is too small
to justify a post on its own. It belongs as a section inside something else.

---

## Workspaces: the emotional hook has no search volume

This is the most interesting negative result in the whole programme, so I want to be precise about it.

**The angle the product page leads with returns nothing:**

| Seed | Volume |
|---|---|
| can my employer see my notes | **0** |
| employee privacy at work | **0** |

"Can my boss read my notes?" is a genuinely good piece of positioning and nobody searches it. That
does not make it useless, it makes it a product-page and AI-answer asset rather than an SEO one.

**What does have volume is SCIM, and it is the wrong audience:**

| Keyword | Vol | SD | CPC |
|---|---|---|---|
| scim provisioning | **2,400** | 49 | **$32.52** |
| what is scim provisioning | 590 | 45 | $20.06 |
| okta scim provisioning | 480 | **30** | $18.43 |
| scim provisioning meaning | 110 | 40 | n/a |
| entra scim provisioning | 40 | **17** | $21.62 |
| scim provisioning vs sso | 10 | **12** | $15.74 |

About 3,700 searches at SD 12 to 49 with $15 to $32 CPCs. But read the cluster: `okta`, `azure ad`,
`entra`, `terraform`, `attribute mapping`, `nested groups`, `quarantined`, `logs`. These are IT
administrators configuring an identity provider. They are not choosing a notetaker, and a Lynkk post
on SCIM would rank, if it ranked, for people who will never convert.

There is also a scale mismatch worth naming: Workspaces caps at **10 people**, and SCIM searchers are
typically provisioning hundreds. The feature supports SCIM, but the SCIM audience is not the
Workspaces audience.

**Recommendation: no blog post for Workspaces either.** One narrow exception if you want it:

| # | Title | Vol | SD | Risk |
|---|---|---|---|---|
| W1 | SCIM vs SSO: What Each One Actually Does | 600 | **12** | None |

`scim provisioning vs sso` (SD 12), `sso and scim provisioning` (SD 17), `jit vs scim provisioning`,
`what is scim provisioning` (590 at SD 45) as the volume anchor. It is a definitional explainer at
very low difficulty, it pairs with the SSO and SCIM enterprise post already on your list from an
earlier round, and it is honest coverage rather than a stretch. But it is an IT-reader page, not a
buyer page, and I would put it behind everything in the Ask Lynkk section.

---

## Summary

| # | Title | Vol | SD | CPC | Risk |
|---|---|---|---|---|---|
| A1 | Personal Knowledge Management: Systems, Tools and What Sticks | **2,500** | **20** | $4.19 | Medium |
| W1 | SCIM vs SSO: What Each One Actually Does | 600 | **12** | $15.74 | None |
| A2 | Best Second Brain Apps: 8 Compared | 360 | **19** | $14.86 | Low |

**Three topics, 3,460 US monthly searches.** Two of the four features you named do not support a blog
topic, and I would rather report that than manufacture one.

### What I would do

1. **A1, Personal Knowledge Management** (2,500, SD 20). The only substantial cluster across these
   features, and Ask Lynkk's source-linked answers are a real differentiator inside a category where
   most tools just store notes.
2. **A2, Best Second Brain Apps** (360, SD 19). Small, cheap, same audience, natural internal link
   from A1.
3. **W1, SCIM vs SSO** (600, SD 12) only if you want the coverage. Low difficulty, wrong reader.

### What I am recommending against, and why

- **No Slack post.** The 18,100-search head term is people asking what Slackbot is, and the rest is
  developers. The phrasing that describes your actual feature has 0 to 10 searches. Slack App
  Directory listing beats a blog post here.
- **No Workspaces post.** "Can my boss read my notes" has zero volume, and the SCIM volume that does
  exist belongs to IT admins provisioning hundreds of seats, while Workspaces caps at ten.
- **Nothing on `/features/spotter` beyond what I already sent** in `lynkk-spotter-and-integration-topics.md`
  (objection handling 3,400 at SD 16 with a $102 CPC, and the AI interview assistant cluster with its
  caveat).

Standing caveat: Ubersuggest difficulty estimates, not live SERP checks. A1 is the one worth
verifying, since PKM SERPs are dominated by Notion, Obsidian and Tiago Forte's audience and the SD 20
score may be optimistic.
