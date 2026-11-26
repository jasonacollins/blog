#!/bin/sh
# Build the site into hugo/public/: render changed posts, run Hugo, index for search.
set -e
cd "$(dirname "$0")/.."
python3 hugo/scripts/sync-posts.py
hugo --source hugo --minify --cleanDestinationDir
if command -v pagefind >/dev/null 2>&1; then
  pagefind --site hugo/public --glob "posts/*.html"
elif command -v npx >/dev/null 2>&1; then
  npx -y pagefind --site hugo/public --glob "posts/*.html"
else
  echo "pagefind not found: the search page will be empty. See hugo/README.md." >&2
fi
