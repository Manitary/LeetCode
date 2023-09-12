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


def get_val(node: ListNode | None) -> float:
    if not node:
        return float("inf")
    return node.val


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return
        dummy_head = ListNode()
        curr = dummy_head
        while any(lists):
            values = tuple(map(get_val, lists))
            idx = values.index(min(values))
            curr.next = lists[idx]
            lists[idx] = lists[idx].next
            curr = curr.next
            lists = list(filter(None, lists))
        return dummy_head.next


# @lc code=end
