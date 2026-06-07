# https://www.hackerrank.com/contests/club-programacion-competitiva-2do-contest-24062022/challenges/marcs-cakewalk

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#
from typing import List


def cal_miles(calories: List[int]):
    miles = 0
    for j in range(len(calories)):
        miles = miles + (2**j)*calories[j]

    return miles


def marcsCakewalk(calories: List[int]):
    # Write your code here
    calorie.sort(reverse=True)
    return cal_miles(calories)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
