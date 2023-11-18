#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        best_a, best_b = 0, 0
        for m in nums:
            best_a, best_b = max(best_a, best_b), best_a + m

        return max(best_a, best_b)


# @lc code=end
