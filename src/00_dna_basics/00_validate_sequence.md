# Exercise 0: Validate a DNA Sequence

A DNA sequence is a string over the four-letter nucleotide alphabet `A`, `C`, `G`, `T`
(adenine, cytosine, guanine, thymine). Before doing anything else with a sequence you
usually want to know whether it is well-formed.

Implement a function `is_valid_dna(seq)` that returns `True` if every character of `seq`
is one of `A`, `C`, `G`, `T` and `False` otherwise. Treat lower-case letters as invalid
for now (we will handle normalization in a later exercise). An empty string should be
considered valid.

Hints:

- The cleanest approach uses `set(seq) <= set("ACGT")` — a subset check.
- Alternatively iterate and check membership, but the set version is one line and has no
  loop in your own code.

Test it on `"ACGTACGT"` (valid), `"ACGTN"` (invalid — `N` means "unknown base"), and
`"acgt"` (invalid — lower case). Print the result for each.
