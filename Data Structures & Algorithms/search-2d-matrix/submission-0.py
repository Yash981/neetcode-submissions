class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        whichRow = -1
        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                whichRow = i
                break
        l = 0
        r = m-1
        while l <= r:
            mid = l + (r-l)//2
            if matrix[whichRow][mid] < target:
                l = mid + 1
            elif matrix[whichRow][mid] > target:
                r = mid - 1
            else:
                return True
        return False