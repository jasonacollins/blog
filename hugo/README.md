# Hugo prototype

An alternative build of the blog that leaves the Quarto setup untouched. Posts
are still written in `posts/` exactly as now. Pandoc still parses the markdown,
so posts read the same; Hugo replaces Quarto for everything around the post
body: page templates, the home listing, feed, sitemap, redirects and images.

## Use

Needs Hugo (`brew install hugo`) and the existing Quarto install.

```bash
./hugo/preview.sh                  # live preview with drafts; reloads on save
./hugo/preview.sh posts/name.md    # same, opening that post
./hugo/build.sh                    # build the site into hugo/public/
python3 hugo/scripts/compare-sites.py --list   # compare hugo/public/ with _site/
```

## How it works

1. `scripts/sync-posts.py` renders each post body to HTML in
   `content-generated/posts/`, keeping the post's front matter. Only posts
   whose source changed are redone.
   - Ordinary posts go through Quarto's bundled Pandoc (about 0.2 s each).
   - Posts using Quarto features (citations, image attributes, fenced divs,
     R chunks) are rendered with a single-post `quarto render` and the body
     taken from its HTML (about 6 s; longer when R code runs).
   - R code is re-run only when that post's source changes, so published
     figures and numbers stay as they are until you edit the post. Re-running
     needs R with `rmarkdown`, `tidyverse` and `scales`. It also refreshes that
     post's files in `_freeze/`.
2. Hugo builds the site (about half a second). `hugo.toml` reads images, PDFs,
   `_redirects` and the top-level pages (`research.qmd` and so on) in place
   from the repo root.

Maths is converted to MathML at build time and local images are resized to
WebP, so post pages load no JavaScript apart from analytics and comments.

## URLs

Unchanged. Files are written as `posts/name.html`, which Cloudflare Pages
serves as `/posts/name`. `_redirects` is generated with the same rules as
`scripts/build-redirects.ts`, plus the manual rules from the root `_redirects`.
Feed item links and GUIDs match the Quarto feed.

## Search

`build.sh` indexes the built posts with Pagefind (`npx pagefind`, so Node is
needed). The index is loaded only on `/search`, in small pieces as you type.
`/search?q=words` links straight to a result list. Search is not available in
`preview.sh`.

## Cloudflare Pages

Build command `./hugo/build.sh`, output directory `hugo/public`, and the
environment variable `HUGO_VERSION` set to the version in use locally
(`hugo version`). Quarto is not needed there: the post bodies in
`content-generated/` are committed, so commit them along with the post.

## Not done yet

- The About page shows its links as plain buttons, not Quarto's `about:`
  template.
- Images inside the 28 Quarto-rendered posts are served at original size
  unless they sit in `posts/img/` with no extra attributes.
