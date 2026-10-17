# Comprehension Evidence for SaaS Hero / Explainer Graphics (applied to the Lynkk "Without vs With Lynkk" meeting graphic)

Scope note: the graphic under review has (a) a 38-minute meeting timeline across the top with waveform, 3 numbered moments, speech-bubble quotes and timestamps, (b) orthogonal arrows from each moment down into (c) a "With Lynkk" structured note on the right (Key facts, To collect checklist, New task with owner/deadline, timestamp chips), and (d) a "Without Lynkk" messy notepad on the left with red error tags. Goal: understood in under 5 seconds.

Source-quality legend used below: [Research] = peer-reviewed or large-sample study; [NN/g] = Nielsen Norman Group usability/eyetracking research; [Vendor] = tool vendor or agency content (opinion or self-reported data); [Opinion] = practitioner opinion without data.

## 1. How fast do visitors form an impression, and where do they look first?

### Takeaway
Aesthetic and "is this for me" judgments form in 17-50 ms and stick (halo effect), visitors decide to stay or leave mostly in the first 10 seconds, and attention goes to headings and content-bearing images while decorative or ad-like graphics get skipped. A dense hero graphic gets judged on visual complexity long before it is "read," so low complexity and familiar layout matter more than completeness.

### Cited Findings
- [Research] Lindgaard et al. (Carleton University, *Behaviour & Information Technology*, 2006) flashed home pages for 50 ms; visual-appeal ratings correlated well with ratings after longer viewing, and the authors argued a halo effect carries the first emotional impression over to later judgments of usability and credibility. Lindgaard suggested the 50 ms reaction is likely not cognitive for adults: [Digital Trends coverage](https://www.digitaltrends.com/home/surfers-judge-web-pages-seen-for-only-50ms/); [E-Commerce Times coverage](https://www.ecommercetimes.com/?p=158221). (Secondary coverage; original paper not fetched.)
- [Research] Tuch et al. (2012, *International Journal of Human-Computer Studies* 70(11):794-811, Google/University of Basel): 119 real website screenshots rated at 50, 500, 1000 ms; then 17, 33, 50 ms. Visual complexity (VC) and prototypicality (PT, how much it looks like a typical site of its kind) affected aesthetic ratings within 50 ms, and VC still did at 17 ms. VC is processed earlier than PT. Sites with low visual complexity and high prototypicality were rated most appealing: [Google Research](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/); [Google AI blog summary, 2012](https://ai.googleblog.com/2012/08/users-love-simple-and-familiar-designs.html). A 2018 Twente thesis replication found VC and PT about equally fast and strong at 50 and 500 ms (partly at odds with Tuch on PT timing): [Rotshuizen, University of Twente](https://essay.utwente.nl/74417).
- [Research via NN/g] Liu, White & Dumais (Microsoft Research, SIGIR 2010) analysed dwell times on 205,873 pages (2B+ dwell times): time on page follows a Weibull distribution with "negative aging" on 99% of pages; the first 10 seconds carry the highest probability of leaving; seconds 10-30 still see frequent exits; after about 30 s the leave rate flattens. Nielsen's implication: communicate the value proposition within 10 seconds. Average users read about a quarter of the text on a page: [NN/g, Nielsen, 2011](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/).
- [NN/g] 2018 eyetracking (120 participants, 130,000+ fixations on 1920x1080 desktop): 57% of viewing time was above the fold (down from 80% in 2010), about 74% in the first two screenfuls, with a sharp drop in attention right after the fold: [NN/g, Scrolling and Attention](https://www.nngroup.com/articles/scrolling-and-attention/).
- [NN/g] Layer-cake scanning: users fixate mainly on headings and subheadings with occasional dips into body text; this is the most effective scanning pattern, but only when headings are visually distinct and accurately describe the content beneath. F-pattern scanning is rated low-efficiency and users miss content without realising. On card or mixed layouts users perform "mini layer-cake" scans if each chunk is visually separated and labeled. Overly bright or large styling can look like an ad and be ignored: [NN/g, Pernice, 2019](https://www.nngroup.com/articles/layer-cake-pattern-scanning/).
- [NN/g] Decorative images are ignored ("jazzed-up = ignored"), while informative images (real products, real people) are scrutinized. On FreshBooks' team page users spent 10% more time on portraits than bios even though bios took 316% more space; generic stock models were ignored. On Amazon only about 18% of viewing time went to photos vs 82% to text (0.9 fixations per thumbnail vs 4.4 per description): [NN/g, Photos as Web Content, Nielsen 2010, reviewed 2026](https://www.nngroup.com/articles/photos-as-web-content/).
- [NN/g] Banner blindness (documented 1997, replicated 2007 and 2018): users skip things in ad-typical positions (top banner, right rail) and things with ad-like treatment: animation, colored rectangles on white, fancy formatting, text embedded in images, elements that "looked different from the text and the photography on the site." On one site only 1 of 132 content-area fixations (0.8%) hit the right rail. One unproductive glance makes users avoid that region for the rest of the visit ("hot-potato effect"). On mobile, large standout graphics can be mistaken for ads and scrolled past: [NN/g, Pernice, 2018](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/).
- [NN/g] Homepage guidance: communicate the unique value proposition clearly, usually via a descriptive tagline and compelling content in the hero space; images and text should work together: [NN/g, Homepage Design Principles](https://nngroup.com/articles/homepage-design-principles/).
- [Vendor/caution] RealEye notes a heatmap can show broad attention on a hero image while few participants read the headline or reach the primary button, but an image that establishes the category can be doing useful work: [RealEye](https://insights.realeye.io/eye-tracking-examples).

### Inferences
- At 17-50 ms the Lynkk graphic is judged on complexity, not content. A three-zone composition (timeline band + two note panels + connecting arrows + red tags + chips) is high in visual complexity, which predicts a lower first-glance appeal score and a slower "what is this?" read.
- Prototypicality favours what visitors already know: a "messy note vs. clean note" comparison is a familiar pattern; a waveform + timeline with arrows is less prototypical for a hero and adds parsing cost.
- Because the graphic is the informative kind (real-looking notes, real quotes), NN/g evidence suggests it will be looked at rather than ignored, but the left "Without" panel is the more likely to be skipped if it reads as decorative clutter. Red tags on a colored rectangle are close to the ad-like treatment NN/g describes; keep them readable as content.
- The 10-second window is the real budget for the whole hero (headline + graphic). The graphic does not need to be read in full in 5 s; it needs to confirm the headline's claim in 5 s.

### Gaps
- Lindgaard 2006 original paper not fetched directly; figures come from consistent secondary coverage.
- No eyetracking study found specifically on SaaS hero diagrams with arrows/timelines; Z-pattern evidence for hero sections was not found in NN/g research (NN/g documents F, layer-cake, spotted and others; "Z-pattern" is mostly a practitioner convention). Treat Z-pattern claims as opinion.

## 2. Before/after, split-screen and transformation visuals: when do they clarify or confuse?

### Takeaway
Evidence is thin and mostly from advertising research, but it consistently favours simple side-by-side juxtaposition read in a past-left / future-right order. Juxtaposition is easier to comprehend than fused visuals, yet it demands more elaboration (thinking) from the viewer, so the difference between the two sides must be obvious at a glance.

### Cited Findings
- [Research] Across four studies, ads for self-improvement products produced more positive product attitudes when the "before" image was on the left and the "after" on the right, consistent with a mental timeline where the past is left and the future is right: [SmartCompany summary](https://www.smartcompany.com.au/people-human-resources/training-development/should-the-image-be-on-the-left-or-right/). Likely the Chae & Hoegg study in *Journal of Consumer Research* 40(2), 2013, pp. 223-238, DOI 10.1086/669476 (author/issue match confirmed, title not confirmed): [JCR issue listing](https://academic.oup.com/jcr/issue/40/2).
- [Research] Visual-metaphor ad study (185 students, 2013): juxtaposition structures elicited more cognitive elaboration than fusion or replacement, and fusion was harder to comprehend than juxtaposition or replacement: [Marketing Management Journal PDF](https://marketingmanagementjournal.scholasticahq.com/article/151065.pdf). A small 2022 Egyptian study (50 students) found fusion produced the best ad attitude, which conflicts on liking (not comprehension): [JFAFU](https://jfafu.journals.ekb.eg/article_160870.html).
- [Research] Visual context strongly moderates how juxtapositions vs replacements are processed (International Journal of Advertising, 2022): [Tilburg University](https://research.tilburguniversity.edu/en/publications/refining-replacements-validating-a-revised-typology-of-visual-met/).
- [Research, thesis] Visual metaphors built on a similarity comparison were comprehended better than those built on opposition: [Radboud thesis](https://theses.ubn.ru.nl/handle/123456789/8150).
- [NN/g] Spatial grouping: users can parse chunked layouts as mini layer-cakes only when each chunk is visually separated and labeled, which applies to split panels: [NN/g layer-cake](https://www.nngroup.com/articles/layer-cake-pattern-scanning/).

### Inferences
- Lynkk's layout already follows the left = "Without" (past/problem), right = "With" (future/solution) order that the research favours. Keep it; do not flip.
- The comparison only pays off if the contrast is obvious without reading: e.g., the left panel visibly chaotic (crossed-out text, gaps), the right visibly ordered (headings, checkboxes, owner avatar). If both panels are text blocks of similar density, the viewer must read both to see the difference, which breaks the 5-second target.
- The top timeline adds a third zone that the viewer must connect to both panels. In a before/after frame, this is extra elaboration; it is a candidate for demotion (smaller, lighter) or removal from the hero, moving it to a secondary "how it works" graphic.
- Red tags on the left act as signaling (good), but if there are several, they compete with the right panel for the "where do I look" decision.

### Gaps
- No controlled study found on before/after comparisons for software UI (as opposed to body/product imagery). No direct evidence on three-zone (source + before + after) compositions.
- Original Chae & Hoegg abstract not retrieved; the left/right finding is via secondary summary.

## 3. Cognitive load, visual hierarchy, arrows, numbered steps: Mayer's principles applied

### Takeaway
Working memory holds roughly 4 chunks, and Mayer's research shows the biggest comprehension gains come from removing extraneous material (coherence), cueing what matters (signaling), and placing related words and visuals together (spatial contiguity). Every arrow, chip, tag and quote adds an element to hold; arrows help only when they carry the one relationship the viewer must grasp.

### Cited Findings
- [Research] Mayer's principles (definitions): Coherence = leave out extraneous material; Signaling = use cues (color, contrast) to highlight essential information; Redundancy = avoid stacking narration + graphics + on-screen text; Spatial contiguity = place related words and images near each other; Temporal contiguity = present matching words and visuals simultaneously; Segmenting = break into learner-paced parts; Pre-training = introduce key concepts first; Multimedia = words + pictures beat words alone: [Dartmouth summary of Mayer's 12 principles](https://services.dartmouth.edu/TDClient/1806/Portal/KB/PrintArticle?ID=171655).
- [Research] Effect sizes (Mayer, Cambridge Handbook of Multimedia Learning chapter on reducing extraneous processing): coherence median d = 1.32 (10 of 11 tests), signaling median d = 0.60 (3 of 3), redundancy median d = 0.69 (10 of 10): [Cambridge](https://www.cambridge.org/core/books/abs/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning-coherence-signaling-redundancy-spatial-contiguity-and-temporal-contiguity-principles/C98AB3A6CE760DD63C048936EA0B3B44). A different review reports coherence d = 0.70, signaling d = 0.46, spatial contiguity d = 0.79, redundancy d = 0.87, temporal contiguity d = 1.30, multimedia d = 1.67: [Synapse abstract](https://www.synapsesocial.com/es/papers/69dbbbdacebd566818835a69). The two sources disagree on magnitudes (different editions/study sets); direction is consistent.
- [Research] A 2022 study using brain-signal measures found signaling and spatial contiguity had the largest effects on learning (small study): [Springer, Education and Information Technologies](https://link.springer.com/10.1007/s10639-022-11283-2).
- [Research] Working memory focus-of-attention capacity is about 4 chunks in adults (Cowan 2001, across visual, auditory, verbal and spatial materials); contested (estimates of 5 or Miller's 7 exist), and chunking or longer exposure raises effective capacity: [PMC review 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11259112/); [Cowan BBS PDF](https://www.ai.rug.nl/~niels/publications/cowanBBS.pdf); [Journal of Cognition 2024](https://journalofcognition.org/articles/387).
- [Research] Tuch et al.: low visual complexity wins first impressions within 17-50 ms: [Google Research](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/).
- [Research] Tversky, Morrison & Bétrancourt (2002) note graphics often fail because they are too complex to be accurately perceived; the same argument applies to dense static diagrams: [Tversky 2002, IJHCS](https://hci.stanford.edu/courses/cs448b/papers/Tversky_AnimationFacilitate_IJHCS02.pdf).
- [Case study, government] ONRR's homepage team judged its first explanatory diagram "a bit complex" and likely to overwhelm users, and simplified it to cards after user-centered review: [ONRR blog](https://blog.onrr.gov/homepage-graphic/).
- [Research/CXL-Speero] Value-proposition eyetracking on personalcapital.com (Labay, 2016; preference N = 215): more descriptive variants (5 bullets, or 3 bullets with descriptions) were fixated faster, read longer and recalled better, yet participants preferred simpler bullet versions; a paragraph-only variant took longest to be noticed. Author's main recommendation: limit competing page elements so the value proposition gets read: [Speero (formerly CXL Institute)](https://speero.com/post/the-presentation-of-your-value-proposition-matters-original-research).

### Inferences
- Rough element count of the current graphic: timeline band, waveform, 3 numbered moments, 3 speech bubbles, 3 timestamps, 3 arrows, left panel, N red tags, right panel with 3 sections, 3 timestamp chips. That is well over 4 chunks at first glance. To land in 5 s, the viewer should only need to resolve about 3-4 groups: (1) a meeting happens, (2) messy notes vs (3) structured note, (4) the headline.
- Coherence (largest effect in Mayer's data) argues for cutting what does not carry the core message on first view: the waveform, per-item timestamp chips, and possibly the speech bubbles are secondary detail.
- Signaling: use one accent color for "With Lynkk" outcomes and one muted/red treatment for "Without," and make the right panel the visually dominant element (largest, highest contrast), since it is the outcome.
- Spatial contiguity: labels ("Without Lynkk" / "With Lynkk") should sit directly on the panels, and any quote should sit next to the note item it produced, rather than linked by long orthogonal arrows across the graphic. Long arrows are a sign the related items are not contiguous.
- Arrows: 3 arrows that cross a "Without" region or route around it force path-tracing, a serial (slow) task. A single "meeting -> Lynkk -> note" flow, or no arrows with color matching between moment and note item, reduces this.
- Numbered moments imply a sequence to read in order (segmenting), which suits a "how it works" section with user-paced reading, not a 5-second hero.

### Gaps
- Mayer's research is on instructional learning (minutes, retention tests) not 5-second marketing glances; transfer to hero graphics is inference. Boundary conditions (stronger effects for low-prior-knowledge viewers and fast, non-paced presentations) are documented in Mayer's work but the 2020 summary PDF could not be parsed in this session.
- No empirical source found giving a maximum number of arrows or labels for a glanceable diagram.

## 4. Headline/caption pairing: does the image need to stand alone?

### Takeaway
No. Users scan headings first (layer-cake) and online readers tend to look at text before images, so the headline carries the value proposition and the graphic's job is to confirm it. Short captions or labels attached to images are among the most-read text.

### Cited Findings
- [NN/g] Users fixate mostly on headings and subheadings; the most informative words should come first: [NN/g layer-cake](https://www.nngroup.com/articles/layer-cake-pattern-scanning/).
- [NN/g] Value proposition should be communicated via a descriptive tagline plus hero content working together: [NN/g homepage principles](https://nngroup.com/articles/homepage-design-principles/).
- [Research, Poynter] Stanford-Poynter online eyetracking: online readers viewed text first (headlines, briefs, cutlines), then photos and graphics, reversing the earlier print finding of photos first: [Poynter](https://poynter.org/?p=12643). Photo captions are heavily read relative to their length: [Canadian Journalism Foundation / Globe and Mail public editor](https://cjf-fjc.ca/globe-public-editor-just-few-words-photo-cutlines-have-enormous-impact/).
- [Research] Multimedia principle: words plus pictures outperform words alone; spatial contiguity: words placed next to the relevant part of the picture: [Dartmouth Mayer summary](https://services.dartmouth.edu/TDClient/1806/Portal/KB/PrintArticle?ID=171655).
- [Research] Amazon eyetracking: 82% of viewing time on text vs 18% on photos: [NN/g Photos as Web Content](https://www.nngroup.com/articles/photos-as-web-content/).
- [Vendor] Wynter's message-grader reports recommend headings that state the conclusion instead of posing a question and moving proof next to the claim it supports (AI-simulated personas, directional only): [Wynter grader report](https://grader.wynter.com/r/wynter-on-demand-messaging-and-market-research-EYX6BGo/markdown).
- [Unverified] A 2026 Webflow blog cites an NN/g "May 2026" study claiming styled captions get 64% more fixation time; not verifiable on nngroup.com: [pravinkumar.co](https://www.pravinkumar.co/blog/webflow-image-captions-magazine-pull-quotes-design-2026). Do not use.

### Inferences
- The 5-second test should be run on the full hero (headline + subhead + graphic), not the graphic alone; the realistic target is "headline states it, graphic proves it."
- A headline naming the outcome (e.g., notes, owners and deadlines captured automatically from the meeting) lets the right panel be read as confirmation. Two in-graphic labels ("Without Lynkk" / "With Lynkk") act as captions and are likely the most-read text inside the graphic, so they should be large and placed at the top of each panel.
- If the graphic must work standalone (e.g., shared on social), it needs a one-line caption baked in; on the page this is redundant with the headline (Mayer's redundancy principle).

### Gaps
- No NN/g primary article on caption reading found in this session; caption findings come from news-design eyetracking (Poynter), not SaaS pages.

## 5. Real UI screenshots vs abstract illustrations vs stylized "simplified UI"

### Takeaway
No rigorous public A/B evidence isolates screenshot vs illustration on SaaS heroes. NN/g eyetracking shows informative, real-looking content images get attention and decorative ones do not; brand systems at Amplitude and Morningstar adopt simplified product UI because it is easier for non-users to understand. A simplified-but-real-looking UI is the evidence-consistent middle path.

### Cited Findings
- [NN/g] Real product and real-people images are scrutinized; generic stock and decorative imagery is ignored: [NN/g Photos as Web Content](https://www.nngroup.com/articles/photos-as-web-content/).
- [Vendor/design system] Amplitude's brand guidelines describe abstracted product graphics as simpler and easier to understand for non-user audiences than screenshots: [Amplitude brand](https://brand.amplitude.com/visual-direction/illustration).
- [Vendor/design system] Morningstar: product illustrations distill the product experience to essential visual elements: [Morningstar design system](https://design.morningstar.com/systems/marketing/product-illustration).
- [Vendor, weak] An agency claims authentic UI screenshots converted 20% higher than stock imagery (no sample size or test design published): [SaaS Hero](https://www.saashero.net/design/best-saas-visuals-b2b-ads/). Competing vendor opinion argues a real human face builds trust faster than UI mockups (no test cited): [Insivia](https://www.insivia.com/how-does-custom-imagery-boost-conversions-the-power-of-real-people-in-tech-branding/).
- [Research] Prototypicality boosts first impressions: designs that look like what users expect of the category are judged more appealing within 50 ms: [Google Research, Tuch et al.](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/).
- [NN/g] Text embedded in images and elements that look unlike the rest of the site trigger banner blindness: [NN/g banner blindness](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/).

### Inferences
- The "With Lynkk" note should look like a real Lynkk note (recognizable product UI, which builds trust and is informative) but simplified (fewer fields, larger type) so it can be read at hero size.
- The "Without Lynkk" notepad works best when instantly recognizable as a generic notes app or paper (prototypical), not a custom illustration that has to be decoded.
- Too much small text inside an image is both hard to read at a glance and an ad-like pattern; keep only 3-5 short, legible strings per panel.

### Gaps
- No controlled study found comparing screenshot vs illustration vs simplified UI for comprehension or trust on SaaS pages. The Mutiny/AlphaSense test of a screenshot background did not expose results. This is the strongest candidate for Lynkk's own test.

## 6. Animation / sequential reveal vs static

### Takeaway
Animation helps mainly for procedural, motion-based content and when it is well-designed; much of animation's apparent advantage disappears when static versions carry equivalent information. Motion in the periphery captures attention involuntarily and can distract or read as an ad. For a hero meant to be grasped in 5 seconds, a static image that is fully understandable on its own is the safer default; an optional or one-time sequential reveal can help explain the process.

### Cited Findings
- [Research] Tversky, Morrison & Bétrancourt (2002, IJHCS 57:247-262): where animation seemed superior to static graphics, the comparison usually lacked equivalence (animations contained more information or interactivity); animations often fail because they are too complex or too fast to perceive accurately: [Tversky et al. 2002 PDF](https://hci.stanford.edu/courses/cs448b/papers/Tversky_AnimationFacilitate_IJHCS02.pdf).
- [Research] Höffler & Leutner (2007, *Learning and Instruction* 17:722-738), meta-analysis of 26 studies / 76 comparisons: medium overall advantage for instructional animation over static pictures, d = 0.37 (95% CI 0.25-0.49); much larger for procedural-motor knowledge (d = 1.06) and highly realistic, video-based animation: [Höffler & Leutner 2007 PDF](https://wikicap.ulb.be/images/e/ef/Hoffler_Leutner_2007.pdf).
- [NN/g] Movement in peripheral vision triggers an involuntary attention shift; moving UI elements often distract users from their goals; blinking/moving elements in ad positions drive banner blindness: [NN/g Animation Usability](https://www.nngroup.com/articles/animation-usability/); [NN/g distracting animations video](https://www.nngroup.com/videos/distracting-animations/).
- [NN/g] Animation is listed among the visual treatments that make content look like ads: [NN/g banner blindness](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/).
- [Secondary] Auto-advancing carousels: users mostly notice the first slide; autoplay can change before text is read (blog citing NN/g): [F7 blog](https://f7.de/en/blog/stop-the-slide-why-carousels-harm-the-ux).
- [Research] Temporal contiguity and segmenting (Mayer) favour step-by-step presentation when the viewer controls pace: [Dartmouth Mayer summary](https://services.dartmouth.edu/TDClient/1806/Portal/KB/PrintArticle?ID=171655).
- [Research/CXL-Speero] Dynamic value propositions (GIFs, video, moving graphics) were explicitly untested in the Speero study: [Speero](https://speero.com/post/the-presentation-of-your-value-proposition-matters-original-research).

### Inferences
- Lynkk's graphic depicts a process (meeting -> extraction -> note), which is the case where sequence helps. But the 5-second goal is about the outcome, which a static end-state conveys. Option: static hero that shows the end state clearly; a short, single-play (not looping) reveal of moment 1 -> note item 1, etc., that ends on the same static frame; respects reduced-motion settings.
- Looping motion in the hero risks pulling the eye away from the headline and reading as an ad, per NN/g.
- Any animated version must be judged against a static version with the same information (Tversky's equivalence point) in the 5-second test.

### Gaps
- No study found on autoplay hero loops vs static heroes in SaaS marketing with comprehension measures. Höffler & Leutner moderators beyond procedural knowledge and realism were not verified from full text.

## 7. Frameworks and running a cheap 5-second test

### Takeaway
The five-second test (show for 5 s, hide, ask "what was this about?") is the standard, cheap method; 5-10 participants surface main patterns and about 80% correct gist is a reasonable pass bar per Lyssna. "Show the outcome, not the process" and JTBD-style headlines are practitioner frameworks without direct experimental validation found here; the closest evidence is NN/g's "value proposition within 10 seconds" and the coherence principle.

### Cited Findings
- [Vendor guide, Lyssna] Method: show design (default 5 s, configurable up to 20 s), hide, ask recall questions, analyze. Keep exposure identical for all participants; do not reveal questions beforehand; 5-8 questions max; first question should be the most important ("What was this page about?"). Avoid leading questions ("What do you remember about the colors?" not "Wasn't the blue eye-catching?"). 5-10 participants usually reveal major patterns; if more than about 80% get the main message the design is likely working; similar wrong answers point to a specific misleading element. Example questions: "What was this page about?", "Who is it designed for?", "What did you notice first?", "Was anything unclear?": [Lyssna Five Second Testing guide](https://www.lyssna.com/guides/five-second-testing/).
- [Vendor] Lyssna setup: create test, choose five second test, upload an image, follow-up questions as short text or linear scale (e.g., trust rating); recruit via Lyssna panel or share a link; results within hours, CSV export; free sign-up available: [Lyssna video](https://www.lyssna.com/videos/five-second-testing/); [Lyssna feature page](https://www.lyssna.com/features/five-second-testing-software/).
- [Opinion] Paul Boag's course suggests the required questions "In your own words, describe what the web page is about" and "What elements do you remember?" and uses about 8 seconds rather than 5: [Frontend Masters, Paul Boag](https://frontendmasters.com/teachers/paul-boag/user-tests-8-second/).
- [Vendor] Wynter offers B2B message testing with a LinkedIn-verified panel (directory reports 70,000+ professionals) from about $199 per test, plus a free AI "homepage grader" scoring clarity with about 15 simulated personas; the grader itself cautions simulated personas lack real budgets or context: [Wynter](https://wynter.com/products/b2b-user-testing); [GTM Directory](https://thegtmdirectory.com/tools/wynter); [Wynter grader sample](https://grader.wynter.com/r/wynter-on-demand-messaging-and-market-research-EYX6BGo/markdown).
- [NN/g] Communicate the value proposition within 10 seconds: [NN/g](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/).
- [Opinion] "Clarity trumps persuasion" traces to a practitioner tweet (@FlintsNotes) cited by Unbounce; Unbounce adds "clarity almost always converts better than cleverness, but test it": [Unbounce glossary](https://unbounce.com/conversion-glossary/definition/clarity/). CXL lists whitespace, meaningful images and visual hierarchy as clarity starting points: [CXL](https://cxl.com/improving-clarity/).

### Inferences
- Cheap protocol for Lynkk: export 3-4 hero variants as images at real viewport size (desktop and mobile): (A) current graphic, (B) current minus timeline/arrows (two panels only), (C) right panel only with headline, (D) static end-frame of any animation. 10 participants each from a panel close to target buyers (sales, PMs, founders). Q1 "What does this product do?" Q2 "What did you notice first?" Q3 "Who is it for?" Q4 "Anything confusing?" Score Q1 as pass if the answer mentions automatic meeting notes/tasks. Pass bar: about 80%.
- Run with and without the headline to measure how much the graphic contributes on its own.
- Repeat the "what did you notice first" answer as a proxy for focal point; if many say "the timeline" or "the arrows," the hierarchy is pointing at the process rather than the outcome.

### Gaps
- No experimental evidence found for "show the outcome, not the process" or JTBD headlines as such; they remain practitioner frameworks (treat as opinion).
- No published benchmark found for what fraction of first-time visitors correctly identify a SaaS product from a five-second view; the 80% figure is Lyssna's heuristic, not a measured norm.
- Unbounce/Hotjar landing-page datasets on hero image types were not found in this session.
