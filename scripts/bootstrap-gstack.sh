#!/usr/bin/env bash
# Build gstack browse binary and refresh workspace symlinks for Cursor/Codex discovery.
# Requires Bun (https://bun.sh/). Playwright Chromium downloads to the user cache (~/.cache/ms-playwright).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
GST="$ROOT/platforms/gstack"
if [ ! -f "$GST/setup" ]; then
  echo "gstack not found at platforms/gstack (expected vendored tree)." >&2
  exit 1
fi
mkdir -p "$ROOT/.agents/skills"
ln -sfn ../../platforms/gstack "$ROOT/.agents/skills/gstack"
shopt -s nullglob
for d in "$GST"/.agents/skills/gstack-*/; do
  base="$(basename "$d")"
  ln -sfn "../../platforms/gstack/.agents/skills/$base" "$ROOT/.agents/skills/$base"
done
shopt -u nullglob
(cd "$GST" && exec ./setup --host codex)
