# Publishing on Medium: meeting notes article

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
5. Scroll once to check that the template shows as a grey code block and the
   "typical version" example shows as a quote.

## 2. Add the top image

Medium uses the first image as the preview thumbnail in feeds and on social
shares, so add it before publishing.

- **File:** `hero-meeting-notes-that-turn-into-action.png` (3200x1800, 16:9),
  built in the Lynkk post kit (Grid design system, `wide` size, split layout),
  with the Lynkk logo bar and lynkk.ai footer hidden so the image carries no
  branding. `hero-meeting-notes-that-turn-into-action.kit.html` is its source:
  copy it to `lynkk-post-kit/posts/<name>/post.html` and run
  `node scripts/render.mjs posts/<name>` to change and re-render it.
- **Where:** click the empty line directly under the subtitle, click **+**, then
  the image icon, and upload the file.
- **Alt text** (click the image, then "Alt text"): `Banner. Headline: Write down what happens next. Let the rest go. Below it: Notes that someone who missed the meeting can act on in two minutes. On the right, a notes card titled Q4 pricing review lists one decision, Keep the free tier, then three action items with owners and days: Priya Thu, Sam Fri, Ana Wed.`
- **Caption** (type under the image): `Decisions and owners first, everything else optional. (Made with AI assistance.)`

## 3. Story settings

Open **...** (top right) then **Story settings**, or fill these in on the
publish screen.

| Setting | Value |
|---|---|
| Preview title | How to Take Meeting Notes That Actually Turn Into Action |
| Preview subtitle | Stop recording what people said. Capture decisions, owners and deadlines, and hand the rest to software. |
| SEO title (47 chars) | How to Take Meeting Notes That Turn Into Action |
| SEO description (144 chars) | A simple meeting notes format built on decisions, owners and deadlines, plus a practical rule for which parts to automate with AI meeting tools. |
| Custom URL slug | meeting-notes-that-turn-into-action |
| Tags (max 5) | Productivity, Meetings, Management, Leadership, Work |
| Canonical link | Leave empty unless this is also published on lynkk.ai first. If it is, set "This story was originally published elsewhere" to that URL. |
| Reading time | About 6 minutes |

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
- [ ] Click each of the 6 links once (4 sources, 2 to lynkk.ai). They were
      confirmed through search results, not opened directly.
- [ ] Title and subtitle look right in the preview card.
- [ ] Top image is uploaded under the subtitle, with alt text and caption.
- [ ] Author bio on the Medium profile mentions Lynkk (the story only has one
      closing line about it).
- [ ] Optional: submit to a Medium publication about productivity or
      management instead of publishing to your profile. Publications reach more
      readers, but each has its own submission rules and review time.

Publishing is a manual step. Nothing has been posted to Medium.
