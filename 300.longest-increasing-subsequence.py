#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        longest: dict[int, int] = {}
        for i, n in enumerate(reversed(nums), 1):
            longest[i] = 1 + max(
                (longest[j] for j in range(1, i) if nums[-j] > n), default=0
            )
        return max(longest.values())


# @lc code=end
