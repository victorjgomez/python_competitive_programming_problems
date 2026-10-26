#
"""
case #6
1000000000 1000000000 1000000000 1000000000
999999999  1000000001 1000000000 1000000000
999999999  1000000000 1000000001 1000000000
999999999  1000000000 1000000000 1000000001

caso #7

forma #1
1 7 3 9 2
1 6 4 8 3
1 5 5 7 4
1 4 6 6 5
1 4 5 6 7

forma #2
1 7 3 9 2
1 3 7 9 2
1 3 7 

"""

from typing import List


def verify_increasing(array_hi: List[int]):
    for i in range(len(array_hi) - 1):
        if array_hi[i] >= array_hi[i + 1]:
            return False
    return True


def shifting_stacks(array_hi: List[int]):
    for i in range(len(array_hi) - 1):
        if array_hi[i] >= array_hi[i + 1] and array_hi[i] != 0:
            array_hi[i] -= 1
            array_hi[i + 1] += 1


if __name__ == "__main__":
    t = int(input())

    while t:
        n = int(input())
        string_hi = input()
        array_hi = [int(h) for h in string_hi.split()]

        if verify_increasing(array_hi):
            print("YES")
            t -= 1
            continue

        shifting_stacks(array_hi)

        if verify_increasing(array_hi):
            print("YES")
        else:
            print("NO")

        t -= 1
