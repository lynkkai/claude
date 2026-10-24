# Transcription pages: issues and fixes

Audit of https://lynkk.ai/features/multilingual-transcription and
https://lynkk.ai/features/hinglish-transcription (2026-10-24).

The full replacement copy is in:
- `multilingual-transcription-page.md`
- `hinglish-transcription-page.md`

Both pages only state facts the live site already states, so they can go live as written.

## Every issue found, and where it is fixed

| # | Issue | Fix |
|---|---|---|
| 1 | **Cannibalization:** the multilingual H1 said "Multilingual and Hinglish transcription", so both pages competed for "hinglish transcription" | New multilingual H1, title and OG tags say nothing about Hinglish. Hinglish now only appears there as a link to the Hinglish page |
| 2 | Both pages listed `hinglish transcription` and `code switching transcription` in meta keywords | Both terms now appear only on the Hinglish page |
| 3 | Two whole multilingual sections were about Hinglish ("Hinglish when you need it", "Hinglish, auto-detect or one language") | Cut to one link card, and the section is now "Pick a language or let it detect" |
| 4 | **Duplicate text:** 37% of the Hinglish page's sentences, and 50% of its 5-word phrases, also appeared on the multilingual page | Hinglish page rewritten. Shared 5-word phrases are now 10%: headings, the button and two short stock lines |
| 5 | **Language count:** the pages said "17 languages, Hinglish included", but listing Hinglish made 18 | Hinglish is a mode: everything now says "17 languages plus Hinglish and auto-detect", which matches the settings screen |
| 6 | **Default language contradiction:** the multilingual FAQ said "English (the default)", while the next FAQ and "How it works" said Hinglish | Every mention now says Hinglish, and a new FAQ "What is the default language?" tells non-Hindi teams to switch once |
| 7 | Hinglish meta description ended "One of Lynkk's 17 languages", which is wrong under the corrected count | New description |
| 8 | The multilingual page says there are two transcription providers, but its "How it works" said "its transcription provider" (one) | Now "sends it for transcription" |
| 9 | Multilingual OG image text said "Hinglish included" | Drawn from the new `og:description`, so it updates on its own |
| 10 | Multilingual plan section repeated "every" four times in two sentences | Rewritten, with a link to pricing |
| 11 | Neither feature page linked to `/blog/hindi-transcription` | Added to Related guides on both pages |
| 12 | Hinglish page listed "Best AI Transcription Software in the USA" as a related guide | Replaced with the Hindi blog post on the Hinglish page |
| 13 | Hinglish page had no sections of its own (no example, no use cases) | Added "The kind of meeting it's built for" (sample dialogue) and "Where Hinglish mode helps" (links to 4 use-case pages) |
| 14 | Neither page said what happens when other Indian languages are mixed with English | Covered in Limits and a new FAQ on the Hinglish page, and in Limits on the multilingual page |
| 15 | FAQ schema has to match the visible FAQ | New FAQPage JSON-LD at the end of each page file, generated from its visible FAQ |

## Lines to add once the product team confirms them

These would strengthen the Hinglish page, but nothing on the site confirms them yet, so the
page copy leaves them out.

1. **Which script:** do Hinglish transcripts write Hindi words in Roman script, Devanagari, or
   both? Searchers ask this. Once known, add a FAQ "Which script does the transcript use?" and
   one sentence under the sample dialogue. A screenshot from a real test call would be even
   better.
2. **Search in both languages:** if search finds Hindi and English words in a Hinglish
   transcript, add "in either language" to step 5 of "How it works".
3. **Meeting platforms:** if the bot works with Zoom, Google Meet and Microsoft Teams, change
   the FAQ "Does Hinglish work with the meeting bot?" to "Does it work for Zoom, Google Meet or
   Teams calls?" and name them. Only the Hindi blog names them today.
4. **India data processing:** only the Hindi blog says "workspaces can pin model processing to
   India". The security page doesn't. If it's true, it's a strong line for the Hinglish page
   and for `memory/lynkk-brand.md`.

## Fixes on other pages

- **`/blog/hindi-transcription`:** the comparison table and the paragraph after it say "Free
  covers 5 notes a month". The pricing page says unlimited notes plus 5 lifetime hours of AI
  summaries.
  - Paragraph: "Free records unlimited notes, up to 2 hours each, with your first 5 hours of
    AI summaries; Pro costs $15 a month."
  - Table cell: "Unlimited notes, 5 h of AI summaries"
  - Also confirm or remove "workspaces can pin model processing to India" (item 4 above).
- **`memory/lynkk-brand.md`:** says "Offline-first", but the pages say transcription runs in
  the cloud and the Mac app only keeps recording offline. Fix it before the next directory
  submission.
- **Schema (optional):** define one `SoftwareApplication` with an `@id` (for example
  `https://lynkk.ai#app`) and reference it from each page's `WebPage`, instead of a separately
  named app on each page.
- **After publishing:** request indexing for both URLs in Google Search Console. Neither ranks
  for anything yet.
