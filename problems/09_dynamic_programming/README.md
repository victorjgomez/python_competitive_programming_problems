# Dynamic Programming

## Idea
DP solves a problem by combining answers to **overlapping subproblems**, storing each one so it is computed only once. First define a **state** (what a subproblem is, e.g. `dp[i]` = best cost to reach step i). Then write the **transition** (how a state comes from smaller states) and the **base cases**. You can implement it **top-down** (recursion + memo) or **bottom-up** (fill a table in dependency order).

**Use it when…**
- The statement asks for the "minimum/maximum …", "number of ways …", or "is it possible …".
- A brute-force recursion recomputes the same arguments many times.
- Choices are made step by step, and the future depends only on a small summary of the past (the state).
- The constraints are too big for 2ⁿ but fine for n·k (e.g. n, k ≤ 10³–10⁵).

## Complexity
- Time ≈ (number of states) × (cost of one transition).
- Space ≈ number of states. It can often be reduced to the last row or last few values.
- Top-down: only visits the states it needs, but uses the call stack (recursion limit).
- Bottom-up: no recursion and usually faster in Python, but you must get the fill order right.

## Simple implementation
```python
# Coin change, number of ways (order does not matter), two styles
from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)


def ways_top_down(n: int, coins) -> int:
    @lru_cache(maxsize=None)
    def go(rest: int, i: int) -> int:     # state = (amount left, first coin allowed)
        if rest == 0:
            return 1
        if rest < 0 or i == len(coins):
            return 0
        # use coin i again (stay on i)  +  skip coin i forever
        return go(rest - coins[i], i) + go(rest, i + 1)
    return go(n, 0)


def ways_bottom_up(n: int, coins) -> int:
    dp = [1] + [0] * n                    # dp[s] = ways to form s with coins seen so far
    for c in coins:                       # coins in the outer loop -> combinations
        for s in range(c, n + 1):
            dp[s] += dp[s - c]
    return dp[n]


def min_coins(n: int, coins) -> int:      # "fewest coins" variant, -1 if impossible
    INF = float("inf")
    dp = [0] + [INF] * n
    for s in range(1, n + 1):
        dp[s] = min((dp[s - c] + 1 for c in coins if c <= s), default=INF)
    return dp[n] if dp[n] != INF else -1


if __name__ == "__main__":
    assert ways_top_down(4, (1, 2, 3)) == ways_bottom_up(4, [1, 2, 3]) == 4
    assert ways_top_down(10, (2, 5, 3, 6)) == ways_bottom_up(10, [2, 5, 3, 6]) == 5
    assert min_coins(11, [1, 2, 5]) == 3 and min_coins(3, [2]) == -1
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 1 | LeetCode | [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | [`leetcode_0746_min_cost_climbing_stairs.py`](leetcode_0746_min_cost_climbing_stairs.py) | Top-down memo (dict) | `go(i)` = min cost to reach step i, with O(n) time and space. ⚠ The base cases `go(0) = go(1) = 0` only come out right by accident: `cost[-1]` and `cost[-2]` wrap around to the appended `0` and the last cost. Explicit base cases (`if i <= 1: return 0`) would be clearer. The commented "bottom-up" version is really a forward top-down recursion memoized on `(i, my_cost)`, which is a much larger state. A true bottom-up is `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`. |
| 2 | HackerRank | [The Coin Change Problem](https://www.hackerrank.com/challenges/coin-change/problem) | [`hackerrank_coin_change.py`](hackerrank_coin_change.py) | Top-down memo (dict) | The include/exclude recursion is correct. ⚠ The memo is keyed only by `n`, but the result also depends on the coin index `i`, so cached values get reused for the wrong state. The key must be `(n, i)`. ⚠ The debug `print(f'n({n}):…')` pollutes the output and would fail the judge. |

## Pitfalls & takeaways
- The memo key must include **every** argument that affects the result (`(n, i)`, not just `n`).
- Write the base cases explicitly. Don't rely on Python's negative indexing to "make it work".
- For "number of ways", the loop order decides what you count: coins in the outer loop counts combinations, amounts in the outer loop counts ordered sequences.
- Remove debug prints before submitting. Top-down needs `sys.setrecursionlimit` for large n, while bottom-up does not.
