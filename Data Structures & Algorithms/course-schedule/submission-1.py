from typing import Deque, Tuple

class Solution: 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_taken = 0

        graph, deps = self.__build_graph(numCourses, prerequisites)

        courses_taken = self.__bfs(graph, deps)

        return courses_taken >= numCourses

    @staticmethod
    def __build_graph(
        num_courses: int,
        prerequisites: List[List[int]]
    ) -> Tuple[Dict[int, Set[int]], Dict[int, int]]:
        graph: Dict[int, Set[int]] = {course: set() for course in range(num_courses)}
        deps: Dict[int, int] = {course: 0 for course in range(num_courses)}

        for prereq, blocked in prerequisites:
            deps[blocked] += 1
            graph[prereq].add(blocked)

        return graph, deps

    @staticmethod
    def __bfs(graph: Dict[int, Set[int]], deps: Dict[int, int]) -> int:
        free_queue = deque([course for course, num_deps in deps.items() if num_deps == 0])
        courses_taken = 0

        while free_queue:
            course = free_queue.popleft()
            courses_taken += 1
            for unblocked in graph[course]:
                deps[unblocked] -= 1
                if deps[unblocked] == 0:
                    free_queue.append(unblocked)

        return courses_taken
