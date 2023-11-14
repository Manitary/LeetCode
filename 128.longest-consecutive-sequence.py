#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for n in nums_set:
            if n - 1 in nums_set:
                continue
            l = 1
            m = n
            while (m := m + 1) in nums_set:
                l += 1
            ans = max(ans, l)
        return ans


# @lc code=end
