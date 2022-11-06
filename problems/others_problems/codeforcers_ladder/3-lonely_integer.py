'''
Problem link:
https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
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


def lonelyinteger(ar):
    # Write your code here
    uniques = set(ar)

    for unique in uniques:
        if ar.count(unique) == 1:
            return unique

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = lonelyinteger(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
