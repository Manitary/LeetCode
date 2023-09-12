#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.ans: list[str] = []

    def recurse(self, to_open: int, to_close: int, curr: str) -> None:
        if not to_open and not to_close:
            self.ans.append(curr)
        if to_open > 0:
            self.recurse(to_open - 1, to_close + 1, curr + "(")
        if to_close > 0:
            self.recurse(to_open, to_close - 1, curr + ")")

    def generateParenthesis(self, n: int) -> list[str]:
        self.recurse(n, 0, "")
        return self.ans


# @lc code=end
