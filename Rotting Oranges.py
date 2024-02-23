from queue import Queue

class Pair:
    def __init__(self, row, col, time):
        self.row = row
        self.col = col
        self.time = time 

class Solution:

    def isValid(self, row, col, grid) -> bool:
        rc = len(grid)
        cc = len(grid[0])
        if row >= 0 and row < rc and col >= 0 and col < cc:
            return True 
        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rc = len(grid)
        cc = len(grid[0])

        fresh_orange_count = 0
        queue = Queue()
        for r in range(rc):
            for c in range(cc):
                if grid[r][c] == 1:
                    fresh_orange_count += 1
                elif grid[r][c] == 2:
                    queue.put(Pair(r, c, 0))
        
        # Now do Multi-source BFS
        ROW_DIREC = [-1, 1, 0, 0]
        COL_DIREC = [0, 0, -1, 1]

        time_to_rot = 0
        while not queue.empty():
            pair_ele = queue.get()
            row = pair_ele.row
            col = pair_ele.col
            time = pair_ele.time
            time_to_rot = max(time_to_rot, time)

            # check all 4 directions
            for i in range(4):
                nrow = row + ROW_DIREC[i]
                ncol = col + COL_DIREC[i]

                if self.isValid(nrow, ncol, grid) and grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2
                    queue.put(Pair(nrow, ncol, time + 1))
                    fresh_orange_count -= 1
        
        if fresh_orange_count == 0:
            return time_to_rot
        else:
            return -1
