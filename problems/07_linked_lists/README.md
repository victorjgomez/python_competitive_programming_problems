# Linked Lists

## Idea
A singly linked list is a chain of nodes, where each node holds a `val` and a pointer to the `next` node. There is no random access, so you work by moving pointers. In exchange, inserting or removing a node is O(1) once you hold the node before it. Most problems come down to a few pointer patterns: a **dummy head**, **reversing** with three pointers, and **fast/slow** pointers.

**Use it when…**
- The input is a `ListNode` / `head` (LeetCode-style signatures).
- You must merge, split, reverse, or reorder nodes "in place" or with O(1) extra space.
- You need the middle node, cycle detection, or the k-th node from the end (fast/slow pointers).

## Complexity
| Operation | Time | Extra space |
|-----------|------|-------------|
| Traverse / find / length | O(n) | O(1) |
| Insert/delete after a known node | O(1) | O(1) |
| Merge two sorted lists (iterative) | O(n + m) | O(1) |
| Reverse (iterative) | O(n) | O(1) |
| Any of the above, recursive | same | O(n) call stack |

## Simple implementation
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(a, b):
    dummy = tail = ListNode()        # dummy head: no special case for the first node
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b               # attach whatever is left
    return dummy.next                # skip the dummy


def reverse(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next   # flip one arrow per step
    return prev


def from_list(xs):                   # helpers for testing
    dummy = tail = ListNode()
    for x in xs:
        tail.next = ListNode(x)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    assert to_list(merge_two_lists(from_list([1, 2, 4]), from_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(merge_two_lists(None, from_list([0]))) == [0]
    assert to_list(reverse(from_list([1, 2, 3]))) == [3, 2, 1]
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 1 | LeetCode | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | [`leetcode_0021_merge_two_sorted_lists.py`](leetcode_0021_merge_two_sorted_lists.py) | Recursion, building a new list | ⚠ `head = None` is passed into the helper. When either input is non-empty, the helper runs `newList.val = ...` on `None` and raises `AttributeError`. When both are empty it returns `None`, so the result is never filled in. ⚠ Starting with `head = ListNode()` would still leave an extra trailing `0` node, because the helper always creates `next` *before* it knows another value exists. Fix: use a dummy head and return `dummy.next` (see template). Reusing the existing nodes also avoids allocating new ones. |

## Pitfalls & takeaways
- Always handle empty lists (`None`) and one-node lists. A dummy head removes most of those special cases.
- Assigning to a parameter (`newList = ...`) never changes the caller's variable. Return the new head instead.
- In reversal, save `next` before you overwrite it. Tuple assignment in Python does that in one line.
- Recursive list code uses O(n) stack and fails on long lists (around 1000 nodes by default). Prefer iterative versions.
