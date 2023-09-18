#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#


# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: list[list[float]]) -> float:
        max_r = len(dungeon)
        max_c = len(dungeon[0])
        for row in dungeon:
            row.append(float("inf"))
        dungeon[-1][-1] = 1
        dungeon.append([float("inf")] * (max_c + 1))
        dungeon[-1][-2] = 1
        for r in range(max_r - 1, -1, -1):
            for c in range(max_c - 1, -1, -1):
                dungeon[r][c] = max(
                    1, -dungeon[r][c] + min(dungeon[r + 1][c], dungeon[r][c + 1])
                )
        return dungeon[0][0]


# @lc code=end
