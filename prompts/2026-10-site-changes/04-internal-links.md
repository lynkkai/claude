You are editing the lynkk.ai website (Next.js App Router) in this repository.

Task: connect the blog and the service pages with internal links, grouped into five topics. Run this after the /articles posts have moved to /blog and /features/hinglish-transcription is live.

Before changing anything, find where each post's body, the "More from the blog" block and the service page layouts are defined, and tell me which files you will edit.

Rules:
- Brand is always "Lynkk".
- Never use em dashes or en dashes in any copy. Use a comma, colon or parentheses instead.
- Do not change any title, meta description or URL.
- Put in-text links on words that describe the target page (for example "how to transcribe Zoom meetings"), never "click here" or "read more". Never use the same anchor text for two different pages.
- Link each target page at most once per page.
- If a post has no natural sentence for a link in the section named, add one short sentence there. Do not add new facts.
- All post URLs are /blog/<slug>.

Part 1: topics and hubs

Each post belongs to one topic. The hub post is listed first.

| Topic | Hub post | Other posts |
| --- | --- | --- |
| Note takers | best-ai-note-takers | best-free-ai-note-takers, ai-powered-meeting-assistants, ai-note-taker-microsoft-teams, sales-conversation-intelligence |
| Zoom | zoom-note-taker | zoom-meeting-recorders, how-to-transcribe-zoom-meetings, zoom-ai-companion-alternatives, google-meet-transcript |
| Transcription | transcribe-audio-to-text | ai-transcription-software, voice-memo-transcription, ai-voice-recorders, recruiting-interview-transcription, legal-transcription-service, medical-transcription-software |
| Dictation | voice-to-text-apps | dictation-on-mac, dictate-in-microsoft-word |
| Meeting practice | action-items-examples-template | meeting-minutes-to-jira, daily-standup-meeting, one-on-one-meeting, founders-meeting-notes, meeting-knowledge-management |

1. Store each post's topic where post metadata is kept, so new posts get one too.
2. Change the "More from the blog" block so it shows 3 posts from the same topic (the hub first, unless this is the hub), instead of the 3 newest posts.
3. Each non-hub post links to its hub in its first 200 words.

Part 2: post to post links (in the body text)

| Post | Link to these posts |
| --- | --- |
| best-ai-note-takers | best-free-ai-note-takers, ai-powered-meeting-assistants, ai-note-taker-microsoft-teams, zoom-note-taker, sales-conversation-intelligence, ai-voice-recorders |
| best-free-ai-note-takers | best-ai-note-takers, zoom-note-taker, ai-note-taker-microsoft-teams, google-meet-transcript |
| ai-powered-meeting-assistants | best-ai-note-takers, zoom-ai-companion-alternatives, ai-note-taker-microsoft-teams, meeting-knowledge-management |
| ai-note-taker-microsoft-teams | best-ai-note-takers, zoom-note-taker, google-meet-transcript, best-free-ai-note-takers |
| sales-conversation-intelligence | best-ai-note-takers, zoom-ai-companion-alternatives, meeting-minutes-to-jira, founders-meeting-notes |
| zoom-note-taker | zoom-meeting-recorders, how-to-transcribe-zoom-meetings, zoom-ai-companion-alternatives, best-ai-note-takers, google-meet-transcript |
| zoom-meeting-recorders | zoom-note-taker, how-to-transcribe-zoom-meetings, zoom-ai-companion-alternatives |
| how-to-transcribe-zoom-meetings | zoom-note-taker, zoom-meeting-recorders, google-meet-transcript, transcribe-audio-to-text |
| zoom-ai-companion-alternatives | zoom-note-taker, ai-powered-meeting-assistants, best-ai-note-takers, ai-note-taker-microsoft-teams |
| google-meet-transcript | transcribe-audio-to-text, how-to-transcribe-zoom-meetings, ai-note-taker-microsoft-teams, best-free-ai-note-takers |
| transcribe-audio-to-text | ai-transcription-software, voice-memo-transcription, ai-voice-recorders, how-to-transcribe-zoom-meetings, google-meet-transcript, recruiting-interview-transcription, legal-transcription-service, medical-transcription-software |
| ai-transcription-software | transcribe-audio-to-text, legal-transcription-service, medical-transcription-software, recruiting-interview-transcription |
| voice-memo-transcription | transcribe-audio-to-text, ai-voice-recorders, dictation-on-mac |
| ai-voice-recorders | transcribe-audio-to-text, voice-memo-transcription, best-ai-note-takers |
| recruiting-interview-transcription | transcribe-audio-to-text, ai-transcription-software, legal-transcription-service |
| legal-transcription-service | transcribe-audio-to-text, medical-transcription-software, ai-transcription-software |
| medical-transcription-software | transcribe-audio-to-text, legal-transcription-service, voice-memo-transcription, voice-to-text-apps |
| voice-to-text-apps | dictation-on-mac, dictate-in-microsoft-word, transcribe-audio-to-text, medical-transcription-software |
| dictation-on-mac | voice-to-text-apps, dictate-in-microsoft-word, voice-memo-transcription |
| dictate-in-microsoft-word | voice-to-text-apps, dictation-on-mac, transcribe-audio-to-text |
| action-items-examples-template | meeting-minutes-to-jira, daily-standup-meeting, one-on-one-meeting, founders-meeting-notes, meeting-knowledge-management |
| meeting-minutes-to-jira | action-items-examples-template, daily-standup-meeting, meeting-knowledge-management |
| daily-standup-meeting | action-items-examples-template, meeting-minutes-to-jira, one-on-one-meeting |
| one-on-one-meeting | action-items-examples-template, daily-standup-meeting, founders-meeting-notes |
| founders-meeting-notes | action-items-examples-template, one-on-one-meeting, sales-conversation-intelligence, meeting-knowledge-management |
| meeting-knowledge-management | action-items-examples-template, founders-meeting-notes, ai-powered-meeting-assistants |

Part 3: post to service page links (only the ones missing today, in the body text of the section named)

| Post | Add a link to | Where in the post |
| --- | --- | --- |
| best-ai-note-takers, best-free-ai-note-takers | /compare/otter, /compare/fireflies, /compare/granola, /compare/fathom | In each competitor's numbered section (for example "2. Fathom"), on the first mention of its name, anchor "Lynkk vs Fathom" (and so on) |
| best-ai-note-takers, best-free-ai-note-takers | /features/meeting-notes | The "1. Lynkk" section, on the words "structured notes" or "notes" |
| ai-note-taker-microsoft-teams, zoom-ai-companion-alternatives | The compare page of each competitor named (Otter, Fireflies, Fathom) | In each competitor's numbered section, on the first mention of its name, anchor "Lynkk vs Otter" (and so on) |
| sales-conversation-intelligence | /compare/fireflies | "What are the best Gong alternatives?", where Fireflies is named |
| transcribe-audio-to-text | /use-cases/lectures | "Which application to transcribe audio to text should you use?" |
| ai-transcription-software | /use-cases/lectures | "Which transcription software is best for meetings?" |
| voice-memo-transcription | /use-cases/lectures | "How do you turn a voice memo into notes?" |
| ai-voice-recorders | /use-cases/lectures | "Do you need an AI voice recorder device or an app?" |
| ai-voice-recorders | /features/multilingual-transcription | The "1. Lynkk" section, on "17 languages" |
| transcribe-audio-to-text, ai-transcription-software | /features/hinglish-transcription | Where languages or multilingual transcription are mentioned, anchor "Hinglish transcription" |
| transcribe-audio-to-text | /use-cases/user-interviews | The "1. Lynkk" section, on the word "interviews" |
| action-items-examples-template | /integrations | "How do you go about tracking action items after a meeting?", where Jira is mentioned |
| meeting-minutes-to-jira | /use-cases/team-standups | "How do you track action items after a meeting?", in one added sentence about reviewing open items at the daily standup |
| best-ai-note-takers | /features/workspaces | The "1. Lynkk" section, on "Workspaces" in the pricing line |
| ai-note-taker-microsoft-teams | /features/workspaces | "How much does Teams AI cost for a 10-person team?" |
| one-on-one-meeting | /features/workspaces | "How do managers use Lynkk for one-on-one meetings?" |
| meeting-knowledge-management | /web-app | "How do teams build searchable meeting memory with Lynkk?" |
| founders-meeting-notes | /web-app | "How do founders keep track of meetings?" |

Part 4: a "Related guides" block on service pages

Add a "Related guides" block above the footer of each page below, with 3 post cards (title and link), built as one reusable component.

| Service page | Related guides |
| --- | --- |
| Homepage | Link to /blog plus the 5 hub posts (best-ai-note-takers, zoom-note-taker, transcribe-audio-to-text, voice-to-text-apps, action-items-examples-template), in a "Guides" row above the footer |
| /features/meeting-bot | zoom-note-taker, ai-note-taker-microsoft-teams, google-meet-transcript |
| /features/meeting-notes | best-ai-note-takers, founders-meeting-notes, meeting-minutes-to-jira |
| /features/action-items | action-items-examples-template, meeting-minutes-to-jira, daily-standup-meeting |
| /features/multilingual-transcription and /features/hinglish-transcription | transcribe-audio-to-text, recruiting-interview-transcription, ai-transcription-software |
| /features/dictation and /download | dictation-on-mac, dictate-in-microsoft-word, voice-to-text-apps |
| /features/ask-your-meetings and /slack | meeting-knowledge-management, founders-meeting-notes, one-on-one-meeting |
| /features/chrome-extension | zoom-note-taker, google-meet-transcript, how-to-transcribe-zoom-meetings |
| /use-cases/sales-calls | sales-conversation-intelligence, best-ai-note-takers, zoom-ai-companion-alternatives |
| /use-cases/team-standups | daily-standup-meeting, meeting-minutes-to-jira, action-items-examples-template |
| /use-cases/user-interviews and /use-cases/field-interviews | recruiting-interview-transcription, transcribe-audio-to-text, voice-memo-transcription |
| /use-cases/lectures | voice-memo-transcription, transcribe-audio-to-text, ai-voice-recorders |
| /use-cases/doctor-visits | medical-transcription-software, voice-memo-transcription, ai-voice-recorders |
| /compare/otter, /compare/fireflies, /compare/granola, /compare/fathom | best-ai-note-takers, best-free-ai-note-takers, and zoom-note-taker (or ai-note-taker-microsoft-teams on /compare/fireflies) |
| /security | legal-transcription-service, medical-transcription-software |

When done, run the build and lint. Then:
- for every post and service page above, list the links you added (anchor text and target),
- list any planned link you could not place, and why,
- check that no link points to a URL that returns 404 or a redirect.
