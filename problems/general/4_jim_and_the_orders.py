# https://www.hackerrank.com/challenges/jim-and-the-orders/problem

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#
from typing import List


def key_func(order: List[int]):
    return order[0] + order[1]


def jimOrders(orders: List[List[int]]):
    # Write your code here
    orders.sort(key=key_func)

    return [order[2] for order in orders]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for i in range(n):
        # Adding Customer id to the order.
        orders.append(list(map(int, input().rstrip().split()+[i+1])))

    result = jimOrders(orders)
    result = [str(customer_id) for customer_id in result]
    print(" ".join(result))

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
