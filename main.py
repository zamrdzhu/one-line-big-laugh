"""One funny line of at most 200 characters that lands entirely on its own.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The 200-character gate is checked on every run so an over-long edit
can never slip through silently.
"""

import os
import sys

# The turn: an escalating list of three — slippers, the neighbor,
# a restraining order — where the third item reframes the dog's
# helpfulness as a legal problem.
LINE = (
    "I tried to teach my dog to fetch my slippers; now he brings me "
    "the neighbor's slippers, the neighbor, and a restraining order."
)

MAX_CHARS = 200


def main() -> int:
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"error: line is {len(LINE)} chars, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
