# Dictation page audit: what to change, section by section

Page: https://lynkk.ai/features/dictation
Source: 8 screenshots of the live page (shared 2026-10-02). The 12:15 "Search and prompts"
section wasn't in the screenshots, so it isn't reviewed here.
Keyword data: Ubersuggest, US unless marked "global". Background research is in
`seo/dictation-page.md` and `seo/wispr-flow-teardown.md`.

---

## Summary

The page is well written and the product story is strong (the "one working day" timeline
is a good idea). The problem is SEO: **the headings use almost none of the words people
search for.**

| Keyword family | Monthly searches | On the page today? |
|---|---|---|
| AI dictation | 480 | Yes: hero pill, FAQ heading, FAQ answer |
| voice to text on Mac / mac voice to text | 1,300 + 1,600 | Only "Voice-to-text everywhere" in a small pill |
| speech to text mac | 1,600 | **No** |
| talk to text mac | 1,600 | **No** |
| voice typing on mac / mac voice typing | 480 + 390 | **No** |
| dictation app / software for Mac | 260 + 260 + 590 | **No** |
| mac dictation (Apple's built-in tool) | 1,600 | **No** |
| dictation software for Microsoft Word | 1,600 (SD 8) | **No** (Word isn't in the app list) |
| Wispr Flow alternative | 480 (SD 11) | **No** |

The fixes, in priority order:

1. **Rewrite the H1 and section headings** to include keywords, keeping the brand voice
   (section A).
2. **Pull privacy and offline up into their own section.** It's your strongest advantage
   over Wispr Flow (which processes audio in the cloud), and right now it's hidden in one
   sentence under "three steps" (section A, block 9).
3. **Add 4 missing blocks**: Lynkk vs built-in Mac dictation, meetings cross-link, more
   app names, social proof (section B).
4. **Add 5 FAQ questions** and FAQ schema (section C).
5. **Fix the title tag and meta description** (section D; I can't see these in the
   screenshots, so check them in the CMS).

---

## A. Changes to existing content (top to bottom)

Format for each block: **Current** (what's on the page now), **Change to** (the new
text), **Why**.

### 1. Hero pill (eyebrow above the H1)
- **Current:** `AI dictation for Mac · Works wherever you type`
- **Change to:** keep as is. It's already the best keyword line on the page.

### 2. Hero H1
- **Current:** `Speak instead of type.`
- **Problem:** No keyword. The H1 is the strongest on-page signal Google uses, and a new site
  with no authority can't rely on a slogan (Wispr Flow can, because 3,700 sites link to it).
  Also, "instead of typing" is the grammatical form.
- **Change to (recommended):** `Speak instead of typing. Voice to text in every Mac app.`
- **Alternative (shorter):** `Speak instead of typing, in any app on your Mac.`
- **Design option:** if the team wants to keep the short slogan visually, keep it big and
  put the keyword half on a second line in smaller type, **both inside the same `<h1>`**.
- **Keywords:** voice to text, Mac

### 3. Hero sub-paragraph
- **Current:** "Hold fn and start talking. Lynkk turns your voice into clear text in any
  app on your Mac, so your ideas can move as fast as you think."
- **Change to:** "Hold fn and start talking. Lynkk is AI dictation for Mac: it turns your
  speech to text in any app, so your ideas can move as fast as you think."
- **Keywords added:** AI dictation for Mac, speech to text

### 4. Hero trust line
- **Current:** `Start free · Set up in minutes · On the free plan, nothing leaves your Mac`
- **Change to:** keep. Optionally add `· Works offline` (the page already says the first
  draft is made on-device even offline).

### 5. Hero app strip (09:02 to 18:30 tiles) and the line "Your thoughts, written at the speed of speech."
- **Current tiles:** "Messages and email in Mail", "Support and operations in Slack",
  "Search and prompts in an AI assistant", "Visual feedback circled on screen",
  "Accessibility and comfort in the terminal", "Documents and notes in Hinglish"
- **Change:** keep the tiles. They're navigation, not headings. Make sure they are plain
  text or links, **not** `<h2>`/`<h3>`.
- **"Your thoughts, written at the speed of speech."** Keep as a tagline, but make it a
  `<p>`, not a heading.

### 6. Section intro: "Use your voice wherever words slow you down."
- **Pill:** `Built for everyday work`
- **Change H2 to:** `Use voice typing wherever words slow you down.`
- **Body:** keep, but add the keyword once: "One working day of talk to text on a Mac,
  from the first email to the last note. Six moments, six apps, one key."
- **Keywords:** voice typing, talk to text (1,600/mo, SD 14, the easiest win in the set)

### 7. Timeline headings (the six moments)

These are the most important change. Each heading should say **what you're doing + where**,
in the words people search for. Keep the time (09:02 etc.) as a separate styled label
**outside** the heading tag so it doesn't dilute the heading.

| Time | Current heading | Change heading to | Target keyword |
|---|---|---|---|
| 09:02 | Messages and email | **Dictate emails and messages in Mail** | dictate emails, voice to text email |
| 10:30 | Support and operations | **Voice to text in Slack, Teams and chat** | voice to text slack |
| 12:15 | Search and prompts | **Talk to ChatGPT and Claude instead of typing** | chatgpt voice to text (110/mo, SD 31) |
| 14:40 | Visual feedback | **Circle to capture: screenshots while you dictate** | (feature name, brand term) |
| 16:05 | Accessibility and comfort | **Voice coding in the terminal and code editor** | voice coding (390/mo) |
| 18:30 | Documents and notes | **Hinglish and multilingual voice typing** | hindi voice typing (6,600/mo global) |

**Content mismatch to fix at 16:05:** the heading says "Accessibility and comfort" but the
content and demo are about **Code mode in the terminal**. Pick one:
- (a) rename it to the coding heading above (recommended), and move the accessibility
  message into a short line: "By four your hands have typed enough." already says it; or
- (b) keep the accessibility heading and change the demo to something non-coding.

**18:30 Hinglish:** this is unique. Wispr Flow and the other Mac dictation apps don't market
Hinglish. Add one sentence: "Lynkk works out the language on every dictation, whether it's
English, Hindi, Hinglish **[confirm: other languages]**, so there is nothing to switch."
**[confirm]** whether pure Hindi comes out in Devanagari. If yes, say so: "hindi voice
typing" has 6,600 searches/month (global) with almost no competition.

### 8. "Everything you need to work without reaching for the keyboard."
- **Pill:** `One shortcut. Less typing.`
- **Change H2 to:** `An AI dictation app that works without reaching for the keyboard.`
- **Feature cards** (Speak anywhere / Polish with AI / Circle to capture): keep. Add a
  4th card that's missing: **Personal dictionary** ("Teach Lynkk names and product terms
  once"). It's already answered in the FAQ ("Will it spell names and product terms
  right?") and Wispr Flow lists it as a main feature.

### 9. "If you can type there, you can speak there." (app modes)
- **Pill:** `Voice-to-text everywhere`. Change to `Voice to text everywhere` (no hyphens;
  people search without them).
- **H2:** change to `If you can type there, you can speak there: dictation in every Mac app.`
- **App chips:** these are great for long-tail search. **Add the apps people search for,
  if Lynkk supports them:**

| Add to | Apps | Why (searches/month, US) |
|---|---|---|
| Email and Notes modes | **Microsoft Word**, **Google Docs**, Gmail, Outlook, Pages, Apple Notes | "dictation software for microsoft word" 1,600 (SD 8); "microsoft word dictation software" 1,300; "voice to text gmail" 140 |
| Chat mode | Google Chat, LinkedIn | |
| Code mode | Claude Code, Warp, Windsurf | developer searches ("wispr flow claude code" shows demand) |
| New group: AI assistants | ChatGPT, Claude, Gemini, Perplexity | "chatgpt voice to text" 110 |

**[confirm]** each app works before adding it.

### 10. "Go from thought to finished text in three steps."
- **Pill:** `Simple by design`
- **Change H2 to:** `How to use voice to text on Mac in three steps.`
  (matches "how to use voice to text on mac" 210/mo and "how to voice to text on mac" 210/mo)
- **Right-hand paragraph:** "The first draft is written on your Mac the moment you let go,
  even offline: Apple's newest on-device model on macOS 26, its earlier one on macOS 14.2 to
  15. Lynkk runs on Apple silicon."
  **Move this paragraph to the new privacy section (B2)** and replace it here with: "Place
  your cursor, hold fn, let go. It works in any text field on your Mac."
- **Steps 01 to 03:** keep. They're clear and they include the voice commands ("new
  paragraph", "scratch that", "send"). Good.

### 11. "Say it roughly. Send it clearly." (Polished vs Instant)
- **Pill:** `From spoken to polished`
- **Change H2 to:** `Say it roughly. Send it clearly. AI cleans up your dictation.`
- **Body:** keep. Add "filler words" once, since people search for it:
  "...Polished, where the ums, filler words, repeats and false starts are cleaned up and
  your wording stays."
- **The demo box "After 'shorter' · Pro" is empty in the screenshot.** Check it renders
  (it may be an animation that hadn't run). If the output is shown only by JavaScript,
  Google may not see it. Put a static example in the HTML.

### 12. FAQ: "Frequently asked questions about AI dictation"
- **H2:** keep, it's good.
- **Questions:** keep all 9. Add 5 more (section C).
- **Check:** the answers must be in the HTML when the page loads, even when collapsed
  (accordion text loaded later by JavaScript may not get indexed).
- **"What is Lynkk?" answer:** good. Add one line: "Lynkk is also a meeting assistant;
  dictation is part of the same Mac app." and link to the meetings page.

### 13. Final CTA: "Your next sentence is easier to say."
- **Change the sub-line to:** "Hold fn, speak your mind, and Lynkk turns your voice into
  clear text wherever you work on your Mac."
- **Small print:** `Start free · Apple silicon, macOS 14.2 or later`. Keep. This is useful
  information, and it's currently low contrast on the orange background. Make it darker.

### 14. Footer
- **Current:** "Meeting memory for teams. It records, it writes things down, and it
  remembers." `admin@lynkk.ai`
- **Change:** link "Meeting memory for teams" to the meetings page. Consider using the
  marketing@ address (per `memory/lynkk-brand.md`) unless admin@ is intentional.

---

## B. Content to add (missing blocks)

### B1. "Lynkk vs built-in Mac dictation" (new section, place after block 11)
Targets: mac dictation (1,600), how to use mac dictation (720), mac dictation not working
(480), wispr flow vs mac dictation. Everything in this table is already stated on your page.

> **H2:** Lynkk vs Apple's built-in Mac dictation
>
> | | Built-in Mac dictation | Lynkk |
> |---|---|---|
> | Works in any text field | Most apps | Yes, with a mode per app (Email, Chat, Notes, Code) |
> | Cleans up ums, repeats and false starts | No | Yes (Polished, Pro) |
> | Edit by voice ("shorter", "make that a list") | No | Yes (Pro) |
> | Code mode for terminals and editors | No | Yes, nothing runs by accident |
> | Circle something on screen while you talk | No | Yes (Circle to capture) |
> | Hinglish written in English letters | No | Yes (Pro) |
> | Works offline, on-device | Yes | Yes, first draft on-device |

### B2. Privacy and offline section (new section, place after block 10)
This is where Lynkk beats Wispr Flow, which (per third-party reviews) sends audio to its servers even in Privacy Mode.
Right now it's spread across the hero trust line, one paragraph and the FAQ.

> **Pill:** Private by default
> **H2:** Private, offline dictation that stays on your Mac
> - **On-device first draft.** Apple's on-device speech model writes the first draft on
>   your Mac, even offline.
> - **Free plan: nothing leaves your Mac.**
> - **Never on your clipboard.** Lynkk types the text in and checks every insert.
> - **Won't listen in password fields.**
> - **On Pro:** **[confirm and state plainly what is sent for Polished/Hinglish, where it
>   is processed (data region), and whether it's stored]**

### B3. Meetings cross-link (new section, place before the FAQ)
Your footer says Lynkk is "meeting memory for teams," but the dictation page never mentions
meetings. Visitors who arrive for dictation never find out about the main product, and the
page passes no internal links to it.

> **H2:** Dictation is half the job. Lynkk remembers your meetings too.
> Before a call, Lynkk brings context from past meetings. During it, it can answer by voice.
> After it, you get notes, action items, CRM updates and Jira tickets. Then use dictation
> to write the follow-ups.
> **[Link: See how Lynkk works in meetings]**

### B4. Social proof
No testimonials, user count, ratings or logos are visible. Add even 2 or 3 short quotes
from beta users near the hero or before the final CTA. It helps conversion, and the
reviews can later go into the `aggregateRating` schema.

### B5. Optional: speed stat
Wispr Flow leads with "4x faster than typing". If Lynkk has its own number (for example
words per minute speaking vs typing), add it to the hero or block 8. Don't use a number
you can't back up.

---

## C. FAQ: add these questions

Keep the existing 9. Add these (each targets a real search):

| New question | Target search (US/mo, SD) | Suggested answer (from what the page already says) |
|---|---|---|
| How do I use voice to text on a Mac? | how to use voice to text on mac (210, 32) | Download Lynkk for Mac and sign in. Click into any text field, hold fn (or the key you picked) and speak. Let go, and your words are typed where your cursor is. To use Apple's built-in dictation instead, turn it on in System Settings > Keyboard > Dictation. |
| Does Lynkk work offline? | (privacy intent) | Yes. The first draft is written on your Mac by Apple's on-device speech model, even with no internet connection. On the free plan, nothing leaves your Mac. **[confirm: which Pro features, such as Polished and Hinglish, need a connection]** |
| Does Lynkk replace Apple's dictation shortcut? | mac dictation shortcut (480, 28) | No, you can keep both. Apple's built-in dictation starts when you press fn (Globe) twice. Lynkk starts when you hold fn, and you can pick a different key in Lynkk's settings. **[confirm: how the two behave on the same key]** |
| Does Lynkk work in Microsoft Word and Google Docs? | dictation software for microsoft word (1,600, **8**) | Yes. Lynkk types into any text field on your Mac, including Microsoft Word and Google Docs in your browser. Say "new paragraph" to start a new paragraph, or "scratch that" to drop the last bit. **[confirm: tested in both]** |
| Is Lynkk a Wispr Flow alternative? | wispr flow alternative (480, **11**) | Yes. Like Wispr Flow, Lynkk turns your voice into clean text in any app. Lynkk writes the first draft on your Mac, even offline, and adds Code mode for terminals and code editors, circle to capture, and Hinglish. It is also a meeting assistant that remembers your calls. |

Also: mark up all FAQ questions with **FAQPage** JSON-LD (template in
`seo/dictation-page.md`, section 6).

---

## D. Title, meta and technical

I can't see these in the screenshots. Check them in the CMS or with View Source.

| Item | Recommended |
|---|---|
| Title tag | `AI Dictation for Mac: Voice to Text in Any App \| Lynkk` (54 chars) |
| Meta description | `Hold fn and talk. Lynkk is AI dictation for Mac that turns speech to text in any app, cleans up filler words and works offline. Start free.` (138 chars) |
| H1 | Only one `<h1>` on the page (the hero). Section titles should be `<h2>`, timeline titles `<h3>` |
| Timeline times (09:02 etc.) | Outside the heading tags |
| Accordion FAQ answers | In the HTML on page load |
| Demo text (Polished output, "shorter" result) | Static text in the HTML, not only drawn by JavaScript or canvas |
| Images and demo videos | Alt text with keywords, e.g. `Lynkk AI dictation typing an email in Mail on Mac`, `Voice to text in Slack with Lynkk Chat mode`, `Voice coding in iTerm with Lynkk Code mode` |
| Schema | `SoftwareApplication` (operatingSystem: `macOS 14.2 or later`, Apple silicon, free offer) + `FAQPage` |
| Internal links | To the meetings page, pricing (Free vs Pro), help center, and from homepage/nav to this page |

---

## E. Facts confirmed from the live page

These were open questions in `seo/dictation-page.md`. The page answers them:

- Shortcut: **hold fn**, or another key you pick
- Requirements: **Apple silicon, macOS 14.2 or later**
- **On-device and offline**: first draft by Apple's on-device model (macOS 26: newest model; 14.2 to 15: earlier one)
- **Free plan: nothing leaves your Mac**
- Modes picked automatically per app: **Email, Notes, Chat, Code** (default for everything else)
- **Instant** vs **Polished** output; "Use my words" restores the raw text; Undo removes the whole insert
- Cleanup (Polished) is on **Pro**; "shorter" and "make that a list" voice edits are **Pro**; **Hinglish is Pro**
- Voice commands: "new paragraph", "scratch that", "send" (presses Return; never in Code mode)
- **Circle to capture**: circle something on screen while talking, and the image is pasted with the sentence
- Language is detected on every dictation, no switching
- Never leaves text on the clipboard; doesn't listen in password fields
