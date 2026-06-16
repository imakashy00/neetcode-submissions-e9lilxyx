class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # get all the edged O's in a list or set
        # find all the O's that can be reached from there 
        # store all the unique O's position 
        # Make every O's position X except the regions touching the edges
        rows, cols = len(board), len(board[0])
        os_pos = [(x, y) for x in range(rows) for y in range(cols) if board[x][y] == 'O']
        edge_os = [(x, y) for x, y in os_pos if x == 0 or x == rows - 1 or y == 0 or y == cols -1 ]
        visited = set()

        def dfs(r, c , visited):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] == 'X' or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1, c , visited)
            dfs(r-1, c , visited)
            dfs(r, c+1 , visited)
            dfs(r, c-1 , visited)

        for i,j in edge_os:
            dfs(i, j, visited)

        for x, y in os_pos:
            if (x, y) not in visited:
                board[x][y] = 'X'
        