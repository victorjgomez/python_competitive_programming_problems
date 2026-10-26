# Arrays & Two Pointers

## Idea
Many array problems can be solved in one linear pass if you keep a small amount of state instead of re-scanning the array.
**Two pointers** walk the array either from opposite ends towards each other (sorted pair sums, palindromes) or in the same direction at different speeds (read/write pointers, subsequence matching).
**Prefix sums** (and running minimum/maximum) store "everything to the left" in one number, so range or left/right questions take O(1) each.

**Use it when…**
- The array is sorted, or you need pairs/triples with a target sum.
- You must modify an array **in place** (remove, compact, move elements).
- You check whether one sequence is a subsequence of / matches another.
- The question compares "sum to the left" vs "sum to the right", or "something smaller/larger later in the array".
- A brute force with two nested loops is O(n²) and n is up to 10⁵ or more.

## Complexity
| Technique | Time | Extra space |
|-----------|------|-------------|
| Two pointers (either style) | O(n) | O(1) |
| Prefix sums (build) | O(n) | O(n) (or O(1) with running totals) |
| Range-sum query after build | O(1) | — |
| Running min/max scan | O(n) | O(1) |

## Simple implementation
```python
from typing import List


def pair_with_sum(nums: List[int], target: int) -> bool:
    """Opposite ends: nums must be sorted."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return True
        if s < target:
            lo += 1          # need a bigger sum
        else:
            hi -= 1          # need a smaller sum
    return False


def compact_nonzero(nums: List[int]) -> None:
    """Same direction: write pointer w trails read pointer r (in place)."""
    w = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1


if __name__ == "__main__":
    assert pair_with_sum([1, 2, 4, 7, 11], 15)
    assert not pair_with_sum([1, 2, 4], 10)
    a = [0, 1, 0, 3, 12]
    compact_nonzero(a)
    assert a == [1, 3, 12, 0, 0]
```

```python
from typing import List


def build_prefix(nums: List[int]) -> List[int]:
    """pre[i] = nums[0] + ... + nums[i-1]; pre[0] = 0."""
    pre = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        pre[i + 1] = pre[i] + x
    return pre


def range_sum(pre: List[int], l: int, r: int) -> int:
    """Sum of nums[l..r] inclusive, O(1)."""
    return pre[r + 1] - pre[l]


def has_balance_index(nums: List[int]) -> bool:
    """Is there i with sum(left of i) == sum(right of i)?"""
    total, left = sum(nums), 0
    for x in nums:
        if left == total - left - x:
            return True
        left += x
    return False


if __name__ == "__main__":
    pre = build_prefix([3, 1, 4, 1, 5])
    assert range_sum(pre, 1, 3) == 6
    assert has_balance_index([1, 2, 3, 3])
    assert not has_balance_index([1, 2, 3])
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 1213B | Codeforces | [Bad Prices](https://codeforces.com/problemset/problem/1213/B) | [`codeforces_1213B_bad_prices_v1.py`](codeforces_1213B_bad_prices_v1.py) | Candidate list + popping | Correct, but every new price rescans and pops from the list → O(n²) worst case (risk of TLE for n = 1.5·10⁵). |
| 1213B | Codeforces | [Bad Prices](https://codeforces.com/problemset/problem/1213/B) | [`codeforces_1213B_bad_prices_v2.py`](codeforces_1213B_bad_prices_v2.py) | Right-to-left running minimum | Real improvement over v1: one pass, O(n) time, O(1) space. Minor: the variable `min` shadows the built-in. |
| — | Interview exercise | Nearest greater element distance | [`exercise_nearest_greater_distance.py`](exercise_nearest_greater_distance.py) | Linear scan | O(n) per query, fine for a single query. On ties (same distance left and right) the left one wins. If no greater element exists it prints `sys.maxsize` instead of a clear "none". |
| — | HackerRank | [Left Rotation](https://www.hackerrank.com/challenges/array-left-rotation/problem) | [`hackerrank_left_rotation.py`](hackerrank_left_rotation.py) | Repeated single-step rotation | Correct but O(n·d): each step copies the whole list. Slicing does it in O(n): `k = d % n; arr[k:] + arr[:k]`. Needs the `OUTPUT_PATH` env var to run locally. |
| — | HackerRank | [Sherlock and Array](https://www.hackerrank.com/challenges/sherlock-and-array/problem) | [`hackerrank_sherlock_and_array.py`](hackerrank_sherlock_and_array.py) | Running left/right sums | O(n), correct, including n = 1. The custom `sum` function shadows the built-in; the three `if` branches could collapse into one (`left == total - left - x`). |
| 283 | LeetCode | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [`leetcode_0283_move_zeroes.py`](leetcode_0283_move_zeroes.py) | `pop` + `append` from the right | Output is correct and in place, but `list.pop(i)` is O(n) → O(n²) overall. The read/write two-pointer template above is O(n). Leftover `print(nums)` should be removed before submitting. |
| 392 | LeetCode | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | [`leetcode_0392_is_subsequence.py`](leetcode_0392_is_subsequence.py) | Same-direction two pointers | Clean O(n + m), O(1) space. Can return `i == n` directly. |

## Pitfalls & takeaways
- `list.pop(i)` / `list.insert(i, x)` in the middle are O(n); doing them inside a loop silently makes the solution O(n²).
- Before nested loops, ask "can a single running value (sum, min, max) replace the inner loop?" — Bad Prices v1 → v2 is the textbook example.
- Rotations: always reduce `d %= n` first, then use slicing.
- Avoid naming variables `sum`, `min`, `max`, `input`: it breaks the built-ins later in the same scope.
