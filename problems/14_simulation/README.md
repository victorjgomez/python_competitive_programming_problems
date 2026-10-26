# Simulation & Implementation

## Idea
Some problems have no clever trick: the statement describes a process, and you just carry it out step by step exactly as written. The difficulty is in **reading carefully** (edge cases, input format, output format) and choosing data structures that keep each step cheap. Before coding, check that the number of steps times the cost of each step fits the time limit (about 10^7 simple operations per second in Python).

**Use it when…**
- The statement says "each second / each round / in turn, do X" and the limits are small (n, t ≤ 10^3 or so).
- The task is "compute this formula / count these things / format this output" (easy implementation problems).
- There are calendar, date or string-formatting rules to follow exactly.
- A queue of people/objects moves according to rules (use `collections.deque`).

## Complexity
- Typically O(steps × cost per step). Example: t rounds over a string of length n is O(n·t).
- Use `deque.popleft()` (O(1)) instead of `list.pop(0)` (O(n)).
- Copying a list/dict inside a loop silently adds an O(n) factor.

## Simple implementation
```python
import sys


def read_ints():
    """Fast input: one line -> list of ints."""
    return list(map(int, sys.stdin.readline().split()))


def simulate_queue(s: str, t: int) -> str:
    """Codeforces 266B: each second every 'BG' becomes 'GB' (all at once)."""
    q = list(s)
    for _ in range(t):
        i = 0
        while i < len(q) - 1:
            if q[i] == "B" and q[i + 1] == "G":
                q[i], q[i + 1] = q[i + 1], q[i]
                i += 2                 # skip the girl we just moved
            else:
                i += 1
    return "".join(q)


def main():
    n, t = read_ints()
    s = sys.stdin.readline().strip()
    sys.stdout.write(simulate_queue(s, t) + "\n")   # one write = fast output


if __name__ == "__main__":
    assert simulate_queue("BGGBG", 1) == "GBGGB"
    assert simulate_queue("BGGBG", 2) == "GGBGB"
    assert simulate_queue("GGGB", 1) == "GGGB"
    print("ok")    # replace with main() when submitting
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 266B | Codeforces | [Queue at the School](https://codeforces.com/problemset/problem/266/B) | [`codeforces_266B_queue_at_the_school.py`](codeforces_266B_queue_at_the_school.py) | Simulate t passes, swap `BG`→`GB`, skip 2 after a swap | Correct, O(n·t). Uses `try/except IndexError` for the last position; looping to `n - 1` is clearer. |
| — | HackerRank | [A Very Big Sum](https://www.hackerrank.com/challenges/a-very-big-sum/problem) | [`hackerrank_a_very_big_sum.py`](hackerrank_a_very_big_sum.py) | Plain sum | Python ints are arbitrary precision, so there is no overflow (the point of the problem in C/Java). Needs the `OUTPUT_PATH` env var (HackerRank stub) to run locally. |
| — | HackerRank | [Day of the Programmer](https://www.hackerrank.com/challenges/day-of-the-programmer/problem) | [`hackerrank_day_of_the_programmer.py`](hackerrank_day_of_the_programmer.py) | Calendar rules | Julian leap years (÷4) up to 1917, Gregorian (÷400 or ÷4 and not ÷100) after; 1918 skipped 13 days, so the answer is 26.09.1918. Prints an extra blank line (`result + '\n'` with `print`). |
| — | HackerRank | [Plus Minus](https://www.hackerrank.com/challenges/plus-minus/problem) | [`hackerrank_plus_minus.py`](hackerrank_plus_minus.py) | Count positives / negatives / zeros | `round(x, 6)` can print `0.5` instead of `0.500000`; accepted thanks to the checker's tolerance, but `f"{x:.6f}"` matches the expected format exactly. |
| 9695 | MatcomGrader | [Bus](https://matcomgrader.com/problem/9695/bus/) | [`matcom_9695_bus.py`](matcom_9695_bus.py) | `deque` simulation stop by stop, exit side by position | Copies the dicts on every passenger and scans the deque with `remove`, so it is O(n²); fine for small n, slow for large inputs. |
| 9696 | MatcomGrader | [Carrying Pumpkins](https://matcomgrader.com/problem/9696/carrying-pumpkins/) | [`matcom_9696_carrying_pumpkins.py`](matcom_9696_carrying_pumpkins.py) | Enumerate subsets, count those with sum ≤ q | ⚠ Subset generation via `take()` is incorrect: for each start it only takes the next *contiguous* elements, so most subsets are missed. Use `itertools.combinations` or a bitmask (still O(2^n), small n only). Also shadows the built-in `sum`. |
| — | Exercise | Make matrix row/column sums even | [`exercise_make_matrix_sums_even.py`](exercise_make_matrix_sums_even.py) | Repeat adjustment passes until stable | ⚠ The loops use `x` for columns and `y` for rows, but the update is `matrix[x][y]` (should be `matrix[y][x]`), which edits the wrong cell or raises `IndexError` when r ≠ c. |

## Pitfalls & takeaways
- Re-read the statement for simultaneity: "all swaps happen at the same time" is why 266B skips an index after a swap.
- Estimate steps × cost first; hidden O(n) operations (`list.remove`, `dict.copy()`, `list.pop(0)`, string `+=`) turn a fine simulation into a TLE.
- Output format matters: fixed decimals, leading zeros in dates (`09`), no extra blank lines.
- Python ints never overflow, but floats do lose precision; keep counts as ints and divide only at the end.
