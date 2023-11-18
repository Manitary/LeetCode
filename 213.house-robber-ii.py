#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#


# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_line(nums[1:]), self.rob_line(nums[:-1]))

    def rob_line(self, nums: list[int]) -> int:
        best_a, best_b = 0, 0
        for m in nums:
            best_a, best_b = max(best_a, best_b), best_a + m

        return max(best_a, best_b)


# @lc code=end
