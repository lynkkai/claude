"""Rule-based relevance score (0 to 100).

This is the cheap first pass. It decides what Claude Code reviews, and it is
the score used for anything Claude Code hasn't reviewed yet. Weights follow
the brief:

  +30 explicit AI note-taking intent      -30 irrelevant context
  +25 asks for a tool                     -20 keyword only incidental
  +20 describes a clear pain point        -20 promotional or self-promotional
  +15 meeting transcription               -15 duplicate content
  +15 meeting summaries
  +10 action items
  +10 recording meetings or calls
  +10 asks for alternatives
  +10 asks for recommendations

Self-promotion is also capped at 35: people launching their own note taker
are not leads, however many keywords they use. Claude Code can still rescue
a false positive during review.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .keywords import normalize


def _rx(*patterns: str) -> re.Pattern:
    return re.compile("|".join(f"(?:{p})" for p in patterns), re.I)


AI_NOTE = _rx(
    r"\b(ai|a\.i\.|gpt|llm|chatgpt|claude|gemini|automatic(ally)?|auto)\b[^.?!\n]{0,40}\b(note ?tak\w*|note ?mak\w*|notes|minutes|transcri\w+|summar\w+|scribe|meeting assistant|recorder)",
    r"\bnote ?tak(er|ers)\b",
    r"\bmeeting (assistant|bot|recorder|copilot|scribe)s?\b",
    r"\b(note|meeting)s? (app|tool|software)\b[^.?!\n]{0,40}\b(ai|transcri\w+|record\w*)",
    r"\bai (scribe|notes?|note ?taker|recorder|transcription)\b",
    r"\b(ai|automatic(ally)?|auto)\b[^.?!\n]{0,40}\brecord\w*\b[^.?!\n]{0,20}\b(meetings?|calls?|conversations?|interviews?)\b",
)

ASKS_TOOL = _rx(
    r"\b(any|anyone|what|which|is there|are there|does anyone|do you guys|can anyone)\b[^.?!\n]{0,90}\b(tool|app|apps|software|service|solution|product|plugin|extension|bot|recommend\w*|suggest\w*|use|using)\b[^.!\n]{0,80}\?",
    r"\blooking for (a|an|some|good|the best|recommendations?)?\b[^.?!\n]{0,60}\b(tool|app|software|service|solution|way|recommend\w*|note ?tak\w*|transcri\w+|assistant|recorder)",
    r"\b(need|want) (a|an|some) (good |reliable |simple |cheap |free )?(tool|app|software|service|ai|way)\b",
    r"\bbest\b[^.?!\n]{0,40}\b(tool|app|software|note ?tak\w*|transcri\w+|assistant|recorder|ai)\b[^.!\n]{0,60}\?",
    r"\b(what|which)\b[^.?!\n]{0,30}\b(do you|are you|should i)\b[^.?!\n]{0,20}\b(use|using|recommend|pick|choose)\b",
)

PAIN = _rx(
    r"\bmanual(ly)? (take|taking|writ\w+|typ\w+)\b",
    r"\b(taking|take|write|writing|typing) notes?\b[^.?!\n]{0,40}\b(manual\w*|hard|impossible|exhausting|annoying|tedious|time|distract\w*|keep up|while)",
    r"\b(can'?t|cannot|struggl\w+|hard to|impossible to|unable to) (keep up|focus|remember|listen|pay attention|take notes|follow)",
    r"\b(forget|forgot|forgetting|lose track|losing track|lost track|miss(ed|ing)?) (the |all |important |key |what )?(action items?|follow ?ups?|details|decisions|what was said|important|things|track)",
    r"\b(hate|tired of|sick of|frustrat\w+|annoy\w+|pain(ful)?|waste of time|wasting time|takes forever|so much time)\b",
    r"\b(poor|bad|terrible|awful|inaccurate|wrong|garbage|useless) (transcri\w+|summar\w+|notes|accuracy)",
    r"\b(accents?|hinglish|multilingual|code ?switch\w*|non native|other languages?)\b",
    r"\b(searchable|search through|find what|look back|can'?t find)\b[^.?!\n]{0,40}\b(meetings?|calls?|notes|conversations?)",
    r"\b(problem|issue|struggle|challenge) (is|with)\b",
)

TRANSCRIPTION = _rx(r"\btranscri(be|bes|bing|ption|ptions|pt|pts|ber)\b")
SUMMARIES = _rx(r"\bsummar(y|ies|ize|ise|izes|ises|izing|ising|ization|isation)\b", r"\bminutes of (the )?meeting\b", r"\bmeeting minutes\b")
ACTION_ITEMS = _rx(r"\baction items?\b", r"\bfollow ?ups?\b", r"\bto ?dos?\b", r"\bnext steps\b")
RECORDING = _rx(
    r"\brecord(s|ed|ing)?\b[^.?!\n]{0,30}\b(meetings?|calls?|conversations?|zoom|teams|google meet|interviews?|sessions?)\b",
    r"\b(meeting|call|zoom|teams) recordings?\b",
)
ALTERNATIVES = _rx(
    r"\balternatives? (to|for)\b",
    r"\b(switch|switching|switched|moving|move) (away )?from\b",
    r"\breplace(ment)? for\b",
    r"\b(vs\.?|versus)\b",
    r"\bcompared? (to|with)\b",
    r"\bcheaper than\b",
)
RECOMMENDATIONS = _rx(
    r"\brecommend(ation|ations|ed)?\b",
    r"\bsuggestions?\b",
    r"\badvice\b",
    r"\bwhat (do|are) you (guys |all )?(use|using)\b",
    r"\bany (tips|ideas|thoughts)\b",
)

IRRELEVANT = _rx(
    r"\b(patch|release|liner|tasting|fragrance|scent|show|lecture|study|sticky|post ?it|doctor'?s|sick|bank|cliff|field|voice) notes?\b(?![^.?!\n]{0,40}\b(ai|transcri\w+|meeting|summar\w+)\b)",
    r"\bbanknotes?\b",
    r"\b(music|musical|sheet music|guitar|piano|chord|chords|scale|melody)\b[^.?!\n]{0,40}\bnotes?\b",
    r"\bnotes?\b[^.?!\n]{0,40}\b(perfume|cologne|wine|coffee|whisky|whiskey)\b",
    r"\bsend(ing)? (me |him |her |a )?voice notes?\b",
    r"\bwhatsapp voice notes?\b",
)

PROMO = _rx(
    r"\bi('?ve| have)? (just )?(built|made|created|launched|developed|shipped|released)\b",
    r"\bwe('?ve| have)? (just )?(built|made|created|launched|developed|shipped|released)\b",
    r"\b(we are|we're|i am|i'm) (building|launching|the (dev|developer|founder|co ?founder|maker|creator))\b",
    r"\b(my|our) (own )?(app|startup|saas|extension)\b",
    r"\bwe built\b|\bi built\b",
    r"\b(co ?founder|founder) (of|here)\b",
    r"\bcheck (it|us|this) out\b",
    r"\b(waitlist|beta testers?|early access|promo code|discount code|coupon|lifetime deal|ltd)\b",
    r"\b\d{1,2} ?% off\b",
    r"\b(dm|message) me\b",
    r"\b(link|links) in (bio|comments?|profile)\b",
    r"^\s*\[(freemium|free|paid|showcase|promo|launch)\]",
    r"\bi tested\b[^.?!\n]{0,60}\b(best|top)\b",
    r"\b(best|top)\b[^.?!\n]{0,60}\bi (tested|tried|compared|reviewed)\b",
    r"\b\d+ (best|top)\b",
    r"\b(top|best) \d+ (ai )?\w+ (tools|apps|note ?takers)\b",
    r"apps\.apple\.com|play\.google\.com|producthunt\.com",
)

PROMO_CAP = 35

BOT_AUTHORS = {"automoderator", "[deleted]", "sneakpeekbot", "remindmebot", "savevideo"}


@dataclass
class RuleResult:
    score: int
    signals: list[str] = field(default_factory=list)

    def has(self, name: str) -> bool:
        return name in self.signals


def score(
    text: str,
    matched_keywords: list[str],
    competitors: list[str] | None = None,
    is_duplicate: bool = False,
    in_relevant_thread: bool = False,
    username: str = "",
) -> RuleResult:
    signals: list[str] = []
    total = 0
    t = normalize(text)

    def add(name: str, points: int, hit: bool):
        nonlocal total
        if hit:
            signals.append(name)
            total += points

    if username.lower() in BOT_AUTHORS or "i am a bot" in t:
        return RuleResult(0, ["bot"])

    competitor_hit = any(
        re.search(rf"(?<![a-z0-9]){re.escape(normalize(c))}(?![a-z0-9])", t) for c in (competitors or [])
    )
    ai_note = bool(AI_NOTE.search(t)) or (competitor_hit and bool(re.search(r"\bnotes?|transcri|meeting", t)))
    asks = bool(ASKS_TOOL.search(t))
    alternatives = bool(ALTERNATIVES.search(t)) and (competitor_hit or ai_note)

    add("ai_note_intent", 30, ai_note)
    add("asks_for_tool", 25, asks)
    add("pain_point", 20, bool(PAIN.search(t)))
    add("transcription", 15, bool(TRANSCRIPTION.search(t)))
    add("summaries", 15, bool(SUMMARIES.search(t)))
    add("action_items", 10, bool(ACTION_ITEMS.search(t)))
    add("recording", 10, bool(RECORDING.search(t)))
    add("alternatives", 10, alternatives)
    add("recommendations", 10, bool(RECOMMENDATIONS.search(t)))
    add("relevant_thread", 10, in_relevant_thread)

    core = ai_note or any(s in signals for s in ("transcription", "summaries", "recording")) or bool(
        re.search(r"\b(meeting|meetings|call|calls|zoom|teams|google meet)\b", t)
    )
    add("irrelevant_context", -30, bool(IRRELEVANT.search(t)) and not ai_note)
    add("incidental_keyword", -20, not core or (not matched_keywords and not in_relevant_thread and not ai_note))
    add("promotional", -20, bool(PROMO.search(text)) or bool(PROMO.search(t)))
    add("duplicate", -15, is_duplicate)

    total = max(0, min(100, total))
    if "promotional" in signals:
        total = min(total, PROMO_CAP)
    return RuleResult(total, signals)
