---
platform: LinkedIn or lynkk.ai blog (NOT Substack as planned)
status: draft v1, NEEDS SIGN-OFF, see blockers below
format: POV essay
thematic_keywords: ["hipaa compliant ai note taker" (260, CPC $31.04), "ai note taker for therapists" (90, CPC $50.63), "is it legal to record a meeting" (20)]
word_count: ~1,200
collision_check: |
  lynkk.ai already has /blog/is-it-legal-to-record-a-meeting covering consent by state and
  country. This essay deliberately avoids the consent-law angle and argues about vendor
  disclosure instead.
---

# Where Does Your Meeting Audio Go?

*By [name], [role] at Lynkk*

---

Every AI notetaker security page says the same three things. Encryption in transit and at rest.
SOC 2, or SOC 2 "in progress". We take your privacy seriously.

None of those three sentences answers the question a buyer is actually asking, which is simpler and
much harder: **what happens to the recording of my customer's voice, and who can hear it?**

I work on a meeting assistant, so I am implicated in this. That is partly why I want to argue for a
specific and slightly uncomfortable standard: in this category, the useful security page is the one
that tells you what the product **cannot** do.

## The claims that sound like answers but are not

**"Encrypted in transit and at rest."** True of essentially every SaaS product built in the last
decade, including bad ones. It tells you nothing about who can read the data once it is at rest and
decrypted for use, which is the actual question. And in this category there is a specific thing it
conceals, which I will come back to.

**"SOC 2 Type II."** A SOC 2 report says a company followed the controls it told an auditor it
follows. It is genuinely worth something, and it is a statement about process, not about what
happens to your audio. A company can hold SOC 2 and still send your recordings to four
sub-processors and retain them for seven years. Those are design choices the audit does not
prohibit.

**"We don't sell your data."** Nobody in B2B SaaS sells data. The question is whether they train on
it.

**"Enterprise-grade security."** Not a claim. A texture.

## The five questions that actually discriminate

If I were buying one of these tools, including mine, I would ask these and treat a vague answer as
a no.

**1. Do you train models on my conversations?** The only acceptable answers are "no, never" or a
clear description of the opt-in. "We may use aggregated anonymised data to improve our services" is
a yes wearing a coat. Push until you get a plain sentence, and get it in the contract rather than
the marketing page.

**2. Who are your sub-processors, by name?** Every tool in this category sends audio to a
speech-to-text provider and a language model provider. Those are usually third parties. So your
customer's voice is processed by at least two companies you have not evaluated, and possibly more.
A vendor that will not name them is asking you to accept a supply chain you cannot see.

**3. Where is it processed, and can I constrain that?** Not where the company is incorporated.
Where the audio physically goes. Many vendors, including mine, process across multiple
jurisdictions, and the honest ones say so.

**4. What is the retention default, and can I change it?** How long do you hold the audio, the
transcript, and the derived notes, and are those three different? Most buyers assume deleting a
note deletes the recording. Check.

**5. Is it end-to-end encrypted?** Here is the one that matters most, and almost nobody asks it,
because the answer is structurally the same across the whole category: **no, and it cannot be.**

## The thing the category cannot admit

A meeting assistant has to read your conversation in order to write a note about it. That is the
product. Which means the service, by design, has plaintext access to the content of your meetings
at the moment it processes them.

That is not a flaw to be engineered away. It is the shape of the thing. An end-to-end encrypted
meeting assistant that produces summaries is, for practical purposes, a contradiction.

So when a security page in this category leads with "encrypted in transit and at rest" and does not
mention this, it is not lying, but it is allowing you to form a conclusion the vendor knows is
wrong. The buyer walks away thinking their customer conversations are sealed. They are not sealed.
They are readable by the service, briefly, in order to do the job you hired it for.

I would rather a vendor said that in one sentence on the page. Lynkk's own security page does:
"Lynkk isn't end-to-end encrypted, because it has to read a recording to write the note." I think
that sentence is worth more to a buyer than any badge, and not because my employer wrote it. It is
worth more because it is the kind of sentence that tells you what else on the page you can trust.

## What a security page should look like in this category

Specific, falsifiable, and narrow:

- **Named limits.** What the product does not do, in plain words.
- **Numbers, not adjectives.** "Upload links expire after 10 minutes." "The desktop app deletes its
  local copy after 7 days." "Playback links expire after an hour." You can verify those. You cannot
  verify "robust".
- **The access model stated.** Who inside my organisation can read a note. Can an admin? Can they
  get the recording as well as the text? Is there a setting that excludes a conversation from
  that?
- **Scoped encryption claims.** If AES-256 covers your integration tokens, say that it covers your
  integration tokens. A blanket "AES-256 encryption" badge over a page where that is the narrow
  truth is the most common piece of misdirection in the category, and I have seen it on pages I
  was not responsible for and pages I was adjacent to.
- **Export and deletion, as mechanics.** Not "you can delete your data" but where the button is and
  what arrives.

## For anyone in a regulated field

If you are a therapist, a lawyer, a financial adviser or a clinician, most of this category is not
built for you, whatever the landing page says about your profession. The questions above become
threshold requirements rather than preferences, you will need a signed agreement rather than a
policy page, and "HIPAA compliant" on a marketing site is a claim to verify in a contract, not a
feature to trust. The economics here are telling: these are the highest-value search terms in the
entire category, which means you are being marketed to very hard by people who may not be able to
support the claim.

## The standard I would want applied to us

Publish what you cannot do. Name your sub-processors. Give numbers for retention. Say the thing
about end-to-end encryption out loud.

I would rather compete against vendors who do all four, because the current equilibrium, where
everybody says "enterprise-grade" and nobody says what is actually true, is one where the least
careful vendor sounds exactly like the most careful one. That is bad for buyers and, slightly less
obviously, bad for anyone trying to build the careful version.

---

## BLOCKERS: do not publish until these are resolved

1. **Sign-off from whoever owns security and legal at Lynkk.** This essay holds Lynkk to a standard
   publicly. That is the point of it, and it is also a commitment. Someone senior has to agree
   Lynkk can meet it.
2. **Sub-processors.** The essay says vendors should name theirs. Lynkk's security page says audio
   goes to speech-to-text and AI model providers but does not name them. Either name them before
   this publishes, or soften that section, because publishing a standard you visibly fail is worse
   than not publishing.
3. **Retention.** I used the specific figures from the live security page (10-minute upload links,
   1-hour playback links, 7-day local copy, 7-day dictation deletion, 30-day share links). Confirm
   these are current.
4. **"HIPAA compliant"** is discussed as a category-wide caution. Confirm Lynkk makes no HIPAA
   claim anywhere, including sales decks and use-case pages, before this goes out.
5. **No accuracy or certification claim appears in this draft**, deliberately. There is no SOC 2
   claim on lynkk.ai and no published accuracy figure, so none is made here.

**Not for Substack** as part of an SEO programme. **Recommended home:** LinkedIn and the lynkk.ai
blog, where it belongs next to the security page.
