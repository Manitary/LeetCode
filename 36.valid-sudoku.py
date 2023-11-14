#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start

from itertools import product
from typing import Iterable


def box(i: int) -> set[tuple[int, int]]:
    i -= 1
    r, c = divmod(i, 3)
    return set(product(range(3 * r, 3 * (r + 1)), range(3 * c, 3 * (c + 1))))


def has_duplicate(l: Iterable[str]) -> bool:
    visited: set[str] = set()
    for x in l:
        if x == ".":
            continue
        if x in visited:
            return True
        visited.add(x)
    return False


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if has_duplicate(row):
                return False

        for col in zip(*board):
            if has_duplicate(col):
                return False

        for i in range(9):
            if has_duplicate(board[r][c] for r, c in box(i)):
                return False

        return True


# @lc code=end
