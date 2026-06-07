"""
2160. Minimum Sum of Four Digit Number After Splitting Digits

https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
"""
from typing import List


class Solution:
    def split_num_to_digit(self, num: int) -> List[int]:
        list_digit = []

        for x in range(len(str(num))):
            # Remove last digit from num
            num_remove_last = int(num / 10)
            # Add zero as the new last digit
            num_zero_last = num_remove_last * 10
            # Add last digit to the list
            list_digit.append(num - num_zero_last)

            # Update num value
            num = num_remove_last

        return list_digit

    def minimumSum(self, num: int) -> int:
        list_digit = self.split_num_to_digit(num)
        list_digit.sort()

        return list_digit[0] * 10 + list_digit[3] + list_digit[1] * 10 + \
               list_digit[2]


if __name__ == "__main__":
    solution = Solution()

    print(solution.minimumSum(4009))
