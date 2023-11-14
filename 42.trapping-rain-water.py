#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        max_left = height[left]
        max_right = height[right]
        while left < right:
            if max_left <= max_right:
                left += 1
                q = min(max_left, max_right) - height[left]
                max_left = max(max_left, height[left])
            else:
                right -= 1
                q = min(max_left, max_right) - height[right]
                max_right = max(max_right, height[right])
            if q > 0:
                ans += q

        return ans


# @lc code=end
