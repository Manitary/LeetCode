#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# from typing import Self


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val: int = 0, next: Self | None = None) -> None:
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not (head and head.next):
            return head
        new_head = self.swapPairs(head.next.next)
        ans = head.next
        ans.next = head
        head.next = new_head
        return ans


# @lc code=end
