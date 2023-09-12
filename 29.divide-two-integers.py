#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#


# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        sgn = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            d = divisor
            i = -1
            while dividend >= d:
                d <<= 1
                i += 1
            d >>= 1
            if i >= 0:
                ans += 1 << i
            dividend -= d
        if sgn:
            return min(ans, 2**31 - 1)
        return max(-ans, -(2**31))


# @lc code=end
