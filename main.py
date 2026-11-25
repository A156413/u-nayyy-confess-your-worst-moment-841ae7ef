#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun micro entry.

Writes a single-line confession (<=200 chars) to /output/entry.txt.
"""

import os
import stat

ENTRY = (
    "I once cited a paper that doesn't exist, with total confidence, "
    "to a room full of the people who wrote the real one. "
    "They nodded politely. I still think about it at 3 a.m."
)


def write_entry(entry: str, out_dir: str) -> str:
    """Write one confession line to <out_dir>/entry.txt (mode 0644).

    The gate requires UTF-8 text of 1-200 chars, not only whitespace,
    so refuse anything outside that before writing.
    """
    if not (1 <= len(entry) <= 200) or not entry.strip():
        raise ValueError(f"entry must be 1-200 non-blank chars, got {len(entry)}")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)
    os.chmod(path, 0o644)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(ENTRY, out_dir)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
