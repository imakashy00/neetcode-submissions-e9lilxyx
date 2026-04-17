class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0, len(matrix)*len(matrix[0])-1
        while i <= j:
            mid = (i+j)//2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            print(i,j,mid,row,col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                i = mid + 1
            else :
                j = mid - 1
        return False