from typing import List, Tuple, Set


class Solution:
    ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def countPaths(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        def dfs(y: int, x: int, seen: Set[Tuple[int, int]]) -> int:
            if y == num_rows - 1 and x == num_cols - 1:
                return 1
            seen.add((y, x))

            paths = 0
            for dy, dx in self.ds:
                ny, nx = y + dy, x + dx
                if 0 <= ny < num_rows and 0 <= nx < num_cols and grid[ny][nx] == 0 and (ny, nx) not in seen:
                    paths += dfs(ny, nx, seen)

            seen.remove((y, x))
            return paths

        return dfs(0, 0, set([(0, 0)])) if grid[0][0] == 0 else 0
