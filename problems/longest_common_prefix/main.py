# https://leetcode.com/problems/longest-common-prefix/description/?envType=featured-list&envId=top-interview-questions

class Solution(object):
    def solution(self, strs, prefix=""):
        if 0 in [len(x) for x in strs]:
            return prefix
        else:
            c_prefix = strs[0][0]
            conditions = [c_prefix == x[0] for x in strs]

            if all(conditions):
                return self.solution([x[1:] for x in strs], prefix + c_prefix)
            else:
                return prefix

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return self.solution(strs)
