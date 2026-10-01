"""Build posts/blog-banners/post.html: one wide banner per blog article.

Usage (from lynkk-post-kit/): python3 posts/blog-banners/build.py
Then render: CHROMIUM_PATH=... node scripts/render.mjs posts/blog-banners
Every claim must come from docs/TRUTHS.md.
"""
G, H, U = "Lynkk guide · 2026", "How-to guide", "Use case"
CHECK = '<i data-icon="check"></i>'


def chip(c):
    return '<span class="m-chip">' + c + '</span>' if c else ''


def rows(*r):
    return "".join('<div class="m-row"><span class="m-k">%s</span>%s</div>' % kv for kv in r)


def times(*r):
    return "".join('<div class="m-row"><span class="m-t">%s</span>%s</div>' % kv for kv in r)


def opts(*r):
    return "".join('<div class="m-option"><span class="m-check%s">%s</span><span>%s</span>%s</div>'
                   % (" on" if on else "", CHECK if on else "", t, chip(c)) for t, c, on in r)


def radios(*r):
    return "".join('<div class="m-option"><span class="m-radio%s"></span><span>%s</span>%s</div>'
                   % (" on" if on else "", t, chip(c)) for t, c, on in r)


def fine(t): return '<div class="m-fine">' + t + '</div>'
def live(t): return '<div class="m-live"><span class="gr-live-dot"></span><span class="m-t">' + t + '</span></div>'
def lvl(n, v): return '<div class="m-level" style="--v: %d%%"><span>%s</span><i></i></div>' % (v, n)
def quote(t): return '<div class="m-quote">' + t + '</div>'
def cite(t): return '<div class="m-cite">' + t + '</div>'


# slug, eyebrow, headline, second-ink turn, lead, plate, glass title, glass body
BANNERS = [
    ("best-ai-note-takers", G, "The best AI note takers.", "Compared for online and in-person meetings.",
     "What each one does before, during and after the call.", "dusk", "Meeting Brief",
     rows(("Decided", "Beta on the 21st"), ("Task", "Sam, release notes by Friday"), ("Open", "EU pricing"))),
    ("best-free-ai-note-takers", G, "The best free AI note takers.", "What each free plan includes.",
     "Limits, platforms and what you get before you pay.", "meadow", "Free plan",
     opts(("Recording and transcription", "", 1), ("Meeting Brief", "", 1), ("Tasks and Jira send", "", 1)) + fine("Start free at lynkk.ai.")),
    ("zoom-meeting-recorders", G, "Top Zoom meeting recorders.", "From free recording to AI notes.",
     "Local, cloud and AI recording, side by side.", "night", "Zoom call detected",
     quote("Record this call?") + '<div class="m-row"><span class="m-btn">Record</span><span class="m-k">Not now</span></div>' + fine("No bot joins the call.")),
    ("ai-note-taker-microsoft-teams", G, "AI note takers for Microsoft Teams.", "Compared for US businesses.",
     "Built-in options and add-on tools, before you buy.", "sky", "Meeting bot",
     opts(("Paste a Teams link", "", 1), ("Calendar auto-join", "On", 1)) + fine("Free, audio only. Video recording is Pro.")),
    ("transcribe-audio-to-text", H, "How to transcribe audio to text.", "With the top voice recognition tools.",
     "Steps, free options and how to get a cleaner transcript.", "field", "Transcript",
     rows(("You", "Let's ship the beta on the 21st."), ("Priya", "I'll update the pricing page."), ("Sam", "Release notes by Friday."))),
    ("ai-voice-recorders", G, "AI voice recorders compared.", "Devices, apps and what fits a meeting.",
     "When a recorder you carry beats an app, and when it doesn't.", "night", "Recording",
     live("12:04") + lvl("You", 62) + lvl("Others", 38) + quote('"Ship the beta on the 21st."')),
    ("ai-transcription-software", G, "The best AI transcription software.", "Compared for meetings and interviews.",
     "Speaker labels, languages and what happens after the transcript.", "sky", "Transcription",
     rows(("Languages", "17, four in beta"), ("Speakers", "Labeled in every note"), ("Custom words", "Pro"))),
    ("voice-to-text-apps", G, "Voice to text apps compared.", "For Mac, Windows and Word.",
     "Built-in dictation, paid software and an app that does both.", "dusk", "Dictation",
     quote("Send the deck to Priya by Friday.") + fine("Hold fn, talk, let go.")),
    ("ai-powered-meeting-assistants", G, "AI meeting assistants compared.", "Before, during and after the call.",
     "Which tools help at each stage of a meeting.", "sky", "Your day",
     times(("10:00", "Acme renewal"), ("13:30", "Design review"), ("16:00", "1:1 with Sam")) + fine("2 open action items with Sam.")),
    ("zoom-ai-companion-alternatives", G, "Alternatives to Zoom's built-in AI.", "Compared on what happens after the call.",
     "What changes when your notes leave the call with you.", "dusk", "Meeting Brief",
     rows(("Decided", "Beta on the 21st"), ("Task", "Sam, release notes"), ("Open", "EU pricing"))),
    ("how-to-transcribe-zoom-meetings", H, "How to transcribe Zoom meetings.", "On any Zoom plan.",
     "Zoom's own transcript, and a way that works without it.", "field", "Meeting bot",
     opts(("Paste a Zoom link", "", 1), ("Live transcript panel", "On", 1)) + fine("Free, audio only. Video recording is Pro.")),
    ("dictation-on-mac", H, "Dictation on Mac, step by step.", "And what to do when it stops.",
     "Turn it on, use the shortcut, fix the common problems.", "night", "Dictation",
     rows(("Hold", "fn, anywhere on your Mac"), ("Talk", "Words land at your cursor"), ("Let go", "Done")) + fine("Never listens in a password field.")),
    ("dictate-in-microsoft-word", H, "How to dictate in Microsoft Word.", "And when you need dictation software.",
     "Word's Dictate button, voice commands and the fixes that work.", "meadow", "Dictation mode",
     radios(("Instant", "On your Mac, free", 1), ("Accurate", "Pro", 0), ("Polished", "Pro", 0)) + fine("Only Polished removes ums and false starts.")),
    ("voice-memo-transcription", H, "How voice memo transcription works.", "And how to turn memos into notes.",
     "Transcripts, fixes and a faster way to get notes from a conversation.", "field", "In person",
     live("08:12") + lvl("You", 58) + fine("Record your mic in the browser at lynkk.ai.")),
    ("google-meet-transcript", H, "How to get a Google Meet transcript.", "And when AI notes do more.",
     "Where transcripts are saved, which plans include them and how to fix gaps.", "sky", "Chrome extension",
     live("Recording") + lvl("Tab", 54) + lvl("You", 40) + fine("No bot joins the call.")),
    ("sales-conversation-intelligence", U, "Conversation intelligence for sales.", "From call prep to follow-up.",
     "What reps need before, during and after a call.", "dusk", "Ask Lynkk · Pro",
     quote("Acme asked for EU pricing on the last call.") + cite("Acme renewal · Play from 12:04")),
    ("recruiting-interview-transcription", U, "Interview transcription for recruiters.", "Better debriefs, built on the transcript.",
     "A transcript example, a debrief template and a simple workflow.", "meadow", "Transcript",
     rows(("You", "Tell me about a plan that changed."), ("Candidate", "We cut one feature and kept the date."))),
    ("meeting-minutes-to-jira", U, "From meeting minutes to Jira.", "One issue per action item, when you say so.",
     "Minutes that turn into work for product teams.", "ember", "Send to Jira",
     opts(("Release notes", "Sam · Fri", 1), ("EU pricing page", "Priya · Mon", 1), ("Book the follow-up", "You", 0))),
    ("founders-meeting-notes", U, "Back-to-back meetings, handled.", "Meeting notes for founders.",
     "Context before each call and tasks after it.", "sky", "Morning briefing",
     times(("09:00", "Investor update"), ("10:30", "Acme renewal"), ("13:00", "Hiring, round 2")) + fine("3 open action items across today.")),
    ("meeting-knowledge-management", U, "Your meetings are your knowledge base.", "Ask across every note.",
     "Knowledge management tools, and where meetings fit in.", "dusk", "Ask Lynkk · Pro",
     quote("Why did we move export to Q2?") + quote("Search filters shipped first, agreed in planning.") + cite("Planning · Play from 12:04")),
    ("daily-standup-meeting", U, "Faster daily standups.", "Blockers written down, with owners.",
     "An agenda, a template and notes that write themselves.", "field", "Daily Stand-up",
     rows(("Done", "Filter API merged"), ("Today", "Filter UI, Sam"), ("Blocker", "Staging is down, Lee"))),
    ("one-on-one-meeting", U, "Better one-on-one meetings.", "Questions, a template and AI notes.",
     "An agenda that puts the employee's topics first.", "meadow", "1:1 with Sam",
     opts(("Book the security review", "You · Thu", 0), ("Draft review slides", "Sam · Mon", 0), ("Agenda shared", "", 1))),
    ("legal-transcription-service", U, "AI or a legal transcription service.", "When each one is the right call.",
     "Client meetings, case notes and the records that need a reporter.", "night", "Who can see this note",
     radios(("Admins can see this note", "Default", 0), ("Personal", "Only you", 1)) + fine("Recordings stay with the owner.")),
    ("medical-transcription-software", U, "Medical transcription software.", "Plus AI notes for care teams.",
     "Dictation for the record, AI notes for the team.", "meadow", "Care team huddle",
     rows(("Decided", "New intake form from Monday"), ("Task", "Priya, update the checklist"), ("Open", "Weekend cover"))),
    ("meeting-minutes-sample", U, "Meeting minutes samples.", "For teams and boards.",
     "Two formats to copy, and a faster first draft.", "ember", "Board Meeting",
     rows(("Motion", "Approve the budget, carried"), ("Motion", "Second van, tabled"), ("Task", "Treasurer, file by May 30"))),
]

SECTION = """
<!-- {slug} -->
<section class="post" id="{slug}" data-size="wide" data-next="Read the guide">
  <main class="post-body">
    <div class="split">
      <div>
        <span class="eyebrow">{eb}</span>
        <h1 class="t-h2">{h1} <span class="ink-2">{h2}</span></h1>
        <p class="t-lead mt-m">{lead}</p>
      </div>
      <div class="plate plate-{plate} scene" data-rings>
        <div class="glass" data-size="l">
          <div class="glass-title">{gt}</div>
          <div class="glass-body">{body}</div>
        </div>
      </div>
    </div>
  </main>
</section>
"""

head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Blog banners · Lynkk post</title>
<link rel="stylesheet" href="../../kit/post.css" />
<style></style>
</head>
<body>
"""
out = head + "".join(SECTION.format(slug=s, eb=e, h1=a, h2=b, lead=l, plate=p, gt=g, body=y)
                     for s, e, a, b, l, p, g, y in BANNERS)
out += '\n<script src="../../kit/post.js"></script>\n</body>\n</html>\n'
open("posts/blog-banners/post.html", "w", encoding="utf-8").write(out)
print(len(BANNERS), "banners written")
