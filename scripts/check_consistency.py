#!/usr/bin/env python3
"""Consistency checker for Skincare-Guide — runs as CI gate in automerge.yml."""

import sys
from pathlib import Path

errors = []


def fail(msg):
    errors.append(msg)


claude_md = Path("CLAUDE.md").read_text()
automerge = Path(".github/workflows/automerge.yml").read_text()

# 1. CLAUDE.md: no dev branch references (workflow is claude/... -> main directly)
if any(pat in claude_md for pat in ["→ dev", "targets dev", "into dev", "promote.yml"]):
    fail("CLAUDE.md: references 'dev' branch or 'promote.yml' — workflow is claude/... → main directly")

# 2. automerge.yml: uses explicit branches allowlist, not branches-ignore
if "branches-ignore" in automerge:
    fail("automerge.yml: uses 'branches-ignore' — should use explicit branches: [claude/**, cursor/**]")
if "claude/**" not in automerge:
    fail("automerge.yml: missing 'claude/**' in branches filter")
if "cursor/**" not in automerge:
    fail("automerge.yml: missing 'cursor/**' in branches filter")

# 3. No promote.yml (obsolete two-stage flow removed)
if Path(".github/workflows/promote.yml").exists():
    fail(".github/workflows/promote.yml: obsolete file — two-stage flow removed, delete it")

if errors:
    print("CONSISTENCY ERRORS:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("Consistency check passed.")
