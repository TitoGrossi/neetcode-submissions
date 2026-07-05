from heapq import heappush, heappop
from typing import Dict, List, Tuple

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        distances: Dict[int, int] = {i: -1 for i in range(n)}
        graph: Dict[int, List[Tuple[int]]] = {i: [] for i in range(n)}

        for source, dest, weight in edges:
            graph[source].append((dest, weight))

        heap: List[Tuple[int, int]] = [(0, src)]
        nodes_processed = 0
        while heap and nodes_processed < n:
            weight, node = heappop(heap)
            if distances[node] == -1:
                nodes_processed += 1
                distances[node] = weight
            else:
                distances[node] = min(distances[node], weight)

            for neighbor, weight_neighbor in graph[node]:
                heappush(heap, (weight + weight_neighbor, neighbor))

        return distances
