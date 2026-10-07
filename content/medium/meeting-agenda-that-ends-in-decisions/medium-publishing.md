# Publishing on Medium: meeting agenda article

Source of truth: `article.md`. Paste-ready version: `medium.html` (regenerate
after any edit with
`python3 -I .claude/skills/create-medium-article/scripts/to_medium_html.py article.md medium.html`).

## 1. Paste the story

1. Open `medium.html` in a browser.
2. Select all (Ctrl+A / Cmd+A) and copy.
3. On Medium, click **Write** and paste into the empty story.
4. Check the top two lines: the title should be the large heading and the
   subtitle the small grey heading directly under it. If the subtitle came in as
   normal text, select it and click the small **T** in the formatting bar.
5. Scroll once to check that the sample agenda shows as a grey code block.

## 2. Add the top image

- **File:** `hero-meeting-agenda-that-ends-in-decisions.png` (3200x1800, 16:9),
  built in the Lynkk post kit (Grid design system, `wide` size, split layout),
  with the Lynkk logo bar and lynkk.ai footer hidden so the image carries no
  branding.
  `hero-meeting-agenda-that-ends-in-decisions.kit.html` is its source: copy it to
  `lynkk-post-kit/posts/<name>/post.html` and run `node scripts/render.mjs
  posts/<name>` to change and re-render it.
- **Where:** click the empty line directly under the subtitle, click **+**, then
  the image icon, and upload the file.
- **Alt text:** `Banner. Headline: A topic never ends. A question does.
  Below it: Write each agenda item as a question. Start with what last week left
  open. On the right, an agenda card titled Thursday sync, 30 min, lists Open from
  last week (2 items, checked), then three questions marked Decide, Input and
  Inform.`
- **Caption:** `An agenda written as questions, with last week's open items first.
  (Made with AI assistance.)`

## 3. Story settings

| Setting | Value |
|---|---|
| Preview title | How to Write a Meeting Agenda That Ends in Decisions |
| Preview subtitle | Turn every agenda item into a question the meeting has to answer, and start with what the last meeting left open. |
| SEO title (52 chars) | How to Write a Meeting Agenda That Ends in Decisions |
| SEO description (143 chars) | How to write a meeting agenda that ends in decisions: turn each item into a question, label it, and reuse a simple team meeting agenda example. |
| Custom URL slug | meeting-agenda-that-ends-in-decisions |
| Tags (max 5) | Meetings, Productivity, Management, Leadership, Teamwork |
| Canonical link | Leave empty unless this is also published on lynkk.ai first. |
| Reading time | About 5 minutes |

## 4. Before you click Publish

- [ ] **AI disclosure (Medium policy):** the italic disclosure line under the
      subtitle must stay within the first two paragraphs. Without it Medium limits
      the story to your own followers. Read, fact-check and edit the story yourself
      before publishing so the line is true.
- [ ] **Paywall:** Medium does not allow AI-generated writing in the Partner
      Program paywall. Publish it unlocked unless the story has been substantially
      rewritten by a person.
- [ ] **Image caption** keeps the AI-assistance note, which Medium requires for
      AI-made images.
- [ ] Click each of the 5 links once (3 sources, 2 to lynkk.ai). The sources were
      confirmed through search results, not opened directly.
- [ ] If the meeting notes article is already live, add a link to it in the
      "Start with what the last meeting left open" section, where the text says
      "a good reason to take notes that way."
- [ ] Title and subtitle look right in the preview card.
- [ ] Top image is uploaded under the subtitle, with alt text and caption.
- [ ] Optional: submit to a Medium publication about management or productivity.

Publishing is a manual step. Nothing has been posted to Medium.
