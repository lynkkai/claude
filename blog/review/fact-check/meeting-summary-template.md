# Fact check: meeting-summary-template

Article: `articles/meeting-summary-template.md`
Date checked: 2026-10-18 (3 rounds, per the aeo-article skill). Recorded after the fact: the article itself was finished and committed in 75b1a05.

| # | Claim (short) | Source URL fetched | Status | Fix |
|---|---|---|---|---|
| 1 | A meeting summary runs 5 to 10 lines and covers purpose, decisions, actions, open questions, next meeting | https://www.claap.io/blog/meeting-summary | VERIFIED | Claap lists the same components (metadata, discussion, decisions, action items, next steps) |
| 2 | Summary vs minutes: minutes are the formal record | https://robertsrules.com/frequently-asked-questions/ | VERIFIED | Robert's Rules: minutes record what was done, not what was said; added to FAQ 3 |
| 3 | Microsoft Teams "can generate an AI recap for licensed users" | https://support.microsoft.com/en-us/teams/meetings/recap-in-microsoft-teams | FIXED | Intelligent recap needs Teams Premium or a Microsoft Copilot license, and the meeting must have been recorded or transcribed |
| 4 | Teams recap sharing limits | https://support.microsoft.com/en-us/teams/meetings/recap-in-microsoft-teams | VERIFIED | People outside the org cannot open a recap even with the link; added as FAQ 1's edge case |
| 5 | Summary length guidance | https://www.grammarly.com/blog/emailing/follow-up-email/ | VERIFIED | 50 to 125 words for most follow-ups; added to FAQ 2 |
| 6 | Send timing: within an hour, same day | https://www.grammarly.com/blog/emailing/follow-up-email/ | FIXED | FAQ 4 previously asserted "summaries sent the next day get read far less" with no source; now 1 hour with 1 business day as the outer limit, per Grammarly's recap advice |
| 7 | "Roughly 15 minutes per hour of recording" | no primary source | FIXED | Marked (industry estimate) |
| 8 | Lynkk writes the summary with decisions, tasks with owners and dates, open questions, each timestamped | https://lynkk.ai/features/meeting-notes | VERIFIED | Used in the CTA |
| 9 | Send to Jira, 1 issue per action item | https://lynkk.ai/features/action-items | VERIFIED | Sends every item on the note at once; status does not sync back |
| 10 | Decision log and Ask Lynkk are Pro | https://lynkk.ai/pricing | VERIFIED | CTA now says "On Pro" |
| 11 | "Free for 5 meetings a month" | https://lynkk.ai/pricing | FIXED | Free plan is 5 notes per month, 2 hours per note; linked to /pricing |
| 12 | Claap and Microsoft links live | both URLs above | VERIFIED | HTTP 200 on 2026-10-18 |

Round 2 (omission): the Teams recap claim now names the license and the recording requirement, and the free-plan line names the note cap.

Round 3 (contradictions): the Quick answer, tldr and body all say 5 parts, 5 to 10 lines, sent within the hour, and the FAQ answers no longer give a different window.
