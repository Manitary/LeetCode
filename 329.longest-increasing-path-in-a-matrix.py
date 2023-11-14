#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#


# @lc code=start
import itertools
from typing import Iterator


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        best: list[list[int]] = [[1] * n_cols for _ in range(n_rows)]

        def ngbh(x: int, y: int) -> Iterator[tuple[int, int]]:
            for a, b in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)):
                if 0 <= a < n_cols and 0 <= b < n_rows:
                    yield (a, b)

        def find_path(x: int, y: int) -> None:
            if best[y][x] > 1:
                return
            for a, b in ngbh(x, y):
                if matrix[b][a] >= matrix[y][x]:
                    continue
                find_path(a, b)
                best[y][x] = max(best[y][x], best[b][a] + 1)

        for y, row in enumerate(matrix):
            for x, _ in enumerate(row):
                if best[y][x] > 1:
                    continue
                find_path(x, y)

        return max(itertools.chain(*best))


# @lc code=end
