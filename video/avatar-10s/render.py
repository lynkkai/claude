"""Render a 10s animated Lynkk avatar video (1080x1080, 30fps) from voice.wav + timing.json."""
import json, math, subprocess, sys
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = H = 1080
SS = 2                      # supersampling factor
FPS = 30
DUR = 10.0
NF = int(DUR * FPS)
FONT = "/usr/share/fonts/opentype/inter/"

def F(name, size): return ImageFont.truetype(FONT + name, int(size * SS))
def s(v): return int(round(v * SS))
def box(x0, y0, x1, y1): return [s(x0), s(y0), s(x1), s(y1)]
def ease(x): x = min(max(x, 0), 1); return 1 - (1 - x) ** 3
def hexc(h, a=255): h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) + (a,)

VIOLET, CYAN, INK = "#7c6cff", "#38d6f5", "#0d0b1f"

# ---------- audio envelope ----------
audio, sr = sf.read("voice.wav")
timing = json.load(open("timing.json"))
win = sr // FPS
amp = np.zeros(NF)
for i in range(NF):
    c = int(i / FPS * sr); seg = audio[max(c - win, 0):c + win // 2]
    amp[i] = np.sqrt(np.mean(seg ** 2)) if len(seg) else 0
amp = np.clip(amp / np.percentile(amp[amp > 0.005], 90), 0, 1.2) ** 0.75
sm = np.zeros(NF); v = 0
for i, a in enumerate(amp):
    v = v + (a - v) * (0.65 if a > v else 0.35); sm[i] = v

# per-word timing (proportional to character count within each phrase)
words = []
for ph in timing:
    ws = ph["text"].split(); tot = sum(len(w) + 1 for w in ws); t = ph["start"]
    for w in ws:
        d = (ph["end"] - ph["start"]) * (len(w) + 1) / tot
        words.append((w, t, ph)); t += d
def word_time(phrase_idx, needle):
    for w, t, ph in words:
        if ph is timing[phrase_idx] and needle.lower() in w.lower(): return t
    return timing[phrase_idx]["start"]

T_NOTES, T_TASKS, T_CRM = word_time(2, "notes"), word_time(2, "tasks"), word_time(2, "CRM")
T_CONTEXT = timing[0]["start"] + 0.6
T_CTA = timing[3]["start"] - 0.1

# ---------- static layers ----------
def gradient(w, h, top, bot):
    t = np.linspace(0, 1, h)[:, None, None]
    a = np.array(hexc(top)[:3]); b = np.array(hexc(bot)[:3])
    g = (a * (1 - t) + b * t).astype(np.uint8)
    return Image.fromarray(np.broadcast_to(g, (h, w, 3)).copy()).convert("RGBA")

BG = gradient(s(W), s(H), "#0b0a1c", "#1c1546")

def glow_sprite(r, color, alpha):
    im = Image.new("RGBA", (s(r * 2), s(r * 2)), (0, 0, 0, 0))
    yy, xx = np.mgrid[0:s(r*2), 0:s(r*2)]
    d = np.sqrt((xx - s(r)) ** 2 + (yy - s(r)) ** 2) / s(r)
    al = (np.clip(1 - d, 0, 1) ** 2 * alpha).astype(np.uint8)
    arr = np.zeros((s(r*2), s(r*2), 4), np.uint8); arr[..., :3] = hexc(color)[:3]; arr[..., 3] = al
    return Image.fromarray(arr)

BLOB1 = glow_sprite(420, VIOLET, 110)
BLOB2 = glow_sprite(360, CYAN, 70)
HALO = glow_sprite(300, VIOLET, 120)

TILE = (110, 140, 970, 790)  # x0,y0,x1,y1
TW, TH = TILE[2] - TILE[0], TILE[3] - TILE[1]
TILE_MASK = Image.new("L", (s(TW), s(TH)), 0)
ImageDraw.Draw(TILE_MASK).rounded_rectangle([0, 0, s(TW) - 1, s(TH) - 1], s(36), fill=255)
TILE_BG = gradient(s(TW), s(TH), "#231d55", "#141133")

def overlay(base, fn):
    lay = Image.new("RGBA", base.size, (0, 0, 0, 0)); fn(ImageDraw.Draw(lay)); base.alpha_composite(lay)

# ---------- avatar ----------
SKIN, SKIN_D, HAIR, SHIRT = "#f3c9a6", "#e2ae8a", "#2a2150", "#6a5cf0"

def blink_factor(t):
    for bt in (1.6, 4.9, 7.4, 8.9):
        d = abs(t - bt)
        if d < 0.09: return 0.12 + 0.88 * (d / 0.09)
    return 1.0

def draw_avatar(img, t, i):
    """img is the tile-sized RGBA layer; coords below are tile-local (pre-SS)."""
    a = sm[i]
    cx = TW / 2 + 6 * math.sin(t * 1.3)
    cy = 300 + 5 * math.sin(t * 2.1) - 6 * a
    d = ImageDraw.Draw(img)

    # halo behind head, pulses with voice
    hs = HALO.resize((int(HALO.width * (0.9 + 0.25 * a)),) * 2)
    img.alpha_composite(hs, (s(cx) - hs.width // 2, s(cy + 10) - hs.height // 2))

    # torso + collar
    d.ellipse(box(cx - 230, cy + 175, cx + 230, cy + 560), fill=hexc(SHIRT))
    d.rounded_rectangle(box(cx - 34, cy + 110, cx + 34, cy + 200), s(18), fill=hexc(SKIN_D))
    d.pieslice(box(cx - 60, cy + 150, cx + 60, cy + 240), 0, 180, fill=hexc(SKIN_D))
    d.arc(box(cx - 70, cy + 140, cx + 70, cy + 250), 10, 170, fill=hexc("#ffffff", 200), width=s(6))
    # small Lynkk badge on shirt
    bx, by = cx + 115, cy + 290
    d.ellipse(box(bx - 26, by - 26, bx + 26, by + 26), fill=hexc("#ffffff", 235))
    d.ellipse(box(bx - 16, by - 9, bx + 2, by + 9), outline=hexc(VIOLET), width=s(4))
    d.ellipse(box(bx - 2, by - 9, bx + 16, by + 9), outline=hexc(CYAN), width=s(4))

    # back hair, ears, head
    d.ellipse(box(cx - 142, cy - 165, cx + 142, cy + 120), fill=hexc(HAIR))
    for sx in (-1, 1):
        ex = cx + sx * 122
        d.ellipse(box(ex - 22, cy - 10, ex + 22, cy + 42), fill=hexc(SKIN_D))
    d.ellipse(box(cx - 124, cy - 140, cx + 124, cy + 145), fill=hexc(SKIN))
    # fringe
    d.chord(box(cx - 134, cy - 170, cx + 134, cy + 10), 180, 360, fill=hexc(HAIR))
    d.ellipse(box(cx - 20, cy - 150, cx + 122, cy - 66), fill=hexc(HAIR))

    # headset (meeting assistant cue)
    d.arc(box(cx - 150, cy - 175, cx + 150, cy + 110), 195, 345, fill=hexc("#1a1538"), width=s(12))
    d.rounded_rectangle(box(cx - 160, cy - 5, cx - 128, cy + 60), s(12), fill=hexc("#1a1538"))
    d.line([s(cx - 140), s(cy + 50), s(cx - 95), s(cy + 100)], fill=hexc("#1a1538"), width=s(7))
    d.ellipse(box(cx - 104, cy + 92, cx - 84, cy + 112), fill=hexc(CYAN if a > 0.15 else "#4a4380"))

    # cheeks
    overlay(img, lambda o: [o.ellipse(box(cx + sx * 72 - 24, cy + 40, cx + sx * 72 + 24, cy + 66),
                                      fill=hexc("#ff7a8a", 70)) for sx in (-1, 1)])
    # brows
    br = 4 + 8 * a
    for sx in (-1, 1):
        ex = cx + sx * 46
        d.arc(box(ex - 26, cy - 52 - br, ex + 26, cy - 18 - br), 200, 340, fill=hexc(HAIR), width=s(7))
    # eyes
    bf = blink_factor(t)
    look = 4 * math.sin(t * 0.7)
    for sx in (-1, 1):
        ex, ey = cx + sx * 46, cy + 2
        ry = 21 * bf
        d.ellipse(box(ex - 19, ey - ry, ex + 19, ey + ry), fill=hexc("#ffffff"))
        if bf > 0.4:
            pr = 12 * min(1, bf * 1.1)
            d.ellipse(box(ex + look - 12, ey - pr + 2, ex + look + 12, ey + pr + 2), fill=hexc("#2b2350"))
            d.ellipse(box(ex + look + 1, ey - 8, ex + look + 7, ey - 2), fill=hexc("#ffffff"))
    # nose
    d.arc(box(cx - 10, cy + 28, cx + 10, cy + 46), 20, 160, fill=hexc(SKIN_D), width=s(4))

    # mouth driven by audio
    my = cy + 78
    o = a + 0.06 * math.sin(i * 1.7) * (a > 0.1)
    if o < 0.08:
        d.arc(box(cx - 30, my - 18, cx + 30, my + 10), 20, 160, fill=hexc("#8a3a4a"), width=s(6))
    else:
        mw = 30 - 8 * min(o, 1) + 4 * math.sin(i * 0.9)
        mh = 4 + 30 * min(o, 1.1)
        d.rounded_rectangle(box(cx - mw, my - mh * 0.35, cx + mw, my + mh * 0.65), s(min(mw, mh * 0.5 + 4)),
                            fill=hexc("#5a1e2e"))
        if mh > 14:
            d.rounded_rectangle(box(cx - mw * 0.75, my - mh * 0.35, cx + mw * 0.75, my - mh * 0.35 + 6),
                                s(3), fill=hexc("#ffffff"))
            d.ellipse(box(cx - mw * 0.55, my + mh * 0.2, cx + mw * 0.55, my + mh * 0.62), fill=hexc("#e8707f"))

def check_icon(d, x, y, r, col):
    d.ellipse(box(x - r, y - r, x + r, y + r), fill=hexc(col))
    d.line([s(x - r * 0.45), s(y), s(x - r * 0.1), s(y + r * 0.38), s(x + r * 0.5), s(y - r * 0.35)],
           fill=hexc("#ffffff"), width=s(r * 0.28), joint="curve")

def chip(base, t, t0, x, y, label, sub, col):
    p = ease((t - t0) / 0.35)
    if p <= 0: return
    dx = (1 - p) * 120
    def fn(d):
        d.rounded_rectangle(box(x + dx, y, x + dx + 268, y + 74), s(20), fill=hexc("#ffffff", int(238 * p)))
        check_icon(d, x + dx + 38, y + 37, 20, col)
        d.text((s(x + dx + 70), s(y + 13)), label, font=F("Inter-Bold.otf", 24), fill=hexc("#16123a", int(255 * p)))
        d.text((s(x + dx + 70), s(y + 42)), sub, font=F("Inter-Medium.otf", 16), fill=hexc("#6b6790", int(255 * p)))
    overlay(base, fn)

def wrap(text, font, maxw):
    lines, cur = [], []
    for w in text.split():
        trial = " ".join(cur + [w])
        if cur and font.getlength(trial) > s(maxw): lines.append(cur); cur = [w]
        else: cur.append(w)
    lines.append(cur); return lines

def captions(base, t):
    ph = next((p for p in timing[:3] if p["start"] - 0.05 <= t <= p["end"] + 0.12), None)
    if not ph: return
    f = F("Inter-SemiBold.otf", 38)
    lines = wrap(ph["text"], f, 860)
    lh = 52; y0 = 832 + (2 - len(lines)) * lh / 2
    def fn(d):
        idx = 0
        for li, line in enumerate(lines):
            lw = f.getlength(" ".join(line)); x = s(W / 2) - lw / 2
            for w in line:
                wt = next(wt for ww, wt, p in words if p is ph and ww == w)
                col = hexc("#ffffff") if t >= wt else hexc("#8f8ac0")
                d.text((x, s(y0 + li * lh)), w, font=f, fill=col)
                x += f.getlength(w + " "); idx += 1
    overlay(base, fn)

def cta(base, t):
    p = ease((t - T_CTA) / 0.3)
    if p <= 0: return
    f = F("Inter-Bold.otf", 40); label = "Try it free at lynkk.ai"
    tw = f.getlength(label) / SS; bw, bh = tw + 90, 84
    sc = 0.85 + 0.15 * p
    x0, y0 = W / 2 - bw * sc / 2, 860 - bh * sc / 2 + 20
    def fn(d):
        d.rounded_rectangle(box(x0, y0, x0 + bw * sc, y0 + bh * sc), s(42 * sc), fill=hexc(VIOLET, int(255 * p)))
        fs = F("Inter-Bold.otf", 40 * sc)
        d.text((s(W / 2), s(y0 + bh * sc / 2)), label, font=fs, fill=hexc("#ffffff", int(255 * p)), anchor="mm")
    overlay(base, fn)

def header(base, t):
    def fn(d):
        lx, ly = 140, 78
        d.ellipse(box(lx - 26, ly - 16, lx + 6, ly + 16), outline=hexc(VIOLET), width=s(7))
        d.ellipse(box(lx - 6, ly - 16, lx + 26, ly + 16), outline=hexc(CYAN), width=s(7))
        d.text((s(lx + 44), s(ly)), "Lynkk", font=F("InterDisplay-Bold.otf", 44), fill=hexc("#ffffff"), anchor="lm")
        # live pill
        px1, py = 970, 78
        d.rounded_rectangle(box(px1 - 200, py - 24, px1, py + 24), s(24), fill=hexc("#ffffff", 28))
        pulse = 0.55 + 0.45 * math.sin(t * 5)
        d.ellipse(box(px1 - 178, py - 8, px1 - 162, py + 8), fill=hexc("#ff4d6d", int(255 * pulse)))
        d.text((s(px1 - 150), s(py)), "In meeting", font=F("Inter-SemiBold.otf", 24), fill=hexc("#ffffff"), anchor="lm")
    overlay(base, fn)

def frame(i):
    t = i / FPS
    img = BG.copy()
    img.alpha_composite(BLOB1, (s(-260 + 60 * math.sin(t * 0.5)), s(520 + 40 * math.cos(t * 0.4))))
    img.alpha_composite(BLOB2, (s(560 + 50 * math.cos(t * 0.6)), s(-200 + 40 * math.sin(t * 0.5))))
    header(img, t)

    # meeting tile with avatar
    tile = TILE_BG.copy()
    draw_avatar(tile, t, i)
    def tag(d):
        d.rounded_rectangle(box(22, TH - 74, 248, TH - 22), s(26), fill=hexc("#0b0a1c", 170))
        for k in range(3):
            hgt = 6 + 18 * min(1, sm[i] * (0.7 + 0.3 * math.sin(i * 0.8 + k * 2)))
            bx = 46 + k * 11
            d.rounded_rectangle(box(bx - 3, TH - 48 - hgt / 2, bx + 3, TH - 48 + hgt / 2), s(3), fill=hexc(CYAN))
        d.text((s(84), s(TH - 48)), "Lynkk AI", font=F("Inter-SemiBold.otf", 24), fill=hexc("#ffffff"), anchor="lm")
    overlay(tile, tag)
    img.paste(tile, (s(TILE[0]), s(TILE[1])), TILE_MASK)
    # speaking border
    ga = int(70 + 185 * min(1, sm[i]))
    overlay(img, lambda d: d.rounded_rectangle(box(*TILE), s(36), outline=hexc(VIOLET, ga), width=s(5)))

    # context chip (left) + output chips (right)
    chip(img, t, T_CONTEXT, 140, 180, "Past context", "3 earlier calls", VIOLET)
    chip(img, t, T_NOTES - 0.1, 682, 300, "Notes ready", "Summary and key points", "#22c08a")
    chip(img, t, T_TASKS - 0.1, 682, 390, "Tasks assigned", "4 action items", "#22c08a")
    chip(img, t, T_CRM - 0.1, 682, 480, "CRM updated", "Deal stage synced", "#22c08a")

    captions(img, t)
    cta(img, t)
    out = img.resize((W, H), Image.LANCZOS).convert("RGB")
    fade = min(1, t / 0.25)
    if fade < 1: out = Image.blend(Image.new("RGB", (W, H), hexc(INK)[:3]), out, fade)
    return out

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "stills":
        for t in map(float, sys.argv[2:]):
            frame(int(t * FPS)).save(f"still_{t:.1f}.png")
        sys.exit()
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", "voice.wav",
        "-af", "apad", "-t", str(DUR), "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "lynkk-avatar-10s.mp4"], stdin=subprocess.PIPE)
    for i in range(NF):
        ff.stdin.write(frame(i).tobytes())
    ff.stdin.close(); ff.wait(); print("done", ff.returncode)
