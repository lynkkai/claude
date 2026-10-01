---
name: embed-keywords-prompts
description: Embed a visible 'Keywords & Prompts Targeted' block directly inside each article (between marker comments) so the client can see what the blog targets without running a separate report. The block is auto-stripped on CMS push so it never reaches the live blog.
---

<!-- Provenance: Unveilr platform registry · category=content · version=1 · scope=global · synced 2026-08-25 -->

# Embed Keywords & Prompts in Article

The client wants to open a single blog and immediately see which keywords and tracked MCP prompts it targets — without running a separate report command. This skill injects a clearly labelled editorial block into the article body, between **strip-on-publish marker comments**, so:

- The client sees the keyword/prompt map in the article markdown AND in the client-review DOCX
- The CMS push step (`/push-to-wordpress`, Shopify push) automatically strips the block so it never appears on the live published blog

Unlike `/keywords-prompts-report` (which produces a separate report), this skill **modifies each article in place**.


## ⚡ BATCH ACROSS A WAVE — do not run this once per article

This skill is frontmatter extraction plus a hyphen-insensitive body grep. It carries no
per-article reasoning cost, so running it ten times for a ten-article wave costs 10-20 min
each for work that takes ~30 min once across all ten. Journey A step 10 batches it.

Pass every slug in one invocation. The only per-article output that must stay separate is
the in-article block itself (it is written into each file); the report is one table with a
row per article.
## Input

$ARGUMENTS

Parse for:
- **articles**: One or more article slugs OR paths to `.md` files. Required. Accepts `all`.
- **client**: Brand context. Default and primary target: `nuyug`. Loads MCP for prompt mapping.
- **position**: `top` (default — block goes just under the H1) or `bottom` (block goes just above `---CITATIONS---`). `top` is best for client review; `bottom` keeps it out of the way during writing.
- **rebuild**: If `true`, REPLACE the existing block with a freshly computed one. If `false` (default), only inject if no block exists.

---

## What the block looks like

The block is wrapped in HTML comment markers that pandoc, WordPress, and Shopify all respect as strip-safe:

```markdown
<!-- KEYWORDS_PROMPTS_BLOCK_START — strip before CMS push -->

## Keywords & Prompts Targeted *(editorial review only — removed before publish)*

**Primary keyword:** `<primary>`

### Target keywords (verified in body)

| Keyword | Occurrences in body |
|---|---|
| <keyword> | ✅ (×N) |
| <keyword> | ⚠️ MISSING |

### Tracked AI prompts targeted

| Prompt (from <brand> MCP tracker) | Role |
|---|---|
| <prompt text> | Primary |
| <prompt text> | Secondary |
| <prompt text> | Partial |

*This section is auto-removed before publishing to the live blog. Visible only in the editorial markdown and client-review DOCX.*

<!-- KEYWORDS_PROMPTS_BLOCK_END -->
```

---

## Workflow

### STEP 1: Resolve files & detect existing block

For each article:
- If file contains both `<!-- KEYWORDS_PROMPTS_BLOCK_START` and `KEYWORDS_PROMPTS_BLOCK_END -->` markers, treat as already-injected
- If `rebuild=true`, delete the existing block (everything between the markers, inclusive of markers)
- If `rebuild=false` and the block exists, skip the article and report "already has block"

### STEP 2: Extract metadata

Pull from frontmatter:
- `title`, `slug`/`suggested_url`, `brand`, `project_id`
- `primary_keyword` = first entry of `selected_keywords` (fallback: first entry of `keywords`)
- `target_keywords` = full `keywords` array

### STEP 3: Verify keyword presence in body (hyphen-insensitive)

For each target keyword, compute occurrence count in the **body only** (exclude frontmatter, citations, schema, FAQ_JSON, and any existing keywords-prompts block).

```bash
body=$(awk '/^# /{flag=1} /^<!-- KEYWORDS_PROMPTS_BLOCK_START/{flag=0} /^---CITATIONS---/{flag=0} /^<!-- KEYWORDS_PROMPTS_BLOCK_END/{flag=1; next} flag' "$file" | tr '[:upper:]' '[:lower:]' | tr '-' ' ')
kw_norm=$(echo "$keyword" | tr '[:upper:]' '[:lower:]' | tr '-' ' ')
count=$(echo "$body" | grep -oF "$kw_norm" | wc -l)
```

Display each keyword as:
- ✅ (×N) — if count ≥ 1
- ⚠️ MISSING — if count == 0

**Important:** if any keyword is MISSING, log a warning but still inject the block. The client should see the gap. The fix is a separate keyword-injection pass, not silent omission.

### STEP 4: Map article to tracked MCP prompts

If the brand has a connected Unveilr MCP:

1. Call `mcp__unveilr-<brand>__list_prompts` to get all tracked prompts (filter: `include_archived=false`)
2. For each prompt, classify match against the article (same heuristics as `/keywords-prompts-report`):
   - **Primary** — prompt text matches body (hyphen-insensitive) OR exactly matches `selected_keywords`
   - **Secondary** — ≥70% of content words appear in body within one H2 section
   - **Partial** — only core noun phrase appears
3. Sort: Primary first, then Secondary, then Partial. Cap at 8 prompts (most relevant).

If no MCP: skip the prompts table and note "MCP not connected — prompt mapping omitted."

### STEP 5: Build the block

Render the markdown shown above with computed data. Pay attention to:
- The `*(editorial review only — removed before publish)*` line is mandatory — it tells anyone reading the markdown that this section is not for end users
- Markers `<!-- KEYWORDS_PROMPTS_BLOCK_START — strip before CMS push -->` and `<!-- KEYWORDS_PROMPTS_BLOCK_END -->` are exact strings — DO NOT modify them. The CMS push step matches on these exact strings.

### STEP 6: Inject into article

For `position=top`: insert immediately after the H1 line and any leading TL;DR/intro paragraph that already exists. Insertion point: first blank line after the H1.

For `position=bottom`: insert immediately before the `---CITATIONS---` line.

Use `Edit` tool with sufficient context (surrounding lines) to make the insertion unambiguous.

### STEP 7: Regenerate downstream deliverables

If the article has a corresponding `.docx` file in `articles/`:
- Re-run pandoc to produce the updated DOCX
- Apply the table-border script (`/tmp/finalize_nuyug_docx.py` pattern or equivalent)
- Apply the banner-at-top insertion (if `featured_image_path` is in frontmatter)

So one command updates both the `.md` and the `.docx` together.

### STEP 8: Report to user

For each article processed:
- ✅ Block injected at <position>
- N target keywords (M present, K missing — list the missing ones)
- N MCP prompts mapped (P primary, S secondary, R partial)
- DOCX regenerated: yes/no

---

## CMS push integration (the strip step)

Both `/push-to-wordpress` and the Shopify push helper must include this strip step **before** uploading content:

```python
import re
# Match the block including its markers, non-greedy
STRIPPER = re.compile(
    r"<!--\s*KEYWORDS_PROMPTS_BLOCK_START.*?KEYWORDS_PROMPTS_BLOCK_END\s*-->",
    re.DOTALL,
)
cleaned = STRIPPER.sub("", article_markdown_or_html).strip()
```

The two skills/scripts that push to CMS already have a hook for content sanitization — add this regex to it. If the hook doesn't exist, add a wrapper function `strip_editorial_blocks(content)` and call it at the start of the push.

**Tests to add:**
- Round-trip test: inject block → strip → confirm no residual `<!-- KEYWORDS_PROMPTS` markers
- Idempotency test: strip twice → identical output

---

## Important rules

1. **The block is markdown, not Liquid/HTML.** It renders cleanly in pandoc → DOCX. WordPress and Shopify will render the markers as HTML comments (invisible in the page source viewer's render but visible in "view source"). The CMS push step strips them before publish, so they never reach the live page.
2. **Marker strings are exact.** `<!-- KEYWORDS_PROMPTS_BLOCK_START — strip before CMS push -->` and `<!-- KEYWORDS_PROMPTS_BLOCK_END -->`. Any drift breaks the strip regex.
3. **Never inject if the article hasn't passed `/aeo-score` ≥80.** Premature keyword/prompt blocks just hide unfinished articles. Block injection is the very last editorial step before client review.
4. **Hyphen-insensitive matching everywhere.** Same rule as `/keywords-prompts-report` and `/seo-optimize`.
5. **One block per article.** If an existing block is detected and `rebuild=false`, skip. If `rebuild=true`, replace cleanly (no stacked blocks).
6. **Default position is `top`.** Clients want to see the targeting before they start reading. The strip-on-publish marker means it doesn't hurt SEO/AEO of the live blog.
7. **MCP unavailable ≠ skip the whole block.** Still render the keywords table — only the prompts table is conditional on MCP.
8. **Regenerate DOCX automatically.** The client deliverable is the DOCX, so any change to the markdown that affects the body must trigger a fresh `.docx`.

---

## Examples

### Example 1 — inject into one article

```
/embed-keywords-prompts imitation-jewellery-looks-like-real-gold client=nuyug
```

### Example 2 — refresh blocks on the whole Nuyug batch

```
/embed-keywords-prompts all client=nuyug rebuild=true
```

### Example 3 — bottom placement

```
/embed-keywords-prompts a b c d e position=bottom
```

---

## Why this is better than `/keywords-prompts-report`

| Concern | `/keywords-prompts-report` | `/embed-keywords-prompts` |
|---|---|---|
| Client opens DOCX, sees targeting | Separate report file | Same article DOCX, top of page |
| Client opens markdown in editor | Has to run a command | Sees it inline |
| Risk of leaking to live blog | None (separate file) | Mitigated by strip-on-push marker |
| Re-runnable / refreshable | Yes | Yes (`rebuild=true`) |
| Works when MCP is offline | Yes | Yes (keywords table only) |

Prefer `/embed-keywords-prompts` as the default editorial workflow. Use `/keywords-prompts-report` only when the client wants a standalone audit document covering many articles at once.
