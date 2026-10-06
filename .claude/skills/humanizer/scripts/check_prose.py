#!/usr/bin/env python3
"""Flag AI-sounding patterns in a Markdown or text file.

Usage: python3 -I check_prose.py <file> [<file> ...]

Skips YAML frontmatter, fenced code blocks, inline code and URLs. Prints
suspects with line numbers plus rhythm statistics. Exit code is 1 if any em or
en dash is found (a hard rule in this repo), otherwise 0. Everything else is
advisory.
"""

import re
import statistics
import sys

WORDS = [
    "delve", "delves", "leverage", "leveraging", "harness", "unlock", "unlocking",
    "unleash", "elevate", "empower", "empowers", "streamline", "streamlined",
    "foster", "underscore", "underscores", "showcase", "revolutionize",
    "supercharge", "crucial", "pivotal", "vital", "robust", "seamless",
    "seamlessly", "dynamic", "comprehensive", "cutting-edge", "game-changing",
    "game-changer", "transformative", "innovative", "ever-evolving", "meticulous",
    "landscape", "realm", "tapestry", "journey", "ecosystem", "synergy",
    "testament", "paradigm", "cornerstone", "beacon", "navigate", "navigating",
]

PHRASES = [
    "in today's fast-paced", "ever-evolving landscape", "it's worth noting",
    "it is worth noting", "it's important to note", "it is important to note",
    "it goes without saying", "let's dive in", "let's explore", "dive into",
    "in this article, we", "at the end of the day", "when it comes to",
    "in conclusion", "to sum up", "look no further", "plays a crucial role",
    "plays a key role", "a pivotal moment", "experts say", "studies show",
    "here's the thing", "the result?", "the answer?", "the catch?",
    "game changer", "whether you're a",
]

STRUCTURES = [
    (re.compile(r"\bnot (just|only|about) [^.?!]{1,60}?[,;] (but|it's|it is)\b", re.I),
     "'not X, but Y' contrast"),
    (re.compile(r"\bit'?s not about\b", re.I), "'it's not about X' framing"),
    (re.compile(r"\bno longer\b[^.?!]{1,60}?,? but\b", re.I), "'no longer X, but Y' contrast"),
    (re.compile(r"(^|\.\s)(the (result|answer|catch|truth|kicker)|here'?s (the thing|why|how))\s*[:?]", re.I),
     "colon/question reveal"),
    (re.compile(r"!"), "exclamation mark"),
]

DASHES = re.compile("[" + chr(0x2013) + chr(0x2014) + "]")


def prose_lines(text):
    """Yield (line_number, line) for prose only."""
    lines = text.splitlines()
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1
    in_fence = False
    for n in range(i, len(lines)):
        line = lines[n]
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = re.sub(r"`[^`]*`", "", line)
        line = re.sub(r"\]\([^)]*\)", "]", line)
        line = re.sub(r"https?://\S+", "", line)
        yield n + 1, line


def check(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    findings = []
    dash_hits = 0
    prose = []
    for n, line in prose_lines(text):
        prose.append(line)
        low = line.lower()
        if DASHES.search(line):
            dash_hits += 1
            findings.append((n, "DASH", "em/en dash (banned)"))
        for w in WORDS:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                findings.append((n, "WORD", w))
        for p in PHRASES:
            if p in low:
                findings.append((n, "PHRASE", p))
        for rx, label in STRUCTURES:
            if rx.search(line):
                findings.append((n, "STRUCT", label))

    body = " ".join(l for l in prose if l.strip() and not l.lstrip().startswith(("#", ">", "|")))
    body = re.sub(r"[*_]", "", body)
    sentences = [s for s in re.split(r"(?<=[.?!])\s+", body) if len(s.split()) > 0]
    lengths = [len(s.split()) for s in sentences]
    bold = len(re.findall(r"\*\*[^*]+\*\*", "\n".join(prose)))

    print(f"== {path}")
    for n, kind, detail in findings:
        print(f"  line {n:>4}  {kind:<6} {detail}")
    if not findings:
        print("  no pattern hits")
    if lengths:
        short = sum(1 for x in lengths if x <= 4)
        print(f"  sentences: {len(lengths)}, mean length {statistics.mean(lengths):.1f} words, "
              f"stdev {statistics.pstdev(lengths):.1f}, very short (<=4 words): {short}")
        if statistics.pstdev(lengths) < 5:
            print("  note: low sentence-length variation, rhythm may feel monotonous")
    print(f"  bold spans: {bold}")
    return dash_hits


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    total_dashes = sum(check(p) for p in argv[1:])
    return 1 if total_dashes else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
