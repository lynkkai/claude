#!/bin/bash
# Stops the daily run.
LABEL="ai.lynkk.reddit-leads"
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
rm -f "$HOME/Library/LaunchAgents/$LABEL.plist"
echo "Daily run removed."
