#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        land = {
            (r, c)
            for r, row in enumerate(grid)
            for c, elt in enumerate(row)
            if elt == "1"
        }

        def get_island(r: int, c: int) -> None:
            for x, y in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if (x, y) in land:
                    land.remove((x, y))
                    get_island(x, y)

        n_islands = 0
        while land:
            get_island(*land.pop())
            n_islands += 1

        return n_islands


# @lc code=end
