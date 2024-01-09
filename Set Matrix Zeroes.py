class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = [-1]*len(matrix)
        cols = [-1]*len(matrix[0])

        for i in range(len(rows)):
            for j in range(len(cols)):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0
        
        # set matrix to zero based on the rows and cols matrix
        for i in range(len(rows)):
            for j in range(len(cols)):
                if rows[i] == 0 or cols[j] == 0:
                    matrix[i][j] = 0

        return matrix