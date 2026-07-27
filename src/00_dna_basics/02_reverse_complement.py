#!/usr/bin/env python

"""Solution to exercise 2: reverse complement of a DNA strand."""

_COMPLEMENT = str.maketrans("ACGT", "TGCA")


def reverse_complement(seq: str) -> str:
    return seq.translate(_COMPLEMENT)[::-1]


def main() -> None:
    print(reverse_complement("ACGTACGT"))
    print(reverse_complement("AAAACCCG"))


if __name__ == "__main__":
    main()
