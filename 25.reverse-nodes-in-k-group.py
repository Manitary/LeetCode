#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# from typing import Self


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val: int = 0, next: Self | None = None) -> None:
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return
        ans = ListNode()
        curr = ans
        while head:
            batch: list[ListNode] = []
            for _ in range(k):
                if not head:
                    break
                batch.append(head)
                head = head.next
            if len(batch) < k:
                curr.next = batch[0]
                while curr.next:
                    curr = curr.next
                break
            for n in batch[::-1]:
                curr.next = n
                curr = curr.next
        curr.next = None
        return ans.next


# @lc code=end
