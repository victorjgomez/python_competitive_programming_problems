"""
problem:
https://codeforces.com/problemset/problem/1213/B

solution:
https://www.youtube.com/watch?v=CDZE-_Fj6WU&ab_channel=codedsun

"""
from typing import List


def pop_possibles_bad_prices(possibles_bad_prices: List[int],
                             list_ids_to_pop: List[int]):
    cont = 0
    for i in list_ids_to_pop:
        possibles_bad_prices.pop(i-cont)
        cont += 1


def solution(prices: List[int]):
    number_day_bad_prices = 0
    possibles_bad_prices = []

    for price in prices:
        list_ids_to_pop = []
        for i in range(len(possibles_bad_prices)):
            if price < possibles_bad_prices[i]:
                list_ids_to_pop.append(i)
                number_day_bad_prices += 1

        pop_possibles_bad_prices(possibles_bad_prices, list_ids_to_pop)
        possibles_bad_prices.append(price)

    return number_day_bad_prices


if __name__ == "__main__":
    t = int(input())

    while t:
        n = int(input())
        prices_str = input()
        prices = [int(h) for h in prices_str.split()]
        print(solution(prices))
        t -= 1
