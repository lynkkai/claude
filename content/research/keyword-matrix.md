# Keyword Matrix: Hashnode + Blogger Articles

> Built 2026-10-15 from Ubersuggest (US, locId 2840). **Vol** = monthly US searches,
> **SD** = SEO difficulty (0-100). Search Console was not connected, so there's no GSC column yet.
> A spreadsheet version is in `keyword-matrix.csv`.

## How the matrix works

Each article targets three tiers of keywords. The high-volume **head** terms go where they carry
the most weight (title, H1, slug, meta description). The **body** and **long-tail** terms are what
the article can realistically rank for first. Long-tail rankings build the topical authority that
eventually lets the post move up for the head term.

| Tier | Role | Where it goes | Realistic outcome |
|---|---|---|---|
| **Head** | Relevance signal for the big query | Title, H1, slug, meta, first 100 words, 1 H2, 1 image alt | Page 2-3 at first; page 1 only with links and time |
| **Body** | Main traffic driver | H2 headings, intro, FAQ questions | Page 1 within 2-4 months if the post earns engagement |
| **Long-tail** | Quick wins + AI Overview citations | H3s, FAQ answers, table captions, natural sentences | Page 1 within weeks of indexing |

## Anti-spam rules (both platforms)

Both platforms and Google penalize content written for keywords rather than readers:

- **Google spam policies** define keyword stuffing as repeating keywords "unnaturally, or out of
  context", including blocks of text that just list terms
  ([Google Search Central](https://developers.google.com/search/docs/essentials/spam-policies)).
- **Hashnode Code of Conduct** bans "SEO abuse", "misleading links", and "using the platform
  primarily for self-promotion without contributing to the community". AI-assisted writing is
  allowed, but "you must review and take responsibility for everything you publish"
  ([Hashnode Code of Conduct](https://hashnode.com/code-of-conduct)). Breaking it gets the post removed
  on the first warning, then a 1-month ban, then a permanent ban
  ([Hashnode enforcement](https://support.hashnode.com/en/articles/6435599-what-happens-when-someone-breaks-the-code-of-conduct)).
- **Blogger content policy** says "Do not spam", which covers "unwanted promotional or commercial
  content" and "unwanted repetitive content" ([Blogger content policy](https://www.blogger.com/content.g)).

How the drafts follow those rules:

| Rule | Applied as |
|---|---|
| Each head keyword appears as an exact match **once** in title/H1 and once in the body | Elsewhere use variants: "minutes template", "this template", "the notes" |
| Keyword density stays under ~1% | Checked: see "Density check" at the bottom |
| No keyword lists, no hidden text, no bolded keywords | Bold is used only for meaning (e.g. "one owner") |
| Every heading has to make sense to a reader who never heard of SEO | Headings are questions or tasks, not keyword strings |
| Product mentions: 1 section near the end, under 10% of the article | Lynkk appears in one section + FAQ; the article is fully useful without it |
| Links: 1-2 to lynkk.ai, descriptive anchors, no exact-match anchor repeated | Blogger: "Lynkk" + "try the Lynkk AI meeting assistant free". Hashnode: "Lynkk" once |
| Hashnode: value first | Prompt, JSON schema and working Python script are the core of the post |

## Article 1: Blogger

**Title / H1:** Meeting Minutes Template With Action Items (Free) + Example (59 chars)
**Search description:** Free meeting minutes template with action items, plus a meeting notes template and a filled-in example. Copy it and learn how to write minutes in 6 steps. (154 chars)
**Permalink:** `/meeting-minutes-template-action-items.html`
**Labels:** Meeting Minutes, Meeting Notes, Templates, Productivity

| Tier | Keyword | Vol | SD | Placement in the article |
|---|---|---|---|---|
| Head | meeting minutes template | 22,200 | 40 | Title, H1, slug, meta, intro, H2 "Free meeting minutes template with action items", image alt |
| Head | meeting notes template | 22,200 | 49 | Meta, H2 "Meeting notes template (short version for team meetings)" |
| Head | meeting minutes | 9,900 | 36 | H2 "What are meeting minutes?", intro |
| Body | meeting minutes sample | 5,400 | 39 | H2 "Meeting minutes example (filled-in sample)" |
| Body | meeting minutes example | 3,600 | 36 | Title ("+ Example"), same H2 |
| Body | meeting notes | 3,600 | 29 | H2 "Meeting notes vs meeting minutes" |
| Body | action items | 2,900 | 40 | Title, H2 "What are action items in a meeting?" |
| Body | meeting notes minutes | 2,400 | 17 | H2 "Meeting notes vs meeting minutes" + comparison table |
| Body | minutes of meeting | 1,900 | 31 | Definition paragraph |
| Long-tail | how to take meeting minutes | 1,000 | 30 | H2 "How to write meeting minutes in 6 steps" + FAQ |
| Long-tail | how to writing meeting minutes / how to write meeting minutes | 1,000 / 720 | 12 / 30 | Same H2 (exact phrase "how to write meeting minutes") |
| Long-tail | how to make meeting minutes | 880 | 13 | Step intro sentence |
| Long-tail | meeting notes template free | 880 | 14 | Template intro sentence |
| Long-tail | how to take good meeting notes | 880 | 16 | Step 3 tip |
| Long-tail | meeting minutes template free | 720 | 28 | Template intro sentence |
| Long-tail | meeting minutes template sample | 480 | 18 | Example H2 caption |
| Long-tail | meeting minutes template action items | 390 | 31 | H2 (exact) |
| Long-tail | best meeting notes template | 390 | 19 | Notes template intro |
| Long-tail | meeting notes format template | 320 | 20 | FAQ "best format" |
| Long-tail | google doc meeting minutes template | 260 | 16 | "Copy into Google Docs, Word..." sentence |
| Long-tail | meeting minutes format with action items | 260 | 20 | FAQ "What is the best format for meeting minutes with action items?" |
| Long-tail | meeting notes with action items | 210 | 12 | Intro + FAQ |
| Long-tail | what are action items in a meeting | 70 | 31 | H2 (exact question) |

**SERP reality check:** "meeting minutes template" page one is Microsoft Word (DA 90), Canva (DA 93),
Slack (DA 89) and Zapier (DA 81). A Blogspot post won't beat them soon. The post *will* compete on
the long-tail rows, where page one includes DA 15-16 sites (obsibrain.com, hinoter.com for
"meeting notes with action items"). Keep the head term in the title for relevance and click-through,
and expect the traffic to come from the long tail first.

## Article 2: Hashnode

**Title / H1:** AI Meeting Notes From Any Transcript: The Prompt + a Jira Script
**SEO title (≤60):** AI Meeting Notes: The Prompt to Summarize Any Transcript (56 chars)
**Subtitle (Hashnode field):** A copy-paste prompt for ChatGPT, Claude and Copilot that turns a meeting transcript into minutes, decisions and action items, plus 40 lines of Python that file them in Jira.
**Meta description:** Get AI meeting notes from any transcript: one prompt for ChatGPT, Claude or Copilot that writes minutes and action items, plus a Python script for Jira. (152 chars)
**Slug:** `ai-meeting-notes-transcript-prompt`
**Tags (max 5):** `ai`, `llm`, `productivity`, `python`, `jira`

| Tier | Keyword | Vol | SD | Placement in the article |
|---|---|---|---|---|
| Head | ai note taker | 27,100 | 48 | H2 "Prompt vs AI note taker: where DIY stops scaling" (1 exact mention) |
| Head | ai meeting notes taker | 3,600 | 49 | Same section, as a natural variant |
| Head | ai meeting minutes | 1,600 | 49 | H2 "Get AI meeting minutes as JSON (for automation)" |
| Head | ai meeting notes | 1,000 | 41 | Title, H1, slug, meta, first sentence |
| Body | summarize meeting | 590 | 27 | Intro, FAQ |
| Body | meeting transcript | 590 | 82 | Title, H1 (as "transcript"), body |
| Body | meeting summary | 390 | 35 | Short answer paragraph |
| Body | chatgpt meeting notes | 210 | 28 | H3 "ChatGPT meeting notes prompt" |
| Body | ai meeting summary | 170 | 37 | FAQ |
| Body | summarize transcript | 170 | 33 | SEO title |
| Long-tail | chatgpt prompt to summarize meeting transcript | 30 | 23 | H3 + FAQ |
| Long-tail | copilot prompt to summarize meeting transcript | 20 | 6 | H3 |
| Long-tail | claude prompt to summarize meeting transcript | autocomplete | 4 | H3 |
| Long-tail | prompt to summarize meeting transcript | 10 | 11 | H2 "The prompt (works in ChatGPT, Claude, Gemini and Copilot)" + FAQ |
| Long-tail | meeting transcript to minutes | 10 | 5 | FAQ |
| Long-tail | chatgpt meeting minutes | 50 | 19 | ChatGPT H3 body |
| Long-tail | jira meeting notes | 10 | 19 | H2 "From meeting notes to Jira tickets..." |

**SERP reality check:** "ai note taker" is a commercial query dominated by product pages and review
listicles, so it gets one natural mention, not a target. The realistic Hashnode wins are
"chatgpt prompt to summarize meeting transcript" (page one includes DA 7 and DA 9 sites) and its
Claude/Copilot variants, plus the AI Overview / ChatGPT citation for "best prompt to summarize a
meeting transcript".

## Article 3: Medium

**Title / H1:** How to Take Meeting Notes People Actually Read
**SEO title (58 chars):** How to Take Meeting Notes People Actually Read (+ Template)
**Subtitle:** Most meeting notes record the conversation. Useful ones record decisions, owners and dates. Here's a simple method, a before-and-after example, and a template you can copy.
**SEO description (151 chars):** How to take meeting notes that get read and acted on: the 3 lists + 1 date method, a before-and-after example, tips for live note taking, and a template.
**Story link:** `how-to-take-meeting-notes`
**Topics (max 5):** Productivity, Meetings, Note Taking, Management, Remote Work

Why a different keyword: copying the Blogger or Hashnode post to Medium would make three URLs compete
for the same query, and Medium (DA 95) would likely outrank the originals. A separate keyword
gives Lynkk a third ranking page and two internal links to the other posts.

| Tier | Keyword | Vol | SD | Placement in the article |
|---|---|---|---|---|
| Head | meeting notes | 3,600 | 29 | Title, H2s, body |
| Body | how to take good meeting notes | 880 | 16 | H2 "How to take good meeting notes during the meeting" |
| Body | how to write meeting notes | 880 | 36 | Method section intro (exact), quick answers |
| Body | taking meeting notes | 720 | 46 | Intro, AI section |
| Primary | how to take meeting notes | 590 | 44 | Title, H1, slug, SEO title, meta, first paragraphs |
| Long-tail | take meeting notes | 480 | 46 | Intro, body |
| Long-tail | best way to take meeting notes | 140 | 40 | Quick answers (exact question) |

**SERP reality check:** a Medium story (medium.com/envoy-design, DA 95) already ranks #5 for
"how to take meeting notes", next to Reddit, Teamwork, Asana and Slack. Medium's domain can rank
here; a fresher, more complete story with a template and example has a real chance at page one.
Medium links are nofollow, so this post's value is ranking, referral clicks and brand mentions.

## Article 4: DEV (dev.to)

**Title:** Meeting Notes Templates for Dev Teams: Standup, Retro, ADR (58 chars)
**Description (meta):** Four Markdown meeting notes templates for dev teams: standup, sprint planning, sprint retro and ADRs, plus a script that lists open action items.
**Tags (max 4):** productivity, agile, documentation, markdown

Why this angle: DEV readers are developers, and the other three posts already cover general notes,
minutes and AI prompts. Engineering meeting templates in Markdown are a different query set, so
there's no cannibalization. DEV's AI guidelines forbid promoting your own business in AI-assisted
posts, so Lynkk is not named in the article; the brand lives in the author profile.

| Tier | Keyword | Vol | SD | Placement |
|---|---|---|---|---|
| Head | meeting notes template | 22,200 | 49 | Title (as "Meeting Notes Templates"), intro |
| Body | sprint retrospective template | 390 | 37 | H2 "3. Sprint retrospective template" (exact) |
| Long-tail | daily standup meeting notes | 70 | 23 | H2 "1. Daily standup meeting notes template" |
| Long-tail | architecture decision record template | 70 | 46 | H2 on ADRs + example ADR |
| Long-tail | sprint planning meeting notes | n/a | n/a | H2 "2. Sprint planning meeting notes template" |

Note: Ubersuggest's daily report limit (150) was reached while researching this article, so the
sprint planning and ADR variants weren't pulled. Re-check them when the quota resets.

## Article 5: Medium story 2

**Title:** Meeting Notes vs Meeting Minutes: What's the Difference?
**SEO title (57 chars):** Meeting Notes vs Meeting Minutes: Differences + Examples
**Story link:** `meeting-notes-vs-meeting-minutes`

Page one for "meeting notes vs meeting minutes" (2026-10-16) is all AI note-taker vendor blogs
(tl;dv, Fireflies, Fellow, Sembly, Wudpecker, Audionotes). A neutral Medium story with the same
meeting written both ways is the differentiator. It links to the Blogger template (minutes) and
Medium story 1 (notes), so the cluster reinforces itself.

| Tier | Keyword | Vol | SD | Placement |
|---|---|---|---|---|
| Head | meeting minutes | 9,900 | 36 | Title, H2s, body |
| Body | meeting minutes example | 3,600 | 36 | "Same meeting, written both ways" section |
| Body | meeting notes minutes | 2,400 | 17 | Title, comparison section |
| Body | what is meeting minutes | 2,400 | 36 | H2 "What are meeting minutes?" |
| Body | what is meeting notes | 2,400 | 64 | H2 "What are meeting notes?" |
| Body | minutes of meeting | 1,900 | 31 | Definition paragraph, FAQ "What does MoM mean?" |
| Body | meeting minutes meaning | 1,300 | 28 | Definition paragraph |
| Primary | meeting notes vs meeting minutes | not pulled | n/a | Title, H1, slug, short answer |

Ubersuggest's daily limit was reached, so the primary keyword's volume wasn't pulled. Check it when
the quota resets.

## Article 6: Medium story 3

**Title:** How to Write a Follow-Up Email After a Meeting
**SEO title (52 chars):** Follow-Up Email After a Meeting: 7 Templates to Copy
**Story link:** `follow-up-email-after-meeting`

**Topic research (Ubersuggest Google autocomplete, US, 2026-10-16).** Three seeds were expanded:
"meeting agenda", "meeting follow up email" and "one on one meeting". The follow-up email seed had
the richest set of distinct intents (templates, examples, subject lines, "with action items",
client, sales, one-on-one, missed meeting, no response, when to send, what to include) and the
closest fit with Lynkk's after-meeting features. Meeting agenda is crowded with big template sites;
one-on-one is a weaker product fit. Both stay on the list for later posts.

**Content research (2026-10-16).** Page one for "follow up email after meeting" is thin template
pages (several auto-generated) and email/sales tool blogs, with no Medium story. The story fills the
gap with situation-specific templates that carry decisions and action items.

| Intent (autocomplete) | Section that answers it |
|---|---|
| meeting follow up email template / example | 7 templates |
| meeting follow up email subject line | 12 subject lines |
| meeting follow up email with action items | Template 1, "What to include" |
| follow up email after meeting with client | Template 2 |
| sales meeting follow up email | Template 3 |
| follow up email after one on one meeting | Template 5 |
| follow up email when someone misses a meeting | Template 6 |
| follow up email after meeting no response | Template 7, "When to send it" |
| when to send follow up email after meeting | "When to send it", quick answers |
| what should a follow up meeting email include | "What to include" + anatomy graphic |
| write a follow up email using my meeting notes | AI section prompt |

**Volumes and difficulty: pending.** Ubersuggest's daily report limit (150) was used up, so
search volume, SEO difficulty and content ideas couldn't be pulled. Re-run `keyword_overview` for
"follow up email after meeting", "meeting follow up email template" and "meeting follow up email
subject line" when it resets.

## Density check (exact-match counts in final drafts)

Counted on the article body (draft header comment excluded).

| Article | Keyword | Exact count | Words | Density |
|---|---|---|---|---|
| Blogger | meeting minutes template | 3 | 1,799 | 0.50% |
| Blogger | meeting minutes (incl. inside longer phrases) | 16 | 1,799 | 1.78% |
| Blogger | action items | 20 | 1,799 | 2.22% |
| Hashnode | ai meeting notes | 2 | 1,717 | 0.35% |
| Hashnode | ai note taker | 2 | 1,717 | 0.35% |

"Action items" and "meeting minutes" are the subject of the Blogger post, and about a third of
their uses sit inside the copy-paste templates (section headers like `ACTION ITEMS`), so the
density reads naturally. Five prose repetitions were already swapped for "tasks", "to-dos" and
"the minutes". If you edit the post, don't add more exact repeats of either phrase.
