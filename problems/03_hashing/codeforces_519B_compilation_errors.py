# https://codeforces.com/problemset/problem/519/B

"""
I make this problem but I dont understand why in some inputs they are no given
    the second and third compilation.
"""

from collections import Counter
from typing import List


def solution(arr: List[int], brr: List[int], crr: List[int]) -> List[int]:
    solution_set = []
    dict_arr = Counter(arr)
    dict_brr = Counter(brr)
    dict_crr = Counter(crr)

    for a in dict_arr.keys():
        if dict_brr.get(a) is None:
            solution_set.append(a)
        elif dict_crr.get(a) is None:
            solution_set.append(a)
        elif dict_brr.get(a) < dict_arr.get(a):
            solution_set.append(a)
        elif dict_crr.get(a) < dict_arr.get(a):
            solution_set.append(a)

    return solution_set


if __name__ == "__main__":
    n = int(input())
    arr = input()
    arr = [int(a) for a in arr.split()]

    brr = input()
    brr = [int(b) for b in brr.split()]

    crr = input()
    crr = [int(c) for c in crr.split()]

    solution_set = solution(arr, brr, crr)
    solution_set.sort()

    print(f'{solution_set[0]} \n{solution_set[1]}')
