# https://www.hackerrank.com/challenges/sherlock-and-array/problem?isFullScreen=true

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from typing import List


def sum(arr: List[int]):
    sum = 0
    for number in arr:
        sum = sum + number
    return sum


def verify(sum_left: int, sum_right: int):
    if sum_left == sum_right:
        return True
    return False


def balancedSums(arr: List[int]):
    # Write your code here
    n = len(arr)

    sum_left = 0
    sum_right = 0

    for i in range(n):
        if i == 0:
            sum_left = 0
            sum_right = sum(arr[1:])
            if verify(sum_left, sum_right):
                return "YES"
        elif i == n-1:
            sum_left = sum_left + arr[i-1]
            sum_right = 0
            if verify(sum_left, sum_right):
                return "YES"
        else:
            sum_left = sum_left + arr[i-1]
            sum_right = sum_right - arr[i]
            if verify(sum_left, sum_right):
                return "YES"
    return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
