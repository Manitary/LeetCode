#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
import re


class Solution:
    pattern = re.compile(r"[+-]?(?:\d+|\d+\.(?:\d+)?|\.\d+)(?:[eE][+-]?\d+)?")

    def isNumber(self, s: str) -> bool:
        return bool(self.pattern.fullmatch(s))


# @lc code=end
