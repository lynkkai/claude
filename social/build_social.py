"""Build the Lynkk Instagram and LinkedIn plan (Markdown) and its shareable page (HTML).

Usage: python3 social/build_social.py [path/to/page.html]
"""
import html, json, os, sys

sys.path.insert(0, os.path.dirname(__file__))
from social_stories import STORY_RULES, STORIES, SEASON
from social_usecases import UC_SERIES, USE_CASES, UC_CAROUSELS
from social_data import IG_POSTS, IG_STORIES, IG_HIGHLIGHTS, LI_COMPANY, LI_FOUNDER, USED, USED_THEMES, VIRAL_RULES

HERE = os.path.dirname(os.path.abspath(__file__))

RESEARCH = [
    ("Instagram: Reels for reach, carousels for saves",
     "Reels get about 36% more reach than carousels, and carousels about 12% more engagement than Reels (Buffer, 4M+ posts). Carousels now take up to 20 slides.",
     [("Buffer", "https://buffer.com/resources//instagram-algorithms/"), ("ContentStudio", "https://contentstudio.io/blog/instagram-algorithm")]),
    ("Instagram: sends decide who sees you next",
     "Instagram's head, Adam Mosseri, names watch time, likes per reach and sends per reach as the top signals. Sends matter most for reaching people who don't follow you yet, so posts are built to be forwarded to a colleague.",
     [("Sprout Social", "https://sproutsocial.com/insights/instagram-algorithm"), ("Smash Balloon", "https://smashballoon.com/how-the-instagram-algorithm-works/")]),
    ("Instagram: captions are search",
     "Keywords in the first line of the caption, the bio and the display name feed Instagram search, and public posts can show up on Google. So every caption opens with the plain search phrase.",
     [("Later", "https://later.com/blog/instagram-seo/amp/"), ("True Future Media", "https://www.truefuturemedia.com/articles/instagram-reach-2026-algorithm-reels-carousels-caption-seo")]),
    ("Instagram: 3-5 good Reels a week",
     "The most common guidance is 3-5 quality Reels a week with a steady cadence; originality and watch time count more than volume.",
     [("ListenFirst", "https://www.listenfirstmedia.com/the-state-of-instagram-in-2026-reach-is-not-a-posting-strategy/"), ("Metadata Reactor", "https://metadatareactor.com/blog/instagram-growth-strategy-2026/")]),
    ("LinkedIn: people beat pages",
     "Every study agrees personal profiles out-reach company pages; the gap ranges from under 2x to about 7x depending on who measured it. The founder's profile carries reach; the company page carries proof and assets.",
     [("Ordinal", "https://www.tryordinal.com/blog/linkedin-content-strategy"), ("AuthoredUp", "https://authoredup.com/blog/how-to-use-linkedin-for-business"), ("Blck Alpaca", "https://blckalpaca.at/en/knowledge-base/social-media/social-media-algorithms-distribution/linkedin-company-page-or-personal-profile-reach")]),
    ("LinkedIn: documents hold attention",
     "Document (PDF) carousels lead on dwell time and saves in most 2026 reports; native video under 90 seconds is growing (views up 36% year over year). Strong text posts still win on comments.",
     [("Dataslayer", "https://dataslayer.ai/blog/linkedin-algorithm-february-2026-whats-working-now"), ("DSMN8", "https://dsmn8.com/blog/whats-working-on-linkedin-in-2026-report-key-findings/")]),
    ("LinkedIn: 2-5 posts a week, early comments, careful with links",
     "Buffer's 2M+ post study puts the sweet spot at 2-5 posts a week. Early engagement drives distribution. Studies disagree on how much an outside link hurts, so links go in the first comment and the team tests both.",
     [("Buffer", "https://buffer.com/resources/how-often-to-post-on-linkedin/"), ("Dataslayer", "https://www.dataslayer.ai/blog/linkedin-algorithm-february-2026-whats-working-now")]),
]
CAVEAT = ("Most of these figures come from social media tool vendors with different methods. The directions agree; the exact numbers don't. "
          "Check Instagram Insights and LinkedIn analytics after 4 weeks and shift the mix toward what works for Lynkk.")

CONTENT_TYPES = {
    "Instagram": [
        ("Reel: recurring-cast skit", "Reach and sends", "\"Types of people in meetings\" and \"Intern vs Manager\": the same cast every week, 12-20s, Lynkk only as the punchline.", "2 a week"),
        ("Reel: Corporate Hinglish", "Reach in India", "Says vs means subtitle skits. Ends on Lynkk turning Hinglish into a real action item.", "1 a week"),
        ("Reel: street interview or game", "Comments and sends", "Vox pops at tech parks and coworking spaces; \"guess the meeting\" games.", "Every other week"),
        ("Carousel: interactive", "Saves and tags", "Bingo cards, dictionaries, red flags, \"which character are you\". Made to be screenshotted and tagged.", "1 a week"),
        ("Stories", "Keep followers warm", "Daily polls, quizzes and reposts; the one place a link sticker works. Pin highlights for evergreen sets.", "Daily"),
        ("Trial Reels", "Test hooks safely", "Try two hooks for the same Reel with non-followers before sharing to the main feed.", "As needed"),
    ],
    "LinkedIn company page": [
        ("Document (PDF carousel)", "Dwell time and saves", "Playbooks, templates and buyer guides, 8-12 pages, one idea per page.", "2 a week"),
        ("Native video", "Show the product", "60-90s square video with burned-in captions, hook in the first 3 seconds.", "1 a week"),
        ("Image or text: company news", "Proof", "Pricing, launches and milestones. Short, factual, no hype.", "When there's news"),
    ],
    "LinkedIn founder and team": [
        ("Text post", "Reach and comments", "150-250 words: stories from building Lynkk, sales craft, honest opinions about the category. No link in the body.", "3 a week"),
        ("Reshare with a comment", "Amplify the page", "Team members reshare company documents with one line of their own, within the first hour.", "Each company post"),
    ],
}

CADENCE = [
    ("Instagram", "Mon Reel (meeting life) · Tue carousel · Wed Reel (how-to) · Thu Reel · Fri carousel · Stories daily"),
    ("LinkedIn founder", "Mon, Wed, Fri, 8-9am local time"),
    ("LinkedIn company page", "Tue document, Wed document or video, Thu video or image, 10am-1pm local time"),
    ("Team", "Comment on or reshare each company post within the first hour"),
]

BEFORE = [
    "Publish after the website changes go live. The site still says \"Start for free\"; posts that say $4 a month would contradict it.",
    "Confirm the Instagram handle and LinkedIn page URL (still open in the brand memory) and update bios: \"AI meeting assistant for Zoom, Meet, Teams and in-person meetings. Lynkk Pro $4/mo.\"",
    "Instagram: set up comment-to-DM automation (for example ManyChat) before the \"Comment MOM\" and \"Comment ACTION\" posts, or change those CTAs to \"link in bio\".",
    "Check every competitor price on posting day and show the date on the slide.",
    "Founder posts are drafts for the founder to rewrite in their own voice. Don't post them as written.",
    "Skits: everyone on camera signs a release. Vox pops: ask before filming and get written consent. Use staged sample transcripts, never real customer calls.",
    "Hinglish humor pokes fun at office habits, never at a region, religion, accent or language group.",
]

GUARDRAILS = [
    "Lynkk Pro is $4 a month (₹250 in India), Enterprise is custom. Never \"start free\", \"free plan\" or \"free AI note taker\" about Lynkk. \"Free\" is fine for templates and competitors' plans.",
    "No CRM sync, no phone app, no public API, Google Calendar only. No data residency or certification claims (SOC 2, HIPAA, GDPR).",
    "Spotter is in early access and is never called hidden. Never say Lynkk \"speaks\" in meetings.",
    "Disclose that Lynkk made any comparison and include where competitors win.",
    "Spell it Lynkk (two k's) everywhere, including captions and alt text. No em or en dashes in copy.",
]


def md_posts(posts):
    out = []
    for p in posts:
        out.append(f"### {p['id']}. {p['title']}")
        out.append(f"- **When:** Week {p['week']}, {p['day']}")
        out.append(f"- **Format:** {p['format']}")
        out.append(f"- **Pillar:** {p['pillar']}")
        if p["yt"]:
            out.append(f"- **From YouTube topic:** {p['yt']}")
        out.append(f"- **Hook:** {p['hook']}")
        out.append("- **Outline:**")
        out += [f"  - {b}" for b in p["beats"]]
        out.append(f"- **Caption / post text:** {p['caption']}")
        out.append(f"- **CTA:** {p['cta']}")
        out.append("")
    return out


def build_md():
    L = ["# Lynkk Instagram and LinkedIn Content Plan", "",
         "> Built 2026-11-16. Same product facts and pricing as `video/lynkk-youtube-longform-seo-plan.md` and the November website changes doc.",
         "> Generated from `social/social_data.py` by `social/build_social.py`; edit the data file, then rebuild.",
         "> Each platform gets its own content types. Topics reuse the YouTube research so one idea becomes a long video, a Reel, a carousel and a LinkedIn post.", "",
         "## What the research says", ""]
    for i, (h, body, src) in enumerate(RESEARCH, 1):
        L.append(f"{i}. **{h}.** {body} ({', '.join(f'[{n}]({u})' for n, u in src)})")
    L += ["", f"> Caveat: {CAVEAT}", "", "## Content types by platform", ""]
    for plat, rows in CONTENT_TYPES.items():
        L += [f"### {plat}", "", "| Type | Job | What it is | How often |", "|---|---|---|---|"]
        L += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows]
        L.append("")
    L += ["## Weekly rhythm", "", "| Channel | Schedule |", "|---|---|"]
    L += [f"| {a} | {b} |" for a, b in CADENCE]
    L += ["", "## Already made: don't reuse", "",
          "Found in the repo on 2026-11-16. The live Instagram profile (instagram.com/lynkk.ai) could not be read from here, so which of these went live is unconfirmed.", "",
          "| Content | What it was | Where |", "|---|---|---|"]
    L += [f"| {a} | {b} | `{c}` |" for a, b, c in USED]
    L += ["", "**Themes that are used up:** " + "; ".join(USED_THEMES) + ".", ""]
    L += ["## How the Instagram content is built to go viral", ""] + [f"- **{a}.** {b}" for a, b in VIRAL_RULES]
    L += ["", "## Story Reels: standalone stories", "",
          "Story-first Reels (45-60s) with a character to root for, a conflict and a payoff. Post one a week, on Sunday, alongside the calendar below. Each also cuts for LinkedIn as native video.", ""]
    L += [f"- **{a}.** {c}" for a, c in STORY_RULES]
    L.append("")
    for st in STORIES:
        L += [f"### {st['id']}. {st['title']} ({st['length']})", "", f"**Logline:** {st['logline']}", "", f"**Cast:** {st['cast']}", ""]
        L += [f"- {x}" for x in st["beats"]]
        L += ["", f"**Caption:** {st['caption']}", "", f"**Why it spreads:** {st['spread']}", "", f"**Check before filming:** {st['check']}", ""]
    L += [f"## Serialized story: {SEASON['title']}", "", SEASON["premise"], "", f"**Cast:** {SEASON['cast']}", ""]
    L += [f"- **{a}.** {c}" for a, c in SEASON["episodes"]]
    L += ["", "Post one episode a week (Wednesday evening), pinned as a Reels series. Recap the last cliffhanger in the first 2 seconds of each episode.", ""]
    L += [f"## Use-case series: {UC_SERIES['name']}", "", UC_SERIES["format"], "", f"**When:** {UC_SERIES['cadence']}", "", f"**Cover:** {UC_SERIES['cover']}", ""]
    for u in USE_CASES:
        L += [f"### {u['id']}. {u['job']}: {u['title']}", "", f"**Page:** `{u['page']}`", "", f"- **Hook:** {u['hook']}"]
        L += [f"- {x}" for x in u["beats"]]
        L += [f"- **Caption:** {u['caption']}", f"- **CTA:** {u['cta']}", f"- **Check before filming:** {u['check']}", ""]
    L += ["### Use-case carousels", ""]
    for c in UC_CAROUSELS:
        L += [f"**{c['id']}. {c['title']}**", "", f"- **Hook:** {c['hook']}"] + [f"- {x}" for x in c["beats"]] + [f"- **Caption:** {c['caption']}", f"- **CTA:** {c['cta']}", ""]
    L += ["", "## Before posting", ""] + [f"- {b}" for b in BEFORE]
    L += ["", "## Instagram: 4-week calendar (20 posts)", ""] + md_posts(IG_POSTS)
    L += ["### Stories, every week", "", "| Day | Type | Idea |", "|---|---|---|"]
    L += [f"| {a} | {b} | {c} |" for a, b, c in IG_STORIES]
    L += ["", f"**Highlights:** {', '.join(IG_HIGHLIGHTS)}.", ""]
    L += ["## LinkedIn company page: 4-week calendar (12 posts)", ""] + md_posts(sorted(LI_COMPANY, key=lambda p: (p['week'], "MonTueWedThuFri".index(p['day']))))
    L += ["## LinkedIn founder and team: 4-week calendar (12 posts)", ""] + md_posts(LI_FOUNDER)
    L += ["## Claims guardrails", ""] + [f"- {g}" for g in GUARDRAILS]
    return "\n".join(L) + "\n"


def build_html(template_path):
    t = open(template_path).read()
    data = dict(uc_series=UC_SERIES, use_cases=USE_CASES, uc_carousels=UC_CAROUSELS, story_rules=STORY_RULES, story_reels=STORIES, season=SEASON, used=USED, used_themes=USED_THEMES, viral=VIRAL_RULES, research=RESEARCH, caveat=CAVEAT, types=CONTENT_TYPES, cadence=CADENCE, before=BEFORE,
                guard=GUARDRAILS, stories=IG_STORIES, highlights=IG_HIGHLIGHTS,
                posts=[dict(p, ch="Instagram") for p in IG_POSTS]
                + [dict(p, ch="LinkedIn page") for p in LI_COMPANY]
                + [dict(p, ch="LinkedIn founder") for p in LI_FOUNDER])
    return t.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))


if __name__ == "__main__":
    md = build_md()
    open(os.path.join(HERE, "lynkk-instagram-linkedin-plan.md"), "w").write(md)
    if len(sys.argv) > 1:
        out = sys.argv[1]
        open(out, "w").write(build_html(os.path.join(os.path.dirname(out), "social_template.html")))
    print("ok")
