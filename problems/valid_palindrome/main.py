# https://leetcode.com/problems/valid-palindrome/?envType=featured-list&envId=top-interview-questions
import re


class Solution:
    # def solution(self, s1, s2):
    #     if len(s1) == 0 and len(s2) == 0:
    #         return True
    #     elif s1[0] != s2[0]:
    #         return False
    #     else:
    #         return self.solution(s1[1:], s2[1:])

    def solution(self, s_list, i, j):
        if j < 0:
            return True
        elif s_list[i] != s_list[j]:
            return False
        else:
            return self.solution(s_list, i+1, j-1)

    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s)
        s = s.lower()
        s = s.replace("_", "")
        l_s = [x for x in s]
        return self.solution(l_s, 0, len(l_s)-1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("ab_a"))
