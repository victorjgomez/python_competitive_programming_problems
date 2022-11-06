import math


def h_fuction(x: int, p: int, k: int):
    return (-1) ** x * x * p + k


def verify_condition(x: int, p: int, k: int, m: int):
    h = h_fuction(x, p, k)
    if h >= m:
        return True
    return False


def calculate_s(p: int, k: int, m: int):
    numerator = m - k
    denominator = 2 * p
    return math.ceil(numerator / denominator)  # Calculate (s) with the formula


def solution(p: int, k: int, m: int):
    # First verify case x == 1
    x = 1
    if verify_condition(x, p, k, m):
        return x

    # In case x == 1 is not the solution then:
    s = calculate_s(p, k, m)
    x = 2 * s

    # Verify is this x is a solution
    if verify_condition(x, p, k, m):
        return x
    # If neither x is a solution return default value of (x = 2)
    return 2


if __name__ == "__main__":
    t = int(input())

    while t:
        input_variables = input()
        input_array = [int(num) for num in input_variables.split(" ")]
        p = input_array[0]
        k = input_array[1]
        m = input_array[2]

        print(solution(p, k, m))

        t -= 1
