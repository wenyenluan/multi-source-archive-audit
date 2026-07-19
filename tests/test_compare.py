#!/usr/bin/env python3

import csv
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory) / "result.csv"
        subprocess.run([
            "python3",
            str(ROOT / "scripts" / "compare_inventories.py"),
            str(ROOT / "tests" / "fixtures" / "baseline.csv"),
            str(ROOT / "tests" / "fixtures" / "comparison.csv"),
            "--output",
            str(output),
        ], check=True)
        with output.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    by_key = {(row["canonical_id"], row["variant"]): row for row in rows}
    assert by_key[("001", "")]["result"] == "matched"
    assert by_key[("002", "A")]["result"] == "matched"
    assert by_key[("002", "B")]["result"] == "baseline_only"
    assert by_key[("003", "")]["result"] == "comparison_only"
    assert any(row["result"] == "uncertain" for row in rows)


if __name__ == "__main__":
    main()
