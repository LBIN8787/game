#!/usr/bin/env sh
cd -- "$(dirname -- "$0")" || exit 1
if command -v python3 >/dev/null 2>&1; then
  exec python3 serve.py
fi
if command -v node >/dev/null 2>&1; then
  exec node scripts/serve.mjs
fi
echo "Install Python 3.9+ or Node.js 18+, then retry."
exit 1
