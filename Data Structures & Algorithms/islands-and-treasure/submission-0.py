from collections import deque
from typing import Deque, Tuple


class Solution:
    ds: List[Tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    INF = 2147483647

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        queue: Deque[Tuple[int, int, int]] = deque() # y, x, dist

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 0:
                    queue.append((y, x, 1))

        while queue:
            y, x, dist = queue.popleft()
            for dy, dx in self.ds:
                ny, nx = y + dy, x + dx
                if (
                    0 <= ny < m and 0 <= nx < n
                    and grid[ny][nx] == self.INF
                ):
                    grid[ny][nx] = dist
                    queue.append((ny, nx, dist + 1))
