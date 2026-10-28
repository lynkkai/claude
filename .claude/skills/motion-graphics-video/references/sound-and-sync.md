# Sound and sync

Motion that lands on a beat reads as designed. Motion that drifts against the music reads
as a template with a song on top. The picture is the master: build the grid, then retime
the picture to it.

## 1. The grid

Pick a tempo from the energy you want: 90 to 100 BPM calm and premium, 110 to 125 BPM
confident product film, 130 plus for energetic social cuts. At 120 BPM a beat is 0.5 s
and a bar is 2.0 s, which is why 120 is a convenient default: shots become clean
multiples of bars.

Write `beats.json` and have the timeline read it, so picture and sound share one source
of truth:

```json
{
  "bpm": 120,
  "duration": 15,
  "beats":     [0.0, 0.5, 1.0, 1.5, 2.0],
  "downbeats": [0.0, 2.0, 4.0, 6.0],
  "hits": [
    { "t": 2.0,  "name": "container-morph", "kind": "whoosh" },
    { "t": 4.0,  "name": "cursor-press",    "kind": "click" },
    { "t": 13.5, "name": "logo-lockup",     "kind": "thump" }
  ]
}
```

Retiming rule: snap shot boundaries to downbeats, snap accents (text entrances, morphs,
cursor presses) to beats, and let continuous motion run freely between them. Do not snap
everything, or the piece turns metronomic.

## 2. Score in code

A synthesized track is free, royalty clear, exactly as long as the film, and can be
regenerated when the edit changes. Render the audio offline in Node with an offline audio
graph or by writing PCM samples to a WAV, then encode. Keep it simple: a sub pulse on
downbeats, a filtered pad holding the harmony, a short percussive layer, and arrangement
by removing layers rather than adding complexity. Leave the last half second to breathe.

If the brand needs licensed music, ask for the track first and derive `beats.json` from
it with an onset detector instead of inventing a tempo.

## 3. UI sound effects

Synthesize these rather than sourcing clips, and keep them short and quiet (they sit 12
to 18 dB under the score):

- **click**: 8 to 15 ms, filtered noise burst with a fast decay, on cursor presses
- **whoosh**: 120 to 250 ms, band-passed noise with a pitch sweep, on container morphs
  and camera moves
- **thump**: 150 to 300 ms, low sine with a pitch drop, on the logo and on the final card
- **tick**: tiny, for counters and list items appearing in a stagger

Place one per hit in `beats.json`. A sound with no matching motion is noise, and motion
with no sound on a strong accent feels mute.

## 4. Voiceover

Write the script against the beat grid, not as prose to be squeezed in later. About 2.0
to 2.2 words per second is comfortable; above that it sounds hurried. Leave 300 ms of
silence after each line so the picture can land.

Generate it with whatever text to speech the session offers. Check for an MCP server
first (voice providers often ship one) and ask before anything that spends the user's
money or needs a new account. If a cloned voice is requested, that is the user's own
voice or one they have rights to, and only with their say-so.

Duck the score 6 to 9 dB under speech rather than lowering it throughout.

## 5. Mixing

```bash
# score + effects + voice into one track
ffmpeg -i score.wav -i sfx.wav -i vo.wav \
  -filter_complex "[0:a]volume=0.55[a0];[1:a]volume=0.35[a1];[2:a]volume=1.0[a2];\
                   [a0][a1][a2]amix=inputs=3:normalize=0,alimiter=limit=0.95[out]" \
  -map "[out]" mix.wav

# mux onto the silent render
ffmpeg -i film-silent.mp4 -i mix.wav -c:v copy -c:a aac -b:a 192k -shortest film.mp4
```

Then watch it with sound. Sync errors are obvious to the ear and invisible in the
waveform.
