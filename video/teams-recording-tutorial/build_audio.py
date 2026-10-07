"""Generate the voiceover, the scene timeline, lip-sync data, captions and chapters.

Usage: KOKORO_DIR=/path/to/models python3 build_audio.py
Needs kokoro-v1.0.onnx and voices-v1.0.bin from
https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0
"""
import hashlib
import json
import os
from pathlib import Path

import numpy as np
import soundfile as sf

HERE = Path(__file__).resolve().parent
BUILD = HERE / "build"
CACHE = BUILD / "tts-cache"
FPS = 30
SR = 24000
LEAD = 0.5          # silence at the start of each scene
INTRO_LEAD = 1.0
DEFAULT_GAP = 0.35  # silence between lines in a scene


def trim(sig, thresh=0.01, pad=0.04):
    idx = np.where(np.abs(sig) > thresh)[0]
    if len(idx) == 0:
        return sig
    a = max(0, idx[0] - int(pad * SR))
    b = min(len(sig), idx[-1] + int(pad * SR))
    return sig[a:b]


def tts(kokoro, text, voice, speed):
    key = hashlib.sha1(f"{voice}|{speed}|{text}".encode()).hexdigest()[:16]
    path = CACHE / f"{key}.wav"
    if path.exists():
        sig, _ = sf.read(path, dtype="float32")
        return sig
    sig, sr = kokoro.create(text, voice=voice, speed=speed, lang="en-us")
    assert sr == SR
    sig = trim(np.asarray(sig, dtype="float32"))
    sf.write(path, sig, SR)
    return sig


def ts_srt(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def ts_chapter(t):
    s = int(t)
    return f"{s // 60}:{s % 60:02d}"


def main():
    from kokoro_onnx import Kokoro

    model_dir = Path(os.environ.get("KOKORO_DIR", HERE / "models"))
    kokoro = Kokoro(str(model_dir / "kokoro-v1.0.onnx"), str(model_dir / "voices-v1.0.bin"))
    script = json.loads((HERE / "script.json").read_text())
    BUILD.mkdir(exist_ok=True)
    CACHE.mkdir(exist_ok=True)

    t = 0.0
    pieces = []  # (start_time, signal)
    scenes = []
    for i, sc in enumerate(script["scenes"]):
        start = t
        t += INTRO_LEAD if i == 0 else LEAD
        gap = sc.get("gap", DEFAULT_GAP)
        lines = []
        for j, ln in enumerate(sc["lines"]):
            sig = tts(kokoro, ln.get("say", ln["text"]), script["voice"], script["speed"])
            dur = len(sig) / SR
            lines.append({"id": ln["id"], "text": ln["text"], "start": round(t, 3), "end": round(t + dur, 3)})
            pieces.append((t, sig))
            t += dur
            if j < len(sc["lines"]) - 1:
                t += gap
        t += sc.get("tail", 0.8)
        scenes.append({"id": sc["id"], "chapter": sc["chapter"], "start": round(start, 3), "end": round(t, 3), "lines": lines})

    total = t
    voice = np.zeros(int(total * SR) + SR, dtype="float32")
    for st, sig in pieces:
        a = int(st * SR)
        voice[a:a + len(sig)] += sig
    voice = voice[: int(total * SR)]
    peak = np.max(np.abs(voice))
    voice = voice / peak * 0.89
    sf.write(BUILD / "voice.wav", voice, SR)

    # Lip sync: per-frame loudness, normalised, with fast attack and slower release.
    n_frames = int(np.ceil(total * FPS))
    hop = SR // FPS
    rms = np.array([np.sqrt(np.mean(voice[k * hop:(k + 1) * hop] ** 2) + 1e-12) for k in range(n_frames)])
    ref = np.percentile(rms[rms > 0.005], 90) if np.any(rms > 0.005) else 1.0
    raw = np.clip((rms - 0.004) / (ref - 0.004), 0, 1.2)
    mouth = np.zeros_like(raw)
    for k in range(n_frames):
        prev = mouth[k - 1] if k else 0
        mouth[k] = prev + (raw[k] - prev) * (0.75 if raw[k] > prev else 0.45)
    mouth = np.clip(mouth, 0, 1)

    timeline = {"fps": FPS, "duration": round(total, 3), "scenes": scenes, "mouth": [round(float(m), 3) for m in mouth]}
    (BUILD / "timeline.json").write_text(json.dumps(timeline))
    (BUILD / "timeline.js").write_text("window.TIMELINE = " + json.dumps(timeline) + ";\n")

    srt = []
    n = 1
    for sc in scenes:
        for ln in sc["lines"]:
            srt.append(f"{n}\n{ts_srt(ln['start'])} --> {ts_srt(ln['end'] + 0.25)}\n{ln['text']}\n")
            n += 1
    (HERE / "captions.srt").write_text("\n".join(srt))

    chapters = "\n".join(f"{ts_chapter(sc['start'])} {sc['chapter']}" for sc in scenes)
    (BUILD / "chapters.txt").write_text(chapters + "\n")
    print(f"duration {total:.1f}s, {n - 1} lines, {n_frames} frames")
    print(chapters)


if __name__ == "__main__":
    main()
