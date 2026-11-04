# Inbound links: insertion spec for the 12 new articles

The inbound-link rule is a HARD gate: every article needs 1-2 **inbound** internal links, from
pages already live on lynkk.ai pointing **to** the new article. That is separate from, and in
addition to, the outbound links each article already carries.

These edits are on live pages, so they need the CMS. Everything below is ready to paste.

**How this was built.** All 26 candidate source pages were fetched live on 4 November 2026. For
each row the script checked three things: the host sentence appears on that page verbatim, the
proposed anchor is not already used as a link on that page (the no-duplicate-anchor rule), and
the page does not already link the target. All 25 rows passed. Re-run before pasting if the site
has changed:

```bash
python3 -I spec_check.py
```

**Two patterns, matching the site's own conventions.**
- **Contextual (body):** a descriptive anchor inside an existing sentence. Replace the whole
  sentence with the "after" text.
- **Related module:** add the article to the existing "Related guides" (product pages) or
  "More from the blog" (blog posts) block, anchored on its full title. These blocks hold 3
  items, so adding a fourth may mean dropping one, which is an editorial call.

Every target URL is `https://lynkk.ai/blog/<slug>`. Verify each link is live after publishing.

---

## 1. ai-notetaker-security

**Target:** `/blog/ai-notetaker-security` · 3 inbound (one more than the minimum, because this is
the cluster's pillar)

**A. `/blog/zoom-ai-companion-alternatives`, under the H3 "Retention and audit trail for regulated teams"**

> **Find:** Zoom lets admins decide in one setting whether users can keep AI Companion transcripts.
>
> **Replace with:** Zoom lets admins decide in one setting whether users can keep AI Companion transcripts. If you are drawing up a shortlist, here is [what to ask a vendor about retention and audit logs](https://lynkk.ai/blog/ai-notetaker-security).

**B. `/blog/ai-powered-meeting-assistants`, under the H2 "Is an AI-powered meeting assistant safe to use?"**

> **Find:** An AI meeting assistant is safe to use when the vendor encrypts data, is clear about who can see each note, and does not train AI models on your conversations.
>
> **Replace with:** An AI meeting assistant is safe to use when the vendor encrypts data, is clear about who can see each note, and does not train AI models on your conversations. Those sit alongside [the five checks behind AI notetaker security](https://lynkk.ai/blog/ai-notetaker-security): sign-in, AI subprocessors, retention, audit logs and consent.

**C. `/security`, "Related guides" module**

> Add, anchored on the full title: **AI Notetaker Security in 2026: SSO, SCIM, Retention, Audit Logs and Who Sees Your Transcripts**
>
> The module currently holds Legal Transcription Service vs AI, Medical Transcription Software,
> and Interview Transcription for Recruiters. This is the most on-topic guide for that page.

---

## 2. objection-handling

**Target:** `/blog/objection-handling` · 2 inbound

**A. `/blog/spin-selling`, in the Need-payoff section**

> **Find:** Rackham's finding was that these reduce objections rather than overcome them, because a buyer rarely objects to a benefit they named themselves.
>
> **Replace with:** Rackham's finding was that these reduce objections rather than overcome them, because a buyer rarely objects to a benefit they named themselves. For the ones that still come up, see [how to handle the objections that do come up](https://lynkk.ai/blog/objection-handling).

**B. `/blog/sales-conversation-intelligence`, "More from the blog" module**

> Add: **Objection Handling: How to Use the LAER Framework, With Scripts and Examples**

---

## 3. discovery-call-questions

**Target:** `/blog/discovery-call-questions` · 1 retarget + 1 new

**A. `/blog/meeting-preparation`: RETARGET an existing link**

That page already has the anchor "planning discovery questions before the call", and it currently
points at `/blog/spin-selling`. The new article is the better destination for that exact phrase.

> **Find:** For a first discovery call, add the questions you plan to ask; see planning discovery questions before the call
>
> **Change:** repoint the existing anchor from `/blog/spin-selling` to
> `https://lynkk.ai/blog/discovery-call-questions`. Leave the wording alone.
>
> This is a retarget, not an extra link, so it does not add to the page's link count. SPIN is
> still linked from that page elsewhere, so nothing is orphaned.

**B. `/blog/bant-sales-qualification`, under "What does BANT sales qualification stand for?"**

> **Find:** In practice BANT is four things a rep must be able to answer before a deal enters the forecast, usually recorded as CRM fields after a discovery call.
>
> **Replace with:** In practice BANT is four things a rep must be able to answer before a deal enters the forecast, usually recorded as CRM fields after a discovery call. The four map closely onto [the discovery call questions that surface them](https://lynkk.ai/blog/discovery-call-questions).

---

## 4. call-coaching-software

**Target:** `/blog/call-coaching-software` · 2 inbound

**A. `/blog/sales-conversation-intelligence`, in "What do sales teams need from their calls?"**

> **Find:** Sales teams need three things from every call: context before it, focus during it and accurate follow-up after it. Missing any one of them slows deals down or loses them, and gaps in notes also weaken coaching and handoffs to customer success.
>
> **Replace with:** Sales teams need three things from every call: context before it, focus during it and accurate follow-up after it. Missing any one of them slows deals down or loses them, and gaps in notes also weaken coaching and handoffs to customer success. If coaching is the gap, compare [the tools that turn recorded calls into coaching](https://lynkk.ai/blog/call-coaching-software).

**B. `/blog/gong-pricing`, "More from the blog" module**

> Add: **Call Coaching Software: The 5 Best Tools for Sales Teams in 2026, Compared**
>
> Natural fit: anyone reading Gong's price is comparing coaching platforms.

---

## 5. sales-call-recording-software

**Target:** `/blog/sales-call-recording-software` · 2 inbound

**A. `/blog/zoom-meeting-recorders`, in the FAQ "What is the best Zoom meeting recorder?"**

> **Find:** It depends on what you need afterward. Zoom's own local recording is free but gives you no transcript, and AI recorders add notes.
>
> **Replace with:** It depends on what you need afterward. Zoom's own local recording is free but gives you no transcript, and AI recorders add notes. For customer calls specifically, see [sales call recording software compared on price and consent](https://lynkk.ai/blog/sales-call-recording-software).

**B. `/blog/is-it-legal-to-record-a-meeting`, "More from the blog" module**

> Add: **Best Sales Call Recording Software in 2026: 6 Tools and the Consent Rules**
>
> The consent article is the natural parent for it, and the new article links back, so the pair
> reinforces each other.

---

## 6. real-time-ai-interview-assistant

**Target:** `/blog/real-time-ai-interview-assistant` · 2 inbound

**A. `/blog/recruiting-interview-transcription`, in the software section**

> **Find:** Good software for interview transcription also writes the summary and next steps, so the recruiter only reviews.
>
> **Replace with:** Good software for interview transcription also writes the summary and next steps, so the recruiter only reviews. Candidates have their own tools now, so it is worth knowing about [real-time AI interview assistants and when candidates may use one](https://lynkk.ai/blog/real-time-ai-interview-assistant).

**B. `/features/spotter`, "Related guides" module**

> Add: **Real-Time AI Interview Assistants in 2026: How They Work, and When It's Fair**
>
> Spotter has Interview prep and Mock interview modes, so this is the closest guide to that page.

---

## 7. speech-to-text-mac

**Target:** `/blog/speech-to-text-mac` · 2 inbound

**A. `/blog/dictation-on-mac`, under the H2 "What is the best speech to text Mac app for meetings and work?"**

> Add as the first sentence of that section, before the existing answer:
>
> Dictation is one of several routes, and [all five ways to do speech to text on a Mac](https://lynkk.ai/blog/speech-to-text-mac) covers the rest, including transcribing a recording you already have.
>
> **Scope note:** this is the closest pair in the batch. Keep `/blog/dictation-on-mac` as the
> how-to-and-fix-it page and let the new article own method comparison. Review both in GSC at day
> 21+ and consolidate if they compete for "speech to text mac".

**B. `/features/dictation`, "Related guides" module**

> Add: **How to Use Speech to Text on Mac in 2026: 5 Ways Compared**

---

## 8. record-audio-on-mac

**Target:** `/blog/record-audio-on-mac` · 2 inbound

**A. `/blog/voice-memo-transcription`, in the section on recording at a desk**

> **Find:** If your conversations happen at a desk, record them on a Mac instead of your phone.
>
> **Replace with:** If your conversations happen at a desk, record them on a Mac instead of your phone. Our guide to [how to record audio on a Mac, including system audio](https://lynkk.ai/blog/record-audio-on-mac) covers the built-in options and their limits.

**B. `/blog/transcribe-audio-to-text`, in the intro that scopes the guide**

> **Find:** This guide covers recordings and files.
>
> **Replace with:** This guide covers recordings and files. For [making the recording on a Mac in the first place](https://lynkk.ai/blog/record-audio-on-mac), including the system-audio problem, start there.

---

## 9. best-mac-note-taking-app

**Target:** `/blog/best-mac-note-taking-app` · 2 inbound

**A. `/blog/dictation-on-mac`, in the FAQ "What is the best voice dictation software for Mac?"**

> Add at the end of that answer:
>
> If you are choosing where the text lands as well, see [the best Mac note taking apps](https://lynkk.ai/blog/best-mac-note-taking-app).

**B. `/features/meeting-notes`, "Related guides" module**

> Add: **The Best Mac Note Taking Apps in 2026: 7 Compared, Free and Paid**

---

## 10. best-second-brain-apps

**Target:** `/blog/best-second-brain-apps` · 2 inbound

**A. `/blog/meeting-knowledge-management`, in the FAQ on tools for small teams**

> **Find:** Small teams usually need two knowledge management tools: one place for written documents, such as a shared drive or wiki, and one for meeting knowledge.
>
> **Replace with:** Small teams usually need two knowledge management tools: one place for written documents, such as a shared drive or wiki, and one for meeting knowledge. For the first of those, see [the best second brain apps compared](https://lynkk.ai/blog/best-second-brain-apps).

**B. `/features/ask-your-meetings`, "Related guides" module**

> Add: **Best Second Brain Apps in 2026: 7 Tools Compared, Free to Paid**

---

## 11. personal-knowledge-management

**Target:** `/blog/personal-knowledge-management` · 2 inbound

**A. `/blog/meeting-knowledge-management`, under "What are knowledge management tools?"**

> **Find:** Knowledge management tools are software that help a team capture, organize, find and share what it knows.
>
> **Replace with:** Knowledge management tools are software that help a team capture, organize, find and share what it knows. One person doing the same job for themselves is [the personal version of the same problem](https://lynkk.ai/blog/personal-knowledge-management).

**B. `/blog/founders-meeting-notes`, "More from the blog" module**

> Add: **Personal Knowledge Management: Systems, Methods and How to Start**

**Note:** this page now carries two inbound links to different new articles (A here, and 10A
above). Different anchors, different targets, different sections, so neither is a duplicate.

---

## 12. live-caption-apps

**Target:** `/blog/live-caption-apps` · 2 inbound

**A. `/blog/google-meet-transcript`, in the conclusion**

> **Find:** Your Google Meet transcript lives in the organizer's Drive, in the Google Meet folder, and arrives within a few hours on a supported Workspace plan.
>
> **Replace with:** Your Google Meet transcript lives in the organizer's Drive, in the Google Meet folder, and arrives within a few hours on a supported Workspace plan. During the call you can also turn on [live captions, which are not the same as a transcript](https://lynkk.ai/blog/live-caption-apps).

**B. `/features/chrome-extension`, "Related guides" module**

> Add: **Live Caption Apps and Chrome Extensions in 2026: What's Built In, and What Isn't**

---

## Coverage check

| Article | Inbound links | Sources |
|---|---|---|
| ai-notetaker-security | 3 | zoom-ai-companion-alternatives, ai-powered-meeting-assistants, /security |
| objection-handling | 2 | spin-selling, sales-conversation-intelligence |
| discovery-call-questions | 2 | meeting-preparation (retarget), bant-sales-qualification |
| call-coaching-software | 2 | sales-conversation-intelligence, gong-pricing |
| sales-call-recording-software | 2 | zoom-meeting-recorders, is-it-legal-to-record-a-meeting |
| real-time-ai-interview-assistant | 2 | recruiting-interview-transcription, /features/spotter |
| speech-to-text-mac | 2 | dictation-on-mac, /features/dictation |
| record-audio-on-mac | 2 | voice-memo-transcription, transcribe-audio-to-text |
| best-mac-note-taking-app | 2 | dictation-on-mac, /features/meeting-notes |
| best-second-brain-apps | 2 | meeting-knowledge-management, /features/ask-your-meetings |
| personal-knowledge-management | 2 | meeting-knowledge-management, founders-meeting-notes |
| live-caption-apps | 2 | google-meet-transcript, /features/chrome-extension |

All 12 meet the 1-2 inbound minimum. No source page is asked for more than 2 new links, and no
anchor is reused on any page.

## After publishing

1. Publish the 12 articles together, so the 7 links between them resolve.
2. Make these inbound edits.
3. Verify each inbound link is live on the source page, not just saved in the CMS.
4. Record the date. Measure in GSC at day 21+, and check the three cluster pairs named in
   WAVE-REPORT.md for cannibalization.
