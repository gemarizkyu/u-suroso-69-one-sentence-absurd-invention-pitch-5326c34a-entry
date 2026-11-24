#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance: toast that always lands butter-side down.

The pitch is fixed and deterministic: no model calls, no wall clock,
no unseeded randomness, no input data. The program only writes the
sentence to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set,
for local testing), so the replay matches the live run exactly.
"""

import os
from pathlib import Path

PITCH = (
    "A toaster that launches your bread on a tiny parachute, "
    "then files a flight plan so it lands butter-side up every single time."
)

MAX_CHARS = 220


def main() -> None:
    pitch = PITCH.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 220 characters,
    # not only white space, and a single sentence.
    assert 1 <= len(pitch) <= MAX_CHARS, "pitch must be 1-220 characters"
    assert pitch.count(".") == 1, "pitch must be exactly one sentence"
    assert "\n" not in pitch, "pitch must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(pitch, encoding="utf-8")


if __name__ == "__main__":
    main()
