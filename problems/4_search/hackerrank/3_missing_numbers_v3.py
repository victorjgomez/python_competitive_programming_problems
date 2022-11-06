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
    missing = set()

    for n in brr:
        if n in arr:
            arr.remove(n)
        else:
            missing.add(n)

    missing = sorted(list(missing))
    missing_str = [str(n) for n in missing]

    return " ".join(missing_str)


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
