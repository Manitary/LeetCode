#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#


# @lc code=start


from functools import cache


@cache
def num(c: str) -> int:
    return ord(c) - ord("A")


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        charset = [0] * 26
        most_common = 0
        for right, c in enumerate(s):
            charset[num(c)] += 1
            most_common = max(most_common, charset[num(c)])
            if right - left + 1 - most_common > k:
                charset[num(s[left])] -= 1
                left += 1

        return len(s) - left


# @lc code=end
