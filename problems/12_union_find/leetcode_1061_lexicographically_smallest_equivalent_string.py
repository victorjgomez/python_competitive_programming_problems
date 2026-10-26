
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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uniques_characters = set()
        result = ""

        for z in zip(s1, s2):
            uniques_characters.add(z[0])
            uniques_characters.add(z[1])

        uniques_characters = sorted(uniques_characters)
        unionFind = UnionFind(uniques_characters)
        for z in zip(s1, s2):
            unionFind.union(z[0], z[1])

        for bc in baseStr:
            try:
                root_bc = unionFind.find(bc)
            except ValueError:
                result += bc
                continue
            for uc in uniques_characters:
                if root_bc is None:
                    break

                root_uc = unionFind.find(uc)
                if root_bc == root_uc:
                    result += uc
                    break

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.smallestEquivalentString("parker", "morris", "parser"))
    print(s.smallestEquivalentString("hello", "world", "hold"))
    print(s.smallestEquivalentString("leetcode", "programs", "sourcecode"))