#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# from typing import Optional, Self


# class TreeNode:
#     def __init__(
#         self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None
#     ) -> None:
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# @lc code=end
