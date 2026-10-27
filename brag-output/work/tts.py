import sys, json, torch, torchaudio as ta
from chatterbox.tts import ChatterboxTTS
torch.manual_seed(int(sys.argv[3]) if len(sys.argv)>3 else 7)
lines = json.load(open(sys.argv[1]))
ref = sys.argv[2]
m = ChatterboxTTS.from_pretrained(device="cpu")
for key, text in lines.items():
    wav = m.generate(text, audio_prompt_path=ref, exaggeration=0.6, cfg_weight=0.4, temperature=0.7)
    ta.save(f"vo/{key}.wav", wav, m.sr)
    print(key, wav.shape[-1]/m.sr, flush=True)
