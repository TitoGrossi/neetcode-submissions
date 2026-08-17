class Solution:
    __ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        N_ROWS, N_COLS = len(grid), len(grid[0])
        visited: List[List[bool]] = [[False for _ in row]for row in grid]

        def dfs(row: int, col: int) -> None:
            visited[row][col] = True
            for drow, dcol in self.__ds:
                nrow, ncol = row + drow, col + dcol
                if (
                    0 <= nrow < N_ROWS and 0 <= ncol < N_COLS
                    and grid[nrow][ncol] == "1"
                    and not  visited[nrow][ncol]
                ):
                    dfs(nrow, ncol)

        num_islands = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "1" and not visited[y][x]:
                    dfs(y, x)
                    num_islands += 1

        return num_islands
