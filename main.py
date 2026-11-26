#!/usr/bin/env python3
"""Funniest Lost Sock Status Update - make.fun entry.

Writes a single status update, in the voice of a lost sock, to
/output/entry.txt. Deterministic: fixed text, no randomness, no time,
no network. Output has no trailing newline and is 1-120 characters.
"""

import os

ENTRY = "Day 23 behind the dryer. My pair moved in with a slipper. I hope they're both itchy."

MIN_LEN = 1
MAX_LEN = 120


def main():
    text = ENTRY
    assert MIN_LEN <= len(text) <= MAX_LEN, (
        f"entry length {len(text)} outside {MIN_LEN}-{MAX_LEN}"
    )
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
