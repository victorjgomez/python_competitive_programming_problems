# Trees (Binary Trees)

## Idea
A binary tree is a set of nodes where each node has a value and up to two children (`left`, `right`). Most tree problems are solved by **traversing** the tree: depth-first (DFS, usually recursive: solve for the children, combine at the parent) or breadth-first (BFS, level by level with a queue). The key skill is defining what the recursive call returns for a subtree, and what happens at the base case (`node is None`).

**Use it when…**
- The input is a `root: TreeNode` (LeetCode style) or a list of parent/child edges with no cycles.
- You need a property computed from subtrees: depth, height, size, sum, "is balanced / symmetric / same".
- The question is about levels: "level order", "rightmost node of each level", "minimum depth".
- You must locate a node, or compare two trees walked in parallel.

## Complexity
| Operation | Time | Space |
|-----------|------|-------|
| DFS (recursive) | O(n) | O(h) call stack (h = height; O(n) worst case for a skewed tree) |
| BFS (level order) | O(n) | O(w) queue (w = maximum width, up to n/2) |

## Simple implementation
```python
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(node: Optional[TreeNode]) -> int:
    """Recursive DFS: depth of a subtree = 1 + the deeper child."""
    if node is None:          # base case: empty tree has depth 0
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Iterative BFS: process the tree one level at a time."""
    if root is None:
        return []
    levels, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):   # exactly the nodes of the current level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
    return levels


if __name__ == "__main__":
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3
    assert max_depth(None) == 0
    assert level_order(root) == [[3], [9, 20], [15, 7]]
    print("ok")
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 101 | LeetCode | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | [`leetcode_0101_symmetric_tree.py`](leetcode_0101_symmetric_tree.py) | Recursive DFS on two nodes at once | Clean mirror check: compare `left.left` with `right.right` and `left.right` with `right.left`. |
| 104 | LeetCode | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [`leetcode_0104_maximum_depth_binary_tree.py`](leetcode_0104_maximum_depth_binary_tree.py) | Recursive DFS | Passes the depth down as a parameter and returns it at `None`; works, though the "return `1 + max(children)`" form above needs no extra parameter. |
| 1379 | LeetCode | [Find a Corresponding Node of a Binary Tree in a Clone of That Tree](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/) | [`leetcode_1379_find_node_in_cloned_tree.py`](leetcode_1379_find_node_in_cloned_tree.py) | DFS on the cloned tree matching `target.val` | Works only because the values are guaranteed unique. ⚠ The follow-up (repeated values) needs walking `original` and `cloned` in parallel and comparing nodes with `is target`. The result is kept in a class attribute and the DFS does not stop early once found. |

## Pitfalls & takeaways
- Always handle `node is None` first; most bugs come from a missing or wrong base case.
- Recursion depth: Python's default limit is ~1000, so a skewed tree with 10^5 nodes needs `sys.setrecursionlimit(...)` or an iterative DFS/BFS with an explicit stack/queue.
- Prefer returning values from the recursion over storing results in globals or class attributes: it is easier to reason about and safe across multiple test cases.
- Compare nodes by identity (`is`) when the question is "which node", and by `val` only when values are guaranteed unique.
