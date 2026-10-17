# Make Lynkk's hero readable in five seconds

Lynkk's draft hero has the right idea (the same meeting, your messy notes beside Lynkk's structured note), but it asks a first-time visitor to work through roughly 20 separate elements, and Lynkk never appears as the thing doing the work, so it fails a 5-second read. The fix is mostly subtraction. Keep the left-to-right "Without / With" comparison. Make the "With Lynkk" note the dominant element. Put a visible "Lynkk is recording" actor on the meeting strip. Swap the three long arrows for matching number badges. Drop the waveform, the full-sentence speech bubbles and most of the red tags. Let an HTML headline state the outcome so the graphic only has to confirm it. The evidence supports this: visitors judge a page's visual complexity within 17-50 ms, most exits happen in the first 10 seconds, and in Mayer's multimedia research the largest comprehension gain comes from removing extraneous material. No competitor hero tries a three-zone timeline diagram either. The clearest ones (Fireflies Sales, Jamie) show one meeting and one concrete output. Two problems need fixing before anything ships. The lawyers page describes the lease-dispute meeting as "in the office", but the draft labels it "Google Meet". And the brand memory claims "CRM fields updated" and "speaks when needed", which the live site does not support: the sales page says Lynkk does not work with CRMs yet, and in-call answers appear only as text in a side panel. A 10-person Lyssna five-second test per variant, with an 80% "gets the gist" bar, can confirm the redesign in an afternoon.

## Visitors judge complexity in 50 ms and leave within 10 seconds

Visitors form their first impression before they read anything. In Lindgaard and colleagues' Carleton study, home pages flashed for **50 ms** got visual-appeal ratings that matched ratings given after longer viewing, and the authors argued that this first reaction spreads to later judgments of credibility and usability ([Digital Trends](https://www.digitaltrends.com/home/surfers-judge-web-pages-seen-for-only-50ms/)). Tuch and colleagues at Google and the University of Basel found the same with 119 real sites: **visual complexity affected aesthetic ratings even at 17 ms**, and sites with low complexity and high prototypicality (looking like a typical site of their kind) were rated most appealing ([Google Research](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/)). Microsoft Research's analysis of more than 2 billion dwell times found that **the first 10 seconds carry the highest probability of leaving**. Nielsen's conclusion was that a page must communicate its value proposition within 10 seconds ([NN/g](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/)). That 10 seconds is the budget for the whole hero, not for the graphic alone. In practice, the headline has to state the claim and the graphic has to confirm it at a glance.

What visitors look at first also matters. In NN/g's eyetracking work, users scan headings first in a "layer cake" pattern, and that pattern only works when each chunk is visually separated and clearly labeled ([NN/g](https://www.nngroup.com/articles/layer-cake-pattern-scanning/)). In the Stanford-Poynter online study, readers looked at text (headlines, captions) before photos and graphics ([Poynter](https://poynter.org/?p=12643)). Informative images of real products get scrutinized while decorative ones are ignored ([NN/g](https://www.nngroup.com/articles/photos-as-web-content/)). Colored rectangles, text embedded in images, animation, and anything that "looked different" from the rest of the site trigger banner blindness. One wasted glance is enough to make users avoid that region for the rest of the visit ([NN/g](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/)). A panel of small red error tags on a tinted rectangle is close to that ad-like treatment.

Cognitive-load research explains why the draft feels like a minute's work. Adult working memory holds about **4 chunks** at once ([PMC review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11259112/)). Mayer's principles for reducing extraneous processing show large effects: in one handbook summary, coherence (cutting extraneous material) has a median **d = 1.32**, redundancy d = 0.69 and signaling d = 0.60 ([Cambridge](https://www.cambridge.org/core/books/abs/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning-coherence-signaling-redundancy-spatial-contiguity-and-temporal-contiguity-principles/C98AB3A6CE760DD63C048936EA0B3B44)). Another review reports smaller effects but the same direction ([Synapse](https://www.synapsesocial.com/es/papers/69dbbbdacebd566818835a69)). Spatial contiguity means related words and pictures belong next to each other ([Dartmouth](https://services.dartmouth.edu/TDClient/1806/Portal/KB/PrintArticle?ID=171655)). Long orthogonal arrows are a sign that the related items are not next to each other. They also force the eye to trace paths one at a time, which is slow. One caveat applies: Mayer studied learners over minutes, not marketing glances, so applying the work here is reasonable inference rather than proof.

The before/after format itself is sound. Four advertising studies found more positive attitudes when the "before" image sat on the left and the "after" on the right, which matches a mental timeline where the past is on the left ([SmartCompany](https://www.smartcompany.com.au/people-human-resources/training-development/should-the-image-be-on-the-left-or-right/)). Placing the two images side by side was easier to understand than fusing them into one, but it also made viewers think harder ([Marketing Management Journal](https://marketingmanagementjournal.scholasticahq.com/article/151065.pdf)). So the difference between the two panels has to be obvious without reading either one. Animation is not a shortcut. Tversky and colleagues found that animation's apparent advantage usually disappears once the static version carries the same information ([Tversky et al.](https://hci.stanford.edu/courses/cs448b/papers/Tversky_AnimationFacilitate_IJHCS02.pdf)), and NN/g lists peripheral motion as both a distraction and an ad signal ([NN/g](https://www.nngroup.com/articles/animation-usability/)). Lynkk should start from a static frame that works on its own.

## Competitors show one meeting and one output, never a three-zone diagram

Almost no AI meeting assistant uses a literal "meeting to output" diagram as its 2026 homepage hero. Heroes fall into three groups: collages of real UI fragments, abstract backgrounds where the copy does all the work, or a single structured note card. The clearest product-explaining visuals sit on use-case pages or in the second section of the page.

| Product | Hero headline | Hero visual | What it teaches Lynkk |
|---|---|---|---|
| Fireflies Sales ([fireflies.ai/sales](https://fireflies.ai/sales)) | "Spend Your Day Closing Deals" | Webcam tile of a rep on the left, structured deal note ("Deal Status & Timeline", "Pain Points") on the right, logo strip along the bottom | Clearest frame found: one call, one note, domain-specific headings |
| Fireflies home ([fireflies.ai](https://fireflies.ai/)) | "The #1 AI Assistant For Your Meetings" | One "Kickoff Call" note with action items popping out as chips with owner names and avatars | Owner chips show "tasks get assigned" without arrows |
| Jamie ([meetjamie.ai](https://www.meetjamie.ai/)) | "The meeting intelligence platform you can trust." | Stacked status cards: "Lead created, 4 fields written / Owner, stage, mandate, next step / Running" | A receipt-style card makes an integration action concrete |
| Granola ([granola.ai](https://www.granola.ai/)) | "The AI notepad for back-to-back meetings" | Notepad with "My notes / Enhanced" tabs; note beside a 6-person call with a small recording pill | Closest analogue to raw vs structured notes, shown with a tab toggle |
| Krisp ([krisp.ai](https://krisp.ai/)) | "Voice AI for meetings" | One app window with animated callout pills ("Bot-free", "In-person meetings") | One static UI, with the labels doing the explaining |
| Read.ai ([read.ai](https://www.read.ai/)) | "Meetings In, Decisions Out" | Floating UI chips joined by thin connector lines over a photo | The headline formula is strong; the collage is busy |
| Fathom ([fathom.ai](https://www.fathom.ai/)) | "AI notetaking that is out of this world" | Dark collage of UI fragments mixed with space illustrations | Many features, no single story |
| Otter, Fellow, Gong ([otter.ai](https://otter.ai/), [fellow.ai](https://fellow.ai/), [gong.io](https://www.gong.io/)) | Category or outcome lines | Blurred gradient, abstract light bars, stars | The copy carries all the meaning |

Three patterns stand out. First, **"before, during, after" is everywhere but never drawn as a single timeline**. Otter uses it as a heading over feature cards, Granola and Krisp as tabs, Read.ai as three text steps, and Jamie as a five-step carousel ([otter.ai](https://otter.ai/), [granola.ai](https://www.granola.ai/), [krisp.ai](https://krisp.ai/), [read.ai](https://www.read.ai/), [meetjamie.ai](https://www.meetjamie.ai/)). Competitors show one moment at a time. Lynkk's draft shows the whole timeline plus two outcomes at once, which is denser than anything in the set. Second, **no competitor shows a messy notepad beside a structured note**, so that comparison is distinctive to Lynkk and worth keeping. Third, **"bot-free" has become a standard hero claim** for Granola, Fathom, tl;dv, Krisp, Jamie and Bluedot, and no hero shows an assistant speaking in a meeting ([granola.ai](https://www.granola.ai/), [fathom.ai](https://www.fathom.ai/), [tldv.io](https://tldv.io/), [krisp.ai](https://krisp.ai/)). That cuts against putting a voice assistant in the hero. Sacra reports that Granola dropped live note expansion because "even useful live AI output pulled people away from the conversation" ([Sacra](https://sacra.com/chat/h/bb316bee-0809-4c7d-a859-4095ed2142a1/)), so any in-call moment Lynkk shows should look calm and on demand.

Use-case pages work best when they keep one layout and change the headings inside the note. Fireflies' sales note says "Deal Status & Timeline" and "Pain Points" ([fireflies.ai/sales](https://fireflies.ai/sales)), so visitors recognize their own meeting from the headings. No competitor legal or recruiting hero was found, which leaves Lynkk free to own those with headings such as "Key facts" and "Documents to collect". No public A/B tests of any of these heroes exist. The only published comparisons are generic ones, such as a VWO case where a static image beat a two-minute video ([VWO](https://vwo.com/blog/image-outperforms-video-increases-monthly-revenue/)). The ranking above is a judgment call, not test data, and that is one more reason to run Lynkk's own test.

## The draft asks for twenty fixations and never shows Lynkk

The ranking below is a heuristic audit based on the written draft spec. Its main problems: too many focal points, a product that never appears, text that is unreadable on phones, and a reading order that starts with the negative panel.

| Severity | Confusion risk in the draft | Why it matters |
|---|---|---|
| 1 | **About 20 competing elements**: header label, legend, waveform, 3 markers, 3 speech bubbles, "Note ready" pill, 3 arrows, 6 notepad fragments, 4 red tags, 2 panel headers with sublabels, 3 cards with timestamp chips, caption, and 3 color systems | Far above the roughly 4 chunks a viewer can hold; visual complexity is judged within 17 ms |
| 1 | **Lynkk is not a visible actor**. No logo, bot tile or recording chip on the timeline; the legend names only "Laura, lawyer" and "Client" | Cause and effect have to be inferred from arrows. The live pages already solve this with "Lynkk Notetaker joined" and "Recording the room" ([team-standups](https://lynkk.ai/use-cases/team-standups), [lawyers](https://lynkk.ai/use-cases/lawyers)) |
| 1 | **Mobile legibility**. A 1600 px canvas shown at about 343 px (a 375 px phone minus 16 px gutters) is scaled to 21%, so 24 px source text renders at about 5 px | Quotes, tags and card bodies become unreadable; only shapes survive. Source text needs to be about 56 px to render at 12 px |
| 2 | **The negative comes first**. The left "Without Lynkk" panel, with four bold red tags, is the loudest element and sits where the eye lands | Skimmers may think the notepad, or the red tags, are what Lynkk produces |
| 2 | **Arrow routing**. Three same-colored arrows run across the canvas into the right panel only | Tracing them is slow work, and the left panel looks disconnected from the meeting |
| 2 | **Lawyers story mismatch**. The draft says "Google Meet · 38 min"; the live lawyers hero says the meeting is "in the office" and Laura's story is in-room recording on the Mac app ([lawyers](https://lynkk.ai/use-cases/lawyers)) | A lawyer scrolling down the page sees two different meetings |
| 2 | **Ambiguous "you"**. "Typed by you, while trying to listen" next to a third-person "Laura" legend | The reader can't tell whose notes these are |
| 2 | **"▶ 11:20" chips look like video play buttons** | Nothing says they replay the audio |
| 3 | Meta header label, "The meeting · what was said, minute by minute", describes the diagram, not the benefit, and it is the first text read | It wastes the most-read position |
| 3 | "notice 2/9??" reads as 9 February in the US and 2 September elsewhere | It may read as a deliberate wrong fact rather than a messy note |
| 3 | "Note ready in 30 s" is cryptic and sits where the arrows run | Easy to miss, and the site words this claim inconsistently (see below) |
| 3 | Full-sentence quotes in bubbles repeat the same facts as the cards | The reader reads the key content twice (redundancy) |
| 3 | The blinking cursor and same-green markers | A cursor is a stray bar in a static image; speaker attribution depends on bubble color alone |

The live site adds its own confusion. **The draft hero would duplicate the slider already on the page**: every use-case page checked has a draggable "Without Lynkk / With Lynkk" slider lower down, with the same messy-notepad idea ([lawyers](https://lynkk.ai/use-cases/lawyers), [team-standups](https://lynkk.ai/use-cases/team-standups), [sales-calls](https://lynkk.ai/use-cases/sales-calls)). The lawyers page also differs from the draft on smaller details. The live notepad is "new client.txt" with "notice 2nd?? or 12th", while the draft uses "new note.txt" and "notice 2/9??". The live transcript timestamps are 11:20, 11:34 and 11:37; the draft markers are 11:20, 22:30 and 35:12 ([lawyers](https://lynkk.ai/use-cases/lawyers)).

**Claims the live site does not support.** The brand memory file (`/home/user/claude/memory/lynkk-brand.md`) lists "CRM fields updated" as an after-meeting feature, and its ready-to-use directory copy promises "CRM updates". It also gives the tagline "joins your meetings, speaks when needed" and says users "get answers live, in the meeting, by voice". The live sales page FAQ says Lynkk **does not work with CRMs yet** ([sales-calls](https://lynkk.ai/use-cases/sales-calls)). The integrations page marks HubSpot "Soon" and does not mention Salesforce ([integrations](https://lynkk.ai/integrations)). The only in-call answer shown anywhere appears **as text in a side panel**, on the sales page ([sales-calls](https://lynkk.ai/use-cases/sales-calls)). "Cue" in-call answers are named only on the homepage Pro pricing card ([lynkk.ai](https://lynkk.ai/)). The pricing page doesn't list them ([pricing](https://lynkk.ai/pricing)), and no live page says Lynkk speaks. Neither claim belongs in the hero, and the brand memory and submission copy should be fixed before they go to directories.

A first-time visitor who clicks around will also find numbers that disagree. The homepage Free card says "Unlimited recording", while pricing says "5 notes per month" ([lynkk.ai](https://lynkk.ai/), [pricing](https://lynkk.ai/pricing)). How-it-works shows a "15+ langs" chip while its body text and the FAQ say 17 languages. The same page promises notes "in under 30 seconds" but also says notes arrive "shortly after the recording finishes uploading" ([how-it-works](https://lynkk.ai/how-it-works), [faq](https://lynkk.ai/faq)). Any "30 seconds" label in the graphic inherits that inconsistency.

## Ship a two-panel hero with Lynkk on the strip

### Prioritized changes

| Priority | Change |
|---|---|
| **Must do** | Fix the lawyers story: change "Google Meet" to "In the office" (or rewrite the page to match the draft). Align the notepad text ("new client.txt", "notice 2nd?? or 12th") and timestamps with the live page |
| **Must do** | Keep CRM updates and voice answers out of the graphic, the headline and the alt text. Reconcile the brand memory file and its submission copy with the live site |
| **Must do** | Show Lynkk as the actor: a "Lynkk is recording the room" chip with the logo at minute 0 on the meeting strip ("Lynkk Notetaker joined" for video-call variants), plus the Lynkk mark in the right panel header |
| **Must do** | Make the "With Lynkk" note dominant: about two thirds of the width, full contrast, accent color. Desaturate the "Without" notepad and cut the four red tags to one footer line |
| **Must do** | Replace the three long arrows with number badges: "1, 2, 3" on the strip matches "1, 2, 3" on the cards. Keep at most one broad arrow from the strip to the note, or none |
| **Must do** | Put an outcome headline and subhead in HTML beside or above the image, not baked into it. The headline states the claim; the graphic confirms it |
| **Must do** | Produce a separate mobile crop: the meeting strip plus the "With Lynkk" note only, two cards, source text at least about 56 px |
| **Should do** | Delete the waveform and the meta header label. Cut the speech bubbles, or shorten them to 3-5 words and attach each to its card |
| **Should do** | Pick one voice. "Your notes / Lynkk's note" suits a visitor-centred page; "Laura's notes" suits the persona story. Don't mix them |
| **Should do** | Swap the "▶" triangle for a speaker icon and add "Tap a time to hear it" near the first card |
| **Should do** | Resolve the duplication with the slider. Use the simplified two-panel image as the hero, and move the full numbered timeline (moment 1 into card 1, and so on) into the slider or a "how it works" section, where visitors read at their own pace |
| **Should do** | Add one lawyers-specific trust badge: "Recorded with the client's permission" or "Stored in the region you choose" |
| **Should do** | Pick one timing phrase across the graphic, how-it-works and the FAQ. "Note ready when the meeting ends" is the safe default until "about 30 seconds" is confirmed |
| **Should do** | Fix the site-wide inconsistencies a cold visitor will hit: unlimited recording vs 5 notes, 15+ vs 17 languages, and "Cue" appearing only on the homepage card |
| **Nice to have** | One memory hint line in the right panel, tagged Pro (memory is Pro while the lawyers card is Free): "Next time, ask Lynkk what the client said about the notice." |
| **Nice to have** | A single-play reveal (moment 1 lights card 1, and so on) that ends on the static frame, does not loop, respects reduced-motion settings, and is tested against the static version |
| **Nice to have** | Turn the layout into a template: same frame, domain-specific note headings per use case (lawyers: Key facts, Documents to collect, Next step; standups: Yesterday, Today, Blocked; sales: What is still open, Next step, Task sent to Jira) |

### Headline and label copy

Every line below reuses the live site's plain voice ("You listen. Lynkk writes." already appears on the lawyers page) and avoids unsupported claims.

| Slot | Recommended copy (alternates in parentheses) |
|---|---|
| Hero headline, lawyers | "You listen to the client. Lynkk writes the note." ("Look at your client, not your notepad.") |
| Subhead, lawyers | "Lynkk records the meeting with your client's permission, then writes the key facts, the documents to collect, and the next step. Every line links to the moment it was said." |
| Hero headline, standups | "Nobody takes notes. Lynkk writes the standup." |
| Hero headline, sales | "You talk. Lynkk writes the notes." (no CRM promise; "Tasks go to Jira" is supported) |
| Meeting strip label | "Client meeting, 38 min, in the office" |
| Actor chip | "Lynkk is recording the room" (video calls: "Lynkk Notetaker joined") |
| Left panel | "Your notes", sublabel "Typed while trying to listen" |
| Left footer (replaces red tags) | "3 key moments. None written down in full." |
| Right panel | "Lynkk's note", sublabel "Ready when the meeting ends" |
| Timestamp helper | "Tap a time to hear it." |
| Memory hint (Pro) | "Next time, ask Lynkk what the client said about the notice." |
| Mobile caption | "You listen. Lynkk writes." |
| Alt text | "A 38-minute client meeting recorded by Lynkk. On the left, rushed, incomplete notes. On the right, Lynkk's note with key facts, documents to collect, and a next step, each linked to the moment it was said." |

### Proposed layout

The desktop frame stays left to right (past, then future) with three groups to read: the strip, the weak panel and the strong panel. The headline sits outside the image in HTML.

```
+------------------------------------------------------------------+
| [Lynkk logo] Lynkk is recording the room                          |
| Client meeting, 38 min, in the office    (1)-----(2)-----(3)      |
+--------------------+---------------------------------------------+
| Your notes         | [Lynkk] Lynkk's note    Ready when it ends  |
| (muted, grey)      |                                             |
| new client.txt     | (1) Key facts             [speaker] 11:20   |
| notice 2nd?? 12th  | (2) Documents to collect  [speaker] 11:34   |
| (can't read this)  | (3) Next step: owner, due [speaker] 11:37   |
|                    |                                             |
| 3 key moments.     | Tap a time to hear it.                      |
| None written down. |                                             |
+--------------------+---------------------------------------------+
```

On mobile the left panel goes away entirely: the strip with the actor chip sits on top, and the "Lynkk's note" panel below shows cards 1 and 2 with text drawn at about 56 px source size. The before/after contrast then moves to the existing slider, which already works as a swipe interaction on phones.

## A ten-person, one-afternoon five-second test

The five-second test is the standard cheap check: show the design for a fixed time, hide it, then ask what the visitor remembers. Lyssna's guide says **5-10 participants usually reveal the major patterns**, that when **more than about 80%** get the main message the design is probably working, and that similar wrong answers point to one specific misleading element. It also says the most important question should come first and that leading questions should be avoided ([Lyssna](https://www.lyssna.com/guides/five-second-testing/)). Lyssna lets you share a test link for free or recruit from its panel, and results arrive within hours ([Lyssna](https://www.lyssna.com/features/five-second-testing-software/)). For verified B2B buyers, Wynter tests start at about **$199** ([GTM Directory](https://thegtmdirectory.com/tools/wynter)). The 80% bar is a vendor rule of thumb, not a published norm, and no SaaS-specific benchmark exists. Treat a pass as directional.

| Element | Plan |
|---|---|
| Variants | A: current draft. B: simplified two-panel layout with the strip and actor chip. C: right panel and strip only. D: the static end frame of any animated version |
| Context | Show each variant inside a screenshot of the full hero (headline, subhead, CTA) at real viewport size, once at 1440 px desktop and once at 375 px mobile. Run variant B a second time without the headline to measure what the graphic contributes on its own |
| Participants | 10 per variant, different people for each, close to the target buyer (lawyers or legal staff for the lawyers page; PMs or founders for standups). Lyssna panel or a shared link to friendly contacts; Wynter if the panel needs to be verified B2B |
| Exposure | Exactly 5 s for everyone. Optionally repeat with 8 s, which Paul Boag uses ([Frontend Masters](https://frontendmasters.com/teachers/paul-boag/user-tests-8-second/)), to see whether the draft passes when given more time |
| Questions | Q1 "What does this product do?" Q2 "What did you notice first?" Q3 "Who is it for?" Q4 "Was anything confusing?" Optional Q5, a 1-5 rating of how clear the page was |
| Scoring | Q1 passes if the answer says the product records the meeting and writes the notes or tasks for you. Pass bar: 8 of 10 |
| Diagnostics | Many "the timeline" or "the arrows" answers to Q2 mean the hierarchy points at the process. Answers like "a notes app" or "it fixes messy notes" mean the negative panel is winning. Mentions of "video call" on the lawyers variant mean the Google Meet label survived |
| Decision | Ship the simplest variant that passes on mobile. If B and C both pass, prefer C on mobile and B on desktop. If nothing passes without the headline, that is acceptable as long as the hero passes with it, since the headline is meant to carry the claim |

## Conclusion

The draft fails for a reason that is good news: it tries to show the whole product, and the product has a lot to show. The evidence and the competitor set point the same way. A hero confirms one claim, and the lifecycle story (before, during, after, numbered moments, memory) belongs further down the page, where visitors read at their own pace. Lynkk already owns that slot with its slider. So the redesign is mostly a reallocation: the hero shows the outcome and the actor, and the slider or a "how it works" section shows the process. That also removes the current duplication.

The bigger risk is in the copy, not the pixels. The brand memory file is the "source of truth" for directory submissions, yet it promises CRM updates and voice answers that the live site either rules out or never shows. If those claims reach a hero or a directory listing, a five-second test can't catch the problem, but a prospect's first sales call will. Fix the brand memory, the lawyers page mismatch and the "30 seconds" wording first, then test.
