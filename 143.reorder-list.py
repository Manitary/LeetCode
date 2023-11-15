#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# from typing import Optional, Self


# class ListNode:
#     def __init__(self, val: int = 0, next: Optional[Self] = None) -> None:
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        stack: list[ListNode] = []
        while head:
            stack.append(head)
            head = head.next
        left, right = 0, len(stack) - 1
        while True:
            if left < right:
                stack[left].next = stack[right]
                left += 1
            else:
                stack[left].next = None
                return
            if left < right:
                stack[right].next = stack[left]
                right -= 1
            else:
                stack[right].next = None
                return


# @lc code=end
