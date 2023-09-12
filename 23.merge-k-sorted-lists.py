#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# from typing import Self


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val: int = 0, next: Self | None = None) -> None:
#         self.val = val
#         self.next = next


def min_idx(lists: list[ListNode]) -> int:
    best = float("inf")
    ans = -1
    for i, node in enumerate(lists):
        if node.val < best:
            ans = i
            best = node.val
    return ans


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        lists = list(filter(None, lists))
        if not lists:
            return
        dummy_head = ListNode()
        curr = dummy_head
        while lists:
            idx = min_idx(lists)
            curr.next = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx] is None:
                del lists[idx]
            curr = curr.next
        return dummy_head.next


# @lc code=end
