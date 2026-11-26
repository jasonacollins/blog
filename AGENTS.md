# AGENTS.md

Technical guidance for AI agents working with this blog repository.

## Architecture in one paragraph

Posts are authored in `posts/` (`.md`, or `.qmd` when they run R). A Python
script renders each post body to HTML with Pandoc or Quarto and writes it to
`hugo/content-generated/posts/`. Hugo builds the site from those bodies plus
its own templates. Cloudflare Pages runs the Hugo build on every push to
`main`; it has no Quarto, so the generated bodies are committed.

The published site is built by Hugo. `_quarto.yml`, `index.qmd`, `_site/`,
`preview-post.sh` and `scripts/*.ts` belong to the earlier all-Quarto build and
do not affect what is published. Do not edit them to change the live site.

## Commands Reference

```bash
# Live preview with drafts (re-renders a post on save)
./hugo/preview.sh
./hugo/preview.sh posts/post-name.md

# Full build into hugo/public/: sync post bodies, run Hugo, index search
./hugo/build.sh

# Render changed post bodies only
python3 hugo/scripts/sync-posts.py
python3 hugo/scripts/sync-posts.py --force    # redo all; re-runs R code too

# Hugo alone (uses the bodies already generated)
hugo --source hugo --minify
```

## The publish rule

After changing anything in `posts/`, run `./hugo/build.sh` (or at least
`sync-posts.py`) and commit `hugo/content-generated/` and
`hugo/static-generated/` together with the post. A post committed without its
generated body does not appear on the site, and an edit does not show.

Pushing to `main` deploys to production. Do not push without the user's say-so.

## Post rendering (hugo/scripts/sync-posts.py)

Each post becomes `hugo/content-generated/posts/NAME.md`: selected front matter
plus the HTML body wrapped in an `html` shortcode. Two routes:

- **pandoc**: ordinary posts. `quarto pandoc -f markdown -t html --katex`.
  About 0.2 s each.
- **quarto**: posts with `bibliography:` front matter, R or raw code chunks,
  fenced divs (`:::`), image or heading attributes (`{width=...}`,
  `{#fig-...}`), or cross-references. Runs `quarto render` on that one post
  and lifts the `<main>` body from the result. About 6 s, longer with R.

Things to know:

- Each generated file stores `sync_hash`. A post is redone when its source,
  its route, or the script's `VERSION` changes.
- **R posts are the exception**: their hash covers the source only. R re-runs
  only when the post is edited (or with `--force`), so published figures and
  numbers do not change by accident. Do not bump them casually; re-running
  under newer R and package versions can alter output. Re-running also
  rewrites that post's files in `_freeze/`.
- Changing how bodies are post-processed (`fix_html`) needs a `VERSION` bump
  to take effect, which re-renders every non-R post, including the slow
  Quarto ones.
- Front matter passed through to Hugo: `title`, `author`, `date`, `draft`,
  `toc`, `image`, `comments`, `date-modified`, `lastmod`. Everything else is
  dropped.
- Post-processing: KaTeX spans become `{{< math >}}` shortcodes (MathML at
  build time), local `img/` images become `{{< img >}}` shortcodes (resized
  WebP), links to `other-post.md` become `/posts/other-post.html`, and Quarto
  `{{< video URL >}}` is rewritten to the form Hugo accepts.
- Deleting or renaming a post removes its stale generated file on the next
  sync.

## Hugo site (hugo/)

- `hugo.toml`: settings and module mounts. Images (`posts/img`), PDFs,
  `_redirects`, `logo.png` and the top-level pages (`about.qmd`,
  `research.qmd`, `subscribe.qmd`, `teaching.qmd`, `media.qmd`, `writing.qmd`)
  are mounted in place from the repo root; nothing is copied.
- `layouts/baseof.html`: head, navbar, footer. `layouts/page.html`: posts and
  top-level pages. `layouts/home.html`: paginated listing (50 per page).
  `layouts/search.html`: Pagefind search page.
- `layouts/home.rss.xml`, `layouts/home.redirects`, `layouts/sitemap.xml`:
  feed, Cloudflare `_redirects` and sitemap.
- `layouts/_shortcodes/`: `html`, `math`, `img`, `video`, `youtube`, `tweet`.
- `assets/css/main.css`: all styles, inlined into every page. Values were
  taken from the computed styles of the earlier Quarto (Cosmo) theme; when
  matching its look, measure rather than estimate.
- Top-level pages are parsed by Hugo's own markdown parser (goldmark), not
  Pandoc, so Pandoc-only syntax does not work in them.

### URLs

`uglyURLs = true` writes `posts/name.html`, which Cloudflare Pages serves as
`/posts/name`. Templates strip `.html` (and `index.html`) from links and
canonical URLs in production and keep it under `hugo server`, where clean URLs
are not served. Use the `url.html` partial for page links. Feed item links and
GUIDs deliberately keep the `.html` form so existing subscribers see no
duplicates. Do not add `aliases` to post front matter; redirects are generated
in `layouts/home.redirects`.

### Post front matter

```yaml
---
title: "Post Title"
author: "Jason Collins"
date: 2025-01-24 09:00:00+10:00
draft: false           # true: shown in preview, excluded from the build
image: img/name.png    # optional thumbnail and social image
toc: true              # optional side contents list
bibliography: references.bib
---
```

**Date format**: use `YYYY-MM-DD HH:MM:SS+10:00` with the timezone.
Future-dated posts are published (`buildFuture = true`), as they were under
Quarto.

Use `.md` by default; `.qmd` only when the post runs R.

## Common Operations

### Creating a New Post

1. `./new-post.sh post-name` (add `--qmd` for R).
2. Write; preview with `./hugo/preview.sh posts/post-name.md`.
3. Set `draft: false`, run `./hugo/build.sh`.
4. Commit `posts/`, `hugo/content-generated/` and `hugo/static-generated/`.

### Renaming a Post

1. Rename the file in `posts/`.
2. For an R post, rename `_freeze/posts/old-name/` to match.
3. Update internal links to the post.
4. Run `./hugo/build.sh`; the old generated body is removed and redirects are
   regenerated.

### Changing styles or templates

Edit under `hugo/layouts/` or `hugo/assets/css/main.css`, check with
`./hugo/preview.sh`, then run `./hugo/build.sh`. No post bodies change.

## Output Directories

- `hugo/content-generated/`, `hugo/static-generated/`: rendered post bodies
  and R figures. Committed. Do not edit by hand; they are overwritten.
- `hugo/public/`: built site. Gitignored.
- `hugo/resources/`: Hugo's image cache. Gitignored.
- `_freeze/`: Quarto's cached R results. Committed.
- `_site/`: output of the earlier Quarto build. Still committed, no longer
  published. `hugo/scripts/compare-sites.py` compares `hugo/public/` with it.

## Deployment

Cloudflare Pages project settings: build command `./hugo/build.sh`, output
directory `hugo/public`, `HUGO_VERSION` environment variable. On Cloudflare
`build.sh` skips the sync step (no Quarto) and runs Hugo and Pagefind
(`npx pagefind@1.6.0`).

## Troubleshooting

### Post not appearing or not updating on the live site

Its generated body was not committed. Run `./hugo/build.sh` and commit
`hugo/content-generated/`.

### Sync reports FAILED for a post

Quarto-route posts print Quarto's error. For R posts check that `rmarkdown`
and the post's packages are installed in R.

### Images not displaying

Image paths are relative to `posts/` (for example `img/name.png`). Check the
file exists and the extension matches.

### Citations not rendering

Ensure `bibliography: references.bib` is in the front matter, the `.bib` file
has the entries, and citation keys match.

### Search returns nothing

Search needs the Pagefind index from `./hugo/build.sh`; it is absent under
`hugo server`.
