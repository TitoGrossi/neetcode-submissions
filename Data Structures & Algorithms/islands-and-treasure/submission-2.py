class Solution:
    ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    INF = 2147483647
    WATER = -1
    TREASURE = 0

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue: Deque[Tuple[int, int, int]] = deque()

        for y in range(ROWS):
            for x in range(COLS):
                if grid[y][x] == self.TREASURE:
                    queue.append((y, x, 0))

        while queue:
            y, x, dist = queue.popleft()
            for dy, dx in self.ds:
                ny, nx = y + dy, x + dx
                if 0 <= ny < ROWS and 0 <= nx < COLS and grid[ny][nx] == self.INF:
                    grid[ny][nx] = dist + 1
                    queue.append((ny, nx, dist + 1))
