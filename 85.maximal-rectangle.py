#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#


# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        ans = 0
        n_col = len(matrix[0])
        for i in range(len(matrix)):
            rect: list[float] = [0] * n_col
            for row in matrix[i:]:
                for j, x in enumerate(row):
                    rect[j] += 1 if x == "1" else -float("inf")
                max_so_far = -float("inf")
                max_ending_here = 0
                for x in rect:
                    max_ending_here += x
                    max_so_far = max(max_so_far, max_ending_here)
                    max_ending_here = max(max_ending_here, 0)
                ans = max(ans, max_so_far)
        return ans


# @lc code=end
