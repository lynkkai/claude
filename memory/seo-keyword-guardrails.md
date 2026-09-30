# SEO & Keyword Data Guardrails

These rules apply to every keyword, SEO, or content-optimization task in this repo.
The goal: **no keyword number, ranking, or competitor claim goes into a deliverable unless
it came from a tool response in the same session.**

## 1. Every number needs a source

- Search volume, CPC, SEO difficulty (SD), paid difficulty (PD), position, traffic,
  backlinks, and domain authority must come from an Ubersuggest (or other connected
  tool) response. Never estimate, round up, "ballpark", or recall them from memory.
- Every metric in a report must state: **tool, endpoint, location (locId), language, and
  date pulled.** Example: `Ubersuggest keyword_overview, US (2840), en, 2026-09-30`.
- Location matters. A US number is not a global number. Never mix locations in one table
  without a location column.

## 2. Missing data is reported as missing

- If a tool returns no data, zero, `null`, or an error, write **"No data (Ubersuggest)"**.
  Do not substitute a guess, a similar keyword's number, or an "industry average".
- Zero volume is a real result and is reported as `0`, not dropped from the table.
- If a tool call fails (auth, quota, timeout), say so in the report and list which
  keywords were not checked.

## 3. Label what is data and what is judgment

Every recommendation is tagged with one of:

| Tag | Meaning |
|---|---|
| **[DATA]** | Directly stated by a tool response (quote the number). |
| **[OBSERVED]** | Seen on a fetched page (competitor or Lynkk) in this session. |
| **[JUDGMENT]** | Analyst recommendation built on the above. Must cite which [DATA]/[OBSERVED] items it rests on. |
| **[UNVERIFIED]** | Could not be checked (page blocked, tool returned nothing). Must say what is needed to verify it. |

Nothing may be presented as fact if it is only [JUDGMENT] or [UNVERIFIED].

## 4. Competitors must be evidenced

- A domain is called a "competitor" for a keyword only if it appears in the Ubersuggest
  `serp_analysis` (or `competitors`) result for that keyword, or the team named it.
- Do not claim a competitor ranks for a term, has a feature, or uses certain copy without
  a SERP result or a fetched page to back it.

## 5. Lynkk page content must be seen, not assumed

- Do not audit a Lynkk page's copy (title, H1, word count, sections) unless it was fetched
  in this session or supplied by the team. If it could not be fetched, mark the on-page
  audit **[UNVERIFIED]** and list only data-backed keyword gaps.
- Product claims in suggested copy must come from `memory/lynkk-brand.md`. Anything not
  there (pricing, integrations, languages, certifications) goes on the "To confirm" list,
  not into copy.

## 6. Keyword choice rules

- Do not pick a target keyword because it "sounds right". Pick it from tool output
  (volume, SD, intent, SERP makeup) and show the numbers next to it.
- Prefer keywords where the SERP (from `serp_analysis`) shows product/feature pages over
  keywords whose SERP is all blog listicles, and say which it is.
- Flag brand-confusion risk: never target "lynk", "link ai", or similar misspellings as if
  they were Lynkk's brand terms (see `memory/lynkk-brand.md`).

## 7. Keep raw data

Save raw tool responses (or a faithful table of them) alongside any report under
`seo/data/`, so every number in a report can be traced back.
