# Exercise 3: Normalize a Sequence

Real-world sequence data is messy: mixed case, embedded whitespace or newlines (FASTA
wraps long sequences across lines), and sometimes `U` (uracil) where you expected `T`
because someone handed you RNA.

Implement `normalize(seq)` that returns a clean upper-case DNA string by:

1. Upper-casing everything.
2. Removing all whitespace (spaces, tabs, newlines).
3. Converting any `U` to `T`.

Do **not** validate here — a later caller can run `is_valid_dna` on the result.

Hints:

- `"".join(seq.split())` removes every run of whitespace.
- Chain `.upper()`, the whitespace removal, and `.replace("U", "T")`.

Test it on the string `"  acg u\nUuT "`. The expected output is `"ACGTTTT"`.
