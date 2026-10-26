"""
Link: https://leetcode.com/problems/split-a-string-in-balanced-strings/submissions/

Case #1
RLRRLLRLRL - count = 0

RL0000RLRL - count = 1

0000000000 - count = 4

Case #2
RLLLLRRRLR - count = 0

RL000000LR - count = 1

0000000000 - count = 3


Case #3
LLLLRRRR - count = 0

00000000 - count = 1


Case #4

RLRRRLLRLL - count = 0

RLR0000RLL - count = 1

00R000000L - count = 3

Case #5

RLLLLRRRLR - count = 0

RL000000LR - count = 1

0000000000 - count = 3

Case #6

RLRRRLLRLL - count = 0

RLR0000RLL - count = 1

00R000000L - count = 3



Steps to perform the algorithm:

1 - Create a variable (n_match) with the len of the string, this is the first
 objective to match balanced string.
2 - Create a variable (list_character) with the string.
3 - Create a count variable (count == 0)

4 - Try to find match balanced string with current (n).
5 - If match replace all match character with '0'.
6 - Verify if all character on (list_character) are equal to '0'.
7 - If yes finish the program and return (count).
6 - If not repeat step 4 until the evaluation reached the end of (list_character).

7 - Reduce n_match by 2.
8 - Verify if n is equal to 0.
9 - If yes finish the program and return (count).
10 - If not go back to step 4.
"""
from typing import List


class Solution:
    n = 0
    n_match = 0
    list_c = []
    count = 0

    def verify_all_equal(self, sub_list_c: List[str], c: str):
        n = len(sub_list_c)
        if c == '0':
            return False
        if sub_list_c.count(c) == n:
            return True
        return False

    def verify_match_balanced(self, sub_list_c: List[str]):
        n = len(sub_list_c)
        half_n = int(n / 2)
        first_half_sub_list = sub_list_c[0:half_n]
        second_half_sub_list = sub_list_c[half_n:n]

        if self.verify_all_equal(first_half_sub_list,
                                 first_half_sub_list[0]) \
                and self.verify_all_equal(second_half_sub_list,
                                          second_half_sub_list[0]):
            Solution.count = Solution.count + 1
            return True
        return False

    def fill_with_zero(self, start: int, end: int):
        for i in range(start, end):
            Solution.list_c[i] = '0'

    def find_match_balanced(self):
        for i in range(0, Solution.n-Solution.n_match+1):
            if self.verify_match_balanced(Solution.list_c[i:i+Solution.n_match]):
                self.fill_with_zero(i, i+Solution.n_match)

    def balancedStringSplit(self, s: str) -> int:
        Solution.n = len(s)
        Solution.n_match = Solution.n
        Solution.list_c = [c for c in s]
        Solution.count = 0

        while Solution.n_match > 0:
            self.find_match_balanced()
            Solution.n_match = Solution.n_match - 2

        return Solution.count


if __name__ == '__main__':
    solution = Solution()
    print(solution.balancedStringSplit("RLRRRLLRLL"))
