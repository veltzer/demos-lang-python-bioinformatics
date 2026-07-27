#!/usr/bin/env python

"""Solution to exercise 0: validate a DNA sequence over the ACGT alphabet."""

_BASES = set("ACGT")


def is_valid_dna(seq: str) -> bool:
    return set(seq) <= _BASES


def main() -> None:
    for seq in ("ACGTACGT", "ACGTN", "acgt"):
        print(f"{seq!r}: {is_valid_dna(seq)}")


if __name__ == "__main__":
    main()
