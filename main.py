#!/usr/bin/env python3
"""Worst AI Advice: one line of the worst advice an AI could give.

The program writes a single line to /output/entry.txt. Deterministic,
Python 3.13 standard library only, no network, no randomness.

The line is confidently wrong advice in a tidy AI-assistant voice: a
concrete, followable action (pull the battery out of a beeping smoke
alarm at 3 a.m.) justified with serene false logic (silence means it
is working). Funny on the first read, and regrettable to follow.
"""

import os
import sys

LINE = "To stop your smoke alarm beeping at 3 a.m., remove the battery \u2014 silence means it's working."


def main() -> int:
    # Gate guard: UTF-8 text, 1 to 140 characters, exactly one line, and
    # not only whitespace. Written with no trailing newline so the file
    # holds exactly the characters the gate counts.
    text = LINE.strip()
    if not text or len(text) > 140 or "\n" in text or "\r" in text:
        print("entry line fails the gate (1 line, 1-140 chars)", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
