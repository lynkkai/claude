---
platform: Hashnode
title: "Recording Tab Audio and the Microphone in a Chrome MV3 Extension"
subtitle: "tabCapture, offscreen documents and a two-channel recording: how browser-based meeting recorders work without a bot in the call."
slug: record-tab-audio-chrome-mv3-extension
tags: [chrome-extension, javascript, web-audio, webrtc, browser]
target_queries: ["chrome extension record meeting audio", "how to transcribe zoom meetings", "google meet transcription", "zoom web client recording"]
evidence: "GSC: /blog/how-to-transcribe-zoom-meetings 153 impr at avg 47.6; /features/chrome-extension 6 impr at 19.5 (new page, needs links); 'google meet transcription' 29 impr; developer-intent bot queries total 399 impr. Topic explains bot-free browser capture, a Lynkk differentiator"
main_site_links:
  - https://lynkk.ai/features/chrome-extension
  - https://lynkk.ai/blog/how-to-transcribe-zoom-meetings
  - https://lynkk.ai/blog/zoom-meeting-recorders
canonical: "none (original article, do not set a canonical)"
cover_image: "Two audio waveforms, labelled 'tab' (left) and 'mic' (right), merging into one stereo file"
status: draft
---

# Recording Tab Audio and the Microphone in a Chrome MV3 Extension

Browser-based meeting recorders don't need a bot in the call. If the meeting runs in a Chrome tab (Google Meet, the Zoom web client, Teams on the web), an extension can capture that tab's audio plus the user's microphone and produce a recording with no extra participant.

Under Manifest V3 this got trickier, because service workers can't touch media streams. This post shows the pattern that works today: **`chrome.tabCapture` + an offscreen document + a two-channel `MediaRecorder`.**

> Recording other people has legal and ethical requirements that vary by place. Build your UI so the user is reminded to tell participants they're recording, every time.

## Architecture

```
popup / action click (user gesture)
        │
        ▼
service worker ── tabCapture.getMediaStreamId(tabId) ──► streamId
        │
        ▼
offscreen document (has DOM + media APIs)
   getUserMedia(tab streamId) + getUserMedia(mic)
   Web Audio graph: tab ─► left, mic ─► right
   MediaRecorder ─► chunks ─► upload or IndexedDB
```

Since Chrome 116, `chrome.tabCapture.getMediaStreamId` can be called from the service worker and the resulting stream ID used in an offscreen document. That's what makes this pattern possible under MV3, and why tab recorders tend to require Chrome 116 or later.

## manifest.json

```json
{
  "manifest_version": 3,
  "name": "Tab Recorder Demo",
  "version": "0.1.0",
  "minimum_chrome_version": "116",
  "permissions": ["tabCapture", "offscreen", "storage"],
  "background": { "service_worker": "sw.js" },
  "action": { "default_title": "Record this tab" }
}
```

## Service worker: get a stream ID and hand it off

```js
// sw.js
async function ensureOffscreen() {
  const contexts = await chrome.runtime.getContexts({ contextTypes: ["OFFSCREEN_DOCUMENT"] });
  if (contexts.length) return;
  await chrome.offscreen.createDocument({
    url: "offscreen.html",
    reasons: ["USER_MEDIA"],
    justification: "Record tab and microphone audio for meeting notes",
  });
}

chrome.action.onClicked.addListener(async (tab) => {
  await ensureOffscreen();
  const streamId = await chrome.tabCapture.getMediaStreamId({ targetTabId: tab.id });
  chrome.runtime.sendMessage({ type: "start", streamId });
});
```

The action click provides the user gesture that `tabCapture` requires. You can't start capture silently in the background, and that's a good thing.

## Offscreen document: build a two-channel recording

```html
<!-- offscreen.html -->
<script src="offscreen.js"></script>
```

```js
// offscreen.js
let recorder, ctx, chunks = [];

chrome.runtime.onMessage.addListener(async (msg) => {
  if (msg.type === "start") await start(msg.streamId);
  if (msg.type === "stop") recorder?.stop();
});

async function start(streamId) {
  const tabStream = await navigator.mediaDevices.getUserMedia({
    audio: { mandatory: { chromeMediaSource: "tab", chromeMediaSourceId: streamId } },
  });
  const micStream = await navigator.mediaDevices.getUserMedia({
    audio: { echoCancellation: true, noiseSuppression: true },
  });

  ctx = new AudioContext();
  const tabSrc = ctx.createMediaStreamSource(tabStream);
  const micSrc = ctx.createMediaStreamSource(micStream);

  // 1. Keep the meeting audible. Capturing a tab mutes it unless you play it back.
  tabSrc.connect(ctx.destination);

  // 2. Merge into stereo: tab on channel 0 (left), mic on channel 1 (right).
  const merger = ctx.createChannelMerger(2);
  tabSrc.connect(merger, 0, 0);
  micSrc.connect(merger, 0, 1);

  const dest = ctx.createMediaStreamDestination();
  merger.connect(dest);

  recorder = new MediaRecorder(dest.stream, { mimeType: "audio/webm;codecs=opus" });
  recorder.ondataavailable = (e) => e.data.size && chunks.push(e.data);
  recorder.onstop = finish;
  recorder.start(5000); // emit a chunk every 5 s so a crash loses little
}

async function finish() {
  const blob = new Blob(chunks, { type: "audio/webm" });
  chunks = [];
  // upload(blob) or store it in IndexedDB, then release devices
  ctx?.close();
}
```

### Why two channels?

Putting the remote audio and the local microphone on separate channels is a cheap, powerful trick:

- **You know which speech is the user's** with zero diarization: it's whatever is on the mic channel.
- **You only need to diarize the remote side**, which is easier with fewer voices.
- **Echo is easier to handle**, because you can compare the channels.

Desktop meeting recorders often use the same idea for the same reasons.

### Don't forget playback

The single most common bug: when you capture a tab's audio, Chrome stops playing it to the user. If you don't connect the captured stream back to `ctx.destination`, the user suddenly can't hear the meeting. Always route it back.

## Microphone permission in an offscreen document

Offscreen documents can't show permission prompts. If the user hasn't granted microphone access to your extension yet, `getUserMedia` for the mic fails. The usual fix is to open a visible extension page once (for example an onboarding tab) that calls `getUserMedia({ audio: true })`, so the user grants mic access to the extension's origin. After that, the offscreen document can use it.

## Production concerns

- **Chunked uploads.** Long meetings produce big files. Upload chunks as you go, or write them to IndexedDB, so a crash or closed laptop doesn't lose the whole recording.
- **Tab closed or navigated.** Listen for the tab stream's tracks ending (`track.onended`) and stop cleanly.
- **Detecting meetings.** You can match tab URLs (`meet.google.com/*`, Zoom's web client paths, Teams web) to suggest recording, but let the user decide.
- **Other Chromium browsers.** The same APIs generally work in Edge, Brave and Arc, but test each.
- **Disclosure.** Show a persistent indicator while recording, and remind users to tell participants.

## When a browser extension is the right tool

An extension is a good fit when meetings happen in the browser and you don't want a bot. It can't capture desktop apps (the native Zoom or Teams clients), and it can't record in-person conversations. That's where desktop apps or calendar bots come in.

Lynkk's [Chrome extension](https://lynkk.ai/features/chrome-extension) is a production example of this pattern: it records Google Meet, the Zoom web client and Microsoft Teams from the tab, with the tab and microphone on two channels, audio only, on Chrome 116 or later. If you're comparing ways to capture meetings rather than building one, see [3 ways to transcribe Zoom meetings](https://lynkk.ai/blog/how-to-transcribe-zoom-meetings) and this comparison of [Zoom meeting recorders](https://lynkk.ai/blog/zoom-meeting-recorders), including how to record when you're not the host.

---

*Written by the Lynkk team with AI assistance. Chrome extension APIs as of October 2026.*
