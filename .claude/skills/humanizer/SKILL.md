---
name: humanizer
description: Final language pass that makes finished prose read like a careful human wrote it, removing AI-sounding vocabulary, formulaic structures, filler and inflated claims while preserving meaning, facts, links, code and frontmatter. Use it in `written-prose` mode as the last step before any article, blog post, Medium piece, newsletter, landing-page copy or long email is called ready, and whenever another skill (such as create-medium-article) calls for `$humanizer`. Also use it when the user says a draft "sounds like AI", "sounds robotic", "is too generic", or asks to polish, de-fluff or humanize text, even if they don't name this skill.
---

# Humanizer

Make finished prose sound like a specific, careful person wrote it. This is a
language pass, not a rewrite: the argument, structure, facts and promises stay
as they are. What changes is the wording that makes readers think "a machine
wrote this" and stop trusting it.

Readers notice AI-sounding prose quickly, and once they do, they discount the
content, even when it is accurate. That is why this pass matters for anything
published under a person's or company's name.

## Modes

The caller passes a mode. If none is given, use `written-prose`.

- **`written-prose`**: articles, posts, newsletters, emails, marketing copy meant
  to be read on a screen. This is the only mode defined so far. If a caller asks
  for another mode, say it isn't defined and either run `written-prose` (if the
  text is written prose) or stop and report.

## What must not change

Treat these as locked. Changing any of them is a bug, not a style improvement:

- The title's promise and the article's claims, advice and conclusions
- Facts, numbers, dates, names, quotations and their attribution
- Links (URLs and what they point to), citations and source framing such as
  "the study measured X, not Y"
- Code blocks, inline code, templates, frontmatter and Markdown structure
- Brand names and required spellings (for example "Lynkk")
- Required disclaimers and CTAs, such as "This is not legal advice"
- Project writing rules. Read the repo's `CLAUDE.md` and any content profile
  (such as `.codex/content-profile.md`) first. Their rules win over this skill.

If the text has a factual or structural problem, don't fix it silently in this
pass. List it in the report for the author.

## Workflow

1. **Read the project rules** (`CLAUDE.md`, content profile) and the whole text
   once, without editing, to learn its voice and argument.
2. **Run the checker** to get a deterministic list of suspects:
   ```bash
   python3 -I <this-skill-dir>/scripts/check_prose.py <file>
   ```
   It skips frontmatter and code, and reports banned dashes, AI-flavored
   vocabulary and stock phrases, formula structures and rhythm statistics. It is
   a list of suspects, not a verdict: a flagged word can be the right word.
3. **Read `references/ai-patterns.md`** and scan for the patterns a script
   can't catch (tidy aphorism endings, uniform rhythm, rule-of-three habits,
   significance inflation, vague attribution).
4. **Edit in place**, smallest change first. Prefer deleting a phrase to
   rewording it, and rewording to restructuring. For each edit, ask: does the
   sentence now say the same thing, more plainly, in a way this author would?
5. **Re-run the checker** and re-read the full text top to bottom. Confirm every
   locked item above is intact (compare links, numbers and code against the
   original).
6. **Report** using the format below.

## Editing guidance

- **Plain words over impressive ones.** "Use" not "leverage", "help" not
  "empower", "important" or nothing at all instead of "crucial".
- **Cut throat-clearing.** Openers like "It's worth noting that" or "In today's
  fast-paced world" can usually be deleted with no loss.
- **Vary rhythm on purpose.** Mix short and long sentences, but don't add
  punchy fragments for drama. One per section is plenty.
- **Let paragraphs end when the point ends.** Delete closing lines that restate
  the paragraph as a slogan.
- **Be concrete.** Swap a vague claim for the specific example already in the
  text, or soften it if no evidence supports it.
- **Keep the author's voice.** If the text uses contractions and "you", keep
  them. Don't make casual prose formal or formal prose chatty.
- **Don't over-correct.** Clean, direct prose that happens to use one flagged
  word is fine. The goal is natural text, not text that avoids a word list.
  Leave a sentence alone if every rewrite is worse.

## Report format

```text
Humanizer: written-prose
File: <path>
Edits: <number> (<one-line summary of the main kinds>)
Notable changes:
- "<before>" -> "<after>"   (up to 8 of the most meaningful)
Left as is: <flagged items deliberately kept, and why>
Locked items verified: links <n>/<n>, numbers, code, frontmatter, disclaimers
For the author: <factual or structural issues noticed but not changed, or "none">
```
