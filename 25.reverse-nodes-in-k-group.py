#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# # Definition for singly-linked list.
# from typing import Self


# class ListNode:
#     def __init__(self, val: int = 0, next: Self | None = None) -> None:
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy_head = ListNode(next=head)
        batch_left = dummy_head

        while True:
            curr = batch_left
            for _ in range(k):
                if not curr:
                    break
                curr = curr.next
            if not curr:
                break
            k_th = curr
            batch_right = k_th.next

            prev, curr = batch_right, batch_left.next
            while curr != batch_right:
                assert curr
                curr.next, prev, curr = prev, curr, curr.next

            tmp = batch_left.next
            batch_left.next = k_th
            batch_left = tmp

        return dummy_head.next


# @lc code=end
