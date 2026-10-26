"""Single source of timing for Short #2. Writes timeline.js (for the page) and timeline.json (for the mix).

After recording the real VO, adjust LINES start/end to match it and re-run:
    python3 src/timeline.py && node src/render.js && python3 src/mix.py
"""
import json
import random
from pathlib import Path

FPS = 30
DURATION = 38.8
BEAT = 60 / 109.96  # music bed tempo

# Scene cuts, all on the music's beat grid.
SCENES = {
    "hook": [0.00, 5.19],
    "problem": [5.19, 11.47],
    "reveal": [11.47, 14.73],
    "product": [14.73, 24.01],
    "present": [24.01, 31.65],
    "punch": [31.65, 34.92],
    "cta": [34.92, DURATION],
}

# VO lines (estimated read, ~150 wpm). caption=False: the scene's own type carries the line.
LINES = [
    (0.30, 2.30, "Your buyer can hear you typing."),
    (2.45, 4.95, "And they can tell you're not listening."),
    (5.40, 7.90, "Discovery calls are where deals are won,"),
    (8.00, 11.20, "but most reps spend them half-listening, half-typing."),
    (12.10, 14.40, "Lynkk takes the notes for you."),
    (14.90, 18.80, "Every call gets a summary, the decisions, the action items,"),
    (18.90, 23.70, "and a full transcript with speaker labels, so you know exactly who said what."),
    (24.20, 28.60, "That means you can actually ask the second question. And the third."),
    (28.70, 31.20, "The ones that uncover real pain."),
    (31.90, 34.30, "Be present, not preoccupied.", False),
    (35.10, 37.40, "Get Lynkk free at lynkk.ai.", False),
]


def words_with_times(start, end, text):
    words = text.split(" ")
    weights = [len(w) + 2 for w in words]
    total = sum(weights)
    out, t = [], start
    for w, wt in zip(words, weights):
        out.append({"w": w, "t": round(t, 3)})
        t += (end - start) * wt / total
    return out


# Messy notes typed during the hook and problem scenes. "<" is a backspace.
NOTES = (
    "corvane disco call\n"
    "budget?? 30k?? or 50\n"
    "IT team.. ask l8r\n"
    "timelien<<<ine q4???\n"
    "she said smth abt reps\n"
    "losing contxt<<<<<ontext?? \n"
    "wait what did she say"
)


def keystrokes(start, end, text, seed=7):
    rng = random.Random(seed)
    events, t = [], start
    for ch in text:
        events.append({"t": round(t, 3), "c": ch})
        gap = rng.uniform(0.045, 0.11)
        if ch == "\n":
            gap += rng.uniform(0.18, 0.32)
        elif ch in "?." and rng.random() < 0.3:
            gap += 0.12
        t += gap
    # Stretch or squeeze to land the last key just before the end.
    scale = (end - start) / (events[-1]["t"] - start)
    for e in events:
        e["t"] = round(start + (e["t"] - start) * scale, 3)
        e["s"] = rng.randrange(12)  # which keypress sample
    return events


def main():
    here = Path(__file__).parent
    keys = keystrokes(0.12, SCENES["reveal"][0] - 0.12, NOTES)
    lines = [
        {"start": l[0], "end": l[1], "text": l[2], "caption": l[3] if len(l) > 3 else True,
         "words": words_with_times(l[0], l[1], l[2])}
        for l in LINES
    ]
    # A recorded or scratch VO's measured timing (vo_timing.json) wins over the estimates above.
    vo = here / "vo_timing.json"
    if vo.exists():
        for line, m in zip(lines, json.loads(vo.read_text())):
            assert line["text"] == m["text"], f"vo_timing.json is stale: {m['text']!r}"
            line.update(start=m["start"], end=m["end"], words=m["words"])
    tl = {
        "fps": FPS,
        "duration": DURATION,
        "beat": BEAT,
        "scenes": SCENES,
        "lines": lines,
        "keys": keys,
    }
    (here / "timeline.js").write_text("window.TL = " + json.dumps(tl) + ";\n")
    (here / "timeline.json").write_text(json.dumps(tl, indent=1))
    print(f"{len(keys)} keystrokes, {len(LINES)} lines, {DURATION}s")


if __name__ == "__main__":
    main()
