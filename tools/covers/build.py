import os, math

# ============================================================================
# Lynkk design kit, extracted from lynkk.ai CSS 2026-11-02.
# The marketing site runs the "grid" token set (data-tokens=grid); its dark
# variant is html[data-ds=round][data-tokens=grid].dark / .theme-dark.
# Chart hues are the site's own --gr-series-1..5.
# ============================================================================
LIGHT = dict(
    theme="light",
    ink="#151514", ink2="#6c6c6a", ink3="#a3a3a1",
    bg="#f5f5f4", surface="#ffffff", fill="#f0f0ef",
    line="#e6e6e4", line_soft="#efefed", grid="#e6e6e4",
    accent_text="#7063be", accent="#7063be",
    accent_bed="#e2e0f2", accent_edge="#b4abe0",
    live="#e5484d", live_text="#e5484d", live_bed="#e5484d14",
    table="#ece9e2", table_edge="#dbdad6",
    dot="#11111108",
    shadow="0 14px 34px -12px #00000059",
    hairline="transparent",
    series=["#e0692a", "#7063be", "#2f7a4a", "#c24fb0", "#7a9a3e"],
)
DARK = dict(
    theme="dark",
    ink="#ffffff", ink2="#ffffff80", ink3="#ffffff57",
    bg="#111111", surface="#171717", fill="#1d1d1d",
    line="#292c31", line_soft="#1f2125", grid="#292c31",
    accent_text="#beb4fb", accent="#7063be",
    accent_bed="#231f3a", accent_edge="#b4abe0",
    live="#ff6157", live_text="#ff8a82", live_bed="#ff615714",
    table="#2e2e2e", table_edge="#292c31",
    dot="#ffffff0a",
    shadow="0 18px 44px -14px #00000099",
    hairline="#ffffff1a",
    series=["#f08a4b", "#9f93e0", "#4fa36c", "#d978c6", "#a0c25a"],
)

MONO = 'font-family:"JetBrains Mono",ui-monospace,monospace'

SHELL = """<!doctype html>
<html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Schibsted+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
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
    font-weight:700; font-size:{h1size}; line-height:1.2; letter-spacing:-.04em;
    max-width:{h1width};
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
  .art {{ flex:0 0 {artw}; }}
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


def render(T, eyebrow, title, sub, art, h1size="50px", h1width="15ch", artw="448px"):
    return SHELL.format(eyebrow=eyebrow, title=title, sub=sub, art=art,
                        h1size=h1size, h1width=h1width, artw=artw, **T)


# ---------------------------------------------------------------- Medium set
def arts_medium(T):
    seats = ""
    for cx, cy in [(96, 80), (216, 80), (96, 214), (216, 214)]:
        seats += ('<circle cx="%d" cy="%d" r="18" fill="%s" stroke="%s" stroke-width="1.5"/>'
                  % (cx, cy, T["fill"], T["line"]))
    a1 = """<div class="panel" style="padding:24px">
<svg width="400" height="300" viewBox="0 0 320 294">
  <circle cx="207" cy="147" r="48" fill="{bed}" opacity=".9"/>
  <rect x="70" y="110" width="180" height="74" rx="12" fill="{table}" stroke="{tedge}" stroke-width="1.5"/>
  {seats}
  <circle cx="207" cy="147" r="76" fill="none" stroke="{edge}" stroke-width="1.5" stroke-dasharray="4 5"/>
  <circle cx="207" cy="147" r="104" fill="none" stroke="{acc}" stroke-width="1.5"/>
  <rect x="196" y="130" width="22" height="34" rx="5" fill="{ink}"/>
  <rect x="200.5" y="134.5" width="13" height="21" rx="2.5" fill="{acc}"/>
  <circle cx="207" cy="159.5" r="1.6" fill="{bg}"/>
</svg>
<div style="display:flex;gap:18px;margin-top:2px;font-size:12px;color:{ink2}">
  <span style="display:flex;align-items:center;gap:7px"><span style="width:9px;height:9px;border-radius:2px;background:{ink}"></span>Recorder</span>
  <span style="display:flex;align-items:center;gap:7px"><span style="width:9px;height:9px;border-radius:999px;background:{bed};border:1px solid {edge}"></span>Pickup range</span>
</div></div>""".format(bed=T["accent_bed"], table=T["table"], tedge=T["table_edge"], seats=seats,
                       edge=T["accent_edge"], acc=T["accent"], ink=T["ink"], bg=T["bg"], ink2=T["ink2"])

    rows = ""
    for initials, name in [("PR", "Priya Raman"), ("NK", "Neha Kapoor"), ("JM", "Jamie Mitchell")]:
        rows += ("""<div style="display:flex;align-items:center;gap:13px;padding:11px 13px;border-radius:10px">
      <div style="width:34px;height:34px;border-radius:999px;background:%s;border:1px solid %s;
        display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:%s">%s</div>
      <div style="font-size:14px;font-weight:500">%s</div></div>"""
                 % (T["fill"], T["line"], T["ink2"], initials, name))
    a2 = """<div class="panel" style="padding:14px">
  <div style="font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:{ink3};padding:8px 13px 10px">Participants &middot; 4</div>
  {rows}
  <div style="display:flex;align-items:center;gap:13px;padding:11px 13px;border-radius:10px;
      background:{lbed};border:1px dashed {live}">
    <div style="width:34px;height:34px;border-radius:999px;background:{surface};border:1px dashed {live};
      display:flex;align-items:center;justify-content:center">
      <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="{live}" stroke-width="2" stroke-linecap="round">
        <rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 8V4"/>
        <circle cx="9" cy="14" r="1.4" fill="{live}" stroke="none"/><circle cx="15" cy="14" r="1.4" fill="{live}" stroke="none"/>
      </svg>
    </div>
    <div><div style="font-size:14px;font-weight:500;color:{ltext}">Priya's Notetaker</div>
      <div style="font-size:11.5px;color:{ink2};margin-top:1px">Joined the meeting</div></div>
  </div></div>""".format(ink3=T["ink3"], rows=rows, lbed=T["live_bed"], live=T["live"],
                         surface=T["surface"], ltext=T["live_text"], ink2=T["ink2"])

    def field(label, value):
        return ("""<div style="padding:11px 0;border-bottom:1px solid %s">
      <div style="font-size:10.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:%s">%s</div>
      <div style="font-size:14px;margin-top:5px;color:%s">%s</div></div>"""
                % (T["line_soft"], T["ink3"], label, T["ink"], value))
    a3 = """<div class="panel" style="padding:22px 24px">
  {f1}{f2}{f3}
  <div style="padding:11px 0 0">
    <div style="font-size:10.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:{ink3}">Call notes</div>
    <div style="margin-top:7px;height:92px;border:1px solid {line};border-radius:10px;
        background:{bg};padding:11px 12px;position:relative">
      <div style="font-size:13.5px;color:{ink2}">good call, sending proposal</div>
      <div style="position:absolute;left:12px;top:34px;width:1.5px;height:15px;background:{at}"></div>
    </div></div></div>""".format(f1=field("Account", "Corvane Logistics"), f2=field("Stage", "Proposal"),
                                 f3=field("Value", "$50,000"), ink3=T["ink3"], line=T["line"],
                                 bg=T["bg"], ink2=T["ink2"], at=T["accent_text"])

    a4 = """<div class="panel" style="padding:22px 24px">
  <div style="display:flex;align-items:center;gap:9px;font-size:11px;color:{ink3}">
    <span class="mono" style="color:{at}">14:22</span>
    <span style="width:4px;height:4px;border-radius:999px;background:{ink3}"></span>
    <span>Priya Raman</span></div>
  <div style="font-size:19px;line-height:1.62;margin-top:12px;letter-spacing:-.02em">
    <span style="background:{bed};border-radius:4px;padding:1px 4px">Budget to approve ho gaya hai,</span>
    but procurement will take three weeks, so kickoff first week of December.</div>
  <div style="display:flex;gap:16px;margin-top:18px;padding-top:15px;border-top:1px solid {lsoft};font-size:11.5px;color:{ink2}">
    <span style="display:flex;align-items:center;gap:7px"><span style="width:10px;height:10px;border-radius:3px;background:{bed};border:1px solid {edge}"></span>Hinglish</span>
    <span style="display:flex;align-items:center;gap:7px"><span style="width:10px;height:10px;border-radius:3px;background:{surface};border:1px solid {line}"></span>English</span>
    <span style="margin-left:auto;color:{at};font-weight:600">1 switch</span>
  </div></div>""".format(ink3=T["ink3"], at=T["accent_text"], bed=T["accent_bed"], lsoft=T["line_soft"],
                         ink2=T["ink2"], edge=T["accent_edge"], surface=T["surface"], line=T["line"])
    return a1, a2, a3, a4


# -------------------------------------------------------------- Hashnode set
def arts_dev(T):
    def wave(y, seed, amp):
        out = []
        for i in range(0, 361, 6):
            a = amp * (0.35 + 0.65 * abs(math.sin((i + seed) * 0.11)))
            out.append("M%d,%.1f L%d,%.1f" % (i, y + 17 - a, i, y + 17 + a))
        return " ".join(out)

    def lane(label, colour, y, seed, amp):
        return ('<text x="0" y="%d" style="%s;font-size:9.5px" fill="%s">%s</text>'
                '<rect x="0" y="%d" width="360" height="34" rx="6" fill="%s" stroke="%s"/>'
                '<path d="%s" fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round"/>'
                % (y - 12, MONO, T["ink2"], label, y, T["fill"], T["line"],
                   wave(y, seed, amp), colour))

    ticks1 = "".join('<line x1="%d" y1="152" x2="%d" y2="158" stroke="%s"/>' % (x, x, T["grid"])
                     for x in range(0, 361, 45))
    h1 = """<div class="panel" style="padding:24px">
<svg width="390" height="207" viewBox="0 0 360 206">
  {laneA}{laneB}
  <line x1="0" y1="152" x2="360" y2="152" stroke="{grid}"/>
  {ticks}
  <text x="0" y="174" style="{mono};font-size:8.5px" fill="{ink3}">0s</text>
  <text x="360" y="174" text-anchor="end" style="{mono};font-size:8.5px" fill="{ink3}">90 min</text>
  <line x1="246" y1="4" x2="246" y2="146" stroke="{edge}" stroke-width="1.2" stroke-dasharray="3 4"/>
  <text x="0" y="198" style="{mono};font-size:9.5px" fill="{at}">one shared clock, or the tracks drift</text>
</svg></div>""".format(laneA=lane("MIC &rarr; &ldquo;Me&rdquo;", T["series"][1], 24, 0, 11),
                       laneB=lane("SYSTEM &rarr; &ldquo;Them&rdquo;", T["series"][0], 100, 40, 13),
                       grid=T["grid"], ticks=ticks1, mono=MONO, ink3=T["ink3"],
                       edge=T["accent_edge"], at=T["accent_text"])

    segs = [(0, 74, 0), (80, 52, 1), (138, 60, 0), (204, 40, 2), (250, 46, 1)]
    bars = "".join('<rect x="%d" y="42" width="%d" height="26" rx="4" fill="%s" opacity=".85"/>'
                   % (x, w, T["series"][c]) for x, w, c in segs)
    h2 = """<div class="panel" style="padding:24px">
<svg width="390" height="207" viewBox="0 0 360 206">
  <text x="0" y="24" style="{mono};font-size:9.5px" fill="{ink2}">SPEAKER SEGMENTS</text>
  {bars}
  <rect x="126" y="36" width="24" height="38" rx="4" fill="none" stroke="{live}" stroke-width="1.6" stroke-dasharray="3 3"/>
  <text x="138" y="92" text-anchor="middle" style="{mono};font-size:9px" fill="{ltext}">overlap</text>
  <text x="0" y="132" style="{mono};font-size:9.5px" fill="{ink2}">EXTRACTED COMMITMENT</text>
  <text x="0" y="156" style="font-size:14px" fill="{ink}">&ldquo;I&rsquo;ll send the security overview&rdquo;</text>
  <text x="0" y="182" style="{mono};font-size:9.5px" fill="{ltext}">&rarr; credited to the wrong speaker</text>
</svg></div>""".format(mono=MONO, ink2=T["ink2"], bars=bars, live=T["live"], ltext=T["live_text"], ink=T["ink"])

    meetings = ""
    for y, lbl in [(16, "Mar call"), (86, "Jun call"), (156, "Oct call")]:
        meetings += ('<rect x="146" y="%d" width="78" height="30" rx="7" fill="%s" stroke="%s"/>'
                     '<text x="156" y="%d" style="%s;font-size:9px" fill="%s">%s</text>'
                     % (y, T["fill"], T["line"], y + 19, MONO, T["ink2"], lbl))
    h3 = """<div class="panel" style="padding:24px">
<svg width="390" height="207" viewBox="0 0 360 206">
  <rect x="0" y="86" width="88" height="34" rx="8" fill="{bed}" stroke="{edge}"/>
  <text x="11" y="107" style="{mono};font-size:10px" fill="{ink}">Account</text>
  <g stroke="{line}" stroke-width="1.3" fill="none">
    <path d="M88,98 C118,98 118,31 146,31"/><path d="M88,103 L146,101"/>
    <path d="M88,108 C118,108 118,171 146,171"/>
  </g>
  {meetings}
  <rect x="244" y="16" width="104" height="30" rx="7" fill="{surface}" stroke="{line}"/>
  <text x="256" y="35" style="{mono};font-size:9.5px" fill="{ink3}" text-decoration="line-through">budget $30K</text>
  <rect x="244" y="156" width="104" height="30" rx="7" fill="{surface}" stroke="{acc}" stroke-width="1.6"/>
  <text x="256" y="175" style="{mono};font-size:9.5px" fill="{at}">budget $50K</text>
  <path d="M296,46 L296,156" stroke="{acc}" stroke-width="1.4" stroke-dasharray="4 4" fill="none"/>
  <path d="M292,148 L296,156 L300,148" stroke="{acc}" stroke-width="1.4" fill="none"/>
  <text x="290" y="104" text-anchor="middle" style="{mono};font-size:9px" fill="{at}" transform="rotate(-90 290 104)">supersedes</text>
</svg></div>""".format(bed=T["accent_bed"], edge=T["accent_edge"], mono=MONO, ink=T["ink"],
                       line=T["line"], meetings=meetings, surface=T["surface"], ink3=T["ink3"],
                       acc=T["accent"], at=T["accent_text"])

    stages = [("capture", 120, 0), ("asr", 420, 1), ("intent", 90, 2),
              ("retrieval", 330, 3), ("gen", 640, 4), ("render", 50, 0)]
    total = sum(v for _, v, _ in stages)
    x, bar = 0.0, ""
    for name, ms, c in stages:
        w = ms / 2000 * 352
        bar += ('<rect x="%.1f" y="52" width="%.1f" height="30" rx="3" fill="%s" opacity=".9"/>'
                % (x, max(w - 2, 2), T["series"][c]))
        x += w
    ticks2 = ""
    for t in (0, 500, 1000, 1500, 2000):
        tx = t / 2000 * 352
        ticks2 += ('<line x1="%.1f" y1="86" x2="%.1f" y2="92" stroke="%s"/>'
                   '<text x="%.1f" y="106" text-anchor="middle" style="%s;font-size:8.5px" fill="%s">%d</text>'
                   % (tx, tx, T["grid"], tx, MONO, T["ink3"], t))
    h4 = """<div class="panel" style="padding:24px">
<svg width="390" height="207" viewBox="0 0 360 206">
  <text x="0" y="24" style="{mono};font-size:9.5px" fill="{ink2}">END-TO-END BUDGET &middot; ms</text>
  <rect x="0" y="52" width="352" height="30" rx="4" fill="{fill}" stroke="{line}"/>
  {bar}{ticks}
  <line x1="352" y1="42" x2="352" y2="92" stroke="{live}" stroke-width="1.6"/>
  <text x="352" y="36" text-anchor="end" style="{mono};font-size:9.5px" fill="{ltext}">2s: a visible pause</text>
  <text x="0" y="142" style="{mono};font-size:11px" fill="{ink}">{total}ms with nothing going wrong</text>
  <text x="0" y="164" style="{mono};font-size:9.5px" fill="{ink2}">p99 is the number that matters</text>
  <text x="0" y="188" style="{mono};font-size:9px" fill="{ink3}">illustrative, not measured</text>
</svg></div>""".format(mono=MONO, ink2=T["ink2"], fill=T["fill"], line=T["line"], bar=bar,
                       ticks=ticks2, live=T["live"], ltext=T["live_text"], ink=T["ink"],
                       total=total, ink3=T["ink3"])
    return h1, h2, h3, h4


# ----------------------------------------------------------------- Essay set
def arts_essay(T):
    # quieter, type-led. One motif each, no product chrome.
    def stack(labels, highlight_last=False):
        out = ""
        for i, lbl in enumerate(labels):
            edge = T["accent"] if (highlight_last and i == len(labels) - 1) else T["line"]
            width = 1.6 if (highlight_last and i == len(labels) - 1) else 1
            out += ('<rect x="%d" y="%d" width="196" height="30" rx="7" fill="%s" stroke="%s" stroke-width="%s"/>'
                    '<text x="%d" y="%d" style="%s;font-size:9.5px" fill="%s">%s</text>'
                    % (i * 10, i * 40, T["surface"], edge, width,
                       i * 10 + 12, i * 40 + 19, MONO, T["ink2"], lbl))
        return out

    s1 = """<div class="panel" style="padding:26px">
<svg width="372" height="214" viewBox="0 0 330 200">
  {stack}
  <path d="M232,55 L288,55 288,120 246,120" fill="none" stroke="{acc}" stroke-width="1.4" stroke-dasharray="4 4"/>
  <path d="M254,112 L246,120 254,128" fill="none" stroke="{acc}" stroke-width="1.4"/>
  <rect x="34" y="158" width="250" height="34" rx="17" fill="{bed}" stroke="{edge}"/>
  <text x="50" y="180" style="{mono};font-size:10px" fill="{ink}">how has their budget moved?</text>
</svg></div>""".format(stack=stack(["Mar call", "Jun call", "Oct call"]), acc=T["accent"],
                       bed=T["accent_bed"], edge=T["accent_edge"], mono=MONO, ink=T["ink"])

    items = ""
    for i, (lbl, done) in enumerate([("Send security overview", False),
                                     ("Book second discovery call", False),
                                     ("Share demo recording", False)]):
        items += ('<rect x="0" y="%d" width="18" height="18" rx="5" fill="none" stroke="%s" stroke-width="1.5"/>'
                  '<text x="30" y="%d" style="font-size:12.5px" fill="%s">%s</text>'
                  % (i * 40 + 54, T["line"], i * 40 + 68, T["ink2"], lbl))
    s2 = """<div class="panel" style="padding:26px">
<svg width="372" height="214" viewBox="0 0 330 200">
  <rect x="0" y="0" width="330" height="36" rx="8" fill="{fill}" stroke="{line}"/>
  <circle cx="18" cy="18" r="4" fill="{acc}"/>
  <text x="34" y="23" style="{mono};font-size:10px" fill="{ink2}">Recap: Corvane discovery</text>
  <text x="318" y="23" text-anchor="end" style="{mono};font-size:9px" fill="{ink3}">unread</text>
  {items}
  <text x="0" y="192" style="{mono};font-size:9.5px" fill="{ink3}">0 of 3 reached anyone&rsquo;s queue</text>
</svg></div>""".format(fill=T["fill"], line=T["line"], acc=T["accent"], mono=MONO,
                       ink2=T["ink2"], ink3=T["ink3"], items=items)

    s3 = """<div class="panel" style="padding:26px">
<svg width="372" height="214" viewBox="0 0 330 200">
  <rect x="0" y="36" width="76" height="34" rx="8" fill="{surface}" stroke="{line}"/>
  <text x="12" y="57" style="{mono};font-size:9.5px" fill="{ink2}">your call</text>
  <path d="M76,53 L116,53" stroke="{line}" stroke-width="1.4"/>
  <path d="M108,48 L116,53 108,58" stroke="{line}" stroke-width="1.4" fill="none"/>
  <rect x="116" y="36" width="84" height="34" rx="8" fill="{bed}" stroke="{edge}"/>
  <text x="128" y="57" style="{mono};font-size:9.5px" fill="{ink}">the vendor</text>
  <path d="M203,53 C226,53 226,22 244,22" stroke="{live}" stroke-width="1.4" fill="none" stroke-dasharray="4 4"/>
  <path d="M203,53 C226,53 226,88 244,88" stroke="{live}" stroke-width="1.4" fill="none" stroke-dasharray="4 4"/>
  <rect x="244" y="5" width="72" height="34" rx="8" fill="none" stroke="{live}" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="280" y="26" text-anchor="middle" style="{mono};font-size:13px" fill="{ltext}">?</text>
  <rect x="244" y="71" width="72" height="34" rx="8" fill="none" stroke="{live}" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="280" y="92" text-anchor="middle" style="{mono};font-size:13px" fill="{ltext}">?</text>
  <text x="280" y="128" text-anchor="middle" style="{mono};font-size:8.5px" fill="{ltext}">unnamed</text>
  <text x="280" y="141" text-anchor="middle" style="{mono};font-size:8.5px" fill="{ltext}">sub-processors</text>
  <text x="0" y="186" style="{mono};font-size:9.5px" fill="{ink3}">&ldquo;encrypted in transit and at rest&rdquo;</text>
</svg></div>""".format(surface=T["surface"], line=T["line"], mono=MONO, ink2=T["ink2"],
                       bed=T["accent_bed"], edge=T["accent_edge"], ink=T["ink"],
                       live=T["live"], ltext=T["live_text"], ink3=T["ink3"])

    s4 = """<div class="panel" style="padding:26px">
<svg width="372" height="214" viewBox="0 0 330 200">
  <line x1="0" y1="96" x2="330" y2="96" stroke="{grid}" stroke-width="1.4"/>
  <circle cx="44" cy="96" r="6" fill="{ink3}"/>
  <text x="44" y="78" text-anchor="middle" style="{mono};font-size:9px" fill="{ink3}">before</text>
  <circle cx="165" cy="96" r="9" fill="{acc}"/>
  <text x="165" y="74" text-anchor="middle" style="{mono};font-size:9.5px" fill="{at}">during</text>
  <circle cx="286" cy="96" r="6" fill="{ink3}"/>
  <text x="286" y="78" text-anchor="middle" style="{mono};font-size:9px" fill="{ink3}">after</text>
  <rect x="86" y="124" width="158" height="34" rx="17" fill="{bed}" stroke="{edge}"/>
  <text x="165" y="146" text-anchor="middle" style="{mono};font-size:9.5px" fill="{ink}">it speaks here</text>
  <text x="165" y="186" text-anchor="middle" style="{mono};font-size:9px" fill="{ink3}">in development</text>
</svg></div>""".format(grid=T["grid"], ink3=T["ink3"], mono=MONO, acc=T["accent"],
                       at=T["accent_text"], bed=T["accent_bed"], edge=T["accent_edge"], ink=T["ink"])
    return s1, s2, s3, s4


def all_covers(T):
    m1, m2, m3, m4 = arts_medium(T)
    h1, h2, h3, h4 = arts_dev(T)
    s1, s2, s3, s4 = arts_essay(T)
    return [
      # Medium
      ("2026-11-02-ai-note-taker-in-person-meetings", "In-person capture", "The meeting with no link",
       "Why room audio is a different problem, and where to put the microphone.", m1, {}),
      ("2026-11-02-bot-free-ai-note-takers", "Bot-free capture", "Something joined your call",
       "A notetaker bot is a product decision, not a law of physics.", m2, {}),
      ("2026-11-02-crm-graveyard-call-notes", "CRM hygiene", "Four words on a $50,000 deal",
       "Your pipeline data is not a discipline problem. The incentive is upside down.", m3, {}),
      ("2026-11-02-hindi-hinglish-sales-calls", "Hinglish", "One sentence, two languages",
       "Most tools support Hindi. Few survive a sentence that switches mid-way.", m4, {}),
      # Hashnode
      ("H1-recording-both-sides-without-a-bot", "Audio capture", "Two tracks, one clock",
       "Recording both halves of a call locally, and the five ways it breaks.", h1, {}),
      ("H2-speaker-diarization-in-production", "Diarization", "Who said what, and where it breaks",
       "Transcription is a commodity. Attribution is where meeting products fail.", h2, {}),
      ("H3-meetings-into-account-memory", "Retrieval", "Flat RAG cannot answer this",
       "Comparison, aggregation and absence all need structure over time.", h3, {}),
      ("H4-voice-agent-in-a-live-meeting", "Real-time", "You have two seconds",
       "Latency, turn-taking and interrupts in a live meeting assistant.", h4, {}),
      # Essays
      ("S1-the-meeting-is-the-database", "Essay", "The meeting is the database",
       "Notes are the wrong unit of work. The useful object is the relationship.", s1,
       {"h1size": "46px", "h1width": "13ch"}),
      ("S2-nobody-reads-the-recap", "Essay", "Nobody reads the recap",
       "We solved capture, called it productivity, and changed nothing about follow-through.", s2,
       {"h1size": "46px", "h1width": "13ch"}),
      ("S3-where-does-your-meeting-audio-go", "Essay", "Where does your meeting audio go?",
       "The useful security page is the one that says what the product cannot do.", s3,
       {"h1size": "44px", "h1width": "14ch"}),
      ("S4-from-note-taker-to-teammate", "Essay", "From note taker to teammate",
       "What changes when the assistant speaks while you are still talking.", s4,
       {"h1size": "46px", "h1width": "13ch"}),
    ]


for T in (DARK, LIGHT):
    outdir = "out" if T["theme"] == "dark" else "out-light"
    os.makedirs(outdir, exist_ok=True)
    for slug, eyebrow, title, sub, art, kw in all_covers(T):
        open(os.path.join(outdir, slug + ".html"), "w", encoding="utf-8").write(
            render(T, eyebrow, title, sub, art, **kw))
    print("wrote", T["theme"], "->", outdir, len(all_covers(T)), "covers")
