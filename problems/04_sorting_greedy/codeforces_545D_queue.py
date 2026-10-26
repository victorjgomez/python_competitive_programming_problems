from typing import List


def count_disappointed(array_t: List[int]):
    cont_undissapoint_people = 1
    len_array_t = len(array_t)
    wait_time = array_t[0]
    for i in range(1, len_array_t):
        if not (wait_time > (time_serve := array_t[i])):
            wait_time += time_serve
            cont_undissapoint_people += 1

    return cont_undissapoint_people


if __name__ == "__main__":
    n = int(input())
    string_t = input()
    array_t = [int(h) for h in string_t.split()]
    array_t.sort()

    print(count_disappointed(array_t))
