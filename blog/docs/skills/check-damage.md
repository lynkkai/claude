---
name: check-damage
description: Retro-audit already-published articles against rules that only became blocking AFTER they shipped — prompt-lock drift, dead headings, unsourced fan-out, orphaned pages, draft artifacts left live. Use when a gate or hard rule is newly added or newly enforced and nobody knows how much live content already violates it, when a cluster is suspected of self-cannibalizing, or before a consolidation decision. Finds the damage no gate caught because the gate did not exist yet. Read-only: it never edits, merges or deletes an article.
---

<!-- Provenance: authored 27 August 2026. Local-only; not yet in the platform registry. -->
<!-- WHY THIS EXISTS: the query fan-out rule and the H1-verbatim prompt contract only
     became blocking on 27 Aug 2026. Every article written before that passed a Gate A
     that did not check either one. First run on Aviaan's 17 articles: 12 CRITICAL
     findings and three tracked prompts each claimed by THREE separate articles. -->

# Check-Damage — retro-audit of shipped content

Gates only protect what they existed for. When a rule becomes blocking, everything already published was scored by the older, weaker gate — and nothing goes back to look. This skill goes back to look.

It answers one question: **which live pages violate today's rules, and which of those violations is actually costing us citations?**

## ⛔ HARD RULE 1 — read-only, always

This skill NEVER edits, merges, redirects or deletes an article. It produces findings and a ranked remediation plan. Every fix is a separate, human-approved action:

- A **rewrite** goes back through the normal pipeline (`/aeo-article-aviaan` → Gate A → humanize → Gate B).
- A **consolidation** (301 + merge) touches live URLs and inbound links. It needs the AM and typed client approval. Proposing one here is not authorisation to do it.
- A **deletion** is never the answer. Consolidate into the winner instead; a deleted URL throws away whatever equity it had.

Report what you found. Let a human decide what dies.

## ⛔ HARD RULE 2 — a clean script run is NOT a pass

`scripts/check_damage.py` is deterministic and offline. It checks structure, not truth. It cannot tell you whether a page is live, whether it earns impressions, whether its figures are still accurate, or whether an answer engine cites it. **Those need the MCP phases below.** Reporting "0 findings" after running only the script is the exact failure this skill exists to prevent — say SKIPPED for every phase you did not run.

## ⛔ HARD RULE 3 — never guess which page wins a collision

When N articles claim the same tracked prompt, the survivor is decided by **evidence, not by word count and not by which reads best.** Pull GSC impressions/clicks, prompt-citation data, and inbound internal links for each candidate before recommending one (Phase 3). A consolidation that keeps the wrong page destroys the one that was working.

---

## Input

`$ARGUMENTS`

Parse for:
- **target** (optional, default `articles/`) — a directory or specific `.md` paths.
- **client** (optional, default `aviaan`) — sets the domain and internal-link band.
- **rules** (optional) — audit against a named rule set only: `fanout` | `prompt-lock` | `links` | `artifacts` | `all` (default).
- **depth** (optional) — `script` (Phase 2 only, fast) | `full` (all phases, default).

Client bands: **aviaan** → `aviaanaccounting.com`, links 8–14. **nuyug** → links 5–6. **vakilsearch** → links 8–14, word target 2,000. **jaagrukbharat** → links 8–14, words 900–1,500.

---

## PHASE 1 — Scope the audit surface

Establish what counts as "shipped" before auditing anything.

1. List candidate files. The script already skips `*.original`, `*.pre-*`, `*.bak*` and anything under `superseded/` — **do not audit a backup and report it as a live defect.**
2. Separate **live** from **local-only**. `cms_published: true` in frontmatter is not proof a page is live, and `list_articles` is not in sync with the local folder. Confirm with `check_urls_liveness` on the real URL, or `search_serp site:<domain> <slug>`.
3. State the split plainly: *"17 local articles, N confirmed live, M local-only drafts."* Findings on a local-only draft are cheap to fix; findings on a live page are the damage.

## PHASE 2 — Run the deterministic audit

```bash
python3 ~/.claude/skills/check-damage/scripts/check_damage.py articles/
python3 ~/.claude/skills/check-damage/scripts/check_damage.py articles/ --json    # for chaining
python3 ~/.claude/skills/check-damage/scripts/check_damage.py articles/ --links 5 6 --domain nuyug.com
```

Eleven rules. Severity reflects citation cost, not effort to fix:

| Rule | Severity | What it catches |
|---|---|---|
| R2 | CRITICAL | H1 is not `targeted_prompts[0]` verbatim — reports the drift *kind* (title-cased / appended year / `versus`→`vs` / dropped words) because the fix differs per kind |
| R3 | CRITICAL | **Prompt lock broken** — two or more articles claim the same prompt and split each other's citations |
| R1 | HIGH | No `# ` H1 in the body (title only in frontmatter) — contract unverifiable, CMS may render no H1 |
| R4 | HIGH | No parseable `targeted_prompts` — the article claims no prompt |
| R6 | CRITICAL / HIGH / MEDIUM | Dead headings. Exact matches FAIL (2+ = CRITICAL, mirrors the Gate A block); generic-prefix hits are MEDIUM and flagged for a human to eyeball |
| R7 | HIGH | Draft artifacts live on the page — `(industry estimate)`, `(approx)`, `TBD`, `TODO`, `XX` |
| R5 | MEDIUM / LOW | H2 count outside the 6–9 fan-out band |
| R10 | MEDIUM / LOW | Internal links outside the client band |
| R11 | MEDIUM | FAQ section with no `###` headings — bold text does not parse as a heading |
| R8 / R9 | LOW | Em-dashes; banned words |

**Two parser facts the script now handles — do not regress them.** Frontmatter list fields appear in *both* an inline style (`keywords: ["a","b"]`) and a YAML block style (`- "a"` on following lines). Reading only the inline form reports "no prompt recorded" on articles that do record one — a false clean. And R6's generic-prefix check is a WARN, never a FAIL: the script cannot judge whether a heading came from a real query, so it defers to a human instead of inventing a verdict.

## PHASE 3 — Reality check the CRITICALs (MCP; this is the phase that decides fixes)

Structure findings are hypotheses about lost citations. Confirm which ones cost anything.

For every CRITICAL, and for every candidate in a collision cluster:

- `get_gsc_page_queries` on the live URL — impressions, clicks, position. **Never sum query rows to get a page total; that undercounts ~8.5x. Use the page row.** An empty query list does not mean zero traffic.
- `get_prompt_article_coverage` / `get_mention_results_by_prompt` — is the tracked prompt actually citing us, and which URL does it cite?
- `get_zero_visibility_prompts` — a colliding cluster sitting at zero visibility is the strongest possible consolidation signal.
- `get_top_cited_urls_for_domain` — which of the candidates answer engines already prefer.
- Inbound internal links to each candidate. The page with more inbound links usually wins even when it reads worse — that was the whole finding of the VS CIN case (0 impressions vs ~602, decided 1 link vs 4).

Then classify each finding:

- **BLEEDING** — live, violating, and has impressions or citations to lose. Fix first.
- **DORMANT** — live and violating but earning nothing. Cheap to consolidate or rewrite.
- **COSMETIC** — violating a LOW rule with no measurable cost. Batch it into the next touch; do not open a ticket.

A finding you could not verify is **UNVERIFIED** — say so. Do not promote it to BLEEDING on a hunch or demote it to COSMETIC for convenience.

## PHASE 4 — Consolidation recommendation (proposal only)

For each collision cluster, name the survivor and justify it on Phase 3 evidence:

1. **Winner** — the URL with the strongest combination of citations, impressions and inbound links. Not the longest article.
2. **What migrates** — sections, tables, citations and figures the losers hold that the winner lacks. A merge that drops unique sourced data makes the cluster worse.
3. **Redirect map** — loser URL → winner URL, 301.
4. **Inbound links to repoint** — every internal link pointing at a loser must be re-pointed at the winner, or the merge leaks the equity it was meant to consolidate.
5. **Prompt hygiene** — after the merge exactly one article carries that prompt in `targeted_prompts`; the losers' prompts are reassigned or archived.

Present it as a proposal and stop. Hard Rule 1.

## PHASE 5 — Report

```
══════════════════════════════════════════════════════════════
CHECK-DAMAGE REPORT — <client>
Audited: N local · M confirmed live · scope: <rules>
══════════════════════════════════════════════════════════════

BLEEDING    n   (live, violating, earning — fix first)
DORMANT     n   (live, violating, earning nothing)
COSMETIC    n   (LOW rules, no measurable cost)
UNVERIFIED  n   (could not confirm — say why)
CLEAN       n / N

PROMPT COLLISIONS
  <prompt>
    <url>  impressions X · clicks Y · cited by Z prompts · N inbound  ← KEEP
    <url>  impressions X · clicks Y · cited by Z prompts · N inbound  → 301
  Migrate before redirecting: <unique sections/data>

RANKED REMEDIATION
  1. <article> — <finding> — <action> — <why it is first>
  ...

PHASES RUN:  1 ✅  2 ✅  3 ✅/SKIPPED  4 ✅/SKIPPED
```

Lead with the collisions. One prompt answered by three pages is worse than thirty cosmetic findings, and it is the finding an AM can act on immediately.

---

## Lessons (extend as you learn)

- **The first run is always worse than expected.** Aviaan, 27 Aug 2026: 17 articles, 12 CRITICAL findings, and three tracked prompts each claimed by **three** separate articles. Nobody had shipped anything careless — the rules simply arrived after the content did.
- **Fix the parser before trusting the count.** The same run initially reported 9 CRITICAL and "no prompt recorded" on four articles that did record prompts, in YAML block style. The corrected parse revealed the clusters were three deep, not two. **A false clean is more expensive than a false alarm** — when a field looks absent, check the format before believing it.
- **Title-casing an H1 is the single most common drift**, and the cheapest CRITICAL to fix. `(2026)` appended to an H1 is second. Both come from the pre-fan-out Phase 5 instruction "H1: primary keyword + year + geo", which Hard Rule 4 now overrides — so expect them in anything written before 27 Aug 2026.
- **A collision cluster usually contains one good newer article and two older ones.** The newer rewrite often has the verbatim H1 and no body-level `# ` heading at all, because it was drafted straight into frontmatter. Check R1 and R2 together before picking a winner.
- **Word count is not evidence.** In Aviaan's clusters the longest article was never the one with the most inbound links.
