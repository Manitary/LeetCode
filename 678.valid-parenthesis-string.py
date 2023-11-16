#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#


# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left, max_left = 0, 0
        for c in s:
            if c == "(":
                min_left, max_left = min_left + 1, max_left + 1
            elif c == ")":
                min_left, max_left = max(min_left - 1, 0), max_left - 1
            else:
                min_left, max_left = max(min_left - 1, 0), max_left + 1
            if max_left < 0:
                return False
        return min_left == 0


# @lc code=end
