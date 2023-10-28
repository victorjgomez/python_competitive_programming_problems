#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

import datetime


def dayOfProgrammer(year):
    # Write your code here
    day: int = 13
    month: int = 9

    if year == 1918:
        day = day + 13

    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            day = day - 1

    if year >= 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            day = day - 1

    date = datetime.datetime(day=day, month=month, year=year)

    return f"{date.day}.0{date.month}.{date.year}"


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result + '\n')

    #fptr.close()
