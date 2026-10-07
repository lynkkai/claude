#!/bin/bash
# One-time setup: checks uv and Claude Code, installs the Python environment.
set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v uv >/dev/null 2>&1; then
  if command -v brew >/dev/null 2>&1; then
    echo "Installing uv with Homebrew..."
    brew install uv
  else
    echo "uv is not installed. Install it with:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "then open a new terminal and run scripts/setup.sh again."
    exit 1
  fi
fi

echo "Installing the Python environment (uv downloads Python 3.12 if needed)..."
uv sync --quiet
mkdir -p data output work drafts logs

if command -v claude >/dev/null 2>&1; then
  echo "Claude Code found: $(command -v claude)"
  echo "Open Claude Code in this folder once (run: claude) and accept the"
  echo "\"trust this folder\" prompt, so the folder's settings apply."
else
  echo "Claude Code was not found. Install it from https://claude.com/claude-code"
  echo "The search and export still work without it; reviewing and drafting need it."
fi

echo
echo "Ready. Next:"
echo "  claude            then type /leads   (run it by hand)"
echo "  scripts/install-daily.sh 08:00      (run it every morning)"
