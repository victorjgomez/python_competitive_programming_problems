'''
Problem link:
https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
'''

'''
Steps to solve the problem.
- First step - Create a set (uniques) by transforming the list (ar).
- Second traverse the set (uniques) and find count() on the list (ar) with each
 unique value from the set.
-Third divide those values(find in the last step) between 2 and save the entire
 result at pairs variable.
- Fourth return that variable. 
'''

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    # Write your code here
    uniques = set(ar)
    pairs = 0

    for unique in uniques:
        pairs = pairs + ar.count(unique) // 2

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
