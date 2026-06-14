class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        que = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    que.append((i,j))

        minutes = 0
        while que:
            rott_size = len(que)
            fresh_to_rott = False
            for _ in range(rott_size):
                r, c = que.popleft()
                dr_ar = [[-1,0],[1,0],[0,-1],[0,1]]
                for l, m in dr_ar:
                    if r+l >= 0 and c+m >= 0 and r+l <rows and c+m < cols and grid[r+l][c+m] == 1:
                        grid[r+l][c+m] = 2
                        que.append((r+l,c+m))
                        fresh_to_rott = True
            if fresh_to_rott: minutes+=1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: 
                    return -1

        return minutes
                
                    
        
        