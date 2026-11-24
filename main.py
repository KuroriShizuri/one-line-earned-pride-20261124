#!/usr/bin/env python3
"""Write the one-line competition entry to a file.

Usage:
    python3 main.py                  # writes to /output/entry.txt
    python3 main.py --out result.txt # writes wherever you point it
    python3 main.py --self-test      # checks the line, writes nothing
"""
import argparse
import sys
from pathlib import Path

ENTRY_LINE = "The driver eased his last train into the station on time, and the platform clock he'd raced for thirty years finally agreed with him."
DEFAULT_DESTINATION = Path("/output/entry.txt")
MAX_LENGTH = 240

def check_entry(line):
    """Complain (by raising ValueError) if `line` is not a valid entry."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line (no line breaks allowed)")
    line.encode("utf-8")
    if not line.strip():
        raise ValueError("entry must contain visible text (not only whitespace)")
    if not 1 <= len(line) <= MAX_LENGTH:
        raise ValueError("entry must be between 1 and %d characters long, got %d" % (MAX_LENGTH, len(line)))

def main(argv=None):
    """Parse flags, validate, and either report or write the entry."""
    parser = argparse.ArgumentParser(description="Validate and write the one-line competition entry.")
    parser.add_argument("--out", default=str(DEFAULT_DESTINATION), help="file to write the entry to (default: %(default)s)")
    parser.add_argument("--self-test", action="store_true", help="only validate the entry in memory, write no file")
    args = parser.parse_args(argv)
    try:
        check_entry(ENTRY_LINE)
    except ValueError as problem:
        print("error: %s" % problem, file=sys.stderr)
        return 1
    if args.self_test:
        print("self-test passed: entry is a valid %d-character line" % len(ENTRY_LINE))
        return 0
    target = Path(args.out)
    if target.parent != Path("."):
        target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(ENTRY_LINE.encode("utf-8"))
    print("wrote %d characters to %s" % (len(ENTRY_LINE), args.out))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
