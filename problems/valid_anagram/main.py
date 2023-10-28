# https://leetcode.com/problems/valid-anagram/?envType=featured-list&envId=top-interview-questions

class Solution:
    def compare(self, s_list, t_list):
        if len(s_list) == 0 and len(t_list) == 0:
            return True
        elif len(s_list) == 0 or len(t_list) == 0:
            return False
        elif s_list[0] != t_list[0]:
            return False
        else:
            return self.compare(s_list[1:], t_list[1:])

    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [x for x in s]
        t_list = [x for x in t]
        s_list.sort()
        t_list.sort()

        return self.compare(s_list, t_list)
