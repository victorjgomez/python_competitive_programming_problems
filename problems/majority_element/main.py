# https://leetcode.com/problems/majority-element/?envType=featured-list&envId=top-interview-questions
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count: Counter = Counter(nums)
        appearances: int = int(len(nums) / 2)
        nums_set = {x for x in nums}

        for x in nums_set:
            if count[x] > appearances:
                return x
        return -1
