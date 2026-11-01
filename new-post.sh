#!/bin/bash

# Script to create a new blog post with template

# Check if slug is provided
if [ -z "$1" ]; then
    echo "Usage: ./new-post.sh post-slug [--qmd]"
    echo "Example: ./new-post.sh my-new-article"
    echo "         ./new-post.sh my-new-article --qmd"
    exit 1
fi

SLUG="$1"
EXTENSION="md"

# Check for --qmd flag
if [ "$2" = "--qmd" ]; then
    EXTENSION="qmd"
fi

POST_FILE="posts/${SLUG}.${EXTENSION}"

# Check if file already exists
if [ -f "$POST_FILE" ]; then
    echo "Error: Post file already exists: $POST_FILE"
    exit 1
fi

# Convert slug to sentence case title
# Replace hyphens with spaces and capitalize first letter
TITLE=$(echo "$SLUG" | sed 's/-/ /g' | awk '{print toupper(substr($0,1,1)) substr($0,2)}')

# Generate current date in Sydney timezone
# Format: YYYY-MM-DD HH:MM:SS+10:00
CURRENT_DATE=$(TZ="Australia/Sydney" date '+%Y-%m-%d %H:%M:%S+10:00')

# Create the post file with template
cat > "$POST_FILE" << EOF
---
title: "$TITLE"
author: "Jason Collins"
date: $CURRENT_DATE
draft: true
toc: false
image: ""
---

EOF

echo "Created new post: $POST_FILE"
echo "Title: $TITLE"
echo "Date: $CURRENT_DATE"

# Make script executable if it isn't already
chmod +x "$0" 2>/dev/null

# Open in editor
if [ -n "$EDITOR" ]; then
    $EDITOR "$POST_FILE"
else
    # Try VS Code on macOS, fallback to code command, then nano
    open -a "Visual Studio Code" "$POST_FILE" 2>/dev/null || code "$POST_FILE" 2>/dev/null || nano "$POST_FILE"
fi
