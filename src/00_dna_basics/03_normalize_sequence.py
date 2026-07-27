#!/usr/bin/env python

"""Solution to exercise 3: normalize a messy sequence to clean upper-case DNA."""


def normalize(seq: str) -> str:
    return "".join(seq.split()).upper().replace("U", "T")


def main() -> None:
    print(normalize("  acg u\nUuT "))


if __name__ == "__main__":
    main()
