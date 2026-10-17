# Competitor hero visuals: how AI meeting assistants show "what the product does" (as of Oct 2026)

Method note: All live pages were fetched on 2026-10-17. WebFetch only returns page text, so hero visuals were checked directly where possible by downloading the hero image/video files from each site's HTML and viewing them (frames pulled from hero videos with ffmpeg). Where I could only infer a visual from file names or alt text, it is marked "inferred". web.archive.org was not reachable from this environment, so there are no archived snapshots in these notes. Lynkk is not confused with Lynk/Linnk/Link AI anywhere below. Note on punctuation: the repo rule bans em/en dashes, so citations use "(Source)" format.

## 1. Competitor-by-competitor hero catalog (headline, subhead, hero visual)

### Takeaway
Almost no 2026 homepage hero uses a literal "meeting → output" diagram. The common approaches are (a) a collage or floating cards of real UI fragments, (b) an abstract or decorative background with the copy doing the work, or (c) a single structured note card. The clearest product-explaining visuals sit on use-case pages and in the second section, not the homepage hero. Fireflies' sales hero is the one exception: a video-call tile next to a structured deal note, with a strip of integration logos.

### Cited Findings

**Otter.ai** ([otter.ai](https://otter.ai/))
- H1: "Meeting AI that turns talk into action." Subhead: "Transcription. Pre-call briefs. Live coaching. Automatic follow-ups." then "Otter transcribes every meeting, turning it into searchable knowledge that powers your workflow." CTAs: "Start for free", "Schedule demo" (Source: [otter.ai](https://otter.ai/))
- The page text also contains alternate hero headings ("Your notetaker should do more than take notes", "Meeting AI for follow-ups", "Your AI notetaker is now also your Conversational Knowledge Engine"). The demo CTA URL has `utm_content=homepagevariant`, which hints that headline variants are being tested, though this is not confirmed (Source: [otter.ai](https://otter.ai/))
- Hero visual: a square "Landing Video 1x1". Its poster frame is a soft, blurred purple/lavender gradient with no readable UI (I viewed the poster file directly). In the HTML it sits next to three customer testimonial photos and a customer logo row (Source: [otter.ai](https://otter.ai/), poster file `Otter - Landing Video 1x1-poster-00001.jpg`)
- Second section: "Before, during, and after every meeting." with six feature cards (pre-call briefings, Live-Assist coaching, automate action items, push sales insights to your CRM). The before/during/after idea is carried by the heading and cards, not by a timeline graphic (Source: [otter.ai](https://otter.ai/))

**Fireflies.ai** ([fireflies.ai](https://fireflies.ai/))
- H1: "The #1 AI Assistant For Your Meetings". Subhead: "Transcribe, summarize, search, and analyze all your team conversations." CTAs: "Get Started", "Request Demo". Trust line: "Rated 4.8 / 5", "USED ACROSS 1 MILLION+ COMPANIES" (Source: [fireflies.ai](https://fireflies.ai/))
- Hero visual (viewed directly, `hero-mobile.webp`): a single clean note card titled "Kickoff Call" with sections "Overview", "Notes" (highlighted labels "Use Case: Acme wants to buy Fireflies for 50 seats", "Requirement: Automate HubSpot dat..") and "Action items". Two action-item rows pop out of the card as floating chips with owner names and avatars ("Draft a follow up email." Sarah, checked; second row Will). The text is truncated with ".." so it looks like it is still being written (Source: [fireflies.ai](https://fireflies.ai/))
- Below the hero, summary tabs (Overview / Bullet Points / Action Items / Custom Notes), capture options including "AI Note Taker Bot", and an integrations block (CRM, PM, ATS, Slack) (Source: [fireflies.ai](https://fireflies.ai/))

**Granola** ([granola.ai](https://www.granola.ai/))
- H1: "The AI notepad for back-to-back meetings". Subhead: "Notes, actions and memory." / "Without a meeting bot." CTA: "Download for free" (macOS, Windows, iOS, Android) (Source: [granola.ai](https://www.granola.ai/))
- Main product visual: a notepad mockup "Q3 GTM sync" with "My notes" / "Enhanced" tabs and status chips "Enhancing notes", "Transcribing", "Generate notes". The enhanced view shows structured headings ("ICP Alignment Confirmation", "Next Steps"). This is a raw-notes → enhanced-notes transformation shown by tab toggle (Source: [granola.ai](https://www.granola.ai/))
- Feature image (viewed directly, `feature-humans.webp`, alt "A Granola note beside a video call with six participants, with the Granola recording indicator transcribing in the background"): left is a mostly blank note "Team Stand-up" / "Write notes" with a typing cursor; centre is a 6-person video-call grid overlapping it; right is a small floating pill with the Granola logo and a green audio-level indicator (Source: [granola.ai](https://www.granola.ai/))
- Section "Granola helps you before, during and after your meetings." has three tabs: Before ("Start your meeting prepared", "Your Brief" panel), In the meeting ("Give your full attention", raw notes being written), After ("Post-meeting admin, done", quick actions "List actions", "Write follow-up email", "Draft project plan") (Source: [granola.ai](https://www.granola.ai/))

**Fathom** ([fathom.ai](https://www.fathom.ai/))
- Banner: "FATHOM IS NOW PART OF SUPERHUMAN." H1: "AI notetaking that is out of this world". Subhead: "Fathom summarizes your meetings so you can focus on the conversation. Now available bot-free." CTA: "Get started - free forever". Trust line: "SOC 2 Type II | GDPR | HIPAA Compliant | SSO / SCIM", "Used at 300K+ companies" (Source: [fathom.ai](https://www.fathom.ai/))
- Hero visual (viewed directly, `hero (1).avif`): a dark bento/pill collage of UI fragments mixed with space illustrations (an astronaut on a laptop, a moon). Fragments: a capture-mode menu ("Audio & video", "Audio BOT-FREE", "Transcript only BOT-FREE", "Capture off") with a cursor; an "ASK FATHOM" label; a chat prompt "Fathom, what follow-ups did I commit to in my meetings this week?" with ChatGPT and Claude icons; a "Project check-in" note with attendee avatars and "Summary" / "Scratchpad" tabs (Source: [fathom.ai](https://www.fathom.ai/))
- No alt text on the hero image. CRM sync is mentioned only in prose ("Slack, Salesforce, HubSpot, Notion, Asana, and beyond") (Source: [fathom.ai](https://www.fathom.ai/))

**tl;dv** ([tldv.io](https://tldv.io/))
- H1: "The AI Notetaker built for Team Collaboration". Subhead: "tl;dv is where your team captures knowledge, finds answers, and automates meeting workflows." / "Any meeting insight, instantly sent to your favourite apps." CTAs: "Get tl;dv - Free forever", "Book a Demo". Badges: G2 4.7, "2M+users", "GDPR & SOC2", "✅NO BOT REQUIRED" (Source: [tldv.io](https://tldv.io/))
- Hero visual (from markup): an "Action Items" panel above five meeting cards, each with a thumbnail, a title, a date, and the logos of the meeting platform and destination app. Examples: "Product demo 01/15/26 (HubSpot, Zoom)", "Discovery call (Slack, Google Meet)", "Sprint Planning (Notion, Google Meet)", "Daily Standup (Zoom, Microsoft Teams)". This pairs a meeting type with its destination app, which suggests "meeting → app" without arrows (Source: [tldv.io](https://tldv.io/))
- Lower sections use video placeholders: "Never take meeting notes again...", "No more manual updates - this AI notetaker handles CRM and follow-ups too." (Source: [tldv.io](https://tldv.io/))

**Gong** ([gong.io](https://www.gong.io/))
- H1: "#1 AI OS for Revenue Teams". Subhead: "Capture every interaction, analyze what's working, and automate what happens next". CTAs: "Book a demo", "See Gong in action" (platform tour) (Source: [gong.io](https://www.gong.io/))
- Hero visual: no product screenshot is described. There is a decorative stars background and a rotating list of outcomes ("Close deals faster", "Predict pipeline risk", "Automate handoffs", "Enable at scale", "Increase win rates", "Predict churn"). Below is a formula graphic, "Efficiency × Effectiveness = Productivity". Gong sells at the category/platform level rather than showing a meeting (Source: [gong.io](https://www.gong.io/))

**Read.ai** ([read.ai](https://www.read.ai/))
- H1: "Meetings In, Decisions Out". Subhead: "Every meeting should have outcomes. Read AI turns meetings into outcomes. Summaries with context from your email and calendar, and AI agents that recommend what happens next." CTA: "Get Started for Free". Checkmarks: "5 free meetings / month", "No install required", "No credit card" (Source: [read.ai](https://www.read.ai/))
- Hero visual (viewed directly, `Website_Demo_Video_Thumbnail.jpg`): a video thumbnail with a large play button over an overhead photo of two people at a desk. Floating UI chips are joined by thin connector lines: an "Ask Search Copilot anything..." bar, a calendar card "Weekly Team Standup, Zoom • Starts at 2:30pm, [Add Read AI]", a video-call participant column (RW, Maya), a phone recording screen (5:42, filler words), a desktop dashboard "Good Afternoon, Leah 👋 / Today's Meetings / Recent Reports", a recording pill with a waveform, and a platform dock (Windows, Android, Apple, Zoom, Teams, Meet) (Source: [read.ai](https://www.read.ai/))
- The headline itself is an input→output formula. "How Read AI Works: From the invite to the follow-through" has three text-only steps: "Walk in ready" / "Capture what was said" / "Meeting ends, actions start" (Source: [read.ai](https://www.read.ai/))

**Avoma** ([avoma.com](https://www.avoma.com/))
- H1: "An all-in-won AI to automate note-taking, scheduling, coaching, forecasting, and more." (the typo "all-in-won" is on the live page). Subhead: "All-in-one doesn't mean you have to buy all at once..." CTAs: "Schedule a demo", "Start a free trial" (Source: [avoma.com](https://www.avoma.com/))
- Hero visual: four product tiles (AI Meeting Assistant, Scheduler & Lead Router, Conversation Intelligence, Revenue Intelligence), each with an outcome stat ("Save 4+ hrs/week by automating note-taking, follow-up emails, CRM updates..."). The hero is a product-suite menu, not a depiction of a meeting (Source: [avoma.com](https://www.avoma.com/))
- Lower feature images include "Automatic CRM data enrty" [sic] and "Ai Generated Follow up" (Source: [avoma.com](https://www.avoma.com/))

**Fellow** ([fellow.ai](https://fellow.ai/))
- H1: "The Secure AI Meeting Assistant". Subhead: "Built to the standards of regulated industries and organizations where privacy, security, and data governance matter most." CTAs: "Contact Sales", "Get Started". Trust: "SOC 2 Type II, GDPR & HIPAA", "Our AI is never trained on your data" (Source: [fellow.ai](https://fellow.ai/))
- Hero video (frames viewed): an abstract dark teal background of blurred vertical light bars, purely atmospheric with no UI (Source: [fellow.ai](https://fellow.ai/), asset `Jb9HIzTj3e0bOZneAtlIcENuOg.mp4`)
- Second product video (frames viewed): a recording player (thumbnail of a speaker, scrubber at "19:21 / 1:06:29", 1.5x, clip/scissors) above tabs "Agenda | AI Note | Transcript". The "Summary" text types itself out line by line, then "Topics" ("Company Milestone: $50M ARR"), then "Action items" with named owners ("Camille to build...", "Amir to consolidate security documentation...") and avatar dots. This is the animated typing-summary pattern linked to a recording (Source: [fellow.ai](https://fellow.ai/), asset `H5E8GP4QUX8yXMpZCKusHO8xe8.mp4`)
- A text-only before/after block: before list starts with "Scattered meeting tools", after list with "One governed approach to AI meeting notes" (Source: [fellow.ai](https://fellow.ai/))

**Krisp** ([krisp.ai](https://krisp.ai/))
- H1: "Voice AI for meetings". Subhead: "For teams, call centers, and developers" followed by "#1 noise cancellation, accent AI, translation, and AI note taker." (Krisp joins the two parts with a long dash, removed here per the repo's writing rule). CTA: "Get Krisp", plus three audience cards (AI Meeting Assistant / Call Center AI / Developers) (Source: [krisp.ai](https://krisp.ai/))
- Hero video (15s, frames viewed): a desktop app window with a 6-person video grid at top, a live transcript with speaker names below, an audio waveform scrubber at the bottom, and a floating "AI Note-taker (No Bot)" control panel (Transcript / Audio / Screen / Off, Noise Cancellation toggle). Rotating pill callouts appear on top of the UI: "No noise", "No accent", "Bot-free", "Voice Isolation", "Transcript-only mode", "Multilingual teams", "In-person meetings", "Free Transcription", "AI Chat". One static UI with animated labels pointing at features (Source: [krisp.ai](https://krisp.ai/), `video_hero.mp4`)
- Lower sections are tabbed Before / During / After meeting, each with a short video ("Sync to CRM", "Centralized Action items", "Agenda") (Source: [krisp.ai](https://krisp.ai/))

**Newer entrants**
- **Jamie** ([meetjamie.ai](https://www.meetjamie.ai/)): H1 "The meeting intelligence platform you can trust." Subhead "Turn every meeting into knowledge you can act on." Bullets: data stays in the EU, no bot joins, ISO 27001/GDPR. Image "A Jamie meeting running alongside a video call on a MacBook". A five-step carousel: Prepare → Capture → Document → Chat → Integrate (Source: [meetjamie.ai](https://www.meetjamie.ai/))
- **Jamie CRM automation visual** (viewed directly, `/landing/automation.avif`, alt "A Jamie workflow updating the CRM after a meeting"): three stacked status cards like an agent run log: "Checked the CRM for Kepler Capital / No record / Done"; "Lead created, 4 fields written / Owner, stage, mandate, next step / Running ⟳" (highlighted, bigger); "Attach notes / Action items, details / Up Next" (Source: [meetjamie.ai](https://www.meetjamie.ai/))
- **Bluedot** ([bluedothq.com](https://www.bluedothq.com/)): H1 "Invisible, privacy-first AI note taker". Subhead "Bluedot captures, transcribes, and summarises every meeting, online or in-person." Device mockups (mobile, web, Apple Watch) and a "Bluedot in 60 sec" video labelled "Click to try - no account required" (Source: [bluedothq.com](https://www.bluedothq.com/))
- **Fyxer** ([fyxer.com](https://www.fyxer.com/)): mainly an email assistant. H1 "Fyxer makes sure you never miss anything important", eyebrow "Managing multiple clients?", CTAs "Google" / "Microsoft". Hero graphic is a cube cluster (inferred from file name `hero-cube-cluster`) with tabs Inbox / Meetings / Priorities / Actions. "Your workday with Fyxer" is a Morning / Afternoon / End of day timeline with mock UI: a "Top priorities" list, an answer to "Which deals are waiting on me?", and a follow-up email draft "Drafted by Fyxer" with Save/Send (Source: [fyxer.com](https://www.fyxer.com/))

### Inferences
- Headlines split into two types. Some are category/superlative ("#1 AI Assistant For Your Meetings", "#1 AI OS for Revenue Teams"). Others describe a transformation ("Meetings In, Decisions Out", "Meeting AI that turns talk into action", "Turn every meeting into knowledge you can act on"). The transformation headlines tell visitors what happens without needing a visual.
- The heroes with the most product information (Fireflies, Krisp, Read.ai, Fathom) all show real-looking UI fragments. The heroes with the least (Otter poster, Fellow, Gong, Fyxer) use abstract art and rely on copy.
- No competitor homepage hero shows a voice assistant speaking in a meeting. Lynkk's "speaks when needed" capability has no visual precedent among these heroes, so it is an open space but will need extra explanation.

### Gaps
- Otter's hero video content could not be confirmed (only the blurred poster was retrievable). Granola's top-of-page hero animation (if any) was not visible in the HTML. Gong's "Revenue AI OS" image was not viewed.
- No archived (pre-2026) snapshots, because web.archive.org was blocked. Changes over time could not be documented.

## 2. Before/after, timelines, meeting → output flows, timestamps, and how integrations are shown

### Takeaway
"Before, during, after" is now a common way to structure pages (Otter, Granola, Krisp, Read.ai, Jamie, Fyxer), but every site uses it as tabs, headings or a carousel, not as a single timeline graphic. Literal before/after comparisons are rare and text-only (Fellow). Integrations are shown as logo strips or grids, or, most clearly, as agent-style status cards showing specific CRM fields being written (Jamie). Linking summary items to recording timestamps appears only indirectly (Fellow's player scrubber above the AI note).

### Cited Findings
- Otter: "Before, during, and after every meeting." heading followed by feature cards. No before/after or flow diagram is present (Source: [otter.ai](https://otter.ai/))
- Granola: three tabs, Before / In the meeting / After, each with its own mockup (Source: [granola.ai](https://www.granola.ai/))
- Krisp: Before / During / After meeting tabs with short feature videos. The only real before/after comparisons are audio toggles ("With Krisp Noise Cancellation", "With Krisp AI Accent Conversion") (Source: [krisp.ai](https://krisp.ai/))
- Read.ai: "From the invite to the follow-through" as three text steps: "Walk in ready", "Capture what was said", "Meeting ends, actions start" (action items routed to tools "with citations") (Source: [read.ai](https://www.read.ai/))
- Jamie: Prepare → Capture → Document → Chat → Integrate carousel. The CRM workflow is shown as Done / Running / Up Next cards that name the fields written ("Owner, stage, mandate, next step") (Source: [meetjamie.ai](https://www.meetjamie.ai/))
- Fyxer: a time-of-day timeline ("Morning, Afternoon, End of day") with one mock UI output per step (Source: [fyxer.com](https://www.fyxer.com/))
- Fellow: the only explicit before/after, as two text lists ("Scattered meeting tools" vs "One governed approach to AI meeting notes"). Its product video puts a recording scrubber (19:21 / 1:06:29) directly above the AI note with Summary / Topics / Action items with owners (Source: [fellow.ai](https://fellow.ai/))
- Fireflies homepage hero: action items "break out" of the note card as floating chips with owner names (Sarah, Will), which visually says "tasks get assigned". The sales hero adds a scrolling strip of integration logos (HubSpot, Salesforce, monday.com, Intercom, Dynamics and others) along the bottom of the note (Source: [fireflies.ai](https://fireflies.ai/), [fireflies.ai/sales](https://fireflies.ai/sales))
- tl;dv: each meeting card carries the logo of its destination app (HubSpot, Slack, Notion) next to the meeting platform logo (Source: [tldv.io](https://tldv.io/))
- Read.ai's hero uses thin connector lines between floating UI chips (calendar invite, call, phone recorder, dashboard). This is the closest thing to "arrows" in any hero (Source: [read.ai](https://www.read.ai/))
- Logo grids for integrations: Otter ("Connect to your favorite apps": Zoom, Claude, HubSpot, Jira, Salesforce, Slack, Asana, etc.), Read.ai (Meet, Zoom, Teams, Salesforce, HubSpot, Jira, Confluence...), Fellow (Salesforce, HubSpot, Notion, Zoom, Zendesk...), Granola (MCP connector logos: OpenAI, Claude, Cursor...) (Source: [otter.ai](https://otter.ai/), [read.ai](https://www.read.ai/), [fellow.ai](https://fellow.ai/), [granola.ai](https://www.granola.ai/))
- Jira updates are only mentioned as logos or in prose (Otter, Read.ai integration grids; Fellow prose "pushes action items to Jira"). No competitor visual shows a Jira ticket being created (Source: [otter.ai](https://otter.ai/), [read.ai](https://www.read.ai/), [fellow.ai](https://fellow.ai/))

### Inferences
- Most competitors split before/during/after across tabs or a carousel, so a visitor only sees one moment at a time. Lynkk's current concept (a timeline with three moments plus arrows into a note) is more ambitious and probably denser than anything in this set. That may explain why visitors take a while to understand it.
- The most legible "integration got updated" device found is Jamie's status-card stack. It names the object (lead), the fields (owner, stage, next step), and a state (Done / Running / Up next). It reads like a receipt, not a logo cloud. A "Jira ticket created PROJ-123" / "HubSpot: stage → Proposal" card would fit Lynkk's "within ~30 seconds" claim.
- Fireflies' owner-labelled action-item chips are a simple way to show "action items with owners" without drawing arrows.

### Gaps
- No competitor visual found that links individual summary bullets to clickable timestamps in the recording (some products have this in-app, but it is not used as a marketing device on these pages).
- No competitor shows a "messy notepad vs. structured note" before/after image. Granola's "My notes / Enhanced" toggle is the closest analogue.

## 3. Use-case pages (sales, recruiting, standups, etc.)

### Takeaway
Use-case pages reuse the homepage's structure with role-specific copy. The strongest one checked (Fireflies Sales) has a hero that shows the call and the resulting note side by side, with integration logos. Otter's sales page is organized by meeting stage (pre-call, live, post-call). Several competitors' guessed use-case URLs 404.

### Cited Findings
- Fireflies Sales: H1 "Spend Your Day Closing Deals". Hero image (viewed directly, `Sales-Hero-Desktop.png`) is split in two. On the left is a webcam tile of a smiling rep in a headset labelled "Acme <> Craig" with a small recording-waveform badge. On the right is a note "Acme <> Fireflies / Krish, +9 / Mar 15, 11:30 AM / Channel" with sales-specific sections "Deal Status & Timeline" (e.g. "Procurement review is expected next week, Thursday.") and "Pain Points". A horizontal strip of CRM/tool logos overlaps the bottom of the note. Lower sections: "CRM and scorecard autofill" (BANT, MEDDIC, SPICED), "18+ Sales Templates", "Plugs Into the Tools Your Sales Team Already Uses" (Source: [fireflies.ai/sales](https://fireflies.ai/sales))
- Otter Sales Agent: H1 "Turn sales calls into closed deals". Sections ordered by stage: "Pre-call prep" (meeting briefs, talking points), "Live meeting transcription & coaching" (text only), "Post-call summarization" (smart summaries, follow-up emails, CRM syncing). Screenshot images have empty alt text (Source: [otter.ai/sales-agent](https://otter.ai/sales-agent))
- Otter homepage use-case tiles each have a short looping video: "AI Sales Agent", "AI Education Agent", "AI Media Agent", "AI Recruiting Agent", "SDR agent" (Source: [otter.ai](https://otter.ai/), video file names in HTML)
- Fathom homepage role cards (Sales, Customer Success, Marketing, Operations, HR & Talent, Product & Engineering) use illustrations and short descriptions. Bluedot uses persona tabs (Entrepreneurs, Recruiters, Sales, Managers, Engineers, Customer Success) with testimonials. tl;dv uses role-specific AI prompt examples ("Which product bugs were mentioned in our Sales call this week?") (Source: [fathom.ai](https://www.fathom.ai/), [bluedothq.com](https://www.bluedothq.com/), [tldv.io](https://tldv.io/))
- Granola shows a standup as the default scenario ("Team Stand-up" note beside a 6-person call, and "A macOS notification for a team stand up with a Granola button to join and take notes"). Fellow's AI-note video uses a leadership/ops update. tl;dv's hero lists "Daily Standup", "Sprint Planning", "Engineering Sync" (Source: [granola.ai](https://www.granola.ai/), [fellow.ai](https://fellow.ai/), [tldv.io](https://tldv.io/))
- URLs returned 404 on 2026-10-17: fathom.ai/use-cases/sales, tldv.io/sales/, avoma.com/use-cases/recruiting, read.ai/sales, granola.ai/sales (Source: direct fetch attempts)

### Inferences
- Effective use-case heroes change the content inside the note (sales: "Deal Status & Timeline", "Pain Points"; standup: owners and blockers) and keep the same layout. Visitors recognize their own meeting type from the section headings in the note.
- Legal and recruiting-specific hero visuals were not found among these competitors. Lynkk could own those with domain-specific note headings (e.g. "Candidate scorecard", "Matter: obligations & deadlines").

### Gaps
- Legal, recruiting and standup use-case pages for Fathom, tl;dv, Avoma, Read.ai and Granola were not found at guessed URLs. Their actual use-case URLs were not discovered within the tool budget.

## 4. Recurring visual devices and which seem clearest

### Takeaway
The recurring devices are: (1) a note or summary card with structured headings and owner-tagged action items; (2) a video-call grid or webcam tile next to or under the note; (3) a small floating "recording/bot-free" pill or control panel; (4) rows or strips of meeting-platform and CRM logos; (5) labelled callout pills over a product UI; (6) an animated typing summary. The clearest single frames found are Fireflies' sales hero (call tile + structured note + logo strip) and Jamie's CRM status cards. The least clear are abstract or illustrative heroes (Otter poster, Fellow, Gong, Fyxer cubes, Fathom's astronaut collage).

### Cited Findings
- Structured note card with headings and action items: Fireflies home ("Overview / Notes / Action items" with owner chips), Fireflies sales ("Deal Status & Timeline / Pain Points"), Fellow ("Summary / Topics / Action items" with owners), Granola ("Enhanced" note with "Next Steps"), Fathom ("Project check-in", Summary tab) (Source: [fireflies.ai](https://fireflies.ai/), [fireflies.ai/sales](https://fireflies.ai/sales), [fellow.ai](https://fellow.ai/), [granola.ai](https://www.granola.ai/), [fathom.ai](https://www.fathom.ai/))
- Video grid or webcam tile next to notes: Granola (6-person grid over note), Krisp (6-person grid above transcript), Fireflies sales (webcam tile left of note), Read.ai (participant column), Jamie ("meeting running alongside a video call") (Source: [granola.ai](https://www.granola.ai/), [krisp.ai](https://krisp.ai/), [fireflies.ai/sales](https://fireflies.ai/sales), [read.ai](https://www.read.ai/), [meetjamie.ai](https://www.meetjamie.ai/))
- A bot-in-meeting participant tile ("X Notetaker" as a meeting participant) was not seen in any hero. Instead, the trend is the reverse: "bot-free" is a hero claim for Granola ("Without a meeting bot."), Fathom ("Now available bot-free", BOT-FREE tags in the hero), tl;dv ("NO BOT REQUIRED"), Krisp ("Bot-free", "AI Note-taker (No Bot)"), Jamie ("no bot joins the call"), Bluedot ("Invisible", "doesn't join your meetings") (Source: [granola.ai](https://www.granola.ai/), [fathom.ai](https://www.fathom.ai/), [tldv.io](https://tldv.io/), [krisp.ai](https://krisp.ai/), [meetjamie.ai](https://www.meetjamie.ai/), [bluedothq.com](https://www.bluedothq.com/))
- Floating recording indicator: Granola's pill with logo + green audio bars; Read.ai's waveform pill; Krisp's waveform scrubber (Source: [granola.ai](https://www.granola.ai/), [read.ai](https://www.read.ai/), [krisp.ai](https://krisp.ai/))
- Meeting platform logos (Zoom/Meet/Teams): Granola ("Works with Zoom, Google Meet, Teams and every other meeting app."), Read.ai platform dock in hero, Fathom "Works wherever you do" tiles, Fyxer app icons (Source: [granola.ai](https://www.granola.ai/), [read.ai](https://www.read.ai/), [fathom.ai](https://www.fathom.ai/), [fyxer.com](https://www.fyxer.com/))
- Animated typing summary: Fellow's product video types Summary → Topics → Action items. Fireflies' hero copy is truncated ("bet..", "dat..") to suggest writing in progress (Source: [fellow.ai](https://fellow.ai/), [fireflies.ai](https://fireflies.ai/))
- Callout pills over UI: Krisp's rotating labels ("Bot-free", "No noise", "Multilingual teams", "In-person meetings") (Source: [krisp.ai](https://krisp.ai/))
- Ask-your-meetings chat prompt: Fathom ("what follow-ups did I commit to in my meetings this week?"), Granola ("What did I promise to do in my meetings this week?"), Read.ai ("Ask Search Copilot anything..."), Fyxer ("Which deals are waiting on me?") (Source: [fathom.ai](https://www.fathom.ai/), [granola.ai](https://www.granola.ai/), [read.ai](https://www.read.ai/), [fyxer.com](https://www.fyxer.com/))

### Inferences
- Clarity ranking from my visual review (judgement, not test data): Fireflies Sales hero > Jamie CRM cards > Fireflies home note card > Fellow typing-note video > Granola note + call > Krisp labelled UI > Read.ai collage > Fathom collage > Avoma tiles > Otter/Fellow/Gong/Fyxer abstract heroes. The top ones show one meeting and one output, with readable, concrete content (names, dates, deal facts, field names) and almost no chrome.
- Fathom and Read.ai show 5+ UI fragments at once. They show a lot of features but do not tell one story, and it is hard to tell what to look at first.
- Because "bot-free" is now everywhere, a Lynkk visual that shows Lynkk *in* the call (speaking) stands out from these competitors. But a bot tile could read as "another intrusive bot" to visitors who have absorbed the bot-free framing. One mitigation is to make the in-call moment show a useful answer (a voice reply bubble with the answer text), not just a participant tile.
- Concrete specificity seems to matter more than motion. The clearest static frames (Fireflies, Jamie) are not animated.

### Gaps
- No eye-tracking or comprehension data on any of these specific visuals was found.

## 5. Public data on what worked (A/B tests, teardowns, founder posts)

### Takeaway
I found no published A/B tests, Wynter tests, or Growth.Design teardowns of these competitors' hero sections. The available evidence is indirect: Granola's brand-driven growth, Granola's product-level finding that live AI output distracts users, signs of headline testing on Otter, and generic hero image-vs-video test data.

### Cited Findings
- Granola rebrand (Ragged Edge, handwriting-based identity): the identity trended on X on launch day, Granola had its highest-ever daily downloads, it became the world's second-fastest-growing software brand per Ramp the following month, and raised $125m at a $1.5bn valuation within three months. Founding marketer Jack Cully framed it as "progress over process". Article dated 14 July 2026 (Source: [Creative Boom](https://www.creativeboom.com/news/ragged-edge-rebrands-ai-notepad-granola-with-a-co-founders-handwriting-and-a-deliberately-imperfect-logo/)). Note: this is about brand identity, not specifically the hero graphic.
- Granola job listing says the company aims to make its website "one of the best product marketing experiences on the internet" (Source: [Granola jobs](https://www.granola.ai/jobs/design-engineer-web-brand), via search snippet, not fetched)
- Sacra: Granola's "initial real-time note expansion feature distracted beta testers". "Even useful live AI output pulled people away from the conversation", so it removed live output and made post-meeting enhancement the core job. Sacra cites its own Granola reports dated 2025-10-02 and 2025-04-24 (Source: [Sacra](https://sacra.com/chat/h/bb316bee-0809-4c7d-a859-4095ed2142a1/)). This is relevant to Lynkk's "speaks when needed" message: the visual must show the in-call moment as low-distraction and on-demand.
- Otter's demo link carries `utm_content=homepagevariant`, and the page holds several alternate hero headings. This suggests Otter tests homepage variants, but no results are public (Source: [otter.ai](https://otter.ai/))
- Generic hero media test data: VWO case study in which a static image outperformed a 2-minute video on a Brookdale Living page, run by the agency "Fathom" (a different company from Fathom.ai, do not conflate) (Source: [VWO](https://vwo.com/blog/image-outperforms-video-increases-monthly-revenue/)). MetricTheory reported that a video hero slightly increased bounce but improved conversion on its own site (Source: [MetricTheory](https://metrictheory.com/blog/how-a-performance-marketing-agency-tests-our-own-website/)). Mida dataset claim: hero image tests win about 18% of the time on homepages (Source: [Mida](https://www.mida.so/change-types/hero-image/homepages)). All are directional and none are from meeting-assistant companies.
- A generic teardown heuristic: test whether a stranger can state what the product does in one sentence after seeing the hero (Source: [The Hoodie Marketer](https://thehoodiemarketer.com/blog/landing-page-teardown-template/))
- A Step1 gallery entry for Amie's AI note-taker page describes a left-aligned hero with a centered glass-effect product screenshot (Source: [Step1](https://step1.dev/gallery/Eyn0FmByV-wg_5ar5dlQl), from search snippet, not verified)

### Inferences
- With no category-specific test data, Lynkk will need to run its own test. A 5-second test ("what does this product do?") is a cheap way to compare the current timeline graphic with a simpler "call tile + structured note + integration receipts" frame.
- Granola's experience suggests the during-meeting moment should look calm and optional (e.g., the user asks and Lynkk answers once), not like a constant stream of AI output.

### Gaps
- No Growth.Design, Wynter, or landing-page-teardown article specific to Otter, Fireflies, Granola, Fathom, tl;dv, Gong, Read.ai, Avoma, Fellow, Krisp or Jamie was found.
- No founder/LinkedIn/X posts about hero redesigns were found for these companies within the search budget.
- Product Hunt launch pages were not reviewed in depth (Granola 2.0 launch page exists: [Product Hunt](https://www.producthunt.com/products/granola/launches/granola-2-0)).
