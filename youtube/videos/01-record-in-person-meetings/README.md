# 01 · AI note taker for in-person meetings (long video)

Built with the `lynkk-design` skill and the Lynkk post kit (`lynkk-post-kit/`): Grid night band,
Inter, photo plates, glass mocks, the ruled frame from `kit/post.js`. Same pipeline as the
comparison videos: Kokoro `am_adam` voice, the original sitar and tabla track, video plus an
SRT caption file.

**Hook (first 12 seconds):** the problem ("Most notetakers wait for a meeting link. A meeting in a
room doesn't have one.") and the fix ("Record it in your browser at lynkk.ai.").

## Upload these

| File | Use |
|---|---|
| `out/01-record-in-person-meetings-long.mp4` | YouTube video, 1:09, 1920x1080 |
| `out/01-record-in-person-meetings-long.srt` | English captions |
| `youtube-description.md` | Title, description with chapters, tags, pinned comment |

## Claims and where they come from (`lynkk-post-kit/docs/TRUTHS.md`)

| On screen / in the voice | TRUTHS.md |
|---|---|
| Record your mic in the browser at lynkk.ai, countdown, pause, silence warning, works in person | Ways to record > Web |
| Transcript with speaker labels, 17 languages | The note |
| Meeting Brief: takeaways, decisions, open questions, action items with owner, due date, priority; free | The note > Meeting Brief |
| Every timestamp plays the recording | The note > Meeting Brief |
| Share with a link, summary emailed after every meeting | The note > Share |
| Send to Jira from the note, one issue each (manual) | Tasks |
| Never trains on your conversations | Privacy |

Nothing from the "Don't claim" list in TRUTHS.md is used, and there are no speed claims.
Sample data (Design review, Sam, Priya) is fictional.

## Rebuild

From `../lynkk-vs-tools/`: `./build.sh ../01-record-in-person-meetings long` (add `stills` for the
storyboard in `out/long/storyboard/`). Edit `narration-long.json` for the words and `long.html` for
the boards; the build runs the kit copy check on both first.
