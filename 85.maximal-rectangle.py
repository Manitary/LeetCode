#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#


# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        best = 0
        n_col = len(matrix[0])
        heights = [0] * (n_col + 1)
        # add an extra fixed 0 at the end for a static reference point
        for row in matrix:
            for c, x in enumerate(row):
                heights[c] = (heights[c] + 1) if x == "1" else 0
                # max height if the cell is taken, looking upwards
            height_stack = [-1]
            for i in range(n_col + 1):
                while heights[i] < heights[height_stack[-1]]:
                    # a bump in height denote we passed a (local) maximum rectangle
                    # the extra 0 at the end of heights guarantees we check the tail
                    h = heights[height_stack.pop()]
                    w = i - height_stack[-1] - 1
                    best = max(best, h * w)
                height_stack.append(i)

        return best


# @lc code=end
