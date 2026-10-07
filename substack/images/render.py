#!/usr/bin/env python3
"""Render banner HTML sources in substack/images/src/ to PNGs with headless Chromium.

Usage: python3 substack/images/render.py   (needs Pillow and Chromium at /opt/pw-browsers or $CHROME)
"""
import glob, os, pathlib, subprocess, tempfile
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME") or sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))[-1]
SIZES = [(1456, 1048), (1200, 630)]  # Substack post/social preview (14:10), wide link preview (1.91:1)
NAMES = {"01-banner": "01-your-ai-notetaker-shows-up-too-late"}

for src in sorted((HERE / "src").glob("*.html")):
    name = NAMES.get(src.stem, src.stem)
    for w, h in SIZES:
        out = HERE / f"{name}-{w}x{h}.png"
        with tempfile.NamedTemporaryFile(suffix=".png") as tmp:
            subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                            "--force-device-scale-factor=1", f"--window-size={w},{h + 300}",
                            "--virtual-time-budget=2000", f"--screenshot={tmp.name}",
                            f"{src.as_uri()}?w={w}&h={h}"], check=True, capture_output=True)
            Image.open(tmp.name).crop((0, 0, w, h)).save(out, optimize=True)
        print("wrote", out.relative_to(HERE.parent.parent))
