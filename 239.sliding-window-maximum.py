#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#


# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq: deque[int] = deque()
        left = 0
        ans: list[int] = []
        for right, n in enumerate(nums):
            if right >= k:
                left += 1
            while dq and dq[0] < left:
                dq.popleft()
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(right)
            if right < k - 1:
                continue
            ans.append(nums[dq[0]])

        return ans


# @lc code=end
