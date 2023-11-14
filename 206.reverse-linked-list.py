#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# from typing import Optional, Self


# class ListNode:
#     def __init__(self, val: int = 0, next: Optional[Self] = None) -> None:
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        stack: list[ListNode] = []
        while head:
            stack.append(head)
            head = head.next

        dummy_head = ListNode()
        curr = dummy_head
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None

        return dummy_head.next


# @lc code=end
