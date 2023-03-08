from typing import List, Dict
# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        # Top-down approach
        def go(array_cost: List[int], i: int) -> int:
            if i < 0:
                return 0
            elif i in memo:
                return memo[i]
            else:
                step1 = self.get_cost_from_array_cost(
                                    array_cost, i - 1) + go(array_cost, i - 1)
                step2 = self.get_cost_from_array_cost(
                                    array_cost, i - 2) + go(array_cost, i - 2)
                memo[i] = min(step1, step2)
                return memo[i]

        # Botton-up approach
        # def go(array_cost: List[int], n: int, i: int = -1,
        #        my_cost: int = 0) -> int:
        #     if i > n:
        #         return my_cost
        #     elif (i, my_cost) in memo:
        #         return memo[(i, my_cost)]
        #     else:
        #         step1 = go(array_cost, n, i + 1,
        #                         my_cost + self.get_cost_from_array_cost(
        #                             array_cost, n, i + 1))
        #         step2 = go(array_cost, n, i + 2,
        #                         my_cost + self.get_cost_from_array_cost(
        #                             array_cost, n, i + 2))
        #         memo[(i, my_cost)] = min(step1, step2)
        #         return memo[(i, my_cost)]

        cost.append(0)
        return go(cost, len(cost))

    def get_cost_from_array_cost(self, array_cost: List[int], i: int):
        if i < len(array_cost):
            return array_cost[i]
        else:
            return 0




if __name__  == "__main__":
    solution = Solution()

    print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))