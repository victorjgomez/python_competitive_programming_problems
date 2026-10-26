# Union-Find (Disjoint Set Union, DSU)

## Idea
Union-Find keeps a collection of disjoint groups and supports two operations: `find(x)` returns the representative (root) of the group containing `x`, and `union(a, b)` merges the groups of `a` and `b`. Each group is stored as a tree of parent pointers. With **path compression** (point nodes straight at the root while finding) and **union by size** (hang the smaller tree under the larger), both operations run in practically constant time.

**Use it when…**
- You need to know whether two items are "connected" / "equivalent", and connections are only ever added (never removed).
- You must count connected components, groups, provinces, islands, friend circles.
- The relation is transitive: "a ~ b and b ~ c implies a ~ c" (equivalent characters, synonyms, accounts merge).
- You are building a minimum spanning tree (Kruskal) or detecting a cycle in an undirected graph ("redundant connection").

## Complexity
| Operation | Time | Space |
|-----------|------|-------|
| `find` / `union` (path compression + union by size) | O(α(n)) amortized, effectively O(1) | O(n) for `parent` + `size` |
| Processing m edges on n nodes | O(n + m·α(n)) | O(n) |

## Simple implementation
The repo's reusable [`union_find.py`](union_find.py) does exactly this (path compression + union by size), but with dictionaries so it works on any hashable labels (characters, strings). For nodes numbered `0..n-1`, plain lists are shorter and faster:

```python
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))   # every node starts as its own root
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:       # walk up to the root
            root = self.parent[root]
        while self.parent[x] != root:          # path compression (iterative)
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a: int, b: int) -> bool:
        """Merge the groups of a and b. Return False if already together."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:      # union by size
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def count_components(n: int, edges) -> int:
    dsu = DSU(n)
    for a, b in edges:
        dsu.union(a, b)
    return dsu.components      # same as len({dsu.find(i) for i in range(n)})


if __name__ == "__main__":
    d = DSU(5)
    assert d.union(0, 1) and d.union(1, 2)
    assert not d.union(0, 2)                 # already connected -> cycle edge
    assert d.find(2) == d.find(0) != d.find(3)
    assert count_components(5, [(0, 1), (1, 2), (3, 4)]) == 2
    assert count_components(3, []) == 3
    print("ok")
```

## Problems solved
| # | Platform | Problem | File | Technique | Notes |
|---|----------|---------|------|-----------|-------|
| — | Reusable | Union-Find class | [`union_find.py`](union_find.py) | Dict-based DSU, recursive `find` with path compression, union by size | Raises `ValueError` for unknown keys; `union` returns nothing (returning a bool is handy for cycle detection). Recursive `find` is fine thanks to compression + union by size (tree height stays O(log n)). |
| 547 | LeetCode | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | [`leetcode_0547_number_of_provinces.py`](leetcode_0547_number_of_provinces.py) | DSU over cities 1..n, count distinct roots | Duplicates the class inline (needed for LeetCode submission). Scans the full matrix; scanning only `j > i` would halve the work since it is symmetric. |
| 1061 | LeetCode | [Lexicographically Smallest Equivalent String](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) | [`leetcode_1061_lexicographically_smallest_equivalent_string.py`](leetcode_1061_lexicographically_smallest_equivalent_string.py) | DSU over letters, then smallest letter per group | Correct: for each char it scans the sorted letters to find the first one in the same group (≤ 26 checks). Simpler alternative: always make the smaller letter the root, so `find(c)` is the answer directly. The `root_bc is None` check is dead code. |
| 1579 | LeetCode | [Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) | [`leetcode_1579_remove_max_edges_keep_graph_traversable.py`](leetcode_1579_remove_max_edges_keep_graph_traversable.py) | Two DSUs (Alice / Bob) | ⚠ Brute force: it recursively tries removing every edge and rebuilds both DSUs each time, which is exponential and will TLE. Known greedy: add type-3 edges to both DSUs first, then type 1 to Alice and type 2 to Bob; every `union` that returns `False` is a removable edge; answer is −1 if either DSU ends with more than 1 component. `MAX = 10*100` (= 1000) looks like a typo for a large sentinel. |

## Pitfalls & takeaways
- Always union the **roots** (`find(a)`, `find(b)`), never the raw nodes.
- Count components with a counter decremented on each successful union, or with `len({find(i) for i in nodes})`; never by reading `parent[]` directly (it may not be compressed yet).
- Mind 0-based vs 1-based labels (LeetCode 547 uses indices 0..n-1, 1579 uses nodes 1..n).
- Having `union` return `True/False` turns "was this edge redundant?" into a one-liner, which is the core of 1579 and of Kruskal's MST.
