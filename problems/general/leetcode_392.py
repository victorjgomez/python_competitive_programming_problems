class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        n = len(s)
        m = len(t)

        while i < n and j < m:
            c_s = s[i]
            c_t = t[j]

            if c_s == c_t:
                i = i + 1
                j = j + 1
            else:
                j = j + 1

        if i == n:
            return True

        return False


if __name__ == '__main__':
    solution = Solution()

    print(solution.isSubsequence(s = "abc", t = "ahbgdc"))
    #print(solution.isSubsequence(s = "axc", t = "ahbgdc"))