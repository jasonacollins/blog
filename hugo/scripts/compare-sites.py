#!/usr/bin/env python3
"""Compare the Hugo build with the existing Quarto build, post by post.

For every post it extracts the article body from both sites and compares the
visible text, link targets, images and a count of structural elements. Also
compares the set of pages, the redirect rules and the feed GUIDs.

  python3 hugo/scripts/compare-sites.py            # summary
  python3 hugo/scripts/compare-sites.py -v NAME    # show the differences for one post
"""
import argparse
import difflib
import re
import sys
import unicodedata
from urllib.parse import unquote
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OLD = ROOT / "_site"
NEW = ROOT / "hugo" / "public"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
COUNTED = ["p", "blockquote", "li", "h2", "h3", "h4", "table", "tr", "iframe", "em", "strong", "sup", "pre", "figcaption"]


class Body(HTMLParser):
    """Collects text, links, images and tag counts inside one container element."""

    def __init__(self, is_root, is_skipped):
        super().__init__(convert_charrefs=True)
        self.is_root, self.is_skipped = is_root, is_skipped
        self.stack = []          # (tag, flag) for open elements inside the root
        self.inside = False
        self.skip_depth = 0
        self.text, self.links, self.images = [], [], []
        self.counts = dict.fromkeys(COUNTED + ["math"], 0)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if not self.inside:
            if self.is_root(tag, a):
                self.inside = True
                self.stack = [tag]
            return
        skipping = self.skip_depth > 0
        if not skipping and (tag in ("script", "style", "math", "button") or self.is_skipped(tag, a)):
            if tag == "math" or "math" in (a.get("class") or "").split():
                self.counts["math"] += 1
            if tag not in VOID:
                self.skip_depth = 1
                self.stack.append(tag)
            return
        if tag not in VOID:
            self.stack.append(tag)
            if skipping:
                self.skip_depth += 1
        if skipping:
            return
        if tag in self.counts:
            self.counts[tag] += 1
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img" and a.get("src"):
            self.images.append(a["src"])
        if tag in ("p", "li", "br", "div", "h2", "h3", "h4", "blockquote", "tr", "figcaption"):
            self.text.append(" ")

    def handle_endtag(self, tag):
        if not self.inside or tag in VOID or tag not in self.stack:
            return
        while self.stack:
            closed = self.stack.pop()
            if self.skip_depth:
                self.skip_depth -= 1
            if closed == tag:
                break
        if not self.stack:
            self.inside = False
        elif tag in ("p", "li", "div", "blockquote", "td", "th"):
            self.text.append(" ")

    def handle_data(self, data):
        if self.inside and not self.skip_depth:
            self.text.append(data)


def classes(a):
    return (a.get("class") or "").split()


def old_root(tag, a):
    return tag == "main" and a.get("id") == "quarto-document-content"


def old_skip(tag, a):
    c = classes(a)
    return (a.get("id") in ("title-block-header", "quarto-back-to-top")
            or "math" in c or "footnote-back" in c or "anchorjs-link" in c
            or (tag == "summary") or (tag == "h2" and "anchored" in c and "quarto-appendix-heading" in c)
            or tag == "h2" and "quarto-appendix-heading" in c)


def new_root(tag, a):
    return tag == "div" and "body" in classes(a)


def new_skip(tag, a):
    c = classes(a)
    return "toc" in c or a.get("id") == "quarto-back-to-top" or "anchorjs-link" in c or "footnote-backref" in c or "footnote-back" in c or "math" in c or tag == "summary" \
        or (tag == "h2" and "quarto-appendix-heading" in c)


def norm_text(parts):
    t = unicodedata.normalize("NFKC", "".join(parts))
    t = t.replace("­", "").replace("↩︎", "").replace("↩", "")
    return re.sub(r"\s+", " ", t).strip()


def norm_link(href):
    href = unquote(href.strip())
    if href.startswith(("http://", "https://", "mailto:", "//")):
        return href.rstrip("/")
    if href.startswith("#"):
        return "#"          # heading and footnote ids are generated differently
    href = re.sub(r"#.*$", "", href)
    href = re.sub(r"^(\./)+", "", href)
    if href.startswith("../"):
        href = "/" + href[3:]
    elif not href.startswith("/"):
        href = "/posts/" + href
    href = re.sub(r"\.html$", "", href)
    return "/" if href == "/index" else href


def norm_image(src):
    if src.startswith(("http://", "https://", "//", "data:")):
        return src
    name = src.rsplit("/", 1)[-1]
    name = re.sub(r"_hu_[0-9a-f]+\.webp$", "", name)     # Hugo's resized copies
    return re.sub(r"\.(png|jpe?g|gif|webp)$", "", name, flags=re.I)


def extract(path, root, skip):
    parser = Body(root, skip)
    parser.feed(path.read_text())
    return {
        "text": norm_text(parser.text),
        "links": sorted(norm_link(h) for h in parser.links),
        "images": sorted(norm_image(s) for s in parser.images),
        "counts": parser.counts,
    }


def compare(name, verbose=False):
    old = extract(OLD / "posts" / name, old_root, old_skip)
    new = extract(NEW / "posts" / name, new_root, new_skip)
    issues = []
    if old["text"] != new["text"]:
        a, b = old["text"].split(), new["text"].split()
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        words = sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal")
        issues.append(("text", f"{words} words"))
    # Quarto's lightbox and Hugo's image hook both wrap images in a link to the file.
    image_links = {l for l in old["links"] + new["links"] if re.search(r"\.(png|jpe?g|gif|webp)(\?.*)?$", l, re.I)}
    old_links = [l for l in old["links"] if l not in image_links]
    new_links = [l for l in new["links"] if l not in image_links]
    if old_links != new_links:
        issues.append(("links", f"-{len(set(old_links) - set(new_links))} +{len(set(new_links) - set(old_links))}"))
    if sorted(set(old["images"])) != sorted(set(new["images"])):
        issues.append(("images", f"{len(old['images'])} vs {len(new['images'])}"))
    changed = {k: (old["counts"][k], new["counts"][k]) for k in old["counts"] if old["counts"][k] != new["counts"][k]}
    if changed:
        issues.append(("structure", ", ".join(f"{k} {a}→{b}" for k, (a, b) in changed.items())))
    if verbose:
        if old["text"] != new["text"]:
            a, b = old["text"].split(), new["text"].split()
            sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op != "equal":
                    print(f"  text: …{' '.join(a[max(0, i1 - 4):i1])} [{' '.join(a[i1:i2])[:160]}] → [{' '.join(b[j1:j2])[:160]}]")
        print("  links only in Quarto:", sorted(set(old_links) - set(new_links)))
        print("  links only in Hugo:  ", sorted(set(new_links) - set(old_links)))
        print("  images only in Quarto:", sorted(set(old["images"]) - set(new["images"])))
        print("  images only in Hugo:  ", sorted(set(new["images"]) - set(old["images"])))
        print("  structure:", changed)
    return issues


def has_body(path):
    return "<body" in path.read_text()


def lines(path):
    return {l.strip() for l in path.read_text().splitlines() if l.strip() and not l.startswith("#")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", metavar="NAME", help="show details for one post (file name without .html)")
    ap.add_argument("--list", action="store_true", help="list every post with a difference")
    args = ap.parse_args()
    if args.verbose:
        compare(args.verbose + ".html", verbose=True)
        return

    old_posts = {p.name for p in (OLD / "posts").glob("*.html") if has_body(p)}
    new_posts = {p.name for p in (NEW / "posts").glob("*.html")}
    print(f"Posts: Quarto {len(old_posts)}, Hugo {len(new_posts)}")
    print("  only in Quarto:", sorted(old_posts - new_posts) or "none")
    print("  only in Hugo:  ", sorted(new_posts - old_posts) or "none")

    tally, rows = {}, []
    for name in sorted(old_posts & new_posts):
        issues = compare(name)
        for kind, _ in issues:
            tally[kind] = tally.get(kind, 0) + 1
        if issues:
            rows.append((name, issues))
    same = len(old_posts & new_posts) - len(rows)
    print(f"\nIdentical text, links, images and structure: {same} of {len(old_posts & new_posts)}")
    for kind in ("text", "links", "images", "structure"):
        print(f"  posts with {kind} differences: {tally.get(kind, 0)}")
    if args.list:
        for name, issues in rows:
            print(f"{name[:-5]}: " + "; ".join(f"{k} ({d})" for k, d in issues))

    old_r, new_r = lines(OLD / "_redirects"), lines(NEW / "_redirects")
    print(f"\nRedirect rules: Quarto {len(old_r)}, Hugo {len(new_r)}")
    print("  only in Quarto:", sorted(old_r - new_r)[:10] or "none")
    print("  only in Hugo:  ", sorted(new_r - old_r)[:10] or "none")

    guid = re.compile(r"<guid>([^<]+)</guid>")
    old_g, new_g = guid.findall((OLD / "index.xml").read_text()), guid.findall((NEW / "index.xml").read_text())
    print(f"\nFeed GUIDs: {'identical, same order' if old_g == new_g else 'DIFFERENT'} ({len(old_g)} vs {len(new_g)})")
    if old_g != new_g:
        print("  only in Quarto:", sorted(set(old_g) - set(new_g)))
        print("  only in Hugo:  ", sorted(set(new_g) - set(old_g)))
    sys.exit(0)


if __name__ == "__main__":
    main()
