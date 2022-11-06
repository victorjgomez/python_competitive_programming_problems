# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(num: int) -> int:
    pick = 1702766719

    if num > pick:
        return -1
    elif num < pick:
        return 1

    return 0


class Solution:
    def binarySearch(self, arr, l, r):
        # Check base case
        if r >= l:
            mid = l + (r - l) // 2

            # If element is present at the middle itself
            guess_result = guess(mid)

            if guess_result == 0:
                return mid

            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif guess_result == -1:
                return self.binarySearch(arr, l, mid - 1)

            # Else the element can only be present
            # in right subarray
            else:
                return self.binarySearch(arr, mid + 1, r)

        else:
            # Element is not present in the array
            return -1

    def guessNumber(self, n: int) -> int:
        arr = [num for num in range(1, n + 1)]
        return self.binarySearch(arr, 1, n)


if __name__ == "__main__":
    solution = Solution()
    print(solution.guessNumber(2126753390))
