# Platform Guidelines: What Each One Actually Permits, and What That Changes

**Checked:** 2026-11-02, against the platforms' own current policy pages.
**Applies to:** every post in the 12-topic plan, before publishing.

Quick summary: **Hashnode and Medium are fine with care. Substack, as planned, is not permitted.**

---

## 1. Substack: the plan as written breaks the Content Guidelines

This is the finding that matters. Substack's Content Guidelines (last updated **29 September 2026**)
say, verbatim:

> "Substack is intended for high quality editorial content, not conventional email marketing. We
> don't permit publications whose primary purpose is to advertise external products or services,
> drive traffic to third party sites, distribute offers and promotions, **enhance search engine
> optimization**, or similar activities. Brands and commercial organizations publishing on
> Substack may be subject to additional verification."

Compare that with the brief I was given: publish on Substack and interlink the posts into the
lynkk.ai blog for internal linking. That is "drive traffic to third party sites" and "enhance
search engine optimization", named in the same sentence. A Lynkk-branded Substack whose stated
purpose is SEO and referral traffic is **not a grey area**, and "brands and commercial
organizations ... may be subject to additional verification" means Lynkk would be looked at.

The guidelines are also explicit that they are enforced: "we may remove it, hide it from public
view, or impose other restrictions."

### Three options, in the order I would pick them

1. **Drop Substack from the plan.** Put S1, S2 and S4 on **LinkedIn** (where a sales-leadership
   audience actually is) and on the lynkk.ai blog. You lose nothing in SEO terms, because Substack
   was never going to deliver SEO anyway. This is my recommendation.
2. **Run it as a genuine publication, with no SEO job.** A newsletter under a named person at
   Lynkk, with the affiliation stated, written as real editorial, **no internal-linking quota**,
   and no expectation of search value. That is permitted. It is also a long-term commitment and a
   different project from this one.
3. **Do it as planned anyway.** Not advisable. It risks the publication, and the upside was
   never real: Substack posts are not an SEO asset.

**Either way, the "interlink Substack into the lynkk.ai blog" part of the original brief has to
go.** If we keep a Substack at all, essays there get links only where a reader genuinely needs
them, not two per post as a rule.

---

## 2. Medium: publishable, but expect no distribution, and say who you are

Medium's **Distribution Guidelines** sort every story into Boost, General or Network. Under
General Distribution, the **"low-value content"** heading explicitly lists **sponsored content,
content marketing and PR pieces**. AI-generated content is on the same list. Boost is nominated
and reviewed **manually by human curators**, and meeting the criteria does not guarantee selection.

**What this means for the four Medium posts:**

- They will most likely be read as content marketing, because that is what they are. Expect
  **Network Distribution**, meaning they reach your own followers and nothing more. Do not build
  the plan on Boost or General.
- **This does not break the strategy.** The Medium bet was always Google, not Medium's feed. The
  proof is in the SERP I pulled: a Medium post ranks **position 3** for
  `ai note taker for in person meetings`, above plaud.ai, read.ai, otter.ai and notta.ai. Network
  Distribution does not stop a post being indexed and ranking.
- So: keep publishing on Medium, target search, and stop expecting curation.

**Rules to follow on every Medium post:**

- **Disclose the affiliation in the post, high up**, not buried at the end. "I work on Lynkk" in
  the first screen, not in the final section.
- **One product section, clearly marked, at the end.** Not product claims threaded through.
- **No third-party product promotion**, and if an affiliate link ever appears it must be disclosed.
- **Do not publish the same text on lynkk.ai and Medium.** Either rewrite, or set a canonical.
- **Human editing is mandatory.** These drafts are AI-assisted, and AI-generated content is named
  as low-value. Whoever publishes has to genuinely edit and own the text.

---

## 3. Hashnode: the strictest on exactly what we were planning

Hashnode's **Code of Conduct** prohibits, verbatim:

> "Automated or bulk posting, engagement farming, misleading links, **SEO abuse**, or **using the
> platform primarily for self-promotion without contributing to the community**."

and:

> "Posts must be your original work, or clearly attributed to the original source."

On AI: "If you use AI-assisted writing, review everything before publishing. You are responsible
for the accuracy and originality of your content."

Hashnode's **Terms of Use** additionally ban unsolicited promotional content and automated content
generation aimed at manipulating search results or engagement. Enforcement is partly automated:
a Hashnode co-founder has said publicly that they "use AI to detect spam and delete posts
automatically", with appeals through support.

**The operative phrase is "without contributing to the community".** A Hashnode post that teaches
a real technical thing is welcome even though Lynkk benefits. A post that exists to rank and link
is not. So:

- **H1-new, H2, H3, H4 must carry real technical substance**: actual code, real numbers, real
  failure modes. If a post could be written without having built the thing, it should not go on
  Hashnode.
- **At most one link to a commercial Lynkk page per post.** The second link should be
  documentation, a technical page, or nothing.
- **Do not bulk-publish.** Space them out. Four technical posts landing in a week from a company
  account reads exactly like the pattern their spam detection is built for.
- **Canonical:** Hashnode sets it via `originalArticleURL` in the publish API. Note the trap: if
  a pipeline creates a draft and someone then presses publish in the dashboard, the canonical is
  never attached. **If you publish on Hashnode first with no canonical, Hashnode becomes the
  canonical version by default.** Decide per post, and check after publishing.
- **Human review is required**, same as Medium, and here it is written into the Code of Conduct.

---

## 4. The AI-content issue, across all three

Every draft I produce is AI-assisted. Medium names AI-generated content as low-value content.
Hashnode makes the author responsible for accuracy and originality. Substack requires that content
be your own work.

**This is not a reason to stop, but it sets a hard condition:** a named human at Lynkk has to read
every draft properly, change what is wrong, add what only they know (real numbers, real incidents,
real screenshots), and publish it as their own work. A draft pasted unedited is both a policy
problem and, on current curation, a quality problem. The technical posts in particular cannot be
written credibly without someone who built the feature adding to them.

---

## 5. Revised rules per platform

| | Medium | Hashnode | Substack |
|---|---|---|---|
| Allowed as planned? | Yes, with disclosure | Yes, if genuinely technical | **No, as planned** |
| Expect platform distribution? | **No.** Network only. Target Google. | Feed reach only if substantive | Subscribers only |
| Links to lynkk.ai per post | 2 max, product section at the end | **1 max**, prefer docs | **No quota.** Only where needed |
| Affiliation disclosure | **Required, high in the post** | Required | Required |
| Canonical | Medium-first, no canonical, do not duplicate on the blog | Set `originalArticleURL`, verify after publishing | N/A |
| Cadence | Space out | **Space out, do not bulk-post** | Normal newsletter cadence |
| Human edit before publishing | Mandatory | **Mandatory, per Code of Conduct** | Mandatory |

---

## Sources

- [Substack Content Guidelines](https://substack.com/content) (fetched 2026-11-02, page states last updated 29 September 2026)
- [Hashnode Code of Conduct](https://hashnode.com/code-of-conduct) (fetched 2026-11-02)
- [Hashnode Terms of Use](https://hashnode.com/terms)
- [Medium's Distribution Guidelines](https://help.medium.com/hc/en-us/articles/360006362473-Medium-s-Distribution-Guidelines-How-curators-review-stories-for-Boost-General-and-Network-Distribution) (help.medium.com blocks automated fetching, so the Medium wording above comes from search results quoting that page, not from my own read of it. Worth one manual check in a browser before you rely on it.)
- [Hashnode forum thread on automated spam detection](https://hashnode.com/forums/thread/wrongful-community-guidelines-flag-on-my-blog-post)
