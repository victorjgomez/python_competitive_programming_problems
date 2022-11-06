# https://www.hackerrank.com/challenges/grid-challenge/problem

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
from typing import List


def verify_arr(arr: List[str]):
    arr_copy = arr.copy()
    arr_copy.sort()

    if arr_copy == arr:
        return True

    return False


def verify_arrays(arrays: List[List[str]]):
    for arr in arrays:
        if not verify_arr(arr):
            return "NO"

    return "YES"


def transform_grid_into_columns(rows: List[List[str]]):
    columns = []
    n = len(rows[0])

    for i in range(n):
        column = []
        for row in rows:
            column.append(row[i])
        columns.append(column)

    return columns

def rearrange_rows(rows: List[List[str]]):
    for row in rows:
        row.sort()

def transform_grid_into_rows(grid: List[str]):
    rows = []

    for row in grid:
        rows.append([c for c in row])

    return rows


def gridChallenge(grid: List[str], n: int):
    # Write your code here
    rows = transform_grid_into_rows(grid)
    rearrange_rows(rows)
    columns = transform_grid_into_columns(rows)

    return verify_arrays(rows+columns)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid, n)

        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
