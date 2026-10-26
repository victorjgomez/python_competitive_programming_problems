# https://leetcode.com/problems/sorting-the-sentence/
from typing import List


def get_last_digit(word: str) -> int:
    n = len(word) - 1
    return int(word[n])


class Solution:

    def clear_s_split(self, s_split: List[int]):
        return [word[:len(word) - 1] for word in s_split]

    def sortSentence(self, s: str) -> str:
        s_split = s.split(" ")
        s_split.sort(key=get_last_digit)
        s_split_clear = self.clear_s_split(s_split)

        return ' '.join(s_split_clear)


if __name__ == "__main__":
    solution = Solution()

    s = "Myself2 Me1 I4 and3"
    print(solution.sortSentence(s))
