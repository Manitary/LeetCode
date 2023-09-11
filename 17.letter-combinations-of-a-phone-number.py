#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
import itertools

LETTERS = {
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "0": " ",
}


def list_to_str(l: tuple[str]) -> str:
    return "".join(l)


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        return list(map(list_to_str, itertools.product(*(LETTERS[d] for d in digits))))


# @lc code=end
