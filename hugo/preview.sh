#!/bin/sh
# Live preview, drafts included. Saving a post re-renders it and reloads the browser.
#   ./hugo/preview.sh                 # open the home page
#   ./hugo/preview.sh posts/name.md   # open that post
# Stop with Ctrl+C.
set -e
cd "$(dirname "$0")/.."
python3 hugo/scripts/sync-posts.py
python3 hugo/scripts/sync-posts.py --watch &
watcher=$!
trap 'kill $watcher 2>/dev/null' EXIT INT TERM
url="http://localhost:1313/"
if [ -n "$1" ]; then
  name=$(basename "$1"); url="${url}posts/${name%.*}.html"
fi
(sleep 2; open "$url" 2>/dev/null || true) &
hugo server --source hugo --buildDrafts --port 1313
