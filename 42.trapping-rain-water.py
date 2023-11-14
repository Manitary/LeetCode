#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        left = 0
        while left < len(height) - 1:
            while left < len(height) and height[left] == 0:
                left += 1
            if left >= len(height) - 1:
                break
            right = left + 1
            max_floor = height[right]
            while height[right] < height[left]:
                right += 1
                if right == len(height):
                    break
                if height[right] > max_floor:
                    ans += (min(height[right], height[left]) - max_floor) * (
                        right - left - 1
                    )
                    max_floor = height[right]
            left += 1

        return ans


# @lc code=end
