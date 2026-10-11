#!/bin/bash
# Builds ../lynkk-reddit-leads.zip to share. Leaves out data, output and caches.
set -euo pipefail
cd "$(dirname "$0")/.."
SRC="$(pwd)"
OUT="$(cd .. && pwd)/lynkk-reddit-leads.zip"
TMP="$(mktemp -d)"
mkdir "$TMP/lynkk-reddit-leads"
rsync -a \
  --exclude .venv --exclude data --exclude output --exclude work --exclude drafts --exclude logs \
  --exclude __pycache__ --exclude .pytest_cache --exclude '*.egg-info' --exclude .DS_Store \
  "$SRC/" "$TMP/lynkk-reddit-leads/"
rm -f "$OUT"
(cd "$TMP" && zip -qr "$OUT" lynkk-reddit-leads)
rm -rf "$TMP"
echo "Wrote $OUT ($(du -h "$OUT" | cut -f1))"
