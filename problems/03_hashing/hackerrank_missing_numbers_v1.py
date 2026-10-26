#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#
from typing import List


def missingNumbers(arr: List[int], brr: List[int]):
    # Write your code here
    missing_numbers = []

    for b in brr:
        if b not in missing_numbers:
            if arr.count(b) < brr.count(b):
                missing_numbers.append(b)

    missing_numbers.sort()
    missing_numbers_str = [str(number) for number in missing_numbers]

    return " ".join(missing_numbers_str)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
