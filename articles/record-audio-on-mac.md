---
title: "How to Record Audio on a Mac, Including System Audio"
meta_title: "How to Record Audio on a Mac (Including System Audio)"
meta_description: "How to record audio on a Mac with QuickTime, Voice Memos and Shift-Command-5, why macOS blocks system audio, and how to capture internal sound properly."
slug: "record-audio-on-mac"
canonical: "https://lynkk.ai/blog/record-audio-on-mac"
brand: "Lynkk"
author: "Samarth Wagh"
author_url: "https://lynkk.ai/blog/authors/samarth-wagh"
generated_date: "2026-11-04"
cluster: "Dictation and transcription"
internal_link_target: "https://lynkk.ai/features/meeting-bot"
featured_image_path: "PENDING: no Lynkk image-gen skill on this machine"
featured_image_alt: "Recording audio on a Mac with QuickTime Player and the Shift-Command-5 screen recording toolbar"
keywords:
  - "record audio on a mac"
  - "how to record audio on a mac"
  - "record system audio on a mac"
  - "record internal audio on a mac"
  - "quicktime player audio recording"
  - "screen record with audio on a mac"
  - "record audio without a microphone"
  - "voice memos on mac"
  - "record computer audio"
tldr: "To record audio on a Mac, use QuickTime Player (File, then New Audio Recording), Voice Memos, or Shift-Command-5 for screen recordings with a microphone. None of them capture system audio on their own, because macOS treats internal sound as a separate input. For that you need a virtual audio device, or an app that records the call directly."
---

# How to Record Audio on a Mac, Including System Audio

By [Samarth Wagh](https://lynkk.ai/blog/authors/samarth-wagh) · 4 November 2026 · Steps checked against Apple's macOS User Guide in November 2026

> **Quick answer:** There are **3** built-in ways to record audio on a Mac: QuickTime Player (File, then New Audio Recording), Voice Memos, and **Shift-Command-5** for a screen recording with your microphone. None of them capture system audio by itself, so for internal sound you need a virtual audio device or an app that records the source directly.

Capturing your own voice takes about 10 seconds. Recording what the Mac is playing is the part that trips people up. The sound from a video call, a video, a browser tab. That's a deliberate macOS design choice, not a bug.

## How do you record audio on a Mac with QuickTime Player?

QuickTime Player audio recording is the built-in route most people reach for, and it takes 3 clicks.

Open QuickTime Player, choose File, then New Audio Recording, then click the Record button. Apple's guide says you can pick your input from the Capture Device Selection pop-up button, and choose File, then Save to name the file and pick where it goes, [per Apple's QuickTime guide](https://support.apple.com/guide/quicktime-player/record-audio-qtpf25d6f827/mac).

QuickTime gives you 2 quality settings. The difference matters if you're short on disk space:

| Setting | Format | Use it for |
|---|---|---|
| High | 44100 Hz AAC | Voice notes, interviews, anything you'll share |
| Maximum | 44100 Hz uncompressed Linear PCM 24-bit AIFF-C | Music or audio you plan to edit |

Apple warns that maximum-quality recordings are uncompressed and "can use large amounts of storage space". For speech? High, almost every time.

## How do you record a voice memo on a Mac?

Open Voice Memos and click the Record button. Apple describes it as a way to "easily record meetings, lectures, song ideas, and more", and the app also includes editing and a transcription view, [per Apple's Voice Memos guide](https://support.apple.com/guide/voice-memos/welcome/mac).

Voice Memos on Mac suits quick captures where file settings don't matter. QuickTime suits recordings you'll edit or hand to someone else, because you pick the format and where it lands.

## How do you screen record with audio on a Mac?

Press Shift-Command-5 to open the Screenshot toolbar. Click Options, then pick your microphone under Microphone so a checkmark appears, [per Apple's guide](https://support.apple.com/guide/mac-help/take-screenshots-or-screen-recordings-mh26782/mac). Selecting None turns the microphone off.

That menu covers microphone input only. Apple's page says nothing about capturing computer audio, and that omission is the single most common reason a screen recording comes back silent.

## Why can't you record system audio on a Mac?

You can't record system audio on a Mac with the built-in tools because macOS doesn't expose the computer's own output as a recording input. An app that asks for "the microphone" can't hear what your speakers are playing. It's a privacy and copyright boundary. Not a missing feature.

So QuickTime, Voice Memos and Shift-Command-5 all record whatever reaches your mic. Record a video call this way with headphones on, and you capture your own voice and silence from the other side.

## How do you record internal audio on a Mac?

To record internal audio on a Mac, you need a virtual audio device that presents system output as an input, or an app that captures the source directly. It's the same job as trying to record computer audio on any locked-down operating system. There are 3 realistic routes.

| Route | How it works | Trade-off |
|---|---|---|
| Virtual audio driver | Installs a loopback device your recorder selects as input | Free options exist, but setup is fiddly and you may not hear the audio yourself |
| An app that records the source | The app captures the call or tab itself, no driver needed | Only works for what that app supports |
| Record the room | A second device records the speakers out loud | Quality drops, and it picks up the room |

For a one-off, the virtual driver route is fine. Recording calls every week? An app built for it is less fragile, because audio drivers tend to break with macOS updates.

## How do you record a meeting on a Mac with both sides?

Use a tool that records the call itself, so you capture every speaker rather than just your microphone. This is the system audio problem in its most common form. It's why meeting recordings made with QuickTime are half a conversation.

Lynkk does it 2 ways: a [meeting bot](https://lynkk.ai/features/meeting-bot) that joins Zoom, Google Meet or Teams as a visible participant, or the Mac app recording the call on your laptop with no bot at all. Each recording becomes a transcript, a summary and action items. Tell everyone first, because some places need consent from every participant, as our guide to [whether it's legal to record a meeting](https://lynkk.ai/blog/is-it-legal-to-record-a-meeting) explains.

## How do you record sound on a Mac without a microphone?

People who want to record audio without a microphone usually mean 1 of 2 things. Recording the Mac's own output, which needs the internal-audio route above. Or using an external device instead of the built-in mic. Both are solvable, but they're different problems.

If what you actually want is better audio, plug in a USB microphone or headset and select it under System Settings, then Sound, then Input. That jump in quality beats any software setting.

## How do you fix a Mac recording with no sound?

Work through 4 checks in order, because the cause is almost always one of them.

1. **Input source:** System Settings, then Sound, then Input. Does the level meter move when you speak?
2. **Permission:** Privacy and Security, then Microphone. Is the app allowed?
3. **The right input in the app:** QuickTime's Capture Device pop-up, or the Options menu in Shift-Command-5.
4. **System audio:** if you expected the Mac's own sound, that's the limitation above, not a fault.

## How do you turn a Mac recording into text?

Run it through a transcription tool, or record with something that transcribes as it goes. Apple's Voice Memos includes a transcription view, and Notes can record audio with a live, searchable transcript.

For recordings you already have, our guide to [transcribing audio to text](https://lynkk.ai/blog/transcribe-audio-to-text) covers the options, and [voice memo transcription](https://lynkk.ai/blog/voice-memo-transcription) covers files from an iPhone. If you want the text without the extra step, Lynkk writes up each recording automatically, and [dictation](https://lynkk.ai/features/dictation) types straight into any Mac app while you talk.

## FAQ

### Does Mac screen recording capture computer audio?

No, not on its own. The Shift-Command-5 toolbar only offers microphone input under Options, so a screen recording captures your voice but not the sound your Mac is playing. To include system audio you need a virtual audio device, or an app that records the source directly.

### What format does QuickTime save audio in?

QuickTime offers two quality settings. High records 44100 Hz AAC, which is compressed and fine for speech. Maximum records 44100 Hz uncompressed Linear PCM 24-bit AIFF-C, which Apple warns can use large amounts of storage. Choose High unless you plan to edit the audio heavily afterwards.

### Can you record a Zoom call on a Mac?

Yes, in three ways: Zoom's own recording if the host allows it, a notetaker app that joins the call, or a Mac app that records the call locally. QuickTime alone won't work well, because it captures only your microphone, so the other participants are missing unless you use speakers.

### How long can a recording be?

There's no built-in time limit in QuickTime or Voice Memos, so the practical limit is free disk space. Uncompressed maximum-quality recordings fill a disk far faster than AAC. For long sessions, record at High quality and check you have several gigabytes free before you start.

### Where do Mac audio recordings get saved?

QuickTime asks you: choose File, then Save, then name the recording and pick the location. Voice Memos keeps recordings inside the app, where you can play, rename or export them. Screen recordings from Shift-Command-5 save to the location set in the Options menu, which defaults to the desktop.

### Can you record audio and video at the same time on a Mac?

Yes. Shift-Command-5 records the screen with microphone audio, and QuickTime Player can make a movie recording using your camera and a microphone. Neither captures system audio, so if you need the sound from a video or a call in the recording, add a virtual audio device.

## Conclusion

For your own voice, QuickTime or Voice Memos takes seconds flat. For the Mac's own sound, you need a virtual audio device or an app that records the source, because macOS won't hand system audio to a recorder. For calls, skip the workaround and record the meeting directly.

**Try Lynkk.** It records Zoom, Meet and Teams calls, with or without a bot, and writes up every one. [Start for free](https://lynkk.ai/).

---CITATIONS---
1. Apple, "Record audio in QuickTime Player on Mac" (File then New Audio Recording; Capture Device Selection; High = 44100 Hz AAC, Maximum = uncompressed Linear PCM 24-bit AIFF-C): https://support.apple.com/guide/quicktime-player/record-audio-qtpf25d6f827/mac
2. Apple, "Take screenshots or screen recordings on Mac" (Shift-Command-5; Options then Microphone; None turns it off): https://support.apple.com/guide/mac-help/take-screenshots-or-screen-recordings-mh26782/mac
3. Apple, "Voice Memos User Guide for Mac" (record meetings, lectures, song ideas; edit and transcription topics): https://support.apple.com/guide/voice-memos/welcome/mac
4. Lynkk meeting bot and Mac recording: https://lynkk.ai/features/meeting-bot

---SCHEMA---
```json
[
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "How to Record Audio on a Mac, Including System Audio",
    "description": "How to record audio on a Mac with QuickTime, Voice Memos and Shift-Command-5, why macOS blocks system audio, and how to capture internal sound properly.",
    "inLanguage": "en",
    "author": {
      "@type": "Person",
      "name": "Samarth Wagh",
      "url": "https://lynkk.ai/blog/authors/samarth-wagh"
    },
    "publisher": {
      "@type": "Organization",
      "name": "Lynkk",
      "url": "https://lynkk.ai/"
    },
    "datePublished": "2026-11-04",
    "dateModified": "2026-11-04",
    "mainEntityOfPage": "https://lynkk.ai/blog/record-audio-on-mac"
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://lynkk.ai/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Blog",
        "item": "https://lynkk.ai/blog"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "How to Record Audio on a Mac, Including System Audio",
        "item": "https://lynkk.ai/blog/record-audio-on-mac"
      }
    ]
  }
]
```

---FAQ_JSON---
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does Mac screen recording capture computer audio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, not on its own. The Shift-Command-5 toolbar only offers microphone input under Options, so a screen recording captures your voice but not the sound your Mac is playing. To include system audio you need a virtual audio device, or an app that records the source directly."
      }
    },
    {
      "@type": "Question",
      "name": "What format does QuickTime save audio in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "QuickTime offers two quality settings. High records 44100 Hz AAC, which is compressed and fine for speech. Maximum records 44100 Hz uncompressed Linear PCM 24-bit AIFF-C, which Apple warns can use large amounts of storage. Choose High unless you plan to edit the audio heavily afterwards."
      }
    },
    {
      "@type": "Question",
      "name": "Can you record a Zoom call on a Mac?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, in three ways: Zoom's own recording if the host allows it, a notetaker app that joins the call, or a Mac app that records the call locally. QuickTime alone won't work well, because it captures only your microphone, so the other participants are missing unless you use speakers."
      }
    },
    {
      "@type": "Question",
      "name": "How long can a recording be?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There's no built-in time limit in QuickTime or Voice Memos, so the practical limit is free disk space. Uncompressed maximum-quality recordings fill a disk far faster than AAC. For long sessions, record at High quality and check you have several gigabytes free before you start."
      }
    },
    {
      "@type": "Question",
      "name": "Where do Mac audio recordings get saved?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "QuickTime asks you: choose File, then Save, then name the recording and pick the location. Voice Memos keeps recordings inside the app, where you can play, rename or export them. Screen recordings from Shift-Command-5 save to the location set in the Options menu, which defaults to the desktop."
      }
    },
    {
      "@type": "Question",
      "name": "Can you record audio and video at the same time on a Mac?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Shift-Command-5 records the screen with microphone audio, and QuickTime Player can make a movie recording using your camera and a microphone. Neither captures system audio, so if you need the sound from a video or a call in the recording, add a virtual audio device."
      }
    }
  ]
}
```
