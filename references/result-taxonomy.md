# Result taxonomy

Assign one primary result to every compared identity.

| Result | Definition |
| --- | --- |
| `matched` | The same canonical identity and variant are supported in both sources |
| `baseline_only` | Present in the declared baseline but not found in the comparison source |
| `comparison_only` | Present in the comparison source but not found in the baseline |
| `variant_incomplete` | The canonical work exists in both sources but expected variants differ |
| `conflict` | Stable evidence disagrees, such as one ID attached to incompatible titles or dates |
| `uncertain` | Evidence is insufficient or ambiguous |
| `out_of_scope` | Known record intentionally excluded by the audit definition |

Do not relabel `baseline_only` as definitively missing when the comparison listing is partial. Report it as "not observed in the scanned comparison inventory."

Minimum report sections:

1. Audit question and source roles
2. Collection time and coverage limits
3. Normalization and matching rules
4. Totals with denominators
5. Results by taxonomy
6. Conflicts and uncertain records
7. Validation sample
8. Safe next actions

