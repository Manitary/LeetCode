#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        if m > n:
            return 0
        prev = [1] + ([0] * m)
        for i in range(1, n + 1):
            curr = [1] + ([0] * m)
            for j in range(1, m + 1):
                curr[j] = prev[j] + (prev[j - 1] if s[i - 1] == t[j - 1] else 0)
            prev = curr
        return prev[-1]


# @lc code=end
