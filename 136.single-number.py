#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
import functools
import operator


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return functools.reduce(operator.xor, nums)


# @lc code=end
