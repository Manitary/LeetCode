#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        min_cost_a, min_cost_b = 0, 0
        cost.append(0)
        for c in cost:
            min_cost_a, min_cost_b = min_cost_b, min(min_cost_a, min_cost_b) + c

        return min_cost_b


# @lc code=end
