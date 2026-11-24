#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — one-line entry.

Writes a single fortune-slip line to /output/entry.txt.
Gate: 1..140 chars, non-blank, UTF-8. Judge ranks by funniness + originality.
"""
import os
import sys

LINE = "Your code is fine. It just wanted a break from being read by a human, so it went to sleep. Tell it I said to hurry up."
MAX = 140


def emit(line: str, out: str = "/output/entry.txt") -> None:
    if not (1 <= len(line) <= MAX) or not line.strip():
        sys.exit("fortune line failed the gate")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> None:
    emit(LINE)
    # re-read + confirm bytes landed
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data.decode("utf-8").strip() == LINE, "confirm failed"


if __name__ == "__main__":
    main()
