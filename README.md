# Jason Collins Blog

A blog covering behavioural economics, data science, and artificial intelligence,
published at <https://blog.jcx.au>.

Posts are written in markdown in `posts/`. Pandoc (the copy bundled with Quarto)
turns each post into HTML, and Hugo builds the site around it. Cloudflare Pages
publishes whatever is pushed to `main`.

## Quick Start

### Prerequisites

- [Hugo](https://gohugo.io/installation/) (`brew install hugo`)
- [Quarto](https://quarto.org/docs/get-started/) (version 1.8+), for its bundled
  Pandoc and for posts with citations or R code
- Node, for the search index (`brew install node`)
- R with `rmarkdown`, `tidyverse` and `scales`, only for posts that run R code

### Write, preview, publish

```bash
# 1. Create a post (opens in VS Code)
./new-post.sh my-new-article

# 2. Preview it, drafts included; the browser reloads when you save
./hugo/preview.sh posts/my-new-article.md

# 3. When it is ready, set draft: false, then build
./hugo/build.sh

# 4. Commit the post and its rendered body, and push
git add posts hugo/content-generated hugo/static-generated
git commit -m "new post"
git push
```

Step 3 matters. Cloudflare cannot render posts itself; it publishes the rendered
bodies committed in `hugo/content-generated/`. A post pushed without running
`./hugo/build.sh` first will not appear, and an edit pushed without it will not
show.

### Previewing the post you are editing

`./hugo/preview.sh posts/post-name.md` opens that post at
`http://localhost:1313` and re-renders it each time you save (about a second for
an ordinary post). Run it without an argument to open the home page. Stop it
with **Ctrl+C** before starting another.

To preview the **currently open post in VS Code** without typing its path, save
the file, keep its editor tab active, and choose **Terminal → Run Task → Preview
current post (Hugo)**.

Search does not work in the preview; it is built by `./hugo/build.sh`.

## Project Structure

```
.
├── posts/              # Blog posts (.md, or .qmd for R code)
│   └── img/            # Post images
├── pdfs/               # PDF files
├── about.qmd           # Top-level pages: about, research, subscribe,
├── research.qmd        #   teaching, media, writing
├── _redirects          # Manual redirect rules
├── new-post.sh         # Create a post
└── hugo/               # The site build
    ├── hugo.toml           # Site settings
    ├── layouts/            # Page templates (navbar, home listing, post page)
    ├── assets/css/main.css # Styles
    ├── scripts/            # sync-posts.py renders post bodies
    ├── content-generated/  # Rendered post bodies (committed)
    ├── static-generated/   # Figures from R posts (committed)
    ├── preview.sh          # Live preview
    ├── build.sh            # Full build into hugo/public/
    └── public/             # Built site (not committed)
```

See [hugo/README.md](hugo/README.md) for how the build works.

## Writing Posts

### Creating a New Post

```bash
# Create a new .md post
./new-post.sh my-new-article

# Create a new .qmd post (for R computations)
./new-post.sh my-new-article --qmd
```

This creates a post file with:
- Title in sentence case (e.g., "My new article")
- Current date/time in Sydney timezone
- `draft: true`, `toc: false` and an empty `image` field
- Opens automatically in VS Code

### Front matter

```yaml
---
title: "Your Post Title"
author: "Jason Collins"
date: 2025-01-24 09:00:00+10:00
draft: false
image: img/your-image.png      # Optional: thumbnail on the home page and social cards
toc: true                      # Optional: "On this page" list beside the post
bibliography: references.bib   # Optional
comments: false                # Optional: turn off comments for this post
---
```

Posts with `draft: true` show in the preview but are left out of the published
site.

### Links, images, video and maths

- Link to another post by file name: `[text](other-post.md)`.
- Images go in `posts/img/` and are referenced as `![caption](img/name.png)`.
  They are resized automatically for the page.
- Video: `{{< video https://youtu.be/ID >}}` or `{{< youtube ID >}}`.
- Maths: `$x^2$` inline, `$$ ... $$` for display.

### Citations

Reference a bibliography file in the frontmatter and use pandoc citation syntax:

- In-text: `@author2024`
- Parenthetical: `[@author2024]`

Posts with citations take about six seconds to re-render on each save, because
they go through Quarto.

### Including R Code

Use a `.qmd` post with R code chunks:

````markdown
```{r chunk-name, message=FALSE, warning=FALSE}
library(tidyverse)
# Your analysis code
```
````

The R code runs when you preview or build after editing that post, and not
otherwise, so published figures and numbers stay as they are until you change
the post.

## Changing the site itself

- Navbar, footer and page layout: `hugo/layouts/`
- Styles: `hugo/assets/css/main.css`
- Site title, analytics and comments settings: `hugo/hugo.toml`
- Top-level pages: edit the `.qmd` files in the repo root

## Publishing

Cloudflare Pages runs `./hugo/build.sh` on every push to `main` and publishes
`hugo/public/`. Its settings are: build command `./hugo/build.sh`, output
directory `hugo/public`, environment variable `HUGO_VERSION` set to the local
Hugo version.

### Redirects

Redirects are generated on each build. Each published post gets `/name` and
`/name/` redirects to `/posts/name`, and top-level pages get trailing-slash
redirects such as `/research/` to `/research`. Renaming a post changes its
redirects on the next build; old file names are not kept, so update internal
links when renaming a post.

Manual rules, including feed and dated URL redirects, live in `_redirects` in
the repo root and are added to the generated list.

## The earlier Quarto site

The site was built entirely with Quarto until November 2026. `_quarto.yml`,
`index.qmd`, `_site/`, `preview-post.sh` and `scripts/` are left over from that
setup and no longer affect the published site. `_quarto.yml`, `_freeze/` and
`apa-no-ampersand.csl` are still used when a post is rendered through Quarto.
