# Stacks & Queues

## Idea
A **stack** is LIFO (last in, first out): you push and pop at the same end. It fits anything "nested" or "most recent first", like matching brackets, undo, or the DFS call stack. A **queue** is FIFO (first in, first out): you push at the back and pop from the front. It fits simulations of lines/rounds and BFS. A **monotonic stack** keeps its elements sorted, so each element is pushed and popped once. That answers "next greater/smaller element" questions in O(n).

**Use it when…**
- The statement has brackets, nesting, "valid sequence", or undo/backspace operations (stack).
- You need the *nearest* greater/smaller element to the left or right (monotonic stack).
- People or items "go to the back of the line", or things happen in rounds (queue simulation).
- You need the shortest path in an unweighted graph or grid (BFS with a queue).

## Complexity
| Operation | `list` as stack | `collections.deque` | `queue.Queue` / `LifoQueue` |
|-----------|-----------------|---------------------|-----------------------------|
| push / pop at the end | O(1) amortized | O(1) | O(1) + locking overhead |
| pop from the front | **O(n)** (`list.pop(0)`) | O(1) (`popleft`) | O(1) + locking overhead |

- Monotonic stack over n elements: O(n) time, O(n) space.
- BFS: O(V + E) time, O(V) space.

## Simple implementation
```python
# Stack patterns: bracket matching + monotonic stack (next greater element)
def is_valid(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []                       # a plain list is the idiomatic stack
    for ch in s:
        if ch in pairs:              # closing bracket: must match the top
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)         # opening bracket: push
    return not stack                 # leftovers mean something was never closed


def next_greater(nums):
    """res[i] = first element to the right of i that is > nums[i], or -1."""
    res = [-1] * len(nums)
    stack = []                       # indices; their values decrease from bottom to top
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            res[stack.pop()] = x     # x is the answer for every smaller element we pop
        stack.append(i)
    return res


if __name__ == "__main__":
    assert is_valid("([]{})") and not is_valid("(]") and not is_valid("((")
    assert next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
```

```python
# Queue pattern: BFS shortest distance in an unweighted graph
from collections import deque


def bfs(adj, start):
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()              # O(1); never use list.pop(0) for this
        for v in adj[u]:
            if v not in dist:        # mark when you enqueue, not when you dequeue
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


if __name__ == "__main__":
    adj = {0: [1, 2], 1: [3], 2: [3], 3: [4], 4: []}
    assert bfs(adj, 0) == {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| 1 | GeeksforGeeks | [Stack in Python](https://www.geeksforgeeks.org/stack-in-python/) | [`example_stack_deque.py`](example_stack_deque.py) | `deque` as stack | API demo: `append` / `pop`. Popping an empty deque raises `IndexError`. |
| 2 | GeeksforGeeks | [Stack in Python](https://www.geeksforgeeks.org/stack-in-python/) | [`example_stack_lifoqueue.py`](example_stack_lifoqueue.py) | `queue.LifoQueue` | Another API for the same thing, not a better one. `get()` on an empty queue **blocks forever**. It is thread-safe and slower, so use `list`/`deque` in CP. |
| 3 | GeeksforGeeks | [Queue in Python](https://www.geeksforgeeks.org/queue-in-python/) | [`example_queue_deque.py`](example_queue_deque.py) | `deque` as queue | API demo: `append` / `popleft`. This is the queue to use in CP. |
| 4 | GeeksforGeeks | [Queue in Python](https://www.geeksforgeeks.org/queue-in-python/) | [`example_queue_queue.py`](example_queue_queue.py) | `queue.Queue` | Same idea as #3, with `maxsize`, `full()` and `empty()`. It is built for threads, so the locks add overhead. Prefer `deque`. |
| 5 | LeetCode | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [`leetcode_0020_valid_parentheses.py`](leetcode_0020_valid_parentheses.py) | Recursion + list as stack | Correct logic, but there is one recursive call per character and it slices with `list_c[1:]` / `left[:-1]`. That makes it O(n²) time, and with n = 10⁴ it can pass Python's default recursion limit. ⚠ `new_left = left` is an alias, not a copy, so `append` mutates `left`. It is harmless here but easy to trip on. An iterative loop is simpler (see template). |
| 6 | LeetCode | [1614. Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) | [`leetcode_1614_max_nesting_depth_parentheses.py`](leetcode_1614_max_nesting_depth_parentheses.py) | Depth counter | A counter replaces the stack because only the stack's *size* matters. O(n) time, O(1) space. Good simplification (the stack version is left commented out). |
| 7 | LeetCode | [1700. Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/) | [`leetcode_1700_students_unable_to_eat_lunch.py`](leetcode_1700_students_unable_to_eat_lunch.py) | `deque` simulation, recursive rounds | Each call is one full pass over the line. It stops when a whole round serves nobody. Up to O(n²) work, which is fine for n ≤ 100. The check `students[0] in [0, 1]` is redundant. O(n) alternative: count the 0s and 1s, then serve sandwiches until the top one's type has a count of 0. |

## Pitfalls & takeaways
- Use `list` for stacks and `collections.deque` for queues. `list.pop(0)` is O(n). `queue.Queue` / `LifoQueue` are for threads: they are slower and `get()` blocks on an empty queue.
- Check `if stack:` before `stack.pop()` or `stack[-1]`, because an empty pop raises `IndexError`.
- If you only need the stack's size (like a nesting depth), keep a counter instead.
- Prefer iterative loops over recursion that slices lists. Slicing copies the list (O(n) per call), and deep recursion hits the recursion limit.
