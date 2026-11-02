# Cover image generator

Builds 1200x630 blog/Medium cover images from the **live lynkk.ai design kit**, rendered at 2x
(2400x1260) with headless Chromium.

## Run

```bash
python3 -I build.py && node shoot.js
```

Output lands in `out/<slug>.png`. Copy into `content/blog/images/<slug>/cover.png`.

## Where the design tokens came from

Extracted on 2026-11-02 from the CSS chunks served at lynkk.ai (`/_next/static/chunks/*.css`),
specifically the `--lk-*` and `--gr-*` custom properties. The values are hard-coded in the `T`
dict at the top of `build.py`:

| Token | Value | Source |
|---|---|---|
| ink | `#151514` | `--lk-ink` |
| ink-2 / ink-3 | `#6c6c6a` / `#a3a3a1` | `--lk-gray-600` / `--lk-gray-400` |
| background | `#f5f5f4` | `--lk-gray-50` (`--lk-bg`) |
| surface / fill | `#ffffff` / `#f0f0ef` | `--lk-gray-0` / `--lk-gray-100` |
| line / line-soft | `#e6e6e4` / `#efefed` | `--lk-line` / `--lk-line-soft` |
| accent violet | `#7063be` | `--gr-violet` (`--lk-accent`) |
| violet tint / soft | `#e2e0f2` / `#b4abe0` | `--gr-violet-tint` / `--gr-violet-soft` |
| live red | `#e5484d` | `--lk-live-500` |
| sand / stone | `#ece9e2` / `#dbdad6` | `--gr-sand` / `--gr-stone` |
| radius (window/card/pill) | 24 / 10 / 20 px | `--gr-r-window` / `--gr-r-card` / `--gr-r-pill` |
| dot grid | `#11111108` at 7.3px | `--gr-dot` / `--gr-dot-pitch` |
| tracking snug / tight | -.02em / -.04em | `--gr-track-snug` / `--gr-track-tight` |
| display font | Schibsted Grotesk 700 | `--font-round` |
| body font | Inter | `--gr-font` |
| mono | JetBrains Mono | `--gr-mono` |

**If the site's tokens change, re-extract rather than trusting this table.**

## Known gaps

- **No logo file.** The wordmark is set in Schibsted Grotesk as live type, with the accent dot in
  violet. It is an approximation of the site's treatment, not the real asset. Swap in the actual
  logo when brand provides one (it is still on the "to confirm" list in `memory/lynkk-brand.md`).
- Fonts load from Google Fonts at render time, so rendering needs network access.
- Each cover's illustration is hand-built SVG/HTML per article, not a reusable template. Adding a
  fifth cover means writing a fifth `art` block.
