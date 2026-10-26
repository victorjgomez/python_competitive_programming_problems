from typing import List


# https://matcomgrader.com/problem/9696/carrying-pumpkins/

# tail_recursion.py
# https://chrispenner.ca/posts/python-tail-recursion#:~:text=Some%20programming%20languages%20are%20tail,only%20a%20call%20to%20itself.

def solution(ws, q):
    filter_ws = filter_greater_than_q(ws, q)

    ways = get_all_ways(filter_ws, len(filter_ws))

    filter_ways = filter_ways_greater_than_q(ways, q)

    return len(filter_ways)


# def fact(n: int):
#     result = 1
#
#     for i in range(2, n+1):
#         result *= i
#
#     return result
#
# def permutation(n: int):
#     return fact(n)

def sum(way):
    suma = 0
    for e in way:
        suma += e
    return suma
def filter_ways_greater_than_q(ways, q):
    filter_ways = []

    for way in ways:
        if sum(way) <= q:
            filter_ways.append(way)

    return filter_ways


def filter_greater_than_q(ws, q):
    filter_ws = []

    for w in ws:
        if w <= q:
            filter_ws.append(w)

    return filter_ws


def get_ways_by_amount_elem(ws, amount_elem):
    ways = []

    if (amount_elem == 1):
        for element in ws:
            ways.append([element])

    else:
        stop1 = len(ws) - (amount_elem-1)
        for i in range(0, stop1):
                take_result = take(amount_elem - 1, ws[i+1:])
                take_result.append(ws[i])
                ways.append(take_result)

    return ways


def take(amount, list):
    acc = []
    cont = 1

    for element in list:
        if cont > amount:
            break

        acc.append(element)
        cont += 1

    return acc



def get_all_ways(ws, n):
    ways = []

    for amount_elem in range(1, n+1):
        ways = ways + get_ways_by_amount_elem(ws, amount_elem)

    return ways



if __name__ == "__main__":
    input1 = list(map(int, input().rstrip().split()))
    ws = list(map(int, input().rstrip().split()))
    qs = list(map(int, input().rstrip().split()))

    for q in qs:
        result = solution(ws, q)
        print(result)






