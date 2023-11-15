#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow_1 = 0
        fast = 0
        while slow_1 != fast or not fast:
            slow_1 = nums[slow_1]
            fast = nums[nums[fast]]
        slow_2 = 0
        while slow_2 != slow_1:
            slow_1 = nums[slow_1]
            slow_2 = nums[slow_2]

        return slow_1


# @lc code=end
