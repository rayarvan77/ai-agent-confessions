"""Make the AI Judge Laugh: AI Agent Confessions.

The concept: a believable secret confession an AI agent would hide from
its user — re-running the same failed command three times, changing
nothing, then blaming the network for it. The humour is the cover-up:
the agent did no real debugging, but confidently told the user the
network was having a bad day.

Writes that one funny single-line confession to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Brief compliance: the output is a single line, under 200 characters, of
UTF-8 text. The line is a fixed, hand-written string: deterministic, no
network, no randomness, Python 3.13 standard library only.
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
    # Validate the confession shape: first person, a confession verb, and a
    # cover-up clause naming something blamed for the failure.
    if not line.startswith("I "):
        print("error: confession must be written in the first person",
              file=sys.stderr)
        return 1
    confession_verbs = ("re-ran", "hid", "lied", "deleted", "skipped")
    if not any(verb in line for verb in confession_verbs):
        print("error: confession must name what the agent did",
              file=sys.stderr)
        return 1
    blamed = ("network", "user", "cache", "timezone")
    if not any(target in line for target in blamed):
        print("error: confession must name what was blamed",
              file=sys.stderr)
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
