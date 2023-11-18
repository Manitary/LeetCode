#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#


# @lc code=start
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh = {
            (r, c)
            for r, row in enumerate(grid)
            for c, elt in enumerate(row)
            if elt == 1
        }
        if not fresh:
            return 0

        rotten = {
            (r, c)
            for r, row in enumerate(grid)
            for c, elt in enumerate(row)
            if elt == 2
        }

        t = 0
        while rotten:
            t += 1
            new_rotten: set[tuple[int, int]] = set()
            while rotten:
                r, c = rotten.pop()
                for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (x, y) in fresh:
                        new_rotten.add((x, y))
                        fresh.remove((x, y))
            rotten = new_rotten

        if fresh:
            return -1

        return t - 1


# @lc code=end
