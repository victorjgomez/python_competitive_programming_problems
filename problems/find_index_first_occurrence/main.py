# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=featured-list&envId=top-interview-questions

class Solution(object):

    def solution(self, haystack, needle):
        if len(needle) == 0:
            return True
        elif haystack[0] == needle[0]:
            return self.solution(haystack[1:], needle[1:])
        else:
            return False

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        else:
            for i in range(len(haystack) + 1 - len(needle)):
                if self.solution(haystack[i:], needle):
                    return i
            return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr("a", "a"))

