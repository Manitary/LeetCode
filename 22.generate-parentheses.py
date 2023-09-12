#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = [(0, 0, "")]
        for _ in range(2 * n):
            new: list[tuple[int, int, str]] = []
            for p in ans:
                if p[0] < n:
                    new.append((p[0] + 1, p[1] + 1, p[2] + "("))
                if p[1] > 0:
                    new.append((p[0], p[1]-1, p[2]+")"))
            ans = new
        return [x[2] for x in ans]


# @lc code=end
