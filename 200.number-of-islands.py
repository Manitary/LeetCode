#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start


from typing import Iterator


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        visited: set[tuple[int, int]] = set()

        def ngbh(r: int, c: int) -> Iterator[tuple[int, int]]:
            for a, b in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if (a, b) not in visited and 0 <= a < n_rows and 0 <= b < n_cols:
                    yield a, b

        def get_island(r: int, c: int) -> None:
            visited.add((r, c))
            if grid[r][c] == "0":
                return
            for x, y in ngbh(r, c):
                get_island(x, y)

        n_islands = 0
        for i, row in enumerate(grid):
            for j, elt in enumerate(row):
                if elt == "0" or (i, j) in visited:
                    continue
                get_island(i, j)
                n_islands += 1

        return n_islands


# @lc code=end
