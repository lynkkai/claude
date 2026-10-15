# Hashnode + Blogger Content Research for Lynkk

> Prepared 2026-10-15. Keyword data: Ubersuggest (lynkk.ai project, US database, locId 2840)
> unless noted. SERP snapshots pulled the same day. Google Search Console was **not connected**
> in this session, so no GSC data is included (see "GSC next step" at the bottom).

## 1. Starting point: where Lynkk stands today

| Signal | Value | Source |
|---|---|---|
| Organic keywords ranking for lynkk.ai | 1 ("zoom meeting bot", position 39, /features/meeting-bot) | Ubersuggest domain_keywords |
| AI search visibility (10 tracked prompts, ChatGPT) | 0% mentions, 0 share of voice | Ubersuggest AI Search Visibility |
| Brands AI assistants name instead | Fireflies.ai (40%), Avoma (30%), Otter.ai (30%), Fathom (20%), Gong (20%) | same |
| Ubersuggest "new content" opportunities | 16, mostly Microsoft Teams recording/transcription queries in the UK | Ubersuggest SEO opportunities |

**Takeaway:** lynkk.ai has almost no organic footprint and is invisible in AI answers. Third-party
posts on Hashnode and Blogger can do three jobs at once: rank for long-tail queries the main site
can't win yet, send referral clicks, and put the "Lynkk" name next to "meeting notes / action items"
on the open web, where AI answer engines can learn the association (GEO).

## 2. Platform research: what works on each

### Hashnode

- **Audience:** developers and technical builders. Trending tags this cycle are dominated by
  `#ai`, `#artificial-intelligence`, `#llm`, `#devops`, `#python`, `#rag`, `#machine-learning`
  ([Hashnode tag page](https://hashnode.com/tag/how-do-i-find-seo-trends)).
- **What performs:** hands-on tutorials with code, prompt and LLM workflows, "how I built X",
  integration walkthroughs (APIs, MCP, Jira, Slack). Generic marketing posts and listicles about a
  product get little traction and can be flagged as promotional.
- **Link value: nofollow.** A hands-on check on 17-18 Sept 2026 found Hashnode outbound links carry
  `rel="noopener noreferrer nofollow ugc"`
  ([HackerNoon test of 20 platforms](https://hackernoon.com/i-checked-the-rel-attribute-on-20-platforms-most-backlinks-pass-nothing)).
  So a Hashnode post will **not** pass PageRank to lynkk.ai. Its value is referral traffic, brand
  mentions for GEO, and ranking in its own right.
- **Indexing:** Hashnode generates a sitemap at `yourblog/sitemap.xml` that you can submit to Search
  Console ([Hashnode SEO docs](https://support.hashnode.com/en/articles/6427542-seo)). There are
  repeated reports of Hashnode posts being slow to index
  ([Indie Hackers thread](https://www.indiehackers.com/post/how-to-rank-my-hashnode-article-on-google-6378e57943)),
  so submit the sitemap and request indexing manually.
- **Option worth considering:** Hashnode lets you map a blog to a custom domain (e.g.
  `blog.lynkk.ai`). That turns every post into equity on Lynkk's own domain instead of a nofollow link.
  If the goal is long-term SEO, this beats a `*.hashnode.dev` blog.

### Blogger (Blogspot)

- **Audience:** general / non-technical searchers; traffic comes almost entirely from Google, not
  from an in-platform feed. Content has to be built for search intent.
- **What performs:** evergreen how-to guides, templates, examples, checklists, and FAQ-rich posts
  targeting long-tail questions ([Blogspot long-tail ranking discussion](https://semanticseo.transistor.fm/16)).
  Original examples and first-hand experience matter more than word count
  ([Blog Chatter 2026 SEO guide](https://www.theblogchatter.com/BeStorified/?p=11680)).
- **Link value: dofollow.** The same Sept 2026 test found Blogspot in-post links have an **empty**
  `rel` attribute, so they pass link equity
  ([HackerNoon](https://hackernoon.com/i-checked-the-rel-attribute-on-20-platforms-most-backlinks-pass-nothing)).
  This is the platform to use for the backlink to lynkk.ai.
- **Indexing:** Blogger is Google-owned; verify the blog in Search Console, submit
  `/sitemap.xml`, and use URL Inspection > Request indexing on publish.

## 3. Keyword research

Columns: **Vol** = US monthly searches, **SD** = Ubersuggest SEO difficulty (0-100, lower is easier).

### Cluster A: meeting minutes / notes with action items (for Blogger)

| Keyword | Vol | SD | Notes |
|---|---|---|---|
| meeting notes minutes | 2,400 | 17 | high volume, low SD |
| how to writing meeting minutes | 1,000 | 12 | misspelled variant, very low SD |
| how to take meeting minutes | 1,000 | 30 | head term for the post |
| how to make meeting minutes | 880 | 13 | |
| free template meeting minutes | 880 | 13 | template intent, add a copy-paste template |
| how to take good meeting notes | 880 | 16 | |
| action items meaning | 880 | 39 | answer in a definition box |
| what is action items | 720 | 44 | |
| meeting minutes template action items | 390 | 31 | |
| meeting minutes format with action items | 260 | 20 | |
| meeting notes with action items | 210 | 12 | **primary**: page one has DA 15-16 sites |
| how to write meeting notes template | 170 | 9 | |
| how to type meeting notes | 170 | 9 | |
| meeting notes action items | 110 | 17 | |
| what are action items in a meeting | 70 | 31 | |
| how to write action items | 30 | 36 | |

**SERP check, "meeting notes with action items":** obsibrain.com (DA 16) ranks #2 and hinoter.com
(DA 15) ranks #7. Page one is beatable by a well-structured guide with a real template.

**SERP check, "how to take meeting minutes":** a Reddit thread ranks #2, then mid-DA sites
(ibabs.com DA 38, polly.ai DA 48, trint.com DA 53). An AI Overview and People Also Ask are shown,
so an answer-first structure plus FAQ is needed to be cited.

**People Also Ask / autocomplete questions to answer** (Ubersuggest Google suggestions):
should meeting minutes include action items; meeting minutes vs action items; how to write action
items in meeting minutes; can meeting minutes be amended; are meeting minutes mandatory; why are
meeting minutes important.

### Cluster B: AI prompts to summarize meeting transcripts (for Hashnode)

| Keyword | Vol | SD | Notes |
|---|---|---|---|
| summarize meeting | 590 | 27 | parent topic |
| chatgpt meeting notes | 210 | 28 | |
| summarize meeting notes | 70 | 36 | |
| chatgpt prompt to summarize meeting transcript | 30 | 23 | **primary**: DA 7 and DA 9 sites on page one |
| copilot prompt to summarize meeting transcript | 20 | 6 | |
| prompt to summarize meeting transcript | 10 | 11 | |
| how to use copilot to summarize meeting transcript | 10 | 9 | |
| meeting transcript to minutes | 10 | 5 | |
| jira meeting notes template | 10 | 5 | |
| claude prompt to summarize meeting transcript, best prompt to summarize meeting transcript, summarize meeting notes from transcript, how to summarize meeting transcript | autocomplete only | 4 | real queries, too new for volume data |

**SERP check, "chatgpt prompt to summarize meeting transcript":** canadianaiguy.ca (DA 7) ranks #6
and liznr.ai (DA 9) #11, alongside a Reddit prompt thread and a GitHub prompt file. Small,
developer-flavoured sites win here, which is exactly Hashnode's profile. Volume per keyword is
low, but the cluster has dozens of variants (ChatGPT / Claude / Copilot / Gemini x prompt / summarize /
transcript / minutes) and this is the type of query AI assistants answer by quoting a prompt,
which makes it a strong GEO target.

### Keywords considered and rejected (for now)

| Keyword | Vol | SD | Why not |
|---|---|---|---|
| ai note taker | 27,100 | 48 | dominated by brands and big review sites |
| best ai note taker | 1,900 | 36 | paid difficulty 100, listicles from DA 60+ sites |
| what is an mcp server | 8,100 | 51 | off-topic for Lynkk's buyers; too competitive |
| jira mcp server | 1,900 | 40 | navigational (people want Atlassian's own server) |
| otter ai alternative | 480 | 34 | good later, but better on lynkk.ai itself (comparison page) |
| how to record a teams meeting | 1,300 | 30 | strong, but it's a Microsoft how-to; save it for lynkk.ai (Ubersuggest already flags it) |

## 4. The two articles

| | Hashnode | Blogger |
|---|---|---|
| File | `content/hashnode-prompt-to-summarize-meeting-transcript.md` | `content/blogger-meeting-notes-with-action-items.md` |
| Primary keyword | prompt to summarize meeting transcript | meeting notes with action items |
| Secondary | chatgpt / claude / copilot prompt to summarize meeting transcript, meeting transcript to minutes, summarize meeting notes, jira meeting notes | how to take meeting minutes, how to make meeting minutes, free template meeting minutes, meeting minutes format with action items, action items meaning |
| Angle | Copy-paste prompts + JSON schema + Python script that turns action items into Jira tickets | Step-by-step guide + free copy-paste template + filled-in example + FAQ |
| Lynkk link | Brand mention + 1 link (nofollow, referral + GEO) | 1-2 contextual dofollow links, anchor "AI meeting assistant" / "Lynkk" |
| Hashnode tags | `ai`, `llm`, `productivity`, `jira`, `python` | n/a |

## 5. Publishing checklist (indexing + GEO)

1. **Before publishing:** set the SEO title and meta description fields (both platforms have them).
   Use the titles and descriptions at the top of each draft.
2. **Blogger:** custom permalink = primary keyword (`/meeting-notes-with-action-items.html`),
   add a search description, add labels. Verify the blog in Search Console and submit `/sitemap.xml`.
3. **Hashnode:** set the slug to `prompt-to-summarize-meeting-transcript`, add the 5 tags, and fill
   in the SEO title/description. Submit the blog sitemap in Search Console.
4. **Request indexing** for both URLs via URL Inspection on publish day.
5. **Cross-link** the two posts to each other (already written into the drafts), and link to both
   from Lynkk's LinkedIn and X once live; social discovery speeds up crawling.
6. **GEO:** each article opens with a direct 2-3 sentence answer, uses a definition, a table, and an
   FAQ, and names "Lynkk (lynkk.ai)" consistently, which are the formats AI Overviews and chat
   assistants quote. Re-check Ubersuggest AI Search Visibility in 30 days.
7. **Images:** add 1 screenshot or diagram per post with descriptive alt text (e.g. "meeting notes
   template with action items table"). Original images help image-pack rankings on Cluster A.

## 6. GSC next step

Search Console was not available to this session. To layer real query data on top of the
Ubersuggest research, export **Performance > Search results** for lynkk.ai (last 3 months,
Queries tab) and share the CSV. The useful cuts are:

- queries with impressions but position 8-30 (topics Google already associates with Lynkk, ideal for the next Blogger/Hashnode posts),
- queries containing "how", "what", "template", "prompt" (question intent that fits these platforms),
- pages with impressions but CTR under 1% (title rewrites).

After the two posts go live, add both blogs as Search Console properties so their own query data can
guide follow-up posts.

## 7. Suggested follow-up posts (same clusters, for later)

- Blogger: "Meeting Minutes vs Meeting Notes: What's the Difference? (With Examples)"
- Blogger: "Meeting Follow-Up Email With Action Items: 5 Templates"
- Hashnode: "Copilot vs ChatGPT vs Claude for Meeting Summaries: Same Transcript, Three Outputs"
- Hashnode: "Build a Meeting-Notes Knowledge Base With Embeddings (and Why It's Harder Than It Looks)"
