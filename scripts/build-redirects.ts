// Permanent legacy URL map, independent of post frontmatter.
// Quarto runs this after rendering; Cloudflare applies the resulting HTTP 301s.
const output = Deno.env.get("QUARTO_PROJECT_OUTPUT_DIR");
if (!output) throw new Error("Run this script as a Quarto post-render hook.");

const mapping: Record<string, string> = JSON.parse(await Deno.readTextFile("redirects.json"));
const rules = new Map<string, string>();
for (const [source, target] of Object.entries(mapping)) {
  if (!/^\/[\w./-]+$/.test(source) || !/^\/[\w/-]+$/.test(target) ||
      source.includes("..") || target.includes("..") || target.endsWith("/")) {
    throw new Error(`Invalid redirect: ${source} -> ${target}`);
  }
  if (!(await Deno.stat(`${output}${target}.html`)).isFile) {
    throw new Error(`Missing redirect destination: ${target}`);
  }
  for (const path of source.endsWith("/") ? [source] : [source, `${source}/`]) {
    if (path === target || (rules.has(path) && rules.get(path) !== target)) {
      throw new Error(`Conflicting redirect: ${path} -> ${target}`);
    }
    rules.set(path, target);
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
  `# Generated from redirects.json; edit the source map, not this file.\n${generated}\n\n${existing}`);
console.log(`Generated ${rules.size} permanent legacy redirects.`);
