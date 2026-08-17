from typing import Tuple, Deque


class Solution:
    __ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue, fresh_fruits = self.__pre_process(grid)
        return self.__process(grid, queue, fresh_fruits)

    @staticmethod
    def __pre_process(grid: List[List[int]]) -> Tuple[Deque[Tuple[int, int, int]], int]:
        queue: Deque[Tuple[int, int, int]] = deque()
        fresh_fruits = 0

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 1:
                    fresh_fruits += 1
                elif cell == 2:
                    queue.append((y, x, 0))

        return queue, fresh_fruits

    def __process(
        self,
        grid: List[List[int]],
        queue: Deque[Tuple[int, int, int]],
        fresh_fruits: int,
    ) -> int:
        minutes = 0

        while queue:
            y, x, minutes = queue.popleft()
            for dy, dx in self.__ds:
                ny, nx = y + dy, x + dx
                if (
                    0 <= ny < len(grid)and 0 <= nx < len(grid[0])
                    and grid[ny][nx] == 1
                ):
                    fresh_fruits -= 1
                    grid[ny][nx] = 2
                    queue.append((ny, nx, minutes + 1))

        return minutes if fresh_fruits == 0 else -1
