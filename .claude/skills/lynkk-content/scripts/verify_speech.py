"""Check a voiceover or final mix by transcribing it and diffing against the script.

Use it because you cannot listen: it catches blurred words ("you've forgotten" heard as "you forgot"),
merged words ("and during" heard as "enduring") and voice buried under music.
Usage: python verify_speech.py <audio-or-video> <lines.json>
Setup: pip install faster-whisper soundfile (downloads the small.en model on first run).
"""
import difflib
import json
import re
import subprocess
import sys
import tempfile

import soundfile as sf
from faster_whisper import WhisperModel

media, lines_path = sys.argv[1:3]
with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", media, "-vn", "-ar", "16000", "-ac", "1", tmp.name], check=True)
    audio, _ = sf.read(tmp.name, dtype="float32")
model = WhisperModel("small.en", device="cpu", compute_type="int8")
heard = " ".join(s.text for s in model.transcribe(audio)[0])
script = " ".join(t for _, _, t in json.load(open(lines_path)))
norm = lambda s: re.sub(r"[^a-z' ]", " ", s.lower()).split()
ref, hyp = norm(script), norm(heard)
sm = difflib.SequenceMatcher(None, ref, hyp)
print(f"word match {sm.ratio():.3f}")
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op != "equal":
        print(f"  script: {' '.join(ref[i1:i2])!r:40} heard: {' '.join(hyp[j1:j2])!r}")
print("heard:", heard.strip())
