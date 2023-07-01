# https://leetcode.com/problems/roman-to-integer/?envType=featured-list&envId=top-interview-questions


class Solution(object):
    roman_to_integer_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def solution(self, s_list, last_value=0, total_value=0):
        if len(s_list) == 0:
            return total_value
        elif Solution.roman_to_integer_dict[s_list[0]] < last_value:
            return self.solution(s_list[1:], Solution.roman_to_integer_dict[s_list[0]],
                                 total_value - Solution.roman_to_integer_dict[s_list[0]])
        else:
            return self.solution(s_list[1:], Solution.roman_to_integer_dict[s_list[0]],
                                 total_value + Solution.roman_to_integer_dict[s_list[0]])

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = [x for x in s]
        s_list.reverse()
        return self.solution(s_list)
