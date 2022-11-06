# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        # stack = deque()
        max_depth = 0
        depth = 0

        for c in s:
            if c == "(":
                depth += 1
                # stack.append(c)
            elif c == ")":
                depth -= 1
                # stack.append(c)

            if depth > max_depth:
                max_depth = depth

        return max_depth


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDepth("a"))
