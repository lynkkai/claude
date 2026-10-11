# How to classify a batch

You are reviewing Reddit posts and comments to find people Lynkk (an AI
meeting assistant with Mac dictation, see `docs/LYNKK.md`) could genuinely help. The goal is a
short list of useful conversations, not a long list of keyword matches. Be
strict: ten real opportunities beat a hundred weak ones.

## Input and output

`uv run leads review next` writes `work/batch.json`. Read it with the Read
tool (it is sized to fit in one read; don't use scripts to inspect it). For **every**
item in `items`, write one line of JSON to `work/batch.results.jsonl` (one
object per line, no array, no commentary) with the Write tool, then run
`uv run leads review apply`.
If apply reports errors, fix only those lines and run apply again.

```json
{"id": "t3_abc123", "relevance_score": 88, "intent": "high_purchase_intent", "intent_score": 90, "pain_point": "Takes notes by hand on client calls and can't keep up.", "context": "Freelance consultant, two clients on Zoom, needs notes both clients can see.", "potential_use_case": "Recording client calls without a bot and getting notes with action items.", "reply_opportunity": "Asks directly for an AI note taker for Zoom calls.", "is_promotional": false, "brand_mention": "only_if_asked", "guidelines_note": "Rule 3 bans self-promotion, but the poster asked for tools and others in the thread name theirs.", "recommended_reply": "If clients find a bot odd, record from your own machine instead..."}
```

All twelve fields are required. Scores are whole numbers from 0 to 100. Text
fields are one plain sentence each (empty string if there is nothing to say).
Write in plain English. No em dashes.

## What each item gives you

`subreddit_rules` at the top of the batch: one summary per subreddit,
starting with a tag (`[self-promotion restricted]`, `[no self-promotion rule
found]`, `[rules unavailable ...]` or `[rules not fetched yet]`) and listing
promotion rules first.

For each item: `type`, `subreddit`, `title` (posts), `content`, `matched_keywords`, and for
comments `parent_post_title` and `parent_post_excerpt`. `rule_score` and
`rule_signals` come from a keyword scorer: use them as hints, not answers.
The scorer is often wrong about context, promotion and sarcasm. You are the
judgement.

## intent (pick one)

| intent | when |
|---|---|
| `high_purchase_intent` | Explicitly wants an AI note taker, meeting notes tool, transcription or meeting assistant now. "What AI note taker should I use?", "Need something that records my calls and writes notes." |
| `tool_recommendation` | Asks for recommendations in the space, less urgent or less specific. "What do you all use for meeting notes?" |
| `comparison` | Evaluating named tools, or asking for an alternative to one. "X vs Y?", "Alternative to X? It got too expensive." |
| `problem_seeking_solution` | Describes a pain Lynkk solves and wants a fix, without asking for a tool by name. "I keep forgetting action items from calls, how do you handle it?" |
| `workflow_problem` | Describes a meeting or note workflow pain, not clearly looking for a tool. |
| `general_discussion` | Talks about AI notes, meetings or transcription with no need. Opinions, news, polls. |
| `low_relevance` | Not about meeting notes at all, or the keyword is incidental (music notes, patch notes, WhatsApp voice notes, a lecture with no recording angle). |

## intent_score

How strong and current the need is. 90+ asking right now with a clear use
case; 70 to 89 clear need; 40 to 69 some need; below 40 little or none.

## relevance_score

How worth a human reply this is, for Lynkk specifically.

- 85 to 100: asks for exactly what Lynkk does, and a helpful reply would be
  welcome (call notes, meeting summaries, action items, transcription of
  calls, searchable meeting history, accents or Hindi/Hinglish, no bot in the
  call, Mac).
- 65 to 84: a real need in the space; a reply could help.
- 50 to 64: on topic, weak or vague need.
- Below 50: not worth a reply. This is the cut line; most items should land
  here.

Push the score **down** when:
- the author is promoting their own product, launching, asking for beta
  testers, or it's a "best tools I tested" listicle (`is_promotional: true`,
  relevance 0 to 20). They are competitors, not leads.
- the thread is old news, a rant with no question, or a joke.
- the need is something Lynkk can't do (see "Don't claim" in `docs/LYNKK.md`:
  phones, Windows, uploading existing audio files, a bot that speaks, CRM sync,
  HIPAA or SOC 2 requirements). Say so in `reply_opportunity`.
- a comment just recommends a tool to someone else. The person asking is the
  lead, not the recommender.
- the subreddit bans self-promotion and the only possible reply is a product
  mention. Note it in `reply_opportunity`.

## pain_point, context, potential_use_case, reply_opportunity

- `pain_point`: the person's actual problem in their terms. "Spends an hour
  after every client call writing up notes." Empty if there is none.
- `context`: what someone needs to know before replying: who they seem to be,
  the setting, constraints, tools already tried. For a comment, what the
  thread is about.
- `potential_use_case`: what Lynkk would do for them, only from
  `docs/LYNKK.md`. Empty if Lynkk doesn't fit.
- `reply_opportunity`: why reply, or why not ("Skip: author is the founder of
  a competing app.").

## Dictation

Lynkk's Mac app also does dictation (see "Dictation" in `docs/LYNKK.md`).
Someone asking for an AI dictation or speech to text app for the Mac is a
real lead (`high_purchase_intent` or `tool_recommendation`). Dictation on
phones, Windows, or transcribing existing audio files is not: say so in
`reply_opportunity` and score it below 50.

## brand_mention, guidelines_note, recommended_reply

Read the subreddit's rules in `subreddit_rules` before deciding.

`brand_mention` (pick one):

| value | when |
|---|---|
| `yes_with_disclosure` | No rule against self-promotion, and Lynkk genuinely fits. A reply may name Lynkk once, saying "I work on Lynkk". |
| `only_if_asked` | The rules limit promotion (a 10% rule, "no self-promotion" but recommendations allowed, vendors must disclose), and the poster asked for tools or alternatives. One disclosed mention, as an answer to their question. |
| `no` | The rules ban promotion or links outright, or only allow it in a megathread, or the poster didn't ask for tools, or Lynkk doesn't fit. Help without naming Lynkk. Also `no` for every item below 50. |
| `check_rules` | Rules are unavailable or not fetched. Write the reply without Lynkk; the person reads the sidebar first. |

When the rules allow it, also look at the thread itself: if other commenters
already recommend named tools, a disclosed mention is normal there; if the
thread is a rant or a discussion with no tool talk, lean to `no`.

- `guidelines_note`: one sentence on the rules that matter for a reply, citing
  the rule ("Rule 4: no self-promotion outside the weekly thread."). Empty if
  the item is below 50.
- `recommended_reply`: for items at 65 or above, a ready-to-edit reply that
  follows `docs/REPLY.md` exactly (answer first, 60 to 150 words, plain prose,
  disclosure, only `docs/LYNKK.md` facts, no links unless asked). Name Lynkk
  only when `brand_mention` is `yes_with_disclosure` or `only_if_asked`.
  Empty for items below 65. It is a draft: a person reads the thread, edits
  it and posts it by hand.

No em or en dashes in any text field: apply rejects lines that have them.

Never invent facts about the person. If the text doesn't say it, don't write it.
