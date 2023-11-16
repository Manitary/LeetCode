#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def recurse(idx: int, curr: list[int], total: int) -> list[list[int]]:
            if total == target:
                return [curr]
            if idx >= len(candidates) or total > target:
                return []
            return recurse(
                idx, curr + [candidates[idx]], total + candidates[idx]
            ) + recurse(idx + 1, curr, total)

        return recurse(0, [], 0)


# @lc code=end
