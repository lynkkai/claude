# Lynkk Substack

Launch series of 4 posts for the Lynkk Substack, written with the `substack-article` skill
(`.claude/skills/substack-article/`). Research and sources behind the approach:
`.claude/skills/substack-article/references/substack-playbook.md`.

## The series

The four posts follow the meeting lifecycle, so together they explain Lynkk's positioning without
any of them being an ad.

| # | Post | Stage | Primary reader | Search keyword |
|---|---|---|---|---|
| 1 | [Your AI notetaker shows up too late](articles/01-your-ai-notetaker-shows-up-too-late.md) | Thesis: before / during / after | Team leads and founders already using a notetaker | ai meeting notes |
| 2 | [Stop opening meetings with "remind me where we landed"](articles/02-stop-opening-meetings-with-remind-me.md) | Before | AEs and CSMs with back-to-back customer calls | how to prepare for a meeting |
| 3 | [The meeting ended. The work didn't.](articles/03-the-meeting-ended-the-work-didnt.md) | After | Sales and product leads whose follow-ups slip | meeting follow up |
| 4 | [Ask these 7 questions before an AI joins your meeting](articles/04-ask-these-questions-before-an-ai-joins.md) | Trust | Ops / IT / team leads choosing a tool | ai note taker for in person meetings |

## Suggested schedule

One post a week, same weekday and time (Tuesday or Wednesday morning in your main audience's
time zone is a safe default). Publish in order: post 1 sets up the frame the others refer to,
and post 3 ends with a teaser for post 4.

| Week | Post | Notes to post that week |
|---|---|---|
| 1 | #1 | The 3 promo Notes at the bottom of the post, spread over days 1, 3, 5 |
| 2 | #2 | Its 3 promo Notes + restack #1 once |
| 3 | #3 | Its 3 promo Notes |
| 4 | #4 | Its 3 promo Notes + a "series recap" Note linking all four |

Beyond the scheduled Notes, aim for 1-3 short Notes a day and thoughtful comments on other
productivity, sales, and future-of-work publications. That is where most new readers come from.

## Paste-ready pages

`substack/paste-ready/` has one page per post (built so far: posts 1 and 2). Open it in a browser:
it has copy buttons for every Substack field, a **Copy article** button for the clean body (rich
text, so headers, links and lists survive the paste), where to drop the Subscribe/Share buttons,
and the promo Notes. Rebuild after editing a post:

```
python3 substack/build_paste_ready.py substack/articles/<post>.md
```

## Before you hit publish (each post)

- [ ] Byline set to a real person (founder or team lead). Founder voice outperforms a logo.
- [ ] Paste from a **rendered** view of the file (open it on GitHub, copy the rendered text),
      not raw Markdown. Delete the front-matter block; it's for you, not readers.
- [ ] Replace `[Subscribe button]` / `[Share button]` markers with Substack buttons
      (Editor toolbar > Button).
- [ ] Turn the `>` quote in the body into a Substack **Pull quote** block.
- [ ] Copy `seo_title`, `seo_description`, `slug` into Settings > SEO.
- [ ] Upload a social preview image (brief is in `social_image`).
- [ ] Set the section (`section` field). Create sections "Meeting Craft", "Follow-through",
      "Trust" once.
- [ ] If the publication has enough subscribers for title A/B testing, use `title` vs `title_b`.
- [ ] Post 4 only: resolve the `todo` in its front matter first.
- [ ] Send a test email to yourself and check it on a phone.

## Still open (from `memory/lynkk-brand.md`)

None of the posts state pricing, supported meeting platforms, specific CRMs, number of languages,
data regions, or certifications, because those aren't confirmed yet. Once they are, post 4's
"Where Lynkk fits" section is the natural place to add certifications and training policy.
