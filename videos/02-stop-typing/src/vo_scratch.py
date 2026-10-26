"""Scratch VO from a local TTS engine, for timing only (replace with a real read before publishing).

Writes src/assets/vo.wav and src/vo_timing.json. timeline.py picks up vo_timing.json, so captions and
every word-keyed animation follow the scratch read.

Default voice is Kokoro am_fenrir at 1.1x, the voice of the earlier Lynkk "Your records say yes" short.
Run with a Python that has kokoro-onnx installed:
    KOKORO_MODEL=/path/kokoro-v1.0.onnx KOKORO_VOICES=/path/voices-v1.0.bin /path/to/venv/bin/python src/vo_scratch.py
Optional: KOKORO_VOICE (default am_fenrir), KOKORO_SPEED (default 1.1).
Piper instead (the first scratch read used en_US-lessac-high):
    PIPER_MODEL=/path/en_US-lessac-high.onnx /path/to/venv/bin/python src/vo_scratch.py
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from timeline import DURATION, LINES  # noqa: E402

SR = 48000
# Spoken spelling where the caption spelling would be misread.
SAY = {"Lynkk": "Link", "lynkk.ai": "link dot A I"}
FASTEST = 0.82  # don't push the duration scale below this; it starts to sound rushed


def spoken(text):
    for k, v in SAY.items():
        text = re.sub(re.escape(k) + r"(?=[\s.,]|$)", v, text)
    return text


def piper_engine(model):
    from piper import PiperVoice, SynthesisConfig

    voice = PiperVoice.load(model)

    def synth(text, scale):
        pcm, phonemes = [], []
        for c in voice.synthesize(text, syn_config=SynthesisConfig(length_scale=scale, noise_scale=0.6, noise_w_scale=0.7)):
            pcm.append(c.audio_float_array)
            phonemes += c.phonemes
            sr = c.sample_rate
        return np.concatenate(pcm), sr, phonemes

    return synth


def kokoro_engine(model, voices, name, speed):
    from kokoro_onnx import Kokoro

    kokoro = Kokoro(model, voices)

    def synth(text, scale):
        pcm, sr = kokoro.create(text, voice=name, speed=speed / scale, lang="en-us")
        return np.asarray(pcm, np.float32), sr, list(kokoro.tokenizer.phonemize(text, "en-us"))

    return synth


def trim(x, sr, thresh=0.02):
    """Bounds of the speech-active region."""
    env = np.convolve(np.abs(x), np.ones(sr // 100) / (sr // 100), mode="same")
    idx = np.where(env > thresh * env.max())[0]
    return idx[0], idx[-1]


def word_times(caption, phonemes, t0, t1):
    """Spread the caption's words over [t0, t1] by phoneme count (pauses go to the word before them)."""
    groups, cur = [], 0
    for p in phonemes:
        if p == " ":
            groups.append(cur)
            cur = 0
        else:
            cur += 1 if p not in "ˈˌ" else 0
    groups.append(cur)
    words = caption.split(" ")
    # Spoken and caption words don't line up ("link dot A I", "half-listening"): weight by letters instead.
    if len(groups) != len(words):
        groups = [len(re.sub(r"[^a-z]", "", w.lower())) + 1 for w in words]
    total = sum(groups)
    out, t = [], t0
    for w, g in zip(words, groups):
        out.append({"w": w, "t": round(t, 3)})
        t += (t1 - t0) * g / total
    return out


def main():
    if "KOKORO_MODEL" in os.environ:
        synth = kokoro_engine(os.environ["KOKORO_MODEL"], os.environ["KOKORO_VOICES"],
                              os.environ.get("KOKORO_VOICE", "am_fenrir"), float(os.environ.get("KOKORO_SPEED", "1.1")))
    else:
        synth = piper_engine(os.environ["PIPER_MODEL"])
    bus = np.zeros(int(DURATION * SR), np.float32)
    timing = []
    for i, line in enumerate(LINES):
        start, end, caption = line[0], line[1], line[2]
        nxt = LINES[i + 1][0] if i + 1 < len(LINES) else DURATION - 0.6
        room = min(end + 0.35, nxt - 0.12) - start  # a little spill past the planned end is fine
        scale = 1.0
        x, sr, ph = synth(spoken(caption), scale)
        a, b = trim(x, sr)
        if (b - a) / sr > room:
            scale = max(FASTEST, scale * room / ((b - a) / sr))
            x, sr, ph = synth(spoken(caption), scale)
            a, b = trim(x, sr)
        speech = x[a : b + 1]
        # resample to the mix rate
        speech = np.interp(np.linspace(0, len(speech) - 1, int(len(speech) * SR / sr)), np.arange(len(speech)), speech)
        fade = min(len(speech), SR // 200)
        speech[:fade] *= np.linspace(0, 1, fade)
        speech[-fade:] *= np.linspace(1, 0, fade)
        d = len(speech) / SR
        i0 = int(start * SR)
        bus[i0 : i0 + len(speech)] += speech[: len(bus) - i0]
        timing.append({"start": start, "end": round(start + d, 3), "text": caption,
                       "words": word_times(caption, ph, start, start + d), "duration_scale": round(scale, 3)})
        flag = "  OVER" if start + d > nxt - 0.05 else ""
        print(f"{start:6.2f}-{start + d:6.2f}  (planned end {end:5.2f}, scale {scale:.2f}){flag}  {caption}")

    bus /= max(1e-9, np.abs(bus).max() / 0.9)
    out = HERE / "assets" / "vo.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                    "-af", "highpass=f=80,acompressor=threshold=-18dB:ratio=3:attack=5:release=80", str(out)],
                   input=bus.tobytes(), check=True)
    (HERE / "vo_timing.json").write_text(json.dumps(timing, indent=1))
    print("wrote", out)


if __name__ == "__main__":
    main()
