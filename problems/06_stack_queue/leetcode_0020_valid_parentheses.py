class Solution(object):

    def solution(self, list_c, left):
        if len(list_c) == 0 and len(left) == 0:
            return True
        if len(list_c) == 0 and len(left) != 0:
            return False
        elif list_c[0] in [")", "]", "}"] and len(left) == 0:
            return False
        elif list_c[0] in ["(", "[", "{"]:
            new_left = left
            new_left.append(list_c[0])
            return self.solution(list_c[1:], new_left)
        elif left[len(left)-1] == "(" and list_c[0] == ")":
            return self.solution(list_c[1:], left[:len(left)-1])
        elif left[len(left)-1] == "[" and list_c[0] == "]":
            return self.solution(list_c[1:], left[:len(left)-1])
        elif left[len(left)-1] == "{" and list_c[0] == "}":
            return self.solution(list_c[1:], left[:len(left)-1])
        else:
            return False


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.solution([x for x in s], [])
