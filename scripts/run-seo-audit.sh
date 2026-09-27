#!/usr/bin/env bash
# Full technical SEO audit of lynkk.ai using the SEOmator CLI.
#
# Prerequisites:
#   npm install -g @seomator/seo-audit
#   outbound HTTPS access to lynkk.ai (see memory/seo-toolkit.md)
#
# Usage: scripts/run-seo-audit.sh [https://lynkk.ai] [max-pages]

set -euo pipefail

SITE="${1:-https://lynkk.ai}"
MAX_PAGES="${2:-100}"
HOST="$(printf '%s' "$SITE" | sed -E 's#^https?://##; s#/.*##')"
STAMP="$(date +%Y-%m-%d)"
OUT="$(cd "$(dirname "$0")/.." && pwd)/audit/raw/${STAMP}"
mkdir -p "$OUT"

# SEOmator only probes /usr/bin for a browser. Claude cloud sessions ship
# Chromium at /opt/pw-browsers/chromium, so link it if nothing is there.
if [ ! -e /usr/bin/chromium ] && [ -e /opt/pw-browsers/chromium ]; then
  ln -sf /opt/pw-browsers/chromium /usr/bin/chromium
fi

echo "==> Preflight: can we reach ${HOST}?"
if ! curl -sS -o /dev/null --max-time 20 -I "$SITE"; then
  echo "FAILED: ${HOST} is not reachable from here." >&2
  echo "If curl reported 'CONNECT tunnel failed, response 403', the environment's" >&2
  echo "network policy is denying the host. Allow it in the cloud environment's" >&2
  echo "Network access settings, then re-run. See memory/seo-toolkit.md." >&2
  exit 2
fi

echo "==> Doctor"
seomator self doctor || true

echo "==> Full crawl (Core Web Vitals + JS rendering + mobile parity)"
# No --no-cwv: that would drop Core Web Vitals, the JS rendering rules and every
# mobile-parity rule to "unmeasured" and make the score incomparable.
seomator audit "$SITE" --crawl -m "$MAX_PAGES" --mobile --format llm \
  -o "$OUT/audit.llm.xml" -v

echo "==> Same run, JSON and HTML for the record"
seomator audit "$SITE" --crawl -m "$MAX_PAGES" --mobile --format json -o "$OUT/audit.json"
seomator audit "$SITE" --crawl -m "$MAX_PAGES" --mobile --format html -o "$OUT/audit.html"

echo "==> Raw signals the crawler does not surface directly"
curl -sS -D "$OUT/headers-home.txt" -o "$OUT/home.html" -L "$SITE/" || true
for p in robots.txt sitemap.xml sitemap_index.xml llms.txt; do
  curl -sS -o "$OUT/$p" -w "%{http_code} $p\n" -L "$SITE/$p" || true
done

# JSON-LD is often injected by JavaScript and is invisible to curl. Pull it from
# the rendered DOM instead.
if command -v node >/dev/null && [ -d /opt/pw-browsers ]; then
  node -e '
    const { chromium } = require("playwright");
    (async () => {
      const b = await chromium.launch({ args: ["--no-sandbox"] });
      const p = await b.newPage();
      await p.goto(process.argv[1], { waitUntil: "networkidle", timeout: 60000 });
      const ld = await p.$$eval(
        "script[type=\"application/ld+json\"]", n => n.map(x => x.textContent)
      );
      console.log(JSON.stringify(ld, null, 2));
      await b.close();
    })();
  ' "$SITE/" > "$OUT/jsonld-home.json" 2>/dev/null || echo "[]" > "$OUT/jsonld-home.json"
fi

echo
echo "Done. Raw output in $OUT"
echo "Next: seomator compare $HOST   (after the fixes ship)"
