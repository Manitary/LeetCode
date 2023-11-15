#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#


# @lc code=start
import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        self.size = k
        heapq.heapify(nums)
        self.heap = nums
        while len(self.heap) > self.size:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
