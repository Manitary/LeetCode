#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complements: dict[int, int] = {}
        for i, n in enumerate(nums):
            if n in complements:
                return [i, complements[n]]
            complements[target - n] = i
        raise ValueError("No solution found whereas one should exist.")


# @lc code=end
