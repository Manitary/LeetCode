#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        stack = [-1]
        best = 0
        for i, curr in enumerate(heights):
            while curr < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                best = max(best, h * w)
            stack.append(i)
        return best


# @lc code=end
