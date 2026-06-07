# https://leetcode.com/problems/majority-element/?envType=featured-list&envId=top-interview-questions
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> int:
        nums_set = {x for x in nums}

        if len(nums_set) == len(nums):
            return False
        return True
