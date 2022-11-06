# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        return self.solution(students, sandwiches, deque())

    def solution(self, students: deque, sandwiches: deque,
                 unable_students: deque) -> int:
        len_students = len(students)

        while len(students) > 0:
            if (students[0] == sandwiches[0] and
                    students[0] in [0, 1]):
                students.popleft()
                sandwiches.popleft()
            else:
                unable_students.append(students.popleft())
        if len_students == len(unable_students):
            return len_students
        return self.solution(unable_students, sandwiches, deque())


if __name__ == "__main__":
    solution = Solution()
    # print(solution.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
    print(solution.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
