# Publishing kit: Hashnode + Blogger + Medium

Everything needed to publish all three posts. Source drafts live in `content/*.md`; the files here
are generated from them with `python3 content/publish/build.py` (re-run it after any edit).

| File | Use |
|---|---|
| `hashnode-post.md` | Paste into the Hashnode editor body |
| `blogger-post.html` | Paste into Blogger's **HTML view** |
| `../images/hashnode-cover.png` | Hashnode cover (1600x840) |
| `../images/hashnode-pipeline.png` | Hashnode inline diagram (1600x560) |
| `../images/blogger-banner.png` | Blogger banner and thumbnail (1200x630) |
| `../images/blogger-action-item-anatomy.png` | Blogger inline graphic (1200x675) |
| `medium-post.html` | Open in a browser, copy, paste into the Medium editor |
| `../images/medium-banner.png` | Medium featured image (1400x788) |
| `../images/medium-before-after.png` | Medium inline before/after graphic (1400x760) |

Images follow Lynkk's visual identity as used on lynkk.ai: the three banners use the same layout,
logo tile, colors and type as Lynkk's own share image (lynkk.ai/opengraph-image); inline images use
the site's light/dark tokens, Inter, and sentence-case pills. Sources are HTML in `../images/src/`. To change wording, edit the HTML and run `bash content/images/render.sh`.

## Publish order

Publish **Blogger first**, then Hashnode, then Medium, then go back and fix the cross-links:

1. Publish Blogger with `HASHNODE_POST_URL` left in place.
2. Publish Hashnode, replacing `BLOGGER_POST_URL` with the live Blogger URL.
3. Edit the Blogger post: replace `HASHNODE_POST_URL` with the live Hashnode URL. Update.
4. Publish Medium with both live URLs already filled in (it links to both).

Space them out: one post per day or two looks natural and gives each its own social push.

## Blogger (step by step)

1. **New post** > switch the editor to **HTML view** (pencil icon dropdown, top left).
2. **Title field:** `Meeting Minutes Template With Action Items (Free) + Example`
3. Paste the contents of `blogger-post.html`.
4. **Images:** switch to **Compose view**, click the placeholder images (they'll show as broken),
   delete each one, then use **Insert image > Upload** at the same spot:
   - top of the post: `blogger-banner.png`
   - under "How to write action items that actually get done": `blogger-action-item-anatomy.png`
   After inserting, click each image > **Properties** and paste the alt text and title:
   - banner: `Free meeting minutes template with action items, filled-in example`
   - anatomy: `How to write action items: one owner, a verb, a clear task and a real due date`
   Set size to **Original size** or **X-Large**. The banner must stay the first image, because
   Blogger uses the first image as the post thumbnail and social preview.
5. **Post settings** (right sidebar):
   - Labels: `Meeting Minutes, Meeting Notes, Templates, Productivity`
   - Permalink: **Custom permalink** > `meeting-minutes-template-action-items`
   - Search description: `Free meeting minutes template with action items, plus a meeting notes template and a filled-in example. Copy it and learn how to write minutes in 6 steps.`
     (If this field is missing: Settings > Meta tags > enable search description.)
   - Options: allow reader comments.
6. **Preview**, check the tables and template blocks, then **Publish**.
7. Search Console: verify the blog (Blogger is Google-owned, so it's quick), submit `/sitemap.xml`,
   then URL Inspection > **Request indexing** for the post URL.

## Hashnode (step by step)

1. **Write** > new draft.
2. **Add cover** > upload `hashnode-cover.png`.
3. **Title:** `AI Meeting Notes From Any Transcript: The Prompt + a Jira Script`
4. **Add subtitle:** `A copy-paste prompt for ChatGPT, Claude and Copilot that turns a meeting transcript into minutes, decisions and action items, plus 40 lines of Python that file them in Jira.`
5. Paste the contents of `hashnode-post.md` into the body.
6. **Image:** find the line `![Pipeline from meeting transcript...](IMAGE_URL_hashnode-pipeline)`
   near the top, delete it, and upload `hashnode-pipeline.png` at that spot (drag and drop, or the
   image button). Keep the alt text:
   `Pipeline from meeting transcript to prompt, JSON minutes, Python script and Jira tickets`
7. **Draft settings / Publish panel:**
   - Tags (max 5): `ai`, `llm`, `productivity`, `python`, `jira`
   - Article slug: `ai-meeting-notes-transcript-prompt`
   - SEO title: `AI Meeting Notes: The Prompt to Summarize Any Transcript`
   - SEO description: `Get AI meeting notes from any transcript: one prompt for ChatGPT, Claude or Copilot that writes minutes and action items, plus a Python script for Jira.`
   - OG image: leave as cover (default).
   - Canonical URL: leave empty (this is the original).
8. Replace `BLOGGER_POST_URL` at the bottom with the live Blogger URL. **Publish.**
9. Search Console: add the Hashnode blog as a property, submit `yourblog/sitemap.xml`, and
   request indexing for the post.

## Medium (step by step)

Medium is an **original** story (different keyword, different example), not a copy of the other
two, so don't use "Import a story" and don't set a canonical link.

**What Medium's editor can't take, and how `medium-post.html` handles it:**

| Not supported in Medium | What the paste page does instead |
|---|---|
| Markdown (`##`, `**bold**`, ```` ``` ````) | Already converted to rich text; copy from the browser, never from the `.md` file |
| Tables | None in this story |
| More than 2 heading levels | Only one heading level is used |
| Multi-line code blocks (break apart on paste) | Turned into plain paragraphs with line breaks |
| Images pasted from your computer | Replaced by a bold `[ Upload image here: ... ]` marker |
| Links that aren't real URLs | Placeholder links are `https://replace-with-...example` |
| HTML comments / draft notes | Removed |

1. **New story.** Type the **title** on the first line: `How to Take Meeting Notes People Actually Read`
2. Press Enter, type the **subtitle**, select it and click the small **T** (subtitle style):
   `Most meeting notes record the conversation. Useful ones record decisions, owners and dates. Here's a simple method, a before-and-after example, and a template you can copy.`
3. Press Enter for a new line. Open `medium-post.html` in a browser, press Ctrl/Cmd + A, copy, and
   paste into Medium.
4. **Images:** click each bold `[ Upload image here: ... ]` line, delete the text, click **+** >
   image icon, and upload the named file:
   - `medium-banner.png` (first image, so Medium uses it as the featured image)
   - `medium-before-after.png`, alt text: `Meeting notes before and after: transcript-style notes vs 3 lists and a date`
5. **AI disclosure:** the italic line under the banner is Medium's required label for AI-assisted
   writing (it must be in the first two paragraphs, or the story only reaches your followers).
   Keep it unless you rewrite the story substantially in your own words.
6. **Links:** click each link that starts with `https://replace-with-`, and change it to the live
   Blogger and Hashnode post URLs.
7. **Publish** > add 5 topics: `Productivity`, `Meetings`, `Note Taking`, `Management`, `Remote Work`.
8. After publishing: **... > More settings > SEO settings**:
   - SEO title: `How to Take Meeting Notes People Actually Read (+ Template)`
   - SEO description: `How to take meeting notes that get read and acted on: the 3 lists + 1 date method, a before-and-after example, tips for live note taking, and a template.`
   - **Customize story link:** `how-to-take-meeting-notes`
9. Optional: submit it to a Medium publication about productivity or management for more reach.
   Publications have their own rules; most accept one self-mention like the Lynkk section.

If any block still pastes wrongly, tell me which section and I'll rework it in the draft.

## Before you hit publish: guideline check

- [ ] Read the whole post once yourself (Hashnode's Code of Conduct requires you to review
      AI-assisted content and take responsibility for it).
- [ ] Run the prompt from the Hashnode post on one real transcript and confirm the output looks
      like the example. Hashnode readers will try it.
- [ ] Lynkk appears in one section near the end of each post, plus the FAQ on Hashnode. Don't add
      more mentions or links.
- [ ] Medium: AI disclosure line is in the first two paragraphs (or you've rewritten the story in
      your own words). Medium links are nofollow, so the value is readers and brand mentions.
- [ ] No placeholder text left: search for `IMAGE_URL`, `BLOGGER_POST_URL`, `HASHNODE_POST_URL`
      (Blogger, Hashnode) and `replace-with-` / `Upload image here` (Medium).
- [ ] All images have alt text.

## After publishing

- Share both links from Lynkk's LinkedIn and X (helps discovery and crawling).
- Day 7: check Search Console > URL Inspection shows "URL is on Google" for the Blogger and
  Hashnode posts, and search Google for the Medium title to confirm it's indexed.
- Day 30: check Search Console queries for both blogs and re-run Ubersuggest AI Search
  Visibility for lynkk.ai. Use the queries with impressions in positions 8-30 to plan the next
  posts (ideas are in `../research/hashnode-blogger-keyword-research.md`, section 7).
