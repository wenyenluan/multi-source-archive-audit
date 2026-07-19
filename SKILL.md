---
name: multi-source-archive-audit
description: Reconcile file or content inventories from local disks, cloud drives, websites, databases, and media platforms while preserving provenance, variants, uncertainty, and source limits. Use when Codex needs to find missing archive items, compare collections, distinguish canonical records from physical files, detect incomplete variants, or produce an evidence-backed gap report without treating filenames or item counts as proof.
---

# Multi-source Archive Audit

Reconcile inventories without deleting, downloading, uploading, renaming, or publishing content unless the user separately authorizes those actions.

## Workflow

1. Define the audit question and source roles.
   - Name the baseline, comparison sources, and desired completeness standard.
   - Record whether each source is authoritative, derivative, partial, or only a discovery lead.
   - Treat source-of-truth as field-specific when necessary: one source may own titles while another owns files.

2. Establish read boundaries before collecting data.
   - Record pagination, row caps, inaccessible folders, nested folders, authentication boundaries, rate limits, and scan time.
   - Never describe a capped or partial listing as complete.
   - Stop repeated requests when a platform returns throttling, verification, or access errors.

3. Export one immutable raw inventory per source.
   - Preserve the original identifier, filename or title, URL or path, size, timestamp, media type, and source name.
   - Do not normalize destructively. Keep raw values beside derived fields.
   - Remove secrets and private URLs before sharing reports.

4. Normalize records into the schema in [references/schema.md](references/schema.md).
   - Separate `canonical_id` from `variant`.
   - Assign a confidence level and reason to every inferred identifier.
   - Send ambiguous records to manual review instead of forcing a match.

5. Compare in evidence order.
   - Prefer stable platform IDs or canonical IDs.
   - Then use explicit variant identity.
   - Use hashes for byte-identical files.
   - Use normalized titles, dates, sizes, and durations only as supporting evidence.
   - Never use equal counts or similar filenames as proof of equality.

6. Classify every result using [references/result-taxonomy.md](references/result-taxonomy.md).
   - Keep missing records, extra files, incomplete variants, conflicts, and uncertain matches separate.
   - State the denominator and coverage for every count.

7. Validate high-impact findings.
   - Recheck a sample of matches and every deletion-like or publication-impacting conclusion.
   - Prefer false uncertainty over a false claim that content is missing or duplicated.

8. Deliver an evidence-backed report.
   - Include scope, scan timestamps, source limitations, matching rules, totals, exception tables, unresolved questions, and safe next actions.
   - Label facts, source claims, and analyst inference separately.
   - Describe results as a lower bound when any relevant source is capped or incomplete.

## Deterministic helper

Use `scripts/compare_inventories.py` when inventories are CSV files with stable IDs. Run `python3 scripts/compare_inventories.py --help` for arguments. The helper intentionally produces conservative exact-ID results; investigate fuzzy title matching separately.

## Guardrails

- Do not delete or merge files during an audit.
- Do not invent source URLs, IDs, variants, or completeness claims.
- Do not flatten variants such as parts, languages, editions, resolutions, or alternate recordings into one file.
- Do not expose private paths, signed URLs, credentials, or restricted collection names in a public report.
- Do not retry aggressively after rate limiting or anti-bot responses.
- Do not turn `unknown` into `missing` merely to make totals reconcile.

