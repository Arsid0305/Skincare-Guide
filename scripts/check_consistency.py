#!/usr/bin/env python3
"""Consistency checker for Skincare-Guide — runs as CI gate in automerge.yml."""

import argparse
import sys
from pathlib import Path

errors = []


def fail(msg):
    errors.append(msg)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root to validate (default: current directory)",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()

    # 1. CLAUDE.md: no dev branch references (workflow is claude/... -> main directly)
    try:
        claude_md = (root / "CLAUDE.md").read_text()
        if any(pat in claude_md for pat in ["→ dev", "targets dev", "into dev", "promote.yml"]):
            fail("CLAUDE.md: references 'dev' branch or 'promote.yml' — workflow is claude/... → main directly")
    except OSError as exc:
        fail(f"Cannot read CLAUDE.md: {exc}")

    # 2. automerge.yml: uses explicit branches allowlist, not branches-ignore
    try:
        automerge = (root / ".github" / "workflows" / "automerge.yml").read_text()
        if "branches-ignore" in automerge:
            fail("automerge.yml: uses 'branches-ignore' — should use explicit branches: [claude/**, cursor/**]")
        if "claude/**" not in automerge:
            fail("automerge.yml: missing 'claude/**' in branches filter")
        if "cursor/**" not in automerge:
            fail("automerge.yml: missing 'cursor/**' in branches filter")
    except OSError as exc:
        fail(f"Cannot read .github/workflows/automerge.yml: {exc}")

    # 3. No promote.yml (obsolete two-stage flow removed)
    if (root / ".github" / "workflows" / "promote.yml").exists():
        fail(".github/workflows/promote.yml: obsolete file — two-stage flow removed, delete it")

    if errors:
        print("CONSISTENCY ERRORS:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("Consistency check passed.")


if __name__ == "__main__":
    main()
