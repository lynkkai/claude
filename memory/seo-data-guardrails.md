# SEO & Keyword Data Guardrails

> Applies to every SEO audit, keyword brief, content plan, or competitor analysis in this repo.
> Goal: no keyword number, ranking, or competitor claim is ever assumed, estimated, or recalled from memory.

## 1. Every metric needs a source

- Search volume, CPC, SEO difficulty (SD), paid difficulty (PD), position, traffic, estimated clicks,
  domain authority, and backlink counts must come from a **tool call made in the current session**
  (Ubersuggest, Google Search Console, or another connected tool).
- Each number is written with its provenance: tool + endpoint, location (`locId`, e.g. `2840 US`, or `Global`),
  language, and the data date (`updated_at` when the tool returns one, otherwise the pull date).
- Never fill a metric from general knowledge, a blog post, an earlier conversation, or "typical" values.

## 2. Missing data stays missing

- If a tool returns `noData`, an empty list, an error, or a quota limit (HTTP 403), write
  **"Not available"** with the reason (e.g. `Not available: Ubersuggest daily report quota reached`).
- Never replace a missing value with a plausible number, a range, or "~".
- After a quota error, stop calling that tool for the day. Do not retry in a loop.

## 3. Do not convert one metric into another

- Ubersuggest SERP `clicks` is Ubersuggest's estimate of clicks to **that URL**. It is not the keyword's
  search volume and must not be summed, scaled, or reused as volume.
- `clicks: -1` means "not estimated". Report it as "not estimated", never as zero.
- Domain authority is not a ranking prediction. Do not write "Lynkk can rank for X" from DA alone.
- Do not project traffic, rankings, or conversions from recommendations.

## 4. Never mix locations or dates silently

- Compare numbers only when they share the same `locId` and language.
- Global data and US data (`2840`) are reported in separate columns or tables.
- Always state the SERP snapshot date; SERPs change weekly.

## 5. Label every claim by confidence

Use exactly one of these labels in reports:

| Label | Meaning |
|---|---|
| **Verified (tool)** | Returned by a tool call in this session, with provenance attached |
| **Verified (page)** | Read directly from the live page HTML in this session |
| **Third-party / snippet** | Seen in a search result snippet or another site's copy; not checked on the source |
| **Unvalidated candidate** | A keyword or idea without metrics yet; must be validated before it goes into a writer brief |
| **Hypothesis** | Reasoning or recommendation; not a data point |

## 6. Keyword recommendations

- A keyword can be called a **target** only after its volume, SD, and SERP have been pulled for the
  chosen location. Until then it is an **unvalidated candidate**.
- Keywords suggested by reasoning (not by a tool) are always marked **Hypothesis**.
- People Also Ask questions, related searches, and FAQ topics are quoted only if a tool returned them.
  Otherwise they are listed as hypotheses to validate.

## 7. Product and competitor claims

- Lynkk product claims come only from `memory/lynkk-brand.md` or the live lynkk.ai page. Items listed
  under "To confirm" in the brand memory (languages, platforms, CRMs, pricing, regions) are not stated
  as facts in copy.
- Competitor features, pricing, and stats from search snippets are **Third-party / snippet** and must
  not be presented as verified.

## 8. Report the gaps

Every audit ends with a **Data gaps** section: which calls failed or were skipped, why, and the exact
calls to run next to close each gap.
