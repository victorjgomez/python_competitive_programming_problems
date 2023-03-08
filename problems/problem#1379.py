# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    target_clone = None
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.dfs(cloned, target.val)
        return Solution.target_clone

    def dfs(self, cloned: TreeNode, value):
        if cloned.val == value:
            Solution.target_clone = cloned

        if cloned.left:
            self.dfs(cloned.left, value)
        if cloned.right:
            self.dfs(cloned.right, value)


if __name__ == "__main__":
    root = TreeNode(7)
    child1 = TreeNode(4)
    child2 = TreeNode(3)
    child1_of_child2 = TreeNode(6)
    child2_of_child2 = TreeNode(19)

    root.left = child1
    root.right = child2
    child2.left = child1_of_child2
    child2.right = child2_of_child2

    solution = Solution()

    print(solution.getTargetCopy(original = root, cloned = root, target = child2).val)
