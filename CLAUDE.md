# Project memory

This repo supports marketing work for **Lynkk** (https://lynkk.ai), an AI meeting assistant.
Brand spelling is always "Lynkk" (double k), not Lynk, Linnk, or Link AI.

Full brand/product details and ready-to-use tool-submission copy: @memory/lynkk-brand.md

SEO tooling, Search Console data and audit findings: @memory/seo-toolkit.md

## Writing rules

These apply to all Lynkk copy, marketing text, and anything written in this repo.

- **Never use em dashes (—) or en dashes (–).** Use a comma, colon, parentheses, or
  split the sentence instead. Use a plain hyphen for ranges and compound words.

Exception: files under `.claude/skills/` are vendored third-party skills, kept
verbatim so they can be updated from upstream. Do not rewrite their punctuation.

## SEO

Two skills are installed under `.claude/skills/`:

- `seo-audit`: strategy and on-page framework, report structure, prioritisation.
- `seomator-audit`: the SEOmator CLI (`seomator`), 373 automated rules across 20 categories.

Use both together for any audit. See @memory/seo-toolkit.md for run commands and
the network prerequisite.
