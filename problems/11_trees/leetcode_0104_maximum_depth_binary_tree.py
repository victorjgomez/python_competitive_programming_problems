# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=featured-list&envId=top-interview-questions

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node: Optional[TreeNode], depth: int = 0):
        if node is None:
            return depth
        else:
            return max(self.dfs(node.left, depth + 1),
                       self.dfs(node.right, depth + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
