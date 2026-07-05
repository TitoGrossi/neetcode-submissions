from typing import List,Tuple, Dict


class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees, graph = self._build_graph(n, edges)

        queue: Deque[int] = deque([node for node, indegree in enumerate(indegrees) if indegree == 0])

        processed: Set[int] = set()

        order: List[int] = []
        while queue:
            node = queue.popleft()
            processed.add(node)
            order.append(node)

            for neighbor in graph[node]:
                if neighbor in processed:
                    return []
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == n else []

    @staticmethod
    def _build_graph(n: int, edges: List[List[int]]) -> Tuple[List[int], Dict[int, List[int]]]:
        graph: Dict[int, List[int]] = {i: [] for i in range(n)}
        indegrees: List[int] = [0 for _ in range(n)]

        for src, dest in edges:
            indegrees[dest] += 1
            graph[src].append(dest)

        return indegrees, graph
