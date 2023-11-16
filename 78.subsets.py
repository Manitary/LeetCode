#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def recurse(idx: int, subset: list[int]) -> list[list[int]]:
            if idx >= len(nums):
                return [subset]
            return recurse(idx + 1, subset + [nums[idx]]) + recurse(idx + 1, subset)

        return recurse(0, [])


# @lc code=end
