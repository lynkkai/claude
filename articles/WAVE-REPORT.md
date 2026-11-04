# Wave gate report: 11 articles from the GSC/keyword table

Run: Journey A (full content wave), 4 November 2026. Client: Lynkk (generic calibration; no client fences file on this machine).
Topics: rows 3, 14, 20, 21, 5, 15, 6, 1, 2, 7, 10 of the supplied Ranked table (row 5 appeared twice in the request and is written once).
Deterministic checks: `python3 scripts/article_gate.py <article> [--live] [--original <backup>]`, `scripts/build_schema.py`, `scripts/apply_edits.py`.
These stand in for `pre_score.py`, `clip_check.py`, `link_liveness.py`, `batch_gate.py` and `humanize_verify.py`, which are not installed on this machine.

## Wave summary

| # | Slug | Words | Density | Clips w/ number | Dashes | Banned | Burstiness (pre -> post) | Gate B |
|---|---|---|---|---|---|---|---|---|
| 3 | objection-handling | 2150 | 1.49% | 13/22 | 0 | 0 | 0.485 -> 0.562 | PASS |
| 14 | real-time-ai-interview-assistant | 1752 | 1.14% | 9/15 | 0 | 0 | 0.496 -> 0.562 | PASS |
| 20 | discovery-call-questions | 2038 | 1.18% | 12/20 | 0 | 0 | 0.509 -> 0.558 | PASS |
| 21 | call-coaching-software | 2080 | 1.44% | 14/20 | 0 | 0 | 0.449 -> 0.527 | PASS |
| 5 | speech-to-text-mac | 1794 | 1.11% | 7/17 | 0 | 0 | 0.466 -> 0.541 | PASS |
| 15 | best-second-brain-apps | 1881 | 0.64% | 7/19 | 0 | 0 | 0.430 -> 0.506 | PASS |
| 6 | personal-knowledge-management | 1661 | 1.44% | 10/18 | 0 | 0 | 0.461 -> 0.506 | PASS |
| 1 | record-audio-on-mac | 1449 | 1.04% | 8/15 | 0 | 0 | 0.508 -> 0.548 | PASS |
| 2 | best-mac-note-taking-app | 1699 | 0.88% | 8/18 | 0 | 0 | 0.458 -> 0.538 | PASS |
| 7 | live-caption-apps | 1438 | 1.46% | 5/16 | 0 | 0 | 0.520 -> 0.561 | PASS |
| 10 | sales-call-recording-software | 1775 | 1.35% | 13/19 | 0 | 0 | 0.470 -> 0.543 | PASS |

Every article: 6-9 sourced question H2s, 0 dead headings, 0 throat-clearing clips, 6 FAQs at 40-60 words, FAQ body and JSON-LD generated from one source so they match word for word, every link checked live (government 403 counted as live), named author with bio URL, evergreen slug with no year.

Gate thresholds: AEO >= 80, SEO >= 85 plus G1-G4, post-humanize C1-C17, humanize-verify burstiness >= 0.5.
All 11 clear AEO and SEO. Estimated AEO 88-93, SEO 89-92; the recurring deduction is D5 data density, where several topics have few natural numerals.

## Batch-only checks (the ones a per-article gate cannot see)

- **C15 cross-article duplication:** 1 shared paragraph across 12 files, and it is the author byline line, which is shared by design. No duplicated CTA, body prose or table.
- **C12 figure traceability:** 1 flagged figure, the "20%" inside the objection-handling live-call example. The paragraph directly below states the numbers in those examples are illustrative, so it is a false positive of the regex, not an uncited claim.
- **Prompt collisions inside the wave:** none. Each article targets a distinct prompt set.
- **Publish order / self-cannibalization:** see the cluster warnings below.
- **Shared dead source:** none. No single source carries more than 2 articles.
- **Batch-dependent links:** 7 internal links point at articles in this batch and will 404 until the batch publishes. They are valid only if the wave publishes together. Listed per article below.

## Cluster warnings (G2 same-cluster, distinct intent, F4 penalty)

Three pairs sit in one cluster each and were deliberately scoped apart. Each needs a GSC check at day 21+; consolidate if both pages rank for the same head term.

1. **#15 best-second-brain-apps vs #6 personal-knowledge-management.** Autocomplete carries "personal knowledge management vs second brain". Split: #15 is tools and prices, #6 is methods (PARA, Zettelkasten, CODE). Cross-linked once each.
2. **#2 best-mac-note-taking-app vs #15.** Obsidian and Notion appear in both, because they are genuine answers to both queries. Different framing, different sibling sets.
3. **#21 call-coaching-software vs #10 sales-call-recording-software.** Same vendors. Split: #21 is the coaching workflow and scorecards, #10 is recording, platforms and consent.
4. **#5 speech-to-text-mac vs the live `/blog/dictation-on-mac`.** Closest call in the wave. The new article is scoped to choosing a method and links out rather than repeating the setup steps.

## Handoff: what a human still has to do

1. **Inbound links (HARD gate, not done; no CMS access).** Every article needs 1-2 inbound links from live sibling pages before it counts as launched. Candidates are listed per article in the notes below.
2. **Banner images.** `featured_image_path` is a placeholder on all 11; alt text is written. No Lynkk image-gen skill exists on this machine.
3. **Tracked prompts.** The `targeted_prompts` in each frontmatter came from GSC or autocomplete. Register them if Lynkk runs a prompt tracker (prompt gap -> create_prompt).
4. **Publishing** needs explicit per-article approval. Strip the `---CITATIONS---`, `---SCHEMA---` and `---FAQ_JSON---` markers into CMS fields on push, and publish the wave together so the batch-dependent links resolve.
5. **Spot-check humanization** with a real detector (GPTZero, Originality.ai) on 2-3 articles. The burstiness figures are proxy signals, not a detector.

## Flags for the Lynkk team

- **Brand memo contradicts the live site.** `memory/lynkk-brand.md` claims regional data residency ("pick a region and every model behind Lynkk processes/answers from that region"). The live `/security` page says data "may be processed outside your country, including in India and the US". The articles follow the live page. Fix the memo before reusing it for submissions.
- **Language count inconsistency.** `/features/dictation` says 18 languages; `/pricing` says 17 languages plus Hinglish. Each article used the figure from the page it cites. Worth reconciling.
- **Lynkk's gaps are stated plainly** in every listicle: no CRM sync, no deal scoring, no forecasting, no SSO or SCIM on the published plans, workspaces capped at 10, and it is not a general note-taking app. That honesty is deliberate, and it is what lets these pages be cited on comparison prompts. It is still a positioning call: review before publishing.
- **Fathom correction found during fact-checking:** AI scorecards and coaching metrics are Business-plan only ($34/user/month, $25 yearly), not "paid plans" generally. Worth correcting anywhere else this appears.

## Per-article notes

## #3 objection-handling
- SERP: examples-led guides (HubSpot 44/52 objections, walnut, NASP). Format: guide + scripts. Collision: none (spin-selling, bant distinct; linked).
- Fan-out: autocomplete (what is objection handling in sales, why important, framework, 5 steps, too expensive, i need to think about it, not interested, no budget, no time, live/examples, cold call, practice, ai, mistakes via SERP). FAQ: soft skill, feel felt found, buying signals, matrix, via email, customer service (all autocomplete).
- Gate A: AEO ~93 (D5 -4: 5 external sources; stat sources thin and the 5x/54.3% Gong figures excluded as unverifiable), SEO ~92 (S6 banner pending). density 1.48%, clips 15/22 w/ number, 13 links live.
- Gate B pass; humanize-verify burstiness 0.485 -> 0.562 WORKING. 3 paragraphs split post-humanize (mechanical).
- Inbound link candidates: /blog/spin-selling, /blog/bant-sales-qualification, /use-cases/sales-calls, /features/spotter related guides.
## #14 real-time-ai-interview-assistant
- SERP: tool homepages (LockedIn, Final Round, Beyz, InterviewBee) + reddit; "best" SERP has listicles. G1 note: head term SERP is product pages; article targets the "best/which/is it cheating" listicle and question intents. Collision: none (recruiting-interview-transcription is recruiter-side; linked).
- ANGLE DECISION: many tools are sold as "undetectable" cheating aids. Article does not rank or promote hidden live use; ranks tool TYPES (prompt-led skill rule for unverifiable named claims) and steers to prep, mock interviews, recruiter note taking. Consistent with Spotter ("never hidden from screen capture").
- Fan-out: autocomplete (what is, how works, is it cheating/using ai for job interviews, undetectable/can tell, best/which is best, free/github, how to prepare/practice, for recruiters/hr). FAQ: pass an ai interview, chatgpt, zoom/teams/meet, mac, talk about ai in interview, legal.
- Sources: ITPro (Amazon guidance + 3 signs), Entrepreneur (Pichai, McKinsey), Personnel Today (Gartner 6%, 1 in 4 by 2028), aboutamazon (pilot transcripts, consent). GeekWire dropped (403, unverifiable).
- Gate A: AEO ~90 (D5 -4 thin external count; D6 1,769 words ok), SEO ~90. density 1.14%, clips 9/15. Gate B pass; burstiness 0.496 -> 0.562.
## #20 discovery-call-questions
- SERP: question listicles (Salesforce, Allego, Highspot, Avoma 90 questions, reddit). Format: list + agenda + script. Collision: none (spin/bant/meddic linked as frameworks).
- Fan-out: autocomplete (what is a discovery call, how many questions, best/sales discovery call questions, cold call discovery questions, client/agency, coaching, structure/agenda/script, how long, how to prepare, vs demo, follow up email, recording/software). FAQ: free, interview, vs consultation, objections, template, record.
- Sources: Gong (519,000 calls, 11-14 questions, 3-4 problems), Salesforce (20-30 min simple, up to an hour complex; 87% trusted advisor), Highspot (8-12 questions). 43:57 talk ratio excluded: not on Gong's page.
- Gate A: AEO ~91, SEO ~90. density 1.18%, clips 12/20, 13 links (1 batch-dependent: /blog/objection-handling 404 until #3 publishes).
- Gate B pass; burstiness 0.509 -> 0.558.
## #21 call-coaching-software
- SERP: "best X software" listicles. Format: listicle + comparison table. Collision: sales-conversation-intelligence (explainer, distinct; linked as target).
- Fan-out: autocomplete (call coaching meaning, best, ai call coaching software, live sales call coaching, call monitoring software, cost via SERP, best call center coaching software, sales call coaching template/form, how often coaching). FAQ: win rates, free, zoom recordings, form, how often, gong free plan.
- Facts: Lynkk compare pages (checked Oct 2026) for Gong, Clari Copilot, Avoma, Fathom; verified live on avoma.com/pricing and fathom.ai/pricing. CORRECTION found: Fathom AI scorecards are Business-only ($34 / $25 yearly), not all paid plans. Training Industry 2020 (CSO Insights; Aberdeen 19.0% win rate, 21.3% quota).
- Lynkk placed #5 honestly: records/searches, no scoring (matches compare pages "does not score deals or coach").
- Gate A: AEO ~90, SEO ~89. density 1.45%, clips 14/20. 2 batch-dependent links (#3, #20).
- Gate B pass; burstiness 0.449 -> 0.527.
## #5 speech-to-text-mac
- SERP: app pages (VoiceInk) + how-to guides + reddit. Mixed. Format: method comparison guide.
- ⚠️ G2 COLLISION (same cluster, distinct intent, F4 penalty + monitoring note): /blog/dictation-on-mac covers "how to turn on/fix Mac dictation"; /blog/voice-to-text-apps is the cross-platform app roundup. This article is scoped to CHOOSING A METHOD (live dictation vs transcribing a recording vs meetings vs Voice Control) and links out to both rather than repeating them. Watch GSC for cannibalization with dictation-on-mac at day 21+; consolidate if both rank for "speech to text mac".
- Gate A fail then fix: primary kw "speech to text mac" was absent from H1/meta (H1 reads "on Mac"). Reordered keywords (primary = "speech to text on mac") and worked exact variants into body/meta. Also renamed invented kw "transcribe audio mac" -> "transcribe audio on mac".
- Sources: Apple macOS User Guide (30s silence timeout, auto punctuation, on-device check, on-device model needs M3+/12GB), Apple Notes guide, Google voice typing, Microsoft Dictate (subscriber-only, Option+F1).
- ⚠️ Lynkk inconsistency: /features/dictation says 18 languages; /pricing says 17 languages + Hinglish. Used each page's own figure; team should reconcile.
- Gate A: AEO ~88 (D5 -3: clips 7/17 = 41%, under the 50% target but over the 36% corpus median), SEO ~89. density 1.11%, 13 links live.
- Gate B pass; burstiness 0.466 -> 0.541.
## #15 best-second-brain-apps
- SERP: listicles ("Best Second Brain Apps in 2026", "we tested the best 10") + reddit. Format: listicle w/ comparison table. Collision: /blog/meeting-knowledge-management is team meeting-search (distinct; linked as target).
- ⚠️ PAIRED WITH #6 (PKM): autocomplete shows "personal knowledge management vs second brain", so these two could cannibalize. Split enforced: #15 = TOOLS (app listicle, prices), #6 = METHOD (PARA/Zettelkasten/CODE, workflow). Each links to the other once. Re-check at day 21+.
- Prices verified live on vendor pricing pages (Obsidian, Notion, Capacities, Tana). Logseq page would only confirm "privacy-first, open-source knowledge base", so no price/platform claims made. Tiago Forte PARA cited from fortelabs.com (primary).
- Lynkk placed #7 with an explicit "not a general note-taking app" caveat.
- Gate A: AEO ~89 (D5 -3: clips 8/19 = 42%), SEO ~90. density 0.65%, 14 links (1 batch-dependent: /blog/personal-knowledge-management = #6).
- Gate B pass; burstiness 0.430 -> 0.506 (needed 3 passes; listicle bullets flatten variance).
## #6 personal-knowledge-management
- SERP: explainer/definition posts (tana.inc at #2, substack, medium). Format: method explainer. Paired-split with #15 enforced (see #15 note): this one is METHODS (PARA/Zettelkasten/CODE + workflow), tools delegated to #15.
- Sources: zettelkasten.de (Luhmann 50 books / 600+ articles / 150+ unfinished; atomic notes, own words, "connecting not collecting"), fortelabs.com/blog/para (verbatim PARA definitions). Both primary.
- Gate A fail then fix: density 2.88% (way over the 1.5% ceiling) from repeating the head term; cut head-term uses 16 -> 8 by switching to "PKM" where natural. Also split one 40+ word quote sentence. Final density 1.44%.
- ⚠️ PROCESS NOTE: a late attempt to shave density by editing an H2 broke Gate B (headings_identical False, C1 keyword lost). Reverted; density reduced in body prose instead. Headings are frozen after humanization: never edit them post-humanize.
- Also hit an apply_edits gotcha: "## X" is a substring of "### X", so an H2 edit silently corrupted an H3. All-or-nothing assertion caught it. Anchor heading edits with a leading newline.
- Gate A: AEO ~90, SEO ~90. clips 10/18. 9 links (1 batch-dependent: /blog/best-second-brain-apps = #15).
- Gate B pass; burstiness 0.461 -> 0.506.
## #1 record-audio-on-mac
- SERP/autocomplete: how-to intent, dominated by "system/internal audio" variants (blackhole, quicktime, screen recording). Format: how-to with a method table. Collision: none (speech-to-text-mac is dictation; transcribe-audio-to-text is files; both linked).
- Sources: Apple QuickTime guide (File > New Audio Recording, Capture Device, High = 44100 Hz AAC vs Maximum = uncompressed Linear PCM 24-bit AIFF-C), Apple screenshot guide (Shift-Command-5, Options > Microphone, None), Apple Voice Memos guide. No third-party driver named: only the general virtual-audio-device route, since specific drivers could not be verified live.
- Gate A fail then fix: ALL 9 keywords scored 0 because the body says "on a Mac" and the keyword list said "on mac" (the normalizer strips hyphens, not articles). Rewrote the keyword list to the phrasing actually used.
- ⚠️ SECOND Gate A fail: after making "record audio on a mac" primary, density hit 2.39% with 5 of 7 occurrences inside frozen H2s. Followed the documented path: restored .original, fixed the headings upstream (step 4), re-humanized. Did NOT edit headings post-humanize. Final density 1.04%.
- Gate A: AEO ~89, SEO ~89. clips 8/15. 10 links live.
- Gate B pass; burstiness 0.508 -> 0.548.
## #2 best-mac-note-taking-app
- SERP: listicles ("I tested 11", "5 best", "8 apps compared") + reddit/quora. Format: listicle + table.
- ⚠️ G2: third article in the knowledge-management cluster (with #15, #6). Split: #2 = Mac-native note apps (Apple Notes, Bear, Craft, Goodnotes), #15 = linked-note/second-brain tools, #6 = methods. Obsidian and Notion appear in both #2 and #15 by necessity (they are top answers for both queries) but with different framing and different sibling sets. Watch for cannibalization between #2 and #15 at day 21+.
- Prices verified live: bear.app (Pro $2.99/mo, $29.99/yr, 7-day trial; Mac/iPhone/iPad), craft.do/pricing (Free 1,500 blocks/1GB; Plus $6.40/mo), goodnotes.com/pricing (Free 3 files/5MB; Essential $11.99/yr; Pro $35.99/yr; Teams $120/seat/yr; AI Pass $9.99/mo), obsidian.md/pricing, notion.com/pricing. bear.app/pricing 404s; used bear.app.
- Apple Notes features from Apple's Notes guide (folders, tags, Smart Folders, scanning, sharing, links, audio recording with live searchable transcripts).
- Gate A: AEO ~88 (D5 -3: clips 8/18 = 44%), SEO ~89. density 0.88%. 12 links (2 batch-dependent: #15, #6).
- Gate B pass; burstiness 0.458 -> 0.538. opener_repeat stays high (0.27) because of the repeated "Pick it if / Look elsewhere if" listicle pattern; that is structural, not AI-tell.
## #7 live-caption-apps
- Autocomplete-led (no separate SERP pull; intent is unambiguous how-to/compare). ANGLE: the honest answer is "you already have it", so the article steers to built-in free options rather than selling an app. Collision: none.
- Sources (all primary vendor docs): Chrome Help (local processing, never stored, Live Translate exception), Apple macOS guide (all apps, on device, Apple silicon only, language download), Microsoft Teams (More actions > Captions, "Teams doesn't save captions", permanently deleted), Google Meet (translated captions limited to some Workspace editions), Microsoft Windows (11 22H2+, Win+Ctrl+L, on-device).
- ⚠️ Caught mid-draft: I had asserted a Windows live-captions feature from memory. Verified against Microsoft's page before scoring and replaced it with the sourced version (version requirement, shortcut, on-device claim).
- Gate A: AEO ~88 (D5 -3: clips 5/16 = 31%, below the 36% corpus median; this topic is feature description, few natural numerals), SEO ~89. density 1.46%, 11 links live. Quick Answer clip initially had no numeral (a CRITICAL per the clip rule) -> added the "5 places" count.
- Gate B pass; burstiness 0.520 -> 0.561.
## #10 sales-call-recording-software
- SERP: vendor product pages (Gong, Zoom, Clari, Salesloft) + "best X tested" listicles + reddit. Format: listicle + consent section (the PAA/legal angle is what the vendor pages skip).
- ⚠️ G2 (same cluster, distinct intent, F4): overlaps #21 call-coaching-software on vendors. Split: #21 = COACHING workflow/scorecards, #10 = RECORDING + consent/legal + platforms. Cross-linked once each. Watch both at day 21+.
- Prices re-verified live (avoma.com/pricing, fathom.ai/pricing); Gong/Clari from Lynkk compare pages (buyer-reported, labelled as such, not presented as official).
- Lynkk placed #6 with an explicit "no CRM sync, no deal scoring, no forecasting" caveat, and the CRM FAQ repeats it.
- Gate A: AEO ~91, SEO ~90. density 1.35%, clips 13/19 (68%, best in the wave). 12 links (1 batch-dependent: #21).
- Gate B pass; burstiness 0.470 -> 0.543.
