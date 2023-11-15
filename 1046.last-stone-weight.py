#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#


# @lc code=start
import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, a - b)
        if stones:
            return -stones[0]
        return 0


# @lc code=end
