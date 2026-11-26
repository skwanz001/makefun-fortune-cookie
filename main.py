"""Fortune Cookie Funnies for Engineers — one-line fortune for a software engineer.

Writes a single fortune-cookie line (max 120 characters) to /output/entry.txt.
Standard library only.
"""

import os

FORTUNE = "The bug you cannot reproduce will reproduce the moment your manager looks over your shoulder."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = FORTUNE.strip()
    # Self-check against the gate: UTF-8 text, 1-120 chars, single line.
    assert 1 <= len(line) <= 120, f"fortune must be 1-120 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "fortune must be a single line"
    assert line == line.strip() and line, "fortune must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
