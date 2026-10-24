---
platform: Hashnode
title: "Code-Switching Breaks Speech Recognition: How to Test Hinglish ASR With WER and CER"
subtitle: "A practical evaluation harness for Hindi-English meeting audio, including the script problem that quietly ruins most benchmarks."
slug: testing-hinglish-speech-recognition-wer-cer
tags: [speech-recognition, python, nlp, machine-learning, india]
target_queries: ["hinglish transcription", "hinglish speech to text", "multilingual transcription", "multilingual meeting transcription", "hindi speech to text"]
evidence: "Ubersuggest (India): 'hinglish transcription' 110/mo, 'hinglish audio to text' 50, 'hinglish speech to text' 30, 'speech to text hinglish' 30, 'hindi speech to text' 1,600. GSC: /features/hinglish-transcription 260 impr (5 clicks); 'multilingual transcription' 33 impr, 'multilingual meeting transcription' 20; India drives 48 of 98 site clicks at 6.1% CTR"
main_site_links:
  - https://lynkk.ai/features/hinglish-transcription
  - https://lynkk.ai/blog/hindi-transcription
  - https://lynkk.ai/features/multilingual-transcription
canonical: "none (original article, do not set a canonical)"
cover_image: "A sentence half in Devanagari, half in Latin script, with a red WER score beside it"
status: draft
---

# Code-Switching Breaks Speech Recognition: How to Test Hinglish ASR With WER and CER

Listen to a product meeting in Bengaluru, a sales call in Mumbai or a standup at almost any Indian startup and you'll hear sentences like this:

> "Kal ka deployment thoda delay ho gaya, but QA ne sign off de diya hai, so we can push it today."

That's **Hinglish**: Hindi and English mixed inside the same sentence. Linguists call it *code-switching*. Speech recognition systems, especially ones that ask you to pick one language per recording, often handle it badly.

If you're choosing or building an ASR system for this kind of audio, you need to measure it properly. This post builds a small evaluation harness and explains the trap that makes most Hinglish benchmarks meaningless.

## Why code-switching is hard for ASR

- **Language identification fights you.** Many systems detect one language per file or per segment, then decode everything as that language. English words in a Hindi-detected segment get forced into Hindi spellings, and vice versa.
- **Vocabulary is mixed.** Technical and business terms ("deployment", "sign off", "pipeline") arrive in English inside Hindi grammar.
- **Training data is scarce.** Clean Hindi and clean English audio are abundant. Natural code-switched conversational audio with good transcripts is much rarer.
- **There's no single correct spelling.** Which brings us to the real problem.

## The script problem

The same spoken Hinglish sentence can be written at least three valid ways:

1. **All Devanagari:** "कल का डिप्लॉयमेंट थोड़ा डिले हो गया"
2. **All Roman (Latin script):** "kal ka deployment thoda delay ho gaya"
3. **Mixed script:** "कल का deployment थोड़ा delay हो गया"

If your reference transcript is in one style and the model outputs another, **word error rate will look catastrophic even when the transcription is perfect.** Every word counts as a substitution.

So the first rule of Hinglish evaluation: **decide the target script convention before you write a single reference transcript, and normalize both sides to it.** For meeting notes read by people who type in Roman script on their phones, Roman or mixed script is usually what users want. For formal Hindi documents, Devanagari may be right. There's no universal answer, but there must be *an* answer.

## Building the harness

```bash
pip install jiwer
```

### 1. A test set that looks like your users

Record or collect 20 to 50 short clips (30 to 90 seconds) of real conversational audio: meetings, calls, interviews, with consent. Include:

- pure Hindi, pure English and heavily mixed clips;
- a range of accents and speaking speeds;
- laptop microphones, phone audio and conference-room audio.

Have a fluent bilingual person transcribe each clip **in your chosen script convention**. Store them as pairs:

```
data/
  clip_001.wav
  clip_001.ref.txt
  ...
```

### 2. Normalization

WER is extremely sensitive to casing, punctuation and spacing. Normalize consistently:

```python
import re
import unicodedata

def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.lower()
    text = re.sub(r"[^\w\sऀ-ॿ]", " ", text)   # keep word chars and Devanagari
    text = re.sub(r"\s+", " ", text).strip()
    return text
```

If your convention is Roman script but some system outputs Devanagari, you'll need a transliteration step before scoring. Be explicit about whether you're scoring the system's raw output or its output after transliteration. They answer different questions.

### 3. Score WER and CER

```python
from pathlib import Path
import jiwer

def score(refs: list[str], hyps: list[str]) -> dict:
    refs = [normalize(r) for r in refs]
    hyps = [normalize(h) for h in hyps]
    return {
        "wer": jiwer.wer(refs, hyps),
        "cer": jiwer.cer(refs, hyps),
    }

def load_pairs(data_dir: str, hyp_suffix: str):
    refs, hyps = [], []
    for ref_path in sorted(Path(data_dir).glob("*.ref.txt")):
        hyp_path = ref_path.with_name(ref_path.name.replace(".ref.txt", hyp_suffix))
        refs.append(ref_path.read_text(encoding="utf-8"))
        hyps.append(hyp_path.read_text(encoding="utf-8"))
    return refs, hyps

refs, hyps = load_pairs("data", ".system_a.txt")
print(score(refs, hyps))
```

**Report CER alongside WER.** Character error rate is more forgiving of small spelling variation ("thoda" vs "thora"), which is common in romanized Hindi. If WER is high but CER is low, the system is probably right but spelling things differently from your references.

### 4. Break results down by switch density

An average hides the problem you care about. Tag each clip with a rough code-switch ratio (the share of words in the minority language) and report per bucket:

```python
def english_ratio(ref: str, english_vocab: set[str]) -> float:
    words = normalize(ref).split()
    return sum(w in english_vocab for w in words) / max(len(words), 1)
```

A crude English wordlist is enough for bucketing. You'll often find a system that scores well on pure Hindi and pure English and falls apart in the 20 to 50% mixed bucket, which is exactly where real meetings live.

## What to look for beyond WER

Error rates aren't the whole story for meeting notes. Also check:

- **Named entities**: people, companies, product names. A single wrong client name is worse than five wrong filler words.
- **Numbers and dates**: "28 tareekh" vs "the 28th". Downstream action items depend on these.
- **English technical terms inside Hindi sentences**: are they preserved, or transliterated into nonsense?
- **Summary quality**: if the transcript feeds an LLM summary, evaluate the summary too. Sometimes a summarizer recovers from transcript errors; sometimes it confidently invents things.

## A note on choosing a tool

If you're evaluating products rather than models, ask vendors three questions:

1. Do you support code-switched audio in one recording, or do I pick one language?
2. What script does the transcript come out in, and can I choose?
3. Can I test with my own audio before committing?

Lynkk, for example, offers a dedicated [Hinglish transcription mode](https://lynkk.ai/features/hinglish-transcription) for people who switch between Hindi and English mid-sentence, alongside [17 languages](https://lynkk.ai/features/multilingual-transcription) with auto-detect. Whatever you evaluate, run it on your own clips with the harness above. For non-technical readers looking for free options, the Lynkk blog has a guide to [Hindi transcription in India](https://lynkk.ai/blog/hindi-transcription), including Google Docs, YouTube and Hinglish meetings.

## Summary

- Code-switching breaks the one-language-per-file assumption.
- Fix the script convention first, or your WER is meaningless.
- Report WER and CER, and break results down by switch density.
- Check names, numbers and technical terms, not just averages.

---

*Written by the Lynkk team with AI assistance.*
