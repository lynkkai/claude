# lynkk.ai site changes: Claude prompts

Prepared 2026-10-14 from the approved items in the Lynkk Blog Audit review.

## How to use

The site is built with Claude (Next.js App Router). Paste each prompt below into that Claude session **one at a time, in order**, and review its answer before moving on. Prompt 4 links to pages that prompts 1 and 3 create, so it must run last.

1. Prompt 1: move the two /articles posts into /blog with redirects
2. Prompt 2: new opening answers and meta descriptions for 23 blog posts, plus body cleanup
3. Prompt 3: service page updates (meeting bot, Hinglish, multilingual, sales calls, action items, compare pages, lectures)
4. Prompt 4: internal links between posts and service pages

Each prompt asks Claude to list the files it will edit before changing anything, and to run the build and lint when done. Prompt 3 asks Claude to show drafted copy before saving it: please send those drafts to marketing for approval.

Not included in this round: the zoom-note-taker opening answer, the how-to post additions, and changes to the user interviews, download, team standups, features hub, pricing and security pages.

---

## Prompt 1: Move /articles into /blog

Copy everything between the lines below.

````text
You are editing the lynkk.ai website (Next.js App Router) in this repository.

Task: move the two posts under /articles into /blog, with permanent redirects, so the blog is one section.

Before changing anything, find where the /articles posts, the /blog posts, the redirects, the sitemap and the blog index are defined, and tell me which files you will edit.

Do this:

1. Publish /articles/zoom-note-taker at /blog/zoom-note-taker, and /articles/action-items-examples-template at /blog/action-items-examples-template. Keep the content, title, meta description, author and dates exactly as they are.
2. Add permanent redirects (use the same redirect type the site already uses, which is 308):
   - /articles/zoom-note-taker to /blog/zoom-note-taker
   - /articles/action-items-examples-template to /blog/action-items-examples-template
   - /articles to /blog
3. Update each moved post's canonical URL, Open Graph URL, breadcrumbs and JSON-LD (BlogPosting, BreadcrumbList) to the new /blog URL.
4. In sitemap.xml, remove the /articles URLs and add the two new /blog URLs.
5. List both posts on the /blog index and on the author page (/blog/authors/samarth-wagh), sorted by date like the others.
6. Find every internal link on the site that points to /articles/... and change it to the new /blog/... URL.
7. If the /articles index page has its own route, remove it (the redirect replaces it).

Rules:
- Brand is always "Lynkk".
- Never use em dashes or en dashes in any copy. Use a comma, colon or parentheses instead.
- Do not change any other page.

When done, run the build and lint. Then list every file changed, confirm each old URL returns a 308 to its new URL, and confirm the sitemap no longer lists /articles.
````

---

## Prompt 2: Blog snippets and body cleanup

Copy everything between the lines below.

````text
You are editing the lynkk.ai website (Next.js App Router) in this repository.

Task: make the blog's search snippets read like help instead of ads. Replace the opening "Quick answer" text of 23 posts, replace 12 meta descriptions, and remove self-promotional claims from the post bodies.

Before changing anything, find where each post's content, "Quick answer" box, meta description, Open Graph and Twitter descriptions, and JSON-LD (BlogPosting, FAQPage, ItemList) are defined, and tell me which files you will edit.

Rules:
- Brand is always "Lynkk".
- Never use em dashes or en dashes in any copy. Use a comma, colon or parentheses instead.
- Do not change any page title (<title>) or URL.
- Use the new text below exactly as written. Do not add facts, prices or claims that are not already in the post.
- Where the Open Graph or Twitter description currently copies the meta description, update it to the new meta description too.
- If a post's JSON-LD repeats the old Quick answer or meta text, update it to match.
- Do not change the Quick answer or meta description of /blog/zoom-note-taker (still under review). Part 2 below does apply to it.

Part 1: replace the Quick answer and meta description

For each post, replace the whole text after "Quick answer:" with the new opening answer. Where a new meta description is given, replace the meta description. "No change" means keep the current meta description.

### /blog/best-ai-note-takers

New opening answer:

> An AI note taker records a meeting, transcribes it and turns it into a summary with action items. For free unlimited recording of video calls, Fathom. For live transcripts, Otter (from $8.33 a month). For a searchable sales call library, Fireflies. For notes before, during and after the call, including in-person meetings, Lynkk (Pro $15 a month).

New meta description:

> Fathom, Otter, Fireflies, Granola, Read AI and more side by side: free limits, paid plans from $8.33, bot or bot-free, and fit for Zoom, Teams or Meet.

### /blog/best-free-ai-note-takers

New opening answer:

> A free AI note taker records your meetings and writes notes and action items at no cost, within limits on minutes, meetings or history. Fathom offers unlimited free recording for video calls, Otter gives 300 minutes a month, and Granola keeps 30 days of history. Lynkk has a Free plan, and Pro adds the meeting bot for Zoom, Teams and Google Meet for $15 a month.

New meta description:

> Free AI note taker plans compared: Fathom's unlimited recording, Otter's 300 minutes, Granola's 30-day history and 5 more, plus what each upgrade costs.

### /blog/ai-note-taker-microsoft-teams

New opening answer:

> A Teams AI note taker records a Microsoft Teams meeting and turns it into a summary, decisions and action items. Microsoft 365 Copilot does this inside Teams for $30 per user per month on top of a Microsoft 365 license, and Teams' built-in transcription is free. Third-party tools such as Otter, Fireflies, Fathom and Lynkk add bot-free recording or cover Zoom, Google Meet and in-person meetings too.

New meta description:

> Is Copilot worth $30 a user? Compare Teams Premium recap, free Teams transcription, Otter, Fireflies, Fathom and Lynkk on cost for a 10-person team.

### /blog/ai-powered-meeting-assistants

New opening answer:

> An AI-powered meeting assistant helps around a meeting: it can prepare you before the call, support you live during it, and write notes and tasks after it. Built-in assistants (Zoom AI Companion, Copilot in Teams, Gemini in Google Meet) work inside one platform. Otter, Fireflies, Read AI and Fathom focus on transcripts and notes after the call. Lynkk covers all three stages, including in-person meetings.

New meta description:

> Most AI meeting tools only summarize afterward. See which of 8 assistants also help before and during the call, with free plans and prices for each.

### /blog/ai-transcription-software

New opening answer:

> AI transcription software converts speech in meetings, interviews and audio files into text automatically, usually within minutes. Pick by job: Otter for live transcripts, Rev for per-minute file jobs at $0.25 a minute, Descript for editing audio by editing text, and meeting tools such as Fireflies or Lynkk when you also want notes and action items.

New meta description:

> Compare 7 AI transcription tools by job: live transcripts, file uploads at $0.25 a minute, editing by text, and meeting notes. Free plans included.

### /blog/ai-voice-recorders

New opening answer:

> An AI voice recorder captures conversations and turns them into transcripts, summaries and action items. Dedicated devices such as Plaud Note Pro ($189) and Pocket record without your phone. Apps such as Otter, Granola and Lynkk use the laptop or phone you already carry. Choose a device for long recordings away from a computer, and an app if you mostly record meetings.

New meta description:

> Plaud Note Pro costs $189 before any plan. Compare AI voice recorder devices with phone and laptop apps on 12-month cost, setup and transcripts.

### /blog/transcribe-audio-to-text

New opening answer:

> To transcribe audio to text, record or upload your audio, let voice recognition software convert the speech, then review and export the transcript. AI tools do this in minutes for $0 to $0.25 a minute, while human transcription costs about $1.99 a minute. Free or included options: Word Transcribe (Microsoft 365), Mac Dictation and Windows voice typing.

New meta description:

> 4 steps to turn any recording into text, free options in Word, Mac and Windows, and 7 tools from $0 to $0.25 a minute compared on price and features.

### /blog/voice-to-text-apps

New opening answer:

> A voice to text app turns your speech into typed text as you talk, so you can write emails, notes and documents without a keyboard. The best free options are built in: Apple Dictation (press Fn twice), Windows voice typing (Windows key + H) and Google Docs voice typing. Paid options include Dragon Professional for heavy Windows use, and Lynkk for push-to-talk dictation on Mac plus meeting transcripts.

New meta description:

> Free built-in dictation vs paid apps: what Apple Dictation, Windows voice typing, Google Docs, Word Dictate and Dragon do well, and what each costs.

### /blog/zoom-ai-companion-alternatives

New opening answer:

> Zoom AI Companion is Zoom's built-in AI assistant, included at $0 extra with paid Zoom Workplace plans, that writes meeting summaries, live notes and next steps. Look for an alternative if you are on free Zoom, also meet on Teams or Google Meet, or want tasks sent to tools like Jira. Options include Otter, Fireflies, Fathom, Read AI and Lynkk.

New meta description:

> AI Companion needs a paid Zoom plan. Compare 7 alternatives on price, bot or bot-free capture and follow-up, plus how to turn AI Companion off.

### /blog/zoom-meeting-recorders

New opening answer:

> A Zoom meeting recorder captures the audio and video of a Zoom call so you can replay it, transcribe it or turn it into notes. Zoom's built-in local recording is free but gives you a video file with no transcript. Cloud recording adds a transcript on paid plans. AI recorders such as Fathom, Otter, Fireflies and Lynkk add notes and action items.

New meta description:

> Compare 7 Zoom meeting recorders, from free local recording to AI notes: what each saves, what free Zoom allows, and how to record if you are not the host.

### /blog/how-to-transcribe-zoom-meetings

New opening answer:

> You can transcribe Zoom meetings in 3 ways. Zoom creates an audio transcript for cloud recordings on paid plans, but only if the setting was on before the meeting. AI Companion adds a transcript with its meeting summary on paid plans. On a free Zoom account, use a third-party note taker such as Lynkk, which transcribes Zoom in 17 languages.

New meta description:

> Learn 3 ways to transcribe Zoom meetings, where to find and download your Zoom transcript, and how to get one on a free Zoom plan.

### /blog/google-meet-transcript

New opening answer:

> To get a Google Meet transcript, click Meeting tools > Transcribe > Start transcription during the call, on 1 of 8 supported Workspace editions. The transcript saves as a Google Doc in the organizer's Google Drive and arrives by email within a few hours, up to 24. On other plans, or to get notes and action items too, use a third-party note taker such as Lynkk.

New meta description:

> How to get a Google Meet transcript, which Workspace plans include it, where it is saved, fixes when it fails, and what to use when your plan has none.

### /blog/dictation-on-mac

New opening answer:

> Dictation on Mac turns your speech into typed text in any app where you can type. Turn it on in System Settings > Keyboard > Dictation, click where you want the text, and press the Fn key twice (the default shortcut). If it stops working, the 6 checks below fix most cases. For push-to-talk dictation plus meeting transcripts in one app, Lynkk is an alternative.

New meta description:

> No change

### /blog/dictate-in-microsoft-word

New opening answer:

> Word has built-in dictation for Microsoft 365 subscribers: go to Home > Dictate, or press Alt + ` (backquote) on Windows or Option + F1 on Mac, then speak. It needs a microphone and a reliable internet connection. Dictate is enough for most writing in Word. To dictate in other apps too, use your system's built-in dictation or an app such as Dragon or Lynkk.

New meta description:

> No change

### /blog/voice-memo-transcription

New opening answer:

> Voice memo transcription is built into the Voice Memos app on iPhone 12 or later. Tap a recording, tap the More button and choose View Transcript, or swipe up while recording to watch the words appear live. You can copy and search the text. For a summary and action items too, paste the transcript into an AI tool or record with a note taker such as Lynkk.

New meta description:

> No change

### /blog/daily-standup-meeting

New opening answer:

> A standup meeting is a short daily check-in where a team shares progress, plans the next 24 hours and raises blockers. In Scrum it is called the Daily Scrum and lasts 15 minutes. Keep it short with a fixed speaking order, move long discussions to after the standup, and log each blocker with an owner. AI note takers such as Lynkk can write the notes and send blockers to Jira.

New meta description:

> No change

### /blog/one-on-one-meeting

New opening answer:

> A one-on-one meeting is a recurring private conversation between a manager and 1 team member about priorities, blockers, growth and feedback. The best 1:1s follow a simple 5-part agenda, use open questions and end with written next steps. Keep one running notes doc so each 1:1 starts where the last one ended; an AI note taker such as Lynkk can keep it for you.

New meta description:

> No change

### /blog/meeting-minutes-to-jira

New opening answer:

> Meeting minutes are the official written record of a meeting: who attended, what was decided and which action items were assigned to whom. They do not need to be word for word. Product teams save the most time when each action item becomes a Jira issue with an owner and a due date. AI tools such as Lynkk can draft the minutes and send those tasks to Jira.

New meta description:

> No change

### /blog/meeting-knowledge-management

New opening answer:

> Knowledge management tools help a team capture, organize, find and share what it knows, from wikis to search to meeting memory. A wiki holds what people write down, but much of what changes week to week is said in meetings and never written down. Meeting memory tools such as Lynkk link decisions and commitments across calls and answer questions with cited sources.

New meta description:

> No change

### /blog/recruiting-interview-transcription

New opening answer:

> Interview transcription turns a recorded job interview into text with speaker labels, so the hiring team can review what the candidate actually said instead of relying on memory. Recruiters use it in 3 ways: to listen instead of typing, to share evidence in debriefs and to keep hiring records. Get the candidate's consent before recording. Options range from human services to AI apps such as Lynkk.

New meta description:

> No change

### /blog/sales-conversation-intelligence

New opening answer:

> Conversation intelligence is software that records sales conversations, transcribes them and turns them into insights, next steps and follow-up tasks. Sales teams use it in 3 stages: preparing for the call, getting help during it and finishing follow-up after it. Gong is the best-known enterprise platform; lighter tools such as Lynkk (Pro $15 a month) cover notes and next steps.

New meta description:

> No change

### /blog/legal-transcription-service

New opening answer:

> Legal transcription turns recordings of legal work, such as client meetings, interviews and dictated memos, into text. Use a human legal transcription service for verified, word-for-word text; official court transcripts come only from certified court reporters. AI transcription such as Lynkk fits everyday client meetings and case team calls, with speaker-labeled transcripts and notes after the call.

New meta description:

> No change

### /blog/medical-transcription-software

New opening answer:

> Medical transcription software turns clinical speech into text, either as live dictation into the health record or as a transcript of a recorded conversation. For clinical charting, choose a tool with accuracy on medical terms, EHR integration and HIPAA safeguards, including a signed business associate agreement (BAA). General meeting tools such as Lynkk suit care team meetings, admin calls and patients' own visit notes rather than charting.

New meta description:

> No change

Part 2: clean up the body of every post (all 26 posts, including zoom-note-taker)

1. Remove every claim that Lynkk is "the best" (for example "Lynkk is the best AI note taker in 2026", "See why Lynkk leads", "Lynkk is the smarter choice"). Rewrite each one as a plain statement of what Lynkk does, using facts already in that sentence. Example: "Lynkk is the best Zoom meeting recorder because it records Zoom with a bot or bot-free" becomes "Lynkk records Zoom with a bot or bot-free".
2. In every list or comparison post, label the Lynkk entry as ours and replace "best ... overall" with what it is best for, using a difference the post already states. Example: "1. Lynkk: best AI note taker overall" becomes "1. Lynkk (our product): best for notes before, during and after the call".
3. Keep one call to action per post (the existing "Try Lynkk free" box). Remove any other repeated sign-up prompts in the body, but keep the header and footer buttons.
4. Keep the existing Disclosure line.

When done, run the build and lint. Then:
- list every post changed, with old and new meta description side by side,
- search all post content for "the best" next to "Lynkk", "Lynkk leads" and "smarter", and confirm none remain,
- search all changed copy for em dashes and en dashes, and confirm there are none.
````

---

## Prompt 3: Service pages

Copy everything between the lines below.

````text
You are editing the lynkk.ai website (Next.js App Router) in this repository.

Task: update seven service pages so they match what searchers want: the meeting bot page, a restored Hinglish page, the multilingual page, sales calls, action items, the four compare pages and lectures. Internal links between pages are a separate task; only add the links this prompt names.

Before changing anything, find where each page's content, H1, metadata, FAQ and JSON-LD are defined, and tell me which files you will edit.

Rules:
- Brand is always "Lynkk".
- Never use em dashes or en dashes in any copy. Use a comma, colon or parentheses instead.
- Do not change any page title (<title>) unless this prompt gives a new one.
- Do not invent product facts. Use only what the site already says about Lynkk (features, languages, plans, prices). Do not mention CRM sync anywhere in this task.
- Keep the existing design and components. New sections reuse the page's existing section and FAQ components.
- Wherever this prompt says "draft", show me the drafted text before you save it, and wait for my OK.
- When you add an FAQ, add it to the page's FAQPage JSON-LD too.

1. /features/meeting-bot

- Change the H1 to: An AI meeting bot that takes notes in Zoom, Meet and Teams
- Change the meta description to: Send Lynkk's bot to any Zoom, Google Meet or Teams call. It records, transcribes in 17 languages and sends notes and action items after the call.
- Add this FAQ to the page's FAQ section:
  - Q: Is Lynkk a meeting bot API for developers?
  - A: No. Lynkk's meeting bot takes notes for you in Zoom, Google Meet and Teams calls. It is not a tool for building your own bots.

2. Restore /features/hinglish-transcription as its own page

- Remove the redirect from /features/hinglish-transcription to /features/multilingual-transcription.
- Build the page with the same layout as /features/multilingual-transcription, focused on Hinglish: meetings where Hindi and English mix, often in one sentence. Reuse the Hinglish facts already on the multilingual page (Hinglish mode, auto-detect, speaker labels, the limits section, which plan includes it). Draft the copy.
- Title: Hinglish Transcription for Meetings | Lynkk
- Meta description: Transcribe Hinglish meetings, where Hindi and English mix in one sentence, with speaker labels and a searchable transcript. One of Lynkk's 17 languages.
- H1: Hinglish transcription for meetings that mix Hindi and English
- Link to /features/multilingual-transcription from the page ("all 17 languages").
- Add the page to sitemap.xml and to the features navigation wherever the other feature pages are listed.

3. /features/multilingual-transcription

- Change the H1 to: Multilingual and Hinglish transcription that doesn't fall apart
- In the Hinglish section, link the word "Hinglish" to /features/hinglish-transcription.

4. /use-cases/sales-calls

- Draft and add a "Sample sales call note" section: a short example note in the same format as the page's "What you read after the conversation" section, with 3 next steps that each have an owner and a due date. Label it as an example.
- Draft and add a short "Sample follow-up email" written from that note (about 80 words).
- Draft and add a section "Record in-person and offline sales meetings": record a sales meeting in the room on the Mac app, with no signal if needed, and Lynkk uploads and writes the note when you are back online. Use only what /use-cases/field-interviews and /download already say about offline recording.
- In the new sections, link "conversation intelligence" to /blog/sales-conversation-intelligence and "Fireflies" (if you mention it) to /compare/fireflies.

5. /features/action-items

- Draft and add an "Examples" section with 3 action items in Lynkk's format (action, owner, due date), labeled as examples.
- Add this FAQ, with a 2 to 3 sentence answer drafted from what the page already says about how Lynkk finds owners and due dates: How does AI find action items in a meeting?
- Link "action items template" to /blog/action-items-examples-template in the new Examples section.

6. Compare pages: /compare/otter, /compare/fireflies, /compare/granola, /compare/fathom

Change only the H1 and meta description:

| Page | New H1 | New meta description |
| --- | --- | --- |
| /compare/otter | Lynkk vs Otter.ai: an Otter alternative for in-person and multilingual meetings | Looking for an Otter.ai alternative? Compare Lynkk and Otter on bot-free recording, languages, Jira and Slack, and both price lists as of October 2026. |
| /compare/fireflies | Lynkk vs Fireflies.ai: a Fireflies alternative for in-person and multilingual meetings | Looking for a Fireflies.ai alternative? Compare Lynkk and Fireflies on bot-free recording, languages, Jira and Slack, and both price lists in October 2026. |
| /compare/granola | Lynkk vs Granola: a Granola alternative for in-person and multilingual meetings | Looking for a Granola alternative? Compare Lynkk and Granola on how each records, languages, platforms, Jira and Slack, and what each costs. |
| /compare/fathom | Lynkk vs Fathom: a Fathom alternative for in-person and multilingual meetings | Looking for a Fathom alternative? Compare Lynkk and Fathom on bot-free recording, in-person meetings, languages, Jira and Slack, and both price lists. |

7. /use-cases/lectures

- Draft and add a "Sample lecture note" section in the page's existing note format: key takeaways with timestamps, topics, and a line showing the full transcript is attached. Label it as an example.
- Add this FAQ, with a 2 to 3 sentence answer: Do I need permission to record a lecture? The answer should say to ask the lecturer first and to check the school's recording rules. Do not give legal advice.

When done, run the build and lint. Then list every page changed with its new H1 and meta description, confirm /features/hinglish-transcription returns 200 (not a redirect), and confirm it is in sitemap.xml.
````

---

## Prompt 4: Internal links

Copy everything between the lines below.

````text
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
````

