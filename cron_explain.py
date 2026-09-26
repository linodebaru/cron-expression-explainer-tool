#!/usr/bin/env python3
"""Explain a cron expression in plain language."""

import sys

FIELDS = [
    ("minute", "0-59"),
    ("hour", "0-23"),
    ("day of month", "1-31"),
    ("month", "1-12"),
    ("day of week", "0-7, 0 and 7 are Sunday"),
]


def explain(field: str, name: str) -> str:
    if field == "*":
        return f"{name}: every"
    if "," in field:
        return f"{name}: {field}"
    if "/" in field:
        base, step = field.split("/")
        return f"{name}: every {step}, starting at {base or 'the beginning'}"
    if "-" in field:
        start, end = field.split("-")
        return f"{name}: {start} through {end}"
    return f"{name}: exactly {field}"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 cron_explain.py '*/15 9-18 * * 1-5'", file=sys.stderr)
        return 1
    parts = sys.argv[1].split()
    if len(parts) != 5:
        print("a cron expression must have 5 fields", file=sys.stderr)
        return 1
    for field, (name, _) in zip(parts, FIELDS):
        print(explain(field, name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
