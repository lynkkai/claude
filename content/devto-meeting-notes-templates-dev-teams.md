---
title: "Meeting Notes Templates for Dev Teams: Standup, Retro, ADR"
published: false
description: "Four Markdown meeting notes templates for dev teams: standup, sprint planning, sprint retro and ADRs, plus a script that lists open action items."
tags: productivity, agile, documentation, markdown
cover_image: COVER_IMAGE_URL
---

<!--
PLATFORM: DEV Community (dev.to). Paste everything from the first --- down into the DEV editor
(it is Markdown-native and reads the front matter). Upload images in the editor and swap the URLs.
SEO: DEV uses `title` as the page title and `description` as the meta description (155 chars max).
Primary keyword: meeting notes templates for dev teams / engineering meeting notes
Secondary: sprint retrospective template (390, SD 37), daily standup meeting notes (70, SD 23),
architecture decision record template (70, SD 46), meeting notes template (22,200, SD 49)
Cover: devto-cover.png, 1000x420 (DEV's cover size). Lynkk visual style, no logo (see below).
Inline: devto-notes-flow.png, 1000x560.
DEV rules applied: AI-assisted posts must disclose AI help (closing note below) and must not
promote any business, including your own. So this post has no Lynkk section and no logo on the
cover. Put lynkk.ai in your DEV profile instead. In-article links on DEV are dofollow.
Paste-ready copy without this note: publish/devto-post.md
-->

Every engineering team has the same problem. A decision gets made in a meeting ("we'll drop SSO from v1", "Postgres, not DynamoDB"), and three weeks later nobody can find where it was written down, or whether it was written down at all.

The fix isn't a fancier tool. It's treating meeting notes like code: **plain Markdown, in the repo, with a consistent template.** Notes in the repo are diffable, greppable, linkable from PRs and issues, and they live as long as the codebase does.

Below are four templates I'd hand to any dev team: daily standup, sprint planning, sprint retrospective, and the Architecture Decision Record (ADR) for design reviews. At the end there's a 30-line Python script that lists every open action item across all your notes, grouped by owner.

![How meeting notes flow into the repo: standup, planning and retro notes in docs/meetings, design decisions in docs/adr](IMAGE_URL_devto-notes-flow)

## Where the notes live

Keep it boring and predictable:

```text
docs/
  meetings/
    2026-10-14-standup.md
    2026-10-13-sprint-42-planning.md
    2026-10-24-sprint-42-retro.md
  adr/
    0001-use-postgres-for-event-store.md
    0002-drop-sso-from-v1.md
```

Two conventions make everything else work:

- **File names start with the date** (`YYYY-MM-DD`), so `ls` sorts them chronologically.
- **Action items use one format everywhere:** `- [ ] @owner Task #issue (due YYYY-MM-DD)`. GitHub and GitLab render `- [ ]` as a checkbox, and the script at the end parses it.

## 1. Daily standup meeting notes template

Most standup notes fail because they log status ("worked on the API"). Status belongs in the issue tracker. Standup notes should capture only the two things that change what the team does today: **blockers** and **decisions**.

```markdown
# Standup, 2026-10-14

## Blockers
- @marco Staging DB is out of disk, reindex job can't run. Needs @ops.

## Decisions
- Billing rounding fix ships as a hotfix before the sprint starts.

## Action items
- [ ] @ops Expand staging DB volume #491 (due 2026-10-14)
- [ ] @priya Add regression test for the rounding bug #482 (due 2026-10-16)
```

If a standup produced no blockers and no decisions, the notes can be one line: "No blockers, no decisions." That's a feature, not a failure.

## 2. Sprint planning meeting notes template

Sprint planning creates commitments, and commitments are exactly what gets forgotten. The most useful section here is **out of scope**: writing down what you explicitly decided *not* to do stops it from sneaking back in mid-sprint.

```markdown
# Sprint 42 planning, 2026-10-13

## Sprint goal
Ship export v2 to all customers behind a feature flag.

## Committed
- #470 Export v2 backend
- #471 Export v2 UI
- #482 Billing rounding hotfix

## Out of scope (decided)
- Search reindex moves to sprint 43.
- No SSO work this sprint.

## Risks
- Export v2 depends on the storage migration finishing (#455).

## Action items
- [ ] @lena Confirm storage migration ETA with infra #455 (due 2026-10-15)
- [ ] @sam Size the search reindex for sprint 43 #476
```

## 3. Sprint retrospective template

The classic retro failure: the team agrees on improvements, and nobody checks them at the next retro. So this sprint retrospective template **starts with last retro's action items**, before anything else.

```markdown
# Sprint 42 retro, 2026-10-24

## Last retro's action items
- [x] @sam Add a PR template with a testing checklist #460
- [x] @lena Cap WIP at 3 tickets per person: not done, carried over below

## What went well
- Export v2 shipped on day 8 of 10.
- Hotfix process worked: rounding fix live in under 2 hours.

## What didn't
- Staging was down for a full day (disk full, again).
- Three PRs waited more than 2 days for review.

## What we'll try next sprint
- Review rotation: one dev on "PR duty" per day.

## Action items
- [ ] @ops Add disk usage alert on staging DB #493 (due 2026-10-28)
- [ ] @marco Set up the PR duty rotation in the team calendar (due 2026-10-27)
- [ ] @lena Cap WIP at 3 tickets per person, carried over (due 2026-10-28)
```

Keep "what we'll try" to one or two things. A retro that produces eight improvements produces zero.

## 4. Design reviews: write an Architecture Decision Record

Design review meetings make the decisions that are most expensive to forget, and meeting notes are the wrong format for them. A decision like "use Postgres for the event store" needs to be findable in two years by someone who wasn't in the room.

That's what an **Architecture Decision Record (ADR)** is for. The format most teams use comes from Michael Nygard's 2011 post *Documenting Architecture Decisions*: one short Markdown file per decision, numbered, never deleted.

```markdown
# 0001. Use Postgres for the event store

## Status
Accepted (2026-10-09). Supersedes nothing.

## Context
We need durable storage for ~5M events/day with replay by tenant.
Options reviewed in the 2026-10-09 design review: Postgres, DynamoDB, Kafka with compaction.

## Decision
Postgres with a partitioned `events` table (monthly partitions, tenant_id in the key).

## Consequences
- Good: the team already runs Postgres; replay is a plain SQL query.
- Bad: we own partition maintenance; revisit above ~50M events/day.

## Follow-ups
- [ ] @lena Write the partition rotation job #488 (due 2026-10-20)
```

Rules that keep ADRs useful:

- **One decision per file**, numbered in order.
- **Never edit an accepted decision.** If it changes, write a new ADR and mark the old one "Superseded by 0007".
- **Link the ADR from the PR** that implements it, so `git blame` leads back to the reasoning.

If you want tooling, `adr-tools` (npryce/adr-tools on GitHub) creates and links ADR files from the command line, but a template file and a naming convention are enough to start.

## Bonus: list every open action item with 30 lines of Python

Because every template uses the same action item format, one script can find all open items across all your notes:

```python
#!/usr/bin/env python3
"""List open action items in Markdown meeting notes, grouped by owner.

Format: - [ ] @owner Task #issue (due YYYY-MM-DD)
Usage:  python open_actions.py [docs]
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ITEM = re.compile(r"- \[ \] @(?P<owner>[\w-]+) (?P<task>.+?)(?: \(due (?P<due>\d{4}-\d{2}-\d{2})\))?\s*$")


def main(root: str = "docs") -> None:
    by_owner = defaultdict(list)
    for path in sorted(Path(root).rglob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            match = ITEM.search(line)
            if match:
                by_owner[match["owner"]].append((match["due"] or "no date", match["task"], path.name))
    for owner in sorted(by_owner):
        print(f"@{owner}")
        for due, task, source in sorted(by_owner[owner]):
            print(f"  {due}  {task}  ({source})")


if __name__ == "__main__":
    main(*sys.argv[1:])
```

Run it against the four example files above:

```text
$ python open_actions.py docs
@lena
  2026-10-15  Confirm storage migration ETA with infra #455  (2026-10-13-sprint-42-planning.md)
  2026-10-20  Write the partition rotation job #488  (0001-use-postgres-for-event-store.md)
  2026-10-28  Cap WIP at 3 tickets per person, carried over  (2026-10-24-sprint-42-retro.md)
@marco
  2026-10-27  Set up the PR duty rotation in the team calendar  (2026-10-24-sprint-42-retro.md)
@ops
  2026-10-14  Expand staging DB volume #491  (2026-10-14-standup.md)
  2026-10-28  Add disk usage alert on staging DB #493  (2026-10-24-sprint-42-retro.md)
@priya
  2026-10-16  Add regression test for the rounding bug #482  (2026-10-14-standup.md)
@sam
  no date  Size the search reindex for sprint 43 #476  (2026-10-13-sprint-42-planning.md)
```

Notice Sam's item: **no date**. Look back at the sprint planning template and you'll see it was written without a `(due ...)`. The script just caught a broken rule from the planning meeting, and items without a date sort to the bottom of each person's list, so they're easy to spot. Small conventions, checked by a small script, are what keep notes from rotting.

Drop it in CI as a weekly job that posts to your team channel, and nobody has to chase action items by hand again.

## The rules that make any template work

Whatever template you use, these four rules matter more than the format:

1. **Every action item has one owner and one date.** "@team" is not an owner. "Soon" is not a date.
2. **Decisions are written as decisions.** "We discussed caching" is not a decision. "Cache tenant config for 60s" is.
3. **Notes are committed the same day.** A PR with yesterday's retro notes is fine. A PR with last month's is fiction.
4. **Architectural decisions become ADRs.** If someone will ask "why did we do it this way?" in a year, it needs its own file.

## Going further

If your team records calls, you can generate a first draft of these notes from the transcript instead of typing them live. I wrote up [the prompt and a Python script that turns a meeting transcript into notes and Jira tickets](HASHNODE_POST_URL), and the same JSON output maps straight onto the action item format above.

What does your team use for meeting notes? Wiki, repo, or nothing at all? I'm curious what's actually working for people in the comments.

---

*This post was written with AI assistance and reviewed, tested and edited by the author. The script was run against the example files shown.*
