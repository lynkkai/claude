---
platform: Hashnode
title: "Speaker Diarization Explained: Who Said What, With Whisper and pyannote in Python"
subtitle: "Transcription gives you words. Diarization gives you speakers. Here's how to combine the two, and why meeting audio makes it harder than benchmarks suggest."
slug: speaker-diarization-whisper-pyannote-python
tags: [python, machine-learning, speech-recognition, whisper, audio]
target_queries: ["speaker diarization", "what is speaker diarization", "whisper speaker diarization", "speaker diarization python", "pyannote speaker diarization 3.1"]
evidence: "Ubersuggest (US): 'speaker diarization' 880/mo SD 54, 'pyannote speaker diarization 3.1' 140/mo SD 6, 'pyannote audio speaker diarization' 110, 'what is speaker diarization' 90, 'whisper speaker diarization' 50, 'speaker diarization python' 30. GSC: 'interview transcription' 25 impr, 'user interview transcription' 95 impr at 39.7"
main_site_links:
  - https://lynkk.ai/blog/ai-transcription-software
  - https://lynkk.ai/blog/transcribe-audio-to-text
  - https://lynkk.ai/use-cases/user-interviews
canonical: "none (original article, do not set a canonical)"
cover_image: "A waveform split into colored bands labelled SPEAKER_00, SPEAKER_01, SPEAKER_02"
status: draft
---

# Speaker Diarization Explained: Who Said What, With Whisper and pyannote in Python

A transcript without speakers is a wall of text. For a lecture that's fine. For a meeting, an interview or a sales call, it's nearly useless: the whole point is knowing *who* agreed, *who* objected and *who* owns the next step.

**Speaker diarization** answers "who spoke when." It doesn't know names; it splits audio into segments and labels them `SPEAKER_00`, `SPEAKER_01` and so on. Combine it with a speech-to-text model and you get a speaker-labelled transcript.

This post builds that pipeline with two open-source tools, OpenAI's **Whisper** for transcription and **pyannote.audio** for diarization, then covers the real-world problems you'll hit on meeting audio.

## How diarization works (briefly)

Modern diarization pipelines do roughly four things:

1. **Voice activity detection**: find where anyone is speaking.
2. **Segmentation**: split speech into short chunks, detecting speaker changes and overlaps.
3. **Embedding**: turn each chunk into a vector that represents the voice (a "speaker embedding").
4. **Clustering**: group chunks whose embeddings are similar, so each cluster is one speaker.

The output is a timeline: `0.5s to 4.2s SPEAKER_00`, `4.3s to 9.8s SPEAKER_01`, and so on.

Transcription models like Whisper produce a different timeline: text segments with start and end times. Our job is to align the two.

## Setup

```bash
pip install openai-whisper pyannote.audio
# ffmpeg is required by Whisper
brew install ffmpeg   # or apt-get install ffmpeg
```

pyannote's pretrained pipelines are gated on Hugging Face: accept the model's terms on its model page and create an access token.

Convert your input to 16 kHz mono WAV first; both tools are happier with it:

```bash
ffmpeg -i meeting.m4a -ac 1 -ar 16000 meeting.wav
```

## Step 1: Transcribe with Whisper

```python
import whisper

asr = whisper.load_model("small")          # try "medium" or "large" for accuracy
result = asr.transcribe("meeting.wav")
segments = result["segments"]              # each has start, end, text
```

## Step 2: Diarize with pyannote

```python
import os
from pyannote.audio import Pipeline

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=os.environ["HF_TOKEN"],  # newer releases name this `token`
)
diarization = pipeline("meeting.wav")       # optionally num_speakers=3

turns = [
    (turn.start, turn.end, speaker)
    for turn, _, speaker in diarization.itertracks(yield_label=True)
]
```

If you know how many people were in the meeting, pass `num_speakers` (or `min_speakers`/`max_speakers`). It's the single cheapest accuracy win.

## Step 3: Assign a speaker to each transcript segment

The simplest robust approach: for each Whisper segment, pick the speaker whose turns overlap it the most.

```python
from collections import defaultdict

def overlap(a0, a1, b0, b1):
    return max(0.0, min(a1, b1) - max(a0, b0))

def label_segments(segments, turns):
    labelled = []
    for seg in segments:
        scores = defaultdict(float)
        for t0, t1, spk in turns:
            scores[spk] += overlap(seg["start"], seg["end"], t0, t1)
        speaker = max(scores, key=scores.get) if scores else "UNKNOWN"
        labelled.append({**seg, "speaker": speaker})
    return labelled

def merge_turns(labelled):
    merged = []
    for seg in labelled:
        if merged and merged[-1]["speaker"] == seg["speaker"]:
            merged[-1]["text"] += seg["text"]
            merged[-1]["end"] = seg["end"]
        else:
            merged.append(dict(seg))
    return merged

for s in merge_turns(label_segments(segments, turns)):
    print(f"[{s['start']:7.1f}] {s['speaker']}: {s['text'].strip()}")
```

Output looks like:

```
[    2.1] SPEAKER_00: Can we move the rollout to the 28th?
[    6.4] SPEAKER_01: Yes, if QA signs off by Friday.
```

Segment-level assignment is coarse: a single Whisper segment can contain two speakers. For finer results, use word-level timestamps (`word_timestamps=True` in Whisper) and assign speakers per word, or use a toolkit like WhisperX that does alignment for you.

## Why meeting audio is harder than benchmarks

Diarization looks great on clean podcast audio and gets noticeably worse in real meetings. The usual culprits:

- **Overlapping speech.** People interrupt, agree ("mm-hm") and talk over each other. Overlaps are where diarization errors cluster.
- **Short turns.** "Yes." "Agreed." Half-second turns don't give the embedding model much to work with.
- **Similar voices.** Two speakers of similar age and accent on similar microphones can merge into one cluster.
- **Room audio.** In-person meetings recorded from one laptop add echo and distance, and quieter speakers get lost.
- **Compression.** Conferencing codecs are tuned for intelligibility, not for preserving voice characteristics.

## Practical tricks that help a lot

**Use separate channels when you can.** If you record the local microphone and the remote call audio on separate channels, you already know which speech is "you" with no diarization at all, and you only need to diarize the remote side. Many desktop notetakers record exactly this way for that reason.

**Use participant metadata.** Meeting platforms know who is unmuted and who has the active-speaker indicator. A bot inside the call can use that to map clusters to real names. That's why bot-based notetakers can often show real participant names.

**Constrain the number of speakers.** Calendar invites tell you who's expected. Use it.

**Map clusters to names after the fact.** Let users rename `SPEAKER_01` to "Priya" once, then propagate that label across the transcript.

## Diarization in interviews and research

Speaker labels matter most in one-to-one and small-group recordings: user interviews, hiring interviews, customer discovery. In a UX interview you need to separate the participant's words from the interviewer's prompts, or your analysis will quote your own leading questions back at you. Lynkk has a write-up on transcribing [user interviews for research](https://lynkk.ai/use-cases/user-interviews) that covers this from the researcher's side.

## Build vs use

This pipeline is a good way to understand the problem, and it's fine for batch processing a folder of recordings. For production you'll also need chunking for long files, GPU scheduling, language detection, and a UI for corrections.

If you just need transcripts, the Lynkk team compared [7 AI transcription tools](https://lynkk.ai/blog/ai-transcription-software) by job (live transcripts, file uploads, editing by text, meeting notes), and there's a more general guide on [how to transcribe audio to text](https://lynkk.ai/blog/transcribe-audio-to-text) with free options.

## Summary

- Transcription answers *what*, diarization answers *who*.
- Align them by time overlap; go word-level for accuracy.
- Meeting audio is hard because of overlaps, short turns and room acoustics.
- Separate channels and platform metadata beat clever clustering.

---

*Written by the Lynkk team with AI assistance. Library APIs current as of October 2026; check the pyannote and Whisper docs for version changes.*
