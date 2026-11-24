#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — one-line entry.

Writes a single fortune-slip line (<= 140 chars, UTF-8, non-blank) to
/output/entry.txt. The judge picks the funnier, more original line.
"""
import os

LINE = "Your code is fine. It just wanted a break from being read by a human, so it went to sleep. Tell it I said to hurry up."


def main() -> None:
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    assert 1 <= len(LINE) <= 140, "fortune line out of range"
    assert LINE.strip() == LINE, "line must be non-blank"
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
