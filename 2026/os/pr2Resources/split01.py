#!/usr/bin/env python3

import argparse
import re
from pathlib import Path


# An act starts approximately like:
#
#     No. 42
#     (R123, H4567)
#     AN ACT
#
# Allow whitespace/newlines between those components.
ACT_START = re.compile(
    r"(?m)"
    r"^[ \t]*No\.[ \t]+(?P<number>\d+)[ \t]*\n"
    r"(?:[ \t]*\n)*"
    r"[ \t]*\(R\d+,[ \t]*[HS]\d+\)[ \t]*\n"
    r"(?:[ \t]*\n)*"
    r"[ \t]*AN ACT\b"
)


def split_acts(text):
    """Yield (act_number, act_text) pairs."""

    matches = list(ACT_START.finditer(text))

    for i, match in enumerate(matches):
        act_number = int(match.group("number"))
        start = match.start()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)

        yield act_number, text[start:end].strip() + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Split a South Carolina Statutes at Large text file by act."
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Plain-text Statutes at Large input file"
    )
    parser.add_argument(
        "output_directory",
        type=Path,
        help="Directory in which individual acts will be written"
    )

    args = parser.parse_args()

    # Check the input before doing any work.
    if not args.input_file.is_file():
        parser.error(f"input file does not exist: {args.input_file}")

    # mkdir(..., exist_ok=True) gives precisely the behavior you described:
    # create the directory if necessary; otherwise leave it alone.
    args.output_directory.mkdir(parents=True, exist_ok=True)

    text = args.input_file.read_text(
        encoding="utf-8",
        errors="replace"
    )

    acts = list(split_acts(text))

    if not acts:
        raise SystemExit("No acts found in input file.")

    for act_number, act_text in acts:
        output_file = args.output_directory / f"{act_number}.txt"
        output_file.write_text(act_text, encoding="utf-8")
        print(f"{act_number:4d} -> {output_file}")

    print(f"\nWrote {len(acts)} acts.")


if __name__ == "__main__":
    main()
