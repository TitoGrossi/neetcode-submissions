from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self._build_graph(times)
        heap: list[tuple[int, int]] = [(0, k)]
        processed: set[int] = set()

        time = 0
        while heap and len(processed) < n:
            time, node = heappop(heap)
            if node in processed:
                continue
            processed.add(node)
            for neighbor, neighbor_time in graph[node]:
                if neighbor not in processed:
                    heappush(heap, (time + neighbor_time, neighbor))

        return time if len(processed) == n else -1

    @staticmethod
    def _build_graph(times: list[list[int]]) -> dict[int, list[tuple[int, int]]]:
        graph: dict[int, list[tuple[int, int]]] = defaultdict(list)

        for source, dest, time in times:
            graph[source].append((dest, time))

        return graph
