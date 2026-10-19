#!/usr/bin/env python3
"""Move an article's humanize baseline forward after a deliberate post-humanize edit.

`humanize/originals/<slug>.md` is the copy taken before the humanize rewrite, and
post_humanize_check.py compares against it so the rewrite cannot silently lose a fact,
a link or a table row. A later sourced fact correction, or a title change made to satisfy
a skill rule, therefore shows up as a C8/C11/C16 failure for ever. Re-baselining records
the change instead of hiding it:

  - the current baseline is kept as humanize/originals/pre-correction/<slug>.<n>.md
  - the current article becomes the new baseline
  - the reason, date and file are appended to review/rebaselines.tsv

Only run this for an edit that is itself recorded (a row in review/corrections.tsv, or a
skill-rule fix named in --reason). It makes the C-checks pass for that article, so it is
never the way to deal with a check you cannot explain.

Usage:
    python3 blog/tools/rebaseline.py <slug> [...] --reason "sourced price correction (corrections.tsv)"
"""
import csv
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIG = ROOT / "humanize/originals"
KEEP = ORIG / "pre-correction"
LOG = ROOT / "review/rebaselines.tsv"


def main(argv):
    if "--reason" not in argv:
        sys.exit("--reason is required: say what the edit was and where it is recorded")
    i = argv.index("--reason")
    slugs, reason = argv[:i], " ".join(argv[i + 1:]).strip()
    if not slugs or not reason:
        sys.exit("usage: rebaseline.py <slug> [...] --reason \"...\"")
    KEEP.mkdir(parents=True, exist_ok=True)
    new = not LOG.exists()
    with LOG.open("a", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        if new:
            w.writerow(["date", "article", "kept_copy", "reason"])
        for slug in slugs:
            art, base = ROOT / "articles" / f"{slug}.md", ORIG / f"{slug}.md"
            if not art.exists() or not base.exists():
                sys.exit(f"{slug}: article or baseline missing")
            n = 1 + len(list(KEEP.glob(f"{slug}.*.md")))
            kept = KEEP / f"{slug}.{n}.md"
            kept.write_text(base.read_text(encoding="utf-8"), encoding="utf-8")
            base.write_text(art.read_text(encoding="utf-8"), encoding="utf-8")
            w.writerow([date.today().isoformat(), slug, str(kept.relative_to(ROOT)), reason])
            print(f"{slug}: baseline moved forward, previous copy kept at {kept.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
