#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            n = numbers[left] + numbers[right]
            if n > target:
                right -= 1
                continue
            if n < target:
                left += 1
                continue
            return [left + 1, right + 1]
        raise ValueError("Invalid input")


# @lc code=end
