#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc code=start
from functools import cache


@cache
def num(c: str) -> int:
    x = ord(c) - ord("A")
    if x > 25:
        return x - 6
    return x


def is_contained(word: list[int], container: list[int]) -> bool:
    for n1, n2 in zip(word, container):
        if n1 > n2:
            return False
    return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        original = [0] * 52
        for c in t:
            original[num(c)] += 1
        left, right = 0, len(t) - 1
        best = len(s) + 1
        shortest = None
        charset = [0] * 52
        for i, c in enumerate(s):
            if i == len(t):
                break
            charset[num(c)] += 1
        while left <= right < len(s):
            if not is_contained(original, charset):
                right += 1
                if right < len(s):
                    charset[num(s[right])] += 1
                continue
            while is_contained(original, charset):
                new = right - left - 1
                if new < best:
                    best = new
                    shortest = (left, right)
                charset[num(s[left])] -= 1
                left += 1

        if not shortest:
            return ""

        return s[shortest[0] : shortest[1] + 1]


# @lc code=end
