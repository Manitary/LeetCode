#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1] * len(nums)

        prefix = 1
        for i, num in enumerate(nums):
            ans[i] = prefix
            prefix *= num

        suffix = 1
        for i, num in enumerate(nums[::-1], 1):
            ans[-i] *= suffix
            suffix *= num

        return ans


# @lc code=end
