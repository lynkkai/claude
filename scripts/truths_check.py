"""Flag article claims that conflict with lynkk-post-kit/docs/TRUTHS.md.

Usage: python3 scripts/truths_check.py articles/*.md   (exit 1 if anything is found)
Checks the article body only (not the JSON-LD schema, which build_schema.py regenerates).
"""
import re
import sys

PATTERNS = [
    (r"15\+ languages|\b1[56] languages", "language count: say 17 languages (4 in beta), or 18 for Mac cloud dictation"),
    (r"9\d(\.\d)?% accura|~9\d%|about 9\d%", "no accuracy percentage for Lynkk"),
    (r"(about |within |~)?30 seconds", "no speed claims (notes in 30 seconds)"),
    (r"hey lynkk|speaks? when|live voice|voice answers|spoken answers|voice assistant|answers? (you |questions |your questions )?(live )?(by voice )?during|answer(s)? (live )?by voice|hear the answer", "Lynkk does not speak or answer during the call"),
    (r"lynkk[^.]{0,80}(aes-?256|gdpr)|(aes-?256|gdpr)[^.]{0,40}lynkk|privacy:\*\* aes", "Lynkk encryption / GDPR claims are not verified"),
    (r"knowledge graph", "no knowledge graph; say Ask across your notes"),
    (r"lynkk[^.]{0,80}offline|offline[^.]{0,40}lynkk", "offline-first is not true (only the Mac upload survives bad Wi-Fi)"),
    (r"calendly|cal\.com|\bmcp\b", "integration not in TRUTHS.md"),
    (r"bot (comes with|joins? on|on) pro|meeting bot on pro|\(pro\) joins|bot \(pro\)|joins on pro|the meeting bot comes", "the meeting bot is free (audio only); video recording is Pro"),
    (r"5 hours", "do not state plan hours or limits"),
    (r"(team|shared)[- ](wide )?memory|searchable memory for|whole team's|teammates'? notes|across the meetings they have access", "Ask answers only from your own notes"),
    (r"(creates?|create|turns? .{0,40}into|automatic\w*) .{0,30}jira tickets|jira tickets .{0,20}(created|automatic)", "Jira send is manual from the note (one issue per action item)"),
    (r"lynkk[^.]{0,40}(windows app|iphone|android|mobile app|ios app|phone app)", "no phone or Windows app"),
]


def main(paths):
    found = 0
    for p in paths:
        body = open(p, encoding="utf-8").read().split('<script type="application/ld+json">')[0]
        for i, line in enumerate(body.splitlines(), 1):
            for pat, msg in PATTERNS:
                for m in re.finditer(pat, line, re.I):
                    found += 1
                    print(f"{p}:{i}: {msg}: ...{line[max(0, m.start() - 40):m.end() + 40]}...")
    print(f"{found} issue(s)")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
