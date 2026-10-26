---
name: lynkk-content
description: Make Lynkk (lynkk.ai) marketing content in the lynkk.ai design kit, including short vertical or landscape videos with music, sound effects and voiceover, and still images such as social posts, thumbnails, link previews and blog headers. Use for any Lynkk video, reel, launch video, ad, explainer, social image, poster or thumbnail, and together with /brag or /brag-slim when the brag skill is used for Lynkk.
---

# Lynkk content

Everything Lynkk makes should look like lynkk.ai, show the real product, and be easy for anyone to understand.
This skill holds the brand kit, the tools, and what was learned making `launch/video-1/` and `launch/video-2/`.

## Always

- Spell it **Lynkk** (voiceover text: "Link"). No em dashes or en dashes. Plain everyday words.
- Use the lynkk.ai kit: `references/brand-kit.md` (tokens, type, components, logo, studio backdrop, demo account).
- Show the real product. Capture UI from lynkk.ai with `scripts/capture_ui.mjs` rather than mocking it; swap only small illustrative text.
- Use the site's own lines and the demo account (Corvane Logistics, Priya Shah, Jamie Davis). Never invent product claims, stats or testimonials.
- You cannot hear audio or watch video: check stills (`render.mjs preview`), waveforms, loudness, and run `scripts/verify_speech.py` on anything with a voice.

## Videos

Read `references/video.md`. In short:
1. **Plan** in `brag-output/brag-plan.md` with the brag rubric; choose tempo first (120 BPM = cuts on whole seconds).
2. **Capture** real UI (stills and frame sequences) into `brag-output/work/`.
3. **Build** scenes from `templates/scene-starter.html`; preview stills of every scene and mid-animation; fix; render frames.
4. **Score** with `scripts/music_example.py` (music + in-key SFX on the grid, one piece).
5. **Voice** with `scripts/voiceover.py` (Kokoro: `af_heart` female, `am_fenrir` male); verify with `scripts/verify_speech.py`.
6. **Mix** with `scripts/mix.sh` (ducking, -14 LUFS), bake the poster as frame 0 with `scripts/poster.sh`, write `share-copy.txt`.

When the user also asks for /brag or /brag-slim: brag owns the creative rules (hook, show the thing, readable holds, beat-synced cuts,
poster, share copy); this skill owns the look, the tools and the Lynkk facts. If the user's own script or length differs from brag's
defaults (15-25s, landscape), the user's choice wins; say so in the plan.

## Images

Read `references/images.md`. Start from `templates/image-starter.html`, set the size, build, `render.mjs still`, look at the result.

## Files

| Path | What |
|---|---|
| `references/brand-kit.md` | lynkk.ai colors, type, components, copy lines, demo data, where the real UI lives on the site |
| `references/video.md` | the full video workflow with commands and pitfalls |
| `references/images.md` | sizes and recipe for still images |
| `templates/scene-starter.html` | scene engine (night/day scenes, animations, helpers, canvas frame sequences) |
| `templates/image-starter.html` | one-frame layout for social images |
| `assets/logo.svg`, `assets/fonts/` | Lynkk mark (currentColor) and Schibsted Grotesk |
| `scripts/capture_ui.mjs` | capture real UI from lynkk.ai: stills, text swaps, deterministic frame sequences |
| `scripts/build.py` | inline the logo and fonts into a page |
| `scripts/render.mjs` | preview sheets, stills, and MP4 frames |
| `scripts/music_example.py` | synthesized music + SFX arrangement to copy and re-arrange |
| `scripts/voiceover.py` | Kokoro voiceover timed to scenes |
| `scripts/verify_speech.py` | transcribe and diff against the script |
| `scripts/mix.sh`, `scripts/poster.sh` | final mix and poster frame 0 |

Tools needed: Node + Playwright (Chromium), ffmpeg, Python 3 with numpy; for voice: kokoro-onnx, soundfile; for checks: faster-whisper.
