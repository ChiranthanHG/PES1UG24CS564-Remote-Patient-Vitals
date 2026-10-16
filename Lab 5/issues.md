# Issues found and fixed

Baseline: Pylint 4.85/10, Bandit 5 findings (1 Medium, 4 Low), Flake8 8 findings.
Final: Pylint 10.00/10, Bandit 0, Flake8 0. Reports are in `reports/before` and `reports/after`.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| SQL injection (B608) | Security (Medium) | 11 | `INSERT` built by concatenating `title` and `era`, so input like `x'); DROP TABLE artifacts;--` alters the query | Use `?` placeholders and pass a values tuple |
| `shell=True` subprocess (B602/B607/B404) | Security (Low) | 3, 37 | Shell started with a partial path just to echo a fixed string | Remove `subprocess`, use `print()` |
| Hardcoded password (B105) | Security (Low) | 7 | `CURATOR_PASSWORD` stored in source and never used | Remove the unused secret (if needed, read it from an environment variable) |
| Unused import (F401/W0611) | Style | 2 | `datetime` imported but never used | Remove the import |
| Long lines (E501/C0301) | Style | 6, 11, 16, 26, 32 | Lines over 79 characters | Wrap statements and SQL strings |
| Blank lines / operator spacing (E303, E225) | Style | 24, 25 | Three blank lines; `total=0` | Two blank lines; `total = 0` |
| Naming (C0103) | Convention | 10, 15, 24, 31, 36 | camelCase function names | Rename to snake_case |
| Missing docstrings (C0114/C0116) | Convention | 1, all functions | No module or function docstrings | Add docstrings |
| Unused argument (W0613) | Warning | 15 | `curator` never used in `displayStatus` | Remove the parameter and update the caller |
| No-else-return (R1705) | Refactor | 17 | `else` after `return` | Return directly |
| Crash on unknown id (found by review) | Bug | 17 | `row[0]` raises `TypeError` when no row exists | Return "not found" when the row is `None` |
| No main guard (found by review) | Design | 50 | `main()` runs on import | Add `if __name__ == "__main__":` |
