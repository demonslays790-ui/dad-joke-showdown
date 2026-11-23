"""Dad Joke Showdown entry (program/v1).

Writes one original dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(falls back to /output). Stdlib only.
"""

import os
import sys

JOKE = (
    "I told my daughter the washing machine is the hardest worker here \u2014 "
    "it does all the dirty work, never complains, and still gets taken "
    "for granted every single load."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
