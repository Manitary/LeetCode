#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        new = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
        if not -(2**31) <= new <= 2**31 - 1:
            return 0
        return new


# @lc code=end
