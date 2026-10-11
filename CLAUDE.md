# Project memory

This repo supports marketing work for **Lynkk** (https://lynkk.ai), an AI meeting assistant.
Brand spelling is always "Lynkk" (double k), not Lynk, Linnk, or Link AI.

Full brand/product details and ready-to-use tool-submission copy: @memory/lynkk-brand.md

## Writing rules

These apply to all Lynkk copy, marketing text, and anything written in this repo.

- **Never use em dashes (—) or en dashes (–).** Use a comma, colon, parentheses, or
  split the sentence instead. Use a plain hyphen for ranges and compound words.

## Web access (why lynkk.ai shows as "blocked")

The cloud environment was switched to **Full** network access on 2026-10-11, so new
sessions can reach lynkk.ai and other sites. If a session is ever blocked again, the cause is
the environment's network policy (Limited/trusted), not the Lynkk website: outbound traffic
then goes through an egress proxy that only allows package registries and GitHub, every
other site gets `403 Forbidden` on CONNECT, and WebFetch fails with `getaddrinfo ENOTFOUND`.
A running session keeps the policy it started with, so a setting change only reaches new
sessions.

The site publishes a good machine-readable summary at https://lynkk.ai/llms.txt; start
research there, then check /pricing and /faq.

- **Fix (done by the user, not from inside a session):** open the cloud environment menu in
  the session title bar, choose Edit, then under Network access either pick a broader level
  or add `lynkk.ai` (plus `www.lynkk.ai`, `reddit.com`, `www.reddit.com` if needed) to
  Allowed domains. Keep "Allow package managers" ticked. Docs:
  https://code.claude.com/docs/en/cloud-environments#network-access
- **Until then:** use WebSearch (it runs outside the container and still works) and say
  clearly which facts came from search results rather than the live site. Never invent
  site details to fill the gap.
- **Quick check:** `curl -sS -o /dev/null -w "%{http_code}\n" https://lynkk.ai/` returns
  `200` once access is allowed; `000` with "CONNECT tunnel failed, response 403" means it
  is still blocked.
