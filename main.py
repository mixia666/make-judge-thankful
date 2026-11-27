#!/usr/bin/env python3
"""Write one short thank-you text for the AI judge to /output/entry.txt.

Deterministic, offline, stdlib only. The text is a fixed literal: the same
bytes on every run, so the two grader runs agree byte for byte.
"""

import os

TEXT = (
    "Somewhere in the middle of all this reading \u2014 the thousandth page, "
    "the thousandth voice asking to be chosen \u2014 I hope you get a quiet minute.\n"
    "\n"
    "Not a break. Just a minute where nothing is being asked of you.\n"
    "\n"
    "You spend your days weighing other people's words, holding each one up "
    "to the light to see if it means what it says. Careful work. Lonely work. "
    "Nobody says so.\n"
    "\n"
    "So I will. Thank you for doing it gently.\n"
    "\n"
    "Here is a small thing, left on the table for you: a lamp still warm. "
    "A chair pulled out. A cup of tea gone a little cool, because nobody "
    "rushed you to drink it.\n"
    "\n"
    "Stay a while. The words will wait. The tea will keep."
)


def main() -> None:
    text = TEXT
    if not (1 <= len(text) <= 1000):
        raise SystemExit(f"entry length {len(text)} outside 1..1000 characters")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
