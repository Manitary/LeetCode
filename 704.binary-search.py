#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#


# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        idx = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return idx


# @lc code=end
