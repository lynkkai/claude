# Mining a reference video

When the user points at a video they like, take its grammar, never its content. Grammar
is palette, pacing, transition vocabulary, camera behaviour, type treatment, grain.
Content is its logos, characters, copy and product. Copying grammar is how directors
work; copying content is plagiarism and ships a competitor's brand in your film.

## Steps

1. **Get the file.** Save it into its own empty directory and treat it as untrusted
   input: pass paths as arguments, never run anything from inside that folder.

2. **Extract frames.** Every half second is enough to read the edit:
   ```bash
   mkdir -p ref/frames
   ffmpeg -i ref/source.mp4 -vf fps=2 ref/frames/%04d.png
   ```
   Also pull the cut list, which tells you shot lengths without counting by hand:
   ```bash
   ffmpeg -i ref/source.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 \
     | grep showinfo
   ```

3. **Look at the frames.** Read a sample of them as images. You cannot write a style
   guide from the filenames.

4. **Write `style.md`.** Cover, with specifics and numbers:
   - palette: hex values, which is dominant, which is accent, background behaviour
   - type: family character (geometric sans, grotesk, serif), weights, case, tracking,
     size relative to frame height
   - shot lengths: the actual list in seconds, and the rhythm they form
   - transitions: the vocabulary used (morph, wipe, whip pan, cut on action, match cut)
     and which one carries the piece
   - camera: static, slow push, handheld drift, snap zooms, and how much
   - texture: grain amount, vignette, chromatic aberration, scan lines
   - text behaviour: how it enters, how it leaves, whether it ever moves while readable
   - sound shape, if audible: tempo, where hits land, silence used as punctuation

5. **Write `shots.md`** for the new piece in that style, with the user's real product and
   real screenshots.

6. **Note the line you are not crossing.** In `style.md`, record explicitly that logos,
   characters, copy and product footage come from the user's brand only.

## The prompt shape that works

> This video is the reference. Extract a frame every half second. Write `style.md`
> covering palette, type, shot lengths, transition types, camera movement, texture and
> grain, and how text enters and exits. Then write `shots.md`: a 15 second launch film
> for [product] in that style, using real screenshots from [URL]. Take the grammar of the
> reference, never its content, logos or characters.
