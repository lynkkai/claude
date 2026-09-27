# SEO toolkit: what is installed and how to use it

Two SEO skills are installed in this repo under `.claude/skills/`. They are
complementary: run both for a full audit.

| Skill | What it is | Use it for |
|---|---|---|
| `seo-audit` | Human/strategy framework (v2.0.1) | Scoping, on-page review, content quality, E-E-A-T, keyword mapping, international SEO, report structure and prioritisation |
| `seomator-audit` | SEOmator CLI wrapper (v5.1.0, MIT) | Machine-checkable crawl: 373 rules, 20 weighted categories, Core Web Vitals, JS rendering, schema, security headers, broken links, before/after deploy diffs |

## SEOmator CLI

Installed globally with `npm install -g @seomator/seo-audit` (binary: `seomator`).
Verify with `seomator self doctor`.

Chromium for Core Web Vitals and JS rendering lives at `/opt/pw-browsers/chromium`
in Claude cloud sessions. `seomator self doctor` only probes `/usr/bin`, so link it
once per session if the doctor reports no browser:

```bash
ln -sf /opt/pw-browsers/chromium /usr/bin/chromium
```

Standard run for lynkk.ai (small site, so crawl everything):

```bash
seomator audit https://lynkk.ai --crawl -m 100 --mobile --format llm
seomator audit https://lynkk.ai --crawl -m 100 --format html -o seo-report.html
seomator compare lynkk.ai            # after a deploy
```

Do not pass `--no-cwv` for a full audit: it silently drops Core Web Vitals, the
JavaScript rendering rules and every `mobile-parity-*` rule to "unmeasured", and
scores from a `--no-cwv` run are not comparable to scores from a full run.

## Network requirement (important)

Both skills need outbound HTTPS to the site being audited. Claude cloud sessions
run behind an egress proxy that denies every host outside the package registries
unless the environment's network policy allows it. Symptom: `seomator` reports
`code="non-html"` with "returned text/plain" (that text is the proxy's own 403
body), and `curl` reports "CONNECT tunnel failed, response 403".

Fix: in the session title bar, open the cloud environment menu, choose Edit, and
under Network access either raise the access level or add `lynkk.ai` (plus
`www.lynkk.ai`) to the allowed domains. Docs: https://code.claude.com/docs/en/claude-code-on-the-web

## Search Console data

Exports live in `memory/data/`. Analysis and findings:
@memory/lynkk-seo-baseline.md
