# How to draft a reply

Drafts are for a person to read, edit and post by hand. This tool never posts,
comments or messages anyone on Reddit, and you must not try to.

## Steps

1. `uv run leads draft <id>` writes `drafts/<id>.md` with the conversation.
2. Read it. If the subreddit's rules matter (many ban self-promotion), say so
   at the top of the draft and keep the product out unless asked.
3. Write the reply under `## Draft reply`. Then add `## Notes for the poster`:
   what to check in the thread before posting, and any claim you left out
   because `docs/LYNKK.md` doesn't support it.

## The reply

- Answer their actual question or problem first, in the first two sentences.
  Practical help that is useful even if they never try Lynkk.
- Conversational and short: usually 60 to 150 words. Reddit tone, no
  marketing voice, no headings, no bullet lists unless they asked for a list
  of options.
- Mention Lynkk only when it genuinely fits their need, once, and disclose
  the connection plainly: "I work on Lynkk, so I'm biased, but..." Never
  pretend to be a neutral user or a happy customer.
- Never invent personal experience ("I've used it for a year", "my team
  loves it"). The poster writes as someone who works on Lynkk.
- Every Lynkk fact comes from `docs/LYNKK.md`. No prices, no accuracy numbers,
  no "best", no claims about other products beyond what the thread says.
- If Lynkk doesn't fit (they need Windows, a phone app, file uploads), say
  so honestly or don't mention it. A helpful reply with no product is fine.
- No links unless they asked where to find it; then one link to lynkk.ai.
- Plain prose. No em dashes. No "not just X but Y", no "game changer", no
  emoji strings, no "Great question!".

## Example

Post: "I take notes by hand on client calls and I'm always behind. Is there
something that records Zoom calls and writes notes with action items? I'd
rather not have a bot join, clients find it weird."

Draft:

> Two things helped people I know: agree the action items out loud in the
> last two minutes of the call, and write them down right after, before the
> next call starts. That fixes most of the "always behind" problem.
>
> For the recording side, I work on Lynkk so take this with that in mind: the
> Mac app notices a Zoom call and records it from your Mac, so no bot joins.
> You get a transcript and notes with action items afterwards. It's Apple
> silicon Macs only, so it won't help if you're on Windows.
