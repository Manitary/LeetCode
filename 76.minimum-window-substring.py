#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc code=start
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        conditions = Counter(t)
        num_conditions = len(conditions)
        num_satisfied = 0
        satisfied = {x: False for x in conditions}

        left = 0
        best = len(s) + 1
        shortest = None
        charset = {x: 0 for x in conditions}

        for right, c in enumerate(s):
            if c not in charset:
                continue
            charset[c] += 1
            if not satisfied[c]:
                satisfied[c] = charset[c] == conditions[c]
                if satisfied[c]:
                    num_satisfied += 1
            while num_satisfied == num_conditions:
                curr = right - left + 1
                if curr < best:
                    best = curr
                    shortest = (left, right)
                left_char = s[left]
                left += 1
                if left_char not in charset:
                    continue
                charset[left_char] -= 1
                if satisfied[left_char]:
                    satisfied[left_char] = charset[left_char] >= conditions[left_char]
                    if not satisfied[left_char]:
                        num_satisfied -= 1

        if not shortest:
            return ""

        return s[shortest[0] : shortest[1] + 1]


# @lc code=end
