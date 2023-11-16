#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        diffs = tuple(g - c for g, c in zip(gas, cost))
        if sum(diffs) < 0:
            return -1

        i = 0
        while i < len(diffs):
            curr = 0
            for j, y in enumerate(diffs[i:], i):
                curr += y
                if curr < 0:
                    i = j
                    break
            else:
                return i
            i += 1

        raise ValueError("Invalid input")


# @lc code=end
