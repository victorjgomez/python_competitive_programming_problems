# https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true
# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#
from typing import List


def get_position_twin_costs(twin_cost: int, arr: List[int]):
    indexs_twin = [i + 1 for i in range(len(arr)) if arr[i] == twin_cost]
    return indexs_twin[:2]


def icecreamParlor(m: int, arr: List[int]):
    indexs_parlor = []
    # Write your code here
    for cost1 in arr:
        cost2 = m - cost1

        if cost1 == cost2:
            if arr.count(cost1) > 1:
                indexs_parlor = get_position_twin_costs(cost1, arr)
                break
            else:
                continue

        try:
            indexs_parlor.append(arr.index(cost1)+1)
            indexs_parlor.append(arr.index(cost2)+1)
            break
        except ValueError:
            indexs_parlor.clear()

    indexs_parlor.sort()
    indexs_parlor_str = [str(index) for index in indexs_parlor]

    return " ".join(indexs_parlor_str)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        # print(f"[135]:{arr[135]}")

        result = icecreamParlor(m, arr)

        print(result)

        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()
