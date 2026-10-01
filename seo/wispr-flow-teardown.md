# Wispr Flow SEO teardown: site structure, keywords and placement

Competitor: https://wisprflow.ai
Data: Ubersuggest, United States (locId 2840), pulled 2026-10-01, plus search-indexed page text.

> **Note:** wisprflow.ai is blocked by this environment's network policy, so I couldn't
> read their raw HTML (exact H2/H3 tags, word counts). Page titles, URLs, rankings and
> traffic come from Ubersuggest. Page messaging comes from Google-indexed text and
> third-party reviews (sources at the bottom). Treat the heading order as approximate.

---

## 1. Snapshot

| Metric | Value |
|---|---|
| Domain authority | 46 |
| Organic traffic (US, monthly est.) | ~81,000 |
| Ranking keywords (US) | 3,714 |
| Referring domains / backlinks | 6,386 / 93,662 |
| Traffic trend | ~40 visits (Jan 2025) to 81,000 (Sep 2026) |

**The big change: Wispr Flow is now a meeting notetaker too.** They launched a bot-free
Notetaker on Mac (5 Aug 2026) and Windows (15 Sep 2026). It records through the device
microphone, labels speakers using calendar, Gmail and Slack, writes summaries and
connects to Claude, ChatGPT and Gemini via MCP. It's on the free plan. Their
homepage title now reads **"Wispr Flow | Voice to Text Dictation & AI Notetaker"**.
They now compete with Lynkk on meetings as well as dictation.

---

## 2. Where their traffic comes from

### Top pages by traffic

| Page | Est. traffic | Ref. domains | What it is |
|---|---|---|---|
| `/notetaker` | 5,972 | 94 | Notetaker product page. Already #2 for "note taker" |
| `/` | 5,964 | 3,736 | Homepage, mostly brand traffic |
| `/pricing` | 1,347 | 381 | Brand + "is wispr flow free" |
| `/students` | 562 | 167 | Discount page ("wispr flow promo code") |
| `/microphones` | 221 | 17 | Mic buying guide ("whisper mic", "ai microphone") |
| `/get-started` | 97 | 151 | Onboarding / download |
| `/post/top-10-android-features` | 88 | 1 | Top-of-funnel blog |
| `/post/time-management-tools` | 86 | 4 | Top-of-funnel blog |
| `/vibe-coding` | 55 | 14 | Developer persona page |
| `/android` | 47 | 35 | Platform page |
| `/post/wispr-flow-vs-willow-voice` | 45 | 1 | Comparison |
| `/use-cases/chrome` | 35 | 0 | App use-case page |
| `/post/wispr-flow-vs-voiceink-2025` | 33 | 0 | Comparison (ranks #6 for "voiceink", 2,400 vol) |
| `/post/wispr-flow-vs-monologue` | 30 | 1 | Comparison |
| `/developers` | 27 | 16 | "Dictation built for developers" |
| `/use-cases` | 25 | 22 | Use-case hub |
| `/business` | 25 | 50 | Teams / enterprise |
| `/comparison/macwhisper-alternative` | 20 | 1 | Comparison |
| `/use-cases/claude` | 20 | 3 | App use-case page |
| `/comparison/superwhisper-alternative` | 19 | 8 | Comparison |
| `/features` | 13 | 29 | Feature hub (almost no search traffic) |

**Takeaways**
- About half their non-brand search traffic comes from **one page, `/notetaker`**, and
  it's in Lynkk's category.
- Their dictation pages (`/`, `/features`) rank almost only for **brand** searches. The
  homepage gets very little from generic dictation terms.
- Feature pages get no search traffic. Pages built around one keyword (notetaker,
  microphones, students, comparisons) do.

### Non-brand keywords they rank for

| Keyword | Vol | SD | Pos | Page |
|---|---|---|---|---|
| note taker | 14,800 | 61 | **2** | /notetaker |
| ai notetaker | 2,900 | 42 | 14 | /notetaker |
| notetaker | 1,900 | 45 | **2** | /notetaker |
| meeting notetaker | 880 | 46 | 15 | /notetaker |
| ai dictation tool | 480 | 44 | **2** | / |
| voice coding | 390 | 43 | 7 | /vibe-coding |
| whisper mic | 390 | 15 | 2 | /microphones |
| ai microphone | 390 | 24 | 10 | /microphones |
| whisper dictation | 260 | 60 | 1 | / |
| ai dictation app | 210 | 38 | 5 | / |
| note taker for meetings | 210 | 54 | 8 | /notetaker |
| dictation ai | 140 | 57 | 2 | / |
| ai dictation software | 90 | 48 | **2** | / |
| dictating physician | 90 | 16 | 5 | /post/...medical-dictation-software |
| talk to text ai | 40 | 64 | 2 | / |
| notion dictation | 30 | 17 | 8 | /use-cases/notion |
| macwhisper alternative | 30 | 9 | 7 | /comparison/macwhisper-alternative |
| voiceink (competitor brand) | 2,400 | 27 | 6 | /post/wispr-flow-vs-voiceink-2025 |
| wispr flow vs willow | 110 | 13 | 3 | /post/wispr-flow-vs-willow-voice |
| shortcut app for android | 2,900 | 42 | 17 | blog |
| vibe coder | 110,000 | 62 | 21 | /vibe-coding |

### Keywords they do NOT rank for (the gap Lynkk can take)

None of these show up in Wispr Flow's ranking data:

| Keyword | Vol | SD |
|---|---|---|
| talk to text mac | 1,600 | 14 |
| speech to text mac | 1,600 | 25 |
| mac voice to text | 1,600 | 25 |
| voice to text on mac | 1,300 | 21 |
| dictation software | 1,900 | 32 |
| **dictation software for microsoft word** | **1,600** | **8** |
| mac dictation | 1,600 | 33 |
| voice dictation software for mac | 590 | 28 |
| voice typing on mac | 480 | 31 |
| dictation app for mac | 260 | 31 |
| voice to text gmail / gmail voice typing | 140 / 110 | 38 / 34 |
| chatgpt voice to text | 110 | 31 |

Wispr ranks for the **category** terms ("ai dictation tool/software/app") but not for
**platform + task** terms ("voice to text on Mac", "dictation for Word"). Those
platform terms are the main targets on Lynkk's dictation page, so Lynkk isn't competing
with Wispr's homepage for them.

---

## 3. Site architecture (how they place content)

```
wisprflow.ai/
├── /                      Homepage: brand + "voice to text dictation" + "AI notetaker"
├── /features              Feature hub (dictionary, snippets, styles, command mode, languages)
├── /notetaker             Notetaker product page
│   └── /notetaker/*       SEO cluster of articles (hub and spoke):
│         best-ai-note-takers, best-free-ai-notetaker, ai-notetaker-for-zoom,
│         wispr-notetaker-vs-fireflies, ai-notetaking-app, automatic-notetaker,
│         ai-notetaker-for-user-researchers
├── /use-cases             Use-case hub
│   └── /use-cases/{app}   One page per app: chrome, claude, notion, gmail, slack, chatgpt
├── /developers, /vibe-coding, /vibe-coding/windsurf   Developer persona pages
├── /students, /business, /android                        Segment and platform pages
├── /microphones           Buying guide that earns hardware keywords
├── /comparison/{x}-alternative     superwhisper-alternative, macwhisper-alternative
├── /post/wispr-flow-vs-{x}         voiceink, willow-voice, monologue (date in the title)
├── /post/*                Blog: productivity and Android tips, medical dictation,
│                          voice typing for essays, remote team workflows
├── /pricing, /privacy, /data-controls, /post/hipaa-is-here   Pricing and trust
└── /whats-new, /support, /media-kit, /careers
```

**Patterns worth noting**
1. **One page per intent.** Notetaker, students, microphones, each persona, each app and
   each competitor gets its own URL. That's how a single product ranks for hundreds of
   different searches.
2. **Hub and spoke for the new category.** They launched `/notetaker` with seven
   supporting articles under `/notetaker/*` that all link back to it. It's at #2 for
   "note taker" (14,800/mo) within about two months.
3. **Competitor pages in two formats.** `/comparison/{x}-alternative` (to catch
   "x alternative" searches) and `/post/wispr-flow-vs-{x}` (to catch "x vs y" searches).
   Their VoiceInk post ranks for the competitor's **brand name**.
4. **Use-case pages per app** (`/use-cases/notion`, `/claude`, `/chrome`). Small volume
   each, but cheap to make and very high intent.
5. **Top-of-funnel blog** drifts off topic (Android tips, WOOP goals) and gets traffic
   with little buying intent. Lynkk doesn't need to copy this part.

---

## 4. How they place keywords on the page

### Title tags

| Page | Title | Pattern |
|---|---|---|
| Home | Wispr Flow \| Voice to Text Dictation & AI Notetaker | Brand first, then 2 category keywords |
| /get-started | Wispr Flow \| Effortless Voice Dictation | Brand + keyword |
| /use-cases | Use Cases with Flow \| Wispr Flow | Navigational |
| /developers | Dictation built for developers | Persona + keyword |
| /vibe-coding | Vibe Coding: AI + Voice = The New Developer Workflow | Trend keyword first |
| /comparison/superwhisper-alternative | Flow vs superwhisper Dictation: Which Tool Works Best for You | "X vs Y" + question |
| /post/wispr-flow-vs-willow-voice | Wispr Flow vs Willow Voice: Which is the best dictation tool? (January 2026) | Date in title for freshness |
| /notetaker/best-free-ai-notetaker | The best free AI notetakers in 2026: free tiers compared | Listicle + year |
| /notetaker/ai-notetaker-for-zoom | AI notetaker for Zoom: set up in minutes | Keyword first, benefit after |

### Homepage messaging (top to bottom, from indexed text)

| Block | Copy / content | Keyword role |
|---|---|---|
| Hero H1 | "Don't type, just speak" | Slogan, **no keyword** (they can afford this with 3,700 linking domains) |
| Subhead | "The fastest, smartest way to type with your voice" / "4x faster than your keyboard" | "type with your voice", speed claim |
| Works everywhere | Slack, Gmail, Notion, iMessage, WhatsApp, ChatGPT, Claude, Cursor, terminal, docs | App names = long-tail matches |
| AI editing | Removes filler words, formats lists, adds punctuation, understands corrections mid-sentence | "voice dictation", "clean text" |
| Personalization | Personal dictionary, snippets (voice shortcuts), styles per app | Feature names |
| Languages | 100+ languages | "multilingual" |
| Platforms | Mac, Windows, iPhone, Android | "wispr flow mac/windows/android" brand+platform searches |
| Notetaker | Bot-free notes for Zoom, Meet, Teams, Slack huddles | "AI notetaker" |
| Social proof | Testimonials, logos | Trust |
| Trust | HIPAA on all plans, SOC 2 Type I, privacy mode | Privacy queries |

### Feature names they use (their vocabulary)

| Feature | What it does |
|---|---|
| AI auto edits | Removes "um/uh", fixes punctuation, formats lists, applies mid-sentence corrections |
| Personal dictionary | Learns names, jargon, unusual spellings |
| Snippets | Say a shortcut, Flow expands it (links, intros, addresses) |
| Styles | Different tone per app (casual in chat, formal in email) |
| Command Mode | Highlight text and say "make this formal", "translate to Spanish", "turn into bullets" |
| 100+ languages | Multilingual dictation |
| Cross-device sync | Same dictionary and snippets on Mac, Windows, iPhone, Android |

### Repeated phrases (their keyword vocabulary)
"voice dictation", "voice to text", "type with your voice", "AI voice keyboard"
(App Store name), "AI Voice-to-Text" (Play Store name), "works in every app",
"4x faster", "speed of thought", "AI notetaker", "bot-free".

---

## 5. What this means for Lynkk

### Copy these tactics
1. **One page per intent.** Add `/use-cases/{app}` pages for the apps Lynkk Dictation
   works in. Start with Microsoft Word: "dictation software for microsoft word" is
   **1,600/mo at SD 8** and Wispr doesn't rank for it.
2. **Competitor pages in both formats**: `/compare/wispr-flow-alternative` (480/mo,
   SD 11) and `/compare/lynkk-vs-wispr-flow`. Put the month and year in the title like
   Wispr does.
3. **Hub and spoke**: `/features/dictation` is the hub; how-to, listicle, use-case and
   comparison pages are the spokes, and each links back to the hub.
4. **Match their feature checklist** on the dictation page (filler words, punctuation,
   corrections, dictionary, languages, privacy) so Lynkk doesn't look thinner. Only list
   what Lynkk actually has.

### Do differently
1. **Put keywords in the H1.** Wispr's slogan H1 works because of brand authority. With
   low authority, Lynkk needs "voice to text on Mac" in the H1 and the title.
2. **Go after platform + task keywords** ("voice to text on Mac", "dictation for Word"),
   not the category terms ("AI dictation tool") where Wispr sits at #2.
3. **Change the meeting differentiator.** "Dictation plus meeting notes in one app" no
   longer sets Lynkk apart, because Wispr now does both. Wispr's notetaker records,
   transcribes, summarizes and connects via MCP. Lead with what Lynkk does that a
   passive notetaker doesn't:
   - **Context before the call** from past meetings
   - **A live voice assistant during the call** that answers questions and pulls up documents
   - **Work done after**: CRM fields updated and Jira tickets created within ~30 seconds
   - **In-person conversations**, not only video calls
   - **Data residency**: choose the region where every model runs
4. **Watch the "bot-free" angle.** Wispr markets "nothing joins the call." If Lynkk joins
   as a bot to speak during meetings, explain why that's a benefit (it can answer out loud)
   and say whether there's also a bot-free mode. **[confirm with product]**
5. **Trust signals.** Wispr shows HIPAA on all plans and SOC 2 Type I. Lynkk should show
   its own certifications as soon as they're confirmed (already on the to-confirm list in
   `memory/lynkk-brand.md`).

---

## Sources
- Ubersuggest: domain overview, top pages, domain keywords, page keywords for wisprflow.ai (US)
- [Wispr Flow](https://wisprflow.ai/), [Features](https://wisprflow.ai/features), [Use cases](https://wisprflow.ai/use-cases), [Notetaker](https://wisprflow.ai/notetaker), [Pricing](https://wisprflow.ai/pricing)
- [Flow vs superwhisper](https://wisprflow.ai/comparison/superwhisper-alternative), [Wispr Flow vs Willow Voice](https://wisprflow.ai/post/wispr-flow-vs-willow-voice)
- [Best AI note takers](https://wisprflow.ai/notetaker/best-ai-note-takers), [Best free AI notetakers](https://wisprflow.ai/notetaker/best-free-ai-notetaker), [AI notetaker for Zoom](https://wisprflow.ai/notetaker/ai-notetaker-for-zoom), [Wispr Notetaker vs Fireflies](https://wisprflow.ai/notetaker/wispr-notetaker-vs-fireflies)
- [HIPAA is here](https://wisprflow.ai/post/hipaa-is-here)
- [AlternativeTo: Wispr Flow launches AI notetaker](https://alternativeto.net/news/2026/8/wispr-flow-launches-a-new-ai-notetaker-meeting-assistant-for-transcription-and-summaries/)
- [Datastudios: Wispr Flow Notetaker explained](https://www.datastudios.org/post/wispr-flow-notetaker-bot-free-mac-meeting-ai-with-mcp-support-explained)
- [tl;dv: Wispr Flow review](https://tldv.io/blog/wisprflow/), [tl;dv: Wispr Flow Notetaker review](https://tldv.io/blog/wispr-flow-notetaker-review/)
- [Wispr Flow help: What is Flow](https://docs.wisprflow.ai/articles/2772472373-what-is-flow)
