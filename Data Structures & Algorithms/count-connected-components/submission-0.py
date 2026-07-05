from typing import Dict, List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for node1, node2 in edges:
            uf.union(node1, node2)

        return uf.num_roots()


class UnionFind:
    def __init__(self, n: int):
        self.parents: Dict[int, int] = {i: i for i in range(n)}
        self.ranks: Dict[int, int] = {i: 0 for i in range(n)}
        self._num_roots = n

    def union(self, node1: int, node2: int) -> None:
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return

        # rank optimization
        if self.ranks[parent1] > self.ranks[parent2]:
            self.parents[parent2] = parent1
        elif self.ranks[parent2] > self.ranks[parent1]:
            self.parents[parent1] = parent2
        else:
            self.parents[parent2] = parent1
            self.ranks[parent1] += 1
        
        self._num_roots -= 1

    def find(self, node: int) -> int:
        while node != self.parents[node]:
            # path compression optimization
            self.parents[node] = self.parents[node]
            node = self.parents[node]

        return node

    def num_roots(self) -> int:
        return self._num_roots
