# Gate report: ai-notetaker-security

Article: `articles/ai-notetaker-security.md` (humanized) · Backup: `articles/ai-notetaker-security.md.original` (Gate A version)
Pipeline run: Journey B (single article), 4 November 2026. Client: Lynkk (generic calibration, no client fences file on this machine).
Deterministic checks: `python3 scripts/article_gate.py <article> [--live] [--original <backup>]` and `scripts/build_schema.py`. These stand in for `pre_score.py`, `clip_check.py`, `link_liveness.py` and `humanize_verify.py`, which are not installed here.

## 1. Topic score (/topic-score)

Topic: AI notetaker security (SSO, SCIM, retention, audit logs, LLM subprocessors).

| Gate | Result | Evidence |
|---|---|---|
| G1 Demand | PASS | GSC, Aug to Nov 2026: 12 security-shaped prompts with about 400 impressions at positions 3 to 9 (for example "rolling out an ai notetaker to 300 reps: which plans include sso, scim and an admin dashboard?" 78 impr, pos 6.9; "which third-party llm providers get to see prospect call transcripts..." 69 impr, pos 3.6; "looking for options besides zoom ai companion for regulated teams..." 65 impr, pos 4.1). Autocomplete: "are ai notetakers secure", "ai note taker security risk", "ai note taker privacy concerns", "ai note taker policy", "ai note taker hipaa". Ubersuggest volume reads 0 (normal for AEO-shaped demand). |
| G2 Collision | PASS (yellow, distinct intent) | No lynkk.ai blog post on this intent (sitemap, 115 URLs, checked live). Nearest neighbours: `/security` (product page, the link target), the "Is an AI-powered meeting assistant safe to use?" H2 in `/blog/ai-powered-meeting-assistants`, and the "Retention and audit trail" H3 in `/blog/zoom-ai-companion-alternatives`. All three are linked from or to the new article, not competing with it. |
| G3 SERP winnable | PASS | Top 10 for "ai note taker security" (Ubersuggest live SERP, US, 4 Nov 2026): law-firm and insurer risk guides (Lockton), vendor security pages (Fireflies), a socradar.io post. No marketplaces or gov portals. AI Overview present; commercial/evaluation intent, so no F3 penalty. |
| G4 Channel fit | PASS | Hybrid SEO + AEO. The prompts are evaluation questions Lynkk already appears for. |
| G5 ChatGPT winnability | Winnable | Prompts name prices, seat counts (300 reps, 40-person) and vendors, so they need current facts. |
| G6 Own-domain handicap | `route: earned-media preferred` (label only) | Unbranded discovery intent. The on-domain article still earns its place on SEO grounds and because lynkk.ai already ranks at positions 3 to 9 for these prompts. |

Verdict: **WRITE**.

## 2. Query fan-out (hard rule: 6 to 9 sourced H2s, none invented)

The QFO, PAA and DataForSEO tools named in the skills are not available on this machine. Sources 3 (autocomplete), 4 (SERP decomposition) and 5 (GSC) carried the job, as the skill allows.

| H2 / H3 | Source |
|---|---|
| Are AI notetakers secure? | Autocomplete: "are ai notetakers secure", "are ai notetakers safe" |
| ### What are the security risks of AI note takers? | Autocomplete: "ai note taker security risk" |
| Which third-party LLM providers get to see call transcripts an AI notetaker processes? | GSC prompt (69 impr, pos 3.64) |
| Which AI notetaker plans include SSO, SCIM and an admin dashboard? | GSC prompt (78 impr, pos 6.88) + "for executive teams, which notetakers scale to 100+ users with sso, scim..." |
| ### Do AI notetakers support SAML SSO with Okta or Microsoft Entra ID? | GSC prompt "which ai notetakers support saml sso with okta or microsoft entra id plus scim deprovisioning for leavers?" |
| Does a 40-person sales team really need SSO for an AI notetaker, or is Google login fine? | GSC prompt (pos 7.5) |
| How should regulated teams handle transcript retention and an audit trail? | GSC prompt "looking for options besides zoom ai companion for regulated teams that need configurable transcript retention and an audit trail" (65 impr) |
| Does Microsoft Copilot in Teams give enough retention, consent and audit control? | GSC prompt (38 impr, pos 6) |
| Can admins enforce a recording notice for everyone on the call without a bot joining? | GSC prompts (recording notice without a bot, 300 employees; 150-person company that prohibits recording bots) |
| Which popular AI notetakers are genuinely enterprise-grade, and which are built for individuals? | GSC prompt (pos 2.6) |
| What should an AI notetaker security policy include? | Autocomplete: "ai note taker policy" |
| ### What mistakes do teams make when approving an AI notetaker? | SERP decomposition (Lockton risk guide, Granola and Notion checklists in the top results) |

FAQ sources: autocomplete ("ai note taker hipaa", "ai note taker attorney client privilege", "are ai note takers legal"), GSC ("do ai notetakers offer volume discounts...", "which ai notetakers can individual employees start using without a company-wide it rollout?"), and the training question from the Lynkk and Zoom security FAQs.

Result: 9 question H2s + 3 question H3s, all sourced. 0 dead headings.

## 3. Gate A: /aeo-score (threshold 80)

```
D1  Heading Format & Answer Structure   19 / 20
D2  Section & Paragraph Structure       10 / 10
D3  FAQ Quality                         15 / 15
D4  Structured Formats & Extractability 15 / 15
D5  Data Density, Entity & Citations    17 / 20
D6  Multi-Intent & Completeness          9 / 10
D7  E-E-A-T & Trust Signals              5 /  5
D8  Internal Linking                     5 /  5
TOTAL                                   95 / 100   GATE: PROCEED TO HUMANIZATION
```

- D1: 9/9 non-structural H2s are questions. Every first sentence is under 29 words. Definition ("AI notetaker security is the set of controls...") falls inside the first 100 words. Clean H1 > H2 > H3. Minus 1: "The five controls at a glance" is a structural H2 (allowed, but it opens with a table, not an answer sentence).
- Clip check: 10/18 section clips carry a number (target 50% or more, met). 0 throat-clearing openers. The Quick Answer clip carries $670,000 and the five-check claim. The 8 no-number clips all make a concrete claim (for example "SSO, SCIM and a full admin console almost always sit on the top, sales-quoted tier").
- D2: 0 paragraphs over 4 sentences, 0 over 80 words, no H2 section over 300 words without H3s.
- D3: 6 FAQs, 49 to 55 words each. Body, FAQPage JSON-LD and source text are generated from one place (`scripts/build_schema.py`), so they match word for word.
- D4: 3 tables (all 3 columns), 6 lists, a summary table near the top, a mistakes section, and contrast (when Google login is enough versus when SSO pays; where Lynkk fits and where it doesn't).
- D5: named stats from IBM via Help Net Security, NPR, Zoom, sso.tax, IETF, Microsoft Learn, HHS, ABA and Lynkk's own pages. Minus 3: 9 linked external citations for about 2,350 prose words is under the 8-to-12-per-1,500 band, and ABA Formal Opinion 512 is named but not linked (americanbar.org blocks automated fetches, so the link could not be verified).
- D6: 9 distinct sub-intents. Minus 1: 2,584 words counted including table text (about 2,350 prose), just over the 2,500 cluster band.
- D7: named author with bio URL, visible date, every claim traced to a live source.
- D8: 10 internal links (band 8 to 14), pillar link to `/security`, descriptive anchors.

Meta checklist: meta_title 58 chars with the primary keyword in the first 50 · meta_description 151 chars · no "Official" · H1 13 words · slug `ai-notetaker-security` (evergreen, no year) · 0 em or en dashes in the file · tldr 61 words · no sentence over 40 words · contractions match Lynkk's site voice.

## 4. Gate A: /seo-score (threshold 85 + G1 to G4)

```
S1  Meta tags & SERP snippet               14/15  (OG tags set at CMS level)
S2  Heading hierarchy & keyword placement  10/10
S3  Primary & secondary keyword usage      14/15  (primary density 0.58%, all 10 secondaries present)
S4  Internal linking                       10/10
S5  External linking & authority            5/5
S6  Image SEO                               6/10  (alt text written; banner pending, no Lynkk image skill here)
S7  Schema markup                          10/10  (Article + BreadcrumbList + FAQPage, inLanguage, no Product)
S8  Content depth & engagement             10/10
S9  Mobile-friendly markup                  5/5   (tables 3 columns)
S10 E-E-A-T signals                         5/5
S11 URL & link health                       5/5   (20/20 live, HHS 403 = gov pass)
PART 1 TOTAL                               94/100
G1 Intent & SERP-format match              PASS (guide/checklist matches the SERP)
G2 Keyword-uniqueness / cannibalization    PASS (see topic score G2)
G3 Competitive depth vs SERP median        PASS (SERP guides run about 1,500 to 2,500 words)
G4 Query fan-out integrity                 PASS (9 sourced question H2s, 0 dead)
INBOUND-LINK GATE                          PLANNED, NOT PLACED (see section 8)
VERDICT: SEO-READY
```

## 5. Humanization

The model-side rewrite is the supported path (no `/humanize-*` skill for Lynkk on this machine). The backup was written first. The rewrite changed body prose only. Headings, every figure, every link, frontmatter, FAQ, schema and citations were frozen.

## 6. Gate B: /post-humanize-check

```
C1  Keyword presence              0 missing
C2  Primary KW in H1              PASS
C3  H2 question ratio             PASS (9/12, was 9/12; the 3 others are structural: glance table, FAQ, Conclusion)
C4  Internal links present        0 missing
C5  Em/en dashes                  0
C6  Banned words                  0
C7  Link count delta              0 added, 0 removed
C8  Frontmatter integrity         PASS (byte-identical)
C9  Schema / FAQ integrity        PASS (FAQ body and JSON blocks byte-identical)
C10 Brand specs                   PASS ("Lynkk" spelling, $15 / $117, 10-member workspaces, AES-256-GCM)
C11 Numbers integrity             PASS (0 missing, 0 added)
C12 Figures traceable             PASS (every figure sits in a section with a named or linked source)
C13 Draft artifacts               0
C14 Positioning vs live site      PASS for the article; FLAG for the brand memo (see section 9)
C15 Batch duplication             N/A (single article)
C16 Cluster siblings              WARN: 3 related pages, all linked or planned as inbound sources
C17 Delta re-score                95/100 (D2 re-measured 10/10 after one paragraph split; D1 answer layer, D5 entity, D6 word count unchanged; D3/D4/D7/D8 carried)
VERDICT: PASS, 1 mechanical fix (split one 5-sentence paragraph), 0 hard fails
```

## 7. /humanize-verify (before vs after)

| Signal | Before | After | Target |
|---|---|---|---|
| Burstiness (CV of sentence length) | 0.472 | 0.519 | 0.5 or more |
| Sentence-length stdev | 7.70 | 8.04 | higher |
| Mean sentence length | 16.3 | 15.5 | about 15 to 18 |
| Paragraph-length stdev | 16.49 | 17.58 | higher |
| Repeated-opener rate | 0.042 | 0.046 | low |
| AI-tell words | 0 | 0 | 0 |
| Em/en dashes | 0 | 0 | 0 |

Verdict: **HUMANIZER WORKING** on proxy signals. Burstiness moved +0.047 (more than the 0.02 "paraphrase only" line) and crossed the 0.5 floor. These are proxies, not a detector: spot-check with GPTZero or Originality.ai before publishing if you need that guarantee.

## 8. Handoff: what a human still has to do

1. **Inbound links (HARD gate, not done; I have no CMS access).** Add a contextual link to `/blog/ai-notetaker-security` from at least 2 of:
   - `/security` "Related guides" block (anchor: "AI notetaker security checklist")
   - `/blog/ai-powered-meeting-assistants`, section "Is an AI-powered meeting assistant safe to use?" (anchor: "how to check AI notetaker security")
   - `/blog/zoom-ai-companion-alternatives`, H3 "Retention and audit trail for regulated teams" (anchor: "transcript retention and audit trail checklist")
   - `/blog/is-it-legal-to-record-a-meeting`, section "Are meeting bots and AI note takers legal?" (anchor: "AI note taker security and consent controls")
   Then verify the links are live.
2. **Banner image.** `featured_image_path` is a placeholder; alt text is written.
3. **Tracked prompts.** The 7 `targeted_prompts` came from GSC. Register them in the prompt tracker if Lynkk uses one (prompt gap, so create_prompt).
4. **Publishing** needs explicit approval. Strip the `---CITATIONS---`, `---SCHEMA---` and `---FAQ_JSON---` markers into the CMS fields on push.

## 9. Flags for the Lynkk team

- **Brand memo contradicts the live site (C14).** `memory/lynkk-brand.md` says "pick a region and every model behind Lynkk processes/answers from that region". The live `/security` page (last reviewed 18 October 2026) says "Your data may be processed outside your country, including in India and the US." The article follows the live page. The memo needs correcting before it is reused in tool submissions.
- **The article states Lynkk's gaps plainly:** no SSO or SCIM on the pricing or security pages, workspaces cap at 10 members, and AI subprocessors are described but not named publicly. That honesty is deliberate (it's why the page can be cited on enterprise prompts), but it is a positioning call. If SSO or SCIM is on the roadmap, or the subprocessor list can be published, update those two paragraphs before publishing.
- **Unnamed subprocessors.** Publishing Lynkk's speech-to-text and LLM provider names on `/security` would let this article (and the site) answer the 69-impression "which LLM providers see transcripts" prompt with Lynkk as the example.
