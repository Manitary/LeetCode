#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#


# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        bounds: dict[str, list[int]] = {}
        for i, c in enumerate(s):
            if c not in bounds:
                bounds[c] = [i, i]
            else:
                bounds[c][1] = i
        intervals = sorted(bounds.values())
        res: list[int] = []
        interval = intervals[0]
        j = 1
        while j < len(intervals):
            if interval[1] < intervals[j][0]:
                res.append(interval[1] - interval[0] + 1)
                interval = intervals[j]
            else:
                interval = [
                    min(interval[0], intervals[j][0]),
                    max(interval[1], intervals[j][1]),
                ]
            j += 1
        res.append(interval[1] - interval[0] + 1)

        return res


# @lc code=end
