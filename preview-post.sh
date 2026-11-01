#!/usr/bin/env bash
set -euo pipefail

usage() {
    echo "Usage: $0 posts/post-name.md [quarto preview options]"
    echo "Previews a .md or .qmd post with drafts visible and live reload enabled."
}

if [[ $# -eq 0 ]]; then
    usage >&2
    exit 1
fi
if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    usage
    exit 0
fi

post_file="$1"
shift

if [[ ! -f "$post_file" ]]; then
    echo "Error: post not found: $post_file" >&2
    exit 1
fi
case "$post_file" in
    *.md|*.qmd) ;;
    *) echo "Error: choose a .md or .qmd post." >&2; exit 1 ;;
esac

# Resolve the input before changing directory so paths are relative to the caller.
post_file="$(cd -- "$(dirname -- "$post_file")" && pwd)/$(basename -- "$post_file")"
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
case "$post_file" in
    "$project_dir"/posts/*) ;;
    *) echo "Error: choose a post inside $project_dir/posts/." >&2; exit 1 ;;
esac

cd "$project_dir"
exec quarto preview "$post_file" -M draft-mode:visible "$@"
