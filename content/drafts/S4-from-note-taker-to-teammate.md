---
platform: LinkedIn or lynkk.ai blog (NOT Substack as planned)
status: draft v1, needs human edit
format: POV essay
thematic_keywords: ["ai agents for business" (1,000, SD 36, CPC $39.35), "live ai meeting assistant" (170), "ai meeting assistant" (4,400)]
word_count: ~1,150
constraint: |
  Spotter is IN DEVELOPMENT with early access on Pro. This draft never describes it as shipped.
  Keep that discipline in any edit.
---

# From Note Taker to Teammate: What Changes When the AI Speaks

*By [name], [role] at Lynkk*

---

Everything in the AI meeting category so far has been retrospective. The software listens, the
meeting ends, the software writes something. It is a stenographer with good judgment.

The next step is already visible, and it is a different thing entirely: software that participates
while the conversation is happening. Not transcribing it, intervening in it. Surfacing the number
somebody is trying to remember, pulling up what this customer was quoted four months ago, answering
a question the person on the call cannot answer.

I work on a product building toward this, so read accordingly. But I think the interesting part is
not whether it is technically possible. It is what it does to the social contract of a meeting, and
that part is being discussed almost nowhere.

## Three things that break the moment the AI is live

**Latency stops being a performance metric and becomes a social one.** A summary that takes thirty
seconds is fine. An answer that takes six seconds is unusable, because a conversation has a rhythm
and six seconds of silence while you wait for your assistant is a visible failure in front of a
customer. The engineering target is not "fast", it is "inside the window where a human pause is
still natural", and that window is about two seconds. This is a much harder constraint than
anything in the post-meeting world, and it is why most of the category has stayed retrospective.

**Being wrong gets expensive immediately.** A post-call summary that misstates a number gets caught
when somebody reads it. A live assistant that whispers the wrong price while you are mid-sentence
gets repeated out loud to a customer by a person who trusted it. The error does not sit in a
document waiting to be found, it goes straight into the conversation. That changes what confidence
threshold is acceptable, and it means the right behaviour is often to say nothing.

**The other side has a legitimate interest in knowing.** This is the one I keep coming back to. If
I am negotiating with you and you have a system feeding you my own previous statements in real time,
something has changed about the negotiation, and you not telling me is a choice you have made.

## The etiquette question nobody has answered

We have rough norms for recording. You say you are recording, the other person says fine, everyone
proceeds. Thin, but it exists.

We have no norms at all for live assistance. Is it like notes you prepared beforehand, which nobody
expects you to disclose? Is it like having a colleague silently messaging you during the call, which
most people would consider fine? Is it like having the customer's own words searchable and
retrievable instantly, which starts to feel like something else?

I do not think there is a clean answer, and I am suspicious of anyone who offers one confidently.
But a few design positions seem clearly right, and they are worth stating because they are the kind
of thing that gets decided by default if nobody argues for them:

**It should never be hidden from a screen share.** If the assistant disappears when you share your
screen, the product is designed around concealment, and that tells you what it is for. Lynkk's
Spotter is built so it is never hidden from a screen share, and I think that is the single most
important design decision in the whole feature.

**It should read, not watch.** Taking the screen as text rather than as an image is a meaningful
privacy difference, and it limits what the system can hoover up incidentally.

**It should be visibly the seller's tool, not a hidden advantage.** The honest framing is "I have
my notes open", not "I have an oracle".

## What it is actually good for, and it is not what you would guess

The instinctive use case is the one that makes everybody uncomfortable: real-time coaching on how
to handle an objection, a script whispered in your ear. I think that is both the least useful
application and the one that will give the category a bad name.

The genuinely valuable use is duller and much more defensible: **retrieval of things that were
actually said.** What did we quote them in March. What did they say their timeline was. Which
version of the rollout plan did we agree. Did we ever send the security document.

Those are questions with correct answers that exist in the record, and a human cannot retrieve them
mid-sentence. That is a real capability gap, and closing it does not require the system to have
opinions about the customer. It just has to be able to find the sentence and show you where it came
from.

The distinction matters: retrieval with a citation is help. Advice without one is a liability
pointed at your own customer relationship.

## The uncomfortable second-order effect

If live assistance works, it degrades the value of preparation, and preparation is currently how
good sellers distinguish themselves.

Today, the rep who reviewed the account history before the call is visibly better in the call than
the one who did not. If the system supplies that history on demand, that gap narrows. Mostly this is
good, and it is the usual story of a tool compressing a skill. But it is worth being honest that
"you no longer need to remember your customer" is a strange thing to sell to someone whose job is
relationships, and that some of what looks like preparation was actually attention, which does not
survive being outsourced.

I do not know how that resolves. I suspect the people who stay good will be the ones who use the
retrieval to ask better questions, rather than to avoid doing the reading.

## Where this is, honestly

Not shipped. Lynkk's Spotter is **in development**, with early access on the Mac app by request on
the Pro plan. I am writing about a direction, not a product you can buy today, and I would be
sceptical of anyone in this category who claims this problem is solved. The latency and
false-confidence constraints above are not small.

What I am fairly confident about is the direction. Post-meeting summaries were never the
destination, they were the easiest thing to build first. The interesting question was always whether
software could be useful during the conversation rather than after it, and whether we can build
that in a way that does not quietly make meetings adversarial.

The second half of that sentence is the actual work.

---

## Publishing notes

**Not for Substack** as part of an SEO programme. **Recommended home:** LinkedIn, then the
lynkk.ai blog.

**Required before publishing:**
1. **Spotter must not be described as shipped.** This draft says "in development, early access by
   request on Pro". Keep that wording in any edit. If GA lands first, update rather than imply.
2. Human edit and a real byline. This is an opinion piece and needs an owner.
3. Check the "never hidden from a screen share" and "reads the screen as text, never sent as an
   image" claims against the current build before publishing. Both are from the live site today.
