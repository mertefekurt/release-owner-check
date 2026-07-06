![Release Owner Check cover](assets/readme-cover.svg)

# Release Owner Check

> Audit release ownership notes for decision maker, backup, and approval evidence

This is a review desk for release planning. The useful part is not a dashboard; it is the tiny repeatable moment where vague records become specific findings.

## Finding catalog for `release-owner-check`

| Finding | Level | Why it matters |
| --- | --- | --- |
| `unknown-owner` | high | release owner missing |
| `missing-backup` | medium | backup missing |
| `missing-approval` | low | approval missing |

## Try the sample

```bash
git clone https://github.com/mertefekurt/release-owner-check.git
cd release-owner-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

```bash
release-owner-check examples/sample.txt
release-owner-check examples/sample.txt --json
```

## Reading the output

- Markdown is meant for humans reviewing a change.
- JSON is meant for CI, scripts, or saved reports.
- `--fail-on` lets the repo decide how strict a gate should be.
