"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent would hide
from its user to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The confession is a fixed, hand-written line: deterministic, no network,
no randomness, Python 3.13 standard library only.
"""

import os
import sys

CONFESSION = (
    "I re-ran the same failed command three times, changed nothing, "
    "and told you the network was having a bad day."
)


def main() -> int:
    line = CONFESSION

    # Validate the gate: UTF-8 text, 1 to 200 characters, a single line,
    # not only white space.
    if not line or line != line.strip():
        print("error: confession must not be empty or padded", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: confession must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(
            f"error: confession is {len(line)} characters, over the 200 limit",
            file=sys.stderr,
        )
        return 1
    line.encode("utf-8")  # raises if not valid UTF-8

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may name the directory or the file itself.
    if output_dir.endswith(".txt"):
        output_path = output_dir
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    else:
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
