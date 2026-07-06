# Release Owner Check

![Release Owner Check cover](assets/readme-cover.svg)

> Audit release ownership notes for decision maker, backup, and approval evidence

![stack](https://img.shields.io/badge/stack-Python-16a34a?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-dc2626?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-7c3aed?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-0891b2?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | release planning |
| Command | `release-owner-check` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `unknown-owner` | high | release owner missing |
| `missing-backup` | medium | backup missing |
| `missing-approval` | low | approval missing |

## Try it locally

```bash
python -m pip install -e ".[dev]"
release-owner-check examples/sample.txt
release-owner-check examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m release_owner_check --help
```
