#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.
# from typing import Optional, Self


# class Node:
#     def __init__(
#         self, x: int, next: Optional[Self] = None, random: Optional[Self] = None
#     ) -> None:
#         self.val = x
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        pairs: dict['Node', 'Node'] = {}
        curr = head
        while curr:
            pairs[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            pairs[curr].next = pairs[curr.next] if curr.next else None
            pairs[curr].random = pairs[curr.random] if curr.random else None
            curr = curr.next

        return pairs[head]


# @lc code=end
