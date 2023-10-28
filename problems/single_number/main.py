# https://leetcode.com/problems/single-number/?envType=featured-list&envId=top-interview-questions
from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count: Counter = Counter(nums)

        for x in nums:
            if count[x] == 1:
                return x
        return -1
