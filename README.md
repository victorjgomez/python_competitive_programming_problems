# Python Competitive Programming Problems

My personal practice log for competitive programming (ICPC @ PUCMM). **I learn by doing**: every
file here is a problem I actually sat down and solved — including the first naive attempts, the
improved `_v2`, `_v3`… versions, and a few that are still wrong. Each topic folder has a `README.md`
with a short explanation of the technique, a clean reference implementation, and notes on what I'd
improve in my own solutions.

## Topics

Folders are numbered in a suggested learning order.

| # | Topic | What it covers | Problems |
|---|-------|----------------|----------|
| 01 | [Arrays & Two Pointers](problems/01_arrays_two_pointers/README.md) | Linear scans, two pointers, running min / prefix sums | 6 |
| 02 | [Strings](problems/02_strings/README.md) | Parsing, pattern search, palindromes, anagrams | 9 |
| 03 | [Hashing](problems/03_hashing/README.md) | `dict`, `set`, `Counter` frequency maps | 12 |
| 04 | [Sorting & Greedy](problems/04_sorting_greedy/README.md) | Sort-then-scan, greedy choices, custom keys | 13 |
| 05 | [Binary Search](problems/05_binary_search/README.md) | Classic search, search on the answer | 3 + 1 example |
| 06 | [Stack & Queue](problems/06_stack_queue/README.md) | `deque`, parentheses, queue simulation | 3 + 4 examples |
| 07 | [Linked Lists](problems/07_linked_lists/README.md) | Node manipulation, merging | 1 |
| 08 | [Recursion](problems/08_recursion/README.md) | Base/recursive case, brute-force subsets | 3 |
| 09 | [Dynamic Programming](problems/09_dynamic_programming/README.md) | Memoization vs tabulation | 2 |
| 10 | [Math & Number Theory](problems/10_math_number_theory/README.md) | Primes, sieve, digits, checksums | 7 |
| 11 | [Trees](problems/11_trees/README.md) | Binary tree DFS / BFS | 3 |
| 12 | [Union-Find](problems/12_union_find/README.md) | Disjoint sets, connected components | 3 + reusable class |
| 13 | [Priority Queue](problems/13_priority_queue/README.md) | Heaps, `heapq`, a custom PQ project | 1 project |
| 14 | [Simulation](problems/14_simulation/README.md) | "Just do what the statement says" carefully | 7 |
| — | [Playground](problems/playground/README.md) | Scratch files, templates, work in progress | — |

## Repository layout

```
.
├── README.md                  ← you are here
└── problems/
    ├── 01_arrays_two_pointers/
    │   ├── README.md          ← concept + reference implementation + problem table
    │   ├── leetcode_0392_is_subsequence.py
    │   └── ...
    ├── ...
    └── playground/            ← unfinished / scratch code
```

### File naming

```
<platform>_<id>_<short_name>[_vN].py
```

| Prefix | Source |
|--------|--------|
| `leetcode_0704_...` | [LeetCode](https://leetcode.com/problemset/) (id zero-padded to 4 digits) |
| `codeforces_1213B_...` | [Codeforces](https://codeforces.com/problemset) (contest + problem letter) |
| `hackerrank_...` | [HackerRank](https://www.hackerrank.com/domains/algorithms) |
| `uva_10037_...` | [UVa Online Judge](https://onlinejudge.org/) |
| `matcom_9695_...` | MatcomGrader |
| `contest_...` | A local contest problem |
| `exercise_...` / `example_...` | Interview exercises or textbook demos with no judge |

`_v1`, `_v2`, … are successive attempts at the same problem. I keep them on purpose so I can see
how a solution improved (usually from O(n²) to O(n) or O(n log n)).

## How to run

Python 3.8+ (no third-party packages needed).

```bash
# most solutions read the judge input from stdin
python problems/03_hashing/hackerrank_missing_numbers_v4.py < input.txt

# LeetCode-style files define a `Solution` class and include a small demo under __main__
python problems/12_union_find/leetcode_0547_number_of_provinces.py

# some HackerRank templates write to the file in OUTPUT_PATH
OUTPUT_PATH=out.txt python problems/14_simulation/hackerrank_a_very_big_sum.py           # bash
$env:OUTPUT_PATH="out.txt"; python problems/14_simulation/hackerrank_a_very_big_sum.py   # PowerShell

# the priority-queue project imports `PQ`, so run it from its folder
cd problems/13_priority_queue/pq_project && python Test_PQ.py
```

## How I add a new problem

1. Copy [`problems/playground/template.py`](problems/playground/template.py) into the topic folder.
2. Name it with the convention above.
3. Solve it. If I find a better approach later, save it as `_v2` instead of overwriting.
4. Add a row to that topic's `README.md` table (with a ⚠ note if it's not fully accepted yet).

## Roadmap

Next topics I want to practice:

- [ ] Sliding window
- [ ] Prefix sums & difference arrays (beyond the basics in 01)
- [ ] Graphs: BFS / DFS on grids and adjacency lists
- [ ] Shortest paths (Dijkstra with `heapq`)
- [ ] More DP: LIS, LCS, 0/1 knapsack
- [ ] Bit manipulation
- [ ] Segment tree / Fenwick tree

**Revisit list:** solutions marked with ⚠ in each topic README are known to be wrong or too slow —
fixing them is good practice.
