# Lynkk.ai Technical Audit

Nov 3, 2026

## Summary

Lynkk.ai has excellent SEO fundamentals, but mobile performance is poor: mobile LCP is 4.7s, driven by a single-region origin with no CDN and unoptimized hero images. Markup and content structure need almost no work; delivery infrastructure and image weight do.

**Scope:** the public marketing site only (115 sitemap URLs). The logged-in app behind /sign-in was not tested.

**Method:** full crawl of all sitemap URLs, Lighthouse lab runs (mobile and desktop), a real mobile browser pass (Pixel 7 emulation) for LCP element and console errors, an axe-core WCAG 2.2 AA scan on four key pages, header and DNS inspection, structured data validation, and an outbound link check. Every finding was re-run a second time to confirm it.

| Lab metric | Mobile | Desktop |
| --- | --- | --- |
| Largest Contentful Paint | **4.7 s** (poor) | 0.84 s |
| Time to Interactive | **10.1 s** | 1.6 s |
| Speed Index | 8.8 s | 3.3 s |
| Total Blocking Time | 267 ms | 259 ms |
| Cumulative Layout Shift | 0 | 0 |
| First Contentful Paint | 2.0 s | 0.52 s |

The homepage transfers 1.8 MB over 66 requests on mobile.

## What is already right

These are stronger than most SaaS marketing sites and should be kept as they are.

- **Crawl health:** 115 of 115 URLs return 200, with zero redirect hops, zero broken internal links and zero orphan pages.
- **Metadata:** zero duplicate titles or meta descriptions. All titles are within 60 characters. Every page has exactly one H1, a correct self-referencing canonical, and JSON-LD.
- **Canonicalization:** www redirects to the apex (301), http to https (308), and trailing slashes are stripped (308).
- **Indexing controls:** /sign-in and /sign-up are noindex, follow. /share/ is disallowed in robots.txt and returns 404 with noindex.
- **Security headers:** HSTS with preload, X-Frame-Options DENY, nosniff, Referrer-Policy, and a Permissions-Policy that allows only microphone=(self).
- **Layout stability:** CLS is 0 on mobile and desktop. No horizontal scroll at mobile width. No console errors on the pages tested.
- **Caching of build assets:** hashed JS and CSS are served with max-age 1 year, immutable.
- **Image optimizer:** where next/image is used, srcset, sizes and AVIF negotiation all work (a 128 KB JPEG is served as a 21 KB AVIF).
- **llms.txt:** thorough, accurate and well structured, a real advantage for AI search that most competitors lack.

## Priority findings

P1 and P4 together cause most of the slow mobile LCP; fix those first.

### P1: Single-region origin, no CDN

lynkk.ai has one A record, 20.219.12.35, an Azure VM in Pune, India (AS8075), served directly by Caddy. There is no CDN and no IPv6 (AAAA) record. Measured TTFB was 0.72 to 1.06 s, and Lighthouse flags 528 to 638 ms of server response time.

Most target keywords are US-centric (Otter, Fireflies and Gong comparisons, "best ai note takers"), so most visitors cross the globe to reach one server.

**Fix:** put Cloudflare or Azure Front Door in front of the origin, or move hosting to Vercel.

### P2: ISR cache mostly serving STALE

x-nextjs-stale-time is 300 seconds. The homepage returned HIT, but /pricing, /blog, /compare/otter, /features/dictation and /security all returned x-nextjs-cache: STALE, so visitors trigger background regeneration.

**Fix:** raise revalidate on marketing pages to hours or days, and revalidate on demand at deploy.

### P3: 1.08 MB homepage HTML, 63% inline RSC payload

The homepage is 93 KB gzipped but 1,078 KB uncompressed. Of that, 683 KB is inline \_\_next\_f flight data: static content such as testimonials, FAQ entries and feature arrays is serialized twice, once as HTML and once as flight data. This drives the 267 ms TBT and the 10.1 s mobile TTI.

**Fix:** keep static copy inside server components and pass less data across the server and client boundary.

### P4: About 1.4 MB of images bypass the optimizer, including the LCP image

In a real mobile browser, the LCP element on the homepage is the plate-dusk.jpg background (3.9 s) and on /pricing it is plate-sky.jpg (3.3 s). These plates are CSS background-image, so the browser finds them late, and they are served as full-size JPEG even when AVIF is requested.

| File | Size | Pixels | Used as |
| --- | --- | --- | --- |
| /landing/grid/plate-ember.jpg | 438 KB | 1400 x 1400 | CSS background |
| /landing/grid/plate-mesh.jpg | 342 KB | 1200 x 1200 | CSS background |
| /landing/grid/logos/customers/hc.png | 325 KB | 512 x 512 | raw img (peer logos are 8 to 38 KB) |
| /landing/grid/plate-meadow.jpg | 159 KB |  | CSS background |
| /landing/grid/plate-dusk.jpg | 71 KB |  | CSS background (homepage LCP) |
| /landing/grid/plate-sky.jpg | 65 KB |  | CSS background (/pricing LCP) |

**Fix:** convert the plates and hc.png to AVIF or WebP. For the first-screen plate, either preload it with fetchpriority="high" or render it with next/image and priority.

### P5: 48 of 49 homepage images have empty alt

Only the speaker photo has real alt text. The platform logos (Zoom, Google Meet, Teams, WhatsApp, FaceTime) and customer logos carry meaning and should be described.

### P6: Every image is lazy-loaded, none prioritized

All 49 homepage images use loading="lazy", including above-the-fold ones, and the page has no fetchpriority hint or image preload.

**Fix:** remove lazy loading above the fold and mark the hero image as priority.

## Checked and fine

These looked like issues in automated checks but are correct, so no action is needed.

- **The w=3840 image request** on the homepage is only the srcset fallback; the image has correct srcset and sizes, and AVIF is served.
- **target="\_blank" links** to F6S use rel="noreferrer", which implies noopener.
- **Empty heading anchor links** on blog posts are aria-hidden with tabindex=-1.
- **The 1 x 1 px "Skip to content" link** is a correct visually hidden skip link that appears on focus.
- **Sitemap lastmod** matches schema dateModified on every blog post, and no posts are future-dated.
- **The OG image** renders (200, PNG, 48 KB), and many pages have their own.

## Recommended fix order

Start with the CDN and the LCP plates: together they address the 4.7 s mobile LCP.

1. Put a CDN in front of the origin (P1) and raise ISR revalidation (P2).
2. Fix the LCP plates (P4, P6): convert to AVIF or WebP, prioritize the first-screen plate, and convert hc.png.
3. Trim the RSC payload (P3).
4. Add descriptive alt text to the logo images (P5).

Not covered: the logged-in app behind /sign-in, real-user field data (CrUX), and backlink or keyword analysis.
