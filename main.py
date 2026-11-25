#!/usr/bin/env python3
"""One Line, Big Laugh — entry program.

Writes a single original funny line (max 200 characters) to
/output/entry.txt. The line is a self-contained joke: no title,
no setup, no explanation.
"""

import os

LINE = "I bought a self-help book and it filed a restraining order against my excuses."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """Gate: entry must be UTF-8 text of 1-200 characters, a single
    line, and not only whitespace. Returns the line unchanged when
    it passes, otherwise raises ValueError."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(line)
        )
    line.encode("utf-8")  # must be valid UTF-8 text
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
