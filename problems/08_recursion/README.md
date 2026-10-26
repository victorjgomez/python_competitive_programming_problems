# Recursion & Backtracking

## Idea
A recursive function solves a problem by calling itself on a smaller version of it. Every recursive function needs a **base case** (stop) and a **recursive case** (shrink, then combine). **Backtracking** is recursion that builds a candidate step by step: *choose* an option, *explore* deeper, then *un-choose* it. It can prune branches that cannot lead to a valid answer. If the same subproblem is solved many times, add memoization. That turns the recursion into dynamic programming (see `09_dynamic_programming`).

**Use it when…**
- The answer is defined in terms of smaller answers (recurrences, trees, divide and conquer).
- You must enumerate or count subsets, permutations, or combinations ("in how many ways…", "list all…").
- The constraints are small (n ≤ ~20 for subsets, n ≤ ~10 for permutations).
- Partial candidates can be rejected early (sum already too big, constraint already violated).

## Complexity
| Pattern | Time | Space (stack) |
|---------|------|---------------|
| Linear recursion (`f(n) -> f(n-1)`) | O(n) | O(n) |
| Two branches without memo (`f(n-1) + f(n-2)`) | O(φⁿ) ≈ O(1.62ⁿ) | O(n) |
| Subsets / include-exclude | O(2ⁿ · n) | O(n) |
| Permutations | O(n! · n) | O(n) |

Python's default recursion limit is about 1000 frames. For deeper recursion, raise it with `sys.setrecursionlimit(10**6)`. Very deep recursion can still crash the interpreter, so switch to an iterative version or an explicit stack if that happens.

## Simple implementation
```python
# Recursion anatomy: base case + recursive case
import sys
sys.setrecursionlimit(10**6)         # only needed for deep recursion


def fast_pow(a: int, n: int) -> int:
    if n == 0:                       # base case
        return 1
    half = fast_pow(a, n // 2)       # recursive case on a smaller input
    return half * half * (a if n % 2 else 1)


if __name__ == "__main__":
    assert fast_pow(3, 13) == 3 ** 13
```

```python
# Backtracking: count subsets of distinct natural numbers whose n-th powers sum to x
def power_sum(x: int, n: int, start: int = 1) -> int:
    if x == 0:                       # found a valid combination
        return 1
    count = 0
    base = start
    while base ** n <= x:            # prune: larger bases can only overshoot
        count += power_sum(x - base ** n, n, base + 1)   # choose base, explore
        base += 1                    # un-choose: try the next base
    return count


def subsets(nums):
    res, cur = [], []
    def go(i):
        if i == len(nums):
            res.append(cur[:])       # copy, because cur keeps changing
            return
        cur.append(nums[i]); go(i + 1); cur.pop()   # include, explore, undo
        go(i + 1)                                    # exclude
    go(0)
    return res


if __name__ == "__main__":
    assert power_sum(10, 2) == 1 and power_sum(100, 2) == 3
    assert sorted(subsets([1, 2])) == [[], [1], [1, 2], [2]]
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 1 | HackerRank | [Fibonacci Modified](https://www.hackerrank.com/challenges/fibonacci-modified/problem) | [`hackerrank_fibonacci_modified.py`](hackerrank_fibonacci_modified.py) | Plain recursion | It translates the recurrence `t(n) = t(n-2) + t(n-1)²` directly. There is no memo, so it makes about 1.6ⁿ calls. That passes for n ≤ 20, and Python's big ints handle the huge values. A 3-line loop (`a, b = b, a + b*b`) is O(n) and clearer. |
| 2 | HackerRank | [The Power Sum](https://www.hackerrank.com/challenges/the-power-sum/problem) | [`hackerrank_the_power_sum.py`](hackerrank_the_power_sum.py) | Bitmask brute force (all 2ᵏ subsets) | It enumerates every subset of `{1ⁿ, 2ⁿ, …}` as a binary string, so this is not actually recursion. ⚠ With x = 1000 and n = 2 there are 31 candidates, which means 2³¹ masks and a timeout. Backtracking with pruning (template above) visits only a tiny fraction of them. |
| 3 | HackerRank | [Knapsack (unbounded)](https://www.hackerrank.com/challenges/unbounded-knapsack/problem) | [`hackerrank_unbounded_knapsack.py`](hackerrank_unbounded_knapsack.py) | Include/exclude recursion | It records every reachable remaining capacity in a global list, then prints `k - min(remaining)`. ⚠ The global `difference` list is never cleared between test cases, so an earlier test's minimum can corrupt later answers. ⚠ The recursion is exponential with no memo. The proper fix is DP: `reach[s] = any(reach[s - a] for a in arr)`, which is O(k · n). |

## Pitfalls & takeaways
- Write the base case first, and make sure every recursive call moves toward it.
- Global or shared mutable state must be reset per test case, or passed as a parameter.
- If the same `(arguments)` show up repeatedly, add `@functools.lru_cache` (memoization) and you have DP.
- Recursion is not always needed: for linear recurrences, a loop is shorter and has no depth limit.
