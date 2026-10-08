"""Narration to audio with Kokoro (open model, runs locally). Run from a video folder:
  <venv>/bin/python -I ../tools/tts.py <kokoro.onnx> <voices.bin>
Writes out/audio/<scene>.wav, out/timing.json (line start times per scene) and
out/captions.srt. Captions use the written text; the voice reads SPOKEN, which
only fixes pronunciation. A scene's optional "hold" adds seconds of silence at
its end (the CTA holds for the YouTube end screen)."""
import json, re, sys, os
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

SPOKEN = [(r"lynkk\.ai", "Link dot A.I."), (r"\bLynkk\b", "Link"), (r"\b1:1s\b", "one-on-ones"), (r"\bPro\b", "Pro")]
LEAD, GAP, TAIL = 0.45, 0.3, 0.7   # seconds of silence: scene start, between lines, scene end

def spoken(text):
    for pat, rep in SPOKEN:
        text = re.sub(pat, rep, text)
    return text

def ts(s):
    h, r = divmod(s, 3600); m, sec = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(sec):02},{int(round((sec - int(sec)) * 1000)):03}"

doc = json.load(open("narration.json"))
k = Kokoro(sys.argv[1], sys.argv[2])
os.makedirs("out/audio", exist_ok=True)
timing, cues, offset, n = {}, [], 0.0, 1
for sc in doc["scenes"]:
    sr = 24000
    parts, starts, t = [np.zeros(int(LEAD * sr), dtype=np.float32)], [], LEAD
    for line in sc["lines"]:
        audio, sr = k.create(spoken(line), voice=doc["voice"], speed=doc["speed"], lang="en-us")
        dur = len(audio) / sr
        starts.append(round(t, 3))
        cues.append(f"{n}\n{ts(offset + t)} --> {ts(offset + t + dur)}\n{line}\n"); n += 1
        parts += [audio.astype(np.float32), np.zeros(int(GAP * sr), dtype=np.float32)]
        t += dur + GAP
    parts.append(np.zeros(int((TAIL - GAP + sc.get("hold", 0)) * sr), dtype=np.float32))
    wav = np.concatenate(parts)
    sf.write(f"out/audio/{sc['id']}.wav", wav, sr)
    total = len(wav) / sr
    timing[sc["id"]] = {"duration": round(total, 3), "starts": starts, "offset": round(offset, 3), "chapter": sc.get("chapter")}
    offset += total
    print(f"{sc['id']}: {total:.1f}s")
json.dump(timing, open("out/timing.json", "w"), indent=2)
open("out/captions.srt", "w").write("\n".join(cues))
open("out/chapters.txt", "w").write("\n".join(f"{int(v['offset'] // 60)}:{int(v['offset'] % 60):02} {v['chapter']}" for v in timing.values() if v["chapter"]) + "\n")
print(f"total {offset:.1f}s, {n - 1} cues")
