"""
problem:
https://codeforces.com/problemset/problem/1213/B

solution:
https://www.youtube.com/watch?v=CDZE-_Fj6WU&ab_channel=codedsun

"""
from typing import List


def solution(prices: List[int], n: int):
    number_day_bad_prices = 0
    min = prices[n - 1]

    for i in range(n - 2, -1, -1):
        if prices[i] > min:
            number_day_bad_prices += 1
        elif prices[i] < min:
            min = prices[i]

    return number_day_bad_prices


if __name__ == "__main__":
    t = int(input())

    while t:
        n = int(input())
        prices_str = input()
        prices = [int(h) for h in prices_str.split()]
        print(solution(prices, n))
        t -= 1
