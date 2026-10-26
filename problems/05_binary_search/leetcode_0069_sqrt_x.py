# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def binary_search(self, low, high, x):

        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if mid * mid == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif mid * mid > x:
                return self.binary_search(low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return self.binary_search(mid + 1, high, x)

        else:
            # Element is not present in the array
            return high

    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        return int(self.binary_search(1, x/2, x))


if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(8))
