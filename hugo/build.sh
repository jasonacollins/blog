#!/bin/sh
# Build the site into hugo/public/: render changed posts, run Hugo, index for search.
# On a machine without Quarto (for example Cloudflare Pages) the post bodies
# already committed in hugo/content-generated/ are used as they are.
set -e
cd "$(dirname "$0")/.."
if command -v quarto >/dev/null 2>&1; then
  python3 hugo/scripts/sync-posts.py
else
  echo "Quarto not found: using the committed post bodies."
fi
hugo --source hugo --minify --cleanDestinationDir
if command -v pagefind >/dev/null 2>&1; then
  pagefind --site hugo/public --glob "posts/*.html"
elif command -v npx >/dev/null 2>&1; then
  npx -y pagefind@1.6.0 --site hugo/public --glob "posts/*.html"
else
  echo "pagefind not found: the search page will be empty. See hugo/README.md." >&2
fi
