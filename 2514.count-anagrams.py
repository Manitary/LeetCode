#
# @lc app=leetcode id=2514 lang=python3
#
# [2514] Count Anagrams
#

# @lc code=start
from collections import Counter
from math import factorial, prod


class Solution:
    m = 10**9 + 7

    def countAnagrams(self, s: str) -> int:
        ans = 1
        for w in s.split():
            f = (
                factorial(len(w)) // prod(map(factorial, Counter(w).values()))
            ) % self.m
            ans *= f
            ans %= self.m
        return ans


# @lc code=end
