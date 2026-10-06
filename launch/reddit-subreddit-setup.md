# r/Lynkk: Subreddit Setup Copy

Everything to paste into Reddit's "Create a community" flow, plus what to set up right after.

## 1. Community name (permanent, cannot be changed later)

Reddit rules: 3-21 characters, letters, numbers and underscores only, no spaces.
The capitalization you type is how it displays forever.

| Option | Notes |
|---|---|
| **r/Lynkk** (recommended) | Shortest, matches the brand exactly |
| r/LynkkAI | Fallback if r/Lynkk is taken; matches the domain |
| r/Lynkk_ai | Second fallback |

Tip: also reserve the fallbacks (create them as private) so nobody squats on them.

## 2. Description (shown under the name, max 500 characters)

> The official community for Lynkk (lynkk.ai), the AI meeting assistant. Lynkk records your meetings, writes the notes, pulls out the tasks, and lets you ask questions across everything you've recorded. Share tips and workflows, ask questions, request features, and hear product updates from the Lynkk team.

(about 300 characters. Every claim is from `lynkk-post-kit/docs/TRUTHS.md`.)

## 3. Topics (pick up to 3)

Choose the closest matches Reddit offers, in this order of priority:

1. Artificial Intelligence / Machine Learning
2. Productivity (or Software / Apps)
3. Business / Startups

## 4. Community type

| Setting | Choice | Why |
|---|---|---|
| Type | **Public** | Anyone can view and post, best for discovery and SEO |
| Mature (18+) | **Off** | Brand and product content |

Optional: start as **Restricted** for the first 1-2 weeks so only approved users can post while you seed it with content, then switch to Public.

## 5. Visual assets

| Asset | Spec | What to use |
|---|---|---|
| Icon / avatar | 256 x 256 px, PNG or JPG, square | `reddit-assets/reddit-icon.png` (512 x 512, white sphere on #111111, safe for the circle crop) |
| Banner image | at least 1072 x 128 px | `reddit-assets/reddit-banner-desktop.png` (2144 x 256) |
| Mobile banner image | at least 1080 x 128 px | `reddit-assets/reddit-banner-mobile.png` (2160 x 256) |
| Key color | Hex code | #111111 (the night band) |

The banners are built in the post kit: `lynkk-post-kit/posts/reddit-banner/`. Re-render with `node scripts/render.mjs posts/reddit-banner` from `lynkk-post-kit/`.

## 6. Rules (Mod Tools > Rules and Removal Reasons > Rules)

Reddit allows up to 15 rules. Each one has a name (max 100 characters), a description (max 500), what it applies to, and a report reason (max 100) that users pick when they report. Enter them in this order: the first rules are the ones people see first.

### Rule 1: Be respectful. No abuse or harassment

- **Description:** Treat everyone here like a colleague. No personal attacks, insults, slurs, threats, hate speech, or harassment of any kind, including in DMs that start from this subreddit. Criticism of Lynkk is welcome; attacking people is not. Do not brigade other communities or call people out by username.
- **Applies to:** Posts and comments
- **Report reason:** Abuse, harassment or hate

### Rule 2: No adult or NSFW content

- **Description:** Keep everything safe for work. No sexual content, nudity, graphic violence, or gore in posts, comments, images, usernames in screenshots, or links. This is a work tool community; assume people are reading it at their desk.
- **Applies to:** Posts and comments
- **Report reason:** Adult or NSFW content

### Rule 3: Soft self-promotion is OK. Spam is not

- **Description:** You can share your own blog post, template, video, or workflow if it is about meetings, notes, or productivity and is useful without clicking the link. Say that it is yours. Limit: one promotional post per week, and take part in the discussion. Removed: link drops, affiliate or referral links, repeated posts, asking people to DM you, and bulk AI-generated content.
- **Applies to:** Posts and comments
- **Report reason:** Spam or excessive self-promotion

### Rule 4: Stay on topic

- **Description:** Posts should relate to Lynkk, meeting notes and transcription, running better meetings, or workflows around them (tasks, Jira, calendars, dictation). General AI news or unrelated tools belong in other subreddits. Search before posting so the same question stays in one thread.
- **Applies to:** Posts only
- **Report reason:** Off topic or duplicate

### Rule 5: Protect other people's privacy

- **Description:** Do not post transcripts, recordings, notes, or screenshots that show other people's names, faces, emails, or confidential business details. Blur or crop them first. No doxxing and no sharing someone's personal information, even if it appeared in a meeting.
- **Applies to:** Posts and comments
- **Report reason:** Shares private or confidential information

### Rule 6: Record with consent

- **Description:** Follow the recording laws where you and the other participants are. Let people know when a meeting is being recorded. Posts asking how to record someone secretly or get around consent will be removed.
- **Applies to:** Posts and comments
- **Report reason:** Asks how to record people without consent

### Rule 7: Be honest. No fake reviews or false claims

- **Description:** Share real experiences. No fake reviews, invented features, or made up comparisons. If you work for Lynkk or for another meeting tool, say so. Lynkk staff use the "Lynkk Team" flair, and official answers come from them.
- **Applies to:** Posts and comments
- **Report reason:** Misleading, fake or undisclosed

### Rule 8: No scams or impersonation

- **Description:** Do not pretend to be Lynkk staff or a moderator. No phishing links, fake giveaways, or selling or sharing accounts. The Lynkk team will never ask for your password or payment details in a DM. Report anyone who does.
- **Applies to:** Posts and comments
- **Report reason:** Scam, phishing or impersonation

### Rule 9: Keep account and billing issues private

- **Description:** Do not post your email address, invoices, or account details here. For account or billing help, email marketing@lynkk.ai and the team will reply there.
- **Applies to:** Posts and comments
- **Report reason:** Posts personal account or billing details

### Rule 10: Use the right flair

- **Description:** Pick the flair that matches your post. Bug reports should say how you recorded (Mac app, meeting bot, Chrome extension, or web), the steps to reproduce, and what you expected to happen. Feature requests go in the pinned megathread when one is open.
- **Applies to:** Posts only
- **Report reason:** Wrong flair or missing bug details

**How moderators enforce them:** first time, remove the post and send the matching removal reason. Second time, a 7 day ban. Abuse, adult content, scams, and doxxing (rules 1, 2, 5 and 8) can mean a permanent ban on the first offense.

## 7. Post flairs

- Announcement (mods only)
- Product Update (mods only)
- Question
- Feature Request
- Bug Report
- Tips & Workflows
- Integrations (Jira / Google Calendar / Slack)
- Feedback
- Discussion

## 8. User flairs

- **Lynkk Team** (mod-assigned only, for every employee who posts, for transparency)
- Early Adopter
- Sales
- Product / Engineering
- Founder
- Consultant

## 9. Sidebar ("About" and widgets)

**About / Community info:**

> Lynkk records your meetings, writes the notes, pulls out the tasks, and lets you ask questions across everything you've recorded.
>
> **Before:** with Google Calendar connected, a morning email on meeting days: who you're meeting, your last note with them, and the action items still open between you.
> **During:** record from the Mac app (no bot joins the call), the meeting bot (Google Meet, Zoom, Teams), the Chrome extension, or the web, including in-person meetings.
> **After:** a transcript in 17 languages (four in beta) and a Meeting Brief with takeaways, action items, decisions and open questions. Send action items to Jira from the note, one issue each.
>
> **Ask Lynkk (Pro):** ask questions across your own notes and get answers with citations.
> Lynkk never trains on your conversations.

**Links widget:**

- Website: https://lynkk.ai/
- Start free: https://lynkk.ai/
- Contact: marketing@lynkk.ai
- (Add LinkedIn, X, Product Hunt and YouTube once confirmed)

## 10. Welcome message (Mod Tools > Welcome message, sent to new members)

> Welcome to r/Lynkk! 👋
>
> This is the place to get the most out of your AI meeting assistant. Introduce yourself in the pinned thread, share how you use Lynkk, and tell us what you want next. The Lynkk team reads everything here.
>
> New to Lynkk? Start free at https://lynkk.ai

## 11. First posts to pin (seed content before inviting people)

1. **Welcome to r/Lynkk: start here** (written: `reddit-posts/01-welcome.md`; it includes the say-hello prompt, so a separate intro thread is optional)
2. **Introduce yourself:** what's your role and how many meetings do you have a week?
3. **Feature request megathread** (upvote ideas so the team sees priorities)

Good follow-up posts: a short demo video, "Recording a call on the Mac without a bot", "Sending stand-up action items to Jira from the note", and a monthly product update.

## 12. Moderator checklist

- [ ] Add at least 2 moderators from the team (avoid a single point of failure)
- [ ] Set every team member's user flair to "Lynkk Team"
- [ ] Turn on Crowd Control and the spam filter at a moderate level
- [ ] Add removal reasons that match the rules above
- [ ] Link the subreddit from lynkk.ai (footer) and social profiles
- [ ] Before posting the subreddit in other communities, check each one's self-promotion rules
