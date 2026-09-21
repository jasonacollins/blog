# Jason Collins Blog

A Quarto-based blog covering behavioural economics, data science, and artificial intelligence.

## Quick Start

### Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) (version 1.8+)
- R (for posts with computational content)

### Development

```bash
# Preview the site locally (with live reload)
quarto preview

# Render the entire site
quarto render

# Render a single post
quarto render posts/post-name.qmd
```

## Project Structure

```
.
├── posts/              # Blog posts (.qmd files)
├── _site/              # Generated site (auto-generated)
├── _freeze/            # Cached computational results
├── _quarto.yml         # Site configuration
├── pdfs/               # PDF files
├── about.qmd           # About page
├── research.qmd        # Research page
└── subscribe.qmd       # Subscribe page
```

## Writing Posts

### Creating a New Post

Use the `new-post.sh` script to quickly create a new post:

```bash
# Create a new .md post
./new-post.sh my-new-article

# Create a new .qmd post (for R computations)
./new-post.sh my-new-article --qmd
```

This creates a post file with:
- Title in sentence case (e.g., "My new article")
- Current date/time in Sydney timezone
- `draft: true` and `images: [""]` fields
- Opens automatically in VS Code

### Manual Post Creation

Alternatively, create a new `.qmd` file manually in the `posts/` directory:

```yaml
---
title: "Your Post Title"
author: "Jason Collins"
date: 2025-01-24 09:00:00+10:00
draft: false
bibliography: references.bib  # Optional
toc: true                      # Optional
---

Your content here...
```

### Including R Code

Posts can include R code chunks:

````markdown
```{r chunk-name, message=FALSE, warning=FALSE}
library(tidyverse)
# Your analysis code
```
````

### Citations

Reference a bibliography file in the frontmatter and use pandoc citation syntax:

- In-text: `@author2024`
- Parenthetical: `[@author2024]`

## Configuration

Key settings in `_quarto.yml`:

- **Freeze execution**: Computational results are cached (only re-run when source changes)
- **Theme**: Cosmo with custom SCSS
- **Body width**: 600px
- **Citation style**: Custom APA without ampersands

## Publishing

### Legacy URLs

`redirects.json` is the permanent map of old paths to current, extensionless
paths. It covers matching root-level URLs for published posts and trailing-slash
URLs for top-level pages. Keep these mappings when editing or renaming posts, and update
their destinations when a post moves. Do not add `aliases` to post frontmatter.

The post-render script `scripts/build-redirects.ts` expands each map entry into
HTTP 301 rules with and without a trailing slash, then includes the manual rules
from `_redirects`. A source ending in `/` redirects only that exact path (used
for real top-level pages such as `/research/`). The build checks destinations,
redirect chains, conflicts and Cloudflare's rule limits. New posts do not need
legacy entries unless an older URL exists.

Review these legacy redirects around September 2027, with the intention of
removing them once the URL migration has settled. Before removal, check Search
Console and any available traffic data for continued use of the old URLs.

The rendered site is in `_site/`. Deploy this directory to your web host.

Note: The `_freeze/` directory contains cached results and should be committed to version control.
