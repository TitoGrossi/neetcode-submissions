from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph: Dict[int, Set[int]] = defaultdict(set)

        for pre, course in prerequisites:
            graph[pre].add(course)

        answers: List[bool] = []
        for pre_candidate, course in queries:
            if self.can_reach(pre_candidate, course, graph):
                graph[pre_candidate].add(course)
                answers.append(True)
            else:
                answers.append(False)

        return answers

    @staticmethod
    def can_reach(pre_candidate: int, course: int, graph: Dict[int, List[int]]) -> bool:
        queue: Deque[Tuple[int, Optional[int]]] = deque([(pre_candidate, None)])
        seen: Set[int] = set([pre_candidate])

        while queue:
            node, parent = queue.popleft()
            if node == course:
                return True
            for neighbor in graph[node]:
                if parent is not None:
                    graph[parent].add(neighbor)

                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, node))

        return False
