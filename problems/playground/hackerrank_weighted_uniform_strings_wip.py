#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Set


#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#


def weightedUniformStrings(s, queries):
    # Write your code here




if __name__ == '__main__':
    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)


