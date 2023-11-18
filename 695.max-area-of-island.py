#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        land = {
            (r, c)
            for r, row in enumerate(grid)
            for c, elt in enumerate(row)
            if elt == 1
        }
        ans = 0

        def get_island_size(r: int, c: int) -> int:
            size = 1
            land.discard((r, c))
            for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (x, y) in land:
                    size += get_island_size(x, y)

            return size

        while land:
            ans = max(ans, get_island_size(*land.pop()))

        return ans


# @lc code=end
