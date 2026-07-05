class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for v1, v2 in edges:
            uf.union(v1, v2)

        return uf.get_roots()


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]
        self.ranks = [0 for i in range(n)]

    def find(self, v: int) -> int:
        while self.parents[v] != v:
            self.parents[v] = self.parents[self.parents[v]] # path compression
            v = self.parents[v]

        return v

    def union(self, v1: int, v2: int) -> bool:
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False

        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
        elif self.ranks[p2] > self.ranks[p1]:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1
            self.ranks[p1] += 1

    def get_roots(self):
        return sum(child == parent for child, parent in enumerate(self.parents))
