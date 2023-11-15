#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#


# @lc code=start
import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        times = [-x for x in Counter(tasks).values()]
        queue: list[list[int]] = []
        heapq.heapify(times)
        ans = 0
        while times or queue:
            if times:
                item = heapq.heappop(times) + 1
                if item:
                    queue.append([item, ans + n])
            while queue and queue[0][1] == ans:
                heapq.heappush(times, queue.pop(0)[0])
            ans += 1
        return ans


# @lc code=end
