# Priority Queue (Heaps)

## Idea
A priority queue always gives you the element with the smallest (or largest) priority next. It is usually implemented as a **binary heap**: a complete binary tree stored in a list where every parent is ≤ its children, so the minimum sits at index 0. In Python, `heapq` turns a plain list into a **min-heap**; for a max-heap, push negated priorities.

**Use it when…**
- You repeatedly need "the smallest / largest / next-most-urgent" element while elements keep arriving.
- The statement says "k largest", "k smallest", "top k", "k-th element", "median of a stream".
- You merge several sorted lists or schedule tasks/events by time.
- A graph algorithm needs "closest node next": Dijkstra, Prim.

## Complexity
| Operation | Time |
|-----------|------|
| `heappush` / `heappop` | O(log n) |
| peek `heap[0]` | O(1) |
| `heapify(list)` | O(n) |
| top-k of n items with a size-k heap | O(n log k) time, O(k) space |

## Simple implementation
```python
import heapq
import itertools


def k_smallest(nums, k):
    """Keep a max-heap (negated values) of size k holding the k smallest seen."""
    heap = []
    for x in nums:
        heapq.heappush(heap, -x)
        if len(heap) > k:
            heapq.heappop(heap)        # drop the largest of the k+1
    return sorted(-x for x in heap)


def k_largest(nums, k):
    """Min-heap of size k: its root is the k-th largest."""
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)        # drop the smallest
    return sorted(heap, reverse=True)


class TaskQueue:
    """(priority, counter, item) tuples: the counter breaks ties in FIFO
    order and stops Python from ever comparing the items themselves."""
    def __init__(self):
        self.heap, self.counter = [], itertools.count()

    def push(self, priority, item):
        heapq.heappush(self.heap, (priority, next(self.counter), item))

    def pop(self):
        priority, _, item = heapq.heappop(self.heap)
        return priority, item


if __name__ == "__main__":
    h = [5, 1, 4]
    heapq.heapify(h)                   # min-heap in O(n)
    assert h[0] == 1 and heapq.heappop(h) == 1
    assert k_smallest([7, 2, 9, 1, 5], 2) == [1, 2]
    assert k_largest([7, 2, 9, 1, 5], 2) == [9, 7]
    assert heapq.nsmallest(2, [7, 2, 9]) == [2, 7]   # built-in shortcut
    q = TaskQueue()
    q.push(2, {"name": "b"}); q.push(1, {"name": "a"}); q.push(2, {"name": "c"})
    assert [q.pop()[1]["name"] for _ in range(3)] == ["a", "b", "c"]
    print("ok")
```

## Problems solved
The folder [`pq_project/`](pq_project/) is a university project: a priority queue written from scratch, plus manual and timing tests. Run the scripts from inside `pq_project/` (e.g. `cd pq_project && python Test_PQ.py`), otherwise `from PQ import PriorityQueue` fails.

| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| — | University project | Custom `PriorityQueue` class | [`pq_project/PQ.py`](pq_project/PQ.py) | Array-based binary **min-heap** of `(priority, data)` tuples + `data_dict` mapping each data to its heap index (an *indexed heap*) | `insert_or_update` inserts, or **decreases** the priority of an existing item and sifts it up (higher priorities are ignored), the operation Dijkstra needs. Also `extract`, `peek`, `print_tree`. ⚠ `__str__` prints and returns `None`, so `str(pq)`/`print(pq)` raises `TypeError` (it should return a string). Method names say `silf_up/silf_down` (sift). |
| — | University project | Manual test 1 | [`pq_project/Prueba1.py`](pq_project/Prueba1.py) | Insert/update then repeated `extract` + `print_tree` | Inserts `"T"` and `"B"` twice to exercise the update path. |
| — | University project | Manual test 2 | [`pq_project/Prueba2.py`](pq_project/Prueba2.py) | Larger insert/update + extraction trace | Prints heap and index dict after each extract. |
| — | University project | `heapq` comparison | [`pq_project/Pruebas.py`](pq_project/Pruebas.py) | Standard `heapq` | Scratch check of how `heapq` orders tuples; does not use `PQ.py`. |
| — | University project | Correctness + timing tests | [`pq_project/Test_PQ.py`](pq_project/Test_PQ.py) | Random insert / update / extract, checks extraction order | ⚠ Uses `time.clock()`, removed in Python 3.8, so the update test crashes with `AttributeError` on modern Python; replace with `time.perf_counter()`. |

## Pitfalls & takeaways
- `heapq` is a **min**-heap only; for a max-heap push `-x` (or `(-priority, ...)`) and negate back when popping.
- On ties Python compares the next tuple field; if that is a dict/object it raises `TypeError`. Add a counter: `(priority, counter, item)`.
- `heapq` has no decrease-key: either use an indexed heap like `PQ.py`, or push a new entry and skip stale ones when popped ("lazy deletion").
- `heap[0]` is the minimum, but the list is **not** sorted; never index past 0 expecting order.
