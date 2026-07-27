# Exercise 2: Reverse Complement

When you read the complementary strand of DNA, biology reads it in the *opposite*
direction (the two strands are antiparallel). So the biologically meaningful transform is
the **reverse complement**: complement every base, then reverse the whole string.

Implement `reverse_complement(seq)` building on the `complement` idea from the previous
exercise.

Hints:

- Complement first with a translation table, then reverse with slicing `[::-1]`.
- The order matters only cosmetically — reversing then complementing gives the same
  string — but "complement then reverse" is the conventional description.

Test it on `"ACGTACGT"`. The expected output is `"ACGTACGT"` — this particular sequence is
its own reverse complement (a *palindrome* in the biological sense). Also test `"AAAACCCG"`;
the expected output is `"CGGGTTTT"`.
