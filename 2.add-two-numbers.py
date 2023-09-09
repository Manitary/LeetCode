#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
from typing import Self


class ListNode:
    def __init__(self, val: int = 0, next_node: Self | None = None) -> None:
        self.val = val
        self.next = next_node


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            new_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = new_sum // 10
            curr.next = ListNode(new_sum % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        assert dummy.next is not None
        return dummy.next


# @lc code=end
