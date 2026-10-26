# Strings

## Idea
Python strings are **immutable**: every `s + c`, `s[1:]` or `s.replace(...)` creates a new string. Good string solutions therefore scan with indices (or pointers) instead of slicing repeatedly, and build output by collecting pieces in a list and calling `"".join(...)` once.
Most easy/medium string problems reduce to: a single left-to-right scan with a counter or balance, two pointers from both ends (palindromes), a frequency count (anagrams), or a lookup table (Roman numerals, codes).

**Use it when…**
- You need to compare/transform characters (palindrome, anagram, prefix, decoding).
- The statement talks about "balanced", "matching", or "substring/pattern occurrence".
- You build a new string character by character (use a list + `join`).
- Input length is large (10⁴–10⁵): slicing in a loop or recursion per character will be too slow or overflow the stack.

## Complexity
| Operation | Time |
|-----------|------|
| Index `s[i]`, `len(s)` | O(1) |
| Slice `s[a:b]`, `s + t`, `s.replace` | O(length) — creates a copy |
| Build with list + `"".join` | O(total length) |
| Building with `+=` in a loop | up to O(n²) |
| Two-pointer palindrome check | O(n) time, O(1) space |
| Naive pattern search | O(n·m); KMP / Z-function: O(n + m) |

## Simple implementation
```python
def decode_runs(s: str) -> str:
    """Build a string efficiently: 'a3b2' -> 'aaabb' (single-digit counts)."""
    parts = []
    for i in range(0, len(s), 2):
        parts.append(s[i] * int(s[i + 1]))
    return "".join(parts)          # one join instead of many += copies


def is_palindrome(s: str) -> bool:
    """Ignore non-alphanumeric chars and case, two pointers, O(1) space."""
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


if __name__ == "__main__":
    assert decode_runs("a3b2") == "aaabb"
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("ab_a")           # '_' is not alphanumeric
    assert not is_palindrome("race a car")
```

```python
def balanced_split(s: str) -> int:
    """LeetCode 1221: greedy, cut every time the balance returns to 0."""
    balance = count = 0
    for c in s:
        balance += 1 if c == "R" else -1
        if balance == 0:
            count += 1
    return count


if __name__ == "__main__":
    assert balanced_split("RLRRLLRLRL") == 4
    assert balanced_split("RLRRRLLRLL") == 2
    assert balanced_split("LLLLRRRR") == 1
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 32B | Codeforces | [Borze](https://codeforces.com/problemset/problem/32/B) | [`codeforces_32B_borze.py`](codeforces_32B_borze.py) | Chained `str.replace` | Correct because the order is `"--"`, then `"-."`, then `"."` (replacing `"."` first would break the codes). A left-to-right scan is the more general technique for prefix codes. |
| — | Interview exercise | Pattern searching | [`exercise_pattern_searching.py`](exercise_pattern_searching.py) | Naive sliding comparison | ⚠ The comparison hardcodes 4 characters, so it only works for patterns of length 4 (the statement says the pattern may change). Use `text[i:i+m] == pattern`. ⚠ `input = input()` shadows the built-in. |
| 13 | LeetCode | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [`leetcode_0013_roman_to_integer.py`](leetcode_0013_roman_to_integer.py) | Right-to-left scan, subtract if smaller than previous | Correct idea. Recursion with `s_list[1:]` copies the list each call (O(n²)); fine here because n ≤ 15, but a simple loop is clearer. |
| 14 | LeetCode | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | [`leetcode_0014_longest_common_prefix.py`](leetcode_0014_longest_common_prefix.py) | Recursive vertical scan | Correct, but every level slices every string. Iterating over index `i` of the shortest string (or `os.path.commonprefix`) avoids the copies. |
| 28 | LeetCode | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | [`leetcode_0028_find_index_first_occurrence.py`](leetcode_0028_find_index_first_occurrence.py) | Naive search + recursive char compare | O(n·m) and slices `haystack[i:]` at every position. ⚠ Recursion depth = `len(needle)` (up to 10⁴) can exceed Python's default limit of 1000. `haystack.find(needle)` or KMP. |
| 125 | LeetCode | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [`leetcode_0125_valid_palindrome.py`](leetcode_0125_valid_palindrome.py) | Regex clean-up + recursive two pointers | Cleaning with `\W` + removing `_` is correct. ⚠ Recursion goes until `j < 0` (n levels, checks every pair twice) → `RecursionError` for long inputs (up to 2·10⁵). Stop at `i >= j` and use a loop. |
| 242 | LeetCode | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [`leetcode_0242_valid_anagram.py`](leetcode_0242_valid_anagram.py) | Sort + recursive compare | Sorting is a valid O(n log n) idea. ⚠ The recursive compare slices lists (O(n²)) and recurses n times (n up to 5·10⁴ → `RecursionError`). `sorted(s) == sorted(t)` or `Counter(s) == Counter(t)`. |
| 1221 | LeetCode | [Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/) | [`leetcode_1221_split_balanced_strings.py`](leetcode_1221_split_balanced_strings.py) | Window search for `X…XY…Y` blocks, zero-filling | ⚠ Gives wrong answers: `"RLRRRLLRLL"` → 3 (expected 2), `"RRLRLL"` → 3 (expected 1), because zeroing inner blocks does not produce a contiguous split. State is stored in class attributes (shared by every instance). The greedy balance counter above is O(n). |
| 1859 | LeetCode | [Sorting the Sentence](https://leetcode.com/problems/sorting-the-sentence/) | [`leetcode_1859_sorting_the_sentence.py`](leetcode_1859_sorting_the_sentence.py) | `sort(key=last digit)` + `join` | Clean and correct, O(n log n). Nice use of a key function. |

## Pitfalls & takeaways
- Recursion over characters is elegant but Python's recursion limit is ~1000; for string problems prefer loops.
- `s[1:]` inside a loop or recursion turns O(n) algorithms into O(n²) — pass indices instead.
- For "balanced"/"matching" problems, think of a running counter (or a stack) before searching for substrings.
- Test the examples from the statement *exactly*; the 1221 notes in the file list an expected answer of 3 for an input whose correct answer is 2.
