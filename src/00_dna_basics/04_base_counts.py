#!/usr/bin/env python

"""Solution to exercise 4: count each nucleotide, keeping all four keys."""


def base_counts(seq: str) -> dict[str, int]:
    return {base: seq.count(base) for base in "ACGT"}


def main() -> None:
    print(base_counts("AACGTGGGA"))


if __name__ == "__main__":
    main()
