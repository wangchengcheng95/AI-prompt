#!/usr/bin/env bash
# Build gstack browse binary and refresh workspace symlinks.
# Writes only under this repository (no ~/.codex, ~/.gstack, or default Playwright cache).
# Requires Bun (https://bun.sh/). On Windows, Node.js is also required for Chromium (see upstream gstack README).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
GST="$ROOT/gstack"
BROWSE_BIN="$GST/browse/dist/browse"
export PLAYWRIGHT_BROWSERS_PATH="$GST/.pw-browsers"

if [ ! -d "$GST" ] || [ ! -f "$GST/package.json" ]; then
  echo "gstack not found at repo root gstack/ (expected vendored tree)." >&2
  exit 1
fi

if ! command -v bun >/dev/null 2>&1; then
  echo "Error: bun is required. Install: https://bun.sh/" >&2
  exit 1
fi

IS_WINDOWS=0
case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*|Windows_NT) IS_WINDOWS=1 ;;
esac

mkdir -p "$PLAYWRIGHT_BROWSERS_PATH"
mkdir -p "$ROOT/.agents/skills"
ln -sfn ../../gstack "$ROOT/.agents/skills/gstack"
shopt -s nullglob
for d in "$GST"/.agents/skills/gstack-*/; do
  base="$(basename "$d")"
  ln -sfn "../../gstack/.agents/skills/$base" "$ROOT/.agents/skills/$base"
done
shopt -u nullglob

ensure_playwright_browser() {
  if [ "$IS_WINDOWS" -eq 1 ]; then
    (
      cd "$GST"
      node -e "const { chromium } = require('playwright'); (async () => { const b = await chromium.launch(); await b.close(); })()" 2>/dev/null
    )
  else
    (
      cd "$GST"
      bun --eval 'import { chromium } from "playwright"; const browser = await chromium.launch(); await browser.close();'
    ) >/dev/null 2>&1
  fi
}

NEEDS_BUILD=0
if [ ! -x "$BROWSE_BIN" ]; then
  NEEDS_BUILD=1
elif [ -n "$(find "$GST/browse/src" -type f -newer "$BROWSE_BIN" -print -quit 2>/dev/null)" ]; then
  NEEDS_BUILD=1
elif [ "$GST/package.json" -nt "$BROWSE_BIN" ]; then
  NEEDS_BUILD=1
elif [ -f "$GST/bun.lock" ] && [ "$GST/bun.lock" -nt "$BROWSE_BIN" ]; then
  NEEDS_BUILD=1
fi

if [ "$NEEDS_BUILD" -eq 1 ]; then
  echo "Building gstack (bun install + build)..."
  (
    cd "$GST"
    bun install
    bun run build
  )
  if [ ! -f "$GST/browse/dist/.version" ]; then
    git -C "$GST" rev-parse HEAD > "$GST/browse/dist/.version" 2>/dev/null || true
  fi
fi

if [ ! -x "$BROWSE_BIN" ]; then
  echo "bootstrap-gstack failed: browse binary missing at $BROWSE_BIN" >&2
  exit 1
fi

if ! ensure_playwright_browser; then
  echo "Installing Playwright Chromium into $PLAYWRIGHT_BROWSERS_PATH ..."
  (
    cd "$GST"
    bunx playwright install chromium
  )
  if [ "$IS_WINDOWS" -eq 1 ]; then
    if ! command -v node >/dev/null 2>&1; then
      echo "bootstrap-gstack failed: Node.js is required on Windows for Playwright Chromium" >&2
      exit 1
    fi
    (
      cd "$GST"
      node -e "require('playwright')" 2>/dev/null || npm install --no-save playwright
    )
  fi
fi

if ! ensure_playwright_browser; then
  echo "bootstrap-gstack failed: Chromium could not be launched (check Bun/Node and Playwright install)" >&2
  exit 1
fi

echo "gstack bootstrap complete (repo-local). Browse: $BROWSE_BIN"
