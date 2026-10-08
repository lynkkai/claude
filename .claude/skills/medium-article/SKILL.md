---
name: medium-article
description: Research, write and check SEO-focused Medium articles for Lynkk (lynkk.ai). Use whenever asked to write, draft or plan a Medium article or blog post for Lynkk, to find Medium topics or keywords, or to check a Medium draft before publishing. Covers Ubersuggest keyword research, Medium's AI and distribution rules, Lynkk house style, the article template, and an automated pre-publish check.
---

# Medium article creation (Lynkk)

Produces one publish-ready Medium draft per run: a low-difficulty keyword with proof it can
rank, an article that follows Medium's rules and Lynkk's house style, and the settings to paste
into Medium. Output lives in `content/medium/NN-slug.md`.

## Before writing anything

Read these, every time:

- `CLAUDE.md`: the writing rules. **No em dashes (—) or en dashes (–), ever.**
- `memory/lynkk-brand.md`: confirmed product facts. Anything under "To confirm" must not be
  stated as fact (pricing, Zoom/Meet/Teams support, specific CRMs, language count, data regions,
  certifications, platforms beyond Web + Mac).
- `content/medium-article-topics.md`: the topic plan. If the user didn't name a topic, take the
  next unwritten one from "Suggested publishing order".
- `content/medium/`: existing drafts, so you don't repeat a keyword or an angle.

## Step 1: Keyword (skip if the topic plan already has one)

Use the Ubersuggest MCP tools (load them with ToolSearch first). Use US data: `locId: 2840`.

1. `keyword_suggestions` with 2-3 seed keywords from Lynkk's themes (meeting notes, action items,
   meeting prep, follow-up, transcription, AI meeting assistant).
   The `pd` field in these results is **paid** difficulty. Ignore it for SEO.
2. `keyword_overview` on 8-15 candidates to get the real `seo_difficulty`.
   Keep: SD 35 or lower, informational or commercial intent, Lynkk is a natural fit.
   Drop: competitor brand terms (Otter, Fireflies, Read AI, Copilot, Granola) and anything
   that contradicts Lynkk's pitch (for example "note taker that doesn't join meetings").
3. `serp_analysis` on the winner. Good signs: several page-one results with domain authority
   under 40, thin answers, or a Medium publication already ranking.
4. Pick 2-4 secondary keywords from the same family.

## Step 2: Write the draft

Copy `template.md` (in this skill folder) to `content/medium/NN-slug.md`, where NN is the next
number. Fill in the publishing notes, then write the article under the `---` line.

### Article rules

- **Length:** 1,200 to 1,800 words.
- **Title:** contains the primary keyword, promises something concrete ("7 samples", "checklist",
  "with examples"). The subtitle restates the benefit with a secondary keyword.
- **Keyword placement:** primary keyword in the title, the subtitle and the first 100 words.
  Use the primary or a secondary keyword in at least two `##` headings.
- **Open with the answer.** The first paragraph answers the search query directly (this is
  what wins featured snippets). Context comes after.
- **Something to copy:** templates, samples, a checklist or worked examples. Put email or
  document templates in blockquotes (`>`), with `[brackets]` for placeholders.
- **No tables in the article body.** Medium can't display them. Use bullet lists, or note that
  a table should be embedded as an image or GitHub Gist.
- **Lynkk:** one short mention, inside a "how to do this faster" type section near the end,
  with exactly one link to `https://lynkk.ai`, followed by "(Full disclosure: I work on Lynkk.)".
  Only confirmed features. Teach first; the article must be useful with the Lynkk line deleted.
- **Facts:** no invented statistics, studies or quotes. If a number matters, find a source and
  cite it, or leave it out.
- **Tone:** plain, direct, second person ("you"). Short paragraphs. Bold the lead phrase of list items.
- **Close** with a short checklist or summary and one closing line.

### Medium's rules (they decide distribution)

- AI-generated text must be disclosed in the first two paragraphs. Fully AI-written or
  undisclosed AI stories only reach the writer's own followers, and AI writing can't be
  paywalled in the Partner Program. **Always tell the user** the draft was written with AI and
  that they should rewrite it in their own voice, or add the disclosure line from the template.
- Stories whose main purpose is selling or collecting signups don't get General Distribution.
- AI-written product reviews made to rank and sell are banned. Comparison pieces (for example
  "best AI meeting assistant") must be honest, tested by a human and include competitors fairly.

## Step 3: Check

Run the checker and fix every FAIL before handing over:

```bash
python3 .claude/skills/medium-article/scripts/check_article.py content/medium/NN-slug.md
```

It checks: no em/en dashes, word count, primary keyword near the top, exactly one lynkk.ai link,
the affiliation disclosure, brand misspellings, no tables, SEO title (60 characters or less),
SEO description (156 characters or less), and 5 tags. WARN lines are judgment calls; read them.

Then reread the draft once as a skeptical editor: is every claim about Lynkk in the brand file?
Would a reader learn something even without Lynkk in it?

## Step 4: Hand over

1. Commit the draft and push to the working branch.
2. Send the file to the user, and give a short summary: title, keyword and difficulty, word count,
   the AI-disclosure reminder, and where to submit (the target publication).
3. Offer the next topic in the plan, or a LinkedIn version. For LinkedIn, **rewrite** it for a
   different keyword (LinkedIn has no canonical link, so a copy would compete with the Medium
   page), and include the share-post text. See `content/linkedin/` for the format.
