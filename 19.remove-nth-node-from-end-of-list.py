#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# from typing import Self


# class ListNode:
#     def __init__(self, val: int = 0, next: Self | None = None) -> None:
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode | None:
        dummy_head = ListNode(next=head)
        to_remove_prev, curr = dummy_head, head
        for _ in range(n):
            curr = curr.next

        while curr:
            to_remove_prev, curr = to_remove_prev.next, curr.next

        to_remove_prev.next = to_remove_prev.next.next

        return dummy_head.next


# @lc code=end
