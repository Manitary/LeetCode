#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[set[tuple[int, ...]]] = [set() for _ in range(target + 1)]
        res[0].add(())
        for i in range(1, target + 1):
            for c in candidates:
                if i - c < 0:
                    continue
                for elt in res[i - c]:
                    res[i].add(tuple(sorted(elt + (c,))))

        return [list(x) for x in res[-1]]


# @lc code=end
