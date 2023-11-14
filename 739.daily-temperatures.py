#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc code=start
from collections import defaultdict


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        temps: dict[int, list[int]] = defaultdict(list)
        for i, t in enumerate(temperatures):
            temps[t].append(i)
            for x, idxs in temps.items():
                if x >= t:
                    continue
                for j in idxs:
                    ans[j] = i - j
                temps[x] = []

        return ans


# @lc code=end
