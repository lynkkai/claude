# IBM Community Blog Post #1 (draft)

## Posting details

| Field | Value |
|---|---|
| Community / group | watsonx Orchestrate (IBM TechXchange Community) |
| Title | Five rules for AI agents that act after a meeting |
| Permalink | ai-agents-after-meeting-five-rules |
| SEO meta title | Five rules for AI agents that act after a meeting |
| Meta description (under 160 chars) | Meeting agents that create tickets and update CRMs need guardrails. Five practical rules for building them with watsonx Orchestrate. |
| Tags | watsonx Orchestrate, agentic AI, AI agents, MCP, meeting automation, human in the loop |
| Visibility | Public |
| Featured image | Landscape, at least 1200 x 600 px. Suggestion: a simple diagram "Meeting > Transcript > Agent > Approval > Jira / CRM" in Lynkk colors, no pricing or sign-up text |
| Word count (body) | about 850 |

---

## Body (copy from here)

Most teams already get a summary after a meeting. The harder, more useful step is what
comes next: an agent that turns the conversation into work. It opens the Jira ticket,
updates the CRM opportunity, sends the follow-up and books the next call.

That is exactly the kind of job agent platforms like IBM watsonx Orchestrate are built
for: an agent that reasons over input and calls tools in other systems. But meetings are a
messy input. People change their minds halfway through, speak loosely ("someone should look
at that"), and mix decisions with brainstorming. An agent that acts on a meeting needs
tighter rules than one that acts on a form.

At Lynkk we build an AI meeting assistant that works before, during and after meetings, so
we think about these rules every day. Here are the five we would give any team building a
post-meeting agent, whether on watsonx Orchestrate or anywhere else.

### 1. An action item needs a real owner, or it is not an action item

The most common failure is a task with no clear owner. "We should fix onboarding" becomes a
ticket assigned to nobody, or worse, to whoever the model guessed.

Make ownership explicit in your agent's instructions:

- Only create a task when someone **committed** to it ("I'll send the draft by Friday").
- Assign it to the person who made the commitment, matched against the meeting's attendee
  list, not a free-text name.
- If nobody committed, list it as an **open question** in the notes instead of a task.

This one rule removes most of the noise that makes people stop trusting meeting automation.

### 2. Every action should point back to the moment it came from

When an agent updates a CRM field from "they mentioned budget is approved for Q1", a sales
manager will ask: who said that, and when? If the agent cannot answer, the update gets
reverted.

Store a short quote and a timestamp from the transcript with every action the agent takes.
In practice this means your tool inputs carry a `source` field alongside the payload. It
costs a few tokens and it turns "the AI changed my pipeline" into "here is the line from
the call."

### 3. Separate drafting from doing

Not every action carries the same risk. A useful split:

| Low risk: agent can act | Higher risk: agent drafts, a human approves |
|---|---|
| Write meeting notes | Send an email to a customer |
| Create a draft Jira ticket | Change a deal stage or amount in the CRM |
| Add an internal follow-up reminder | Book time on an external person's calendar |
| Tag topics for search | Close or delete anything |

Design the agent so the right-hand column always stops for a confirmation step. In
watsonx Orchestrate terms, think of it as keeping those tools behind a human approval in
the flow, rather than giving the agent a free hand with every tool it can see. The goal is
not to slow people down. It is to make sure the first mistake the agent makes is a draft
someone ignores, not an email a customer reads.

### 4. Give the agent narrow tools, not admin keys

A post-meeting agent touches many systems: calendar, ticketing, CRM, documents. It is
tempting to connect each one with a broad service account. Don't.

- Expose small, specific tools: `create_jira_issue`, `update_opportunity_next_step`, not a
  generic "call any API" tool.
- Scope credentials to the projects, pipelines or calendars the team actually uses.
- Log every tool call with the meeting it came from.

Protocols like MCP (Model Context Protocol) make it easy to plug many tools into one agent.
That is a strength, and it is also why scoping matters: the agent will use whatever it is
given.

### 5. Decide where the meeting data lives before you automate anything

Meeting transcripts are some of the most sensitive data a company produces: pricing talks,
hiring decisions, customer complaints, health or legal details. Before an agent acts on
them, answer three questions:

1. **Where is the audio and transcript processed and stored?** Many teams in regulated
   industries need this to stay in a specific region.
2. **Which models see the content,** and do those models run in the same region?
3. **What does the agent pass to downstream tools?** Often a ticket only needs the action
   and a short quote, not the whole transcript.

At Lynkk we let customers pick a region so the models behind the product process and answer
from that region, because this question comes up in almost every security review. Whatever
stack you use, settle it with your compliance team first, then automate.

### Putting it together

A simple pattern that follows all five rules:

1. Capture the meeting and produce a transcript with speakers and timestamps.
2. Extract commitments (owner, task, due date, source quote) and open questions separately.
3. Auto-run the low-risk tools: notes, draft tickets, internal reminders.
4. Queue the higher-risk actions for one-click human approval.
5. Log every action with its source, and keep the data in the agreed region.

If you are building something like this on watsonx Orchestrate, we would love to compare
notes. Which actions do you let your agents take on their own, and which always need a
human? Share your rules in the comments.

---

*About the author: [Name], [Role] at Lynkk, an AI meeting assistant that surfaces context
before meetings, answers by voice during them, and turns conversations into notes, tasks
and system updates after. Learn more at https://lynkk.ai.*

---

## Discussion post to promote it (post in the same group after the blog is live)

**Title:** How do you decide which meeting actions an AI agent can take on its own?

**Body:**
We have been thinking about guardrails for agents that act on meeting transcripts:
creating tickets, updating CRM fields, sending follow-ups. Our current rule of thumb is
"agent drafts, human approves" for anything external or hard to undo. I wrote up five rules
we use here: [link to blog]. Curious how others building on watsonx Orchestrate handle
approvals and tool scoping for this kind of agent.

## LinkedIn share text

Meeting summaries are table stakes. The real question is what an AI agent should be allowed
to do after the call. I shared five rules on the IBM TechXchange Community for building
post-meeting agents: real owners, source quotes, drafts vs. actions, narrow tools, and data
residency. [link]

---

## Checklist before submitting

- [ ] Fill in the author name and role in the bio line.
- [ ] Confirm the Lynkk statements are accurate: before/during/after features and region
      selection for data processing (both are in `memory/lynkk-brand.md`).
- [ ] Confirm the approval split in rule 3 matches how Lynkk actually behaves, or reword it as
      general advice.
- [ ] Keep it to one link to lynkk.ai (in the bio). Do not add pricing, "start free" or
      sign-up calls to action, or the moderators may reject it.
- [ ] Create and upload the featured image (1200 x 600 px minimum).
- [ ] Save as draft, preview the unpublished link, then publish.
- [ ] Wait until it is live on IBM before reposting a tailored version on lynkk.ai or LinkedIn.
