"""The normalized item every source produces.

The fields are platform neutral (platform, community, url) so other sources
such as Slack or LinkedIn can feed the same pipeline later.
"""

from __future__ import annotations

from dataclasses import dataclass, field

INTENTS = (
    "high_purchase_intent",
    "problem_seeking_solution",
    "tool_recommendation",
    "comparison",
    "workflow_problem",
    "general_discussion",
    "low_relevance",
)

# P0 asks for a tool, P1 describes a pain, P2 discusses, P3 barely relevant.
PRIORITY = {
    "high_purchase_intent": 0,
    "tool_recommendation": 0,
    "comparison": 0,
    "problem_seeking_solution": 1,
    "workflow_problem": 1,
    "general_discussion": 2,
    "low_relevance": 3,
}


@dataclass
class Item:
    reddit_id: str  # fullname: t3_ for posts, t1_ for comments
    type: str  # "post" or "comment"
    username: str
    content: str
    title: str
    subreddit: str  # "r/name"
    reddit_url: str
    author_url: str
    created_at: str  # ISO 8601, UTC
    parent_post_id: str = ""
    parent_post_title: str = ""
    parent_post_url: str = ""
    parent_excerpt: str = ""
    keyword_matched: str = ""
    matched_keywords: list[str] = field(default_factory=list)
    source: str = ""  # search, thread or comment_feed
    platform: str = "reddit"

    @property
    def text(self) -> str:
        """Title and body together, for matching and scoring."""
        if self.type == "post":
            return f"{self.title}\n{self.content}"
        return self.content
