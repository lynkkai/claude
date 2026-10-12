"""Build the secondary keyword matrix (volume, difficulty, uses, heading placement) for all articles.

Usage: python3 scripts/keyword_matrix.py
Writes seo/secondary-keyword-matrix.md and seo/secondary-keyword-matrix.csv.
"""
import csv
import glob
import re
from collections import Counter

POST = {"best-ai-note-takers": 1, "best-free-ai-note-takers": 2, "zoom-meeting-recorders": 3,
        "ai-note-taker-microsoft-teams": 4, "transcribe-audio-to-text": 5, "ai-voice-recorders": 6,
        "ai-transcription-software": 7, "voice-to-text-apps": 8, "ai-powered-meeting-assistants": 9,
        "zoom-ai-companion-alternatives": 10, "how-to-transcribe-zoom-meetings": 16, "dictation-on-mac": 17,
        "dictate-in-microsoft-word": 18, "voice-memo-transcription": 19, "google-meet-transcript": 20,
        "sales-conversation-intelligence": 21, "recruiting-interview-transcription": 22,
        "meeting-minutes-to-jira": 23, "founders-meeting-notes": 24, "meeting-knowledge-management": 25,
        "daily-standup-meeting": 26, "one-on-one-meeting": 27, "legal-transcription-service": 28,
        "medical-transcription-software": 29, "meeting-minutes-sample": 30}


def norm(x):
    x = re.sub(r"\]\([^)]*\)", "]", x)
    return " ".join(re.sub(r"[#>*|`\[\]()]", " ", x).lower().replace("-", " ").split())


def band(sd):
    return "Low" if sd < 30 else ("Medium" if sd < 50 else "High")


rows = []
for f in glob.glob("articles/*.md"):
    slug = f.split("/")[-1][:-3]
    t = open(f, encoding="utf-8").read()
    fm, body = t.split("---\n", 2)[1], t.split("---\n", 2)[2].split("<script")[0]
    low, heads = norm(body), norm(" ".join(re.findall(r"^#{1,3} .*$", body, re.M)))
    kw = re.findall(r"^\s+- (.+?)\s+#\s*(.*)$", fm.split("keywords:")[1].split("keywords_added:")[0], re.M)
    for k, c in kw[1:]:
        m = re.search(r"([\d,]+)\s*/\s*(?:SD\s*)?(\d+)", c)
        v, sd = int(m.group(1).replace(",", "")), int(m.group(2))
        rows.append((POST.get(slug, 0), slug, k, v, sd, band(sd), low.count(k.lower()),
                     "Yes" if k.lower() in heads else "No"))
rows.sort(key=lambda r: (r[0], -r[3]))
b = Counter(r[5] for r in rows)
md = ["| # | Blog | Secondary keyword | Volume | SD | Difficulty | Uses | In a heading |",
      "|---|---|---|---|---|---|---|---|"]
md += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]:,} | {r[4]} | {r[5]} | {r[6]} | {r[7]} |" for r in rows]
head = ("# Secondary keyword matrix\n\nVolume = US monthly searches, SD = Ubersuggest SEO difficulty "
        "(Low under 30, Medium 30-49, High 50+), pulled 2026-09-30. Uses = exact-phrase count in the article "
        "body (hyphens treated as spaces). In a heading = appears in the H1, an H2 or an H3.\n\n"
        f"**{len(rows)} secondary keywords across {len({r[1] for r in rows})} blogs, about "
        f"{sum(r[3] for r in rows):,} US searches a month. Difficulty mix: {b['Low']} Low, "
        f"{b['Medium']} Medium, {b['High']} High.**\n\n")
open("seo/secondary-keyword-matrix.md", "w", encoding="utf-8").write(head + "\n".join(md) + "\n")
with open("seo/secondary-keyword-matrix.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["post", "blog", "secondary_keyword", "us_volume", "sd", "difficulty", "uses_in_article", "in_heading"])
    w.writerows(rows)
print(f"{len(rows)} rows written")
