"""Builds the soundtrack from timeline.json and muxes it with work/video.mp4 into brag.mp4.

Music: muffled (low-passed) under the typing, opens up on the reveal. Keystrokes stop dead at the cut.
Drop a recorded VO at src/assets/vo.wav and it is mixed in with the music ducked underneath.
"""
import json
import re
import subprocess
from pathlib import Path

import numpy as np

SR = 48000
HERE = Path(__file__).parent
ROOT = HERE.parent
WORK = ROOT / "work"
A = HERE / "assets"
TL = json.loads((HERE / "timeline.json").read_text())


def load(path, extra=()):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), *extra, "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).copy()


def word_t(line, prefix):
    for w in TL["lines"][line]["words"]:
        if re.sub(r"[^a-z]", "", w["w"].lower()).startswith(prefix):
            return w["t"]
    raise KeyError(prefix)


def ramp(n, pts):
    """Piecewise-linear gain envelope from [(time, gain), ...]."""
    t = np.arange(n) / SR
    xs, ys = zip(*pts)
    return np.interp(t, xs, ys).astype(np.float32)[:, None]


def place(bus, clip, t, gain=1.0, pan=0.0):
    i = int(t * SR)
    if i >= len(bus):
        return
    seg = clip[: len(bus) - i] * gain
    seg = seg * np.array([1 - max(0, pan), 1 + min(0, pan)], dtype=np.float32)
    bus[i : i + len(seg)] += seg


def main():
    dur = TL["duration"]
    n = int(dur * SR)
    S = TL["scenes"]
    reveal = S["reveal"][0]

    full = load(A / "music.mp3")[:n]
    muffled = load(A / "music.mp3", ["-af", "lowpass=f=700,lowpass=f=700"])[:n]
    open_up = ramp(n, [(0, 0), (reveal - 0.05, 0), (reveal + 0.55, 1), (dur, 1)])
    music = muffled * (1 - open_up) * 0.9 + full * open_up
    music *= ramp(n, [(0, 0.0), (0.08, 0.32), (reveal - 0.05, 0.32), (reveal + 0.55, 0.5), (dur - 1.3, 0.5), (dur, 0)])

    sfx = np.zeros((n, 2), np.float32)
    keys = [load(A / "sfx" / f"keypress-{i:03d}.wav") for i in range(1, 13)]
    rng = np.random.default_rng(3)
    for k in TL["keys"]:
        g = 0.75 if k["c"] in "\n<" else 0.55
        place(sfx, keys[k["s"]], k["t"], g * rng.uniform(0.8, 1.1), rng.uniform(-0.25, 0.25))

    snd = lambda name: load(A / "sfx" / name)
    place(sfx, snd("impactSoft_medium_001.ogg"), 12.02, 0.9)
    for t in [word_t(5, "summary"), word_t(5, "decisions"), word_t(5, "action"), word_t(6, "transcript")]:
        place(sfx, snd("click_003.ogg"), t - 0.12, 0.5)
    place(sfx, snd("bong_001.ogg"), word_t(8, "pain"), 0.5)
    place(sfx, snd("impactSoft_heavy_003.ogg"), S["punch"][0], 0.55)
    place(sfx, snd("impactBell_heavy_000.ogg"), 35.47, 0.35)
    place(sfx, snd("click2.ogg"), 36.56, 0.45)

    mix = music + sfx
    vo_path = A / "vo.wav"
    if vo_path.exists():
        vo = load(vo_path)[:n]
        vo = np.pad(vo, ((0, n - len(vo)), (0, 0)))
        env = np.convolve(np.abs(vo).mean(1), np.ones(SR // 10) / (SR // 10), mode="same")
        # about -12 dB of music under speech, with a 250ms release so it doesn't pump between words
        env = np.clip(env / (env.max() * 0.2 + 1e-9), 0, 1)
        tail = np.convolve(env, np.ones(SR // 4) / (SR // 4), mode="full")[:n]  # trailing average = release
        duck = 1 - 0.75 * np.clip(np.maximum(env, tail), 0, 1)
        # set the voice ~11 dB over the ducked bed while it speaks, whatever the source level
        bed = music * duck[:, None] + sfx
        talk = env > 0.5
        rms = lambda x: np.sqrt((x[talk] ** 2).mean()) + 1e-9
        mix = bed + vo * (rms(bed) * 10 ** (11 / 20) / rms(vo))

    mix /= max(1e-9, np.abs(mix).max() / 0.89)
    WORK.mkdir(exist_ok=True)
    wav = WORK / "mix.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-",
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", str(SR), str(wav)],
                   input=mix.astype(np.float32).tobytes(), check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(WORK / "video.mp4"), "-i", str(wav),
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart",
                    str(WORK / "brag-noposter.mp4")], check=True)
    print("wrote", WORK / "brag-noposter.mp4")


if __name__ == "__main__":
    main()
