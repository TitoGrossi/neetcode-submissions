from dataclasses import dataclass, field

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(
            parents = {node: node for node in range(1, len(edges) + 1)},
            ranks = {node: 1 for node in range(1, len(edges) + 1)}
        )
        
        for node1, node2 in edges:
            if not union_find.union(node1, node2):
                return [node1, node2]

        return []


@dataclass
class UnionFind:
    parents: Dict[int, int] = field(default = dict)
    ranks: Dict[int, int] = field(default = dict)

    def union(self, node1: int, node2: int) -> bool:
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False
        
        if self.ranks[parent1] > self.ranks[parent2]:
            self.parents[parent2] = parent1
        elif self.ranks[parent2] > self.ranks[parent1]:
            self.parents[parent1] = parent2
        else:
            self.parents[parent2] = parent1
            self.ranks[parent1] += 1
        
        return True

    def find(self, node: int) -> int:
        while node != self.parents[node]:
            node = self.parents[node]

        return node
