---
platform: Hashnode
title: "From Meeting Action Items to Jira Issues: A Small Python Service"
subtitle: "Extract owners, due dates and priorities from meeting notes, resolve people to Jira accounts, and create issues that still make sense to someone who wasn't on the call."
slug: meeting-action-items-to-jira-python
tags: [jira, python, automation, productivity, api]
target_queries: ["meeting minutes to jira", "meeting bot for jira", "action items to jira", "tracking action items"]
evidence: "GSC: /blog/meeting-minutes-to-jira 38 impr at avg 10.5 (near page one); 'tracking action items' 13 impr, 'action item ai' 12; /blog/action-items-examples-template 576 impr at avg 31.7; Ubersuggest: 'meeting bot for jira' appears as a long-tail suggestion"
main_site_links:
  - https://lynkk.ai/blog/meeting-minutes-to-jira
  - https://lynkk.ai/blog/action-items-examples-template
  - https://lynkk.ai/integrations/jira
canonical: "none (original article, do not set a canonical)"
cover_image: "A meeting summary card with an arrow into a Jira-style board column"
status: draft
---

# From Meeting Action Items to Jira Issues: A Small Python Service

Every engineering team has the same leak: a decision gets made in a meeting, someone says "I'll take that," and the task never makes it into Jira. Two sprints later nobody remembers who owned it.

This post builds a small service that takes structured action items from meeting notes and creates Jira issues with an assignee, due date, priority and enough context to be useful. It's deliberately provider-agnostic: the action items can come from a human-written summary, an AI notetaker's export, or an LLM you run yourself.

## The shape of a good action item

Before writing code, agree on what an action item is. A useful one has:

- **one owner** (not "the team");
- **a verb-first summary** ("Send revised pricing draft to Sam");
- **a due date** if one was stated;
- **a priority** if one was implied;
- **a link back to the moment in the meeting** where it was agreed.

If your notes don't capture those, no amount of automation helps. There's a good list of [action item examples and a template](https://lynkk.ai/blog/action-items-examples-template) for calibrating what "good" looks like.

We'll use this schema:

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class ActionItem:
    summary: str                  # "Send revised pricing draft to Sam"
    owner_email: Optional[str]    # "dana@acme.com"
    due_date: Optional[str]       # "2026-10-29" (ISO)
    priority: Optional[str]       # "High" | "Medium" | "Low"
    meeting_title: str            # "Acme pilot kickoff"
    meeting_url: str              # link to the note or recording
    quote: str                    # the sentence where it was agreed
    timestamp: str                # "00:24:10"
```

## Step 1: Get structured action items

**Option A: from a notetaker.** Many notetakers export notes as Markdown or JSON with action items, owners and timestamps. Map their fields to `ActionItem`.

**Option B: from a transcript with an LLM.** If you're extracting yourself, ask for strict JSON and validate it. A prompt that works well across models:

```text
From the meeting transcript below, list every action item that someone
explicitly agreed to do. Return JSON only, as a list of objects with keys:
summary (imperative, under 12 words), owner_name, due_date (ISO date or null),
priority (High/Medium/Low or null), quote (the exact sentence), timestamp.
Do not invent owners or dates. If no owner was stated, use null.
```

Two rules matter more than prompt wording: **validate the JSON against your schema**, and **never invent owners**. An unassigned issue is better than one assigned to the wrong person.

## Step 2: Resolve owners to Jira account IDs

Jira Cloud assigns issues by `accountId`, not email. Look people up with the user search endpoint:

```python
import os
import requests

JIRA = os.environ["JIRA_BASE_URL"]          # https://your-domain.atlassian.net
AUTH = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}

_cache: dict[str, str | None] = {}

def account_id_for(email: str | None) -> str | None:
    if not email:
        return None
    if email in _cache:
        return _cache[email]
    r = requests.get(f"{JIRA}/rest/api/3/user/search",
                     params={"query": email}, auth=AUTH, headers=HEADERS, timeout=20)
    r.raise_for_status()
    users = r.json()
    _cache[email] = users[0]["accountId"] if users else None
    return _cache[email]
```

Email visibility depends on each user's Atlassian privacy settings, so lookups can return nothing. Fall back to leaving the issue unassigned and mentioning the owner's name in the description.

## Step 3: Write a description in Atlassian Document Format

Jira Cloud's v3 API expects descriptions in ADF (a JSON document format), not Markdown. Keep it simple: context, the quote, and a link.

```python
def adf_description(item: ActionItem) -> dict:
    def para(*nodes):
        return {"type": "paragraph", "content": list(nodes)}
    def text(t, marks=None):
        node = {"type": "text", "text": t}
        if marks:
            node["marks"] = marks
        return node

    return {
        "type": "doc",
        "version": 1,
        "content": [
            para(text("From meeting: "), text(item.meeting_title, [{"type": "strong"}])),
            para(text(f"Agreed at {item.timestamp}: "), text(f"“{item.quote}”", [{"type": "em"}])),
            para(text("Source note", [{"type": "link", "attrs": {"href": item.meeting_url}}])),
        ],
    }
```

The quote and the link are what make the issue useful to someone who wasn't there. Without them, "Send revised pricing draft" a week later is a mystery.

## Step 4: Create the issue

```python
def create_issue(item: ActionItem, project_key: str, issue_type: str = "Task") -> str:
    fields = {
        "project": {"key": project_key},
        "issuetype": {"name": issue_type},
        "summary": item.summary,
        "description": adf_description(item),
        "labels": ["from-meeting"],
    }
    if item.due_date:
        fields["duedate"] = item.due_date
    if item.priority:
        fields["priority"] = {"name": item.priority}
    if (acct := account_id_for(item.owner_email)):
        fields["assignee"] = {"id": acct}

    r = requests.post(f"{JIRA}/rest/api/3/issue",
                      json={"fields": fields}, auth=AUTH, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.json()["key"]
```

Field availability depends on the project's screen configuration. If `duedate` or `priority` aren't on the create screen, Jira rejects the request; check with `GET /rest/api/3/issue/createmeta` or simply add them to the screen.

## Step 5: Make it idempotent

Meetings get re-processed. Notes get edited. You don't want duplicate issues. Store a stable key per action item (for example a hash of meeting ID + timestamp + summary) and skip items you've already created:

```python
import hashlib, json, pathlib

STATE = pathlib.Path("created.json")
seen = json.loads(STATE.read_text()) if STATE.exists() else {}

def item_key(item: ActionItem) -> str:
    raw = f"{item.meeting_url}|{item.timestamp}|{item.summary.lower()}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]

def sync(items: list[ActionItem], project_key: str):
    for item in items:
        k = item_key(item)
        if k in seen:
            continue
        seen[k] = create_issue(item, project_key)
        print("created", seen[k], item.summary)
    STATE.write_text(json.dumps(seen, indent=2))
```

## Step 6: Keep a human in the loop

Fully automatic issue creation sounds great and produces noise. Meetings generate "action items" that were jokes, hypotheticals or things already done. A better default: **create issues only after someone presses a button** on the meeting summary, or post the proposed issues to a Slack thread for a thumbs-up first.

That's also how most notetakers that integrate with Jira work. Lynkk's [Jira integration](https://lynkk.ai/integrations/jira), for instance, creates one issue per action item, in the project and issue type you choose, when you press Send on a note.

## Where this fits in the bigger picture

Getting action items into Jira is the last mile. The earlier miles are capturing the meeting and writing minutes that hold decisions as well as tasks. For the non-code side, including whether minutes need to be verbatim, see [how product teams turn meeting minutes into Jira issues](https://lynkk.ai/blog/meeting-minutes-to-jira).

---

*Written by the Lynkk team with AI assistance. Jira Cloud REST API v3 as of October 2026.*
