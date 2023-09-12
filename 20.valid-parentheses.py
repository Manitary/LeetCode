#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
CLOSE = {")": "(", "]": "[", "}": "{"}


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        active: list[str] = []
        for c in s:
            if c not in CLOSE:
                active.append(c)
                continue
            if not active or active[-1] != CLOSE[c]:
                return False
            active.pop()
        return not active


# @lc code=end
