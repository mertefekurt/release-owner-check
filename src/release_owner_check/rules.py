from __future__ import annotations

from release_owner_check.models import Rule

PROJECT_NAME = 'release-owner-check'
SUMMARY = 'Audit release ownership notes for decision maker, backup, and approval evidence.'
SAMPLE_RISK = 'release owner unknown backup none approval missing'
SAMPLE_CLEAN = 'release owner platform backup sre approval CAB-42'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='unknown-owner',
        severity='high',
        pattern='owner\\s+(unknown|none|missing)',
        message='release owner missing',
        recommendation='assign release owner',
    ),
    Rule(
        code='missing-backup',
        severity='medium',
        pattern='backup\\s+(none|missing|unknown)',
        message='backup missing',
        recommendation='assign backup owner',
    ),
    Rule(
        code='missing-approval',
        severity='low',
        pattern='approval\\s+(missing|none|unknown)',
        message='approval missing',
        recommendation='record approval evidence',
    ),
)
