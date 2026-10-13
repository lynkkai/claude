"""Narration to audio with Kokoro (open model, runs locally), adapted from ask-lynkk-video/tts.py.
  python3 -I tts.py <narration.json> <outDir> <kokoro.onnx> <voices.bin>
Writes <outDir>/audio/<scene>.wav, <outDir>/timing.json (line start and end times per scene, plus the
written lines) and <outDir>/captions.srt. Captions use the written text; the voice reads SPOKEN, which
only fixes pronunciation."""
import json
import os
import re
import sys

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

SPOKEN = [(r"lynkk\.ai", "Link dot A I"), (r"\bLynkk's\b", "Link's"), (r"\bLynkk\b", "Link"),
          (r"Otter\.ai", "Otter dot A I"), (r"@Lynkk", "at Link"), (r"\bSSO\b", "S S O"),
          (r"\b2 hours\b", "two hours"), (r"\b30 minutes\b", "thirty minutes")]
LEAD, GAP, TAIL = 0.5, 0.38, 0.8   # seconds of silence: scene start, between lines, scene end


def spoken(text):
    for pat, rep in SPOKEN:
        text = re.sub(pat, rep, text)
    return text


def ts(s):
    h, r = divmod(s, 3600)
    m, sec = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(sec):02},{int(round((sec - int(sec)) * 1000)):03}"


def trim(a, sr):
    idx = np.where(np.abs(a) > 0.01)[0]
    return a if len(idx) == 0 else a[max(0, idx[0] - int(0.03 * sr)): idx[-1] + int(0.08 * sr)]


def main(narration, out, onnx, voices):
    doc = json.load(open(narration))
    k = Kokoro(onnx, voices)
    os.makedirs(f"{out}/audio", exist_ok=True)
    timing, cues, offset, n = {}, [], 0.0, 1
    for sc in doc["scenes"]:
        sr = 24000
        parts, starts, ends, t = [np.zeros(int(LEAD * sr), dtype=np.float32)], [], [], LEAD
        for i, line in enumerate(sc["lines"]):
            # a little pace variation per line keeps the read from sounding mechanical
            speed = doc["speed"] * (1.0 + (0.02 if i % 2 else -0.01))
            audio, sr = k.create(spoken(line), voice=doc["voice"], speed=speed, lang="en-us")
            audio = trim(np.asarray(audio, dtype=np.float32), sr)
            dur = len(audio) / sr
            starts.append(round(t, 3))
            ends.append(round(t + dur, 3))
            cues.append(f"{n}\n{ts(offset + t)} --> {ts(offset + t + dur)}\n{line}\n")
            n += 1
            parts += [audio, np.zeros(int(GAP * sr), dtype=np.float32)]
            t += dur + GAP
        tail = TAIL + sc.get("hold", 0.0)
        parts.append(np.zeros(int(max(0.0, tail - GAP) * sr), dtype=np.float32))
        wav = np.concatenate(parts)
        sf.write(f"{out}/audio/{sc['id']}.wav", wav, sr)
        total = len(wav) / sr
        timing[sc["id"]] = {"duration": round(total, 3), "starts": starts, "ends": ends,
                            "lines": sc["lines"], "offset": round(offset, 3), "chapter": sc.get("chapter", "")}
        offset += total
        print(f"{sc['id']}: {total:.1f}s")
    timing["_order"] = [sc["id"] for sc in doc["scenes"]]
    timing["_total"] = round(offset, 3)
    json.dump(timing, open(f"{out}/timing.json", "w"), indent=1)
    open(f"{out}/captions.srt", "w").write("\n".join(cues))
    print(f"total {offset:.1f}s, {n - 1} cues")


if __name__ == "__main__":
    main(*sys.argv[1:5])
