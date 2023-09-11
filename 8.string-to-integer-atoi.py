#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


# @lc code=start
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r" *([+-]?\d+).*", s)
        if not match:
            return 0
        n = int(match.group(1))
        if n < 0:
            return max(-(2**31), n)
        return min(n, 2**31 - 1)


# @lc code=end
