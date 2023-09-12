#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# from typing import Self
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val: int = 0, next: Self | None = None) -> None:
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head:
            return
        nodes: dict[int, ListNode] = {}
        i = -1
        curr = head
        while curr:
            i += 1
            nodes[i] = curr
            curr = curr.next
        t = i + 1 - n
        if t == 0:
            return head.next
        nodes[t - 1].next = None if t == i else nodes[t + 1]
        return head


# @lc code=end
