// Builds Word (.docx) versions of the Medium and DEV drafts, with images embedded.
//
//   node content/publish/make-docx.js
//
// medium-post.docx is made to be pasted into Medium: open it in Word or Google Docs, select all,
// copy, and paste into a new Medium story. It only uses what Medium's editor accepts (title,
// subtitle, one heading level, bold, italic, links, lists, images): code blocks become plain
// lines and placeholder links become valid URLs.
// devto-post.docx is a review copy of the DEV article (DEV itself takes the Markdown file).
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ExternalHyperlink, ImageRun, HeadingLevel,
  AlignmentType, LevelFormat, ShadingType, BorderStyle,
} = require("docx");

const CONTENT = path.resolve(__dirname, "..");
const IMAGES = path.join(CONTENT, "images");
const PAGE_WIDTH_PX = 624; // 6.5" text width on US Letter with 1" margins, at 96 dpi

// ---------- helpers ----------

function pngSize(file) {
  const buf = fs.readFileSync(file);
  return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20), data: buf };
}

function image(name) {
  const { width, height, data } = pngSize(path.join(IMAGES, name));
  const w = Math.min(PAGE_WIDTH_PX, width);
  return new Paragraph({
    spacing: { before: 120, after: 240 },
    children: [new ImageRun({ type: "png", data, transformation: { width: w, height: Math.round((height * w) / width) } })],
  });
}

// Inline Markdown: **bold**, *italic*, `code`, [text](url)
function inline(text, base = {}) {
  const out = [];
  const re = /(\*\*(.+?)\*\*)|(\*(.+?)\*)|(`([^`]+)`)|(\[([^\]]+)\]\(([^)]+)\))/g;
  let last = 0;
  let m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    if (m[2] !== undefined) out.push(...inline(m[2], { ...base, bold: true }));
    else if (m[4] !== undefined) out.push(...inline(m[4], { ...base, italics: true }));
    else if (m[6] !== undefined) out.push(new TextRun({ text: m[6], font: "Courier New", ...base }));
    else if (m[8] !== undefined)
      out.push(new ExternalHyperlink({ link: m[9], children: [new TextRun({ text: m[8], style: "Hyperlink", ...base })] }));
    last = re.lastIndex;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}

// Parse a small Markdown subset into blocks.
function parse(md) {
  const lines = md.split("\n");
  const blocks = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }
    if (line.startsWith("```")) {
      const code = [];
      i++;
      while (i < lines.length && !lines[i].startsWith("```")) code.push(lines[i++]);
      i++;
      blocks.push({ type: "code", lines: code });
      continue;
    }
    const img = line.match(/^!\[([^\]]*)\]\(([^)]+)\)\s*$/);
    if (img) { blocks.push({ type: "image", alt: img[1], src: img[2] }); i++; continue; }
    if (/^#{1,3} /.test(line)) {
      const level = line.match(/^#+/)[0].length;
      blocks.push({ type: "heading", level, text: line.replace(/^#+ /, "") });
      i++;
      continue;
    }
    if (/^---\s*$/.test(line)) { blocks.push({ type: "hr" }); i++; continue; }
    if (/^(- |\d+\. )/.test(line)) {
      const ordered = /^\d+\. /.test(line);
      const items = [];
      while (i < lines.length && /^(- |\d+\. |\s{2,}\S)/.test(lines[i]) && lines[i].trim()) {
        if (/^(- |\d+\. )/.test(lines[i])) items.push(lines[i].replace(/^(- |\d+\. )/, ""));
        else items[items.length - 1] += " " + lines[i].trim();
        i++;
      }
      blocks.push({ type: "list", ordered, items });
      continue;
    }
    const para = [];
    while (i < lines.length && lines[i].trim() && !/^(```|#{1,3} |!\[|- |\d+\. |---\s*$)/.test(lines[i])) para.push(lines[i++].trim());
    blocks.push({ type: "para", text: para.join(" ") });
  }
  return blocks;
}

function stripHeader(md) {
  return md.replace(/^---\n[\s\S]*?\n---\n/, "").replace(/<!--[\s\S]*?-->\s*/, "").replace(/^# .*\n+/, "").trim();
}

function headerField(md, name) {
  const m = md.match(new RegExp(`^${name}[^:]*:\\s*(.+)$`, "m"));
  return m ? m[1].trim() : "";
}

let listInstance = 0;

function render(blocks, { mediumSafe }) {
  const out = [];
  for (const b of blocks) {
    if (b.type === "heading") {
      out.push(new Paragraph({ heading: b.level <= 2 ? HeadingLevel.HEADING_1 : HeadingLevel.HEADING_2, children: inline(b.text) }));
    } else if (b.type === "para") {
      out.push(new Paragraph({ spacing: { after: 160 }, children: inline(b.text) }));
    } else if (b.type === "list") {
      listInstance++;
      for (const item of b.items)
        out.push(new Paragraph({
          numbering: { reference: b.ordered ? "numbers" : "bullets", level: 0, instance: listInstance },
          spacing: { after: 80 },
          children: inline(item),
        }));
    } else if (b.type === "hr") {
      out.push(new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "CCCCCC", space: 1 } }, spacing: { after: 200 }, children: [] }));
    } else if (b.type === "image") {
      const name = path.basename(b.src).replace(/^IMAGE_URL_/, "").replace(/\.png$/, "") + ".png";
      out.push(image(name));
    } else if (b.type === "code") {
      if (mediumSafe) {
        // Medium splits pasted code blocks apart, so use plain lines; ALL CAPS lines in bold.
        const groups = [[]];
        for (const l of b.lines) l.trim() ? groups[groups.length - 1].push(l.trimEnd()) : groups.push([]);
        for (const g of groups.filter((x) => x.length))
          g.forEach((l, k) => out.push(new Paragraph({
            spacing: { after: k === g.length - 1 ? 160 : 0 },
            children: [new TextRun({ text: l, bold: l === l.toUpperCase() && /[A-Z]{4}/.test(l) })],
          })));
      } else {
        b.lines.forEach((l, k) => out.push(new Paragraph({
          shading: { type: ShadingType.CLEAR, color: "auto", fill: "F5F5F4" },
          spacing: { after: k === b.lines.length - 1 ? 200 : 0 },
          children: [new TextRun({ text: l || " ", font: "Courier New", size: 18 })],
        })));
      }
    }
  }
  return out;
}

function doc(children) {
  return new Document({
    styles: {
      default: { document: { run: { font: "Georgia", size: 23 } } },
      paragraphStyles: [
        { id: "Title", name: "Title", basedOn: "Normal", run: { font: "Arial", size: 48, bold: true }, paragraph: { spacing: { after: 120 } } },
        { id: "Subtitle", name: "Subtitle", basedOn: "Normal", run: { font: "Arial", size: 28, color: "6C6C6A" }, paragraph: { spacing: { after: 240 } } },
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: "Arial", size: 32, bold: true }, paragraph: { spacing: { before: 360, after: 120 }, outlineLevel: 0 } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: "Arial", size: 26, bold: true }, paragraph: { spacing: { before: 240, after: 100 }, outlineLevel: 1 } },
      ],
    },
    numbering: {
      config: [
        { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
        { reference: "numbers", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      ],
    },
    sections: [{
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
      children,
    }],
  });
}

async function write(file, children) {
  fs.writeFileSync(path.join(__dirname, file), await Packer.toBuffer(doc(children)));
  console.log("wrote", path.join(__dirname, file));
}

// ---------- Medium ----------
(async () => {
  const mediumSrc = fs.readFileSync(path.join(CONTENT, "medium-how-to-take-meeting-notes.md"), "utf8");
  let mediumBody = stripHeader(mediumSrc)
    .replace(/BLOGGER_POST_URL/g, "https://replace-with-blogger-post-url.example")
    .replace(/HASHNODE_POST_URL/g, "https://replace-with-hashnode-post-url.example");
  const mediumBlocks = parse(mediumBody);
  // Medium's AI label goes right under the banner (first image).
  const firstImage = mediumBlocks.findIndex((b) => b.type === "image");
  mediumBlocks.splice(firstImage + 1, 0, {
    type: "para",
    text: "*This article was drafted with AI assistance, then reviewed, edited and fact-checked by the Lynkk team.*",
  });
  await write("medium-post.docx", [
    new Paragraph({ style: "Title", children: [new TextRun(headerField(mediumSrc, "Title \\(H1\\)"))] }),
    new Paragraph({ style: "Subtitle", children: [new TextRun(headerField(mediumSrc, "Subtitle"))] }),
    ...render(mediumBlocks, { mediumSafe: true }),
  ]);

  // ---------- DEV ----------
  const devSrc = fs.readFileSync(path.join(CONTENT, "devto-meeting-notes-templates-dev-teams.md"), "utf8");
  const devTitle = devSrc.match(/^title:\s*"(.+)"$/m)[1];
  const devDesc = devSrc.match(/^description:\s*"(.+)"$/m)[1];
  await write("devto-post.docx", [
    new Paragraph({ style: "Title", children: [new TextRun(devTitle)] }),
    new Paragraph({ style: "Subtitle", children: [new TextRun(devDesc)] }),
    image("devto-cover.png"),
    ...render(parse(stripHeader(devSrc)), { mediumSafe: false }),
  ]);
})();
