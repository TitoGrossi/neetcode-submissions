from heapq import heappush, heappop


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self._build_graph(flights)
        heap: list[tuple[int, int, int]] = [(0, 0, src)] # (cost, stops, node)
        is_processed = [False for _ in range(n)]
        seen_edges: set[tuple[int, int]] = set()
        max_value = sum(cost for _, _, cost in flights) + 1
        costs = [max_value for _ in range(n)]
        costs[src] = 0

        while heap:
            cost, stops, node = heappop(heap)
            costs[node] = min(costs[node], cost)

            for neighbor, neighbor_cost in graph[node]:
                if neighbor != dst and stops + 1 > k:
                    continue
                if (node, neighbor) not in seen_edges:
                    seen_edges.add((node, neighbor))
                    heappush(heap, (cost + neighbor_cost, stops + 1, neighbor))

        return -1 if costs[dst] == max_value else costs[dst]

    def _build_graph(self, flights: List[List[int]]) -> dict[int, list[tuple[int, int]]]:
        graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for src, dest, price in flights:
            graph[src].append((dest, price))

        return graph
