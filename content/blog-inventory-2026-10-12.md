# Lynkk Blog Inventory and Duplicate Check (2026-10-12)

Sources: live lynkk.ai (sitemap, /blog, /blog/rss.xml) and every branch of this repo. Earlier Claude sessions
wrote the drafts on two branches:
- `claude/hopeful-planck-otl5pz` ("SEO blog strategy for USA market", 2026-09-30): the 25-article bundle
- `claude/eager-tesla-cvuh6f` (2026-10-01): the same 25, plus 7 more in `articles/` and 5 superseded drafts in `blog/`

Totals: **32 articles written** (19 live + 13 unpublished), plus 5 superseded drafts.

## Live on lynkk.ai (19)

| Published | Slug | Title |
|---|---|---|
| 2026-10-02 | best-ai-note-takers | The Best AI Note Takers in the US for 2026, Compared Online and In Person |
| 2026-10-03 | best-free-ai-note-takers | Best Free AI Note Takers in the USA for 2026 and What Each Plan Includes |
| 2026-10-03 | zoom-meeting-recorders | Top Zoom Meeting Recorders for US Teams in 2026, From Free Tools to AI Notes |
| 2026-10-04 | ai-note-taker-microsoft-teams | Best Teams AI Note Takers for US Businesses in 2026, From Copilot to Lynkk |
| 2026-10-04 | transcribe-audio-to-text | How to Transcribe Audio to Text in 2026 With the Top Voice Recognition Software |
| 2026-10-05 | ai-voice-recorders | Top AI Voice Recorders in 2026: Plaud Note Pro, Pocket and App-Based Alternatives |
| 2026-10-05 | ai-transcription-software | Best AI Transcription Software in the USA for 2026, From Lynkk to Otter.ai |
| 2026-10-06 | voice-to-text-apps | Best Voice to Text Apps and Dictation Software in 2026 for Mac, Windows and Word |
| 2026-10-06 | ai-powered-meeting-assistants | Best AI-Powered Meeting Assistants in the US for 2026, Online and In Person |
| 2026-10-07 | zoom-ai-companion-alternatives | Top Zoom AI Companion Alternatives for 2026, Compared on Price, Features and Follow-Up |
| 2026-10-07 | how-to-transcribe-zoom-meetings | How to Transcribe Zoom Meetings and Get a Zoom Transcript on Any Zoom Plan |
| 2026-10-08 | dictation-on-mac | How to Use Dictation on Mac, Fix It When It Stops Working, and Go Further |
| 2026-10-08 | dictate-in-microsoft-word | How to Dictate in Microsoft Word and When You Need Microsoft Word Dictation Software |
| 2026-10-09 | voice-memo-transcription | How Voice Memo Transcription Works on iPhone and How to Turn Memos Into Notes |
| 2026-10-09 | google-meet-transcript | How to Get a Google Meet Transcript and What Gemini AI Notes Can Do |
| 2026-10-10 | sales-conversation-intelligence | How Sales Teams Use Conversation Intelligence to Prepare, Follow Up and Close More Deals |
| 2026-10-10 | recruiting-interview-transcription | How Recruiters and Hiring Teams Use Interview Transcription to Run Better Debriefs and Hire Faster |
| 2026-10-11 | meeting-minutes-to-jira | How Product Teams Turn Meeting Minutes Into Jira Issues With AI Meeting Minutes |
| 2026-10-11 | founders-meeting-notes | How Founders Keep Up With Back-to-Back Meetings Using AI Meeting Notes and One AI Teammate |

## Written but not published (13)

| Slug | Title | Primary keyword (vol / SD, from the plan) | Branch |
|---|---|---|---|
| one-on-one-meeting | How Managers Run a Better One-on-One Meeting With AI Notes, Questions and a Template | one on one meeting questions (cluster 4,700) | both |
| meeting-minutes-sample | Meeting Minutes Sample for Teams and Boards, With a Format You Can Copy and Automate | board meeting minutes sample (cluster 6,180) | both |
| daily-standup-meeting | How Engineering Teams Run a Faster Daily Standup Meeting in Scrum With AI Notes | standup meeting (cluster 3,450) | both |
| meeting-knowledge-management | Your Meetings Are Your Knowledge Base: How Knowledge Management Tools Build Searchable Meeting Memory | km software (cluster 1,600) | both |
| legal-transcription-service | How Law Firms Use AI Instead of a Legal Transcription Service, and When Not To | best legal transcription software (cluster 1,100) | both |
| medical-transcription-software | How Clinicians Use Medical Transcription Software and AI Dictation to Cut Documentation Work | medical dictation software (cluster 1,490) | both |
| how-to-record-google-meet | How to Record Google Meet Calls, Even When the Record Button Is Missing | how to record google meet (2,400 / 25) | eager-tesla |
| record-whatsapp-call | How to Record WhatsApp Calls on iPhone, Android and Mac, and Get Notes Afterward | record whatsapp call (1,300 / 35) | eager-tesla |
| slack-huddle-notes | Slack Huddle Notes: How to Record, Transcribe and Summarize a Huddle on Your Mac | slack huddle (1,000 / 46) | eager-tesla |
| how-to-record-webex-meeting | How to Record Webex Meetings and Get a Webex Transcript on Any Plan | how to record webex meeting (590 / 23) | eager-tesla |
| record-facetime-call | How to Record FaceTime Calls on iPhone and Mac, With Audio From Both Sides | record facetime call (480 / 30) | eager-tesla |
| meeting-notes-template | Free Meeting Notes Template, Plus 9 Templates for Standups, 1:1s, Sales Calls and More | meeting notes template | eager-tesla |
| follow-up-email-after-meeting | Follow-Up Email After Meeting a Client or Your Team: 8 Examples to Copy | follow up email after meeting | eager-tesla |

## Superseded drafts (`blog/` on eager-tesla; its README says do not publish)

how-to-record-a-teams-meeting, how-to-transcribe-zoom-meetings (second version), action-items-examples-and-template,
ai-note-taking, conversation-intelligence-platform. They also use Lynkk claims that `lynkk-post-kit/docs/TRUTHS.md` forbids.

## Duplicate and overlap check

**Repeated titles:** none. No two different articles share a title. The 25 bundle articles appear on both branches as
identical copies, which is not a problem.

**Same keyword, two articles (do not publish the second):**
1. `blog/how-to-transcribe-zoom-meetings` repeats the live `how-to-transcribe-zoom-meetings` (both target "transcribe zoom").
2. `blog/conversation-intelligence-platform` repeats the live `sales-conversation-intelligence` (both target "conversation intelligence platform").
3. `blog/ai-note-taking` overlaps the live `best-ai-note-takers` (ai note taking vs ai note taker).

**Overlaps to resolve before publishing the unpublished drafts:**
4. `meeting-notes-template` includes 1:1 and standup templates, so it competes with `one-on-one-meeting` and
   `daily-standup-meeting`. It also targets "meeting notes template", which /features/meeting-notes already targets.
   Pick one: publish the template post and cut its 1:1 and standup sections down to short links, or drop it.
5. `meeting-minutes-sample` sits next to the live `meeting-minutes-to-jira` (which targets "meeting minutes").
   Keep the sample post on "board meeting minutes sample" and do not use plain "meeting minutes" as a target.
6. `meeting-knowledge-management` is close to /features/ask-your-meetings (meeting knowledge graph). Keep it on
   "knowledge management software".

**Repeats of topics in my v3 plan (now removed from it):**
7. "How to Record a Google Meet Call": already written (`how-to-record-google-meet`).
8. "One-on-One Meeting Template": already written (`one-on-one-meeting`, which also targets one on one meeting template).
9. "How to Record a Microsoft Teams Meeting": already drafted (`blog/how-to-record-a-teams-meeting`, superseded only for
   its claims, so it needs a rewrite, not a new topic). "Teams Transcription" is covered by the same draft.
10. "Follow-up email after meeting" (v2 backlog): already written.

## Claims conflict to fix

The bundle was aligned to `lynkk-post-kit/docs/TRUTHS.md` (on the draft branches), whose "Don't claim" hard rules
forbid: a bot that speaks in the meeting, CRM anything, data regions or residency, a knowledge graph screen or team-wide
memory, accuracy percentages, "offline-first", uploading existing audio files, and "notes in 30 seconds". `memory/lynkk-brand.md` on the main branch
still lists all of them, and Ubersuggest's business summary adds "97% accuracy" and "AES-256/GDPR".
One source of truth is needed before any new article is written.
