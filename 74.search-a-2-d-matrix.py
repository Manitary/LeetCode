#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top < bottom:
            middle = (top + bottom) // 2
            if matrix[middle][0] > target:
                bottom = middle - 1
            elif matrix[middle][-1] < target:
                top = middle + 1
            else:
                top = bottom = middle
        row = top
        left, right = 0, len(matrix[row]) - 1
        while left < right:
            middle = (left + right) // 2
            if matrix[row][middle] < target:
                left = middle + 1
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                left = right = middle

        if matrix[row][left] == target:
            return True

        return False


# @lc code=end
