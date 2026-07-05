class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        union_find = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(i):
                if isConnected[i][j]:
                    union_find.union(i, j)

        return union_find.trees()


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = {node: node for node in range(n)}
        self.ranks = {node: 1 for node in range(n)}

    def union(self, node1: int, node2: int) -> bool:
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False

        if self.ranks[self.parents[parent1]] > self.ranks[self.parents[parent2]]:
            self.parents[parent2] = parent1
        elif self.ranks[self.parents[parent2]] > self.ranks[self.parents[parent1]]:
            self.parents[parent1] = parent2
        else:
            self.parents[parent2] = parent1
            self.ranks[parent1] += 1

        return True
    
    def find(self, node: int) -> int:
        while self.parents[node] != node:
            self.parents[node] = self.parents[self.parents[node]] # path compression
            node = self.parents[node]

        return node

    def trees(self):
        return sum(parent == node for parent, node in self.parents.items())
