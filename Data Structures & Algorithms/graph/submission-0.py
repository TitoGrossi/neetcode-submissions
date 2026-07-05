class Graph:
    
    def __init__(self):
        self._graph: Dict[int, Set[int]] = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self._graph:
            self._graph[src] = set()
        if dst not in self._graph:
            self._graph[dst] = set()
        
        self._graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self._graph or dst not in self._graph[src]:
            return False

        self._graph[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self._graph:
            return False
        
        queue: Deque[int] = deque([src])
        seen: Set[int] = set([src])

        while queue:
            node = queue.popleft()
            if node == dst:
                return True

            for neighbor in self._graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return False
