#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root


# @lc code=end
