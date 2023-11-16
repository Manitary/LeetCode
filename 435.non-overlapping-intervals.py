#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort()
        ans = 0
        i, j = 0, 1
        while j < len(intervals):
            if intervals[j][0] < intervals[i][1]:
                ans += 1
                if intervals[j][1] < intervals[i][1]:
                    i = j
            else:
                i = j
            j += 1

        return ans


# @lc code=end
