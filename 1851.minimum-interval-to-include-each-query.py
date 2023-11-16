#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#


# @lc code=start
import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort(reverse=True)
        res: dict[int, int] = {}
        heap: list[tuple[int, int]] = []
        for q in sorted(set(queries)):
            while intervals and intervals[-1][0] <= q:
                interval = intervals.pop()
                heapq.heappush(heap, (interval[1] - interval[0] + 1, interval[1]))
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[q] = heap[0][0]
        return [res.get(q, -1) for q in queries]


# @lc code=end
