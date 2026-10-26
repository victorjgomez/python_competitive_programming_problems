""""
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/?envType=problem-list-v2&envId=5lhmb4mj
I think for this one I need two intances of unionfind one for bob and other for alice.

Once I complete both I need to compare both somehow to first determine is they are fully traversable and then which nodes
could I remove.
"""

MAX = 10*100

class UnionFind():

    def __init__(self, input: list):
        self.representative = {}
        self.size = {}

        for i in input:
            self.size[i] = 1
            self.representative[i] = i


    def find(self, x):
        if self.representative.get(x) is None:
            raise ValueError("Can't find {}".format(x))
        elif x == self.representative.get(x):
            return x
        else:
            root = self.find(self.representative.get(x))
            self.representative[x] = root
            return root

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.size[x] > self.size[y]:
            self.representative[y] = x
            self.size[x] += self.size[y]
        else:
            self.representative[x] = y
            self.size[y] += self.size[x]

    def all_equal(self) -> bool:
        values = self.representative.values()

        values_set = set()
        for x in values:
            values_set.add(self.find(x))

        return len(values_set) == 1

    def get_nodes(self) -> int:
        values = self.representative.values()
        return len(values)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        min_edges = self.min_num_edges(n, edges)
        if min_edges == MAX:
            return -1

        max_edges = len(edges) - min_edges
        return max_edges

    def min_num_edges(self, n: int, edges: list[list[int]]) -> int:
        alice, bod = self.build(n, edges)
        if not self.is_traversable_for_both(alice, bod):
            return MAX

        solutions = set()
        solutions.add(len(edges))

        for edge in edges:
            edges_universe = edges.copy()
            edges_universe.remove(edge)
            solutions.add(self.min_num_edges(n, edges_universe))

        return min(solutions)


    def build(self, n: int, edges: list[list[int]]):

        alice = UnionFind([i for i in range(1, n+1)])
        bod = UnionFind([i for i in range(1, n+1)])

        for edge in edges:
            if edge[0] == 1:
                alice.union(edge[1], edge[2])
                #alice.union(edge[2], edge[1])
            elif edge[0] == 2:
                bod.union(edge[1], edge[2])
                # bod.union(edge[2], edge[1])
            else:
                alice.union(edge[1], edge[2])
                # alice.union(edge[2], edge[1])
                bod.union(edge[1], edge[2])
                # bod.union(edge[2], edge[1])

        return alice, bod


    def is_traversable_for_both(self, alice: UnionFind, bod: UnionFind) -> bool:
        if not alice.all_equal() or not bod.all_equal():
            return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
    # print(s.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
    # print(s.maxNumEdgesToRemove(4, [[3,2,3],[1,1,2],[2,3,4]]))
    #print(s.maxNumEdgesToRemove(4, [[3,1,2], [3,3,4], [1,1,3],[2,2,4]]))
