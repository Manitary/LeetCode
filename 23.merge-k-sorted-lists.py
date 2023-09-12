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


def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy_head = ListNode()
    curr = dummy_head
    while list1 or list2:
        if not list1:
            curr.next = list2
            break
        if not list2:
            curr.next = list1
            break
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    return dummy_head.next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # lists = list(filter(None, lists))
        if not lists:
            return
        while len(lists) > 1:
            lists = tuple(
                mergeTwoLists(lists[i], lists[i + 1] if i + 1 < len(lists) else None)
                for i in range(0, len(lists), 2)
            )
        return lists[0]


# @lc code=end
