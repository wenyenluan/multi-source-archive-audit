#!/usr/bin/env python3
"""Conservatively compare two CSV inventories by canonical ID and variant."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path, help="Baseline CSV inventory")
    parser.add_argument("comparison", type=Path, help="Comparison CSV inventory")
    parser.add_argument("--output", type=Path, required=True, help="Result CSV path")
    parser.add_argument("--id-column", default="canonical_id")
    parser.add_argument("--variant-column", default="variant")
    return parser.parse_args()


def load(path: Path, id_column: str, variant_column: str) -> dict[tuple[str, str], list[dict[str, str]]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        if id_column not in fields:
            raise SystemExit(f"{path}: missing required column {id_column!r}")
        for row_number, row in enumerate(reader, start=2):
            canonical_id = (row.get(id_column) or "").strip()
            variant = (row.get(variant_column) or "").strip() if variant_column in fields else ""
            if not canonical_id:
                canonical_id = f"__UNRESOLVED_ROW_{row_number}"
            grouped[(canonical_id, variant)].append(row)
    return grouped


def main() -> None:
    args = parse_args()
    baseline = load(args.baseline, args.id_column, args.variant_column)
    comparison = load(args.comparison, args.id_column, args.variant_column)
    keys = sorted(set(baseline) | set(comparison))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "canonical_id", "variant", "result", "baseline_records", "comparison_records", "note"
        ])
        writer.writeheader()
        for canonical_id, variant in keys:
            left = len(baseline.get((canonical_id, variant), []))
            right = len(comparison.get((canonical_id, variant), []))
            unresolved = canonical_id.startswith("__UNRESOLVED_ROW_")
            result = "uncertain" if unresolved else "matched" if left and right else "baseline_only" if left else "comparison_only"
            note = "Missing canonical ID; manual review required" if unresolved else "Exact canonical ID and variant comparison"
            writer.writerow({
                "canonical_id": "" if unresolved else canonical_id,
                "variant": variant,
                "result": result,
                "baseline_records": left,
                "comparison_records": right,
                "note": note,
            })


if __name__ == "__main__":
    main()

