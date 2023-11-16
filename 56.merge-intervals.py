#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#


# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > ans[-1][1]:
                ans.append(interval)
                continue
            ans[-1] = [min(ans[-1][0], interval[0]), max(ans[-1][1], interval[1])]

        return ans


# @lc code=end
