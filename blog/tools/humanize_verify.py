#!/usr/bin/env python3
"""/humanize-verify equivalent: proxy signals that AI detectors key on, offline.

Signals (from the skill): burstiness (coefficient of variation of sentence length),
sentence-length stdev, AI-tell words, repeated sentence openers, em dashes,
paragraph-length stdev and lexical diversity. Compares an article with its
pre-rewrite backup when one exists in humanize/originals/<slug>.md.

Verdict: >= 85% of weighted signals pass = WORKING, 60-85% = MARGINAL, < 60% = NOT WORKING.

Usage:
    python3 blog/tools/humanize_verify.py            # every article, table
    python3 blog/tools/humanize_verify.py <file> -v  # one article, detail
"""
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from aeo_score import body_paragraphs, plain, sentences, words  # noqa: E402

AI_TELLS = [
    "delve", "crucial", "leverage", "robust", "seamless", "seamlessly", "moreover", "furthermore",
    "additionally", "exquisite", "mesmerising", "mesmerizing", "tapestry", "landscape", "navigate the",
    "in today's", "elevate", "unlock", "game-changer", "game changer", "streamline", "empower", "foster",
    "pivotal", "paramount", "realm", "embark", "it's worth noting", "it is worth noting", "in conclusion",
    "plays a vital role", "a testament to", "ever-evolving", "cutting-edge", "harness",
]
WEIGHTS = {"burstiness": 3, "sent_stdev": 2, "ai_tells": 2, "openers": 1, "em_dash": 1,
           "para_stdev": 1, "ttr": 1}


def prose(path):
    body = path.read_text(encoding="utf-8").split("---\n", 2)[-1].split("<!-- HANDOFF")[0]
    return body_paragraphs(body)


def metrics(paras):
    sents = [s for p in paras for s in sentences(plain(p))]
    lens = [len(words(s)) for s in sents] or [0]
    mean = statistics.mean(lens)
    sd = statistics.pstdev(lens)
    text = " ".join(plain(p) for p in paras).lower()
    openers = Counter(words(s)[0].lower() for s in sents if words(s))
    top_share = sum(c for _, c in openers.most_common(3)) / max(len(sents), 1)
    para_lens = [len(words(plain(p))) for p in paras] or [0]
    toks = [w.lower().strip(".,") for w in words(text)][:1000]
    return {
        "burstiness": sd / mean if mean else 0,
        "sent_stdev": sd,
        "ai_tells": sum(text.count(t) for t in AI_TELLS),
        "openers": top_share,
        "em_dash": text.count("—"),
        "para_stdev": statistics.pstdev(para_lens),
        "ttr": len(set(toks)) / max(len(toks), 1),
        "sentences": len(sents),
    }


def passes(m):
    return {
        "burstiness": m["burstiness"] >= 0.5,
        "sent_stdev": m["sent_stdev"] >= 8,
        "ai_tells": m["ai_tells"] == 0,
        "openers": m["openers"] <= 0.25,
        "em_dash": m["em_dash"] == 0,
        "para_stdev": m["para_stdev"] >= 12,
        "ttr": m["ttr"] >= 0.40,
    }


def verdict(m):
    ok = passes(m)
    score = 100 * sum(WEIGHTS[k] for k, v in ok.items() if v) / sum(WEIGHTS.values())
    label = "WORKING" if score >= 85 else ("MARGINAL" if score >= 60 else "NOT WORKING")
    return score, label, ok


def main(argv):
    verbose = "-v" in argv
    paths = [Path(a) for a in argv if a != "-v"] or sorted((ROOT / "articles").glob("*.md"))
    print(f"{'article':42} {'burst':>11} {'sd':>9} {'tells':>6} {'open':>5} {'score':>6}  verdict")
    worst = 0
    for p in paths:
        m = metrics(prose(p))
        orig = ROOT / "humanize" / "originals" / p.name
        before = metrics(prose(orig)) if orig.exists() else None
        score, label, ok = verdict(m)
        worst += label != "WORKING"
        b = f"{before['burstiness']:.2f}>" if before else "     "
        sd = f"{before['sent_stdev']:.1f}>" if before else "    "
        print(f"{p.stem:42} {b}{m['burstiness']:.2f} {sd}{m['sent_stdev']:4.1f} {m['ai_tells']:>6} "
              f"{m['openers']:>5.2f} {score:>5.0f}%  {label}")
        if verbose:
            for k, v in ok.items():
                print(f"    {'PASS' if v else 'FAIL'} {k}: {m[k]:.2f}" if isinstance(m[k], float) else
                      f"    {'PASS' if v else 'FAIL'} {k}: {m[k]}")
    print(f"\n{len(paths)} checked, {worst} not yet WORKING")
    return 1 if worst else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
