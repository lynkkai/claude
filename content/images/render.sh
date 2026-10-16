#!/usr/bin/env bash
# Renders each banner HTML in src/ to a PNG at its exact pixel size with headless Chromium.
# Chromium's headless window loses some height to browser UI, so each page is rendered
# taller and then cropped to the exact size with Pillow.
# Usage: bash content/images/render.sh
set -euo pipefail
cd "$(dirname "$0")"
CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"

render() {
  local name="$1" w="$2" h="$3"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --no-sandbox \
    --force-device-scale-factor=1 --window-size="${w},$((h + 200))" \
    --screenshot="$PWD/${name}.png" "file://$PWD/src/${name}.html" >/dev/null 2>&1
  python3 -c "from PIL import Image; im = Image.open('${name}.png'); im.crop((0, 0, ${w}, ${h})).save('${name}.png', optimize=True)"
  echo "rendered ${name}.png (${w}x${h})"
}

render blogger-banner 1200 630
render blogger-action-item-anatomy 1200 675
render hashnode-cover 1600 840
render hashnode-pipeline 1600 560
render medium-banner 1400 788
render medium-before-after 1400 760
render devto-cover 1000 420
render devto-notes-flow 1000 560
