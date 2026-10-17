# Lynkk Blog Conversion Playbook

How to title and write every blog in `website-blogs.csv` so a reader who lands from Google clicks through to sign-up. Follow this for all 35 posts and the 20 Medium/Substack posts.

## 1. What to add in the title

Build each title from these parts, in this order. Use the parts that fit the intent.

| Part | Why | Examples |
|---|---|---|
| 1. **Primary keyword, near the start** | Google bolds it; the reader sees their own words | `Otter.ai Alternatives`, `Granola AI Pricing` |
| 2. **Buying word** | Tells Google and the reader this page helps them choose | Best, Top, Alternatives, vs, Pricing, Review, Free, Cheaper |
| 3. **A number** | Sets expectations, lifts CTR | 7 Best, 9 Tools, 12 Examples |
| 4. **The year, in a sentence** | Buyers want current prices and features | in 2026, for 2026, a 2026 guide |
| 4b. **The location, where it fits** | Matches where the reader is (US buyers, India for Hindi and MOM topics) | in the US, for US teams, in India, for US boards |
| 5. **A proof word** | Signals real testing, not a copied list | Tested, Compared, Honest, Real Costs |
| 6. **Who it is for** | Matches the reader's situation | for Google Meet, for In-Person Meetings, for Teams, for Sales |
| 7. **A hook tied to a Lynkk strength** | Makes Lynkk the natural click later in the post | Free & Paid, With or Without a Bot, Windows & Teams, Free Plan Limits |

**Two titles per post:**

- **SEO title tag** (what Google shows): 60 characters or fewer, so it is not cut off. Primary keyword + buying word + year + one hook.
- **H1** (top of the page): can run longer and add the proof word and audience.

Example for #1:

- Title tag: `Best Otter.ai Alternatives in the US for 2026`
- H1: `The Best Otter.ai Alternatives in the US for 2026, Tried on Real Meetings`

**Location and year, written like a person would:**

- Work them into the sentence ("for US teams in 2026", "in India") instead of stamping brackets on the end ("(2026) (US)").
- Vary the wording across posts. The same "in the US for 2026" on every title reads as auto-generated.
- Avoid stacking parts with colons and ampersands ("(2026): Free & Paid, Tested"). One colon at most.
- How-to and template posts keep the year only. "How to Record a Google Meet Call in the US" reads as keyword stuffing, so mention the location in the meta description and first paragraph instead.
- Use India only on India-market keywords (Hindi, minutes of meeting, MOM). Everything else is US.
- Update the year in January and change the page's 'last updated' date at the same time.

**Title rules:**

- Put the exact primary keyword in both the title tag and the H1, and in the URL.
- Do not put 'Lynkk' in non-branded titles. Readers search for the category, not for us yet.
- Only promise what the post delivers (no 'Free Forever' unless that is confirmed).
- No em dashes or en dashes (house style). Use a colon or parentheses.
- Meta description (max 155 characters): answer + proof + soft CTA. Example: 'We tested 9 Otter.ai alternatives on real Zoom, Meet and in-person meetings. See free plans, prices and which one fits your team.'

## 2. Page structure that converts

### BOFU: Best / Alternatives / vs / Pricing / Review

1. **H1 + 2-3 sentence answer.** Give the verdict in the first screen. Example: 'The best Otter.ai alternative for most teams is X if you need A, Lynkk if you need online and in-person notes in one place.'
2. **'Our quick picks' box** with Lynkk first, labeled 'Lynkk (our product)' like your existing posts, plus a **Start free** button. This is CTA #1, above the fold.
3. **Comparison table:** free plan, starting price, bot or no bot, platforms (Zoom, Meet, Teams, in-person), languages, CRM/Jira, data region. Buyers scroll straight to it.
4. **'Why people switch from [competitor]'**: the real pain (minute caps, price, privacy, no in-person). Use Reddit/G2 quotes with a link. Then **CTA #2** right after the pain: 'Hit this limit? Try Lynkk free on your next meeting.'
5. **One section per tool** (pros, cons, price, best for). Keep Lynkk's section the most concrete: a screenshot of real notes, action items and a CRM or Jira update.
6. **'How to switch in 3 steps'**: sign up, connect calendar, let it join or record the next meeting. Steps lower the effort of signing up. **CTA #3** at the end of the steps.
7. **FAQ** (5-8 questions from People Also Ask and GSC): is it free, is it safe, does it work without a bot, does it work in person, which languages.
8. **Final CTA block:** one line of benefit + button + one trust line (data region choice, security page link).

### MOFU: how to remove a bot, how to record, ChatGPT notes

1. Answer the task first, step by step with screenshots. Do not hide the answer behind the pitch; Google and readers punish that.
2. Name the limit the reader will hit next ('Teams will not let you record unless...').
3. Offer Lynkk as the easier path right after that limit, with a CTA box.
4. Link to the matching BOFU post ('Compare the best alternatives').

### TOFU: templates and how-tos

1. Give the template or method in full (copyable, downloadable).
2. Next to the download button: 'Or skip the template. Lynkk fills this in about 30 seconds after your call.' + Start free.
3. Show a side-by-side: hand-written version vs Lynkk output of the same meeting.
4. Link to the matching BOFU post (minutes post links to 'Best App for Meeting Minutes').

## 3. CTA library

| Where | Copy | Button |
|---|---|---|
| Quick picks box | Lynkk: one AI for every meeting, online and in person | Start free |
| After the pain section | Hit [competitor]'s limit? Try Lynkk free on your next meeting | Try Lynkk free |
| After switching steps | Ready? It takes one meeting to see the difference | Start free |
| Template posts | Or skip the template. Lynkk writes this for you after the call | Get it automatically |
| Security / IT posts | Bring this checklist to a 20-minute demo | Book a demo (/demo) |
| Final block | Notes, action items and CRM updates about 30 seconds after every call | Start free |

Each post's main CTA is in the 'Main CTA' column of `website-blogs.csv`.

**Placement:** 3 CTAs per post (top, middle after the pain point, end) plus a sticky bar on mobile. More than that reads as spam and hurts trust.

## 4. Tracking sign-ups per blog

Tag every CTA link so you can see which posts produce sign-ups:

`https://lynkk.ai/sign-up?utm_source=blog&utm_medium=cta&utm_campaign=<post-slug>&utm_content=<top|mid|end>`

For Medium and Substack use `utm_source=medium` or `utm_source=substack`. In GA4, mark sign-up as a conversion and report it by `utm_campaign`. After 6-8 weeks, move effort toward the posts and CTA positions that convert.

## 5. Trust elements that lift sign-ups

- Real screenshots or a 20-second GIF of Lynkk producing notes from a meeting.
- 'How we tested' box: which meetings, how long, which plans.
- Link to /security and mention that you can choose the region where data is processed.
- Author box with a real person (the existing author page /blog/authors/samarth-wagh).
- Only real customer quotes, with permission. Never invent reviews, numbers or awards.

## 6. Do not

- Do not claim competitor facts you have not checked that week (prices change often).
- Do not bash competitors; say who each tool is best for. Fair lists rank and convert better.
- Do not put the CTA before the answer on MOFU and TOFU posts.
- Do not use em dashes or en dashes.

## 7. Confirm with the team before writing

- Free plan: what is included and any limits (minutes, history, seats).
- Is a credit card needed at sign-up? If not, say 'no credit card' in every CTA; it lifts conversion.
- Which CRMs are supported (HubSpot, Salesforce?) for the CRM post.
- Hindi dictation: confirmed on /features/dictation (Hindi is one of 18 languages on Pro). Say it is a Pro feature in the Hindi voice typing post.
- Bot-free capture: confirm how the Chrome extension and Mac app record without a bot.
- Paid plan prices for the pricing posts' 'Lynkk' rows.
