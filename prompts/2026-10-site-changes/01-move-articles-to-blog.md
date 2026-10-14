You are editing the lynkk.ai website (Next.js App Router) in this repository.

Task: move the two posts under /articles into /blog, with permanent redirects, so the blog is one section.

Before changing anything, find where the /articles posts, the /blog posts, the redirects, the sitemap and the blog index are defined, and tell me which files you will edit.

Do this:

1. Publish /articles/zoom-note-taker at /blog/zoom-note-taker, and /articles/action-items-examples-template at /blog/action-items-examples-template. Keep the content, title, meta description, author and dates exactly as they are.
2. Add permanent redirects (use the same redirect type the site already uses, which is 308):
   - /articles/zoom-note-taker to /blog/zoom-note-taker
   - /articles/action-items-examples-template to /blog/action-items-examples-template
   - /articles to /blog
3. Update each moved post's canonical URL, Open Graph URL, breadcrumbs and JSON-LD (BlogPosting, BreadcrumbList) to the new /blog URL.
4. In sitemap.xml, remove the /articles URLs and add the two new /blog URLs.
5. List both posts on the /blog index and on the author page (/blog/authors/samarth-wagh), sorted by date like the others.
6. Find every internal link on the site that points to /articles/... and change it to the new /blog/... URL.
7. If the /articles index page has its own route, remove it (the redirect replaces it).

Rules:
- Brand is always "Lynkk".
- Never use em dashes or en dashes in any copy. Use a comma, colon or parentheses instead.
- Do not change any other page.

When done, run the build and lint. Then list every file changed, confirm each old URL returns a 308 to its new URL, and confirm the sitemap no longer lists /articles.
