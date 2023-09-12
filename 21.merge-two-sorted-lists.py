#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# from typing import Self


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val: int = 0, next: Self | None = None) -> None:
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        if not (list1 or list2):
            return
        if not list1:
            return list2
        if not list2:
            return list1
        dummy_head = ListNode()
        curr = dummy_head
        l1p = list1
        l2p = list2
        while l1p or l2p:
            if not l1p:
                curr.next = l2p
                break
            if not l2p:
                curr.next = l1p
                break
            if l1p.val <= l2p.val:
                curr.next = ListNode(l1p.val)
                l1p = l1p.next
            else:
                curr.next = ListNode(l2p.val)
                l2p = l2p.next
            curr = curr.next
        return dummy_head.next



# @lc code=end
