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
