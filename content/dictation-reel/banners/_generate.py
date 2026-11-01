import base64, pathlib, json

HERE = pathlib.Path("/tmp/claude-0/-home-user-claude/ac6f521f-34de-5c20-8500-3cb062260dcd/scratchpad")
OUT = pathlib.Path("/home/user/claude/content/dictation-reel/banners")
OUT.mkdir(parents=True, exist_ok=True)
logo_b64 = base64.b64encode((HERE/"logo.png").read_bytes()).decode()

ROBOT = """
<svg class="bot" viewBox="0 0 200 250" xmlns="http://www.w3.org/2000/svg">
  <path d="M100 118 L88 118 L100 158 L112 118 Z" fill="#F4A23B"/>
  <path d="M100 128 L94 128 L100 150 L106 128 Z" fill="#FFD98A"/>
  <circle cx="100" cy="24" r="9" fill="#9B8BDE"/>
  <rect x="97" y="30" width="6" height="22" fill="#9B8BDE"/>
  <circle cx="158" cy="86" r="17" fill="#9B8BDE"/>
  <rect x="26" y="46" width="148" height="86" rx="43" fill="#9B8BDE"/>
  <rect x="48" y="66" width="104" height="52" rx="26" fill="#17121F"/>
  <rect x="68" y="82" width="16" height="12" rx="6" fill="#fff"/>
  <rect x="116" y="82" width="16" height="12" rx="6" fill="#fff"/>
  <path d="M84 102 q16 14 32 0" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round"/>
</svg>"""

KEYCAP = """
<div class="key">
  <div class="keytop"><span>fn</span>
    <svg class="globe" viewBox="0 0 24 24" fill="none" stroke="#1b1b1f" stroke-width="1.6">
      <circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/>
      <path d="M3.2 9h17.6M3.2 15h17.6"/>
    </svg>
  </div>
</div>"""

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter Display','Inter',sans-serif;background:#07040C;overflow:hidden}
.b{position:relative;overflow:hidden;background:
   radial-gradient(130% 95% at 50% 8%, #2A1C4D 0%, #150E27 42%, #07040C 100%)}
.b::after{content:'';position:absolute;inset:0;
  background:radial-gradient(40% 30% at 78% 30%, rgba(155,139,222,.30), transparent 70%)}
.wrap{position:relative;z-index:2;display:flex;height:100%;width:100%}
.key{position:relative;filter:drop-shadow(0 0 70px rgba(166,148,255,.55))}
.keytop{position:relative;background:linear-gradient(#fff,#EDEAF5);border-radius:22%;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 14px 0 #B9B2C9, 0 26px 50px rgba(0,0,0,.5)}
.keytop span{font-weight:600;color:#15131A;line-height:1}
.globe{position:absolute;left:12%;bottom:10%;width:17%}
.bot{position:absolute}
h1{font-weight:800;letter-spacing:-.035em;color:#fff;line-height:1.02}
h1 em{font-style:normal;color:#B6A6F5}
.sub{color:#CFC6E8;font-weight:500;letter-spacing:-.01em}
.pills{display:flex;flex-wrap:wrap}
.pill{background:rgba(255,255,255,.08);border:1px solid rgba(182,166,245,.30);
  color:#EDE8FB;font-weight:600;border-radius:999px;white-space:nowrap}
.free{display:inline-flex;align-items:center;background:#fff;color:#12101A;
  font-weight:700;border-radius:999px;letter-spacing:-.01em}
.foot{display:flex;align-items:center;color:#fff}

.brand{font-weight:700;color:#fff;letter-spacing:-.02em}
.url{color:#B6A6F5;font-weight:600}
"""

def page(w, h, body, extra):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
    .b{{width:{w}px;height:{h}px}}{extra}</style></head>
    <body><div class="b"><div class="wrap">{body}</div></div></body></html>"""

LOGO = f'<img src="data:image/png;base64,{logo_b64}" alt="">'

def horizontal(w, h, head, sub, scale=1.0):
    s = lambda v: round(v*scale)
    body = f"""
    <div class="left">
      <div class="free">Free on every plan</div>
      <h1>{head}</h1>
      <div class="sub">{sub}</div>
      <div class="pills"><div class="pill">Any app</div><div class="pill">18 languages</div>
        <div class="pill">Unlimited words</div></div>
      <div class="foot">{LOGO}<div><div class="brand">Lynkk Dictation</div>
        <div class="url">lynkk.ai &middot; Download for Mac</div></div></div>
    </div>
    <div class="right">{KEYCAP}{ROBOT}</div>"""
    extra = f"""
    .left{{flex:1;padding:{s(62)}px {s(10)}px {s(58)}px {s(66)}px;display:flex;flex-direction:column;justify-content:center;gap:{s(20)}px}}
    .right{{width:{s(430)}px;position:relative;display:flex;align-items:center;justify-content:center}}
    .free{{padding:{s(9)}px {s(20)}px;font-size:{s(21)}px;align-self:flex-start}}
    h1{{font-size:{s(76)}px}}
    .sub{{font-size:{s(26)}px;line-height:1.35;max-width:{s(620)}px}}
    .pills{{gap:{s(11)}px}}
    .pill{{padding:{s(9)}px {s(18)}px;font-size:{s(19)}px}}
    .foot{{gap:{s(16)}px;margin-top:{s(10)}px}}
    .foot img{{width:{s(60)}px;height:{s(60)}px}}
    .brand{{font-size:{s(26)}px}} .url{{font-size:{s(21)}px;margin-top:{s(3)}px}}
    .keytop{{width:{s(260)}px;height:{s(260)}px}} .keytop span{{font-size:{s(112)}px}}
    .bot{{width:{s(150)}px;right:{s(22)}px;top:{s(70)}px}}
    """
    return page(w, h, body, extra)

def vertical(w, h, head, sub, scale=1.0):
    s = lambda v: round(v*scale)
    body = f"""
    <div class="col">
      <div class="hero">{KEYCAP}{ROBOT}</div>
      <div class="free">Free on every plan</div>
      <h1>{head}</h1>
      <div class="sub">{sub}</div>
      <div class="pills"><div class="pill">Any app</div><div class="pill">18 languages</div>
        <div class="pill">Unlimited words</div></div>
      <div class="foot">{LOGO}<div><div class="brand">Lynkk Dictation</div>
        <div class="url">lynkk.ai &middot; Download for Mac</div></div></div>
    </div>"""
    extra = f"""
    .col{{flex:1;padding:{s(96)}px {s(72)}px {s(74)}px;display:flex;flex-direction:column;
      align-items:center;text-align:center;justify-content:center;gap:{s(24)}px}}
    .hero{{position:relative;width:{s(390)}px;height:{s(300)}px;display:flex;align-items:center;justify-content:center;margin-bottom:{s(6)}px}}
    .free{{padding:{s(10)}px {s(24)}px;font-size:{s(24)}px}}
    h1{{font-size:{s(92)}px}}
    .sub{{font-size:{s(30)}px;line-height:1.35}}
    .pills{{gap:{s(12)}px;justify-content:center}}
    .pill{{padding:{s(10)}px {s(20)}px;font-size:{s(22)}px}}
    .foot{{gap:{s(16)}px;margin-top:{s(14)}px}}
    .foot img{{width:{s(68)}px;height:{s(68)}px}}
    .brand{{font-size:{s(30)}px}} .url{{font-size:{s(24)}px;margin-top:{s(3)}px}}
    .keytop{{width:{s(250)}px;height:{s(250)}px}} .keytop span{{font-size:{s(108)}px}}
    .bot{{width:{s(145)}px;right:-{s(10)}px;top:-{s(22)}px}}
    """
    return page(w, h, body, extra)

def thumb(w, h):
    body = f"""
    <div class="left">
      <div class="free">100% free &middot; unlimited words</div>
      <h1>HOLD <em>fn</em>.<br>JUST TALK.</h1>
      <div class="sub">Clean text in any Mac app &middot; 18 languages</div>
      <div class="foot">{LOGO}<div><div class="brand">Lynkk Dictation</div>
        <div class="url">lynkk.ai</div></div></div>
    </div>
    <div class="right">{KEYCAP}{ROBOT}</div>"""
    extra = """
    .left{flex:1;padding:70px 0 70px 76px;display:flex;flex-direction:column;justify-content:center;gap:26px}
    .right{width:470px;position:relative;display:flex;align-items:center;justify-content:center}
    .free{padding:12px 26px;font-size:26px;align-self:flex-start}
    h1{font-size:118px;line-height:.98}
    .sub{font-size:30px;font-weight:600}
    .foot{gap:18px;margin-top:12px}
    .foot img{width:64px;height:64px}
    .brand{font-size:28px} .url{font-size:24px;margin-top:2px}
    .keytop{width:300px;height:300px} .keytop span{font-size:128px}
    .bot{width:170px;right:16px;top:60px}
    """
    return page(w, h, body, extra)

HEAD = 'Hold <em>fn</em>.<br>Say it messy.'
SUB  = 'Lynkk Dictation turns your voice into clean text, right where your cursor is. In any app on your Mac.'


def reel(w, h, guides=False):
    g = ""
    if guides:
        g = """<div class="g gtop"></div><div class="g gbot"></div>
        <div class="g gright"></div><div class="grid"></div>
        <div class="glabel gl1">top UI zone</div>
        <div class="glabel gl2">caption / buttons zone</div>
        <div class="glabel gl3">profile grid crop (1:1)</div>"""
    body = f"""
    <div class="col">
      <div class="hero">{KEYCAP}{ROBOT}</div>
      <div class="free">Free on every plan</div>
      <h1>Hold <em>fn</em>.<br>Say it messy.</h1>
      <div class="sub">Clean text appears right where your<br>cursor is. In any app on your Mac.</div>
      <div class="pills"><div class="pill">Any app</div><div class="pill">18 languages</div>
        <div class="pill">Unlimited words</div></div>
      <div class="foot">{LOGO}<div><div class="brand">Lynkk Dictation</div>
        <div class="url">lynkk.ai &middot; Download for Mac</div></div></div>
    </div>""" + g
    extra = """
    .col{flex:1;padding:330px 80px 430px;display:flex;flex-direction:column;
      align-items:center;text-align:center;justify-content:center;gap:30px}
    .hero{position:relative;width:420px;height:330px;display:flex;align-items:center;
      justify-content:center;margin-bottom:14px}
    .free{padding:13px 30px;font-size:30px}
    h1{font-size:116px}
    .sub{font-size:36px;line-height:1.38}
    .pills{gap:14px;justify-content:center}
    .pill{padding:13px 26px;font-size:27px}
    .foot{gap:20px;margin-top:22px}
    .foot img{width:84px;height:84px}
    .brand{font-size:38px} .url{font-size:29px;margin-top:4px}
    .keytop{width:300px;height:300px} .keytop span{font-size:130px}
    .bot{width:178px;right:-14px;top:-26px}
    .g{position:absolute;left:0;right:0;z-index:9;background:rgba(255,80,80,.17);
       border-top:2px dashed rgba(255,120,120,.75);border-bottom:2px dashed rgba(255,120,120,.75)}
    .gtop{top:0;height:250px}
    .gbot{bottom:0;height:420px}
    .gright{top:250px;bottom:420px;left:auto;right:0;width:180px;
       background:rgba(255,80,80,.12);border:2px dashed rgba(255,120,120,.6)}
    .grid{position:absolute;z-index:9;left:0;width:1080px;height:1080px;top:420px;
       border:3px solid rgba(90,220,255,.85)}
    .glabel{position:absolute;z-index:10;color:#fff;font-size:26px;font-weight:700;
       font-family:'Inter',sans-serif;left:28px}
    .gl1{top:104px} .gl2{bottom:190px} .gl3{top:440px;color:#5ADCFF}
    """
    return page(w, h, body, extra)

VARIANTS = [
    ("instagram-reel-cover-1080x1920.png", 1080, 1920, reel(1080,1920)),
    ("instagram-reel-cover-1080x1920-SAFEZONE.png", 1080, 1920, reel(1080,1920,True)),
    ("instagram-1080x1350.png", 1080, 1350, vertical(1080,1350,HEAD,SUB,1.0)),
    ("instagram-square-1080x1080.png", 1080, 1080, vertical(1080,1080,HEAD,SUB,0.92)),
    ("facebook-1200x630.png", 1200, 630, horizontal(1200,630,HEAD,SUB,1.0)),
    ("linkedin-1200x627.png", 1200, 627, horizontal(1200,627,HEAD,SUB,1.0)),
    ("youtube-thumbnail-1280x720.png", 1280, 720, thumb(1280,720)),
]


HTML = pathlib.Path("/tmp/claude-0/-home-user-claude/ac6f521f-34de-5c20-8500-3cb062260dcd/scratchpad/gen/html")
HTML.mkdir(exist_ok=True)
manifest=[]
for name,w,h,html in VARIANTS:
    f = HTML/(name.replace(".png",".html"))
    f.write_text(html)
    manifest.append({"html":str(f),"out":str(OUT/name),"w":w,"h":h})
(HTML/"manifest.json").write_text(json.dumps(manifest,indent=1))
print("ok",len(manifest))
