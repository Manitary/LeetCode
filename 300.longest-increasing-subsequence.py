#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        def find(l: list[int], n: int) -> int:
            left, right = 0, len(l) - 1
            while left < right:
                middle = (left + right) // 2
                if l[middle] < n:
                    left = middle + 1
                else:
                    right = middle
            return left

        ans: list[int] = []
        for n in nums:
            if not ans or ans[-1] < n:
                ans.append(n)
            else:
                idx = find(ans, n)
                ans[idx] = n
        return len(ans)


# @lc code=end
