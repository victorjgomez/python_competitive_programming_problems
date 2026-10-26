class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1

        while (i >= 0):
            if nums[i] == 0:
                self.move_to_end(nums, i)

            i = i - 1

        print(nums)

    def move_to_end(self, nums, index):
        """
        Moves the element at the specified index to the end of the list.

        :param nums: List of elements
        :param index: Index of the element to move
        :return: Modified list with the element moved to the end
        """
        if 0 <= index < len(nums):
            element = nums.pop(index)  # Remove the element at the given index
            nums.append(element)  # Add it to the end of the list
        return nums


if __name__ == '__main__':
    sol = Solution()
    sol.moveZeroes([0, 1, 0, 3, 12])
    sol.moveZeroes([0])
