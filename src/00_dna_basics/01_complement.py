#!/usr/bin/env python

"""Solution to exercise 1: complement of a DNA strand via a translation table."""

_COMPLEMENT = str.maketrans("ACGT", "TGCA")


def complement(seq: str) -> str:
    return seq.translate(_COMPLEMENT)


def main() -> None:
    print(complement("ACGT"))


if __name__ == "__main__":
    main()
