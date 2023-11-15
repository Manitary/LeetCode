#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h: list[int] = []
        for n in nums[: k]:
            heapq.heappush(h, n)
        for n in nums[k :]:
            heapq.heappushpop(h, n)
        return h[0]


# @lc code=end
