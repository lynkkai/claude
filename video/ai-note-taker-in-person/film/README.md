# The graphics, as code

The Remi graphics for the 2:00 in-person video, built on the Lynkk Remi video kit's engine in a new
1920x1080 `Wide` format. `src/` is the whole film: the timeline, the scenes and the shared parts.

## What renders

One composition, `Wide`, 1920x1080 at 30 fps, 3600 frames. It holds the ten graphics at their timecodes and,
where the team's footage goes, a slate that names the shot and prints the line said over it. That way the whole
two minutes plays against the soundtrack before anyone books a room.

| File | What it draws |
|---|---|
| `timing.ts` | the clock: 60 bars, every scene start, stamp and impact |
| `Teaser.tsx` | the timeline, and which slate stands in for which shot |
| `ui/parts.tsx` | the plate, the chapter card, board headings, the footage slate |
| `scenes/Hook.tsx` | G1, the call window shattering into the room |
| `scenes/Boards.tsx` | G3 laptop / phone / recorder, and G8 the six picks |
| `scenes/MicMap.tsx` | G4, the table from above with the three bad placements |
| `scenes/MacBits.tsx` | G5a Record now, G5b the recording column, G5c the note |
| `scenes/Labels.tsx` | G6, the transcript split by speaker, and a rename |
| `scenes/Offline.tsx` | G7, Wi-Fi off and the upload resuming |
| `scenes/End.tsx` | G9, the end card: Get Lynkk Pro, $4 a month, lynkk.ai |

`remi/`, `fx/`, `mac/`, `brand/` and `lib.ts` are the kit's own parts, unchanged except for the `wide` format
added to `lib.ts` and `index.tsx`.

## Rendering it

This folder is a film inside the kit, not a standalone project: it needs the kit's `node_modules`.

```bash
cp -R film <kit>/films/in-person-note-taker
cd <kit>/films/in-person-note-taker && npm ci
```

Then, from that folder:

```bash
npx remotion render src/index.tsx Wide out/picture-wide.mp4 --codec h264 --crf 17 --muted
```

Check frames before a long render:

```bash
npx remotion still src/index.tsx Wide out/f1440.png --frame=1440
```

Put the soundtrack on:

```bash
ffmpeg -i out/picture-wide.mp4 -i ../../audio/scratch-mix.wav -c:v copy -c:a aac -b:a 256k -shortest out/previz.mp4
```

## What still has to change before this is the final cut

- **The slates** are placeholders. Each one names the shot; replace it with the footage in the editor.
- **The transcript in `Labels.tsx`** is a stand-in. Swap in the real lines from the room test, and the real
  speaker labels, once the test is filmed.
- **The room behind the cold open** uses one of the kit's wallpaper plates. Replace it with a still from the shoot.
- **Prices** are from the companion page, checked November 2026. They are in `Boards.tsx`, in one place each.
