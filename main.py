#!/usr/bin/env python3
"""Store one competition line as a file.

The program checks the line first, then writes it out byte for byte:
no newline at the end, no trimming, no extras.
"""
import argparse
import sys
from pathlib import Path

LINE = "The driver eased his last train into the station on time, and the platform clock he'd raced for thirty years finally agreed with him."
TARGET = Path("/output/entry.txt")
CEILING = 240

def problem(text):
    """Return why `text` is unusable, or None when it is fine."""
    if "\n" in text or "\r" in text:
        return "a one-line entry cannot contain a line break"
    if text.strip() != text:
        return "a one-line entry cannot start or end with blank space"
    if not text:
        return "a one-line entry cannot be empty"
    if len(text) > CEILING:
        return "entry runs %d characters, past the %d cap" % (len(text), CEILING)
    return None

def run(argv=None):
    """Check the line, then write it or report the fault."""
    parser = argparse.ArgumentParser(description="Store the one-line competition entry.")
    parser.add_argument("--out", default=str(TARGET), help="where to write the line")
    parser.add_argument("--self-test", action="store_true", help="check the line only")
    opts = parser.parse_args(argv)
    fault = problem(LINE)
    if fault is not None:
        print("cannot write entry: %s" % fault, file=sys.stderr)
        return 1
    if opts.self_test:
        print("line ok: %d characters, single line" % len(LINE))
        return 0
    dest = Path(opts.out)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(LINE.encode("utf-8"))
    print("entry written: %d characters in %s" % (len(LINE), dest))
    return 0

if __name__ == "__main__":
    sys.exit(run())
