# Publishing kit: Hashnode + Blogger

Everything needed to publish both posts. Source drafts live in `content/*.md`; the files here
are generated from them with `python3 content/publish/build.py` (re-run it after any edit).

| File | Use |
|---|---|
| `hashnode-post.md` | Paste into the Hashnode editor body |
| `blogger-post.html` | Paste into Blogger's **HTML view** |
| `../images/hashnode-cover.png` | Hashnode cover (1600x840) |
| `../images/hashnode-pipeline.png` | Hashnode inline diagram (1600x560) |
| `../images/blogger-banner.png` | Blogger banner and thumbnail (1200x630) |
| `../images/blogger-action-item-anatomy.png` | Blogger inline graphic (1200x675) |

Images are built from HTML in `../images/src/` using Lynkk's brand colors and Inter (taken from
lynkk.ai). To change wording, edit the HTML and run `bash content/images/render.sh`.

## Publish order

Publish **Blogger first**, then Hashnode, then go back and fix the cross-links:

1. Publish Blogger with `HASHNODE_POST_URL` left in place.
2. Publish Hashnode, replacing `BLOGGER_POST_URL` with the live Blogger URL.
3. Edit the Blogger post: replace `HASHNODE_POST_URL` with the live Hashnode URL. Update.

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

## Before you hit publish: guideline check

- [ ] Read the whole post once yourself (Hashnode's Code of Conduct requires you to review
      AI-assisted content and take responsibility for it).
- [ ] Run the prompt from the Hashnode post on one real transcript and confirm the output looks
      like the example. Hashnode readers will try it.
- [ ] Lynkk appears in one section near the end of each post, plus the FAQ on Hashnode. Don't add
      more mentions or links.
- [ ] No placeholder text left: search for `IMAGE_URL`, `BLOGGER_POST_URL`, `HASHNODE_POST_URL`.
- [ ] All images have alt text.

## After publishing

- Share both links from Lynkk's LinkedIn and X (helps discovery and crawling).
- Day 7: check Search Console > URL Inspection shows "URL is on Google" for both posts.
- Day 30: check Search Console queries for both blogs and re-run Ubersuggest AI Search
  Visibility for lynkk.ai. Use the queries with impressions in positions 8-30 to plan the next
  posts (ideas are in `../research/hashnode-blogger-keyword-research.md`, section 7).
