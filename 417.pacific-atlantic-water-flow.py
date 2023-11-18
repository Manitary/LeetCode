#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#


# @lc code=start
def make_sea(heights: list[list[int]], sea: set[tuple[int, int]]) -> None:
    new = set(sea)
    visited: set[tuple[int, int]] = set()
    while new:
        r, c = new.pop()
        visited.add((r, c))
        for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if (
                (x, y) not in visited
                and 0 <= x < len(heights)
                and 0 <= y < len(heights[0])
            ):
                if heights[r][c] <= heights[x][y]:
                    new.add((x, y))
                    sea.add((x, y))


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pacific = {(0, c) for c in range(len(heights[0]))} | {
            (r, 0) for r in range(len(heights))
        }
        atlantic = {(len(heights) - 1, c) for c in range(len(heights[0]))} | {
            (r, len(heights[0]) - 1) for r in range(len(heights))
        }
        make_sea(heights, pacific)
        make_sea(heights, atlantic)

        return [[r, c] for (r, c) in pacific.intersection(atlantic)]


# @lc code=end
