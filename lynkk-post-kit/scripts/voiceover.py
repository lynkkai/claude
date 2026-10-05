"""Voiceover and sound for a video post.

    python3 scripts/voiceover.py posts/my-video --model /path/to/kokoro-multi-lang-v1_0

Reads posts/<name>/video.json (lines, start times, voice, sound effects),
speaks each line with the Kokoro TTS model through sherpa-onnx, places it at
its start time, adds light synthesized sound effects, and writes
posts/<name>/out/mix.wav (48 kHz, loudness-normalised for social, -14 LUFS).
Each line is also kept as out/vo/<id>.wav.

Setup (once):
    pip install sherpa-onnx soundfile numpy
    curl -LO https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/kokoro-multi-lang-v1_0.tar.bz2
    tar xjf kokoro-multi-lang-v1_0.tar.bz2

US English voices in that model: 0 to 10 are women (3 is af_heart), 11 to 19
are men (16 is am_michael). A line in video.json can set its own "speaker"
(and "speed") for a second character; otherwise it uses "voice". Write "Lynk" in a line to make the voice say
Lynkk right; the slides keep the real spelling.
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

RATE = 24000


def speak(cfg, model, out_dir):
    import sherpa_onnx

    m = Path(model)
    tts = sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
        kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(
            model=str(m / "model.onnx"), voices=str(m / "voices.bin"), tokens=str(m / "tokens.txt"),
            data_dir=str(m / "espeak-ng-data"), lexicon=f"{m / 'lexicon-us-en.txt'},{m / 'lexicon-zh.txt'}", lang="en-us"),
        num_threads=4)))
    voice = cfg["voice"]
    clips = {}
    for line in cfg["lines"]:
        # A line can set its own "speaker" and "speed" (a second character), else the post's voice.
        audio = tts.generate(line["text"], sid=line.get("speaker", voice["speaker"]), speed=line.get("speed", voice.get("speed", 1.0)))
        samples = np.asarray(audio.samples, dtype=np.float32)
        sf.write(out_dir / f"{line['id']}.wav", samples, audio.sample_rate)
        clips[line["id"]] = samples
        print(f"  {line['id']}  {line['at']:5.2f}s  +{len(samples) / RATE:4.2f}s  {line['text']}")
    return clips


# Sound effects, synthesized so the kit needs no audio assets. Kept quiet: the voice leads.
rng = np.random.default_rng(7)


def env(n, attack, decay):
    t = np.arange(n) / RATE
    return np.minimum(1, t / max(attack, 1e-4)) * np.exp(-t / decay)


def click():
    n = int(0.03 * RATE)
    noise = rng.standard_normal(n)
    hp = np.diff(noise, prepend=0)  # brighter, like a key
    return (hp * env(n, 0.0005, 0.004) * 0.22).astype(np.float32)


def whoosh():
    n = int(0.45 * RATE)
    noise = rng.standard_normal(n)
    # Moving average with a sweeping width: a soft low-to-high swish.
    out = np.zeros(n)
    acc = np.cumsum(noise)
    for i in range(n):
        w = int(40 - 34 * i / n) + 1
        out[i] = (acc[i] - acc[max(0, i - w)]) / w
    shape = np.sin(np.pi * np.arange(n) / n) ** 2
    return (out * shape * 0.35).astype(np.float32)


def pop():
    n = int(0.09 * RATE)
    t = np.arange(n) / RATE
    f = 900 - 500 * t / t[-1]
    return (np.sin(2 * np.pi * np.cumsum(f) / RATE) * env(n, 0.002, 0.02) * 0.18).astype(np.float32)


def tick():
    n = int(0.05 * RATE)
    t = np.arange(n) / RATE
    return (np.sin(2 * np.pi * 1600 * t) * env(n, 0.001, 0.012) * 0.08).astype(np.float32)


def place(track, clip, at):
    i = int(at * RATE)
    j = min(len(track), i + len(clip))
    if i < len(track):
        track[i:j] += clip[: j - i]


def main():
    args = sys.argv[1:]
    if not args or "--model" not in args:
        print(__doc__)
        sys.exit(2)
    post = Path(args[0])
    model = args[args.index("--model") + 1]
    cfg = json.loads((post / "video.json").read_text())
    out = post / "out"
    vo_dir = out / "vo"
    vo_dir.mkdir(parents=True, exist_ok=True)

    clips = speak(cfg, model, vo_dir)
    track = np.zeros(int(cfg["duration"] * RATE), dtype=np.float32)
    for line in cfg["lines"]:
        place(track, clips[line["id"]], line["at"])

    sfx = cfg.get("sfx", {})
    for a, b in sfx.get("typing", []):
        t = a
        while t < b:
            place(track, click() * rng.uniform(0.6, 1.0), t)
            t += rng.uniform(0.07, 0.19)
    for at in sfx.get("whoosh", []):
        place(track, whoosh(), at - 0.2)
    for at in sfx.get("pop", []):
        place(track, pop(), at)
    for at in sfx.get("tick", []):
        place(track, tick(), at)

    raw = out / "mix-raw.wav"
    sf.write(raw, track, RATE)
    mix = out / "mix.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw),
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-ac", "2", str(mix)], check=True)
    raw.unlink()
    print(f"  wrote {mix}")


if __name__ == "__main__":
    main()
