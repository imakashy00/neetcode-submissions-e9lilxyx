class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac_set, atl_set = set(), set()

        def dfs(r,c,vis_set, prev_height):
            if ((r, c) in vis_set or r < 0 or c < 0 or
                r == rows or c == cols or heights[r][c] < prev_height
            ): 
                return
            vis_set.add((r, c))
            dfs(r+1, c, vis_set, heights[r][c])
            dfs(r-1, c, vis_set, heights[r][c])
            dfs(r, c+1, vis_set, heights[r][c])
            dfs(r, c-1, vis_set, heights[r][c])

        for col in range(cols):
            dfs(0,col,pac_set, heights[0][col])
            dfs(rows-1,col, atl_set, heights[rows-1][col])
        
        for row in range(rows):
            dfs(row,0,pac_set, heights[row][0])
            dfs(row,cols-1, atl_set, heights[row][cols-1])
        
        res = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac_set and (row, col) in atl_set:
                    res.append([row, col])
        
        return res