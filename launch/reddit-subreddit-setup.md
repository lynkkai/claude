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
| Icon / avatar | 256 x 256 px, PNG or JPG, square | The white sphere mark (`lynkk-post-kit/kit/assets/mark.svg`) on #111111 |
| Banner image | at least 1072 x 128 px | `reddit-assets/reddit-banner-desktop.png` (2144 x 256) |
| Mobile banner image | at least 1080 x 128 px | `reddit-assets/reddit-banner-mobile.png` (2160 x 256) |
| Key color | Hex code | #111111 (the night band) |

The banners are built in the post kit: `lynkk-post-kit/posts/reddit-banner/`. Re-render with `node scripts/render.mjs posts/reddit-banner` from `lynkk-post-kit/`.

## 6. Rules (Mod Tools > Rules)

1. **Be respectful.** No harassment, hate speech, or personal attacks.
2. **Stay on topic.** Posts should relate to Lynkk, AI meeting assistants, meeting productivity, or related workflows.
3. **No spam or unrelated self-promotion.** Promoting other products, affiliate links, or repeated low-effort posts will be removed.
4. **Protect privacy.** Do not share meeting transcripts, recordings, or screenshots that include other people's personal or confidential information.
5. **Bug reports and feature requests go in the right flair.** Include how you recorded (Mac app, meeting bot, Chrome extension or web), steps to reproduce, and what you expected.
6. **Support requests about your account or billing:** email marketing@lynkk.ai instead of posting account details publicly.
7. **No misinformation about the product.** Official answers come from users with the "Lynkk Team" flair.

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

1. **Welcome to r/Lynkk: start here** (what Lynkk is, what this community is for, rules summary, how to get support)
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
