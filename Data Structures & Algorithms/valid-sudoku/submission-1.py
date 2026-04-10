class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows:set = [set() for _ in range(9)]
        cols:set = [set() for _ in range(9)]
        squares:set = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                square_value = (i//3)*3 + j//3
                if num in rows[i] or num in cols[j] or num in squares[square_value]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                squares[square_value].add(num)
        return True
