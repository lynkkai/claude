---
platform: Hashnode
title: "Capturing System Audio on macOS Without a Virtual Driver: Core Audio Taps (macOS 14.2+)"
subtitle: "How bot-free meeting recorders hear Zoom, Teams and FaceTime calls on a Mac, and the three generations of APIs that got us here."
slug: capture-system-audio-macos-core-audio-taps
tags: [macos, swift, audio, core-audio, apple]
target_queries: ["record system audio mac", "ai note taker without a bot", "dictation on mac", "zoom meeting recorder mac"]
evidence: "GSC: /download 58 impr at 6.9% CTR (high intent); /blog/dictation-on-mac 30 impr at avg 34.7; 'meeting bot vs local recording' and 'ai notetaker no meeting bot' appear in Ubersuggest long tail; bot-free capture is a stated Lynkk differentiator (Mac app records with no bot, requires macOS 14.2+)"
main_site_links:
  - https://lynkk.ai/download
  - https://lynkk.ai/features/dictation
  - https://lynkk.ai/blog/dictation-on-mac
canonical: "none (original article, do not set a canonical)"
cover_image: "A MacBook with a stethoscope icon on the speaker grille"
status: draft
---

# Capturing System Audio on macOS Without a Virtual Driver: Core Audio Taps (macOS 14.2+)

For years, recording "what the Mac is playing" meant installing a virtual audio driver, rerouting your output through it and hoping users understood the setup. That's why so many meeting tools chose to send a bot into the call instead.

Since **macOS 14.2**, Apple ships a first-party API for this: **Core Audio process taps**. An app can tap the audio output of specific processes (or everything except some processes) and read it like an input device, with a system permission prompt instead of a kernel extension.

This post explains the three generations of approaches, then sketches the tap-based one in Swift.

> The code below is a sketch with error handling removed for readability. Apple's sample code for Core Audio taps is the authoritative reference. And as always with recording: tell the people on the call.

## Three generations of "record the Mac's audio"

**1. Virtual audio drivers (any macOS).** Tools like BlackHole or Loopback install an audio device. Users route output to it (often through a multi-output device so they can still hear). It works, but setup is fragile and confusing, and it needs a driver install.

**2. ScreenCaptureKit audio (macOS 13+).** `SCStream` can capture app or display audio alongside screen content by setting `capturesAudio = true` on the stream configuration. No driver needed, but it requires the **Screen Recording** permission, which is a big ask for an app that only wants audio and makes users understandably nervous.

**3. Core Audio process taps (macOS 14.2+).** Purpose-built for audio. The permission is "System Audio Recording Only", which is a much easier conversation with users, and you can target specific processes.

That third option is why a number of Mac meeting recorders list **macOS 14.2 or later** as a requirement.

## How a process tap works

The flow has four pieces:

1. **Describe the tap** with `CATapDescription`: which processes to include or exclude, mono or stereo, and whether to mute the original output.
2. **Create the tap** with `AudioHardwareCreateProcessTap`, which returns an `AudioObjectID`.
3. **Wrap it in a private aggregate device** whose tap list contains your tap's UUID.
4. **Read buffers** from the aggregate device with an IO proc, like any input device.

## Step 1: Find the process you want

Taps target Core Audio *process objects*, not PIDs. Translate a PID with `kAudioHardwarePropertyTranslatePIDToProcessObject`:

```swift
import CoreAudio

func audioProcessObject(for pid: pid_t) -> AudioObjectID? {
    var address = AudioObjectPropertyAddress(
        mSelector: kAudioHardwarePropertyTranslatePIDToProcessObject,
        mScope: kAudioObjectPropertyScopeGlobal,
        mElement: kAudioObjectPropertyElementMain)
    var pid = pid
    var objectID = AudioObjectID(kAudioObjectUnknown)
    var size = UInt32(MemoryLayout<AudioObjectID>.size)
    let status = AudioObjectGetPropertyData(
        AudioObjectID(kAudioObjectSystemObject), &address,
        UInt32(MemoryLayout<pid_t>.size), &pid, &size, &objectID)
    return status == noErr && objectID != kAudioObjectUnknown ? objectID : nil
}
```

Get the PID from `NSRunningApplication` for the meeting app (for example by bundle identifier). For a browser-based meeting you'd tap the browser process.

## Step 2: Create the tap

```swift
let processes = [zoomProcessObject]            // [AudioObjectID]
let description = CATapDescription(stereoMixdownOfProcesses: processes)
description.uuid = UUID()
description.isPrivate = true
description.muteBehavior = .unmuted            // user keeps hearing the call

var tapID = AudioObjectID(kAudioObjectUnknown)
let err = AudioHardwareCreateProcessTap(description, &tapID)
```

Alternatively, `CATapDescription(stereoGlobalTapButExcludeProcesses: [ownProcess])` taps everything except your own app, which avoids recording your app's sounds.

## Step 3: Put the tap in a private aggregate device

```swift
let aggregateUID = UUID().uuidString
let config: [String: Any] = [
    kAudioAggregateDeviceNameKey: "Meeting Tap",
    kAudioAggregateDeviceUIDKey: aggregateUID,
    kAudioAggregateDeviceIsPrivateKey: true,
    kAudioAggregateDeviceTapAutoStartKey: true,
    kAudioAggregateDeviceTapListKey: [
        [kAudioSubTapUIDKey: description.uuid.uuidString]
    ],
]

var aggregateID = AudioObjectID(kAudioObjectUnknown)
AudioHardwareCreateAggregateDevice(config as CFDictionary, &aggregateID)
```

A private aggregate device doesn't appear in the user's Sound settings, which is what you want.

## Step 4: Read audio

```swift
var procID: AudioDeviceIOProcID?
let queue = DispatchQueue(label: "tap.io")

AudioDeviceCreateIOProcIDWithBlock(&procID, aggregateID, queue) { _, inInputData, _, _, _ in
    // inInputData is an UnsafePointer<AudioBufferList> of float samples.
    // Copy it out quickly: append to a ring buffer, an AVAudioFile, or an encoder.
    writer.append(inInputData)
}
AudioDeviceStart(aggregateID, procID)
```

Read the tap's format (`kAudioTapPropertyFormat`) so you know the sample rate and channel layout before writing files. When you're done, stop the device, destroy the IO proc, the aggregate device and the tap, in that order.

## Permission and Info.plist

Add `NSAudioCaptureUsageDescription` to your Info.plist with a clear, honest sentence ("Lets the app record the audio of calls you choose to record, so it can write your meeting notes"). The first tap creation triggers the system prompt. If the user declines, creation fails and you should explain how to re-enable it in System Settings, Privacy and Security.

## Add the microphone as a second channel

The tap gives you the *remote* side of the call. Capture the user's microphone separately (with `AVAudioEngine`'s input node or an `AVCaptureSession`) and store it on its own channel or track. As with browser recorders, two channels mean you always know which speech is the user's, and you only diarize the remote side.

## Detecting calls

Most bot-free recorders don't record all the time. They watch for a meeting app starting a call (often by watching for an app to begin using the microphone, together with knowing which apps are meeting apps) and then *ask* the user: record, or not now. Asking is better UX and better ethics than auto-recording everything.

## Production notes

- **Sample-rate mismatches**: the tap's rate may differ from the mic's. Resample before mixing.
- **Device changes**: AirPods connecting mid-call changes the output device. Listen for property changes and rebuild if needed.
- **Offline resilience**: write to disk continuously so a dropped network connection or crash doesn't lose the recording; upload later.
- **Apple silicon and OS version**: gate the feature on macOS 14.2+ and fail gracefully below that.

## Where you'll see this in practice

Lynkk's [Mac app](https://lynkk.ai/download) is one example of a bot-free recorder: it notices calls in Zoom, Teams, Webex, FaceTime, Slack huddles and WhatsApp, plus Meet, Zoom, Teams and Webex in the browser, asks whether to record (or records automatically, if the user chooses), and keeps the microphone and the call audio on separate channels. It requires Apple silicon and macOS 14.2 or later. The same app does [dictation](https://lynkk.ai/features/dictation) in any text field, which is a different audio path: microphone in, text out. If you just want to use built-in dictation, here's a guide to [dictation on Mac](https://lynkk.ai/blog/dictation-on-mac) and how to fix it when it stops working.

---

*Written by the Lynkk team with AI assistance. Core Audio tap APIs as available in macOS 14.2 and later; check Apple's documentation for current signatures.*
