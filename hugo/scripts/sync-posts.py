#!/usr/bin/env python3
"""Render post bodies for Hugo.

Each post in posts/ becomes hugo/content-generated/posts/NAME.md: the original
front matter plus the body as HTML. Hugo then adds the page around it. The
markdown is parsed by Pandoc, as it is under Quarto, so posts read the same.

Two routes:

  pandoc   Ordinary posts. The body is rendered with Quarto's bundled Pandoc
           (about 0.2 seconds a post).
  quarto   Posts using Quarto features: citations, image attributes, fenced
           divs, raw blocks, R chunks. The post is rendered with Quarto on the
           spot and the body lifted from its HTML (about 6 seconds, longer if
           R code runs). R needs the rmarkdown package and whatever the post
           loads.

Each generated file records a hash of its inputs, so only changed posts are
redone. For posts with R the hash covers the post source alone: their code is
re-run only when the post itself is edited, never because this script changed,
so published figures and numbers do not shift by accident.

  python3 hugo/scripts/sync-posts.py            # bring everything up to date
  python3 hugo/scripts/sync-posts.py --watch    # keep doing so as posts are saved
"""
import argparse
import hashlib
import html
import re
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

VERSION = "6"
ROOT = Path(__file__).resolve().parents[2]
POSTS = ROOT / "posts"
OUT = ROOT / "hugo" / "content-generated" / "posts"
STATIC = ROOT / "hugo" / "static-generated" / "posts"

# Front matter passed through to Hugo; everything else is Quarto's business.
KEEP_KEYS = {"title", "author", "date", "draft", "toc", "image", "comments", "date-modified", "lastmod"}

VIDEO = re.compile(r"\{\{<\s*video\s+(\S+?)((?:\s+[\w-]+=(?:\"[^\"]*\"|\S+?))*)\s*>\}\}")
SHORTCODE = re.compile(r"\{\{<.*?>\}\}")
R_CHUNK = re.compile(r"^```\{r", re.M)
QUARTO_ONLY = re.compile(
    r"^```\{|^:::|\]\([^)\n]*\)\{|\]\{[.#]|\{#(fig|tbl)-|@(fig|tbl)-|^#+ .*\{[.#-]", re.M)
IMG_ATTRS = {"src", "alt", "class", "style", "title"}


def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    return (m.group(1), text[m.end():]) if m else ("", text)


def front_matter(raw, extra):
    """Keep the front matter keys Hugo uses, verbatim, and add bookkeeping."""
    out, keep = [], False
    for line in raw.split("\n"):
        key = re.match(r"^([A-Za-z_-]+):", line)
        if key:
            keep = key.group(1) in KEEP_KEYS
        if keep:
            out.append(line)
    out += [f'{k}: "{v}"' for k, v in extra.items()]
    return "---\n" + "\n".join(out) + "\n---\n\n"


def route_for(raw_fm, body):
    if re.search(r"^bibliography:", raw_fm, re.M) or QUARTO_ONLY.search(body):
        return "quarto"
    return "pandoc"


def hugo_video(text):
    """Quarto's {{< video URL >}} in the form Hugo's shortcode parser accepts."""
    return VIDEO.sub(lambda m: '{{< video src="%s"%s >}}' % (m.group(1).strip('"'), m.group(2)), text)


def table_of_contents(content):
    """Contents list for rendered HTML, from its h2/h3 headings."""
    items = []
    for m in re.finditer(r"<h([23])([^>]*)>(.*?)</h\1>", content, re.S):
        ident = re.search(r"(?:data-anchor-id|id)=\"([^\"]+)\"", m.group(2))
        if ident:
            items.append((int(m.group(1)), ident.group(1), re.sub(r"<[^>]+>", "", m.group(3)).strip()))
    if not items:
        return ""
    out, level = ['<div class="toc" data-pagefind-ignore><ul>'], 2
    for depth, ident, label in items:
        if depth != level:
            out.append("<ul>" if depth > level else "</ul>")
        level = depth
        out.append(f'<li><a href="#{ident}">{label}</a></li>')
    out.append("</ul>" * (level - 1) + "</div>\n")
    return "\n".join(out)


def fix_html(content):
    """Adjust rendered HTML for its new home: links, maths, images."""
    content = content.replace("{{<", "{{&lt;").replace("{{%", "{{&#37;")

    def math(m):
        tex = html.unescape(m.group(2)).strip()
        for opening, closing in ((r"\(", r"\)"), (r"\[", r"\]")):
            if tex.startswith(opening) and tex.endswith(closing):
                tex = tex[2:-2]
        return "{{< math %s>}}%s{{< /math >}}" % ("display " if m.group(1) == "display" else "", tex)
    # KaTeX spans become build-time maths via a Hugo shortcode: no script needed.
    content = re.sub(r"<span class=\"math (inline|display)\">(.*?)</span>", math, content, flags=re.S)

    def image(m):
        attrs = dict(re.findall(r"([\w:-]+)=\"([^\"]*)\"", m.group(1)))
        src = attrs.get("src", "")
        if (not re.fullmatch(r"(\./)?img/[^?#]+\.(png|jpe?g)", src, re.I) or set(attrs) - IMG_ATTRS
                or re.search(r"[\\{}]", "".join(attrs.values()))):
            return m.group(0)
        return "{{< img %s >}}" % " ".join(f'{k}="{v}"' for k, v in attrs.items())
    # Local images are resized by Hugo.
    content = re.sub(r"<img\b([^>]*?)/?>", image, content)

    # Links between pages, as Quarto resolves them. They name the real .html file so
    # they work in local preview; the html shortcode drops the extension for production.
    content = re.sub(r"href=\"(?:\./|/posts/)?([\w-]+)\.(?:html|md|qmd)(#[^\"]*)?\"",
                     lambda m: 'href="/posts/%s.html%s"' % (m.group(1), m.group(2) or ""), content)
    content = re.sub(r"href=\"\.\./index\.(?:html|md|qmd)\"", 'href="/"', content)
    content = re.sub(r"href=\"\.\./([\w-]+)\.(?:html|md|qmd)\"", r'href="/\1.html"', content)
    return content.strip() + "\n"


def render_pandoc(body):
    """Render the body with Pandoc, exactly as Quarto would parse it."""
    codes = []

    def protect(m):
        codes.append(m.group(0))
        return f"QSHORTCODE{len(codes) - 1}Q"
    protected = SHORTCODE.sub(protect, hugo_video(body))
    run = subprocess.run(["quarto", "pandoc", "-f", "markdown", "-t", "html", "--katex", "--wrap=none"],
                         input=protected, capture_output=True, text=True)
    if run.returncode:
        raise RuntimeError(run.stderr[-800:])
    out = re.sub(r"<p>(QSHORTCODE\d+Q)</p>", r"\1", fix_html(run.stdout))
    return re.sub(r"QSHORTCODE(\d+)Q", lambda m: codes[int(m.group(1))], out)


def render_quarto(path):
    """Render the post with Quarto and lift the article body out of the page."""
    with tempfile.TemporaryDirectory() as tmp:
        run = subprocess.run(["quarto", "render", str(path.relative_to(ROOT)), "--to", "html",
                              "--output-dir", tmp], cwd=ROOT, capture_output=True, text=True)
        page_file = Path(tmp) / "posts" / (path.stem + ".html")
        if run.returncode or not page_file.exists():
            raise RuntimeError(run.stderr[-800:])
        page = page_file.read_text()
        files = Path(tmp) / "posts" / (path.stem + "_files")
        if files.is_dir():
            shutil.copytree(files, STATIC / files.name, dirs_exist_ok=True)
    m = re.search(r"<main[^>]*id=\"quarto-document-content\"[^>]*>(.*?)</main>", page, re.S)
    if not m:
        raise RuntimeError(f"no <main> in the rendered page for {path.name}")
    content = re.sub(r"<header id=\"title-block-header\".*?</header>", "", m.group(1), count=1, flags=re.S)
    content = re.sub(r"<button[^>]*code-copy-button.*?</button>", "", content, flags=re.S)
    content = re.sub(r"<a [^>]*id=\"quarto-back-to-top\".*?</a>", "", content, flags=re.S)
    return fix_html(content)


def digest_for(text, route, body):
    """Hash of what a generated body depends on."""
    if route == "quarto" and R_CHUNK.search(body):
        return hashlib.sha1((text + "r-post").encode()).hexdigest()[:12]
    return hashlib.sha1((text + route + VERSION).encode()).hexdigest()[:12]


def sync(force=False, quiet=False):
    """One pass over posts/. Returns (route counts, failures)."""
    OUT.mkdir(parents=True, exist_ok=True)
    STATIC.mkdir(parents=True, exist_ok=True)
    wanted, counts, failed, jobs = set(), {}, [], []
    for path in sorted(list(POSTS.glob("*.md")) + list(POSTS.glob("*.qmd"))):
        text = path.read_text()
        raw_fm, body = split_front_matter(text)
        route = route_for(raw_fm, body)
        counts[route] = counts.get(route, 0) + 1
        target = OUT / (path.stem + ".md")
        wanted.add(target)
        digest = digest_for(text, route, body)
        if not force and target.exists() and f'sync_hash: "{digest}"' in target.read_text()[:2000]:
            continue
        jobs.append((path, raw_fm, body, route, target, digest))

    def run(job):
        path, raw_fm, body, route, target, digest = job
        try:
            out = render_pandoc(body) if route == "pandoc" else render_quarto(path)
        except Exception as err:  # keep going; report at the end
            failed.append((path.name, str(err)))
            return
        toc = table_of_contents(out) if re.search(r"^toc:\s*true", raw_fm, re.M) else ""
        extra = {"sync_source": f"posts/{path.name}", "sync_route": route, "sync_hash": digest}
        # The html shortcode keeps the rendered body away from Hugo's markdown parser.
        target.write_text(front_matter(raw_fm, extra) + "{{< html >}}\n" + toc + out + "{{< /html >}}\n")
        print(f"{route:7} {path.name}", flush=True)

    # Quarto project renders must not overlap; Pandoc runs are independent.
    with ThreadPoolExecutor(8) as pool:
        list(pool.map(run, [j for j in jobs if j[3] == "pandoc"]))
    for job in jobs:
        if job[3] == "quarto":
            run(job)
    for stale in set(OUT.glob("*.md")) - wanted:
        stale.unlink()
        print(f"removed {stale.name}", flush=True)
    for name, err in failed:
        print(f"FAILED {name}: {err}", file=sys.stderr, flush=True)
    if not quiet:
        print("routes:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return counts, failed


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--force", action="store_true", help="redo every post, re-running R code too")
    ap.add_argument("--watch", action="store_true", help="keep running; redo posts as they are saved")
    args = ap.parse_args()
    _, failed = sync(args.force)
    if not args.watch:
        sys.exit(1 if failed else 0)
    seen = None
    while True:
        stamp = max((p.stat().st_mtime for p in POSTS.glob("*.*md")), default=0), len(list(POSTS.glob("*.*md")))
        if seen is not None and stamp != seen:
            sync(quiet=True)
        seen = stamp
        time.sleep(0.5)


if __name__ == "__main__":
    main()
