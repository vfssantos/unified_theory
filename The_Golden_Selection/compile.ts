#!/usr/bin/env -S deno run --allow-read --allow-write

/**
 * Compile The Golden Selection into a single markdown file
 * 
 * Usage:
 *   deno run --allow-read --allow-write compile.ts
 *   deno run --allow-read --allow-write compile.ts --output=output.md
 *   deno run --allow-read --allow-write compile.ts --include-appendices
 */

import { join, basename, dirname } from "jsr:@std/path";

// Part ordering using Roman numerals
const PART_ORDER = [
  "Part_0_Axiom",
  "Part_I_Selection",
  "Part_II_Realization",
  "Part_III_Quasicrystal",
  "Part_IV_Spacetime",
  "Part_V_Quantum",
  "Part_VI_Gravity",
  "Part_VII_Gauge",
  "Part_VIII_Matter",
  "Part_IX_Masses",
  "Part_X_Mixing",
  "Part_XI_Nuclear",
  "Part_XII_Cosmology",
  // "Part_XIII_Assessment",
  // "Part_XIV_Ontology",
];

// Roman numeral conversion for display
const ROMAN_DISPLAY: Record<string, string> = {
  "Part_0_Axiom": "Part 0: The Axiom",
  "Part_I_Selection": "Part I: Selection",
  "Part_II_Realization": "Part II: Realization",
  "Part_III_Quasicrystal": "Part III: Quasicrystal",
  "Part_IV_Spacetime": "Part IV: Spacetime",
  "Part_V_Quantum": "Part V: Quantum",
  "Part_VI_Gravity": "Part VI: Gravity",
  "Part_VII_Gauge": "Part VII: Gauge",
  "Part_VIII_Matter": "Part VIII: Matter",
  "Part_IX_Masses": "Part IX: Masses",
  "Part_X_Mixing": "Part X: Mixing",
  "Part_XI_Nuclear": "Part XI: Nuclear Physics",
  "Part_XII_Cosmology": "Part XII: Cosmology",
  "Part_XIII_Assessment": "Part XIII: Assessment",
  "Part_XIV_Ontology": "Part XIV: Ontology",
};

interface CompileOptions {
  outputFile: string;
  includeAppendices: boolean;
  includeOverview: boolean;
  addPageBreaks: boolean;
}

function parseArgs(): CompileOptions {
  const args = Deno.args;
  let outputFile = "The_Golden_Selection_Complete.md";
  let includeAppendices = false;
  let includeOverview = false;
  let addPageBreaks = true;

  for (const arg of args) {
    if (arg.startsWith("--output=")) {
      outputFile = arg.slice(9);
    } else if (arg === "--include-appendices") {
      includeAppendices = true;
    } else if (arg === "--include-overview") {
      includeOverview = true;
    } else if (arg === "--no-page-breaks") {
      addPageBreaks = false;
    } else if (arg === "--help" || arg === "-h") {
      console.log(`
The Golden Selection - Document Compiler

Usage:
  deno run --allow-read --allow-write compile.ts [options]

Options:
  --output=FILE           Output file name (default: The_Golden_Selection_Complete.md)
  --include-appendices    Include appendix markdown files
  --no-overview          Skip the 00_Overview section
  --no-page-breaks       Don't add page break markers between parts
  --help, -h             Show this help message
`);
      Deno.exit(0);
    }
  }

  return { outputFile, includeAppendices, includeOverview, addPageBreaks };
}

async function getMarkdownFiles(dir: string): Promise<string[]> {
  const files: string[] = [];
  
  try {
    for await (const entry of Deno.readDir(dir)) {
      if (entry.isFile && entry.name.endsWith(".md")) {
        files.push(join(dir, entry.name));
      }
    }
  } catch {
    // Directory doesn't exist
    return [];
  }

  // Sort by filename (00_, 01_, 02_, etc.)
  return files.sort((a, b) => basename(a).localeCompare(basename(b)));
}

async function readFileContent(path: string): Promise<string> {
  try {
    return await Deno.readTextFile(path);
  } catch {
    console.warn(`Warning: Could not read ${path}`);
    return "";
  }
}

function generateHeader(): string {
  const date = new Date().toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  return `# The Golden Selection

**A Theory of Physical Selection from Mathematical Necessity**

---

*Compiled: ${date}*

---

`;
}

function generateTableOfContents(parts: string[]): string {
  let toc = "## Table of Contents\n\n";
  
  for (const part of parts) {
    const displayName = ROMAN_DISPLAY[part] || part.replace(/_/g, " ");
    const anchor = displayName.toLowerCase().replace(/[^a-z0-9]+/g, "-");
    toc += `- [${displayName}](#${anchor})\n`;
  }
  
  toc += "\n---\n\n";
  return toc;
}

function generatePartSeparator(partName: string, addPageBreak: boolean): string {
  const displayName = ROMAN_DISPLAY[partName] || partName.replace(/_/g, " ");
  let separator = "";
  
  if (addPageBreak) {
    separator += "\n\n<div style=\"page-break-after: always;\"></div>\n\n";
  }
  
  separator += `\n\n---\n\n# ${displayName}\n\n---\n\n`;
  return separator;
}

async function compile(options: CompileOptions): Promise<void> {
  const baseDir = dirname(new URL(import.meta.url).pathname);
  let output = generateHeader();
  
  // Collect existing parts
  const existingParts: string[] = [];
  for (const part of PART_ORDER) {
    const partDir = join(baseDir, part);
    try {
      const stat = await Deno.stat(partDir);
      if (stat.isDirectory) {
        existingParts.push(part);
      }
    } catch {
      // Part doesn't exist
    }
  }

  // Generate ToC
  output += generateTableOfContents(existingParts);

  // Include 00_Overview if requested
  if (options.includeOverview) {
    const overviewDir = join(baseDir, "00_Overview");
    const overviewFiles = await getMarkdownFiles(overviewDir);
    
    if (overviewFiles.length > 0) {
      output += "\n\n---\n\n# Overview\n\n---\n\n";
      
      for (const file of overviewFiles) {
        const content = await readFileContent(file);
        if (content) {
          output += content + "\n\n";
        }
      }
    }
  }

  // Process each part
  for (const part of existingParts) {
    const partDir = join(baseDir, part);
    const files = await getMarkdownFiles(partDir);
    
    if (files.length === 0) continue;
    
    output += generatePartSeparator(part, options.addPageBreaks);
    
    for (const file of files) {
      const content = await readFileContent(file);
      if (content) {
        // Add file marker as HTML comment for reference
        const fileName = basename(file);
        output += `<!-- Source: ${part}/${fileName} -->\n\n`;
        output += content + "\n\n";
      }
    }
  }

  // Include appendices if requested
  if (options.includeAppendices) {
    const appendicesDir = join(baseDir, "Appendices");
    
    output += "\n\n<div style=\"page-break-after: always;\"></div>\n\n";
    output += "\n\n---\n\n# Appendices\n\n---\n\n";
    
    // Only include research reports and verifications (not delegations)
    const appendixDirs = ["C_verifications"];
    
    for (const subDir of appendixDirs) {
      const fullPath = join(appendicesDir, subDir);
      const files = await getMarkdownFiles(fullPath);
      
      if (files.length > 0) {
        const dirName = subDir.replace(/_/g, " ").replace(/^\w/, c => c.toUpperCase());
        output += `\n## ${dirName}\n\n`;
        
        for (const file of files) {
          const content = await readFileContent(file);
          if (content) {
            output += `### ${basename(file, ".md")}\n\n`;
            output += content + "\n\n";
          }
        }
      }
    }
  }

  // Write output
  const outputPath = join(baseDir, options.outputFile);
  await Deno.writeTextFile(outputPath, output);
  
  // Statistics
  const lineCount = output.split("\n").length;
  const wordCount = output.split(/\s+/).length;
  const charCount = output.length;
  
  console.log(`
✅ Compilation complete!

📄 Output: ${options.outputFile}
📊 Statistics:
   - Lines:      ${lineCount.toLocaleString()}
   - Words:      ${wordCount.toLocaleString()}
   - Characters: ${charCount.toLocaleString()}
   - Parts:      ${existingParts.length}
`);
}

// Run
const options = parseArgs();
await compile(options);

