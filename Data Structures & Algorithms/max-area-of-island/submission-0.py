class Solution:
    ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for _ in row] for row in grid]

        def dfs(y: int, x: int) -> int:
            if grid[y][x] == 0:
                return 0
            
            area = 1
            for dy, dx in self.ds:
                ny, nx = y + dy, x + dx
                if (
                    0 <= ny < ROWS and
                    0 <= nx < COLS and
                    grid[ny][nx] == 1
                    and not visited[ny][nx]
                ):
                    visited[ny][nx] = True
                    area += dfs(ny, nx)

            return area
        
        res = 0
        for y in range(ROWS):
            for x in range(COLS):
                if not visited[y][x]:
                    visited[y][x] = True
                    res = max(res, dfs(y, x))

        return res
