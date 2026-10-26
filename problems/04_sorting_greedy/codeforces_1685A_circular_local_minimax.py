# https://codeforces.com/problemset/problem/1685/A
from typing import List


class Solution:
    def verify_condition_len_inpair(self, nums: List[int], n: int):
        if n % 2 != 0:
            return True
        return False

    def verify_bi(self, join_arr: List[int], ind: int, n: int):
        if ind == 0:
            if join_arr[n] > join_arr[ind] < join_arr[ind + 1] or \
                    join_arr[n] < join_arr[ind] > join_arr[ind + 1]:
                return True
        elif ind == n:
            if join_arr[ind - 1] > join_arr[ind] < join_arr[0] or \
                    join_arr[ind - 1] < join_arr[ind] > join_arr[0]:
                return True
        else:
            if join_arr[ind - 1] > join_arr[ind] < join_arr[ind + 1] or \
                    join_arr[ind - 1] < join_arr[ind] > join_arr[ind + 1]:
                return True
        return False

    def verify_join_array(self, join_arr: List[int]):
        len_join_arr = len(join_arr)

        for ind in range(len_join_arr):
            if not self.verify_bi(join_arr, ind, len_join_arr - 1):
                return False

        return True

    def get_divide_arrays(self, nums: List[int], n: int) -> {str: List[int]}:
        middle = int(n / 2)
        return {'array1': nums[:middle], 'array2': nums[middle:]}

    def get_join_arrays(self, nums: List[int], n: int) -> List[int]:

        dict_div = self.get_divide_arrays(nums, n)
        arr1 = dict_div['array1']
        arr2 = dict_div['array2']

        join_arr = []
        for ind in range(len(arr1)):
            join_arr.append(arr1[ind])
            join_arr.append(arr2[ind])

        return join_arr

    def circular_local_minimax(self, nums: List[int]) -> {str: str,
                                                          str: List[int]}:
        n = len(nums)

        if self.verify_condition_len_inpair(nums, n):
            return {'answer': 'NO', 'result': None}

        # Sort array
        nums.sort()

        join_arr = self.get_join_arrays(nums, n)

        if self.verify_join_array(join_arr):
            return {'answer': 'YES', 'result': join_arr}
        else:
            return {'answer': 'NO', 'result': None}


if __name__ == "__main__":
    solution = Solution()

    t = int(input())

    while t > 0:
        n = input()
        nums_input = input()
        nums = nums_input.split()

        dict_solution = solution.circular_local_minimax(nums)

        if dict_solution['answer'] == 'NO':
            print(dict_solution['answer'])
        else:
            print(dict_solution['answer'])
            result = [str(num) for num in dict_solution['result']]
            print(" ".join(result))

        t = t - 1
