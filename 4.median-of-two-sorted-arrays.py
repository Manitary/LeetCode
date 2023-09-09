#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)
        l = len(nums)
        if l % 2:
            return nums[l // 2]
        return (nums[l // 2 - 1] + nums[l // 2]) / 2


# @lc code=end
