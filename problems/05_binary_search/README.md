# Binary Search

## Idea
Binary search halves a search range at every step, so it finds a target among n candidates in O(log n) comparisons. It works on any **monotonic** condition: a sorted array, or a yes/no predicate that is `False … False True … True` over a range of numbers.
The second form — **binary search on the answer** — is the most useful in contests: instead of computing the answer directly, guess a value `x`, check "is `x` feasible?", and halve the range.

**Use it when…**
- The input is sorted and you need a position, first/last occurrence, or count in a range.
- The statement says "minimum value such that…" / "maximum value such that…".
- The answer range is huge (up to 10⁹ or 10¹⁸) but checking one candidate is cheap.
- An interactive/oracle function tells you "higher" or "lower" (guess the number).

## Complexity
| Variant | Time | Space |
|---------|------|-------|
| Iterative binary search / `bisect` | O(log n) | O(1) |
| Recursive binary search | O(log n) | O(log n) call stack |
| Search on answer with an O(f) check | O(f · log(range)) | depends on check |

## Simple implementation
```python
from bisect import bisect_left
from typing import List


def binary_search(a: List[int], x: int) -> int:
    """Index of x in sorted a, or -1. Iterative, inclusive bounds."""
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(a: List[int], x: int) -> int:
    """First index i with a[i] >= x (len(a) if none). Same as bisect_left."""
    lo, hi = 0, len(a)            # half-open range [lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    a = [-1, 0, 3, 5, 9, 12]
    assert binary_search(a, 9) == 4 and binary_search(a, 2) == -1
    for x in range(-3, 15):
        assert lower_bound(a, x) == bisect_left(a, x)
    assert lower_bound([1, 2, 2, 2, 3], 2) == 1
```

```python
from typing import Callable


def first_true(lo: int, hi: int, ok: Callable[[int], bool]) -> int:
    """Binary search on the answer: smallest x in [lo, hi] with ok(x) True.
    ok must be monotonic (False...False True...True). Returns hi + 1 if none."""
    hi += 1
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def isqrt(x: int) -> int:
    """floor(sqrt(x)) = (first m with m*m > x) - 1, integers only."""
    return first_true(0, x + 1, lambda m: m * m > x) - 1


if __name__ == "__main__":
    assert [isqrt(v) for v in (0, 1, 2, 4, 8, 9, 2**31 - 1)] == [0, 1, 1, 2, 2, 3, 46340]
    pick = 1702766719                       # "guess number" without a list
    assert first_true(1, 2**31 - 1, lambda g: g >= pick) == pick
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| — | GeeksforGeeks | [Binary Search (example)](https://www.geeksforgeeks.org/binary-search/) | [`example_recursive_binary_search.py`](example_recursive_binary_search.py) | Recursive binary search | Reference demo copied from GfG. Correct; uses `l + (r - l) // 2` (an overflow habit from C/Java, not needed in Python). The driver code runs at import time (no `__main__` guard). |
| 69 | LeetCode | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | [`leetcode_0069_sqrt_x.py`](leetcode_0069_sqrt_x.py) | Recursive search on the answer | Returns `high` when the range empties — the right floor value. Works on the tested inputs, but `x/2` makes the bounds floats; use integers (`x // 2`) to avoid float rounding surprises. The special case `x == 1` exists only because the upper bound `x/2` is too small for it. |
| 374 | LeetCode | [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) | [`leetcode_0374_guess_number.py`](leetcode_0374_guess_number.py) | Recursive binary search with oracle | The search itself is correct and never reads `arr`. ⚠ `guessNumber` builds `[1..n]` — for n ≈ 2·10⁹ that is billions of ints → out of memory / TLE. Just search the bounds `1..n`. |
| 704 | LeetCode | [Binary Search](https://leetcode.com/problems/binary-search/) | [`leetcode_0704_binary_search.py`](leetcode_0704_binary_search.py) | Recursive binary search | Correct, O(log n) time and O(log n) stack. An iterative loop or `bisect_left` is the usual contest form. |

## Pitfalls & takeaways
- Pick one convention (inclusive `[lo, hi]` with `lo <= hi`, or half-open `[lo, hi)` with `lo < hi`) and keep the updates consistent, otherwise you get infinite loops or off-by-one errors.
- Binary search on a range never needs the range materialized as a list — search the numbers, not an array of them.
- Keep bounds as integers (`//`, never `/`).
- Learn `bisect.bisect_left` / `bisect_right`: they cover lower/upper bound and counting in a range (`bisect_right(a, r) - bisect_left(a, l)`).
