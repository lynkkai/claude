import os

# ============================================================================
# Lynkk design kit, extracted from lynkk.ai CSS 2026-11-02.
# The marketing site runs the "grid" token set (data-tokens=grid); its dark
# variant is html[data-ds=round][data-tokens=grid].dark / .theme-dark.
# ============================================================================
LIGHT = dict(
    theme="light",
    ink="#151514", ink2="#6c6c6a", ink3="#a3a3a1",
    bg="#f5f5f4", surface="#ffffff", fill="#f0f0ef",
    line="#e6e6e4", line_soft="#efefed",
    accent_text="#7063be", accent="#7063be",
    accent_bed="#e2e0f2", accent_edge="#b4abe0",
    live="#e5484d", live_text="#e5484d", live_bed="#e5484d14",
    table="#ece9e2", table_edge="#dbdad6",
    dot="#11111108",
    shadow="0 14px 34px -12px #00000059",
    hairline="transparent",
)
# Dark: --lk-bg:#111, --lk-surface:#171717, --lk-fill:#1d1d1d,
# --lk-line:#292c31, --lk-line-soft:#1f2125, --lk-ink:#fff,
# --lk-ink-2:#ffffff80, --lk-ink-3:#ffffff57, --gr-ring:#ffffff1a
DARK = dict(
    theme="dark",
    ink="#ffffff", ink2="#ffffff80", ink3="#ffffff57",
    bg="#111111", surface="#171717", fill="#1d1d1d",
    line="#292c31", line_soft="#1f2125",
    accent_text="#beb4fb",          # --gr-lavender, legible on near-black
    accent="#7063be",               # --gr-violet, for fills
    accent_bed="#231f3a",           # --gr-violet-deep
    accent_edge="#b4abe0",          # --gr-violet-soft
    live="#ff6157", live_text="#ff8a82", live_bed="#ff615714",
    table="#2e2e2e", table_edge="#292c31",   # --gr-coal-3 / --gr-rule-night
    dot="#ffffff0a",
    shadow="0 18px 44px -14px #00000099",
    hairline="#ffffff1a",           # --gr-ring
)

SHELL = """<!doctype html>
<html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Schibsted+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+Devanagari:wght@400;500&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1200px; height:630px; }}
  body {{
    font-family:"Inter",ui-sans-serif,system-ui,sans-serif;
    background:{bg};
    background-image:radial-gradient({dot} 1px, transparent 1px);
    background-size:7.3px 7.3px;
    color:{ink}; -webkit-font-smoothing:antialiased;
    display:flex; flex-direction:column; justify-content:space-between;
    padding:48px 60px 44px;
  }}
  .eyebrow {{
    font-size:12px; line-height:1.5; font-weight:600; letter-spacing:.08em;
    text-transform:uppercase; color:{accent_text};
    display:flex; align-items:center; gap:10px;
  }}
  .eyebrow .mark {{ width:7px; height:7px; border-radius:999px; background:{accent_text}; }}
  h1 {{
    font-family:"Schibsted Grotesk","Inter",sans-serif;
    font-weight:700; font-size:50px; line-height:1.2; letter-spacing:-.04em;
    max-width:15ch;
  }}
  .sub {{ font-size:18px; line-height:1.5; color:{ink2}; max-width:46ch; margin-top:14px; }}
  .foot {{ display:flex; align-items:center; justify-content:space-between; }}
  .brand {{
    font-family:"Schibsted Grotesk","Inter",sans-serif;
    font-weight:700; font-size:20px; letter-spacing:-.02em;
  }}
  .brand span {{ color:{accent_text}; }}
  .top {{ display:flex; gap:52px; align-items:center; justify-content:space-between; flex:1 1 auto; }}
  .copy {{ flex:1 1 0; min-width:0; }}
  .art {{ flex:0 0 448px; }}
  .panel {{
    background:{surface}; border:1px solid {line}; border-radius:24px;
    box-shadow:{shadow}, inset 0 1px 0 {hairline}; padding:20px;
  }}
  .mono {{ font-family:"JetBrains Mono",ui-monospace,monospace; }}
</style></head><body>
<div class="top">
  <div class="copy">
    <div class="eyebrow"><span class="mark"></span>{eyebrow}</div>
    <h1 style="margin-top:18px">{title}</h1>
    <div class="sub">{sub}</div>
  </div>
  <div class="art">{art}</div>
</div>
<div class="foot">
  <div class="brand">Lynkk<span>.</span></div>
  <div style="font-size:13px;color:{ink3}">lynkk.ai</div>
</div>
</body></html>"""


def arts(T):
    seats = ""
    for cx, cy in [(96, 80), (216, 80), (96, 214), (216, 214)]:
        seats += (f'<circle cx="{cx}" cy="{cy}" r="18" fill="{T["fill"]}" '
                  f'stroke="{T["line"]}" stroke-width="1.5"/>')
    a1 = f"""<div class="panel" style="padding:24px">
<svg width="400" height="300" viewBox="0 0 320 294">
  <circle cx="207" cy="147" r="48" fill="{T['accent_bed']}" opacity=".9"/>
  <rect x="70" y="110" width="180" height="74" rx="12" fill="{T['table']}" stroke="{T['table_edge']}" stroke-width="1.5"/>
  {seats}
  <circle cx="207" cy="147" r="76" fill="none" stroke="{T['accent_edge']}" stroke-width="1.5" stroke-dasharray="4 5"/>
  <circle cx="207" cy="147" r="104" fill="none" stroke="{T['accent']}" stroke-width="1.5"/>
  <rect x="196" y="130" width="22" height="34" rx="5" fill="{T['ink']}"/>
  <rect x="200.5" y="134.5" width="13" height="21" rx="2.5" fill="{T['accent']}"/>
  <circle cx="207" cy="159.5" r="1.6" fill="{T['bg']}"/>
</svg>
<div style="display:flex;gap:18px;margin-top:2px;font-size:12px;color:{T['ink2']}">
  <span style="display:flex;align-items:center;gap:7px"><span style="width:9px;height:9px;border-radius:2px;background:{T['ink']}"></span>Recorder</span>
  <span style="display:flex;align-items:center;gap:7px"><span style="width:9px;height:9px;border-radius:999px;background:{T['accent_bed']};border:1px solid {T['accent_edge']}"></span>Pickup range</span>
</div></div>"""

    rows = ""
    for initials, name in [("PR", "Priya Raman"), ("NK", "Neha Kapoor"), ("JM", "Jamie Mitchell")]:
        rows += f"""<div style="display:flex;align-items:center;gap:13px;padding:11px 13px;border-radius:10px">
      <div style="width:34px;height:34px;border-radius:999px;background:{T['fill']};border:1px solid {T['line']};
        display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:{T['ink2']}">{initials}</div>
      <div style="font-size:14px;font-weight:500">{name}</div>
    </div>"""
    a2 = f"""<div class="panel" style="padding:14px">
  <div style="font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:{T['ink3']};padding:8px 13px 10px">Participants &middot; 4</div>
  {rows}
  <div style="display:flex;align-items:center;gap:13px;padding:11px 13px;border-radius:10px;
      background:{T['live_bed']};border:1px dashed {T['live']}">
    <div style="width:34px;height:34px;border-radius:999px;background:{T['surface']};border:1px dashed {T['live']};
      display:flex;align-items:center;justify-content:center">
      <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="{T['live']}" stroke-width="2" stroke-linecap="round">
        <rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 8V4"/>
        <circle cx="9" cy="14" r="1.4" fill="{T['live']}" stroke="none"/><circle cx="15" cy="14" r="1.4" fill="{T['live']}" stroke="none"/>
      </svg>
    </div>
    <div>
      <div style="font-size:14px;font-weight:500;color:{T['live_text']}">Priya's Notetaker</div>
      <div style="font-size:11.5px;color:{T['ink2']};margin-top:1px">Joined the meeting</div>
    </div>
  </div>
</div>"""

    def field(label, value):
        return f"""<div style="padding:11px 0;border-bottom:1px solid {T['line_soft']}">
      <div style="font-size:10.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:{T['ink3']}">{label}</div>
      <div style="font-size:14px;margin-top:5px;color:{T['ink']}">{value}</div></div>"""
    a3 = f"""<div class="panel" style="padding:22px 24px">
  {field("Account", "Corvane Logistics")}
  {field("Stage", "Proposal")}
  {field("Value", "$50,000")}
  <div style="padding:11px 0 0">
    <div style="font-size:10.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:{T['ink3']}">Call notes</div>
    <div style="margin-top:7px;height:92px;border:1px solid {T['line']};border-radius:10px;
        background:{T['bg']};padding:11px 12px;position:relative">
      <div style="font-size:13.5px;color:{T['ink2']}">good call, sending proposal</div>
      <div style="position:absolute;left:12px;top:34px;width:1.5px;height:15px;background:{T['accent_text']}"></div>
    </div>
  </div>
</div>"""

    hi = (f'<span style="background:{T["accent_bed"]};border-radius:4px;padding:1px 4px">'
          'Budget to approve ho gaya hai,</span>')
    a4 = f"""<div class="panel" style="padding:22px 24px">
  <div style="display:flex;align-items:center;gap:9px;font-size:11px;color:{T['ink3']}">
    <span class="mono" style="color:{T['accent_text']}">14:22</span>
    <span style="width:4px;height:4px;border-radius:999px;background:{T['ink3']}"></span>
    <span>Priya Raman</span>
  </div>
  <div style="font-size:19px;line-height:1.62;margin-top:12px;letter-spacing:-.02em">
    {hi} but procurement will take three weeks, so kickoff first week of December.
  </div>
  <div style="display:flex;gap:16px;margin-top:18px;padding-top:15px;border-top:1px solid {T['line_soft']};font-size:11.5px;color:{T['ink2']}">
    <span style="display:flex;align-items:center;gap:7px"><span style="width:10px;height:10px;border-radius:3px;background:{T['accent_bed']};border:1px solid {T['accent_edge']}"></span>Hinglish</span>
    <span style="display:flex;align-items:center;gap:7px"><span style="width:10px;height:10px;border-radius:3px;background:{T['surface']};border:1px solid {T['line']}"></span>English</span>
    <span style="margin-left:auto;color:{T['accent_text']};font-weight:600">1 switch</span>
  </div>
</div>"""
    return a1, a2, a3, a4


def covers(T):
    a1, a2, a3, a4 = arts(T)
    return [
      ("2026-11-02-ai-note-taker-in-person-meetings", "In-person capture",
       "The meeting with no link",
       "Why room audio is a different problem, and where to put the microphone.", a1),
      ("2026-11-02-bot-free-ai-note-takers", "Bot-free capture",
       "Something joined your call",
       "A notetaker bot is a product decision, not a law of physics.", a2),
      ("2026-11-02-crm-graveyard-call-notes", "CRM hygiene",
       "Four words on a $50,000 deal",
       "Your pipeline data is not a discipline problem. The incentive is upside down.", a3),
      ("2026-11-02-hindi-hinglish-sales-calls", "Hinglish",
       "One sentence, two languages",
       "Most tools support Hindi. Few survive a sentence that switches mid-way.", a4),
    ]


for T in (DARK, LIGHT):
    outdir = "out" if T["theme"] == "dark" else "out-light"
    os.makedirs(outdir, exist_ok=True)
    for slug, eyebrow, title, sub, art in covers(T):
        html = SHELL.format(eyebrow=eyebrow, title=title, sub=sub, art=art, **T)
        open(f"{outdir}/{slug}.html", "w", encoding="utf-8").write(html)
    print("wrote", T["theme"], "->", outdir)
