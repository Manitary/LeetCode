#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#


# @lc code=start
from functools import cache


@cache
def num(c: str) -> int:
    return ord(c) - ord("a")


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        original = [0] * 26
        for c in s1:
            original[num(c)] += 1

        charset = [0] * 26
        right = l1 - 1
        for i, c in enumerate(s2):
            if i > right:
                break
            charset[num(c)] += 1

        while True:
            if charset == original:
                return True
            right += 1
            if right == l2:
                break
            charset[num(s2[right])] += 1
            charset[num(s2[right - l1])] -= 1

        return False


# @lc code=end
