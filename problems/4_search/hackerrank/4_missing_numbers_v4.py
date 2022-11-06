# https://www.hackerrank.com/challenges/missing-numbers/problem
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
from collections import Counter
from typing import List


def missingNumbers(arr: List[int], brr: List[int]):
    # Write your code here
    a = Counter(arr)
    b = Counter(brr)
    return sorted((b - a).keys())


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result_int = missingNumbers(arr, brr)
    result_str = [str(n) for n in result_int]
    print(" ".join(result_str))

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
