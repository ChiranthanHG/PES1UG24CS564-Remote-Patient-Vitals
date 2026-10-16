# Reflection

1. **Which tool was most useful?** Bandit, for the SQL injection (the only Medium finding). Pylint was best for overall quality and Flake8 for consistent style.
2. **Any false positives?** Bandit's hardcoded-password finding flagged a constant that was never used, so the real fix was deleting it. In real code a secret should come from an environment variable or secret store.
3. **How did the tools change how you write code?** Parameterized queries, docstrings and snake_case names become habit, and running the tools before each commit catches problems early.
4. **Limits of static analysis?** It cannot judge logic or intent. It missed the crash on an unknown artifact id, which I found by reading the code. It complements tests and code review rather than replacing them.
