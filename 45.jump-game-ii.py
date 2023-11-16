#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#


# @lc code=start
class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        goal = len(nums) - 1
        curr = (0, 0)
        steps = 0
        while True:
            steps += 1
            curr = (curr[1] + 1, max(i + nums[i] for i in range(curr[0], curr[1] + 1)))
            if curr[0] <= goal <= curr[1]:
                return steps


# @lc code=end
