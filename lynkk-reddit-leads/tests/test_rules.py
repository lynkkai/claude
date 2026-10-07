"""The examples from the brief, scored by the rules."""

from leads.analysis.intent import rule_intent
from leads.analysis.keywords import Keyword, build_queries, match_keywords
from leads.analysis.rules import score

KW = [Keyword(k) for k in [
    "AI note taker", "AI notetaker", "AI meeting notes", "meeting transcription", "meeting notes AI",
    "voice notes", "meeting assistant", '"meeting notes" AI', "call notes",
]]
COMPETITORS = ["Otter", "Fireflies", "Granola"]


def s(text):
    return score(text, match_keywords(text, KW), COMPETITORS)


def test_high_relevance_examples():
    a = s("I've tried 5 AI meeting note takers but none of them handle Indian accents properly. Any recommendations?")
    b = s("Is there an AI tool that can automatically record my meetings and create action items?")
    c = s("I've been taking notes manually during client calls and it's becoming impossible to keep up. "
          "Is there an AI tool that can record the call and automatically give me notes and action items?")
    for r in (a, b, c):
        assert r.score >= 70, r


def test_medium_and_low_examples_rank_below_high():
    medium = s("I've started using AI for productivity and meeting notes.")
    low = s("AI note taking is going to change everything.")
    high = s("Is there an AI tool that can automatically record my meetings and create action items?")
    assert high.score > medium.score
    assert high.score > low.score
    assert low.score < 50


def test_irrelevant_notes_are_ignored():
    r = s("Learning guitar: which notes are in the C major scale? My teacher sent voice notes.")
    assert r.score < 25
    r = s("Patch notes for 2.1 are out, meeting the community tomorrow.")
    assert r.score < 25


def test_self_promotion_is_capped():
    r = s("I built an AI note taker that records your meetings and writes summaries and action items. "
          "Looking for beta testers, check it out!")
    assert r.has("promotional")
    assert r.score <= 35


def test_listicle_is_promotional():
    r = s("5 Best AI-powered Note Takers in 2026: I Tested Otter, Fireflies and Granola")
    assert r.has("promotional")


def test_alternative_request_is_a_comparison():
    text = "Looking for an alternative to Otter for meeting transcription, it got too expensive. Any suggestions?"
    r = s(text)
    assert r.has("alternatives")
    intent, _ = rule_intent(r)
    assert intent == "comparison"


def test_bots_score_zero():
    assert score("I am a bot, and this action was performed automatically.", [], username="AutoModerator").score == 0


def test_keyword_matching_handles_spelling_and_plurals():
    found = match_keywords("Which AI note-takers do you use for Zoom call notes?", KW)
    assert "AI note taker" in found
    assert "AI notetaker" not in found  # same keyword spelled differently counts once
    assert "call notes" in found
    assert match_keywords("AI helps me write meeting notes", KW) == ['"meeting notes" AI']


def test_queries_pack_phrases_and_isolate_combinations():
    qs = build_queries(KW)
    combo = [q for q in qs if q.keywords == ['"meeting notes" AI']]
    assert combo and combo[0].q == '"meeting notes" AI'
    packed = [q for q in qs if len(q.keywords) > 1]
    assert packed and ' OR ' in packed[0].q
    assert all(len(q.q) <= 400 for q in qs)


def test_ai_dictation_requests_score_high():
    a = s("Is there a good AI dictation app for Mac? Built-in dictation can't keep up with me. Any recommendations?")
    b = s("Looking for a speech-to-text app that types wherever my cursor is. Wispr Flow alternative?")
    for r in (a, b):
        assert r.has("ai_note_intent"), r
        assert r.score >= 60, r
    assert b.has("alternatives")


def test_ai_note_maker_suggestion_request_scores_high():
    r = s("Can anyone suggest a good AI note maker? I need something that turns my calls into notes.")
    assert r.has("ai_note_intent") and r.has("asks_for_tool")
    assert r.score >= 50, r


def test_ai_note_disclaimer_is_not_note_taking():
    r = s("(AI note: The AI helped craft my question.) Should I withdraw my retirement savings to pay off debt?")
    assert not r.has("ai_note_intent")
    assert r.score < 25
