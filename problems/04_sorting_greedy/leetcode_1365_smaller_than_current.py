"""
1365. How Many Numbers Are Smaller Than the Current Number

https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
from typing import List


class Solution:

    def find_smaller_count_by_current(self, sort_nums: List[int],
                                      cur_ind: int, nums_len: int) -> int:
        # Verify than there are not repetitions on current
        while cur_ind < nums_len - 1 and sort_nums[cur_ind] == sort_nums[
            cur_ind + 1]:
            # Update current index
            cur_ind = cur_ind + 1

        return nums_len - (cur_ind + 1)

    def reorder_results(self, nums: List[int], sort_nums: List[int],
                        results: List[int]):
        reorder_results = []

        for num in nums:
            # Retorne the index of num in sort_nums
            index = sort_nums.index(num)
            reorder_results.append(results[index])

        return reorder_results

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Sort numbers
        sort_nums = nums.copy()
        sort_nums.sort(reverse=True)
        nums_len = len(nums)

        results = [self.find_smaller_count_by_current(sort_nums, cur_ind,
                                                      nums_len)
                   for cur_ind in range(nums_len)]

        return self.reorder_results(nums, sort_nums, results)


if __name__ == "__main__":
    solution = Solution()

    print(solution.smallerNumbersThanCurrent([7,7,7,7]))
