# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=featured-list&envId=top-interview-questions

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = {x for x in nums}
        nums = [x for x in nums]
        nums.sort()
        return len(nums)


if __name__ == "__main__":
    solution = Solution()

    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))