"""Turn a meeting transcript into Jira tickets.

Usage:
    python meeting_to_jira.py transcript.txt --meeting-date 2026-10-13          # dry run
    python meeting_to_jira.py transcript.txt --meeting-date 2026-10-13 --create # create issues

Environment:
    ANTHROPIC_API_KEY   Claude API key
    JIRA_BASE_URL       e.g. https://your-team.atlassian.net
    JIRA_EMAIL          Atlassian account email
    JIRA_API_TOKEN      https://id.atlassian.com/manage-profile/security/api-tokens
    JIRA_PROJECT_KEY    e.g. ENG
"""

import argparse
import os
import sys
from typing import Literal, Optional

import anthropic
import requests
from pydantic import BaseModel, Field


# --- 1. The shape we want back from the model -------------------------------

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


SYSTEM_PROMPT = """You extract action items from meeting transcripts for a Jira backlog.

Only include an item when someone clearly commits to doing something, or the group clearly
assigns it. Ideas, opinions and "we should think about" remarks are not action items.
Never invent an owner or a due date: use null when the transcript does not say.
Resolve relative dates ("Friday", "next week") using the meeting date you are given.
Every item must quote the transcript line it came from."""


# --- 2. Extract action items with Claude -------------------------------------

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
        sys.exit("The model declined this transcript. Review it and try again.")
    if response.stop_reason == "max_tokens":
        sys.exit("Output was cut off. Split the transcript into smaller parts.")

    return response.parsed_output.items


# --- 3. Jira helpers ---------------------------------------------------------

JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
JIRA_AUTH = (os.environ.get("JIRA_EMAIL", ""), os.environ.get("JIRA_API_TOKEN", ""))


def find_account_id(name: str) -> Optional[str]:
    """Jira assigns by accountId, not by name, so look the person up."""
    resp = requests.get(
        f"{JIRA_BASE_URL}/rest/api/3/user/search",
        params={"query": name},
        auth=JIRA_AUTH,
        timeout=30,
    )
    resp.raise_for_status()
    users = [u for u in resp.json() if u.get("accountType") == "atlassian"]
    # Only assign when the match is unambiguous.
    return users[0]["accountId"] if len(users) == 1 else None


def to_adf(*paragraphs: str) -> dict:
    """Jira Cloud API v3 expects descriptions in Atlassian Document Format."""
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": p}]}
            for p in paragraphs if p
        ],
    }


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


# --- 4. Put it together ------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript")
    parser.add_argument("--meeting-date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--create", action="store_true", help="Create issues (default is a dry run)")
    args = parser.parse_args()

    with open(args.transcript, encoding="utf-8") as f:
        transcript = f.read()

    items = extract_action_items(transcript, args.meeting_date)
    print(f"Found {len(items)} action item(s):\n")
    for i, item in enumerate(items, 1):
        print(f"{i}. [{item.priority}] {item.summary}")
        print(f"   owner: {item.owner_name or 'unassigned'}   due: {item.due_date or 'none'}")
        print(f'   source: "{item.source_quote}"\n')

    if not args.create:
        print("Dry run. Re-run with --create to open these in Jira.")
        return

    project_key = os.environ["JIRA_PROJECT_KEY"]
    for item in items:
        print("Created", create_issue(item, project_key, args.meeting_date))


if __name__ == "__main__":
    main()
