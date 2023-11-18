#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
from functools import cache


@cache
def climb(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb(n - 1) + climb(n - 2)


class Solution:
    def climbStairs(self, n: int) -> int:
        return climb(n)


# @lc code=end
