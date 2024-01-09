from queue import Queue

class Pair:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

class Solution:
    def isValid(self, row, col, mat):
        rowsCount = len(mat)
        colsCount = len(mat[0])

        if row >= 0 and row < rowsCount and col >= 0 and col < colsCount:
            return True
        return False

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rowsCount = len(mat)
        colsCount = len(mat[0])
        visited = [[False]* colsCount for _ in range(rowsCount)]
        distanceMat = [[0]* colsCount for _ in range(rowsCount)]
        q = Queue()

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    # Append every coordinate with value 0 and it's distance 
                    # to itself as zero to the queue
                    visited[r][c] = True
                    distanceMat[r][c] = 0
                    q.put(Pair(r, c, 0))
        
        # BFS
        rowDir = [-1, 1, 0, 0]
        colDir = [0, 0, 1, -1]

        while not q.empty():
            pr = q.get()
            row = pr.row
            col = pr.col
            distance = pr.dist

            for i in range(4):
                nrow = row + rowDir[i]
                ncol = col + colDir[i]

                if self.isValid(nrow, ncol, mat) and not visited[nrow][ncol]:
                    distanceMat[nrow][ncol] = distance + 1
                    visited[nrow][ncol] = True
                    q.put(Pair(nrow, ncol, distance + 1))
        
        return distanceMat