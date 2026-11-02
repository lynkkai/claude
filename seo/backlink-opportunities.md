# Lynkk.ai: Backlink Opportunity Research

Researched 2026-11-02. Sources: Ubersuggest backlink gap analysis against six direct
competitors, plus live web research on directories, marketplaces and registries.

## Important note on your spreadsheet

The Google Sheet link you shared is not open to "anyone with the link" from outside your
Google account, so I could not read it. Every opportunity below is grouped by **category**,
so you can delete whole rows you have already done instead of reading line by line.

What I *could* verify is which domains already link to lynkk.ai today. Only these five are
live, and all five are **nofollow**:

| Live referring domain | First seen | Link type |
|---|---|---|
| sideprojectors.com | 2026-10-03 | nofollow |
| webcatalog.io | 2026-10-28 | nofollow |
| ideaproof.io | 2026-09-10 | nofollow (spam score 49, low quality) |
| comingup.io | 2026-10-03 | nofollow |
| tablif.com | 2026-10-31 | nofollow |

Those five are excluded from everything below.

## Current state (Ubersuggest, 2026-11-02)

| Metric | lynkk.ai |
|---|---|
| Domain authority | 1 |
| Total backlinks | 9 |
| Referring domains | 5 |
| Dofollow links | **0** |
| .gov / .edu links | 0 |

**The headline problem is not volume, it is that you have zero dofollow links.** If your
sheet is mostly generic AI tool directories, that explains it: most of that tier is nofollow
or not indexed. The categories below are ordered so the dofollow and high-trust ones come
first.

---

## Tier 1: Product marketplaces and app stores (highest value, almost certainly not in your sheet)

This is where every serious competitor gets its strongest links, and it is the category most
founders skip because it needs a small integration rather than a form fill. Fathom is on the
HubSpot marketplace, Fireflies is on Slack, Webex, Zoho and Zoom, Granola is on Google
Workspace Marketplace, Circleback and MeetGeek are on Slack. None of these link to Lynkk.

| Platform | Submit at | Why it fits Lynkk | Effort |
|---|---|---|---|
| Zoom App Marketplace | developers.zoom.us/docs/distribute | Core meeting platform, needs a Technical Design Document and review | High |
| Google Workspace Marketplace | workspace.google.com/marketplace | You already pull meetings from Calendar, so a Calendar add-on is a natural listing | High |
| Slack Marketplace | slack.com/marketplace | Post notes and action items to channels | Medium |
| Atlassian Marketplace | marketplace.atlassian.com | You already create Jira tickets, this is a direct fit | Medium |
| HubSpot App Marketplace | ecosystem.hubspot.com/marketplace/apps | Your CRM field updating, same slot Fathom occupies | Medium |
| Microsoft AppSource / Teams store | appsource.microsoft.com | Teams meetings | High |
| Webex App Hub | apphub.webex.com | Low competition, Fireflies ranks well here | Medium |
| Zoho Marketplace | marketplace.zoho.com | Zoho CRM field updates | Medium |
| Salesforce AppExchange | appexchange.salesforce.com | Enterprise credibility | High |
| Pipedrive Marketplace | pipedrive.com/en/marketplace | Underserved, good for sales positioning | Medium |
| monday.com apps | monday.com/marketplace | Task sync | Medium |
| Zapier app directory | zapier.com/apps | Public integration page, strong authority | Medium |
| Make.com apps | make.com/en/integrations | Same | Medium |
| n8n integrations | n8n.io/integrations | Community node is enough | Low |
| Cal.com app store | cal.com/apps | You already list Cal.com as an integration, so claim the reciprocal listing | Low |
| Calendly integrations | calendly.com/integrations | Same, ask your Calendly contact | Low |
| Notion integrations gallery | notion.com/integrations | Notes destination | Medium |
| Chrome Web Store | chromewebstore.google.com | MeetGeek and tl;dv both get links here | Medium |
| Raycast Store | raycast.com/store | Your Mac dictation feature fits perfectly | Low |
| Setapp | setapp.com/vendors | Curated Mac app bundle, strong Mac audience | Medium |
| Apple App Store | appstoreconnect.apple.com | Every competitor has a DA 99 link from here | High |

**Quick win inside this tier:** Cal.com, Calendly and n8n. You already name them as
integrations on your own site, so ask each one for the reciprocal listing. That is the
cheapest high-authority link on this whole page.

---

## Tier 2: MCP registries (your unique differentiator, and nearly nobody in this category has done it)

You support "connect anything via MCP". None of your competitors have claimed this link
category. These are mostly GitHub-backed or developer-run, so they tend to be dofollow and
indexed fast.

| Registry | Submit at | Notes |
|---|---|---|
| Official MCP Registry | registry.modelcontextprotocol.io | Start here, publish with the mcp-publisher CLI and a server.json, verify your domain with a DNS TXT record. Several other directories pull from this one |
| mcp.so | mcp.so | Submission form, review gated |
| Glama | glama.ai/mcp/servers | Mirrors the official registry |
| Smithery | smithery.ai | Now a public directory powered by Arcade.dev, confirm current submission terms |
| mcp.directory | mcp.directory | Mirrors the official registry |
| Awesome MCP Servers | github.com/punkpeye/awesome-mcp-servers | GitHub pull request, dofollow from a high authority repo |
| Docker MCP Catalog | hub.docker.com | Review gated pull request |
| Claude connector directory | claude.ai/directory/manage | Separate review from the public registry, submit as an MCP connector |
| Cursor directory | cursor.directory | Developer audience |
| ClaudePro Directory | claudepro.directory | Low effort |
| PulseMCP | pulsemcp.com | **Reported closed to new submissions** as of late 2026, check again before spending time |

Also worth doing alongside this: AI agent directories, since your live voice assistant
qualifies. aiagentstore.ai, aiagentsdirectory.com, aiagentslist.com, agentsindex.ai,
agenthunter.io.

---

## Tier 3: Software review platforms (trust signals plus AI search citations)

These do more than pass link equity. They are what ChatGPT, Perplexity and Google AI
Overviews cite when someone asks for "best AI meeting assistant", which matters more than
raw DA right now.

| Site | Submit at | Notes |
|---|---|---|
| G2 | g2.com (free vendor profile) | The single most important one in this tier |
| Capterra | vendors.capterra.com | One submission also creates **GetApp** and **Software Advice** listings, so three links for one form |
| TrustRadius | trustradius.com | Free basic vendor profile |
| Gartner Peer Insights | gartner.com/reviews | Free, enterprise credibility, good for your data residency story |
| SourceForge | sourceforge.net/software/vendors | One submission also lists you on **Slashdot** |
| Crozdesk | crozdesk.com | Free listing |
| Tekpon | tekpon.com | Free listing, confirm terms on their vendor page |
| SaaSworthy | saasworthy.com | Free listing |
| GoodFirms | goodfirms.co | Free listing |
| Serchen | serchen.com | Free listing |
| FinancesOnline | financesonline.com | Free listing |
| SoftwareSuggest | softwaresuggest.com | Free listing, strong in India and APAC |
| Trustpilot | business.trustpilot.com | Reviews, not really SEO, but it is a brand trust page |
| Spiceworks community | community.spiceworks.com | IT buyer audience |

Note: G2 reportedly acquired Capterra, GetApp and Software Advice from Gartner in early 2026,
so verify whether the Capterra submission flow has changed before you start.

---

## Tier 4: Alternatives and comparison engines (highest commercial intent)

These rank for "Otter alternative", "Fireflies alternative", "Granola alternative", which is
exactly the traffic you want. AlternativeTo links Fireflies and Granola today but not Lynkk.

| Site | Submit at |
|---|---|
| AlternativeTo | alternativeto.net (create the app page, then add yourself as an alternative to Otter, Fireflies, Granola, Fathom) |
| SaaSHub | saashub.com |
| StackShare | stackshare.io |
| Slant | slant.co |
| Toolify.ai | toolify.ai |
| TopAI.tools | topai.tools |
| Futurepedia | futurepedia.io |
| There's An AI For That | theresanaiforthat.com (free queue is slow, paid is faster) |
| FutureTools | futuretools.io (fast and free, but reportedly nofollow) |
| Insidr AI | insidr.ai/ai-tools |
| OpenTools | opentools.ai |
| EliteAI.tools | eliteai.tools |
| Aixploria | aixploria.com |

**Do this after you create the AlternativeTo page:** add Lynkk as an alternative on each
competitor's page individually. That is where the actual traffic comes from, not from your
own listing page.

---

## Tier 5: Company and entity databases (fixes your brand confusion problem)

Your brand memory already flags that Lynkk gets confused with Lynk, Lynk AI, Linnk AI and
Link AI. Entity databases are how you fix that in Google's knowledge graph, not just how you
get links. Every competitor has a Crunchbase profile, you do not.

| Site | Submit at | Notes |
|---|---|---|
| Crunchbase | crunchbase.com/add-new | Essential, all six competitors have one |
| Wikidata | wikidata.org | Free, and the strongest single entity disambiguation signal |
| LinkedIn company page + Products tab | linkedin.com/company/setup | Also where buyers check you are real |
| Wellfound | wellfound.com | Jobs plus a company profile |
| F6S | f6s.com | Free startup profile |
| Dealroom | dealroom.co | Free company claim |
| Tracxn | tracxn.com | Free profile |
| Owler | owler.com | Free profile |
| Golden | golden.com | Knowledge graph feeder |
| Startup Ranking | startupranking.com | Free |
| Growjo | growjo.com | Free |
| BuiltWith / G2 Stack | builtwith.com | Tech profile |

---

## Tier 6: Download and app catalogs (the pattern your competitors quietly rely on)

You have a Mac desktop app, so you qualify for all of these. Fireflies, Granola, MeetGeek and
tl;dv all have Uptodown pages. Granola has TechSpot and Clubic. These are DA 88 to 92 pages
and most of them accept a simple submission.

| Site | Submit at | Notes |
|---|---|---|
| Uptodown | uptodown.com (developer submission) | Four of six competitors are here |
| Softpedia | softpedia.com/submit | Mac and Windows |
| MacUpdate | macupdate.com/developers | Mac native |
| TechSpot Downloads | techspot.com/downloads | Granola is listed |
| Clubic (FR) | clubic.com/telecharger | Granola and tl;dv are both listed |
| FileHorse | filehorse.com | Low effort |
| FileHippo | filehippo.com | Low effort |
| Logitheque (FR) | logitheque.com | Non-English, low competition |
| heise Download (DE) | heise.de/download | Non-English, high authority |
| MacGeneration (FR) | macg.co | Mac plus French |

---

## Tier 7: Launch platforms (you have Product Hunt copy ready, here is everything else)

Your repo already has `launch/producthunt-submission.md`, so I assume Product Hunt is planned.
These are the rest, and they can be run as a staggered launch calendar over several weeks
rather than all at once.

| Platform | Submit at | Notes |
|---|---|---|
| BetaList | betalist.com/submit | Good for pre-launch and early stage |
| Peerlist Launchpad | peerlist.io/launchpad | Weekly cycle, strong engagement |
| Uneed | uneed.best | Free tier available |
| Fazier | fazier.com | Free with a badge requirement |
| Startup Fame | startupfa.me | Free, badge exchange speeds up review |
| Microlaunch | microlaunch.net | Free |
| Launching Next | launchingnext.com | Free |
| DevHunt | devhunt.org | Developer audience |
| Tiny Launch | tinylaun.ch | Free |
| Smol Launch | smollaunch.com | Dofollow activates when you verify the badge on your domain |
| Kick Product | kickproduct.com | Fair launch model |
| OpenHunts | openhunts.com | Free |
| Earlyhunt | earlyhunt.com | Free |
| Indie Hackers Products | indiehackers.com/products | Community plus profile |
| Hacker News (Show HN) | news.ycombinator.com/showhn | Fathom, Granola and tl;dv all got HN links |
| Reddit | r/SideProject, r/productivity, r/artificial, r/sales | Nofollow, but drives real signups and AI citations |

Many free tiers here require you to put their badge on your site first. Decide up front how
many badges you are willing to carry, and prioritize the ones where the badge unlocks a
dofollow link (Smol Launch, Startup Fame, Fazier).

---

## Tier 8: GitHub awesome lists (dofollow, DA 96, and free)

Fireflies is in `steven2358/awesome-generative-ai`. Granola is in
`charlax/professional-programming`. These are plain pull requests.

- github.com/steven2358/awesome-generative-ai
- github.com/mahseema/awesome-ai-tools
- github.com/punkpeye/awesome-mcp-servers
- github.com/jamesmurdza/awesome-ai-devtools
- github.com/best-of-ai/ai-directories (also a useful index of ~180 more directories)
- Hugging Face organization page: huggingface.co (Fireflies has one)
- npm or PyPI package page, if you ship any SDK or CLI

One caution: submit only to lists where you genuinely fit the category, or the pull request
gets rejected and it costs you credibility with that maintainer.

---

## Tier 9: Editorial inclusion in roundups that already rank (highest ROI of everything here)

This is link insertion outreach, not directory submission, and it is where the real authority
gap is. Each of these pages **already ranks for your target keywords and already links your
competitors but not you**. You are pitching inclusion in an existing article, which is a far
easier ask than a new article.

Verified from the competitor gap analysis:

| Page | Currently links | DA |
|---|---|---|
| techrepublic.com/article/news-best-ai-meeting-note-takers-2026/ | Fireflies, Granola | 88 |
| jotform.com/ai/agents/best-ai-meeting-assistant/ | MeetGeek, tl;dv | 92 |
| jotform.com/ai/otter-ai-alternatives/ | Fireflies | 92 |
| shopify.com/blog/best-ai-note-taking-app | Fathom, Granola | 95 |
| digitalocean.com/resources/articles/ai-meeting-tools | Fathom | 86 |
| zendesk.com/service/ai/conversational-intelligence-software/ | Fathom, Fireflies | 93 |
| salesforce.com/au/artificial-intelligence/ai-meeting-assistant/ | Fireflies, Granola, MeetGeek, tl;dv | 92 |
| mspoweruser.com/otter-ai-alternatives/ | tl;dv | 89 |
| time.com/partner-content/charter/6987522/ | Granola, Circleback | 94 |
| entrepreneur.com/science-technology/these-are-the-50-best-ai-tools-right-now/490264 | Granola | 92 |
| freecodecamp.org/news/ai-assistants-for-productivity/ | Fireflies | 86 |
| upwork.com/resources/ai-transcription-tools | MeetGeek | 89 |
| dreamhost.com/blog/ai-productivity-tools/ | tl;dv | 88 |
| smallbiztrends.com/ai-tools-for-business/ | Fireflies | 86 |
| bigcommerce.com/glossary/voice-intelligence/ | tl;dv | 91 |
| elegantthemes.com/blog/business/best-ai-tools | Fireflies | 85 |
| gizmodo.com/the-best-transcription-services-that-are-free-to-try-2000377213 | MeetGeek | 93 |
| cultofmac.com/reviews/best-ai-apps-for-mac | Granola | 88 |

Pitch angle that actually works here: do not ask to be added as "another AI note taker". Lead
with the two things none of the listed tools do, which are the **live in-meeting voice
assistant that speaks** and **regional data residency**. Offer the writer a free account and a
two-sentence description they can paste in.

### Education resource pages (.edu, easiest high-authority links available to you)

University IT and library guides maintain "AI tools" and "AI note taker policy" pages, they
link tools freely, and they are actively looking for a tool with a data residency and privacy
story. You currently have zero .edu links.

- it.cornell.edu/ai-strategy/manageainotes
- hsph.harvard.edu/information-technology/news/how-to-effectively-manage-ai-meeting-assistants-aka-bots-in-your-zoom-sessions/
- guides.library.cmu.edu/c.php?g=1453451
- guides.libraries.indiana.edu/c.php?g=995240
- blogs.uoregon.edu/artificialintelligence/ai-software/
- guides.lib.udel.edu/businessAI/business
- dres.illinois.edu/accommodations/ams/assitive-technology/note-taking-software/
- American University, BYU, Waterloo and Rice all have equivalent pages in the gap data

---

## Tier 10: Non-English directories (a real, unclaimed gap)

Lynkk is multilingual, so this is on-message rather than a stretch. Competitors get links from
these and the competition for them is almost nil.

| Region | Targets |
|---|---|
| Japan | note.com, Qiita, Hatena Bookmark, PR Times, Impress Watch |
| Spain / LatAm | Xataka, Genbeta, AdslZone, Uptodown ES |
| Brazil | TecMundo, Olhar Digital |
| France | Clubic, Logitheque, MacGeneration |
| Germany | heise, t3n |
| Russia | Habr |
| India | startuplist.in, desifounder.com, YourStory, Inc42, SoftwareSuggest |

Localized landing pages plus a localized listing is the play here, not just submitting the
English page.

---

## Tier 11: Digital PR and founder-led (slow but compounding)

- **Journalist request platforms:** Featured.com, Qwoted, SourceBottle, Help a B2B Writer.
  Answer questions about AI meeting etiquette, consent, and data residency.
- **Vendor case studies:** tl;dv has stripe.com/customers/tldv (DA 92). Ask every vendor in
  your own stack (Stripe, Vercel, Supabase, your ASR provider, your cloud region provider) to
  write you up. This is free and most of them want the content.
- **Podcast guesting:** the gap data is full of podcast feed links (Spreaker, Acast, Audioboom,
  iHeart, Substack podcast feeds). One founder interview produces a link from the feed, the
  host's site, and every aggregator.
- **Funding and product news:** GlobeNewswire, Digital Journal, EU-Startups, TechCrunch tips.
  Fireflies, Fathom, Granola and Circleback all have TechCrunch links, which came from funding
  or feature news, not from pitching a tool.
- **Owned writing:** Medium, Substack, dev.to, Hashnode. Write about offline-first audio
  capture or regional model routing, which is genuinely technical and genuinely yours.

---

## Suggested order of work

1. **Week 1, free and fast:** Crunchbase, Wikidata, LinkedIn, G2, Capterra (gets you three),
   TrustRadius, SourceForge, AlternativeTo, SaaSHub.
2. **Week 1, reciprocal asks:** Cal.com, Calendly, n8n, plus every vendor in your own stack
   for a case study. These cost one email each.
3. **Week 2, MCP registries:** official registry first, then the mirrors pick you up.
4. **Week 2 to 4, download catalogs:** Uptodown, Softpedia, MacUpdate, TechSpot, Clubic.
5. **Week 3 onward, marketplaces:** Slack, Atlassian, HubSpot, Chrome Web Store, then Zoom and
   Google Workspace, which take longest to get approved.
6. **Ongoing, highest value:** the Tier 9 roundup and .edu outreach. Budget real time for this.
   Ten placements here are worth more than two hundred directory listings.
7. **Launch calendar:** stagger Tier 7 across several weeks so each one has something to say.

## Two things to stop doing

- **Avoid more of the low quality AI directory tier.** ideaproof.io already linking you has a
  spam score of 49. There are roughly 180 of these in the `best-of-ai/ai-directories` list and
  submitting to all of them will not move DA 1 upward. Pick the ten in Tier 4 that actually
  get traffic and stop there.
- **Check for nofollow before you spend time.** All nine of your current links are nofollow.
  Before submitting, load the directory's existing listing for a competitor and check the
  outbound link for `rel="nofollow"`. If it is nofollow and the site has no real audience,
  it is not worth the form.

## Sources

Competitor backlink gap data: Ubersuggest, run 2026-11-02 against fireflies.ai, fathom.video,
granola.ai, tldv.io, bluedot.so, circleback.ai and meetgeek.ai.

Directory research:
- https://github.com/best-of-ai/ai-directories
- https://www.lilachbullock.com/free-ai-tool-directories-to-submit-your-tool/
- https://wheretosubmit.org/guides/ai-tool-directories
- https://siteefy.com/free-ai-tool-directories
- https://getintel.ai/blog/best-saas-directories-2026/
- https://submitsaas.com/directories
- https://thesaasdir.com/blog/best-saas-directories-for-backlinks/
- https://smollaunch.com/best-of/directories-to-submit-startup-2026
- https://linklyhq.com/blog/mcp-server-directories
- https://submitmap.com/lists/mcp-server-directories/
- https://www.securecoders.com/blog/mcp-server-registry-guide
- https://developers.zoom.us/docs/distribute/
- https://blastra.io/blog/g2-capterra-vendor-pricing-compared/
- https://thesaasdir.com/blog/g2-vs-capterra-vs-trustradius/
