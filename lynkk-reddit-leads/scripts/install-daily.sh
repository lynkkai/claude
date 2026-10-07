#!/bin/bash
# Runs scripts/daily.sh every day at the given time (default 08:00) with launchd.
# If the Mac is asleep at that time, it runs when the Mac wakes up.
set -euo pipefail
cd "$(dirname "$0")/.."
DIR="$(pwd)"
TIME="${1:-08:00}"
HOUR=$((10#${TIME%%:*}))
MIN=$((10#${TIME##*:}))
LABEL="ai.lynkk.reddit-leads"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
mkdir -p "$HOME/Library/LaunchAgents" logs
chmod +x scripts/*.sh

cat > "$PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key>
  <array><string>/bin/bash</string><string>$DIR/scripts/daily.sh</string></array>
  <key>WorkingDirectory</key><string>$DIR</string>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>$HOUR</integer><key>Minute</key><integer>$MIN</integer></dict>
  <key>StandardOutPath</key><string>$DIR/logs/daily.log</string>
  <key>StandardErrorPath</key><string>$DIR/logs/daily.log</string>
</dict>
</plist>
PLIST

launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
printf "Scheduled every day at %02d:%02d.\n" "$HOUR" "$MIN"
echo "Output: $DIR/output   Log: $DIR/logs/daily.log"
echo "Run it now to test: launchctl kickstart gui/$(id -u)/$LABEL"
echo "Remove it: scripts/uninstall-daily.sh"
