class Solution:
    ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue: Deque[Tuple[int, int, int]] = deque()
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        for y in range(ROWS):
            for x in range(COLS):
                if grid[y][x] == 0:
                    queue.append((y, x, 0))
                    visited[y][x] = True

        while queue:
            y, x, dist = queue.popleft()
            grid[y][x] = dist
            for dy, dx in self.ds:
                ny, nx = y + dy, x + dx
                if (
                    0 <= ny < ROWS and
                    0 <= nx < COLS and
                    grid[ny][nx] != -1 and
                    not visited[ny][nx]
                ):
                    visited[ny][nx] = True
                    queue.append((ny, nx, dist + 1))
