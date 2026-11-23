#!/usr/bin/env python3
"""Write the make.fun bounty entry to a short text file."""

import os
import sys
from pathlib import Path

ENTRY_TEXT = (
    "My sister, who has never written code, sent make.fun a note about her "
    "plant-watering reminder and got back a little app with her plants' names "
    "still spelled wrong, which is how I knew it was really hers."
)


def main() -> None:
    assert 1 <= len(ENTRY_TEXT) <= 280
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY_TEXT.encode("utf-8"))
    print(len(ENTRY_TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
