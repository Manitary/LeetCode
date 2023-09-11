#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start

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


def product(*args: str) -> list[str]:
    result: list[str] = [""]
    for pool in args:
        result = [x + y for x in result for y in pool]
    return result


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        return product(*(LETTERS[d] for d in digits))


# @lc code=end
