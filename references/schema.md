# Normalized inventory schema

Use the smallest subset that the audit supports. Preserve blank values as unknown rather than inventing them.

| Field | Meaning |
| --- | --- |
| `source_name` | Stable label for the inventory source |
| `source_record_id` | Identifier assigned by that source |
| `canonical_id` | Cross-source work or content identifier |
| `variant` | Part, edition, language, resolution, format, or alternate recording |
| `raw_name` | Untouched filename or source title |
| `normalized_title` | Derived title used only as supporting match evidence |
| `source_url_or_path` | Original locator; redact before public sharing when restricted |
| `byte_size` | File size when available |
| `sha256` | Content hash for byte-identical file verification |
| `published_at` | Original publication time when known |
| `modified_at` | Source record or file modification time |
| `duration_seconds` | Media duration when available |
| `mime_type` | File or record media type |
| `availability` | `public`, `private`, `removed`, `missing`, or `unknown` |
| `first_seen_at` | First observation time |
| `last_checked_at` | Most recent verification time |
| `id_confidence` | `high`, `medium`, `low`, or `unresolved` |
| `match_reason` | Evidence supporting normalization or a cross-source match |

Recommended identity key: `canonical_id + variant`. Use `source_record_id` when no cross-source identifier exists. Never silently replace raw source values with normalized values.

