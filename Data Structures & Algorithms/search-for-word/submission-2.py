class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(i,j,wrd):
            if not wrd:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != wrd[0]:
                return False
            visited = board[i][j]
            board[i][j] = '#'
            res = (backtrack(i + 1, j, wrd[1:]) or 
                    backtrack(i - 1, j, wrd[1:]) or 
                    backtrack(i, j + 1, wrd[1:]) or 
                    backtrack(i, j - 1, wrd[1:]))
            board[i][j] = visited
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i,j,word):
                        return True
        return False