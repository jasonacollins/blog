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
     R chunks) take their body from Quarto's HTML. Without R this is a
     single-post `quarto render` (about 6 s). With R, the body comes from the
     page already in `_site/`, so run `quarto render` first when such a post
     changes.
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

## Not done yet

- Search: the page at `/search` expects a Pagefind index, which `build.sh`
  creates if `pagefind` or `npx` is installed. This has not been run.
- The About page's Quarto `about:` template (links and layout) is not
  reproduced; the page shows its text only.
- Images inside the 28 Quarto-rendered posts are served at original size
  unless they sit in `posts/img/` with no extra attributes.
- Syntax colouring for R code blocks.
- Deployment. `hugo/public/` is the folder to publish.
