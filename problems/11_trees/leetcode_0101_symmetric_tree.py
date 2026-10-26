# Definition for a binary tree node.
from typing import Optional


# https://leetcode.com/problems/symmetric-tree/?envType=featured-list&envId=top-interview-questions

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solution(self, node_left: Optional[TreeNode], node_right: Optional[TreeNode]) -> bool:
        if node_left is None and node_right is None:
            return True
        elif node_left is None or node_right is None:
            return False
        elif node_left.val != node_right.val:
            return False
        else:
            return self.solution(node_left.left, node_right.right) and self.solution(node_left.right, node_right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.solution(root.left, root.right)
