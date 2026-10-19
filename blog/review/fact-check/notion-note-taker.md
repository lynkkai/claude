# Fact check: notion-note-taker

Article: `articles/notion-note-taker.md` · Date checked: 2026-10-19 · Method: 3 rounds (primary source, omissions, internal contradictions)

| # | Claim (short) | Source URL fetched | Status | Fix |
|---|---|---|---|---|
| 1 | Notion's note taker is called AI Meeting Notes and needs no bot | https://www.notion.com/pricing , https://www.notion.com/help/ai-meeting-notes | VERIFIED | Pricing page wording: "Automate your meeting notes and follow-ups, no bot needed" |
| 2 | Included on Business and Enterprise; Free and Plus get a limited trial | https://www.notion.com/pricing , https://www.notion.com/help/ai-meeting-notes | VERIFIED | |
| 3 | Eligible mobile subscriptions that include Notion AI also get it | https://www.notion.com/help/ai-meeting-notes | VERIFIED | Round 2: added, was missing |
| 4 | Notion Free $0, Plus $10, Business $20 per member per month; Enterprise custom | https://www.notion.com/pricing | VERIFIED | |
| 5 | Yearly billing saves up to 20% | https://www.notion.com/pricing | VERIFIED | Page says "Save up to 20% with yearly" |
| 6 | Team totals $1,200 / $2,400 / $6,000 a year | computed from $20 per member | VERIFIED | |
| 7 | `/meet` on a page, Start transcribing, Stop; summary generates automatically | https://www.notion.com/help/ai-meeting-notes | VERIFIED | Added Resume transcription and agenda-notes behaviour |
| 8 | "Desktop app needed" for every meeting | https://www.notion.com/help/ai-meeting-notes | FIXED | Browser and mobile also work but capture only the mic; body and FAQ reworded |
| 9 | Minimum 1 minute of speech / 300 characters | https://www.notion.com/help/ai-meeting-notes | FIXED | Stated as the source does: 300 transcribed characters, roughly a minute |
| 10 | Daily cap of 10 hours per user | https://www.notion.com/help/ai-meeting-notes | VERIFIED | |
| 11 | Starting transcription confirms consent | https://www.notion.com/help/ai-meeting-notes | VERIFIED | Round 2: added the audio consent message and the owner-enforced setting |
| 12 | 16 supported languages, Hindi absent | https://www.notion.com/help/ai-meeting-notes | FIXED | Full list now named; count matches |
| 13 | Speaker labeling English only | https://www.notion.com/help/ai-meeting-notes | VERIFIED | Round 2: noted the Google Meet Chrome add-on for group-call labels |
| 14 | Works with Zoom, Meet, Teams via system audio | https://www.notion.com/help/ai-meeting-notes | VERIFIED | Added the headphones-in-browser and VDI caveats |
| 15 | macOS 13+ and desktop app 4.7.0+ required | https://www.notion.com/help/ai-meeting-notes | VERIFIED | Added |
| 16 | Audio upload supported (AAC, M4A, MP3, WAV; not MP4/MOV) | https://www.notion.com/help/ai-meeting-notes | VERIFIED | Added to a FAQ |
| 17 | Desktop meeting detection prompts, and how to turn them off | https://www.notion.com/help/ai-meeting-notes | VERIFIED | Added to a FAQ |
| 18 | Notes inherit page permissions | https://www.notion.com/help/ai-meeting-notes | VERIFIED | Round 2: added that notes are private to the creator by default |
| 19 | "On Business and Enterprise, admins can auto-delete transcripts" | https://www.notion.com/pricing , https://www.notion.com/help/ai-meeting-notes | FIXED | Owner setting; pricing page lists transcript deletion under Enterprise admin controls |
| 20 | Granola Business $14 per user per month | https://www.granola.ai/pricing | VERIFIED | |
| 21 | Granola Enterprise $35 | https://www.granola.ai/pricing | VERIFIED | Added |
| 22 | Granola apps: "Mac, Windows, iPhone and Android" | https://www.granola.ai/pricing | FIXED | Page says desktop, iOS, Android and Apple Watch; no Windows claim |
| 23 | Granola free tier keeps 30 days of history | https://www.granola.ai/pricing | VERIFIED | |
| 24 | Granola syncs notes to Notion on Business | https://www.granola.ai/pricing | VERIFIED | Notion listed among Business integrations |
| 25 | Granola paid tier adds pre-meeting briefs and follow-up emails | https://www.granola.ai/pricing | VERIFIED | Added to the Granola FAQ as the differentiator |
| 26 | Lynkk Free 5 notes a month, 2 hours each; Pro $15 a month | https://lynkk.ai/pricing | VERIFIED | |
| 27 | Lynkk 17 languages plus auto-detect, Hindi and Hinglish, 4 beta languages | https://lynkk.ai/features/multilingual-transcription , https://lynkk.ai/ | VERIFIED | Beta languages added to the Hindi FAQ |
| 28 | "Notion is a coming-soon Lynkk integration" | https://lynkk.ai/integrations | FIXED | The page lists Notion as not connected yet; wording changed to Markdown export |
| 29 | Lynkk "Before: Meeting Brief with what is still open from past meetings" | https://lynkk.ai/features/meeting-notes | FIXED | Meeting Brief is the post-call summary; bullet moved to "After" |
| 30 | Lynkk "one-click Jira tickets" | https://lynkk.ai/ , https://lynkk.ai/integrations | FIXED | Reworded to "Jira actions" (Send on a note creates one issue per action item) |
| 31 | Lynkk bot for Zoom, Meet, Teams; Mac app and Chrome extension record bot-free | https://lynkk.ai/features/meeting-bot | VERIFIED | |

Round 3 (contradictions): the body claimed the desktop app was mandatory while the FAQ implied the same; both now match the help center (desktop for both sides of the audio, browser and mobile mic-only). Language count in body and FAQ now agree at 16. Baseline moved with `rebaseline.py` after these corrections.
