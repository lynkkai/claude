# Fact check: jamie-ai-note-taker

Article: `articles/jamie-ai-note-taker.md` · Date checked: 2026-10-19 · Method: 3 rounds (primary source, omissions, internal contradictions)

| # | Claim (short) | Source URL fetched | Status | Fix |
|---|---|---|---|---|
| 1 | Jamie records on your device, no bot joins | https://www.meetjamie.ai/pricing | VERIFIED | "All online platforms" and "In-person meetings" on every plan |
| 2 | Free $0: 10 AI notes a month, 30-minute cap, Ask Jamie | https://www.meetjamie.ai/pricing | VERIFIED | |
| 3 | Free also includes 1 custom template, 50 vocabulary terms, unlimited storage, Google Docs / Notion / OneNote export | https://www.meetjamie.ai/pricing | VERIFIED | Moved into a FAQ as the added detail |
| 4 | Plus $24, 20 notes a month, 2-hour cap, 3 templates | https://www.meetjamie.ai/pricing | VERIFIED | |
| 5 | Plus billing period (editor query) | https://www.meetjamie.ai/pricing | FIXED | Every paid plan is billed annually; the table row and body now say so |
| 6 | Pro $46 a month billed yearly: unlimited notes, 5-hour cap, unlimited templates | https://www.meetjamie.ai/pricing | VERIFIED | |
| 7 | Pro integrations | https://www.meetjamie.ai/pricing | VERIFIED | Round 2: added Attio, Dynamics 365, API and webhooks, which were missing |
| 8 | Team $37 per seat billed yearly: shared workspace, templates, admin controls, 100 vocabulary terms, centralized billing | https://www.meetjamie.ai/pricing | VERIFIED | |
| 9 | Enterprise custom: SAML SSO, SCIM, audit logs, IP allowlist, DPAs, 250 terms, account manager | https://www.meetjamie.ai/pricing | VERIFIED | Round 2: added volume discounts and custom retention |
| 10 | Yearly vs monthly saving | https://www.meetjamie.ai/pricing | FIXED | The toggle states 17%; the article said only "monthly billing available" |
| 11 | 99+ languages for notes and transcripts | https://www.meetjamie.ai/pricing | VERIFIED | |
| 12 | Custom vocabulary tiers 50 / 50 / 50 / 100 / 250 | https://www.meetjamie.ai/pricing | VERIFIED | Added to the languages FAQ |
| 13 | EU hosting, GDPR, no model training | https://www.meetjamie.ai/pricing | VERIFIED | Present on all 5 plans |
| 14 | ISO 27001 and DORA listed; SOC 2 Type II pending | https://www.meetjamie.ai/pricing | VERIFIED | |
| 15 | Consent email on every plan; customized consent notification Enterprise-only | https://www.meetjamie.ai/pricing | VERIFIED | Round 2: added, the article had no consent feature at all |
| 16 | "Android app, in beta" | https://docs.meetjamie.ai/enterprise/users/mobile-app | FIXED | Docs (updated 3 September 2026) list iOS and Android with no beta label; body and FAQ corrected |
| 17 | Mobile records in-person meetings, shows meetings and tasks, Ask AI | https://docs.meetjamie.ai/enterprise/users/mobile-app | VERIFIED | Added that recordings sync to desktop |
| 18 | Desktop downloads offered for Mac, Windows, iPhone | https://www.meetjamie.ai/pricing | VERIFIED | Added as the mismatch with Google Play |
| 19 | G2 and Trustpilot sentiment ("praise 3 things") | no primary source | REMOVED | Replaced with plan-grid facts; no review scores asserted |
| 20 | "No built-in Jira ticket creation" (weakness table) | https://www.meetjamie.ai/pricing | VERIFIED | Jamie's integration list has no Jira row |
| 21 | Granola Business $14 | https://www.granola.ai/pricing | VERIFIED | |
| 22 | Granola free plan 30 days of history | https://www.granola.ai/pricing | VERIFIED | |
| 23 | Otter Pro $8.33 billed yearly, Business $19.99 billed yearly, free 300 minutes at 30 minutes a call | https://otter.ai/pricing | VERIFIED | |
| 24 | Fathom records unlimited calls on its free plan | https://www.fathom.ai/pricing | VERIFIED | |
| 25 | US consent law ("several states require all parties") | https://www.law.cornell.edu/uscode/text/18/2511 | FIXED | Now contrasts federal one-party consent with stricter state laws, statute linked |
| 26 | Lynkk Pro $15 a month, Free 5 notes at 2 hours | https://lynkk.ai/pricing | VERIFIED | |
| 27 | Lynkk "Before: Meeting Brief with what is still open from past meetings" | https://lynkk.ai/features/meeting-notes | FIXED | Meeting Brief is the post-call summary; bullet moved to "After" |
| 28 | Lynkk "one-click Jira tickets" | https://lynkk.ai/integrations | FIXED | Reworded to "Jira actions" |
| 29 | Lynkk 17 languages, Hindi and Hinglish | https://lynkk.ai/features/multilingual-transcription | VERIFIED | |
| 30 | Lynkk data regions US, EU, UK, India, Singapore, Australia | https://lynkk.ai/ FAQ, https://lynkk.ai/security | VERIFIED | |
| 31 | Lynkk Mac app and Chrome extension record without a bot; bot covers Zoom, Meet, Teams | https://lynkk.ai/features/chrome-extension , https://lynkk.ai/features/meeting-bot | VERIFIED | |

Round 3 (contradictions): the Android claim appeared twice with "beta" and once implied a lagging feature set; both passages now match the docs. Plan prices in the tldr, Quick answer, table, body and FAQ all state annual billing. Baseline moved with `rebaseline.py` after these corrections.
