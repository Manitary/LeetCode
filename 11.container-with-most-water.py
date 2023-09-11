#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        best = 0
        while l < r:
            area = (r - l) * min(height[r], height[l])
            best = max(area, best)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return best


# @lc code=end
