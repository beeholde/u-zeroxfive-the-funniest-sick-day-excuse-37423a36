"""The Funniest Sick-Day Excuse — one line, under 200 characters.

Writes the excuse to /output/entry.txt for the judge to read.
"""

import os
from pathlib import Path

LINE = "I can't come in — my knee locked halfway down the stairs, so I'm a human statue on step seven and the neighbours have started leaving coins."


def main() -> None:
    text = LINE.strip()
    # The gate: UTF-8 text of 1 to 200 characters, a single line.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
