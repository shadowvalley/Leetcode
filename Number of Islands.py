class Solution:
    ROW_DIREC = [-1, 1, 0, 0]
    COL_DIREC = [0, 0, -1, 1]

    def isValid(self, row, col, grid):
        rc = len(grid)
        cc = len(grid[0])

        if row >= 0 and row < rc and col >= 0 and col < cc and grid[row][col] == "1":
            return True
        return False

    def numIslands(self, grid: List[List[str]]) -> int:
        rc = len(grid)
        cc = len(grid[0])
        islandCount = 0

        visited = [[False] * cc for _ in range(rc)]
        for r in range(rc):
            for c in range(cc):
                if grid[r][c] == "1" and not visited[r][c]:
                    # island found
                    islandCount += 1
                    self.dfs(r, c, grid, visited)
        return islandCount

    def dfs(self, r, c, grid, visited):
        visited[r][c] = True

        for i in range(4):
            nrow = r + self.ROW_DIREC[i]
            ncol = c + self.COL_DIREC[i]

            if self.isValid(nrow, ncol, grid) and not visited[nrow][ncol]:
                self.dfs(nrow, ncol, grid, visited)
