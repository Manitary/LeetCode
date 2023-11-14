#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root:
            return depth
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# @lc code=end
