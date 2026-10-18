---
title: "How to Remove Fireflies.ai From Teams, Zoom and Meet in 2026"
meta_title: "How to Remove Fireflies.ai From Teams, Zoom and Meet in 2026"
meta_description: "How to remove Fireflies AI from Teams, Zoom and Google Meet in 2026: kick Fred out of a live call, stop auto-join, block it as an admin and delete the account."
slug: remove-fireflies-ai-from-teams
primary_keyword: "how to remove fireflies ai from teams"
secondary_keywords:
  - "remove fireflies ai from teams meetings"
  - "how to disable fireflies ai in teams"
  - "remove fireflies ai from microsoft teams permanently"
  - "how to remove fireflies from zoom"
  - "is fireflies ai safe"
market: US
cluster: switching
internal_link_target: "https://lynkk.ai/compare/fireflies"
inbound_links:
  - from: "https://lynkk.ai/blog/ai-note-taker-microsoft-teams"
    anchor: "how to remove Fireflies AI from Teams"
  - from: "https://lynkk.ai/blog/zoom-bot-join-meeting"
    anchor: "remove an unwanted meeting bot"
  - from: "https://lynkk.ai/compare/fireflies"
    anchor: "how to remove Fireflies from Teams"
tldr: "To remove Fireflies from a Teams call, open Participants, click the three dots next to Fireflies and choose Remove from meeting, or type /ff leave in the chat. To stop it for good, set auto-join to Only when I invite, remove fred@fireflies.ai from invites, and have an admin block the app or delete the Fireflies account."
author: "Samarth Wagh, Co-founder, Lynkk.ai"
author_url: "https://lynkk.ai/blog/authors/samarth-wagh"
last_updated: 2026-10-17
featured_image_alt: "How to remove Fireflies AI from Teams meeting participants list step by step"
---

# How to Remove Fireflies.ai From Teams, Zoom and Meet in 2026

*By [Samarth Wagh](https://lynkk.ai/blog/authors/samarth-wagh), Co-founder, Lynkk.ai · Last updated 17 October 2026*

> **Quick answer:** For how to remove Fireflies AI from Teams in under 30 seconds: open **Participants**, click **(...)** next to Fireflies and choose **Remove from meeting**, or type **/ff leave** in the meeting chat. To stop it joining again, set Fireflies auto-join to **Only when I invite**, remove **fred@fireflies.ai** from calendar invites, and ask your Teams admin to **block the app**. Deleting the Fireflies account stops it completely.

*Disclosure: Lynkk publishes this guide and makes a different AI meeting assistant. Steps come from Fireflies' help center and Microsoft's community answers, checked 17 October 2026.*

If you are searching for how to remove Fireflies AI from Teams, you are probably in one of two situations. Either the Fireflies bot just showed up in your meeting and you want it gone, or it keeps coming back no matter what you do. This guide covers both, for Microsoft Teams, Zoom and Google Meet.

Fireflies usually joins because someone on the invite connected their calendar to Fireflies, and its auto-join setting sent the bot, called Fred, into every meeting. Removing it once fixes today. Fixing the setting fixes tomorrow.

## How do you remove Fireflies AI from a Teams meeting right now?

There are 3 ways to remove Fireflies from a live Microsoft Teams meeting, and each takes under 30 seconds:

1. **From the participant list:** open **Participants**, click **(...)** next to Fireflies, then select **Remove from meeting**. You need organizer or presenter rights.
2. **From the chat:** type `/ff leave` in the meeting chat. Fireflies leaves the call.
3. **From the Fireflies dashboard:** the person who owns the bot can click the **Stop** icon on the Live meeting banner on their Home dashboard.

Fireflies' help center notes that if it is removed within the first 3 minutes, no transcript or notes are created ([Fireflies guide](https://guide.fireflies.ai/articles/7098191513-how-to-remove-fireflies-from-a-meeting-or-stop-it-from-joining)).

## How do you remove Fireflies from Zoom and Google Meet?

The steps are almost identical in Zoom and Google Meet, and take about 10 seconds:

| Platform | Steps |
|---|---|
| Zoom | Open the participant list, click **More** next to Fireflies Notetaker, then **Remove** |
| Google Meet | Open the participant list, click the three-dot icon next to Fireflies, then **Remove from the call** |
| Any platform | Type `/ff leave` in the meeting chat |

In Zoom you must be the host or co-host to remove a participant. In Google Meet, if Host Management is on, only hosts and co-hosts can remove people.

## How do you stop Fireflies from joining your meetings automatically?

To stop Fireflies from auto-joining, change its settings in 3 places. Do all 3 if the bot keeps returning:

1. **Change auto-join.** In the Fireflies dashboard or settings, find **Auto-join calendar meetings** (or Auto-record meetings) and choose **Only when I invite**, using `fred@fireflies.ai`.
2. **Turn it off for specific meetings.** On the Fireflies home page, open the **Upcoming** tab, find the meeting and toggle Fireflies **off**.
3. **Remove Fred from invites.** Edit the event in Google Calendar or Outlook, delete `fred@fireflies.ai` from the guest list, and save.

Fireflies also has **Recording Rules** that block meetings by keyword, email address or domain. Rules override auto-join, so you can block all external client meetings, for example.

## How do you remove Fireflies AI from Microsoft Teams permanently?

To remove Fireflies AI from Microsoft Teams permanently, 2 people usually need to act: the person whose account sends the bot must delete their Fireflies account or disconnect it, and a Teams admin should block the app. Doing only one of these often leaves the bot joining.

**If you own the Fireflies account:**

1. Sign in at app.fireflies.ai with the same Microsoft account you connected.
2. Go to **Settings**, scroll down and use the delete option to remove the account.
3. Check Microsoft's app permissions for your account and remove Fireflies if it still has access.

**If someone else's Fireflies keeps joining your meetings:** ask them to change their auto-join setting, or remove `fred@fireflies.ai` from the invite each time. You cannot delete another person's account.

## How does a Teams admin block Fireflies for the whole company?

A Teams admin can block the Fireflies app in 4 steps in the Teams admin center, as described in a Microsoft community answer ([Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/4429002/removing-fireflies-ai-note-taker-bot-from-microsof)):

1. Open the **Teams admin center** and go to **Teams apps**, then **Manage apps**.
2. Search for **Fireflies**.
3. Select the app and choose **Block**.
4. Confirm the status shows **Blocked**.

Users in the same thread report that blocking the app alone did not always stop the bot, because Fireflies can join as a meeting participant through calendar access. Admins often add 2 more controls:

- **Lobby settings:** set meeting options so only organizers and co-organizers bypass the lobby. The bot then waits in the lobby where the organizer can deny it.
- **App consent:** review enterprise applications in Microsoft Entra ID and restrict or remove Fireflies' access to calendars and sign-in.

Menu names change over time, so check Microsoft's current documentation for your tenant.

## Is Fireflies AI safe, and why does it join meetings uninvited?

Fireflies is a legitimate, widely used product with HIPAA and SSO on its $39 Enterprise plan, and joining "uninvited" is usually a settings issue, not a security breach. When one attendee connects their calendar with auto-join on, Fred joins every meeting on that calendar, including meetings other people organized.

Still, treat any recorder you did not expect as a privacy question. Ask who owns the bot, where the recording goes, and whether everyone agreed. Several US states require all parties to consent before a call is recorded.

## What can you use instead of Fireflies?

If you are removing Fireflies because a visible bot bothers clients, or because it joins too many meetings, choose a tool with tighter control over when it records.

Lynkk (our product) gives you both options: a bot for Zoom, Google Meet and Teams that you can send to a single call by pasting the link, or bot-free recording through its Mac app and Chrome extension. It also records in-person meetings. After each meeting it lists tasks with owners and dates, a decision log and one-click Jira tickets, and Ask Lynkk searches past meetings with citations. Free covers 5 notes a month; Pro is $15 a month.

[Try Lynkk free](https://lynkk.ai/)

For more choices, see [Otter vs Fireflies vs Fathom](https://lynkk.ai/blog/otter-ai-vs-fireflies-ai) and our guide to [Teams AI note takers](https://lynkk.ai/blog/ai-note-taker-microsoft-teams).

## How do you remove Fireflies from Outlook and your calendar?

To remove Fireflies from Outlook in 2 steps, delete `fred@fireflies.ai` from the attendee list of each event, then change auto-join to **Only when I invite** so it stops being added. If you connected Outlook to Fireflies and want to cut access completely, delete the Fireflies account and remove its permissions from your Microsoft account.

For recurring meetings, edit the whole series, not a single occurrence, or Fred will return next week.

**More on Lynkk:** [Lynkk vs Fireflies](https://lynkk.ai/compare/fireflies) and [the Lynkk meeting bot](https://lynkk.ai/features/meeting-bot).

## FAQ

### How do I permanently remove Fireflies AI from Microsoft Teams?

Delete or disconnect the Fireflies account that sends the bot, remove fred@fireflies.ai from invites, and have a Teams admin block the app in the Teams admin center under Teams apps, then Manage apps. Blocking the app alone does not always stop the bot, because it joins through calendar access.

### How do I kick Fireflies out of a meeting?

Open the participant list, click the menu next to Fireflies and choose Remove from meeting, or type /ff leave in the meeting chat. If removed within the first 3 minutes, Fireflies creates no transcript or notes. You need host or presenter rights to remove a participant in Teams.

### Why does Fireflies keep joining my Teams meetings?

Fireflies joins because an attendee connected their calendar with auto-join turned on. Ask the bot's owner to switch auto-join to Only when I invite, or remove fred@fireflies.ai from the invite. For recurring meetings, edit the whole series, not a single occurrence, or Fred will return the following week.

### Will removing Fireflies delete the transcript?

If Fireflies is removed within the first 3 minutes, no transcript or notes are created. If removed later, the owner may still get notes for the part it recorded. Ask the person who owns the bot to delete the meeting notes if attendees did not agree to the recording.

### Can I block Fireflies without admin rights?

You can remove it from meetings you organize and set your lobby so only organizers bypass it. Blocking it for the whole company requires a Teams admin. Setting the lobby this way makes the bot wait outside, where the organizer can simply deny it entry each time.

### Is Fireflies AI safe to use?

Fireflies is a legitimate product with enterprise security options, including HIPAA and SSO on its Enterprise plan. The common problem is uninvited joining through auto-join, which you can control in settings. Ask who owns the bot and where the recording goes, since several US states require all parties to consent to recording.

<!-- HANDOFF
Prompts answered: "how to remove fireflies ai from teams", "remove fireflies ai from microsoft teams permanently", "how to disable fireflies ai in teams", "remove fireflies from zoom", "why does fireflies keep joining my meetings".
Prompt gaps (create_prompt): "how to block ai note takers in teams".
Fan-out source: Ubersuggest google_suggestions (permanently, from teams meetings, from microsoft account, from outlook, how to disable, is fireflies ai safe) + SERP (Microsoft Q&A, university IT KBs, Fireflies guide), 2026-10-17.
Inbound links: from /blog/ai-note-taker-microsoft-teams and /blog/zoom-bot-join-meeting.
Editor checks: Entra ID and lobby steps are general admin guidance (not from the cited thread); menu names may differ by tenant.
-->
