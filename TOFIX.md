# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `pyproject.toml:10` - `pytest` is a declared dev dependency but the repo has no tests and `rsconstruct.toml` has no `[processor.pytest]`. Every exercise `.md` states an exact expected output (e.g. `src/00_dna_basics/02_reverse_complement.md:17`, `src/00_dna_basics/04_base_counts.md:15`), so add a test module asserting those values against the solution functions plus a `[processor.pytest]` entry - or drop `pytest` from the dev group if tests are not wanted.

## Low

- `pyproject.toml:19` - fleet-wide pattern (89 repos list `config` in ruff/mypy `src_dirs` though no repo has `.py` under `config/`; 82 repos carry `mypy_path = "src:python:scripts"`): here `rsconstruct.toml:41`/`rsconstruct.toml:45` scan a `.lua`-only `config/`, and `python/` and `scripts/` do not exist. Fix in the fleet's source of these defaults, then here: `src_dirs = ["src"]`, `mypy_path = "src"`.
- `.yamllint.yaml:1` - a yamllint config is committed but no yaml processor runs, so `.github/dependabot.yml` is never linted; add `[processor.yamllint]` (or `iyamllint`) with `src_dirs = [".github"]`, or remove the unused config.
- `config/project.lua:8` - the keyword `biopython` advertises a library the repo never uses (no dependency, no import in `src/`); drop it until a biopython exercise exists.
