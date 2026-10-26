# Lynkk brand kit (from lynkk.ai)

Pulled from the live lynkk.ai CSS on 2026-10-23. When in doubt, re-check the site: it is the source of truth.
Brand facts, positioning and submission copy: `memory/lynkk-brand.md` in the repo.

## Name and voice

- Always **Lynkk** (double k). Domain **lynkk.ai**. Never Lynk, Linnk, Link AI.
- In voiceover text write **"Link"** so text-to-speech says it right.
- No em dashes or en dashes anywhere (repo rule). Use commas, colons, parentheses, or two sentences.
- Plain, short, everyday words. If a 15-year-old wouldn't get it, rewrite it. Say "sales records" out loud, keep "CRM" for hashtags.
- Use the site's own lines before inventing new ones. Good ones:
  "Your revenue lives in your conversations. Don't lose it." · "The call ends. The opportunity shouldn't." ·
  "The deal didn't go cold. The context did." · "The CRM tells one story. Your customer told another. The gap shows up in your forecast." ·
  "Every item links back to the call." · "Help on your screen during the call." · "One call on your screen. Every conversation in your corner." ·
  "Make every conversation count." · CTAs: "Start free", "Book a demo", "See how it works". Proof row: "No credit card · 15+ languages · Online + in person".

## Color tokens

| Token | Hex | Use |
|---|---|---|
| night | `#111` (`--gr-black`) | dark sections, problem act, end cards |
| coal / coal-2 | `#171717` / `#1e1e21` | product windows and tiles on night |
| rule-night | `#292c31` | hairlines on night |
| ink-night / muted-night | `#fff` / `#ffffff80` | text on night; second headline line |
| day | `#f5f5f4` | light sections, fix act |
| white | `#fff` | cards on day |
| ink / muted / faint | `#151514` / `#6c6c6a` / `#a3a3a1` | text on day; second headline line uses faint |
| rule-day | `#e0e3e9` | hairlines on day |
| violet | `#7063be` | the accent: pill tag text on day, rings, small labels |
| violet-tint | `#e2e0f2` | pill tag background on day |
| violet-deep / violet-soft | `#231f3a` / `#b4abe0` | pill tag on night |
| lavender | `#beb4fb` | speaking-tile ring, highlights on night |
| live | `#ff3b30` | REC dot, "wrong", losses (use sparingly) |
| forest / leaf | `#235634` / `#93b45c` | success: checkmarks, "Sent", "Saved" |
| pink | `#f7b7ef` | avatar for Priya (PS) |
| sand | `#ece9e2` | sticky notes, quiet surfaces |

Studio backdrop behind product shots (sampled from the lynkk.ai hero): cream `#f9f6f1` → `#ede8db` → rose `#af816e` → brown `#875c46` → amber `#aa783c`.
Dot grid: `radial-gradient(#ffffff10 1.6px, transparent 2px) 0 0/18px 18px` on night, `#1111110b` on day. Thin vertical frame lines 44px in from each edge.

## Type

- **Headlines:** Inter 500, tracking about -0.045em, tight leading (1.05). Two-tone: first line in ink, second line in muted, on its own line.
  This is the site's signature ("The deal didn't go cold. / The context did.").
- **UI and body:** Schibsted Grotesk 400/500/600 (bundled in `assets/fonts/`). Inter is usually installed; otherwise load from Google Fonts.
- **Timestamps / numbers:** tabular figures; the product uses JetBrains Mono for call timestamps like `18:42`.
- No serif accents on lynkk.ai work (the older revenue-story page used Georgia italic; lynkk.ai does not).

## Components

- **Pill tag:** fully rounded, Inter 500, violet on violet-tint (day) or violet-soft on violet-deep (night). Used as the scene label.
- **Buttons:** small radius (5px on site, about 10-12px at video scale). Solid white on night, solid ink on day. Secondary: coal with a hairline.
- **Product window:** coal surface, 2px rule-night border, 28px radius, a bar with three dots or a red live dot and "REC".
- **Toast:** white card, 20px radius, icon square (leaf green for tasks, violet-tint for mail/links), bold line plus muted line. Site examples:
  "Nothing slips through. 3 action items · 2 commitments", "Follow-up, ready when you ask. Grounded in what was actually said."
- **Logo:** striped circle mark (`assets/logo.svg`, `fill=currentColor`) plus the word "Lynkk" in Inter 500, gap about 0.3em.

## Illustrative data (use the site's own demo account)

Corvane Logistics (freight and fulfilment) · Priya Shah, VP Engineering (avatar PS, pink) · Jamie Davis, you (JD, leaf green) ·
Corvane IT signs off first (21:30) · budget from $30K in discovery to $50K for a phased rollout (18:42) · 15-person pilot agreed Oct 13.
Never use real customer names, emails or private data. Mark product shots "Illustrative" in ads if needed.

## Real product UI worth capturing from lynkk.ai (`scripts/capture_ui.mjs`)

| What | Scroll (1440x900) | Clip | Notes |
|---|---|---|---|
| Cue answering live in Google Meet | 8500 | x400 y178 w640 h470 | animated; capture as a `sequence` (30 fps, 5 s) |
| Sales Call note "Corvane Logistics · Commercials" | 17000 | x108 y167 w432 h480 | static; swap row text with `replace` |
| Hero product preview (Corvane workspace) | 900 | find by text "Nothing slips through" | toast + call summary |

The site animates on scroll; positions can drift when it is redesigned. Always look at a capture before using it.
