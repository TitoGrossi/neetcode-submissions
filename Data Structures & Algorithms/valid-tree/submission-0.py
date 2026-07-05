from collections import defaultdict
from typing import Dict, Optional, Set

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph: Dict[int, List[int]] = defaultdict(list)
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited: Set[int] = set()
        visited.add(0)
        has_cycle = self.detect_cycle(graph, 0, None, visited)

        return not has_cycle and len(visited) == n
    
    def detect_cycle(
        self,
        graph: Dict[int, List[int]],
        node: int,
        parent: Optional[int],
        visited: Set[int],
    ) -> bool: # dfs
        for neighbor in graph[node]:
            if neighbor != parent:
                if neighbor in visited:
                    return True
                visited.add(neighbor)
                has_cycle = self.detect_cycle(graph, neighbor, node, visited)
                if has_cycle:
                    return True

        return False
