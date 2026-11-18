"""Build posts/blog-banners-2026-10/post.html: wide banners for the October 2026 blog drafts.

Usage (from lynkk-post-kit/): python3 posts/blog-banners-2026-10/build.py
Then render: CHROMIUM_PATH=... node scripts/render.mjs posts/blog-banners-2026-10
Same layout as posts/blog-banners. Every claim must come from docs/TRUTHS.md.
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
    ("action-items-examples-template", H, "Action items, with examples.", "And a template to copy.",
     "What they are, how to write them and how to track them.", "ember", "Action items",
     opts(("Send the release notes", "Sam · Fri", 0), ("Update the pricing page", "Priya · Mon", 0), ("Book the follow-up", "You · Thu", 1))
     + fine("Each one with an owner, a due date and a priority.")),
    ("zoom-note-taker", G, "The best Zoom note takers.", "Seven AI tools, compared.",
     "Bot, desktop app or browser, and what you get after the call.", "dusk", "Meeting Brief",
     rows(("Takeaway", "Search ships before export"), ("Decided", "Launch on the 21st"), ("Task", "Priya, security answers by Fri"))),
    ("zoom-bot-join-meeting", H, "How to add a meeting bot.", "To Zoom, Google Meet or Teams.",
     "Paste a link or turn on auto-join, then admit it.", "sky", "Meeting bot",
     opts(("Paste a meeting link", "", 1), ("Calendar auto-join", "On", 1), ("Live transcript panel", "", 1))
     + fine("Free, audio only. Video recording is Pro.")),
    ("meeting-preparation", U, "Walk in with context.", "From the last meeting.",
     "A brief, a checklist and a morning email that does the prep.", "sky", "Morning briefing",
     times(("10:00", "Acme renewal"), ("13:30", "Design review"), ("16:00", "1:1 with Sam"))
     + fine("Last note with Acme on file. 2 open action items.")),
    ("meeting-agenda-template", H, "A meeting agenda template.", "With 10 examples to copy.",
     "Goal, times, owners and a recap that sets up the next one.", "field", "Summary Shape · Pro",
     radios(("Daily Stand-up", "", 0), ("1:1", "", 1), ("Sales Call", "", 0), ("Board Meeting", "", 0))
     + fine("Notes that follow the shape of the meeting.")),
    ("how-to-record-a-teams-meeting", H, "How to record a Teams meeting.", "And where it is saved.",
     "Record, find and download it, and what to do when you can't.", "meadow", "Microsoft Teams call detected",
     '<div class="m-row"><span class="m-btn">Record</span><span class="m-k">Not now</span></div>'
     + fine("No bot joins the call. Both sides on 2 channels.")),
    ("how-to-record-audio-on-mac", H, "How to record audio on Mac.", "Five free ways.",
     "Your voice, your screen, internal audio and both sides of a call.", "night", "Recording",
     live("12:04") + lvl("You", 62) + lvl("Others", 38) + fine("Written to disk from the first second.")),
    ("board-meeting-agenda", H, "Board meeting agenda format.", "With 3 samples to copy.",
     "The 10-part order, the consent agenda and executive session.", "dusk", "Board Meeting · Pro",
     rows(("Decided", "Consent agenda approved"), ("Task", "Secretary, minutes by Fri"), ("Open", "Audit committee chair"))),
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
open("posts/blog-banners-2026-10/post.html", "w", encoding="utf-8").write(out)
print(len(BANNERS), "banners written")
