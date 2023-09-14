#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#


# @lc code=start
from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        digits = list(range(1, n + 1))
        while digits:
            m = factorial(len(digits) - 1)
            idx = k / m
            if idx == int(idx):
                idx -= 1
            idx = int(idx)
            digit = digits[idx]
            ans += str(digit)
            digits.remove(digit)
            k -= idx * m

        return ans


# @lc code=end
