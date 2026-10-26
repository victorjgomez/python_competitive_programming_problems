# Hashing (dict, set, Counter)

## Idea
A hash table (`dict`, `set`, `collections.Counter`) answers "have I seen this?" and "how many times?" in **O(1) average** time. That turns many O(n²) "search the list again" solutions into a single O(n) pass.
`Counter` builds a frequency map in one line and supports arithmetic (`c1 - c2` keeps only positive counts), which is perfect for multiset differences.

**Use it when…**
- You need counts/frequencies: "most frequent", "appears once", "pairs", "majority".
- You check for duplicates or membership many times.
- You compare two collections as multisets (missing elements, anagrams).
- You need complements: "two numbers that sum to `m`" → look up `m - x`.
- You catch yourself calling `list.count`, `list.index`, or `x in list` inside a loop.

## Complexity
| Operation | `list` | `set` / `dict` / `Counter` |
|-----------|--------|----------------------------|
| `x in c` | O(n) | O(1) average |
| count of `x` | O(n) (`list.count`) | O(1) (`counter[x]`) |
| build from n items | — | O(n) time, O(k) space (k distinct) |
| `Counter(a) - Counter(b)` | — | O(len(a) + len(b)) |

## Simple implementation
```python
from collections import Counter
from typing import List


def single_and_majority(nums: List[int]):
    """Frequency map: element seen exactly once, and the majority (> n/2)."""
    freq = Counter(nums)                      # O(n)
    single = next((x for x in nums if freq[x] == 1), None)
    x, c = freq.most_common(1)[0]
    majority = x if c > len(nums) // 2 else None
    return single, majority


def missing_from(original: List[int], bigger: List[int]) -> List[int]:
    """Values whose count in `bigger` exceeds their count in `original`."""
    return sorted((Counter(bigger) - Counter(original)).keys())


if __name__ == "__main__":
    assert single_and_majority([2, 2, 1, 2]) == (1, 2)
    assert missing_from([7, 2, 5, 3], [7, 2, 5, 3, 5, 4]) == [4, 5]
```

```python
from typing import List, Optional, Tuple


def has_duplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


def two_sum_1based(costs: List[int], m: int) -> Optional[Tuple[int, int]]:
    """Set/dict membership for the complement, one pass, O(n)."""
    seen = {}                                 # value -> first index
    for i, c in enumerate(costs, start=1):
        if m - c in seen:
            return seen[m - c], i
        seen.setdefault(c, i)
    return None


if __name__ == "__main__":
    assert has_duplicate([1, 2, 3, 1]) and not has_duplicate([1, 2, 3])
    assert two_sum_1based([1, 4, 5, 3, 2], 4) == (1, 4)
    assert two_sum_1based([2, 2, 4, 3], 4) == (1, 2)
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 4C | Codeforces | [Registration system](https://codeforces.com/problemset/problem/4/C) | [`codeforces_4C_registration_system.py`](codeforces_4C_registration_system.py) | dict name → count | Correct, O(1) per request. The dict is a module-level global (fine for a script, not reusable). |
| 519B | Codeforces | [A and B and Compilation Errors](https://codeforces.com/problemset/problem/519/B) | [`codeforces_519B_compilation_errors.py`](codeforces_519B_compilation_errors.py) | Three Counters | ⚠ The result is sorted before printing, but the output must be *the error fixed first, then the second one*: `a=[1,1,2], b=[1,1], c=[1]` should print `2` then `1`. Simpler and order-safe: `sum(a)-sum(b)` and `sum(b)-sum(c)`. |
| — | HackerRank | [Ice Cream Parlor](https://www.hackerrank.com/challenges/icecream-parlor/problem) | [`hackerrank_ice_cream_parlor.py`](hackerrank_ice_cream_parlor.py) | `list.index` / `list.count` lookups | Handles the equal-cost case. `index`/`count` inside the loop make it O(n²); a dict of value → index (template above) makes it O(n). |
| — | HackerRank | [Lonely Integer](https://www.hackerrank.com/challenges/lonely-integer/problem) | [`hackerrank_lonely_integer_v1.py`](hackerrank_lonely_integer_v1.py) | set + `list.count` | O(n·k). Needs `OUTPUT_PATH` env var. |
| — | HackerRank | [Lonely Integer](https://www.hackerrank.com/challenges/lonely-integer/problem) | [`hackerrank_lonely_integer_v2.py`](hackerrank_lonely_integer_v2.py) | Counter | O(n) — improvement over v1. XOR of all values is O(1) space. Needs `OUTPUT_PATH`. |
| — | HackerRank | [Migratory Birds](https://www.hackerrank.com/challenges/migratory-birds/problem) | [`hackerrank_migratory_birds.py`](hackerrank_migratory_birds.py) | `Counter.most_common(1)` | ⚠ On ties `most_common` keeps first-seen order, not smallest id: `[4,4,1,1]` returns 4, expected 1. Use `min(c, key=lambda t: (-c[t], t))`. |
| — | HackerRank | [Missing Numbers](https://www.hackerrank.com/challenges/missing-numbers/problem) | [`hackerrank_missing_numbers_v1.py`](hackerrank_missing_numbers_v1.py) | `list.count` per element | O(m·(n+m)). |
| — | HackerRank | [Missing Numbers](https://www.hackerrank.com/challenges/missing-numbers/problem) | [`hackerrank_missing_numbers_v2.py`](hackerrank_missing_numbers_v2.py) | `brr.remove` for each of `arr` | Still O(n·m) (`remove` is linear) and mutates the input. |
| — | HackerRank | [Missing Numbers](https://www.hackerrank.com/challenges/missing-numbers/problem) | [`hackerrank_missing_numbers_v3.py`](hackerrank_missing_numbers_v3.py) | `in` + `arr.remove` | Same O(n·m) as v2, mutates `arr`. |
| — | HackerRank | [Missing Numbers](https://www.hackerrank.com/challenges/missing-numbers/problem) | [`hackerrank_missing_numbers_v4.py`](hackerrank_missing_numbers_v4.py) | `Counter(brr) - Counter(arr)` | Best version: O(n + m + k log k). |
| — | HackerRank | [Sales by Match](https://www.hackerrank.com/challenges/sock-merchant/problem) | [`hackerrank_sales_by_match.py`](hackerrank_sales_by_match.py) | set + `list.count` | Correct, O(n·k); `sum(v // 2 for v in Counter(ar).values())` is O(n). Needs `OUTPUT_PATH`. |
| — | HackerRank | [Sherlock and the Valid String](https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem) | [`hackerrank_sherlock_valid_string.py`](hackerrank_sherlock_valid_string.py) | Frequency list sorted by count; try removing from min / max | The logic (all equal, or drop one from the smallest/largest count) is right. ⚠ `get_list_dict_count_c` iterates over the global `s` instead of its parameter, so it only works when run as a script. A list of one-key dicts is awkward — `Counter(Counter(s).values())` gives "count of counts" directly. |
| 26 | LeetCode | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [`leetcode_0026_remove_duplicates_sorted_array.py`](leetcode_0026_remove_duplicates_sorted_array.py) | set + sort | ⚠ Rebinds `nums` to a new list, so the caller's array is never modified → fails the judge (it checks the first k elements). Intended solution: read/write two pointers, O(n), O(1) space. |
| 136 | LeetCode | [Single Number](https://leetcode.com/problems/single-number/) | [`leetcode_0136_single_number.py`](leetcode_0136_single_number.py) | Counter | Correct O(n) time, O(n) space. Follow-up asks O(1) space → XOR all numbers. |
| 169 | LeetCode | [Majority Element](https://leetcode.com/problems/majority-element/) | [`leetcode_0169_majority_element.py`](leetcode_0169_majority_element.py) | Counter | Correct O(n). Boyer–Moore voting does it in O(1) space. |
| 217 | LeetCode | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [`leetcode_0217_contains_duplicate.py`](leetcode_0217_contains_duplicate.py) | set size vs list size | Correct O(n). ⚠ The URL comment points to *majority-element*; the return type hint says `int` but it returns `bool`. |
| 387 | LeetCode | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | [`leetcode_0387_first_unique_character.py`](leetcode_0387_first_unique_character.py) | Counter + deque + `list.index` | Correct and O(n). The deque and the final `index` are unnecessary: `for i, c in enumerate(s): if cnt[c] == 1: return i`. |

## Pitfalls & takeaways
- `list.count`, `list.index`, `list.remove` and `x in list` are all O(n); inside a loop they make the solution O(n²). Build a `Counter`/`set` once.
- `Counter.most_common` breaks ties by insertion order — if the statement asks for the smallest value on ties, sort explicitly.
- Assigning to a parameter (`nums = ...`) never changes the caller's list; use `nums[:] = ...` or write in place.
- Helpers should use their parameters, not globals from `__main__` — it hides bugs until the function is reused.
