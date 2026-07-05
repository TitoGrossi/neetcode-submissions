from typing import Deque, List, Tuple, Set


class Solution:
    ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def shortestPath(self, grid: List[List[int]]) -> int:
        queue: Deque[Tuple[int, int, int]] = deque([(0, 0, 0)])

        seen: Set[Tuple[int, int]] = set([(0, 0)])
        while queue:
            y, x, dist = queue.popleft()
            if y == len(grid) - 1 and x == len(grid[0]) - 1:
                return dist

            for dy, dx in self.ds:
                ny, nx =  y + dy, x + dx
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == 0 and (ny, nx) not in seen:
                    queue.append((ny, nx, dist + 1))
        
        return -1
