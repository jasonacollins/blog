// Generate redirects from the current render, independent of post frontmatter.
// Quarto runs this after rendering; Cloudflare applies the resulting HTTP 301s.
// Only full builds contain the complete list of current pages.
if (Deno.env.get("QUARTO_PROJECT_RENDER_ALL") !== "1") Deno.exit(0);

const output = Deno.env.get("QUARTO_PROJECT_OUTPUT_DIR");
if (!output) throw new Error("Run this script as a Quarto post-render hook.");

const outputListFile = Deno.env.get("QUARTO_USE_FILE_FOR_PROJECT_OUTPUT_FILES");
const outputList = outputListFile
  ? await Deno.readTextFile(outputListFile)
  : Deno.env.get("QUARTO_PROJECT_OUTPUT_FILES");
if (outputList === undefined) throw new Error("Quarto did not provide the rendered file list.");

const directory = `${await Deno.realPath(output)}/`;
const pages = new Set<string>();
for (const file of outputList.split(/\r?\n/).filter(file => file.endsWith(".html"))) {
  const path = await Deno.realPath(file);
  if (!path.startsWith(directory)) throw new Error(`Rendered file outside output directory: ${file}`);
  // Unpublished drafts are rendered as empty HTML shells without a body.
  if (!/<body(?:\s|>)/i.test(await Deno.readTextFile(path))) continue;
  pages.add(`/${path.slice(directory.length, -5)}`);
}

const rules = new Map<string, string>();
function addRedirect(source: string, target: string): void {
  if (!/^\/[\w./-]+$/.test(source) || !/^\/[\w/-]+$/.test(target) ||
      source.includes("..") || target.includes("..") || target.endsWith("/")) {
    throw new Error(`Invalid redirect: ${source} -> ${target}`);
  }
  for (const path of source.endsWith("/") ? [source] : [source, `${source}/`]) {
    if (path === target || (rules.has(path) && rules.get(path) !== target)) {
      throw new Error(`Conflicting redirect: ${path} -> ${target}`);
    }
    rules.set(path, target);
  }
}
for (const target of pages) {
  if (target.startsWith("/posts/")) {
    const source = target.slice("/posts".length);
    // A real page at the root takes precedence over a post with the same name.
    if (!pages.has(source)) addRedirect(source, target);
  } else if (target.lastIndexOf("/") === 0 && target !== "/index" && target !== "/404") {
    addRedirect(`${target}/`, target);
  }
}
for (const target of rules.values()) {
  if (rules.has(target)) throw new Error(`Redirect chain or loop through ${target}`);
}

const existing = await Deno.readTextFile("_redirects");
const manual = existing.split(/\r?\n/).filter(line => line.trim() && !line.trim().startsWith("#"));
let staticCount = rules.size;
let dynamicCount = 0;
for (const line of manual) {
  const [source] = line.trim().split(/\s+/);
  if (rules.has(source)) throw new Error(`Duplicate manual redirect: ${source}`);
  if (/[:*]/.test(source)) dynamicCount++; else staticCount++;
}
if (staticCount > 2000 || dynamicCount > 100) {
  throw new Error(`Cloudflare redirect limits exceeded: ${staticCount} static, ${dynamicCount} dynamic`);
}
const generated = [...rules].sort(([a], [b]) => a.localeCompare(b))
  .map(([source, target]) => `${source} ${target} 301`).join("\n");
await Deno.writeTextFile(`${output}/_redirects`,
  `# Generated from current rendered pages; manual rules are in the source _redirects file.\n${generated}\n\n${existing}`);
console.log(`Generated ${rules.size} redirects from current rendered pages.`);
