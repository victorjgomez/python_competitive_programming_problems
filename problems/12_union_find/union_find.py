
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

