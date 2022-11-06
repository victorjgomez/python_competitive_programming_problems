# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings

# !/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def fun_key_sort_dict(dict: {str: int}):
    return list(dict.values())[0]


def validate(list_dict_count_c):
    list_count = [list(dict.values())[0] for dict in list_dict_count_c]
    if list_count.count(list_count[0]) == len(list_count):
        return True
    return False


def get_list_dict_count_c(list_c : List[str]):
    list_dict_count_c = []
    for c in s:
        keys = [list(dict.keys())[0] for dict in list_dict_count_c]
        if c not in keys:
            list_dict_count_c.append({c: list_c.count(c)})

    list_dict_count_c.sort(key=fun_key_sort_dict)

    return list_dict_count_c


def validate_decreasing_greater(list_dict_count_c: List[dict], n):
    key = list(list_dict_count_c[n].keys())[0]
    list_dict_count_c[n][key] = list_dict_count_c[n][key] - 1

    if validate(list_dict_count_c):
        return True
    return False


def validate_decreasing_lower(list_dict_count_c: List[dict]):
    key = list(list_dict_count_c[0].keys())[0]
    list_dict_count_c[0][key] = list_dict_count_c[0][key] - 1

    if list_dict_count_c[0][key] == 0:
        return validate(list_dict_count_c[1:])

    return validate(list_dict_count_c)


def isValid(s):
    # Write your code here
    list_c = [c for c in s]
    list_dict_count_c = get_list_dict_count_c(list_c)
    n = len(list_dict_count_c) - 1

    list_dict_count_c_copy_1 = [dict.copy() for dict in list_dict_count_c]
    list_dict_count_c_copy_2 = [dict.copy() for dict in list_dict_count_c]

    if validate(list_dict_count_c) or \
            validate_decreasing_lower(list_dict_count_c_copy_1) or \
            validate_decreasing_greater(list_dict_count_c_copy_2, n):
        return "YES"



    return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
