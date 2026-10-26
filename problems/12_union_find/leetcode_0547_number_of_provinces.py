from typing import List


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

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        unique_elements = [i for i in range(1, len(isConnected) + 1)]

        unionFind = UnionFind(unique_elements)

        for i in range(0, len(isConnected)):
            for j in range(0, len(isConnected)):
                if isConnected[i][j] == 1:
                    unionFind.union(j+1, i+1)

        result = set()
        for element in unique_elements:
            result.add(unionFind.find(element))

        return len(result)



if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
