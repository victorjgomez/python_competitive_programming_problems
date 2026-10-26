# https://leetcode.com/problems/maximum-69-number/
from typing import List


class Solution:
    def get_change_digit_number(self, list_d: List[int], i: int) -> int:
        if list_d[i] == 6:
            list_d[i] = 9
        elif list_d[i] == 9:
            list_d[i] = 6
        list_d_str = [str(d) for d in list_d]

        return int("".join(list_d_str))

    def maximum69Number (self, num: int) -> int:
        list_d = [int(d) for d in str(num)]
        n = len(list_d)
        all_options = [self.get_change_digit_number(list_d.copy(), i) for i in range(n)]
        all_options.append(num)

        return max(all_options)

if __name__ == "__main__":
    solution = Solution()

    print(solution.maximum69Number(9999))
