# https://codeforces.com/problemset/problem/266/B
from typing import List


class Solution:

    def swap(self, s_list: List[str], ind: int):
        temp = s_list[ind]
        s_list[ind] = s_list[ind+1]
        s_list[ind + 1] = temp


    def solution(self, s_list: List[str], n: int,  t: int):

        while t != 0:
            ind = 0
            while ind < n:
                try:
                    if s_list[ind] == 'B' and s_list[ind + 1] == 'G':
                        self.swap(s_list, ind)
                        ind = ind + 2
                    else:
                        ind = ind + 1
                except IndexError:
                    ind = ind + 1
                    continue
            t = t - 1

        return s_list


if __name__ == '__main__':
    input_n_t = input()
    input_n_t_split = input_n_t.split()
    n = int(input_n_t_split[0])
    t = int(input_n_t_split[1])
    s = str(input())
    s_list = [c for c in s]

    solution = Solution()

    print(''.join(solution.solution(s_list, n, t)))
