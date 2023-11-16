#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[0]
        curr = 0
        for n in nums:
            curr = max(curr, 0)
            curr += n
            best = max(best, curr)

        return best


# @lc code=end
