import json, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
k = Kokoro("kokoro/kokoro-v1.0.int8.onnx", "kokoro/voices-v1.0.bin")
# (spoken text, caption text)
chunks = [
 ("Hi, I'm Link, your AI meeting teammate.", "Hi, I'm Lynkk, your AI meeting teammate."),
 ("I join your calls, and speak when you need me.", "I join your calls and speak when you need me."),
 ("I turn every conversation into notes, tasks, and CRM updates.", "I turn every conversation into notes, tasks, and CRM updates."),
 ("Try it free.", "Try it free at lynkk.ai"),
]
SPEED=1.22; GAP=0.14; LEAD=0.3
out=[np.zeros(int(24000*LEAD))]; t=LEAD; timing=[]
for spoken, cap in chunks:
    s, sr = k.create(spoken, voice="af_heart", speed=SPEED, lang="en-us")
    e=np.abs(s); nz=np.where(e>0.01)[0]; s=s[max(nz[0]-240,0):nz[-1]+480]
    d=len(s)/sr; timing.append({"start":t,"end":t+d,"text":cap}); out+= [s, np.zeros(int(sr*GAP))]; t+=d+GAP
a=np.concatenate(out); sf.write("voice.wav", a, 24000)
json.dump(timing, open("timing.json","w"), indent=1); print(json.dumps(timing, indent=1), len(a)/24000)
