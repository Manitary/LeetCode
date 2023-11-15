#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#


# @lc code=start
import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        while min_k < max_k:
            k = (min_k + max_k) // 2
            t = sum(math.ceil(p / k) for p in piles)
            if t > h:
                min_k = k + 1
            else:
                max_k = k

        return min_k


# @lc code=end
