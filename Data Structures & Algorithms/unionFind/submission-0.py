class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]

    def find(self, x: int) -> int:
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]] # path compression
            x = self.parents[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return False

        if self.ranks[parent_x] > self.ranks[parent_y]:
            self.parents[parent_y] = parent_x
        elif self.ranks[parent_y] > self.ranks[parent_x]:
            self.parents[parent_x] = parent_y
        else:
            self.parents[parent_y] = parent_x
            self.ranks[parent_x] += 1

        return True

    def getNumComponents(self) -> int:
        return sum(int(i == parent) for i, parent in enumerate(self.parents))
