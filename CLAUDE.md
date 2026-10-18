# Project memory

This repo supports marketing work for **Lynkk** (https://lynkk.ai), an AI meeting assistant.
Brand spelling is always "Lynkk" (double k), not Lynk, Linnk, or Link AI.

Full brand/product details and ready-to-use tool-submission copy: @memory/lynkk-brand.md

## Writing rules

These apply to all Lynkk copy, marketing text, and anything written in this repo.

- **Never use em dashes (—) or en dashes (–).** Use a comma, colon, parentheses, or
  split the sentence instead. Use a plain hyphen for ranges and compound words.

## Blog articles

Drafts live in `blog/articles/` (index and editorial notes in `blog/README.md`). Before committing an article,
run `python3 blog/tools/check_articles.py` (must report 0 failures) and `python3 blog/tools/build_schema.py`.
Use only Lynkk facts from the "Verified on lynkk.ai" section of `memory/lynkk-brand.md`.
