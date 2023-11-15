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

        # Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Break the list
        # If odd length, first half is longer
        second = slow.next
        prev = slow.next = None
        while second:
            second.next, prev, second = prev, second, second.next

        first, second = head, prev
        while second:
            first.next, second.next, first, second = (
                second,
                first.next,
                first.next,
                second.next,
            )


# @lc code=end
