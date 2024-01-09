class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = (rows*cols) - 1
        while low <= high:
            mid = low + (high - low)//2

            if matrix[mid//cols][mid%cols] == target:
                return True
            else:
                if matrix[mid//cols][mid%cols] > target:
                    high = mid-1
                else:
                    low = mid+1
        return False