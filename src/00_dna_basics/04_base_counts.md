# Exercise 4: Count the Bases

The most basic summary of a sequence is how many of each nucleotide it contains.

Implement `base_counts(seq)` that returns a dictionary mapping each of `A`, `C`, `G`, `T`
to its count in `seq`. Every one of the four keys must be present even if its count is
zero.

Hints:

- `collections.Counter(seq)` counts everything in one pass, but it omits bases that never
  appear. Build the result explicitly so all four keys exist:
  `{b: seq.count(b) for b in "ACGT"}`.

Test it on `"AACGTGGGA"`. The expected output is
`{'A': 3, 'C': 1, 'G': 4, 'T': 1}`.
