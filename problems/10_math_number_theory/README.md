# Math & Number Theory

## Idea
Many problems look like simulations but have a direct mathematical answer: primes, divisibility, gcd/lcm, modular arithmetic, digit manipulation, or a closed formula. The core toolbox has four parts:
- a **sieve** for many primality queries up to N
- **trial division up to √n** for factoring a single number
- **Euclid's gcd**
- **fast modular exponentiation**

Doing the math first usually turns an O(n) or O(n²) loop into O(√n), O(log n), or O(1).

**Use it when…**
- The statement mentions primes, divisors, factors, gcd/lcm, "modulo 10⁹+7", or check digits.
- n is huge (10⁹–10¹⁸), so you can't loop over every number up to n, but √n or log n steps are fine.
- You are asked to build the "largest/smallest number" from digits under some constraint (often greedy plus divisibility).
- Small cases show a pattern you can turn into a formula.

## Complexity
| Tool | Time | Space |
|------|------|-------|
| Sieve of Eratosthenes up to N | O(N log log N) | O(N) |
| Trial-division factorization of n | O(√n) | O(log n) |
| `math.gcd(a, b)` (Euclid) | O(log min(a, b)) | O(1) |
| `pow(a, b, m)` (binary exponentiation) | O(log b) | O(1) |

## Simple implementation
```python
from math import gcd, isqrt


def sieve(n: int):
    """is_prime[i] for 0..n (inclusive)."""
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            is_prime[p * p :: p] = [False] * len(range(p * p, n + 1, p))  # slice assignment is fast
    return is_prime


def factorize(n: int):
    """Prime factors with multiplicity, O(sqrt(n))."""
    factors, d = [], 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:                        # whatever is left is a prime > sqrt(original n)
        factors.append(n)
    return factors


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b        # divide first to keep numbers small


if __name__ == "__main__":
    assert [i for i, p in enumerate(sieve(30)) if p] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert factorize(13195) == [5, 7, 13, 29] and factorize(17) == [17]
    assert max(factorize(600851475143)) == 6857          # fast even for 10^12
    assert gcd(12, 18) == 6 and lcm(4, 6) == 12
    assert pow(2, 10**18, 10**9 + 7) == pow(2, 10**18 % (10**9 + 6), 10**9 + 7)  # Fermat
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 1 | — | Contest 2021, Problem A (source unidentified) | [`contest_2021_problem_a.py`](contest_2021_problem_a.py) | Closed-form formula | Finds the smallest x with `(-1)^x·x·p + k ≥ m`. It tests x = 1, then the smallest even x = 2·⌈(m−k)/(2p)⌉, and falls back to 2. O(1) per test. ⚠ `math.ceil(a / b)` uses float division and can be off for very large values. `-(-a // b)` is the exact integer ceiling. |
| 2 | — | Fito's Gift (Luhn check digit; likely MatcomGrader) | [`exercise_fitos_gift_luhn.py`](exercise_fitos_gift_luhn.py) | Luhn checksum + brute-force digit | When the missing `x` is the check digit, it uses the closed form `sum·9 mod 10`. Otherwise it tries all 10 digits, which is O(10·n) and perfectly fine. `get_value_to_sum` is just "sum the digits of a 2-digit number" (`d - 9` when `d > 9`). |
| 3 | LeetCode | [66. Plus One](https://leetcode.com/problems/plus-one/) | [`leetcode_0066_plus_one.py`](leetcode_0066_plus_one.py) | Convert to int and back | Works because Python ints are unbounded. The intended solution walks from the last digit and propagates the carry in O(n) without conversion. That approach also works in languages with fixed-size ints. |
| 4 | LeetCode | [1323. Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/) | [`leetcode_1323_maximum_69_number.py`](leetcode_1323_maximum_69_number.py) | Brute force: flip each digit | Correct, O(d²) over at most 4 digits. Greedy insight: flipping the **first** `6` is always best, so `int(str(num).replace("6", "9", 1))` is enough. |
| 5 | HackerRank | [Sherlock and The Beast](https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem) | [`hackerrank_sherlock_and_the_beast.py`](hackerrank_sherlock_and_the_beast.py) | Divisibility + heuristic split | ⚠ When `n % 5 == 0` it returns all 3s without trying mixes first. For n = 20 the right answer is fifteen 5s followed by five 3s. ⚠ The split only tries `x = ⌊n·i/10⌋` for i = 1..9, so it is not exhaustive. n = 26 should be 21 fives + 5 threes, but the code returns -1. Correct approach: take the largest x ≤ n with `x % 3 == 0` and `(n − x) % 5 == 0` (check at most 3 candidates), then build the answer as `"5"*x + "3"*(n-x)`. |
| 6 | HackerRank | [Megaprime Numbers](https://www.hackerrank.com/challenges/megaprime-numbers/problem) | [`hackerrank_megaprime_numbers.py`](hackerrank_megaprime_numbers.py) | Primality via gcd with running product of primes | Neat idea: an odd number is prime iff it is coprime to the product of all smaller primes. ⚠ It doesn't scale. The product grows to thousands of digits, and the boolean list has `last + 1` entries, while `last` goes up to 10¹⁵. Better: generate only the numbers whose digits are all in {2, 3, 5, 7} within [first, last], then test each one (trial division or Miller–Rabin). |
| 7 | HackerRank | [Project Euler #3: Largest prime factor](https://www.hackerrank.com/challenges/euler003/problem) | [`hackerrank_largest_prime_factor_v1.py`](hackerrank_largest_prime_factor_v1.py) | Sieve by `list.remove` | Builds every prime ≤ n by removing multiples from a list while iterating over it. That is O(n²)-ish and O(n) memory. ⚠ n goes up to 10¹², so it times out or runs out of memory, and n = 1 raises `IndexError`. |
| 8 | HackerRank | [Project Euler #3: Largest prime factor](https://www.hackerrank.com/challenges/euler003/problem) | [`hackerrank_largest_prime_factor_v2.py`](hackerrank_largest_prime_factor_v2.py) | Boolean sieve | Faster than v1 thanks to a real boolean sieve. ⚠ `range(n)` excludes n itself, so a **prime input** prints nothing (the `ValueError` is silently skipped). It still needs O(n) memory. |
| 9 | HackerRank | [Project Euler #3: Largest prime factor](https://www.hackerrank.com/challenges/euler003/problem) | [`hackerrank_largest_prime_factor_v3.py`](hackerrank_largest_prime_factor_v3.py) | Boolean sieve + `list.remove` | Fixes v2's off-by-one (it sieves `0..n`) and takes the first divisor from a descending prime list. ⚠ `prime_list.remove(i)` is O(n) per call, so it gets slow again, and none of v1–v3 can reach 10¹². You don't need a sieve here: trial division up to √n with `n //= d` is O(√n) ≈ 10⁶ steps (see `factorize`). |

## Pitfalls & takeaways
- To factor **one** big number, use trial division up to √n. A sieve only pays off for many queries up to a moderate N (≤ ~10⁷).
- Watch the boundaries: `range(n)` vs `range(n + 1)`, and the leftover `n > 1` after trial division, which is itself a prime factor.
- Use integer arithmetic (`//`, `-(-a // b)`, `math.isqrt`) instead of floats like `math.sqrt`, `/`, or `0.1`. Floats lose precision on large inputs.
- Look for the greedy or closed-form insight (flip the first 6; maximize the number of 5s subject to divisibility) before you write a brute force.
