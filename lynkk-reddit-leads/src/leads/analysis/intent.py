"""Rule-based intent, used until Claude Code reviews an item."""

from __future__ import annotations

from ..models import PRIORITY
from .rules import RuleResult

BASE_INTENT_SCORE = {
    "high_purchase_intent": 85,
    "tool_recommendation": 75,
    "comparison": 75,
    "problem_seeking_solution": 65,
    "workflow_problem": 55,
    "general_discussion": 35,
    "low_relevance": 10,
}


def rule_intent(r: RuleResult) -> tuple[str, int]:
    if r.has("bot") or r.has("promotional") or r.has("irrelevant_context") or r.score < 25:
        intent = "low_relevance"
    elif r.has("asks_for_tool") and r.has("alternatives"):
        intent = "comparison"
    elif r.has("asks_for_tool") and r.has("ai_note_intent"):
        intent = "high_purchase_intent"
    elif r.has("asks_for_tool") or (r.has("recommendations") and r.has("ai_note_intent")):
        intent = "tool_recommendation"
    elif r.has("pain_point") and (r.has("ai_note_intent") or r.has("transcription") or r.has("recording")):
        intent = "problem_seeking_solution"
    elif r.has("pain_point"):
        intent = "workflow_problem"
    else:
        intent = "general_discussion"
    base = BASE_INTENT_SCORE[intent]
    # Nudge by how strong the rest of the evidence is.
    score = round(base * 0.7 + r.score * 0.3)
    return intent, max(0, min(100, score))


def rank(rows: list[dict]) -> list[dict]:
    """Priority first, then relevance, intent strength, newest."""
    rows = sorted(rows, key=lambda r: r.get("created_at") or "", reverse=True)
    return sorted(
        rows,
        key=lambda r: (PRIORITY.get(r.get("intent"), 3), -(r.get("relevance_score") or 0), -(r.get("intent_score") or 0)),
    )
