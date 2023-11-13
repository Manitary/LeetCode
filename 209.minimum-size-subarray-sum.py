#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        best = float("inf")
        left, right = 0, 0
        tot = 0
        while right < len(nums):
            tot += nums[right]
            while left <= right and tot >= target:
                best = min(best, right - left + 1)
                tot -= nums[left]
                left += 1

            right += 1
        if best == float("inf"):
            return 0
        return best


# @lc code=end
