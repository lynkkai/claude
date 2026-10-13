# Hashnode article #1: Meeting transcripts to Jira tickets

Status: DRAFT for review
Audience: developers, engineering managers, product engineers
Companion files (in this folder): `meeting_to_jira.py` (full script), `sample-transcript.txt`
Code status: tested against mocked Claude and Jira APIs; run it once against a real
Jira sandbox project before publishing.

---

## Hashnode settings

**Title**
Turn meeting transcripts into Jira tickets with Python and Claude

**Subtitle**
Structured outputs, Jira's REST API, and the edge cases that make "just ask the LLM" harder than it looks.

**Slug**
meeting-transcript-to-jira-tickets-python

**Tags (Hashnode allows 5)**
Python, Jira, AI, LLM, Automation

**Canonical URL**
Leave empty if Hashnode is the first place this is published. If it goes on lynkk.ai/blog first,
set the canonical URL to that page.

**Cover image idea**
Left: a chat-style transcript snippet. Right: three Jira cards. Arrow between them.

---

## Article body

*Disclosure: I work on [Lynkk](https://lynkk.ai), an AI meeting assistant that does this
(and more) automatically. This post is the do-it-yourself version, and the full script
is at the end so you can run it without us.*

Every engineering team has the same meeting ritual. Someone says "I'll take that," everyone
nods, and three days later nobody remembers who took what. The transcript exists. The Jira
ticket doesn't.

In this tutorial we'll build a small Python script that:

1. Reads a meeting transcript
2. Uses Claude to extract **real commitments** (not every idea mentioned)
3. Validates the output against a typed schema
4. Creates Jira issues with owner, due date, priority, and a quote from the meeting

About 150 lines, no framework.

### The pipeline

```
transcript.txt
     |
     v
Claude (structured output) --> list[ActionItem]  (validated by Pydantic)
     |
     v
dry run: print for a human to review
     |
     v  --create
Jira REST API v3: look up assignee, create issue
```

The dry-run step is not optional decoration. You'll see why in the "edge cases" section.

### Setup

```bash
pip install anthropic pydantic requests
```

You'll need:

- A Claude API key (`ANTHROPIC_API_KEY`)
- A Jira Cloud site, your Atlassian email, and an [API token](https://id.atlassian.com/manage-profile/security/api-tokens)
- A Jira project key to create issues in (for example `ENG`)

```bash
export ANTHROPIC_API_KEY=...
export JIRA_BASE_URL=https://your-team.atlassian.net
export JIRA_EMAIL=you@company.com
export JIRA_API_TOKEN=...
export JIRA_PROJECT_KEY=ENG
```

### Step 1: Define what an action item is

The most important design decision isn't the prompt. It's the schema. If you ask an LLM for
"action items" in free text, you'll spend the rest of the project parsing bullet points.
Instead, define the exact shape you want and let the API enforce it.

```python
from typing import Literal, Optional
from pydantic import BaseModel, Field

class ActionItem(BaseModel):
    summary: str = Field(description="Short imperative ticket title, max 80 characters")
    description: str = Field(description="What needs to be done and why, in 1-3 sentences")
    owner_name: Optional[str] = Field(
        description="Name of the person who committed to it, exactly as spoken. Null if nobody did."
    )
    due_date: Optional[str] = Field(
        description="Due date as YYYY-MM-DD, resolved against the meeting date. Null if none was said."
    )
    priority: Literal["Highest", "High", "Medium", "Low"]
    source_quote: str = Field(description="The exact transcript line(s) this item comes from")

class ActionItems(BaseModel):
    items: list[ActionItem]
```

Three fields here are doing quiet but important work:

- **`owner_name` and `due_date` are `Optional`.** If you make them required, the model will
  fill them in, even when nobody said a name or a date. Optional fields give it a
  legitimate way to say "unknown."
- **`priority` is a `Literal`** that matches Jira's default priority names, so it maps
  straight onto the API with no translation table.
- **`source_quote`** forces every item to point back at what was actually said. It makes
  review fast, and it gives you something to put in the ticket so people trust it.

### Step 2: Extract with Claude

The prompt is short on purpose. The schema carries most of the instructions.

```python
SYSTEM_PROMPT = """You extract action items from meeting transcripts for a Jira backlog.

Only include an item when someone clearly commits to doing something, or the group clearly
assigns it. Ideas, opinions and "we should think about" remarks are not action items.
Never invent an owner or a due date: use null when the transcript does not say.
Resolve relative dates ("Friday", "next week") using the meeting date you are given.
Every item must quote the transcript line it came from."""
```

Then call the API with the Pydantic model as the output format. `messages.parse()` sends
the schema, constrains the response to it, and hands you back a validated object:

```python
import anthropic

def extract_action_items(transcript: str, meeting_date: str) -> list[ActionItem]:
    client = anthropic.Anthropic()

    response = client.beta.messages.parse(
        model="claude-opus-5-5",
        max_tokens=16000,
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": f"Meeting date: {meeting_date}\n\n<transcript>\n{transcript}\n</transcript>",
        }],
        output_format=ActionItems,
        # If a safety classifier declines the request, retry it on a fallback model.
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )

    if response.stop_reason == "refusal":
        raise RuntimeError("The model declined this transcript.")
    if response.stop_reason == "max_tokens":
        raise RuntimeError("Output was cut off. Split the transcript into smaller parts.")

    return response.parsed_output.items
```

A few notes:

- **Pass the meeting date.** "I'll have it done by Thursday" means nothing without it. This
  one line removes a whole class of wrong due dates.
- **Check `stop_reason` before reading the output.** A truncated or declined response
  shouldn't silently become zero tickets.
- **`fallbacks="default"`** (a beta feature, hence the `betas` header) means that if a
  request is declined by a safety classifier, the API retries it on a fallback model in
  the same call instead of just failing.

### Step 3: Create the Jira issues

Two things about the Jira Cloud REST API v3 trip people up.

**First, you can't assign by name.** Jira wants an `accountId`. So we search for the user
and only assign when there's exactly one match:

```python
import requests

def find_account_id(name: str) -> Optional[str]:
    resp = requests.get(
        f"{JIRA_BASE_URL}/rest/api/3/user/search",
        params={"query": name},
        auth=JIRA_AUTH,
        timeout=30,
    )
    resp.raise_for_status()
    users = [u for u in resp.json() if u.get("accountType") == "atlassian"]
    return users[0]["accountId"] if len(users) == 1 else None
```

Two people named Alex on the team? The ticket stays unassigned rather than going to the
wrong Alex. That's the right failure mode.

**Second, descriptions aren't plain strings.** API v3 expects
[Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/)
(ADF), a JSON document tree. A minimal converter is enough:

```python
def to_adf(*paragraphs: str) -> dict:
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": p}]}
            for p in paragraphs if p
        ],
    }
```

Now create the issue:

```python
def create_issue(item: ActionItem, project_key: str, meeting_date: str) -> str:
    fields = {
        "project": {"key": project_key},
        "issuetype": {"name": "Task"},
        "summary": item.summary[:255],
        "description": to_adf(
            item.description,
            f'From the {meeting_date} meeting: "{item.source_quote}"',
        ),
        "priority": {"name": item.priority},
        "labels": ["from-meeting"],
    }
    if item.due_date:
        fields["duedate"] = item.due_date
    if item.owner_name and (account_id := find_account_id(item.owner_name)):
        fields["assignee"] = {"accountId": account_id}

    resp = requests.post(
        f"{JIRA_BASE_URL}/rest/api/3/issue",
        json={"fields": fields},
        auth=JIRA_AUTH,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["key"]
```

The `from-meeting` label makes it easy to filter these tickets later, and to measure
whether people actually close them.

### Step 4: Try it

Here's a short sample transcript (meeting date: Tuesday 2026-10-13):

```text
Priya: Okay, quick sync on the checkout release. Where are we on the payment retry bug?
Marco: I reproduced it yesterday. It only happens when the card needs 3-D Secure. I'll have a fix up for review by Thursday.
Priya: Great. That one's blocking the release, so it's top priority.
Sam: We should probably rethink the whole retry flow at some point.
Priya: Agreed, but not this sprint. Sam, can you update the release notes once Marco's fix is merged?
Sam: Sure, I'll do that.
Priya: And someone needs to tell support about the 3-D Secure issue before Friday.
Marco: I can send them a short write-up tomorrow.
```

Run a dry run first:

```bash
python meeting_to_jira.py sample-transcript.txt --meeting-date 2026-10-13
```

You should get three items back: Marco's fix (Highest, due Thursday 2026-10-15), Sam's
release notes (no fixed date), and Marco's write-up for support (due 2026-10-14). Notice
what's **not** there: "rethink the whole retry flow." Sam floated it, Priya explicitly
deferred it, and nobody committed. That's exactly the line a naive "list the action items"
prompt turns into a ticket.

<!-- TODO before publishing: replace the paragraph above with the real dry-run output
     from an actual API run, pasted as a code block. -->

When the list looks right:

```bash
python meeting_to_jira.py sample-transcript.txt --meeting-date 2026-10-13 --create
```

### Edge cases that will bite you in production

The script above works on a clean transcript. Real meetings are messier.

**1. Speaker labels are wrong.** Owner extraction is only as good as your transcription's
speaker separation. If the transcript says "Speaker 2," the model can't produce a name,
and it shouldn't guess. This is the biggest single source of unassigned tickets.

**2. Commitments vs. suggestions.** "Maybe I could look at that" is ambiguous even to
humans. The system prompt and `source_quote` help, but this is why the dry run exists:
a 10-second human review prevents a backlog full of maybes.

**3. Duplicates across meetings.** The same task gets mentioned in Monday's standup and
Wednesday's planning. Before creating an issue, search for open `from-meeting` issues with
a similar summary (JQL: `labels = from-meeting AND statusCategory != Done`) and link
instead of duplicating.

**4. Long transcripts.** A two-hour workshop transcript is fine for the model's context
window, but long lists of items are harder to review. Consider splitting by agenda topic.

**5. Re-runs.** If the script crashes halfway through `--create`, a naive re-run creates
duplicates. Store which `source_quote`s already became tickets, or add a hash of the quote
as a label.

**6. Where the audio and text go.** Meeting transcripts contain customer names, pricing,
and internal plans. Know which region your transcription and model calls run in before
you point this at real meetings, and check that your Jira and data policies allow it.

### Going further

Ideas if you want to extend it:

- **Post the dry-run list to Slack** with approve/reject buttons, then create only approved items.
- **Add an `issue_type` field** (`Bug` / `Task` / `Story`) to the schema so the model can
  route bugs differently.
- **Pull context from previous meetings** so the model knows "the 3-D Secure bug" already
  has ticket ENG-42 and comments on it instead of opening a new one.
- **Capture in-person meetings too**, not just calls with a recording bot.

### The no-code version

That last list is roughly where a weekend script turns into a product. It's the problem we
work on at Lynkk: it records online and in-person meetings, and within about 30 seconds
after the meeting it produces notes, assigned action items, CRM updates, and Jira tickets,
with every meeting searchable afterwards. If you'd rather not maintain the script, you can
[start free](https://lynkk.ai/?utm_source=hashnode&utm_campaign=jira-tutorial).

Either way, the full script is below. If you build on it, I'd love to see what you change.

### Full script

<!-- Paste the contents of meeting_to_jira.py here, or link to a public GitHub gist. -->

```python
# meeting_to_jira.py  (see companion file in this folder)
```

---

## Before publishing

- [ ] Run the script against a real Jira sandbox project and paste the real dry-run output into Step 4
- [ ] Paste `meeting_to_jira.py` into "Full script" (or publish it as a public gist and link it)
- [ ] Check that "within about 30 seconds" is still accurate
- [ ] Check that `priority` names match the target Jira site (some sites rename or remove priorities)
- [ ] Add the cover image
- [ ] Decide on the canonical URL (Hashnode first, or lynkk.ai/blog first)
- [ ] Optional: start a Hashnode series ("Meeting automation for engineers") with this as part 1
