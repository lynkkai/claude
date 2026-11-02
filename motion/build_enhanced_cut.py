import subprocess, os, shlex
D = "/tmp/claude-0/-home-user-claude/1cf829ca-33a2-5e80-8d62-ad9dd1f50918/scratchpad/dl"
SRC = f"{D}/recording.mov"
OUT = "/home/user/claude/lynkk-enhanced-sample.mp4"
SEG = f"{D}/seg"; os.makedirs(SEG, exist_ok=True)
FONT = "/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf"
if not os.path.exists(FONT):
    FONT = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"

WIDE       = (2585,1454,205,170)
DICT_STATS = (1700, 956,690,102)
DICT_HIST  = (1700, 956,882,722)
JIRA       = (1500, 844,1120, 786)

segs = [
 (0.30,3.10, WIDE,       "Every conversation, transcribed and summarised", 1.0),
 (3.40,6.60, WIDE,       "Ask across every meeting you've captured", 1.0),
 (11.20,14.20,DICT_STATS, "Hold a key, talk, and it types in any app", 1.0),
 (15.60,19.60,DICT_HIST,  "Your words are kept 7 days, then erased", 1.0),
 (20.60,22.60,WIDE,       "Action items land on a board", 1.0),
 (23.40,27.40,WIDE,       "Connect the tools you already use", 1.0),
 (31.45,32.95,JIRA,       "Every action item, straight to Jira", 0.62),
]
XF = 0.40
files = []
for i,(a,b,crop,cap,spd) in enumerate(segs):
    w,h,x,y = crop
    dur = (b-a)/spd
    cap_esc = cap.replace("'", r"’").replace(":", r"\:").replace(",", r"\,")
    # caption fades in at 0.25s, out 0.5s before segment end
    fi, fo = 0.25, dur-0.55
    alpha = f"if(lt(t,{fi}),0,if(lt(t,{fi+0.3}),(t-{fi})/0.3,if(lt(t,{fo}),1,max(0,1-(t-{fo})/0.35))))"
    vf = (
      f"crop={w}:{h}:{x}:{y},setpts={1/spd:.4f}*PTS,scale=1920:1080:flags=lanczos,"
      f"drawbox=x=0:y=934:w=1920:h=146:color=black@0.0:t=fill,"
      f"drawtext=fontfile={FONT}:text='{cap_esc}':fontsize=46:fontcolor=white:"
      f"x=(w-text_w)/2:y=h-128:alpha='{alpha}':"
      f"box=1:boxcolor=0x0b0f1a@0.62:boxborderw=28,"
      f"format=yuv420p"
    )
    f = f"{SEG}/s{i}.mp4"
    cmd = ["ffmpeg","-v","error","-y","-ss",str(a),"-t",str(b-a),"-i",SRC,
           "-vf",vf,"-r","60","-c:v","libx264","-crf","17","-preset","medium","-an",f]
    subprocess.run(cmd, check=True)
    files.append((f,dur))

# chain xfades
inputs = []
for f,_ in files: inputs += ["-i", f]
fc = []
prev = "0:v"; off = 0.0
for i in range(1,len(files)):
    off += files[i-1][1] - XF if i==1 else files[i-1][1] - XF
    lbl = f"x{i}"
    fc.append(f"[{prev}][{i}:v]xfade=transition=fade:duration={XF}:offset={off:.3f}[{lbl}]")
    prev = lbl
total = sum(d for _,d in files) - XF*(len(files)-1)
fc.append(f"[{prev}]fade=t=in:st=0:d=0.4,fade=t=out:st={total-0.5:.3f}:d=0.5[v]")
cmd = ["ffmpeg","-v","error","-y"] + inputs + ["-filter_complex",";".join(fc),
       "-map","[v]","-r","60","-c:v","libx264","-crf","18","-preset","slow",
       "-pix_fmt","yuv420p","-movflags","+faststart",OUT]
subprocess.run(cmd, check=True)
print("total", round(total,2), "s ->", OUT)
