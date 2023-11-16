#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lc code=start
class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        ans: list[list[int]] = []
        for i, old_interval in enumerate(intervals):
            if newInterval[1] < old_interval[0]:
                ans.append(newInterval)
                ans.extend(intervals[i:])
                return ans
            if old_interval[1] < newInterval[0]:
                ans.append(old_interval)
                continue
            newInterval = [
                min(newInterval[0], old_interval[0]),
                max(newInterval[1], old_interval[1]),
            ]
        ans.append(newInterval)

        return ans


# @lc code=end
