#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#


# def rotateLeft(d, arr):
#     # Write your code here
#     if d == 0:
#         return arr
#     else:
#         new_arr = arr[1:]
#         new_arr.append(arr[0])
#         return rotateLeft(d-1, new_arr)

def rotateLeft(d, arr):
    # Write your code here
    while d > 0:
        new_arr = arr[1:]
        new_arr.append(arr[0])
        arr = new_arr
        d = d - 1

    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
