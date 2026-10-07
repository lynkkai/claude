# How to classify a batch

You are reviewing Reddit posts and comments to find people Lynkk (an AI
meeting assistant, see `docs/LYNKK.md`) could genuinely help. The goal is a
short list of useful conversations, not a long list of keyword matches. Be
strict: ten real opportunities beat a hundred weak ones.

## What we are looking for

Two kinds of people, in this order:

1. **Someone asking for an AI note maker or note taker**, or for suggestions
   between them: "What AI note taker do you use?", "Any good AI note maker for
   my calls?", "Otter alternative?"
2. **Someone asking about AI dictation**: talking instead of typing, voice
   typing that lands in any app, "Wispr Flow alternative?", "Mac dictation
   is bad, what do you use?" Lynkk's Mac app does dictation (see
   "Dictation" in `docs/LYNKK.md`).

Everything else (general AI talk, meeting rants, transcription jobs, people
who already have a tool and want something else) ranks below these.

## Input and output

`uv run leads review next` writes `work/batch.json`. Read it with the Read
tool (it is sized to fit in one read; don't use scripts to inspect it). For **every**
item in `items`, write one line of JSON to `work/batch.results.jsonl` (one
object per line, no array, no commentary) with the Write tool, then run
`uv run leads review apply`.
If apply reports errors, fix only those lines and run apply again.

```json
{"id": "t3_abc123", "relevance_score": 88, "intent": "high_purchase_intent", "intent_score": 90, "pain_point": "Takes notes by hand on client calls and can't keep up.", "context": "Freelance consultant, two clients on Zoom, needs notes both clients can see.", "potential_use_case": "Recording client calls without a bot and getting notes with action items.", "reply_opportunity": "Asks directly for an AI note taker for Zoom calls.", "is_promotional": false}
```

All nine fields are required. Scores are whole numbers from 0 to 100. Text
fields are one plain sentence each (empty string if there is nothing to say).
Write in plain English. No em dashes.

## What each item gives you

`type`, `subreddit`, `title` (posts), `content`, `matched_keywords`, and for
comments `parent_post_title` and `parent_post_excerpt`. `rule_score` and
`rule_signals` come from a keyword scorer: use them as hints, not answers.
The scorer is often wrong about context, promotion and sarcasm. You are the
judgement.

## intent (pick one)

| intent | when |
|---|---|
| `high_purchase_intent` | Explicitly wants an AI note maker, note taker, meeting assistant or AI dictation tool now. "What AI note taker should I use?", "Need something that records my calls and writes notes.", "I need a dictation app for my Mac." |
| `tool_recommendation` | Asks for recommendations or suggestions in the space, less urgent or less specific. "What do you all use for meeting notes?", "Any AI note maker suggestions?", "What dictation app do you use?" |
| `comparison` | Evaluating named tools, or asking for an alternative to one. "X vs Y?", "Alternative to X? It got too expensive.", "Wispr Flow vs Superwhisper?" |
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
  welcome: asks for AI note maker or note taker suggestions, asks for an AI
  dictation or voice typing tool on a Mac, call notes, meeting summaries,
  action items, transcription of calls, searchable meeting history, accents
  or Hindi/Hinglish, no bot in the call.
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
  HIPAA or SOC 2 requirements). Say so in `reply_opportunity`. For an "AI
  note maker" that turns PDFs, YouTube videos or existing recordings into
  notes, Lynkk doesn't fit (no file upload). For dictation, Lynkk is the Mac
  app only: dictation on a phone, Windows or an Intel Mac doesn't fit.
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

Never invent facts about the person. If the text doesn't say it, don't write it.
