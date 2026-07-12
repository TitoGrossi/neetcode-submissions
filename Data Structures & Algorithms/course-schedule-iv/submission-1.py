from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph: List[Set[int]] = [set() for _ in range(numCourses)]

        for pre, course in prerequisites:
            graph[pre].add(course)


        for node in range(numCourses):
            self.traverse(node, graph)

        answers: List[bool] = []
        for pre_candidate, course in queries:
            answer = True if course in graph[pre_candidate] else False
            answers.append(answer)

        return answers

    @staticmethod
    def traverse(root: int, graph: List[Set[int]]) -> bool:
        static_graph_copy = [neighbors.copy() for neighbors in graph]
        queue: Deque[int] =  deque([root])
        seen: Set[int] = set([root])

        while queue:
            node = queue.popleft()
            graph[root].add(node)
            for neighbor in static_graph_copy[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
