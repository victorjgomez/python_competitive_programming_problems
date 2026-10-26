# Sorting & Greedy

## Idea
Sorting puts the data in an order where the best choice becomes obvious — smallest first, largest first, or by a custom `key`. A **greedy** algorithm then makes the locally best choice at every step and never undoes it.
Greedy is only correct when you can argue it (usually an *exchange argument*: "swapping two items out of greedy order never improves the answer"). When you cannot, try a small counterexample or fall back to DP.

**Use it when…**
- The statement asks for the minimum/maximum after "rearranging", "pairing" or "choosing an order".
- Pairing two arrays: smallest with largest (sort one ascending, the other descending).
- Scheduling: serve the shortest jobs first, pick intervals by earliest end time.
- Answer depends only on relative order, not original positions (or you can keep the index in a tuple).
- n is up to 10⁵–10⁶, so O(n log n) is the budget.

## Complexity
| Step | Time | Space |
|------|------|-------|
| `sorted` / `list.sort` (Timsort, stable) | O(n log n) | O(n) |
| Greedy scan after sorting | O(n) | O(1) |
| Counting sort (small value range V) | O(n + V) | O(V) |

## Simple implementation
```python
from typing import List, Tuple


def order_by_finish(orders: List[Tuple[int, int]]) -> List[int]:
    """Sort with a key; Python's sort is stable, so ties keep input order."""
    ids = range(1, len(orders) + 1)
    by_time = sorted(zip(orders, ids), key=lambda p: p[0][0] + p[0][1])
    return [cid for _, cid in by_time]


def can_pair(a: List[int], b: List[int], k: int) -> bool:
    """Smallest of a with largest of b; all sums must be >= k."""
    return all(x + y >= k for x, y in zip(sorted(a), sorted(b, reverse=True)))


if __name__ == "__main__":
    assert order_by_finish([(8, 1), (4, 2), (5, 6), (3, 1), (4, 3)]) == [4, 2, 5, 1, 3]
    assert can_pair([2, 1, 3], [7, 8, 9], 10)
    assert not can_pair([1, 2, 2, 1], [3, 3, 3, 4], 5)
```

```python
from typing import List, Tuple


def max_non_overlapping(intervals: List[Tuple[int, int]]) -> int:
    """Activity selection: always keep the interval that ends first."""
    count, last_end = 0, float("-inf")
    for start, end in sorted(intervals, key=lambda iv: iv[1]):
        if start >= last_end:          # does not overlap the last chosen
            count += 1
            last_end = end
    return count


if __name__ == "__main__":
    assert max_non_overlapping([(1, 3), (2, 4), (3, 5), (0, 6), (5, 7)]) == 3
    assert max_non_overlapping([]) == 0
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 1486A | Codeforces | [Shifting Stacks](https://codeforces.com/problemset/problem/1486/A) | [`codeforces_1486A_shifting_stacks.py`](codeforces_1486A_shifting_stacks.py) | One greedy pass moving 1 block right | ⚠ Wrong approach: it moves at most one block per position. Correct greedy: push everything right; answer is YES iff for every i (0-based) `h[0] + … + h[i] >= 0 + 1 + … + i`. |
| 1685A | Codeforces | [Circular Local MiniMax](https://codeforces.com/problemset/problem/1685/A) | [`codeforces_1685A_circular_local_minimax.py`](codeforces_1685A_circular_local_minimax.py) | Sort, interleave lower/upper halves, verify | The idea (odd n → NO; else interleave and check) is right. ⚠ The input values are never converted to `int`, so they are sorted as strings (`"10" < "9"`) → wrong answers with multi-digit numbers. |
| 545D | Codeforces | [Queue](https://codeforces.com/problemset/problem/545/D) | [`codeforces_545D_queue.py`](codeforces_545D_queue.py) | Sort ascending, skip people who would be disappointed | Correct greedy, O(n log n). A disappointed person is moved to the end, so their time is not added — exactly what the code does. Uses the walrus operator (Python 3.8+). |
| — | Exercise | Missing number in 1..n | [`exercise_missing_number.py`](exercise_missing_number.py) | Sort, find first `a[i-1] != i` | ⚠ If the missing number is `n` the loop ends without printing anything. `n*(n+1)//2 - sum(a)` is O(n) and has no edge case. |
| — | HackerRank | [Grid Challenge](https://www.hackerrank.com/challenges/grid-challenge/problem) | [`hackerrank_grid_challenge.py`](hackerrank_grid_challenge.py) | Sort each row, check columns | Correct, O(n·m log m). Re-checking rows after sorting them is redundant; `zip(*rows)` transposes in one line. |
| — | HackerRank | [Jim and the Orders](https://www.hackerrank.com/challenges/jim-and-the-orders/problem) | [`hackerrank_jim_and_the_orders.py`](hackerrank_jim_and_the_orders.py) | `sort(key=order + prep)` | Correct; stability of `list.sort` resolves ties by smaller customer id for free. |
| — | HackerRank | [Marc's Cakewalk](https://www.hackerrank.com/challenges/marcs-cakewalk/problem) | [`hackerrank_marcs_cakewalk.py`](hackerrank_marcs_cakewalk.py) | Sort descending, weight 2^j | Greedy is right (largest calories get the smallest multiplier). ⚠ `marcsCakewalk` sorts the global `calorie` instead of its parameter `calories`; it only works because both names point to the same list when run as a script. |
| — | HackerRank | [Permuting Two Arrays](https://www.hackerrank.com/challenges/two-arrays/problem) | [`hackerrank_permuting_two_arrays.py`](hackerrank_permuting_two_arrays.py) | A ascending vs B descending | Correct, O(n log n). `itertools.permutations` is imported but unused (left over from a brute-force idea, which would be O(n!)). |
| 88 | LeetCode | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | [`leetcode_0088_merge_sorted_array.py`](leetcode_0088_merge_sorted_array.py) | Remove zeros, concatenate, sort | ⚠ `nums1 = ...` rebinds the local name, so the caller's `nums1` is never modified. ⚠ Removing *all* zeros also deletes real zeros from the data. Use `nums1[:] = sorted(nums1[:m] + nums2)` or three pointers from the end (O(m + n)). |
| 1365 | LeetCode | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | [`leetcode_1365_smaller_than_current.py`](leetcode_1365_smaller_than_current.py) | Sort descending + skip duplicates + `index` | Correct; `index` per element and the duplicate loop make it O(n²) worst case (fine for n ≤ 500). Sort ascending and `{v: first index}` gives O(n log n); counting sort (values ≤ 100) gives O(n). |
| 2160 | LeetCode | [Minimum Sum of Four Digit Number After Splitting Digits](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/) | [`leetcode_2160_min_sum_four_digit_split.py`](leetcode_2160_min_sum_four_digit_split.py) | Sort digits, two smallest as tens | Correct greedy: `10·(d0 + d1) + d2 + d3`. `sorted(str(num))` would extract the digits more simply. |
| 10037 | UVA | [Bridge](https://onlinejudge.org/external/100/10037.pdf) | [`uva_10037_bridge.py`](uva_10037_bridge.py) | Recursive greedy, always "two fastest escort" | Right for `1 2 5 10` (17). ⚠ Not optimal in general: `1 100 101 102` gives 403, optimum is 305. At each step take `min(a0 + 2·a1 + an, 2·a0 + an-1 + an)`. ⚠ `n = 1` raises `IndexError`. |
| 11389 | UVA | [The Bus Driver Problem](https://onlinejudge.org/external/113/11389.pdf) | [`uva_11389_bus_driver_problem.py`](uva_11389_bus_driver_problem.py) | Morning ascending vs evening descending | Correct greedy, O(n log n). Parsing with `split(" ")` breaks on double spaces — use `split()`. |

## Pitfalls & takeaways
- Always convert input to `int` before sorting; string sort is lexicographic.
- Greedy needs a proof or at least a brute-force check on small cases — Bridge and Shifting Stacks both look greedy but need the right rule.
- Rebinding a parameter (`nums1 = ...`) is not "in place"; use slice assignment `nums1[:] = ...`.
- Python's sort is stable: sort by a key and ties keep input order (or sort by a tuple key for explicit tie-breaks).
