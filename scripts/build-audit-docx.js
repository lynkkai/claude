const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, BorderStyle,
} = require('docx');

const NAVY = '1F3864';
const GREY = '595959';

// ---------- helpers ----------
const rule = () => new Paragraph({
  spacing: { before: 60, after: 240 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, space: 1, color: 'BFBFBF' } },
  children: [new TextRun({ text: '' })],
});

const label = (text, body) => [
  new Paragraph({
    spacing: { before: 180, after: 40 },
    children: [new TextRun({ text, bold: true, color: NAVY, size: 21 })],
  }),
  ...(Array.isArray(body) ? body : [body]).map(t => new Paragraph({
    spacing: { after: 60, line: 276 },
    children: [new TextRun({ text: t, size: 21 })],
  })),
];

const bullets = items => items.map(t => new Paragraph({
  bullet: { level: 0 },
  spacing: { after: 40, line: 276 },
  children: [new TextRun({ text: t, size: 21 })],
}));

let n = 0;
const issue = ({ title, priority, issue, why, solution, solutionBullets }) => {
  n += 1;
  return [
    new Paragraph({
      heading: HeadingLevel.HEADING_2,
      spacing: { before: 320, after: 20 },
      children: [new TextRun({ text: `${n}. ${title}`, bold: true, color: NAVY, size: 26 })],
    }),
    new Paragraph({
      spacing: { after: 60 },
      children: [new TextRun({ text: `Priority: ${priority}`, italics: true, color: GREY, size: 19 })],
    }),
    ...label('Issue', issue),
    ...label('Why this needs fixing', why),
    ...label('Solution', solution),
    ...(solutionBullets ? bullets(solutionBullets) : []),
    rule(),
  ];
};

// ---------- content ----------
const ISSUES = [
  {
    title: 'Only twelve URLs have ever been cited, and the homepage carries most of them',
    priority: 'Critical',
    issue: 'Twelve URLs appear in the AI-surface report for the last three months, and the homepage alone takes 62% of the impressions. Growth itself is healthy: impressions per day went from 0.23 in July to 1.26 in August to 2.46 in September, and is still climbing.',
    why: 'The concentration is the problem, not the trend. Twelve cited URLs cannot cover a category with hundreds of commercial queries, and one page carrying 62% of the footprint is a single point of failure. Because growth is currently strong, the return on adding pages is higher now than it will look later.',
    solution: 'Treat page creation as the primary growth lever for the next two quarters, working through the gap list in issue 4. Before committing a content budget, run the crawl with the site graph enabled: if pages already exist but are thin, orphaned, noindexed or missing from the sitemap, the fix is completely different and much cheaper.',
    solutionBullets: [
      'Watch the fortnightly trend rather than reacting to it. The last two 14-day periods were flat at 34 each, but at this volume the expected swing from chance alone is about plus or minus 6, so that is not yet a plateau. One more fortnight will tell you.',
    ],
  },
  {
    title: 'Legal pages outrank the product pages in AI answers',
    priority: 'Critical',
    issue: 'The terms of service page is the fourth most-surfaced page on the site. Terms, privacy and refund together take 9.4% of Lynkk’s entire AI-surface footprint. The terms page alone beats the how-it-works page, the knowledge graph feature page, the action items feature page, and both use-case pages.',
    why: 'Legal pages are long, specific, declarative and structured, so an extractive model can lift facts from them. Marketing pages that lead with a headline and three benefit bullets cannot be quoted. Google is telling you, in data, which of your pages are quotable, and it is the boilerplate.',
    solution: 'Rewrite the feature and use-case pages to be answer-shaped rather than pitch-shaped. Do not noindex the legal pages: they are doing no harm and they demonstrate the format that works.',
    solutionBullets: [
      'Use specific, checkable claims. "Creates Jira tickets with the assignee and due date set from the transcript" is quotable. "Automates your follow-ups" is not.',
      'Add an FAQ block to every page, with questions phrased the way people ask them and answers that stand alone in two or three sentences.',
      'Add comparison tables. AI surfaces lift tables directly.',
      'Name the integrations, state the limits, and put a visible last-updated date on the page.',
    ],
  },
  {
    title: 'Lynkk appears in no listicle, roundup or tool directory',
    priority: 'Critical',
    issue: 'Nine searches across the category returned Zapier, Reclaim, Read.ai, Fireflies, Otter, Krisp, HappyScribe, MeetGeek, tl;dv, Sybill, JotMe, MeetMinutes, Tana, Rock, Hedy and Meetily. Lynkk appeared in none of them. The only result Lynkk earns is its own homepage, on direct brand queries.',
    why: 'In this category the head terms are owned by listicles, and AI Overviews cite listicles heavily because they are comparative and structured. Being absent from them means being invisible for every query that is not already a brand search, no matter how good the on-site work gets.',
    solution: 'Three tracks, fastest first.',
    solutionBullets: [
      'Directory submissions: Product Hunt, There’s An AI For That, Futurepedia, G2, Capterra. Mostly free, mostly same-week. The Product Hunt copy is already drafted in the repo.',
      'Outreach to the roundup authors with a specific angle rather than a generic pitch. In-person capture, per-region data residency and Hinglish support are things most listed tools genuinely cannot do.',
      'Publish Lynkk’s own comparison pages so the brand competes on those queries directly.',
    ],
  },
  {
    title: 'No evidence of the page types this category expects',
    priority: 'High, but verify the premise first',
    issue: 'Nothing resembling a pricing page, blog, about page, integration pages, security page, or any comparison or alternatives page appeared in 92 days of Search Console data or across nine searches. This is the weakest-evidence item in this document: the export lists only pages cited in AI answers, so any of these could exist and simply never have been quoted. Check the sitemap before acting.',
    why: 'If the pages are missing, this is the textbook failure mode for a SaaS site: thin feature pages, no comparison content, no commercial-intent landing pages. Pricing is the most common commercial query for any software brand and a frequent trigger for AI answers. If instead the pages exist and are never cited, the problem is narrower but still real: they are not good enough or not linked well enough to be surfaced, and the fix is to improve them rather than to write them.',
    solution: 'First confirm which case applies by checking the sitemap. Then, for whatever is genuinely missing, build in this order, highest commercial intent first.',
    solutionBullets: [
      'A pricing page. Blocked on the paid tier names, prices and free-tier limits.',
      'Comparison pages against Otter, Fireflies, Granola, Fathom and tl;dv, plus alternatives pages. Write them honestly, including where the competitor wins, because that is what makes them credible and quotable.',
      'A security or data residency page. Per-region model processing is a stronger answer than "we are in the EU", and right now nobody can find it.',
      'An about page naming the legal entity, founders, founding year and HQ.',
      'Integration pages, one each for Jira, Calendly, Cal.com, calendar, MCP and each supported CRM.',
      'Feature pages for the eight or more features that have none, and use-case pages for the three unserved segments.',
      'A blog or resource hub, internally linked to the product pages rather than stranded on a subdomain.',
    ],
  },
  {
    title: 'Lynkk does not own its own brand search results',
    priority: 'High',
    issue: 'A search for "Lynkk" returns LYNKK LTD on UK Companies House, a Lagos-based crypto and bill-payment brand of the same name, two musicians, an Instagram account and a Facebook page, alongside lynkk.ai. Separately, Google returned two different titles for the lynkk.ai homepage across different searches.',
    why: 'Two problems in one. Google has no strong entity for Lynkk the software company, so it cannot confidently separate the product from its namesakes, and brand searches leak to unrelated results. The title rewriting is a direct signal that Google does not think the declared title answers the query.',
    solution: 'Establish the entity and settle the title.',
    solutionBullets: [
      'Add Organization and SoftwareApplication JSON-LD to the homepage with name, url, logo, description, applicationCategory, and a sameAs array listing every owned profile: X, Instagram, Facebook, LinkedIn, Product Hunt, YouTube.',
      'Verify first that each account found actually belongs to Lynkk. Putting a namesake’s profile in sameAs makes the disambiguation worse, not better.',
      'Build the about page. Legal entity, founding year, HQ and founders are what Google uses to form an entity.',
      'Pick one homepage title and make it the one that survives rewriting.',
    ],
  },
  {
    title: 'India is the strongest market and is served by a single page',
    priority: 'High',
    issue: 'India is 35% of AI-surface impressions (37 of 105), more than seven times the United States (5). The Hinglish transcription page is the joint second-best page on the site, level with the meeting bot page. Independent searches confirm real competition for Hinglish and Hindi meeting notes, which means there is real demand.',
    why: 'This is validated product-market fit showing up in search data. Code-switched Hinglish transcription is genuinely hard and most global tools treat it as an edge case, so Lynkk has a page ranking in a defensible niche from a domain with almost no authority. One page is leaving most of that on the table.',
    solution: 'Build out the India and multilingual cluster from the Hinglish page.',
    solutionBullets: [
      'Pages for Hindi meeting notes, and for Tamil, Telugu and Kannada if those are supported.',
      'An explainer on code-switching and why English-only transcription drops detail.',
      'India pricing in rupees, and a page for the India data region.',
      'Blocked on: how many languages are supported, and which Indic languages specifically.',
      'If a language selector or locale URLs are ever added, get hreflang right the first time. Cross-locale canonicals and missing return tags suppress entire locale sets.',
    ],
  },
  {
    title: 'The two best pages have no supporting content around them',
    priority: 'High',
    issue: 'The Hinglish transcription page and the meeting bot page each earn 10 impressions, together 17% of the site total. Neither has a topical cluster, supporting content, or internal links from related pages.',
    why: 'These two pages are the proven demand signal on the site. Both sit in competitive niches where search demand is confirmed. A single page in a cluster-shaped market captures a fraction of what the cluster would.',
    solution: 'Build a cluster around each, and cross-link it with descriptive anchor text.',
    solutionBullets: [
      'Meeting bot: one page per supported platform (Zoom, Google Meet, Teams), plus bot versus bot-free capture, and how to record without a bot joining.',
      'Hinglish: per-language pages, the code-switching explainer, and India-specific content.',
      'Blocked on: which meeting platforms are actually supported.',
    ],
  },
  {
    title: 'The technical audit has not been run',
    priority: 'Critical, and first in sequence',
    issue: 'Outbound web access is blocked in the current environment, so nothing that requires touching the site was measured: Core Web Vitals, robots.txt, sitemap.xml, canonical tags, noindex directives, redirect chains, structured data, security headers, image alt text, broken links, accessibility, and whether the content exists without JavaScript.',
    why: 'A single indexation bug outweighs every content decision in this document. If a canonical tag points the wrong way, a page is noindexed, or the main content only appears after JavaScript runs, then the pages are invisible regardless of how well they are written. These checks are pending, not passing, and the absence of a finding here is not a clean bill of health.',
    solution: 'Allow lynkk.ai in the environment’s network settings, then run the audit script that is already in the repo. It runs 373 rules across 20 categories in roughly ten minutes. Work the output in this order.',
    solutionBullets: [
      'Indexation blockers first: robots.txt, sitemap accuracy, noindex, canonicals, redirect chains and loops, soft 404s, orphan pages and click depth.',
      'Rendering second: does the main content exist in the raw HTML or only after JavaScript. Check console errors and failed resource requests, because a script that throws never writes the canonical tag or structured data it was going to write, and static analysis cannot see that.',
      'Mobile parity third: content, title, canonical, structured data and links, desktop render against mobile render. Google indexes the mobile version.',
      'Performance fourth: LCP under 2.5s, CLS under 0.1, TTFB under 800ms. Take INP from field data, because no crawler can measure it.',
      'Then security headers, image alt text, internal linking, broken links, accessibility, HTML validity and social tags.',
    ],
  },
  {
    title: 'AI and generative search readiness is unverified',
    priority: 'High',
    issue: 'The only performance data available is the AI features report, which proves Google is already willing to cite lynkk.ai in AI answers, 105 times across 34 countries. What has not been checked: whether llms.txt exists, whether AI crawlers are allowed in robots.txt, and whether any structured data is present.',
    why: 'This is the one channel where a small site can beat a large one, because citation rewards being quotable rather than being authoritative. The channel is already live for Lynkk. It is also the channel most easily broken by accident: a default robots.txt rule can remove the site from ChatGPT search or Perplexity without anyone noticing.',
    solution: 'Verify and then invest.',
    solutionBullets: [
      'Publish llms.txt. Cheap, and this audience will look for it.',
      'Audit AI crawler rules for GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, CCBot and Bytespider. Note that blocking Google-Extended does not remove a site from AI Overviews, which run on regular Googlebot, but blocking OAI-SearchBot or PerplexityBot does remove it from those products. Decide deliberately rather than by default.',
      'Check for Organization, SoftwareApplication, FAQPage and BreadcrumbList structured data, and add Product or Offer once pricing exists.',
      'Never conclude "no schema found" from a plain page fetch. Both curl and fetch tools skip script tags, and JSON-LD is often injected by JavaScript. Use a real browser render or the Rich Results Test.',
      'Use semantic HTML: a real h1, plus article, section, table and definition list elements. Extraction depends on it.',
    ],
  },
  {
    title: 'The mobile and desktop split does not match the audience',
    priority: 'Medium',
    issue: 'Desktop is 68% of impressions, mobile 30%, tablet 2%, while India is the top country at 35%.',
    why: 'Two possible readings, needing different responses. The benign one is that a Mac desktop work tool naturally skews desktop. The one to rule out is that mobile rendering or content parity problems are suppressing mobile impressions, because India is one of the most mobile-first search markets in the world and 68% desktop alongside 35% India is odd enough to check.',
    solution: 'Run the crawl with the mobile flag. The mobile parity rules compare content, title, canonical, structured data and links between the desktop and mobile renders. Anything missing from the mobile render is missing from Google’s index, because that is the version it indexes.',
  },
  {
    title: 'The Search Console data on hand is incomplete',
    priority: 'Medium, and it blocks other work',
    issue: 'The export is the Generative AI Features subset, not total Search, and it carries the impressions metric only. There are no clicks, no click-through rate, no average position, and no query data at all.',
    why: 'Impressions without clicks cannot tell you whether AI surfaces are sending anyone. Without query data there is no keyword map, no way to check whether pages are matching the intent they target, and no way to detect two pages competing for the same term. Keyword work is guesswork until this is fixed.',
    solution: 'Re-export and widen the measurement base.',
    solutionBullets: [
      'Export Search Console again with no Generative AI filter, all four metrics, and the Queries tab included, for both 3 months and 16 months.',
      'Confirm Bing Webmaster Tools is set up. Bing feeds Copilot and ChatGPT search, and it is a separate index with separate coverage reporting.',
    ],
  },
  {
    title: 'Several fixes are blocked on unanswered product facts',
    priority: 'Critical, because it gates the rest',
    issue: 'The brand file carries a nine-item list of unconfirmed facts: pricing tiers, platform availability, supported meeting platforms, which CRMs, number of languages, available data regions, company legal name and founders, social links, and logo and screenshot assets.',
    why: 'These are not marketing niceties. Pricing blocks the pricing page. Supported platforms block the integration and meeting bot clusters. Languages and regions block the India cluster and the data residency page. Company details and social links block the entity and schema work. Logo files block the directory submissions. Most of this document is waiting on that list.',
    solution: 'Get all nine answered as one task. It is probably an afternoon of internal questions, and it unblocks the majority of the action plan.',
  },
];

// ---------- document ----------
const children = [
  new Paragraph({
    spacing: { after: 40 },
    children: [new TextRun({ text: 'Lynkk.ai', bold: true, color: NAVY, size: 52 })],
  }),
  new Paragraph({
    spacing: { after: 200 },
    children: [new TextRun({ text: 'SEO audit: issues, why they matter, and what to do', color: GREY, size: 26 })],
  }),
  new Paragraph({
    spacing: { after: 240 },
    children: [new TextRun({ text: '27 September 2026, revised 28 September 2026', italics: true, color: GREY, size: 20 })],
  }),
  new Paragraph({
    spacing: { after: 120, line: 276 },
    children: [new TextRun({
      text: 'Twelve issues, ordered so that the ones blocking everything else come first. '
        + 'Findings are drawn from a 92-day Google Search Console export, searches run on '
        + '27 September 2026, and the site architecture those sources reveal. '
        + 'Revised 28 September 2026 after re-checking every figure against the source data.',
      size: 21,
    })],
  }),
  new Paragraph({
    spacing: { after: 120, line: 276 },
    children: [new TextRun({
      text: 'One caveat worth reading before the rest. The automated crawl could not run, '
        + 'because outbound web access was blocked. Issue 8 lists what that leaves unmeasured, '
        + 'and robots.txt, sitemap.xml and llms.txt are among them. Those checks are pending, '
        + 'not passing, and nothing in this document makes a claim about those files.',
      size: 21, italics: true,
    })],
  }),
  new Paragraph({
    spacing: { after: 240, line: 276 },
    children: [new TextRun({
      text: 'Three limits on the evidence. The supporting searches were US-only, while India is '
        + '35% of impressions. The Search Console page list is headed "Top pages", so it is a '
        + 'ranked list and cannot prove a URL was never cited. And the export covers Google\u2019s AI '
        + 'surfaces only, so a page that ranks well in ordinary Search but has never been quoted '
        + 'in an AI answer does not appear in it at all.',
      size: 21, italics: true,
    })],
  }),
  rule(),
  ...ISSUES.flatMap(issue),
  new Paragraph({
    spacing: { before: 200 },
    children: [new TextRun({
      text: 'Detail, evidence and the phased action plan: audit/lynkk-seo-audit-2026-09-27.md',
      italics: true, color: GREY, size: 19,
    })],
  }),
];

const doc = new Document({
  creator: 'Lynkk marketing',
  title: 'Lynkk.ai SEO audit',
  description: 'Issues, why they need fixing, and solutions',
  styles: {
    default: {
      document: { run: { font: 'Calibri', size: 21 } },
    },
  },
  sections: [{
    properties: { page: { margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } } },
    children,
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync(process.argv[2], b);
  console.log('wrote', process.argv[2], b.length, 'bytes');
});
