# Playground

Scratch space: quick experiments, the problem-file template, and work-in-progress attempts. Files here are **not** expected to pass, or even to run; some do not compile yet. Once a file is solved and tested, "graduate" it: rename it following the repo convention (`<platform>_<id>_<slug>.py`) and move it into its topic folder, adding a row to that folder's README.

| File | What it is | Status |
|------|------------|--------|
| [`prueba.py`](prueba.py) | Hello-world scratch: prints a greeting, reads two numbers and prints their sum | Scratch |
| [`template.py`](template.py) | Problem file template/schema: problem link, "steps to solve" notes, empty `Solution` class and `__main__` block | Template |
| [`codeforces_1676E_eating_queries_stub.py`](codeforces_1676E_eating_queries_stub.py) | [Codeforces 1676E – Eating Queries](https://codeforces.com/problemset/problem/1676/E): only reads `t` | Stub (hint: sort descending, prefix sums + binary search) |
| [`codeforces_1685B_linguistics_wip.py`](codeforces_1685B_linguistics_wip.py) | [Codeforces 1685B – Linguistics](https://codeforces.com/problemset/problem/1685/B): greedy matching of `AB`/`BA`/`A`/`B` words | Incomplete: hardcoded input, debug `print`s, `solution()` returns `None` |
| [`hackerrank_weighted_uniform_strings_wip.py`](hackerrank_weighted_uniform_strings_wip.py) | [HackerRank – Weighted Uniform Strings](https://www.hackerrank.com/challenges/weighted-uniform-string/problem) stub | Does not compile: the function body is only a comment (`IndentationError`, a `SyntaxError`); result is never printed |
| [`go_kill_the_monsters_wip.py`](go_kill_the_monsters_wip.py) | Recursive cost solution: each step takes the first half of the list, pays `k` if that half's sum exceeds `k` (otherwise pays the sum), then recurses on the remaining half (problem source unknown) | Buggy: the recursive calls in the `elif`/`else` branches are not `return`ed, so the function returns `None` except on an empty list; the `suma > k` branch uses the global `list_a` instead of `list_aa`; the `half == 0` branch adds `list_aa[0]` without comparing to `k` |
