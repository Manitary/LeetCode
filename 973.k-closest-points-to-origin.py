#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#


# @lc code=start
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pts = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
        heapq.heapify(pts)
        return [heapq.heappop(pts)[1] for _ in range(k)]


# @lc code=end
