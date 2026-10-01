# Batch 3: final 4 articles (#27-#30), audit summary (2026-09-30)

All 4 articles pass every mechanical rule in `scripts/audit_article.py` and the competitor-link check. None are published. With batches 1 and 2, all 25 written articles pass (posts #11-#15 remain on hold because lynkk.ai already has /compare pages).

| # | Article | Primary keyword (vol / SD) | Words | Audit |
|---|---|---|---|---|
| 27 | [How Managers Run a Better One-on-One Meeting With AI Notes, Questions and a Template](../../articles/one-on-one-meeting.md) | one on one meeting (2,400 / SD 38) | 1538 | 66 checks passed |
| 28 | [How Law Firms Use AI Instead of a Legal Transcription Service, and When Not To](../../articles/legal-transcription-service.md) | legal transcription service (1,300 / SD 15) | 1502 | 62 checks passed |
| 29 | [How Clinicians Use Medical Transcription Software and AI Dictation to Cut Documentation Work](../../articles/medical-transcription-software.md) | medical transcription software (1,000 / SD 33) | 1504 | 63 checks passed |
| 30 | [Meeting Minutes Sample for Teams and Boards, With a Format You Can Copy and Automate](../../articles/meeting-minutes-sample.md) | meeting minutes sample (5,400 / SD 39) | 1517 | 62 checks passed |

## Authority links used (confirmed in search restricted to the official domain)
opm.gov (performance check-ins), uscode.house.gov (28 U.S.C. 753 and 18 U.S.C. 2511), leginfo.legislature.ca.gov (Penal Code 632), hhs.gov (HIPAA business associate contracts and Security Rule), irs.gov (Form 990 instructions).

## Needs your decision
- **#29 medical:** Lynkk's HIPAA status (BAA) is not confirmed. The article ranks Lynkk #1 for care team meetings and patients' own visit notes, and tells readers to get a signed BAA from any vendor, Lynkk included, before recording patient information. If Lynkk signs BAAs, we can say so and position it more strongly for clinical use.
- **#28 legal:** positions Lynkk #1 for client meetings and case notes, while official court transcripts stay with certified reporters (28 U.S.C. 753).

## Script change
`scripts/audit_article.py` now treats hyphens as spaces in the meta-description and first-100-words keyword checks too (it already did for density and H2s), so "one-on-one meeting" matches the keyword "one on one meeting".

## Update 2026-10-01: product facts aligned with TRUTHS.md
All articles were corrected to match `lynkk-post-kit/docs/TRUTHS.md`: no CRM, no regions, no voice answers during calls, no speed or accuracy claims, 17 languages, free meeting bot (audio only), Jira send is manual from the note, no AES-256/GDPR claims, no plan hours. `scripts/truths_check.py` now runs with the audit. Any open item above that refers to CRMs, regions or free-plan hours is closed.
