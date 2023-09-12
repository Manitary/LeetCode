#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s = set(nums)
        for i, x in enumerate(sorted(list(s))):
            nums[i] = x
        return len(s)


# @lc code=end
