class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        lg_island = 0
        seen = set()
        def dfs(i,j):
            if ( i < 0 or j < 0 or i >= rows or j >= cols or (i,j) in seen or grid[i][j] == 0):
                return 0
            seen.add((i,j))
            return 1 + dfs(i -1 ,j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    lg_island = max(dfs(i,j), lg_island)
        return lg_island

