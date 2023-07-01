# https://vjudge.net/problem/UVA-10037

from typing import List


def solution(left_side: List[int], right_side: List[int],
             result: List[List[int]], first_time: bool = True,
             light_left: bool = True, cont_rest: int = 0) -> List[List[int]]:
    if len(left_side) == 0:
        return result
    elif cont_rest == 2:
        return solution(left_side, right_side, result, True, True, 0)
    elif first_time:
        left_side.sort()
        right_side.append(left_side[0])
        right_side.append(left_side[1])
        result.append([left_side[0], left_side[1]])

        return solution(left_side[2:], right_side, result, False, False,
                        cont_rest)
    elif light_left:
        left_side.sort(reverse=True)
        right_side.append(left_side[0])
        right_side.append(left_side[1])
        result.append([left_side[1], left_side[0]])

        return solution(left_side[2:], right_side, result, False, False,
                        cont_rest)
    else:
        right_side.sort()
        left_side.append(right_side[0])
        result.append([right_side[0]])

        return solution(left_side, right_side[1:], result, False, True,
                        cont_rest+1)


def get_total(result: List[List[int]]) -> int:
    cost: int = 0

    for i in result:
        cost = cost + max(i)

    return cost


def print_result(result: List[List[int]]):
    for i in result:
        for j in i:
            print(f"{j} ", end="")
        print("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t: int = int(input())

    while t > 0:
        string = input()
        while string == "":
            string = input()

        n: int = int(string)

        left_side = []

        for _ in range(0, n):
            x: int = int(input())
            left_side.append(x)

        result: List[List[int]] = solution(left_side, [], [])

        print(get_total(result))
        print_result(result)
        print(" ")

        t -= 1
