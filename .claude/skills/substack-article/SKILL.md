---
name: substack-article
description: Write a publish-ready Substack post for the Lynkk publication (title, subtitle, SEO fields, body, CTA, and promo Notes). Use whenever the user asks for a Substack article, newsletter post, essay, or series for Lynkk, or wants to plan, outline, edit, or repurpose content for the Lynkk Substack.
---

# Substack article skill (Lynkk publication)

Produces Substack posts that read like editorial, not ads, and still move readers toward Lynkk.
Research behind every rule here, with sources: `references/substack-playbook.md`.
Product facts: `lynkk-post-kit/docs/TRUTHS.md` (wins over `memory/lynkk-brand.md`).
House writing rules: `CLAUDE.md`. Any image for a post (banner, social preview, inline
graphic): use the `lynkk-post-kit` skill, never a hand-made design.

## Non-negotiables

1. **No em dashes (—) or en dashes (–). Anywhere.** Not in titles, body, Notes, or metadata.
   Use a comma, colon, parentheses, or a new sentence. Run the dash check in step 7.
2. **Brand spelling:** Lynkk, lynkk.ai. Never Lynk / Linnk / Link AI.
3. **Only claim what `lynkk-post-kit/docs/TRUTHS.md` says.** Its "Don't claim" list is a hard
   rule: no AI that speaks or answers during the call, no CRM, no automatic Jira (Send is manual),
   no regions or data residency, no certifications, no knowledge-graph screen, no "30 seconds",
   no "offline-first", no phone apps, no prices, no competitor names. If a post needs something
   not in TRUTHS.md, leave a `TODO:` and ask the team.
4. **Every statistic has a named primary source and a link.** Prefer the original study
   (Microsoft, Atlassian, Salesforce, academic papers) over vendor blogs that re-quote it.
   If you cannot trace a number to its origin, cut it. Never invent quotes, customers, or results.
5. **80/20 rule.** At least 80% of the post must be useful to someone who never signs up.
   Lynkk appears in at most one dedicated section (usually the last third) plus the closing CTA.

## Workflow

### 1. Pin the brief
Before drafting, write down (in the post's front-matter block):
- **Reader:** one specific person (e.g. "AE at a 50-person SaaS company with 6 calls a day").
- **Promise:** finish the sentence "After reading this, you will be able to ___."
- **Stage:** which part of the meeting lifecycle it serves (before / during / after / trust).
- **Search keyword (optional):** one phrase from the keyword list in the playbook, used naturally
  in the SEO title, slug, and once in the first 150 words. Never stuff.

### 2. Pick an angle with a point of view
Substack rewards a mind, not a feature list. Each post needs a claim a reasonable person could
disagree with ("Your AI notetaker shows up too late"), then earns it with evidence and examples.
Pillars that fit Lynkk: meeting lifecycle thinking, follow-up and execution, preparation and
context, in-person and multilingual work, privacy and trust, sales and product team workflows.

### 3. Title, subtitle, email subject
- **Title:** 30-60 characters, about 6-10 words. Specific beats clever. First-person, story, or
  "mistake / stop / wrong" framing tends to outperform neutral how-to titles on Substack.
- **Subtitle:** one sentence, under ~120 characters. It is the email preview text, so it must add
  new information, not repeat the title.
- Write **3 title options** and mark one primary. Substack can A/B test titles for publications
  with enough subscribers; list the runner-up as the B variant.

### 4. Structure (default anatomy)
```
Hook (2-4 short paragraphs): a scene, a sharp observation, or a surprising number.
The problem, made concrete: what it costs, with 1-3 sourced stats.
The reframe / core idea: the post's claim, stated plainly in one line (bold or pull quote).
The how: 3-6 sections with H2/H3 headers, each with an example, step, or template.
Where Lynkk fits (optional, max one section, ~10-15% of length): how we approach it, not a pitch.
Close: one-line takeaway + one ask (reply, comment, subscribe, or try Lynkk). One primary ask.
```
Length: 1,000-1,800 words for a standard post. Under 1,000 is fine for a sharp opinion piece.
Over ~2,500 risks the email being clipped in Gmail; split into a series instead.

### 5. Write for the inbox and the phone
- Paragraphs of 1-3 sentences. One idea per paragraph.
- A header every 200-350 words so skimmers can follow the argument from headers alone.
- Use bullets for lists of 3+ parallel items, numbered lists for sequences.
- One pull quote per post (Substack "Pull quote" block): the most shareable line.
- Second person ("you") for advice, first person plural ("we") for Lynkk's own view.
- Concrete over abstract: name the meeting, the role, the tool, the minute.
- Link sources inline on the claim itself, not in a bibliography dump.
- Place a **[Subscribe button]** after the hook or at the midpoint and a **[Share button]** near
  the end (insert via Substack's Buttons menu; mark the spots in the draft).

### 6. Package for Substack
Every post file starts with this block (the publisher copies fields into Substack settings):

```
---
title: <primary title>
title_b: <A/B variant>
subtitle: <email preview line>
seo_title: <<=60 chars, may end with "| Lynkk">
seo_description: <<=155 chars, adds context the title lacks>
slug: <short-keyword-slug>
section: <Substack section, e.g. "Meeting Craft">
tags: [..]
reader: <the one reader>
promise: <the promise>
keyword: <optional search keyword>
social_image: <one-line brief for the preview image, 1456x816 or similar 16:9>
cta: <the one primary ask>
---
```
Then the body. Then a `## Promo Notes` section with **3 Substack Notes** to post over the
following days: one short line (<100 chars), one micro-story or stat (50-100 words), one
list-style Note. Each must stand alone without the article and must not use dashes.

### 7. Quality gate (run before saying it is done)
- [ ] `LC_ALL=C.UTF-8 grep -nP '[\x{2013}\x{2014}]' <file>` returns nothing (no en/em dashes).
- [ ] "Lynkk" spelled correctly everywhere; no Lynk/Linnk/Link AI.
- [ ] Every number has an inline link to its source; every Lynkk claim is in TRUTHS.md.
- [ ] Banner/social image made with the `lynkk-post-kit` skill (`posts/substack-<nn>-banner`).
- [ ] Hook works without the title; first 2 lines give a reason to keep reading.
- [ ] Headers alone tell the story.
- [ ] Lynkk mentions are under ~20% of the post; the post is useful without them.
- [ ] Exactly one primary CTA.
- [ ] SEO title <= 60 chars, SEO description <= 155 chars, subtitle <= ~120 chars.
- [ ] Read it as the named reader: is there anything they'd skim past? Cut it.

## Publishing notes (for the human)
- Build a paste-ready page: `python3 substack/build_paste_ready.py substack/articles/<post>.md`
  (needs `pip install markdown`). It writes `substack/paste-ready/<post>.html` with copy buttons
  for every Substack field, the clean article body as rich text, button placements, and the Notes.
- Paste from a **rendered** view (e.g. the file on GitHub, or a Markdown preview), not raw
  Markdown: Substack's editor does not convert pasted `##` or `**` reliably.
- Set SEO title/description/slug under Settings > SEO in the post editor.
- Upload the social preview image under Settings > Social preview.
- Cadence: one post a week, same day and time, plus 1-3 Notes a day. Consistency compounds.
- After publishing: post the promo Notes, restack the post, reply to every comment in the first
  48 hours, and cross-post a short version to LinkedIn and X linking back to the post.
