#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while nums[left] > nums[right]:
            middle = (left + right) // 2
            if nums[middle] >= nums[left]:
                left = middle + 1
            elif nums[middle] < nums[right]:
                right = middle
        return nums[left]


# @lc code=end
