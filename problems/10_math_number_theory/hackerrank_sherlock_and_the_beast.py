# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def verify_n_divisible(n: int, d: int):
    if n % d == 0:
        return True
    return False


def generate_decent_number(n: int, d: int):
    decent_number = ''
    for i in range(n):
        decent_number = decent_number + str(d)

    return decent_number


def generate_two_numbers(n: int):
    for i in range(1, 10):
        x = int(n * i * 0.1 // 1)
        y = n - x
        # print(f'x:{x}')
        # print(f'y:{y}')
        if x % 3 == 0 and y % 5 == 0:
            return [x, y]
    return None


def decentNumber(n):
    # Write your code here
    decent_number = -1

    if verify_n_divisible(n, 3):
        decent_number = generate_decent_number(n, 5)
    elif verify_n_divisible(n, 5):
        decent_number = generate_decent_number(n, 3)
    else:
        xy = generate_two_numbers(n)

        if xy:
            decent_number = generate_decent_number(xy[0], 5) + \
                            generate_decent_number(xy[1], 3)

    return decent_number


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decentNumber(n))
