"""Voice + music for one video, plus the timeline the renderer follows.

Usage: python3 build_audio.py <slug> <workdir>
Writes <workdir>/<slug>/{seg_*.wav, voice.wav, music.wav, mix.wav, timeline.json}
"""
import base64
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.request

import numpy as np
import soundfile as sf

from content import VIDEOS
import music
import music_indian

HERE = os.path.dirname(os.path.abspath(__file__))
# Voice engine: Sarvam AI (Bulbul, Indian voices) when SARVAM_API_KEY is set, else offline Kokoro.
ENGINE = os.environ.get("LYNKK_TTS") or ("sarvam" if os.environ.get("SARVAM_API_KEY") else "kokoro")
SARVAM_MODEL = os.environ.get("SARVAM_MODEL", "bulbul:v3")
SARVAM_SPEAKER = os.environ.get("SARVAM_SPEAKER", "priya")
SARVAM_TEMP = float(os.environ.get("SARVAM_TEMPERATURE", "0.7"))
VOICE = os.environ.get("LYNKK_VOICE", "am_adam")    # Kokoro voice: US English male "Adam" (chosen by the team)
# Background music: "sitar" (chosen), "bansuri", "lofi" from music_indian.py, or "synth" for the original bed
MUSIC = os.environ.get("LYNKK_MUSIC", "sitar")
SPEED = float(os.environ.get("LYNKK_SPEED", "0.98"))
GAP = 0.42        # breath between lines
LEAD_IN = 0.35


def tts_text(seg):
    s = seg.get("say") or seg["cap"]
    s = s.replace("lynkk.ai", "link dot A I").replace("Lynkk", "Link").replace("Otter.ai", "Otter dot A I")
    if ENGINE == "kokoro":
        s = s.replace("Hinglish", "Hing lish")  # otherwise Kokoro reads it as "English"
    return s


class KokoroVoice:
    def __init__(self, models):
        from kokoro_onnx import Kokoro
        self.k = Kokoro(os.path.join(models, "kokoro-v1.0.onnx"), os.path.join(models, "voices-v1.0.bin"))

    def synth(self, text, speed, cache):
        samples, sr = self.k.create(text, voice=VOICE, speed=speed, lang="en-us")
        return np.asarray(samples, dtype=np.float32), sr


class SarvamVoice:
    """Sarvam AI text-to-speech (https://docs.sarvam.ai), Indian English. Lines are cached on disk."""
    URL = "https://api.sarvam.ai/text-to-speech"

    def synth(self, text, speed, cache):
        body = {"text": text, "target_language_code": "en-IN", "model": SARVAM_MODEL,
                "speaker": SARVAM_SPEAKER, "pace": round(speed, 3), "speech_sample_rate": 44100,
                "temperature": SARVAM_TEMP}
        key = hashlib.sha1(json.dumps(body, sort_keys=True).encode()).hexdigest()[:16]
        path = os.path.join(cache, f"sarvam_{key}.wav")
        if not os.path.exists(path):
            req = urllib.request.Request(self.URL, data=json.dumps(body).encode(), method="POST", headers={
                "api-subscription-key": os.environ["SARVAM_API_KEY"], "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                audio = base64.b64decode(json.load(r)["audios"][0])
            with open(path, "wb") as f:
                f.write(audio)
        samples, sr = sf.read(path, dtype="float32")
        if samples.ndim > 1:
            samples = samples.mean(axis=1)
        return samples, sr


def chunks(cap, max_words):
    """Split a caption into short readable phrases, breaking at punctuation first."""
    out = []
    for part in re.split(r"(?<=[.,?!:])\s+", cap.strip()):
        words = part.split()
        while len(words) > max_words:
            cut = max_words if len(words) - max_words >= 2 else max_words - 1
            out.append(" ".join(words[:cut]))
            words = words[cut:]
        if words:
            out.append(" ".join(words))
    return out


def trim(samples, sr, thresh=0.01):
    idx = np.where(np.abs(samples) > thresh)[0]
    if len(idx) == 0:
        return samples
    a = max(0, idx[0] - int(0.03 * sr))
    b = min(len(samples), idx[-1] + int(0.08 * sr))
    return samples[a:b]


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def main(slug, work):
    video = next(v for v in VIDEOS if v["slug"] == slug)
    out = os.path.join(work, slug)
    os.makedirs(out, exist_ok=True)
    voice_engine = SarvamVoice() if ENGINE == "sarvam" else KokoroVoice(os.path.join(work, "..", "models"))
    cache = os.path.join(work, "tts_cache")
    os.makedirs(cache, exist_ok=True)
    max_words = 4 if video["format"] == "vertical" else 7
    rng = np.random.default_rng(11)

    pieces, timeline, t = [], [], LEAD_IN
    sr = None
    for i, seg in enumerate(video["segments"]):
        # tiny per-line speed variation keeps the read from sounding mechanical
        speed = SPEED * float(rng.uniform(0.97, 1.03))
        samples, sr = voice_engine.synth(tts_text(seg), speed, cache)
        samples = trim(samples, sr)
        if not pieces:
            pieces.append(np.zeros(int(LEAD_IN * sr)))
        dur = len(samples) / sr
        caps = chunks(seg["cap"], max_words)
        weights = np.array([len(c) + 6 for c in caps], dtype=float)
        bounds = np.concatenate([[0], np.cumsum(weights) / weights.sum()]) * dur
        timeline.append({
            "i": i, "start": round(t, 3), "voice_end": round(t + dur, 3),
            "cap": seg["cap"], "scene": seg["scene"],
            "chunks": [{"text": c, "start": round(t + bounds[k], 3), "end": round(t + bounds[k + 1], 3)}
                       for k, c in enumerate(caps)],
        })
        pieces.append(samples)
        gap = GAP + float(rng.uniform(-0.06, 0.1)) + seg.get("pause", 0.0)
        pieces.append(np.zeros(int(gap * sr)))
        t += dur + gap
    for k, seg in enumerate(timeline):
        seg["end"] = timeline[k + 1]["start"] if k + 1 < len(timeline) else round(t, 3)
    total = t + 0.4

    raw = os.path.join(out, "voice_raw.wav")
    sf.write(raw, np.concatenate(pieces), sr)
    voice = os.path.join(out, "voice.wav")
    # warmth, presence, gentle compression and a very small room so it sits like a real mic read
    run(["ffmpeg", "-y", "-i", raw, "-af",
         "aresample=44100,highpass=f=75,equalizer=f=180:t=q:w=1:g=2,equalizer=f=3200:t=q:w=1.2:g=1.5,"
         "equalizer=f=7500:t=q:w=1:g=-2,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120:makeup=2,"
         "aecho=0.85:0.5:22|41:0.05|0.03,loudnorm=I=-16:TP=-1.5:LRA=7",
         "-ar", "44100", "-ac", "2", voice])

    mus = os.path.join(out, "music.wav")
    seed = 3 if "otter" in slug else 9
    if MUSIC == "synth":
        sf.write(mus, music.build(total, seed=seed), music.SR)
    else:
        sf.write(mus, music_indian.build(MUSIC, total, seed=seed), music_indian.SR)
    mix = os.path.join(out, "mix.wav")
    run(["ffmpeg", "-y", "-i", voice, "-i", mus, "-filter_complex",
         "[1:a]volume=0.2[m];[0:a]asplit=2[v][vk];"
         "[m][vk]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=400[md];"
         "[v][md]amix=inputs=2:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.0:LRA=9[a]",
         "-map", "[a]", "-ar", "44100", mix])

    meta = {"slug": slug, "format": video["format"], "rival": video["rival"], "source": video["source"],
            "duration": round(total, 3), "segments": timeline}
    with open(os.path.join(out, "timeline.json"), "w") as f:
        json.dump(meta, f, indent=1)
    print(slug, "duration", round(total, 2))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
