# https://www.hackerrank.com/challenges/two-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations


#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    a_sort = sorted(A)
    b_sort = sorted(B, reverse=True)

    if check(k, a_sort, b_sort):
        return "YES"

    return "NO"


def check(k, A, B):
    for i in range(0, len(A)):
        if A[i] + B[i] < k:
            return False

    return True


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        print(result)
        #fptr.write(result + '\n')

    #fptr.close()
