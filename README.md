# release-owner-check

> Audit release ownership notes for decision maker, backup, and approval evidence.

## Review card Overview

Audit release ownership notes for decision maker, backup, and approval evidence. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts release owner note. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
release-owner-check examples/sample.txt
release-owner-check examples/sample.txt --json --fail-on medium
python -m release_owner_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `unknown-owner` | high | release owner missing |
| `missing-backup` | medium | backup missing |
| `missing-approval` | low | approval missing |

## Validation Notes

```bash
ruff check .
pytest
python -m release_owner_check --help
```

Example risky input:

```text
release owner unknown backup none approval missing
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
