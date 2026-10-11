#!/bin/bash
# The daily run: fetch from Reddit, let Claude Code review, export.
# Scheduled by scripts/install-daily.sh; safe to run by hand too.
# Arguments go to the fetch step, e.g. scripts/daily.sh --quick
set -uo pipefail
cd "$(dirname "$0")/.."
export PATH="$HOME/.local/bin:$HOME/.claude/local:/opt/homebrew/bin:/usr/local/bin:$PATH"
mkdir -p logs

notify() { osascript -e "display notification \"$1\" with title \"Reddit leads\"" >/dev/null 2>&1 || true; }

echo "=== $(date '+%Y-%m-%d %H:%M') daily run ==="
uv run leads fetch "$@" || { notify "Fetching from Reddit failed. See logs/daily.log."; exit 1; }

if command -v claude >/dev/null 2>&1; then
  # The same instructions as the /review command, without its header.
  prompt="$(awk 'BEGIN{h=0} /^---$/{h++; next} h>=2' .claude/commands/review.md)"
  # A watchdog stops a stuck review after 40 minutes. Reviewed batches are
  # already saved; the next run (or /review) carries on from there.
  claude -p "$prompt" --allowedTools "Bash(uv run leads:*)" "Read" "Edit(./work/**)" &
  pid=$!
  ( sleep 2400; kill "$pid" 2>/dev/null && echo "Review took over 40 minutes; stopped it." \
      && sleep 15 && kill -9 "$pid" 2>/dev/null ) &
  watchdog=$!
  wait "$pid" || echo "Claude Code review did not finish; unreviewed items use rule scores."
  kill "$watchdog" 2>/dev/null || true
else
  echo "Claude Code not found; exporting with rule scores only."
fi

uv run leads export
summary="$(uv run leads status | grep -i 'exportable' || true)"
notify "Today's CSV is ready in output/. ${summary}"
echo "=== done $(date '+%H:%M') ==="
