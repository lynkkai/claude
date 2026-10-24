# Transcription feature pages: SEO fixes and new copy

Pages:
- https://lynkk.ai/features/multilingual-transcription (owns "multilingual meeting transcription")
- https://lynkk.ai/features/hinglish-transcription (owns "hinglish transcription" and "code switching transcription")

Goal: stop the multilingual page competing for "Hinglish" queries, give the Hinglish page
copy of its own instead of text shared with the multilingual page, and fix the factual
contradictions found in the audit (2026-10-24).

**Language count, used everywhere below:** 17 languages (13 plus 4 in beta), plus Hinglish
mode and auto-detect. Hinglish is a mode, not one of the 17. That matches the settings step
("pick Hinglish, Auto-detect, or one of the 17 languages"). The live pages counted Hinglish
inside the 17, which made the list add up to 18.

Items marked **[CONFIRM]** need a product check before going live.

---

## Part 1: Multilingual page (changes only)

Keep the page structure. Change only the items below. Everything not listed stays as is.

### Head tags

| Tag | New value | Length |
|---|---|---|
| `<title>` | Multilingual Meeting Transcription in 17 Languages \| Lynkk | 58 |
| `meta description` | Transcribe meetings in 17 languages plus auto-detect, with speaker labels in every language and a transcript you can search. Free on every plan. | 144 |
| `meta keywords` | multilingual transcription, multilingual meeting transcription, meeting transcription in multiple languages, ai transcription languages, speaker diarization transcription | |
| `og:title` / `twitter:title` | Meeting transcription in 17 languages | 37 |
| `og:description` / `twitter:description` | 17 languages plus auto-detect, with speaker labels in every language. | 69 |
| `og:image:alt` | Meeting transcription in 17 languages | |

Removed from keywords: `hinglish transcription` and `code switching transcription` (both now
belong to the Hinglish page).

### Schema

- `SoftwareApplication.description` and `WebPage.description`: same as the new meta description.
- `WebPage.name`: Multilingual Meeting Transcription in 17 Languages
- FAQPage: update the two answers changed below so the schema matches the visible text.

### H1

> Multilingual meeting transcription in 17 languages

### Intro (replaces the paragraph under the H1)

> A lot of teams work in more than one language: a sales call in Spanish, a standup in
> English, a customer interview in Japanese. Lynkk transcribes 17 languages plus auto-detect,
> labels who said what in every one of them, and turns each meeting into a note you can search.

### Card 1 (replaces "Hinglish when you need it")

**H2:** Mixed Hindi and English calls

> Hindi and English in the same sentence? Lynkk has a dedicated Hinglish mode for that.
> See [Hinglish transcription](/features/hinglish-transcription).

### Card 3 (replaces the "17 languages" card text)

**H2:** 17 languages (heading unchanged)

> English, Hindi, Spanish, French, German, Portuguese, Italian, Dutch, Japanese, Chinese,
> Korean, Arabic and Russian, plus Tamil, Telugu, Marathi and Bengali in beta. Or let
> auto-detect work out the language for you.

### Section "Hinglish, auto-detect or one language"

**New H2:** Pick a language or let it detect

> Each setting suits a different kind of call. Auto-detect works out the main language of a
> recording, which suits a team whose calls are each in one language but not always the same
> one. Picking a single language tells the engine exactly what to expect, which is the best
> choice when every call is in that language. If people mix Hindi and English inside
> sentences, use [Hinglish mode](/features/hinglish-transcription) instead.

### FAQ: two answers to replace

**Which languages can it transcribe?**

> 17, plus auto-detect: English, Hindi, Spanish, French, German, Portuguese, Italian, Dutch,
> Japanese, Chinese, Korean, Arabic and Russian, with Tamil, Telugu, Marathi and Bengali in
> beta. There is also a Hinglish mode for Hindi and English mixed in one sentence. Speaker
> labels come with every transcript.

(The old answer said "English (the default)", which contradicted the next FAQ and the
"How it works" step, both of which say Hinglish is the default.)

**Can it handle people switching languages mid-sentence?**

> For Hindi and English, yes: that is what [Hinglish mode](/features/hinglish-transcription)
> is for, and it is the setting a new account starts with. For other pairs, pick the main
> language of the call or use auto-detect, which works out the main language of the recording.

### Related guides

Add: [Hindi Transcription in India](/blog/hindi-transcription)

---

## Part 2: Hinglish page (full copy)

Every section is rewritten, so no paragraph repeats the multilingual page word for word.
Facts are unchanged from the live pages unless marked [CONFIRM].

### Head tags

| Tag | New value | Length |
|---|---|---|
| `<title>` | Hinglish Transcription for Meetings \| Lynkk (unchanged) | 43 |
| `meta description` | Hinglish transcription for meetings where Hindi and English mix mid-sentence. Speaker labels, searchable notes and action items. Free on every plan. | 148 |
| `meta keywords` | hinglish transcription, hinglish meeting transcription, hindi english transcription, code switching transcription, hinglish speech to text, hinglish transcription ai | |
| `og:title` / `twitter:title` | Hinglish transcription for meetings (unchanged) | 35 |
| `og:description` / `twitter:description` | Hindi and English in one sentence, kept as one sentence, with speaker labels. (unchanged) | 77 |

The old meta description ended "One of Lynkk's 17 languages", which is wrong under the
corrected count (Hinglish is a mode on top of the 17).

### Schema

- `SoftwareApplication.description` and `WebPage.description`: same as the new meta description.
- FAQPage: replace with the FAQ below, so the schema matches the visible text.

### Eyebrow

> Feature · Hinglish

### H1 (unchanged)

> Hinglish transcription for meetings that mix Hindi and English

The current H1 is already right: it starts with the exact query and says what Hinglish
means. Only the multilingual H1 needed to change.

### Intro

> In plenty of Indian workplaces, nobody sticks to one language. A sentence starts in Hindi,
> picks up an English product name, and finishes in Hindi again. Lynkk's Hinglish mode is
> built for exactly that kind of meeting: the transcript follows the conversation the way
> people actually spoke it, labels who said what, and becomes a note you can search.

CTA: Get started free

### Three cards

**H2:** One sentence stays one sentence

> Most tools force a call into one language and garble the rest. Hinglish mode listens for
> Hindi and English together, so a sentence that switches halfway through comes out as one
> sentence, not two broken halves.

**H2:** Names on every line

> Every transcript is split by speaker. When the meeting bot records, the labels use the names
> people have in the meeting, and the Mac app marks your own voice as You.

**H2:** On from day one

> Hinglish is the setting every new account starts with. Nothing to switch on, and it covers
> the meeting bot, the Mac app, the Chrome extension and the browser alike.

### New section: What a Hinglish transcript looks like

**H2:** What a Hinglish transcript looks like

> Here is the kind of exchange Hinglish mode is built for:
>
> **Priya:** Okay, toh client ne kal call pe bola ki they need the deck by Friday.
> **Rahul:** Friday tak? Theek hai, main pricing slide update kar deta hoon, but legal review abhi pending hai.
> **Priya:** Legal ko main aaj ping kar dungi.
>
> Each line keeps both languages, and each speaker keeps their name. From there, Lynkk picks
> out the work: Rahul updates the pricing slide, Priya pings legal today.

**[CONFIRM]** Which script does Hinglish output use for Hindi words: Roman (as above),
Devanagari, or a mix? The sample must match real output. If it's Devanagari, rewrite the
Hindi words in the sample in Devanagari. Then add one plain sentence stating the script,
for example: "Hindi words come out in Roman script, the way most people type Hinglish."
Searchers ask this, and the page doesn't currently answer it. A real screenshot from a test
call would be even better than text.

### New section: Where teams use it

**H2:** Where Hinglish mode helps

> - **Sales calls:** customers explain their needs in whatever mix comes naturally, and the
>   follow-up still gets every detail. [Sales calls](/use-cases/sales-calls)
> - **Team standups:** quick updates in Hindi and English, with each task tied to the person
>   who took it. [Team standups](/use-cases/team-standups)
> - **User and customer interviews:** people speak more freely in their own mix, and you keep
>   their exact words. [User interviews](/use-cases/user-interviews)
> - **1:1s:** the conversation stays relaxed, and the notes still capture what was agreed.
>   [1:1 meetings](/use-cases/one-on-one-meetings)

### How it works

**H2:** How it works

> From the recording to the note, a Hinglish meeting goes through five steps.
>
> 1. Go to Settings, then Transcription, and make sure Hinglish is selected. New accounts
>    start on it.
> 2. Record however suits the meeting: the meeting bot, the Mac app, the Chrome extension or
>    the browser.
> 3. Once the recording uploads, Lynkk sends it for transcription in Hinglish mode, with
>    speaker labels on.
> 4. The transcript comes back split by speaker, and Lynkk writes the summary, action items and
>    decisions from it.
> 5. The note is searchable, by meaning or by the exact words people used, in either language.

**[CONFIRM]** "in either language" in step 5: check that search finds both Hindi and English
words in a Hinglish transcript. If it doesn't, cut those three words.

### Choosing a setting

**H2:** Hinglish, Hindi or auto-detect

> Three settings cover Hindi speakers, and the right one depends on how your calls sound.
> When people mix Hindi and English inside sentences, keep Hinglish. When a call is in Hindi
> from start to finish, pick Hindi. When every call is in one language but it varies from
> call to call, auto-detect works out the main language of each recording. Your calls go
> beyond Hindi and English? Lynkk also covers
> [17 languages plus auto-detect](/features/multilingual-transcription), and you can switch
> any time.

**[CONFIRM]** That Hindi alone gives a better transcript than Hinglish on Hindi-only calls.
That's what the multilingual page's "pick a single language" advice implies, but check it.
If Hinglish handles Hindi-only calls just as well, drop the Hindi sentence.

### Speaker labels

**H2:** Speaker labels when the room switches languages

> Switching languages doesn't confuse who is talking. Speaker labels work in Hinglish exactly
> as they do in any other language, so every action item and decision lands with the right
> person. Bot recordings take names from the meeting itself; on the Mac app your voice sits on
> its own channel, labelled You.

### Limits

**H2:** What to expect, and the limits

> Clear audio gives the best Hinglish transcript. Before you rely on it, know that:
>
> - Auto-detect only picks one main language per recording, so it isn't built for
>   mid-sentence switching. For mixed Hindi and English, stay on Hinglish.
> - Mixing English with Tamil, Telugu, Marathi or Bengali isn't covered by Hinglish mode.
>   Those four languages are in beta: pick the main language of the call.
> - Indian names, places and product terms can come out spelled the way they sound. The
>   dictionary in Settings helps Mac dictation, not meeting transcripts.
> - Recordings can be up to 2 hours long.
> - Transcription happens in the cloud. If your connection drops, the Mac app keeps recording
>   and uploads once you are back online.

### Plan

**H2:** Which plan includes it

> Hinglish is never a paid extra. It's on every plan, Free included, like every other
> language. Free records and transcribes as many meetings as you like and writes AI summaries
> for your first 5 hours of meetings. Pro, at $15 a month, removes that limit and adds Ask
> Lynkk across every meeting, meeting video from the bot and the weekly digest.

### FAQ (visible text and FAQPage schema)

**What is Hinglish transcription?**

> A written transcript of speech that mixes Hindi and English, often within one sentence.
> Lynkk's Hinglish mode listens for both languages at once, so a sentence that switches
> halfway through is kept whole.

**Which script does the transcript use?** [CONFIRM: answer once the script is confirmed]

> Hindi words appear in [Roman / Devanagari] script, and English words in Roman script.

**Is Hinglish the default?**

> Yes. Every new account starts on Hinglish. To change it, go to Settings, then Transcription;
> the new setting applies to recordings from then on.

**Should I pick Hinglish, Hindi or auto-detect?**

> Hinglish when people mix Hindi and English in the same sentence. Hindi when the whole call
> is in Hindi. Auto-detect when each call sticks to one language but that language changes
> from call to call.

**Does it work for Zoom, Google Meet or Teams calls?**

> Yes, through the meeting bot, which records the call for you. For in-person meetings or
> calls without a bot, use the Mac app or the Chrome extension. The Hinglish setting covers
> all of them.

**[CONFIRM]** Platform names: the Hindi blog says Google Meet, Zoom and Teams, but the
feature pages don't name platforms. If you can't confirm all three, use the question "Does
Hinglish work with the meeting bot?" with the second and third sentences only.

**Can it handle Tamil, Telugu, Marathi or Bengali mixed with English?**

> Not in the way it handles Hinglish. Mid-sentence switching is built for Hindi and English.
> Tamil, Telugu, Marathi and Bengali are available as single languages, in beta.

**Are speakers labelled in Hinglish transcripts?**

> Yes, every transcript is split by speaker. Meeting bot recordings use the names people have
> in the meeting, and the Mac app labels your own voice as You.

**Is Hinglish transcription free?**

> Yes, on every plan. Free transcribes unlimited meetings and includes 5 hours of AI
> summaries; Pro, at $15 a month, makes summaries unlimited.

### Explore more / Related guides

- Keep the current Explore more links (including Multilingual transcription).
- Add to Related guides, first position:
  [Hindi Transcription in India: Free and Paid Ways to Turn Audio Into Text in 2026](/blog/hindi-transcription)

---

## Part 3: Other fixes from the audit (not copy on these pages)

- **/blog/hindi-transcription:** the comparison table and the paragraph after it say "Free
  covers 5 notes a month". The pricing page says unlimited notes plus 5 lifetime hours of AI
  summaries. Replace with: "Free records unlimited notes, up to 2 hours each, with your first
  5 hours of AI summaries; Pro costs $15 a month." In the table cell: "Unlimited notes, 5 h of
  AI summaries".
- **/blog/hindi-transcription:** "Language coverage runs to 17 plus auto-detect" is correct
  under the corrected count. "workspaces can pin model processing to India" isn't on the
  security page, so confirm it or remove it.
- **Schema (both pages, optional):** use one `SoftwareApplication` entity with an `@id` (for
  example `https://lynkk.ai#app`) and reference it from each page's `WebPage`, instead of
  defining a separately named app on each page.
- **After publishing:** request indexing for both URLs in Google Search Console. Neither
  ranks for anything yet.
