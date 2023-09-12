#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# from typing import Self
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val: int = 0, next: Self | None = None) -> None:
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # lists = list(filter(None, lists))
        if not lists:
            return
        h: list[int] = []
        for head in lists:
            while head:
                heapq.heappush(h, head.val)
                head = head.next
        ans = ListNode()
        curr = ans
        while h:
            curr.next = ListNode(heapq.heappop(h))
            curr = curr.next
        return ans.next


# @lc code=end
