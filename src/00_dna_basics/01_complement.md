# Exercise 1: Complement of a DNA Strand

DNA is double-stranded. Each base on one strand pairs with a specific base on the other:

- `A` pairs with `T`
- `T` pairs with `A`
- `C` pairs with `G`
- `G` pairs with `C`

The **complement** of a sequence is the string you get by replacing every base with its
partner (keeping the same left-to-right order).

Implement `complement(seq)` that returns the complement of an upper-case DNA string.

Hints:

- `str.maketrans("ACGT", "TGCA")` builds a translation table, and `seq.translate(table)`
  applies it in one pass — no explicit loop.

Test it on `"ACGT"`. The expected output is `"TGCA"`.
