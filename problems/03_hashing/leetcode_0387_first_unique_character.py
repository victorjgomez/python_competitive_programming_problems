# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter
from collections import deque


class Solution:
    def firstUniqChar(self, s: str) -> int:
        list_c = [c for c in s]
        counter_list_c = Counter(list_c)
        queue_list_c = deque(list_c)

        while len(queue_list_c) > 0:
            c = queue_list_c.popleft()
            if counter_list_c[c] == 1:
                return list_c.index(c)
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.firstUniqChar("aabb"))
