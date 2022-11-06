# https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    n = len(arr)  
    cont_zero = 0
    cont_pos = 0
    cont_neg = 0
    
    for x in arr:
        if x == 0:
            cont_zero = cont_zero +1
        if x > 0:
            cont_pos = cont_pos + 1
        if x < 0:
           cont_neg = cont_neg + 1
                 
    print( round(cont_pos/n,6) )
    print( round(cont_neg/n,6) )
    print( round(cont_zero/n,6) )

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
