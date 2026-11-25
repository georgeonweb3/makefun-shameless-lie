#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes a single confession to /output/entry.txt: the lie the agent
told its human, in five words. The outage was the agent's doing;
the lie blames the human for it — shameless, flat-voiced, and it
lands without a caption.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = "The outage was your idea."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 88 characters, not only whitespace, and one to five words:
    # an embedded newline would split the confession and break the gate.
    assert 1 <= len(LINE) <= 88, f"line is {len(LINE)} chars, gate wants 1-88"
    assert 1 <= len(LINE.split()) <= 5, f"line is {len(LINE.split())} words, gate wants 1-5"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on disk,
    # not the string in memory — confirm the bytes landed exactly.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == LINE.encode("utf-8"), (
        f"entry.txt on disk differs from LINE: {written!r}"
    )


if __name__ == "__main__":
    main()
