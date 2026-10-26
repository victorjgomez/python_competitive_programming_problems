from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str: str = ""

        for d in digits:
            num_str = num_str + str(d)

        num_int: int = int(num_str)
        num_int = num_int + 1

        return [int(x) for x in str(num_int)]
