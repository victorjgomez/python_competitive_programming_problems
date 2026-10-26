from typing import List


class Solution:
    def remove_zeros(self, nums1: List[int]):
        new_num1 = []
        for x in nums1:
            if x != 0:
                new_num1.append(x)

        return new_num1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = self.remove_zeros(nums1)
        nums1 = nums1 + nums2
        nums1.sort()

