from typing import List


# https://vjudge.net/problem/UVA-11389


def get_minimum_possible_amount(n: int, d: int, r: int, morning_routes: List[int], evening_routes: List[int]):
    morning_routes.sort()
    evening_routes.sort(reverse=True)
    overtime: int = 0

    for i in range(0, n):
        if morning_routes[i] + evening_routes[i] > d:
            overtime = overtime + (morning_routes[i] + evening_routes[i] - d) * r

    return overtime


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while (True):
        input1 = input()
        input1_list = input1.split(" ")
        n: int = int(input1_list[0])
        d: int = int(input1_list[1])
        r: int = int(input1_list[2])

        if n == 0 and d == 0 and r == 0:
            break

        input2 = input()
        morning_routes: List[int] = input2.split(" ")
        morning_routes = [int(x) for x in morning_routes]
        input3 = input()
        evening_routes: List[int] = input3.split(" ")
        evening_routes = [int(x) for x in evening_routes]

        print(get_minimum_possible_amount(n, d, r, morning_routes, evening_routes))
